"""Adaptive Chameleon / Knowledge Conflicts — dual Evidence must surface ConflictSet."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.compose import compose_view
from kedger.hydrate import project_hydrate
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_dual_decision_compose_escalates() -> None:
    a = {
        "id": "anc_left",
        "kind": "decision",
        "statement": "Deploy target is us-east-1",
        "status": "active",
        "provenance": {"source": "explicit"},
    }
    b = {
        "id": "anc_right",
        "kind": "decision",
        "statement": "Deploy target is eu-west-1",
        "status": "active",
        "provenance": {"source": "explicit"},
    }
    kept, cs = compose_view([a, b])
    assert any(c["action"] == "ESCALATE" for c in cs.conflicts)
    assert any(c["type"] == "contradiction" for c in cs.conflicts)
    # Projection keeps one view; conflict records both ids (distinct-view coverage)
    assert len(kept) == 1
    ids = {c["left_id"] for c in cs.conflicts} | {c["right_id"] for c in cs.conflicts}
    assert "anc_left" in ids and "anc_right" in ids


def test_hydrate_surfaces_dual_evidence_conflicts(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
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
    ws = store.get_workstream_by_slug("default")
    proj = project_hydrate(
        store, principal_id=p.principal_id, workstream_id=ws["id"]
    )
    assert proj.conflicts, "dual contradictory decisions must emit ConflictSet"
    assert any(c.get("action") == "ESCALATE" for c in proj.conflicts)

    live = runner.invoke(main, ["hydrate", "--live"])
    assert live.exit_code == 0, live.output
    assert "conflicts:" in live.output
    assert "contradiction" in live.output or "ESCALATE" in live.output


def test_false_premise_abstain_unknown_anchor(
    kedger_env: Path, runner: CliRunner
) -> None:
    """CRAG-style false premise: why must not invent an answer for missing id."""
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    why = runner.invoke(main, ["why", "anc_false_premise_00000000000001"])
    assert why.exit_code != 0
    assert "Redis" not in why.output
    assert "JWT" not in why.output
