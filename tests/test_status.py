from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main


def test_status_lists_active_anchors(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "constraint", "JWT only for session auth", "--reason", "policy"],
    )
    assert rem.exit_code == 0, rem.output

    status = runner.invoke(main, ["status", "--list"])
    assert status.exit_code == 0, status.output
    assert "repo_fingerprint:  rf_" in status.output
    assert "kedger_home:" in status.output
    assert "active=1" in status.output
    assert "JWT only for session auth" in status.output
    assert "[constraint]" in status.output
