"""Close-memory-gaps gates — faithfulness, consolidate, surface, inject, recurrence."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.cognify.extract import _clean_statement, extract_claims_from_text
from kedger.compose.similarity import near_duplicate
from kedger.consolidate import consolidate_workstream
from kedger.constants import (
    RECURRENCE_PROMOTE_THETA,
    VISIBLE_SURFACE_K,
)
from kedger.hooks.runner import run_hook
from kedger.hydrate import project_hydrate
from kedger.keys import load_principal
from kedger.promote import promote_candidates
from kedger.store import Store, repo_fingerprint


def test_faithfulness_idempotency_key_survives_extract() -> None:
    text = (
        "must send Idempotency-Key on every charge create. "
        "never auto-ack unverified webhooks."
    )
    claims = extract_claims_from_text(text, source_type="user_prompt")
    blob = " ".join(c.statement for c in claims)
    assert "Idempotency-Key" in blob or "idempotency-key" in blob.lower()
    assert "create-Key" not in blob
    assert _clean_statement(
        "must send Idempotency-Key on every charge create"
    ).count("on every charge create") == 1


def test_consolidate_near_dup_decisions(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "decision", "Use Redis for session store caching"]
        ).exit_code
        == 0
    )
    assert (
        runner.invoke(
            main,
            ["remember", "decision", "Use Redis for session store caching layer"],
        ).exit_code
        == 0
    )
    assert (
        runner.invoke(
            main, ["remember", "constraint", "All APIs require authentication"]
        ).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    before = [
        a
        for a in store.ranked_active_anchors(workstream_id=ws["id"])
        if a["kind"] == "decision"
    ]
    assert len(before) >= 2
    assert near_duplicate(before[0]["statement"], before[1]["statement"])

    dry = consolidate_workstream(
        store, principal=p, workstream_id=ws["id"], dry_run=True
    )
    assert dry.actions
    assert dry.merged == 0
    assert len(store.ranked_active_anchors(workstream_id=ws["id"])) >= 3

    res = consolidate_workstream(
        store, principal=p, workstream_id=ws["id"], dry_run=False
    )
    assert res.merged >= 1
    decisions = [
        a
        for a in store.ranked_active_anchors(workstream_id=ws["id"])
        if a["kind"] == "decision"
    ]
    assert len(decisions) == 1
    assert any(
        "authentication" in (a.get("statement") or "").lower()
        for a in store.ranked_active_anchors(workstream_id=ws["id"])
    )
    assert store.counts().get("supersedes_edges", 0) >= 1

    cli = runner.invoke(main, ["consolidate", "--dry-run"])
    assert cli.exit_code == 0, cli.output


def test_consolidate_does_not_merge_escalating_conflicts(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "decision", "Deploy target is us-east-1"]
        ).exit_code
        == 0
    )
    assert (
        runner.invoke(
            main, ["remember", "decision", "Deploy target is eu-west-1"]
        ).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    res = consolidate_workstream(
        store, principal=p, workstream_id=ws["id"], dry_run=False
    )
    active = store.ranked_active_anchors(workstream_id=ws["id"])
    assert len(active) == 2, "contradictory decisions must not merge"
    assert res.merged == 0


def test_visible_surface_k_caps_seeds(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    for i in range(12):
        kind = "gotcha" if i > 6 else "decision"
        assert (
            runner.invoke(
                main, ["remember", kind, f"Policy item number {i} about module_{i}"]
            ).exit_code
            == 0
        )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    proj = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        surface_k=VISIBLE_SURFACE_K,
        walk_budget=8,
    )
    assert len(proj.seed_ids) <= VISIBLE_SURFACE_K
    assert proj.surface_k == VISIBLE_SURFACE_K
    tight = project_hydrate(
        store,
        principal_id=p.principal_id,
        workstream_id=ws["id"],
        surface_k=2,
        walk_budget=4,
    )
    assert len(tight.seed_ids) <= 2
    cli = runner.invoke(main, ["hydrate", "--live", "--surface-k", "3"])
    assert cli.exit_code == 0, cli.output
    assert "surface_k:    3" in cli.output


def test_inject_includes_evidence_and_conflicts(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main, ["remember", "constraint", "Must send Idempotency-Key on every charge"]
    )
    assert rem.exit_code == 0
    anc_id = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()
    assert (
        runner.invoke(
            main, ["remember", "decision", "Use Redis for session store"]
        ).exit_code
        == 0
    )
    assert (
        runner.invoke(
            main, ["remember", "decision", "Use JWT bearer tokens for sessions"]
        ).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    store.insert_evidence(
        supports_anchor_id=anc_id,
        snippet="rg Idempotency-Key charges.py → 0 hits on POST",
        source_ref="tool_result:obs_ev1",
        weight=1.2,
    )
    out = run_hook(
        store,
        principal=p,
        payload={"type": "SessionStart", "session_id": "inject_gap"},
        source="cursor",
        workstream_slug="default",
    )
    ctx = out.get("additionalContext") or ""
    assert "Idempotency" in ctx or "idempotency" in ctx.lower()
    assert "Evidence" in ctx
    assert "rg Idempotency-Key" in ctx or "charges.py" in ctx
    assert "conflicts:" in ctx
    assert "ESCALATE" in ctx or "contradiction" in ctx


def test_recurrence_theta_promotes_on_normal_mode(
    kedger_env: Path, runner: CliRunner
) -> None:
    """C7 complete: θ=3 under mode=normal → Anchor; shareable stays false."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    stmt = "Do not silently retry flaky payment tests in CI"
    for i in range(RECURRENCE_PROMOTE_THETA):
        store.insert_promotion_candidate(
            {
                "schema_version": "kedger.memory.v1",
                "id": f"cand_rec_{i}",
                "tier": "B",
                "kind": "gotcha",
                "statement": stmt,
                "status": "candidate",
                "heat": 1.0,
                "recurrence": RECURRENCE_PROMOTE_THETA if i == 0 else 1,
                "workstream_id": ws["id"],
                "created_at": f"2026-08-09T0{i}:00:00Z",
                "shareable": False,
                "source_type": "note",
            }
        )
    # Conservative must not auto-promote Tier B note gotchas
    cons = promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="conservative"
    )
    assert cons == []
    # Normal + recurrence ≥ θ
    # Reset first candidate if conservative left it — still candidate
    promoted = promote_candidates(
        store, principal=p, workstream_id=ws["id"], mode="normal"
    )
    assert promoted, "θ recurrence under normal must promote"
    assert all(a.get("shareable") is False for a in promoted)
    assert any(stmt.lower()[:20] in (a.get("statement") or "").lower() for a in promoted)

    # CLI path
    store.insert_promotion_candidate(
        {
            "schema_version": "kedger.memory.v1",
            "id": "cand_rec_cli",
            "tier": "B",
            "kind": "gotcha",
            "statement": "Watch out for missing cache key namespace stampede",
            "status": "candidate",
            "heat": 5.0,
            "recurrence": 1,
            "workstream_id": ws["id"],
            "created_at": "2026-08-09T10:00:00Z",
            "shareable": False,
            "source_type": "note",
        }
    )
    cli = runner.invoke(main, ["promote", "--mode", "normal"])
    assert cli.exit_code == 0, cli.output
    assert "promoted:" in cli.output
