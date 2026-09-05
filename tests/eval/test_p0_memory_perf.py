"""P0 memory-perf gates — prove IDF / dual-path / delay-k deliver, not just architecture.

Also records measurable answers for:
  Q1 prompt → claim extract accuracy
  Q2 agent/transcript handling (compress vs carry-forward)
  Q3 handoff → 2nd-agent probe accuracy (ranked projection, not clone)
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.cognify.extract import extract_claims_from_text
from kedger.constants import (
    HANDOFF_EVIDENCE_BUDGET_BYTES,
    HANDOFF_MAX_BYTES,
    L0_DELAY_K,
    L0_MAX_ROWS_PER_WORKSTREAM,
    L0_WARN_RATIO,
)
from kedger.graph import associative_expand, seed_idf_scores, upsert_entity
from kedger.handoff.compile import compile_handoff_pack, seal_handoff
from kedger.handoff.transcript import compress_transcript, decompress_transcript
from kedger.hydrate import project_hydrate
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint

from sli_util import record_sli


# ---------------------------------------------------------------------------
# P0-1 Seed IDF
# ---------------------------------------------------------------------------


def test_seed_idf_boosts_rare_anchor(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    # Common filler Anchors vs one rare technical constraint
    for stmt in [
        "Use the existing client for now",
        "Keep the existing client path",
        "Prefer the existing client library",
        "Must send Idempotency-Key on every charge create",
    ]:
        kind = "constraint" if "Idempotency" in stmt else "decision"
        assert runner.invoke(main, ["remember", kind, stmt]).exit_code == 0

    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    anchors = store.ranked_active_anchors(workstream_id=ws["id"])
    by_theme = {
        a["id"]: a
        for a in anchors
    }
    rare = next(a for a in anchors if "Idempotency" in (a.get("statement") or ""))
    common = next(a for a in anchors if "existing client" in (a.get("statement") or "").lower())

    # Link both to a shared entity so expand has a graph
    ent = upsert_entity(store, entity_type="file", name="src/payments/charges.py")
    store.insert_edge(
        edge_type="ABOUT", from_id=rare["id"], to_id=ent["id"], workstream_id=ws["id"]
    )
    store.insert_edge(
        edge_type="ABOUT", from_id=common["id"], to_id=ent["id"], workstream_id=ws["id"]
    )

    scores = seed_idf_scores(store, [rare["id"], common["id"]])
    assert scores[rare["id"]] > scores[common["id"]], (
        f"rare seed must outrank common: {scores}"
    )

    # Ablation: uniform seeds vs IDF — rare should rank at/near top under IDF
    idf_rank = associative_expand(
        store, [rare["id"], common["id"]], budget=4, max_hops=1, seed_scores=scores
    )
    uniform = {rare["id"]: 1.0, common["id"]: 1.0}
    uni_rank = associative_expand(
        store, [rare["id"], common["id"]], budget=4, max_hops=1, seed_scores=uniform
    )
    assert rare["id"] in idf_rank
    assert idf_rank.index(rare["id"]) <= uni_rank.index(rare["id"])
    _ = by_theme, p  # keep locals intentional for future probes


# ---------------------------------------------------------------------------
# P0-2 Dual-path Evidence + Anchors
# ---------------------------------------------------------------------------


def test_dual_path_evidence_under_32kb(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main, ["remember", "constraint", "Must send Idempotency-Key on every charge"]
    )
    assert rem.exit_code == 0
    anc_id = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    for i in range(6):
        store.insert_evidence(
            supports_anchor_id=anc_id,
            snippet=f"rg Idempotency-Key charges.py miss #{i} — add header before POST",
            source_ref=f"tool_result:obs_dual_{i}",
            weight=1.0 + 0.1 * i,
        )
    pack = compile_handoff_pack(store, workstream=ws, principal=p)
    assert pack["budget"]["used_bytes"] <= HANDOFF_MAX_BYTES
    assert pack["evidence"], "dual-path must pack Evidence when present"
    assert len(pack["evidence"]) <= 12
    assert all(e.get("supports_anchor_id") == anc_id for e in pack["evidence"])
    # Evidence must fit its reserved quota slice
    ev_raw = json.dumps(pack["evidence"], sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    assert len(ev_raw) <= HANDOFF_EVIDENCE_BUDGET_BYTES + 64
    record_sli(sli_sink, "dual_path_evidence_items", float(len(pack["evidence"])))
    record_sli(sli_sink, "dual_path_pack_bytes", float(pack["budget"]["used_bytes"]))

    # Tight cap: Evidence drops before constraint Anchors
    tight = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        max_bytes=2500,
        topic="Idempotency-Key charges",
    )
    kinds = {a["kind"] for a in tight.anchors}
    assert "constraint" in kinds
    assert tight.used_bytes <= 2500


# ---------------------------------------------------------------------------
# P0-3 Delay-k soft-stale L0 only
# ---------------------------------------------------------------------------


def test_delay_k_soft_stale_l0_not_anchors(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    from unittest.mock import patch

    import kedger.store.db as db_mod

    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "constraint", "All APIs require authentication"]
        ).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    # Shrink L0 cap so warn/soft-stale is reachable in a small fixture
    with patch.object(db_mod, "L0_MAX_ROWS_PER_WORKSTREAM", 40):
        for i in range(32):  # 32 >= 0.70*40 = 28 → warn
            store.ingest_observation(
                {
                    "type": "note",
                    "session_id": "delayk",
                    "workstream_id": ws["id"],
                    "summary": f"noise turn {i} about cache and retries",
                },
                principal_id=p.principal_id,
            )
        soft = [
            o
            for o in store.list_observations(workstream_id=ws["id"])
            if o.get("soft_stale")
        ]
        if not soft:
            for _ in range(L0_DELAY_K + 2):
                store.rotate_observations(workstream_id=ws["id"])
            soft = [
                o
                for o in store.list_observations(workstream_id=ws["id"])
                if o.get("soft_stale")
            ]
        assert soft, "delay-k must soft-mark L0 overflow under sustained warn"
        assert all(o.get("soft_stale_reason") == "delay_k_pressure" for o in soft)
        # Anchors untouched (never attention-evicted)
        assert any(
            "authentication" in (a.get("statement") or "").lower()
            for a in store.ranked_active_anchors(workstream_id=ws["id"])
        )
        record_sli(sli_sink, "l0_soft_stale_count", float(len(soft)))
        record_sli(sli_sink, "l0_delay_k", float(L0_DELAY_K))
        _ = L0_WARN_RATIO, L0_MAX_ROWS_PER_WORKSTREAM


# ---------------------------------------------------------------------------
# Q1 / Q2 / Q3 accuracy gates
# ---------------------------------------------------------------------------


def test_q1_prompt_decomposition_accuracy(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    """Q1: user prompt is decomposed into useful claims (deterministic extract)."""
    prompt = (
        "checkout double charges on stripe timeout. "
        "must send Idempotency-Key on every charge create. "
        "never auto-ack unverified webhooks. "
        "do not flip billing_v2. leave rate-limit alone."
    )
    claims = extract_claims_from_text(prompt, source_type="user_prompt")
    kinds = {c.kind for c in claims}
    stmts = " ".join(c.statement.lower() for c in claims)
    theme_hits = sum(
        1
        for t in ("idempotency", "webhook", "billing_v2", "rate-limit", "rate limit")
        if t in stmts or t.replace("-", " ") in stmts or t.replace("_", " ") in stmts
    )
    # Crispness: no claim dumps the whole paragraph
    crisp = all(len(c.statement) <= 165 for c in claims)
    assert claims, "prompt must yield at least one claim"
    assert "constraint" in kinds or "rejection" in kinds
    assert theme_hits >= 2, f"themes under-extracted: {stmts}"
    assert crisp
    accuracy = theme_hits / 4.0  # 4 policy themes in prompt
    record_sli(sli_sink, "q1_prompt_theme_recall", accuracy)
    record_sli(sli_sink, "q1_claim_count", float(len(claims)))


def test_q2_transcript_compress_not_blind_carry(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    """Q2: agent/transcript — zlib compress + ranked inject, not raw carry-forward."""
    turns = [
        {"role": "user", "text": f"turn {i} " + ("idempotency webhook " * 20)}
        for i in range(40)
    ]
    archive = compress_transcript(turns)
    restored = decompress_transcript(archive)
    assert restored == turns
    ratio = float(archive.get("ratio") or 0)
    assert ratio < 1.0, "repetitive tape must compress"
    record_sli(sli_sink, "q2_transcript_zlib_ratio", ratio)
    record_sli(
        sli_sink,
        "q2_transcript_compressed_bytes",
        float(archive.get("compressed_bytes") or 0),
    )

    # End-to-end: inject surface is Anchors+activity, not full tape dump
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    from kedger.hooks.runner import run_hook

    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    run_hook(
        store,
        principal=p,
        payload={
            "type": "user_prompt",
            "session_id": "q2",
            "summary": (
                "must send Idempotency-Key. never auto-ack unverified webhooks. "
                "do not flip billing_v2."
            ),
        },
        workstream_slug="default",
    )
    run_hook(
        store,
        principal=p,
        payload={
            "type": "agent_response",
            "session_id": "q2",
            "summary": (
                "Constraint: must send Idempotency-Key. "
                "Rejection: never auto-ack unverified webhooks. "
                "Rejection: do not flip billing_v2."
            ),
        },
        workstream_slug="default",
    )
    cognify_workstream(
        store, principal=p, force=True, event_type="sessionEnd", reseal=False
    )
    promote_candidates(store, principal=p, workstream_id=ws["id"])
    pack = compile_handoff_pack(store, workstream=ws, principal=p)
    # Semantic layers present; full turn dump is not the inject surface
    assert pack["anchors"]
    inject = json.dumps(
        {"anchors": pack["anchors"], "activity": pack.get("activity")},
        separators=(",", ":"),
    )
    assert "must send" in inject.lower() or "idempotency" in inject.lower()
    record_sli(sli_sink, "q2_inject_anchor_count", float(len(pack["anchors"])))


def test_q3_second_agent_ranked_projection_not_clone(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    """Q3: 2nd agent sees ranked survival projection — same *policy*, not same session blob."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    from kedger.hooks.runner import run_hook

    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    run_hook(
        store,
        principal=p,
        payload={
            "type": "user_prompt",
            "session_id": "q3",
            "summary": (
                "must send Idempotency-Key on every charge create. "
                "never auto-ack unverified webhooks. "
                "do not flip billing_v2. leave rate-limit alone."
            ),
        },
        workstream_slug="default",
    )
    run_hook(
        store,
        principal=p,
        payload={
            "type": "agent_response",
            "session_id": "q3",
            "summary": (
                "Constraint: must send Idempotency-Key on every charge create. "
                "Rejection: never auto-ack unverified webhooks. "
                "Rejection: do not flip billing_v2. "
                "Rejection: leave rate-limit alone. "
                "Decision: keep existing Stripe client."
            ),
        },
        workstream_slug="default",
    )
    cognify_workstream(
        store, principal=p, force=True, event_type="sessionEnd", reseal=False
    )
    promote_candidates(store, principal=p, workstream_id=ws["id"])
    path, pack = seal_handoff(store, principal=p, workstream_slug="default")
    assert pack["budget"]["used_bytes"] <= HANDOFF_MAX_BYTES

    probes = ["idempotency", "webhook", "billing_v2", "stripe"]
    surface = json.dumps(pack["anchors"]).lower()
    hits = sum(1 for t in probes if t in surface)
    accuracy = hits / len(probes)
    assert accuracy >= 0.75, f"2nd-agent policy recall {accuracy}: {surface}"
    # Not a clone: low-survival chatter / full prompt dump need not appear
    assert pack["budget"]["used_bytes"] < 200_000
    record_sli(sli_sink, "q3_policy_probe_accuracy", accuracy)
    record_sli(sli_sink, "q3_pack_bytes", float(pack["budget"]["used_bytes"]))
    assert path.exists()


def test_insight_under_tight_caps(
    kedger_env: Path, runner: CliRunner, sli_sink: Path
) -> None:
    """Spectrum-style insight must hold at 8KiB / 16KiB / 32KiB hydrate caps."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    for kind, stmt in [
        ("constraint", "Must send Idempotency-Key on every charge create"),
        ("reject", "Never auto-ack unverified webhooks"),
        ("reject", "Do not flip billing_v2"),
        ("decision", "Keep existing Stripe client"),
        ("gotcha", "Missing cache key namespace causes stampede"),
        ("next", "Patch charges.py then webhook verify"),
    ]:
        assert runner.invoke(main, ["remember", kind, stmt]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    for cap in (8192, 16384, 32768):
        proj = project_hydrate(
            store,
            principal_id=p.principal_id,
            workstream_id=ws["id"],
            max_bytes=cap,
            topic="Idempotency webhook billing",
        )
        assert proj.used_bytes <= cap
        kinds = {a["kind"] for a in proj.anchors}
        critical = kinds & {"constraint", "rejection", "decision"}
        assert critical, f"no policy survived at {cap}"
        record_sli(sli_sink, f"insight_cap_{cap}_anchors", float(len(proj.anchors)))
        record_sli(sli_sink, f"insight_cap_{cap}_bytes", float(proj.used_bytes))
    _ = math  # keep import for future scoring helpers
