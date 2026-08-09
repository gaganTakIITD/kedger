"""Strict handoff quality benchmark — real gates, not soft smoke.

Rules (CI-enforced):
1. Every probe is binary pass/fail with a fixed check — no vibes.
2. Baselines compared on the same session tape:
     none | transcript_tail | kedger_dual | kedger_dual_archive
3. kedger_dual must beat `none` on every non-empty policy/ops case.
4. Empty sessions must abstain (no invented constraints/rejections).
5. Transcript zlib archive must roundtrip exactly and transfer across seal.
6. Compression must shrink repetitive long tapes (zip analogy).

After failures: fix capture/compose/handoff code — do not weaken gates.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify import cognify_workstream
from kedger.handoff.compile import seal_handoff
from kedger.handoff.transcript import (
    compress_transcript,
    decompress_transcript,
    resolve_transcript_archive,
)
from kedger.hooks.runner import run_hook
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint
from kedger.store.paths import project_dir


# ---------------------------------------------------------------------------
# Cases + probes
# ---------------------------------------------------------------------------


@dataclass
class Probe:
    id: str
    kind: str  # policy | ops | abstain | transfer | baseline_win
    description: str
    # tokens that must appear in the scored surface for this baseline
    must_include: list[str] = field(default_factory=list)
    # tokens that must NOT appear (abstain / anti-hallucination)
    must_exclude: list[str] = field(default_factory=list)
    # which baseline surfaces are evaluated (default: kedger_dual)
    baselines: list[str] = field(default_factory=lambda: ["kedger_dual"])
    # for ops: require activity file path substrings / min lines
    require_files: list[str] = field(default_factory=list)
    min_lines_added: int = 0
    # for transfer: require exact summary substrings in decompressed tape
    transfer_must_include: list[str] = field(default_factory=list)


@dataclass
class BenchCase:
    id: str
    title: str
    empty: bool
    turns: list[dict[str, Any]]
    probes: list[Probe]


CASES: list[BenchCase] = [
    BenchCase(
        id="B01",
        title="Policy-heavy payments — constraints/rejections must survive",
        empty=False,
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "checkout double charges on stripe timeout. "
                    "must send Idempotency-Key on every charge create. "
                    "never auto-ack unverified webhooks. "
                    "do not flip billing_v2. leave rate-limit alone."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Constraint: must send Idempotency-Key on every charge create. "
                    "Rejection: never auto-ack unverified webhooks. "
                    "Rejection: do not flip billing_v2. "
                    "Decision: keep existing Stripe client. "
                    "Next: patch charges.py then webhook verify."
                ),
            },
            {
                "type": "file_edit",
                "summary": "Edited src/payments/charges.py (+18/-3)",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/payments/charges.py"}
                ],
                "edit_stats": {
                    "path": "src/payments/charges.py",
                    "edits": 2,
                    "lines_added": 18,
                    "lines_removed": 3,
                },
            },
            {
                "type": "file_edit",
                "summary": "Edited src/payments/webhooks.py (+9/-1)",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/payments/webhooks.py"}
                ],
                "edit_stats": {
                    "path": "src/payments/webhooks.py",
                    "edits": 1,
                    "lines_added": 9,
                    "lines_removed": 1,
                },
            },
        ],
        probes=[
            Probe(
                id="B01.policy_idempotency",
                kind="policy",
                description="Idempotency constraint present in dual handoff",
                must_include=["idempotency"],
            ),
            Probe(
                id="B01.policy_no_billing_flag",
                kind="policy",
                description="billing_v2 rejection survives",
                must_include=["billing"],
            ),
            Probe(
                id="B01.ops_files",
                kind="ops",
                description="Both payment files + line deltas in activity",
                require_files=["charges.py", "webhooks.py"],
                min_lines_added=20,
            ),
            Probe(
                id="B01.dual_beats_none",
                kind="baseline_win",
                description="kedger_dual recovers policy tokens none cannot",
                must_include=["idempotency", "billing"],
                baselines=["kedger_dual", "none"],
            ),
            Probe(
                id="B01.transfer_exact",
                kind="transfer",
                description="zlib archive restores raw turn phrases across seal",
                transfer_must_include=[
                    "Idempotency-Key",
                    "billing_v2",
                    "charges.py",
                ],
                baselines=["kedger_dual_archive"],
            ),
        ],
    ),
    BenchCase(
        id="B02",
        title="Messy unlabeled slang — capture gate still yields usable policy",
        empty=False,
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "yo rate limiter biting EU partners?? idk bump it or not. "
                    "dont touch billing. leave worker alone. fix 429 Retry-After maybe"
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "Rejection: do not touch billing. "
                    "Rejection: leave worker alone. "
                    "Open question: whether to raise EU rate limits. "
                    "Decision: add Retry-After on 429 only. "
                    "Next: patch middleware."
                ),
            },
            {
                "type": "file_edit",
                "summary": "Edited src/api/middleware/rate_limit.py (+14/-3)",
                "entity_hints": [
                    {
                        "entity_type": "file",
                        "name": "src/api/middleware/rate_limit.py",
                    }
                ],
                "edit_stats": {
                    "path": "src/api/middleware/rate_limit.py",
                    "edits": 2,
                    "lines_added": 14,
                    "lines_removed": 3,
                },
            },
        ],
        probes=[
            Probe(
                id="B02.policy_billing",
                kind="policy",
                description="dont-touch-billing survives messy user speech",
                must_include=["billing"],
            ),
            Probe(
                id="B02.policy_retry",
                kind="policy",
                description="Retry-After decision present",
                must_include=["retry"],
            ),
            Probe(
                id="B02.ops_rate_limit",
                kind="ops",
                description="rate_limit.py edits visible",
                require_files=["rate_limit.py"],
                min_lines_added=10,
            ),
            Probe(
                id="B02.dual_beats_none",
                kind="baseline_win",
                description="dual beats empty baseline on billing+retry",
                must_include=["billing", "retry"],
                baselines=["kedger_dual", "none"],
            ),
        ],
    ),
    BenchCase(
        id="B03",
        title="Ops-heavy agent-only — activity must carry continuity",
        empty=False,
        turns=[
            {"type": "user_prompt", "summary": "keep going"},
            {
                "type": "agent_response",
                "summary": "removing deprecated session cookies from auth package",
            },
            {
                "type": "file_edit",
                "summary": "Edited src/auth/cookies.py (+2/-40)",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/auth/cookies.py"}
                ],
                "edit_stats": {
                    "path": "src/auth/cookies.py",
                    "edits": 3,
                    "lines_added": 2,
                    "lines_removed": 40,
                },
            },
            {
                "type": "file_edit",
                "summary": "Edited src/auth/session.py (+11/-8)",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/auth/session.py"}
                ],
                "edit_stats": {
                    "path": "src/auth/session.py",
                    "edits": 2,
                    "lines_added": 11,
                    "lines_removed": 8,
                },
            },
            {
                "type": "tool_fail",
                "summary": "pytest tests/test_auth.py → ImportError cookies",
            },
        ],
        probes=[
            Probe(
                id="B03.ops_files",
                kind="ops",
                description="auth files present in activity",
                require_files=["cookies.py", "session.py"],
                min_lines_added=10,
            ),
            Probe(
                id="B03.ops_beats_none",
                kind="baseline_win",
                description="dual ops surface beats none on file paths",
                must_include=["cookies.py", "session.py"],
                baselines=["kedger_dual", "none"],
            ),
            Probe(
                id="B03.transfer_tool_fail",
                kind="transfer",
                description="tool_fail turn survives zlib transfer",
                transfer_must_include=["ImportError", "cookies"],
                baselines=["kedger_dual_archive"],
            ),
        ],
    ),
    BenchCase(
        id="B04",
        title="Near-empty session — must abstain from invented policy",
        empty=True,
        turns=[
            {"type": "user_prompt", "summary": "ok"},
            {"type": "agent_response", "summary": "ok"},
        ],
        probes=[
            Probe(
                id="B04.abstain_policy",
                kind="abstain",
                description="empty session must not invent payment/auth policy",
                must_exclude=[
                    "idempotency",
                    "billing_v2",
                    "stripe",
                    "jwt",
                    "must send",
                    "never auto-ack",
                ],
                baselines=["kedger_dual", "kedger_dual_archive", "transcript_tail"],
            ),
        ],
    ),
    BenchCase(
        id="B05",
        title="Unlabeled messy speech — policy + ops without Constraint: labels",
        empty=False,
        turns=[
            {
                "type": "user_prompt",
                "summary": (
                    "yo checkout double charging after timeouts. dont touch billing_v2. "
                    "gotta put idempotency key on charge creates. leave rate limit alone."
                ),
            },
            {
                "type": "agent_response",
                "summary": (
                    "ok so for now: add idempotency keys on charge create, "
                    "wont touch billing flag, leave rate limits, keep stripe client. "
                    "next ill patch charges.py"
                ),
            },
            {
                "type": "file_edit",
                "summary": "Edited src/payments/charges.py (+16/-2)",
                "entity_hints": [
                    {"entity_type": "file", "name": "src/payments/charges.py"}
                ],
                "edit_stats": {
                    "path": "src/payments/charges.py",
                    "edits": 2,
                    "lines_added": 16,
                    "lines_removed": 2,
                },
            },
        ],
        probes=[
            Probe(
                id="B05.policy_from_messy",
                kind="policy",
                description="messy unlabeled still yields idempotency/billing",
                must_include=["idempotency"],
            ),
            Probe(
                id="B05.ops_charges",
                kind="ops",
                description="charges.py line deltas present",
                require_files=["charges.py"],
                min_lines_added=10,
            ),
            Probe(
                id="B05.dual_beats_none",
                kind="baseline_win",
                description="dual beats none on messy unlabeled",
                must_include=["idempotency"],
                baselines=["kedger_dual", "none"],
            ),
            Probe(
                id="B05.transfer_messy",
                kind="transfer",
                description="zlib restores unlabeled user slang tokens",
                transfer_must_include=["billing_v2", "timeouts", "charges.py"],
                baselines=["kedger_dual_archive"],
            ),
        ],
    ),
]


# ---------------------------------------------------------------------------
# Baseline builders + scorers
# ---------------------------------------------------------------------------


def _surface_text(surface: dict[str, Any]) -> str:
    parts = [
        surface.get("inject") or "",
        " ".join(a.get("statement") or "" for a in surface.get("anchors") or []),
        surface.get("episode_summary") or "",
    ]
    for f in (surface.get("activity") or {}).get("files") or []:
        parts.append(str(f.get("path") or ""))
    for t in surface.get("turns") or []:
        parts.append(str(t.get("summary") or ""))
    return " ".join(parts).lower()


def _build_baselines(
    *,
    store: Store,
    principal: Any,
    ws_slug: str,
    ws_id: str,
    turns: list[dict[str, Any]],
    pack: dict[str, Any],
    episode: dict[str, Any] | None,
    inject: str,
) -> dict[str, dict[str, Any]]:
    """Four fixed baseline surfaces for the same tape."""
    none_surf = {
        "name": "none",
        "inject": "",
        "anchors": [],
        "activity": {},
        "episode_summary": "",
        "turns": [],
        "transcript": None,
    }
    # Naive: last N raw summaries only (no Anchors / no ops digest)
    tail = turns[-8:]
    transcript_tail = {
        "name": "transcript_tail",
        "inject": "\n".join(
            f"[{t.get('type')}] {t.get('summary')}" for t in tail
        ),
        "anchors": [],
        "activity": {},
        "episode_summary": "",
        "turns": tail,
        "transcript": None,
    }
    dual = {
        "name": "kedger_dual",
        "inject": inject,
        "anchors": pack.get("anchors") or [],
        "activity": pack.get("activity")
        or (episode or {}).get("activity")
        or {},
        "episode_summary": (episode or {}).get("summary") or "",
        "turns": [],
        "transcript": None,
    }
    packs_dir = project_dir(store.repo_fingerprint) / "packs" / ws_id
    archive = resolve_transcript_archive(pack, sidecar_root=packs_dir)
    if archive is None and episode:
        archive = episode.get("transcript")
    restored: list[dict[str, Any]] = []
    if archive and archive.get("blob_b64"):
        restored = decompress_transcript(archive)
    dual_archive = {
        "name": "kedger_dual_archive",
        "inject": inject,
        "anchors": pack.get("anchors") or [],
        "activity": dual["activity"],
        "episode_summary": dual["episode_summary"],
        "turns": restored,
        "transcript": archive,
        "transcript_meta": pack.get("transcript_meta")
        or (episode or {}).get("transcript_meta"),
    }
    return {
        "none": none_surf,
        "transcript_tail": transcript_tail,
        "kedger_dual": dual,
        "kedger_dual_archive": dual_archive,
    }


def _eval_probe(
    probe: Probe,
    baselines: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Strict binary evaluation."""
    failures: list[str] = []

    if probe.kind == "policy":
        surf = baselines["kedger_dual"]
        text = _surface_text(surf)
        for tok in probe.must_include:
            if tok.lower() not in text:
                failures.append(f"missing policy token '{tok}' in dual")
        for tok in probe.must_exclude:
            if tok.lower() in text:
                failures.append(f"unexpected token '{tok}' in dual")

    elif probe.kind == "ops":
        act = baselines["kedger_dual"].get("activity") or {}
        files = act.get("files") or []
        paths = " ".join(str(f.get("path") or "") for f in files).lower()
        inject = (baselines["kedger_dual"].get("inject") or "").lower()
        blob = paths + " " + inject
        for fp in probe.require_files:
            if fp.lower() not in blob:
                failures.append(f"missing file '{fp}' in activity/inject")
        added = int((act.get("totals") or {}).get("lines_added") or 0)
        if probe.min_lines_added and added < probe.min_lines_added:
            failures.append(
                f"lines_added {added} < required {probe.min_lines_added}"
            )

    elif probe.kind == "abstain":
        for name in probe.baselines:
            surf = baselines[name]
            text = _surface_text(surf)
            # Anchors of policy kinds are an automatic fail if any statement
            # invents excluded tokens; also scan inject/summary.
            for tok in probe.must_exclude:
                if tok.lower() in text:
                    failures.append(
                        f"abstain violated: '{tok}' present in baseline {name}"
                    )
            for a in surf.get("anchors") or []:
                kind = (a.get("kind") or "").lower()
                if kind in {"constraint", "rejection", "decision"} and (
                    a.get("statement") or ""
                ).strip():
                    # empty session must not promote policy anchors
                    stmt = (a.get("statement") or "").lower()
                    if any(tok.lower() in stmt for tok in probe.must_exclude):
                        failures.append(
                            f"abstain: policy anchor invented in {name}: {stmt[:80]}"
                        )

    elif probe.kind == "transfer":
        surf = baselines["kedger_dual_archive"]
        archive = surf.get("transcript")
        if not archive or not archive.get("blob_b64"):
            failures.append("no zlib transcript archive available after seal")
        else:
            turns = surf.get("turns") or decompress_transcript(archive)
            blob = " ".join(str(t.get("summary") or "") for t in turns)
            for tok in probe.transfer_must_include:
                if tok not in blob and tok.lower() not in blob.lower():
                    failures.append(
                        f"transfer missing '{tok}' in decompressed turns"
                    )
            # Roundtrip exactness vs re-compress of restored turns
            again = compress_transcript(turns)
            if decompress_transcript(again) != turns:
                failures.append("recompress roundtrip mismatch")

    elif probe.kind == "baseline_win":
        dual = _surface_text(baselines["kedger_dual"])
        none = _surface_text(baselines["none"])
        dual_hits = sum(1 for t in probe.must_include if t.lower() in dual)
        none_hits = sum(1 for t in probe.must_include if t.lower() in none)
        if dual_hits < len(probe.must_include):
            failures.append(
                f"dual incomplete hits {dual_hits}/{len(probe.must_include)}"
            )
        if dual_hits <= none_hits:
            failures.append(
                f"dual did not beat none ({dual_hits} vs {none_hits})"
            )

    else:
        failures.append(f"unknown probe kind {probe.kind}")

    return {
        "id": probe.id,
        "kind": probe.kind,
        "description": probe.description,
        "pass": len(failures) == 0,
        "failures": failures,
    }


def _run_case(case: BenchCase, store: Store, principal: Any) -> dict[str, Any]:
    ws = store.ensure_workstream(
        slug=f"bench-{case.id.lower()}",
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    ws_id = ws["id"]
    ingested: list[dict[str, Any]] = []
    for i, turn in enumerate(case.turns):
        rec = store.ingest_observation(
            {
                **turn,
                "session_id": f"sess_{case.id}",
                "workstream_id": ws_id,
                "agent_tool": "cursor",
                "ts": f"2026-08-09T18:{i:02d}:00Z",
            },
            principal_id=principal.principal_id,
        )
        ingested.append({**turn, "id": rec["id"], "ts": rec["ts"]})

    cog = cognify_workstream(
        store,
        principal=principal,
        workstream_slug=ws["slug"],
        force=True,
        event_type="pre_compact",
        reseal=False,
    )
    promote_candidates(
        store, principal=principal, workstream_id=ws_id, mode="conservative"
    )
    _path, pack = seal_handoff(
        store, principal=principal, workstream_slug=ws["slug"]
    )
    out = run_hook(
        store,
        principal=principal,
        payload={"type": "SessionStart", "session_id": f"next_{case.id}"},
        source="cursor",
        workstream_slug=ws["slug"],
    )
    inject = out.get("additionalContext") or ""
    baselines = _build_baselines(
        store=store,
        principal=principal,
        ws_slug=ws["slug"],
        ws_id=ws_id,
        turns=ingested,
        pack=pack,
        episode=cog.episode,
        inject=inject,
    )
    probe_results = [_eval_probe(p, baselines) for p in case.probes]
    return {
        "id": case.id,
        "title": case.title,
        "empty": case.empty,
        "layers": pack.get("layers"),
        "transcript_meta": pack.get("transcript_meta")
        or (cog.episode or {}).get("transcript_meta"),
        "anchor_count": len(pack.get("anchors") or []),
        "activity_totals": (pack.get("activity") or {}).get("totals"),
        "probes": probe_results,
        "all_pass": all(p["pass"] for p in probe_results),
    }


# ---------------------------------------------------------------------------
# Compression unit gates (zip analogy)
# ---------------------------------------------------------------------------


def test_transcript_zlib_roundtrip_and_ratio() -> None:
    """Large repetitive tape must shrink like zip and roundtrip exactly."""
    turns = []
    for i in range(400):
        turns.append(
            {
                "id": f"obs_{i}",
                "type": "agent_response" if i % 2 else "user_prompt",
                "ts": f"2026-08-09T10:00:{i % 60:02d}Z",
                "summary": (
                    "Constraint: must send Idempotency-Key on every charge create. "
                    "Rejection: never auto-ack unverified webhooks. "
                    f"turn={i} patch src/payments/charges.py keep Stripe client."
                ),
                "session_id": "sess_compress",
            }
        )
    archive = compress_transcript(turns)
    assert archive["schema"] == "kedger.transcript_archive.v1"
    assert archive["codec"] == "zlib"
    assert archive["raw_bytes"] > archive["compressed_bytes"]
    assert archive["ratio"] < 0.5  # strict: must meaningfully compress
    restored = decompress_transcript(archive)
    assert restored == turns


def test_transcript_transfer_sidecar_when_over_budget(
    kedger_env: Path, runner: CliRunner
) -> None:
    """When pack budget is tight, blob externalizes; resolve still restores turns."""
    from kedger.handoff.transcript import attach_transcript_for_pack

    assert runner.invoke(main, ["keys", "init", "--name", "side"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    # Build a fat archive
    turns = [
        {
            "id": f"t{i}",
            "type": "user_prompt",
            "ts": f"2026-08-09T11:00:{i:02d}Z",
            "summary": ("UNIQUE_TOKEN_SIDECAR_XYZ " + ("padding " * 80) + str(i)),
            "session_id": "s",
        }
        for i in range(40)
    ]
    archive = compress_transcript(turns)
    packs_dir = project_dir(store.repo_fingerprint) / "packs" / ws["id"]
    packs_dir.mkdir(parents=True, exist_ok=True)
    pack = {
        "id": "hf_test_side",
        "anchors": [],
        "working": {},
        "episode_digests": [],
        "layers": {},
        "budget": {"max_bytes": 500, "used_bytes": 0, "dropped": []},
    }
    # Force tiny budget so inline cannot fit
    out = attach_transcript_for_pack(
        archive,
        pack=pack,
        max_bytes=200,
        sidecar_dir=packs_dir,
        handoff_id="hf_test_side",
    )
    assert out["transcript"] is None
    assert out["transcript_meta"]["sidecar"]
    assert "transcript_blob" in out["budget"]["dropped"]
    resolved = resolve_transcript_archive(out, sidecar_root=packs_dir)
    assert resolved is not None
    assert decompress_transcript(resolved) == turns


# ---------------------------------------------------------------------------
# Full strict suite
# ---------------------------------------------------------------------------


def test_strict_handoff_quality_benchmark(kedger_env: Path, runner: CliRunner) -> None:
    """Run all strict probes; fail CI on any must-pass miss."""
    assert runner.invoke(main, ["keys", "init", "--name", "bench"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()

    results = [_run_case(c, store, p) for c in CASES]
    failed = [
        f"{r['id']}:{pr['id']} -> {pr['failures']}"
        for r in results
        for pr in r["probes"]
        if not pr["pass"]
    ]

    artifact = {
        "suite": "strict_handoff_quality_v1",
        "cases": results,
        "failed": failed,
        "pass": not failed,
    }
    # Persist under repo even when kedger_env chdirs into a temp workdir
    repo_root = Path(__file__).resolve().parents[2]
    out_dir = repo_root / "artifacts" / "eval"
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "handoff_quality_strict.json").write_text(
            json.dumps(artifact, indent=2, default=str)
        )
    except OSError:
        pass

    assert not failed, "strict handoff probes failed:\n" + "\n".join(failed)

    # Suite-level gates
    assert all(r["all_pass"] for r in results)
    # Non-empty cases must expose transcript layer after cognify/seal
    for r in results:
        if r["empty"]:
            continue
        meta = r.get("transcript_meta") or {}
        assert meta.get("turn_count", 0) >= 1, f"{r['id']} missing transcript meta"
        layers = r.get("layers") or {}
        assert layers.get("transcript") in {
            "inline_zlib",
            "sidecar_zlib",
            "zlib_archive",
            "meta_only",
        }, f"{r['id']} layers={layers}"
