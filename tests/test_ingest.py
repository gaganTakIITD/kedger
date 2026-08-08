from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.store import Store, repo_fingerprint


def test_ingest_from_hook_stdin(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    payload = {
        "type": "user_prompt",
        "session_id": "sess_test",
        "summary": "Reject cookie sessions; use JWT",
        "agent_tool": "cursor",
        "importance": 0.8,
    }
    result = runner.invoke(
        main,
        ["ingest", "--from-hook"],
        input=json.dumps(payload),
    )
    assert result.exit_code == 0, result.output
    assert "type:    user_prompt" in result.output
    assert "Reject cookie sessions" in result.output

    store = Store.open(repo_fingerprint())
    assert store.counts()["observations"] == 1
