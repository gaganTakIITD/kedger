"""Phase A hardening: redact-before-persist, L0 pressure, WorkingState budget."""

from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.constants import WORKING_MAX_BYTES
from kedger.redact import redact_text, scan_secrets
from kedger.store import Store, repo_fingerprint


def test_redact_masks_github_token() -> None:
    text = "token ghs_abcdefghijklmnopqrstuvwx and more"
    assert "github_token" in scan_secrets(text) or "github_pat" in scan_secrets(text)
    out = redact_text(text)
    assert out.redacted
    assert "ghs_" not in out.text
    assert out.blocked_for_share


def test_ingest_redacts_and_soft_patches(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    ws = store.ensure_workstream(slug="default", principal_id="pr_test")
    payload = {
        "type": "user_prompt",
        "session_id": "sess_1",
        "workstream_id": ws["id"],
        "summary": "deploy with ghs_abcdefghijklmnopqrstuvwxyz12",
        "entity_hints": [{"entity_type": "file", "name": "auth/session.ts"}],
    }
    result = runner.invoke(main, ["ingest", "--from-hook"], input=json.dumps(payload))
    assert result.exit_code == 0, result.output
    assert "redacted: true" in result.output
    assert "ghs_" not in result.output

    store = Store.open(repo_fingerprint())
    working = store.get_working_state(ws["id"])
    assert working is not None
    assert "ghs_" not in json.dumps(working)
    assert "auth/session.ts" in (working.get("files_in_flight") or [])


def test_working_state_budget(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    store = Store.open(repo_fingerprint())
    ws = store.ensure_workstream(slug="default", principal_id="pr_test")
    record = {
        "schema_version": "kedger.memory.v1",
        "id": "wk_testbudget00000000000001",
        "workstream_id": ws["id"],
        "repo_fingerprint": store.repo_fingerprint,
        "goal": "x",
        "last_user_ask": "y" * 200,
        "files_in_flight": [f"path/to/file_{i}.ts" for i in range(80)],
        "open_questions": ["q" * 100 for _ in range(20)],
        "blockers": [],
        "active_branch": None,
        "active_anchor_ids": [],
        "updated_at": "2026-08-08T00:00:00Z",
        "updated_by_session_id": "t",
        "visibility": "workstream_private",
    }
    saved = store.upsert_working_state(record)
    raw = json.dumps(saved, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert len(raw) <= WORKING_MAX_BYTES


def test_repo_policy_written(kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch) -> None:
    import subprocess

    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    monkeypatch.chdir(repo)
    monkeypatch.setenv("KEDGER_HOME", str(kedger_env))
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    assert (
        runner.invoke(main, ["remember", "decision", "Use JWT"]).exit_code == 0
    )
    assert (repo / ".kedger" / "project.json").exists()
    assert (repo / ".kedger" / ".gitignore").exists()
