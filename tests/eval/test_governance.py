"""Governance fixtures — no-relitigation, supersession, L0 vs Anchors, Inv-Scope, isolation."""

from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.constants import WORKING_MAX_BYTES
from kedger.keys import load_principal
from kedger.store import Store, repo_fingerprint


def test_no_relitigation_rejection_survives_hydrate(
    kedger_env: Path, runner: CliRunner
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "reject", "Do not use cookie sessions", "--reason", "CSRF"],
    )
    assert rem.exit_code == 0
    hyd = runner.invoke(main, ["hydrate", "--live"])
    assert hyd.exit_code == 0
    assert "cookie" in hyd.output.lower()
    # Subsequent cognify must not drop the rejection
    assert runner.invoke(main, ["cognify", "--force"]).exit_code == 0
    hyd2 = runner.invoke(main, ["hydrate", "--live"])
    assert "cookie" in hyd2.output.lower()


def test_supersession_chain_integrity(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "decision", "Use session cookies"])
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    assert runner.invoke(main, ["forget", anc]).exit_code == 0
    rem2 = runner.invoke(main, ["remember", "decision", "Use JWT only"])
    assert rem2.exit_code == 0
    store = Store.open(repo_fingerprint())
    old = store.get_anchor(anc)
    assert old["status"] == "superseded"
    assert old["superseded_by"]
    why = runner.invoke(main, ["why", anc])
    assert why.exit_code == 0
    assert "superseded" in why.output.lower() or "SUPERSEDES" in why.output


def test_l0_rotation_preserves_anchors(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(
            main, ["remember", "constraint", "TLS required on all endpoints"]
        ).exit_code
        == 0
    )
    store = Store.open(repo_fingerprint())
    p = load_principal()
    ws = store.get_workstream_by_slug("default")
    assert ws
    # Flood L0 then rotate
    for i in range(120):
        store.ingest_observation(
            {
                "type": "note",
                "session_id": "flood",
                "workstream_id": ws["id"],
                "summary": f"noise event {i} " + ("x" * 40),
            },
            principal_id=p.principal_id,
        )
    store.rotate_observations(workstream_id=ws["id"])
    store = Store.open(repo_fingerprint())
    active = store.ranked_active_anchors(workstream_id=ws["id"])
    assert any("TLS required" in (a.get("statement") or "") for a in active)


def test_parallel_workstream_isolation(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    p = load_principal()
    a = store.ensure_workstream(
        slug="auth", principal_id=p.principal_id, signing_key=p.signing_key
    )
    b = store.ensure_workstream(
        slug="billing", principal_id=p.principal_id, signing_key=p.signing_key
    )
    store.remember(
        "decision",
        "Auth uses JWT",
        principal_id=p.principal_id,
        workstream_id=a["id"],
    )
    # Billing hydrate must not see auth-only anchor via live project on billing ws
    from kedger.hydrate import project_hydrate

    proj = project_hydrate(
        store, principal_id=p.principal_id, workstream_id=b["id"]
    )
    assert not any("JWT" in (x.get("statement") or "") for x in proj.anchors)


def test_inv_scope_why_unauthorized(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch
) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "alice"]).exit_code == 0
    rem = runner.invoke(main, ["remember", "gotcha", "Secret internal gotcha"])
    anc = [ln for ln in rem.output.splitlines() if ln.startswith("id:")][0].split(":", 1)[
        1
    ].strip()
    bob = tmp_path / "bob"
    bob.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(bob))
    assert runner.invoke(main, ["keys", "init", "--name", "bob"]).exit_code == 0
    why = runner.invoke(main, ["why", anc])
    # Inv-Scope: deny looks like not found
    assert why.exit_code != 0 or "not found" in why.output.lower()
    assert "Secret internal gotcha" not in why.output


def test_working_state_budget_ceiling(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    ws = store.ensure_workstream(slug="default", principal_id="pr_test")
    record = {
        "schema_version": "kedger.memory.v1",
        "id": "wk_evalbudget000000000000001",
        "workstream_id": ws["id"],
        "repo_fingerprint": store.repo_fingerprint,
        "goal": "g" * 200,
        "last_user_ask": "y" * 400,
        "files_in_flight": [f"path/to/file_{i}.ts" for i in range(80)],
        "open_questions": ["q" * 80 for _ in range(30)],
        "blockers": ["b" * 80 for _ in range(10)],
        "active_branch": None,
        "active_anchor_ids": [],
        "updated_at": "2026-08-08T00:00:00Z",
        "updated_by_session_id": "t",
        "visibility": "workstream_private",
    }
    saved = store.upsert_working_state(record)
    raw = json.dumps(saved, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert len(raw) <= WORKING_MAX_BYTES
