"""Phase D: resolver, promote, compose, hydrate rank, why."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.compose import compose_view
from kedger.graph import upsert_entity
from kedger.hydrate import project_hydrate
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint
from kedger.workstream import resolve_workstream


def test_compose_constraint_escalates() -> None:
    a = {
        "id": "anc_a",
        "kind": "constraint",
        "statement": "Must use JWT",
        "status": "active",
        "provenance": {"source": "explicit"},
    }
    b = {
        "id": "anc_b",
        "kind": "constraint",
        "statement": "Must use cookies",
        "status": "active",
        "provenance": {"source": "auto_signal"},
    }
    kept, cs = compose_view([a, b])
    assert any(c["action"] == "ESCALATE" for c in cs.conflicts)
    assert len(kept) == 1


def test_resolver_explicit(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    r = resolve_workstream(store, principal=p, explicit_slug="auth-refactor")
    assert r.action == "explicit"
    assert r.workstream["slug"] == "auth-refactor"


def test_why_and_live_hydrate(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main, ["remember", "reject", "Do not use cookie sessions", "--reason", "CSRF"]
    )
    assert rem.exit_code == 0, rem.output
    anc_id = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(
        ":", 1
    )[1].strip()

    store = Store.open(repo_fingerprint())
    p = load_principal()
    ent = upsert_entity(store, entity_type="file", name="auth/session.ts")
    store.insert_edge(
        edge_type="ABOUT", from_id=anc_id, to_id=ent["id"], workstream_id=None
    )

    why = runner.invoke(main, ["why", anc_id])
    assert why.exit_code == 0, why.output
    assert anc_id in why.output
    assert "provenance" in why.output

    live = runner.invoke(main, ["hydrate", "--live", "--topic", "auth jwt"])
    assert live.exit_code == 0, live.output
    assert "Do not use cookie sessions" in live.output

    # forget then why still finds superseded via scoped get? superseded active_only
    assert runner.invoke(main, ["forget", anc_id]).exit_code == 0
    why2 = runner.invoke(main, ["why", anc_id])
    # superseded still readable to principal with workstream cap
    assert why2.exit_code == 0, why2.output


def test_promote_conservative(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.ensure_workstream(
        slug="default", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.insert_promotion_candidate(
        {
            "id": "anc_01HPROMOTE000000000000001",
            "workstream_id": ws["id"],
            "tier": "A",
            "kind": "decision",
            "statement": "Prefer refresh-token rotation",
            "status": "candidate",
            "heat": 6,
            "recurrence": 1,
            "created_at": "2026-08-08T18:00:00Z",
            "shareable": False,
        }
    )
    prom = runner.invoke(main, ["promote", "--mode", "conservative"])
    assert prom.exit_code == 0, prom.output
    assert "promoted: 1" in prom.output
    shared = runner.invoke(main, ["anchors", "--shared"])
    assert shared.output.strip() == "(none)"


def test_project_hydrate_inv_scope(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    from kedger.acl import InvScopeError
    import pytest

    with pytest.raises(InvScopeError):
        project_hydrate(
            store, principal_id="pr_stranger", workstream_id="ws_missing"
        )
