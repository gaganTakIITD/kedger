from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main


def test_doctor_passes_after_init(kedger_env: Path, runner: CliRunner) -> None:
    assert runner.invoke(main, ["keys", "init", "--name", "ci"]).exit_code == 0
    rem = runner.invoke(
        main,
        ["remember", "decision", "Use JWT refresh tokens"],
    )
    assert rem.exit_code == 0, rem.output

    doc = runner.invoke(main, ["doctor"])
    assert doc.exit_code == 0, doc.output
    assert "[ok] principal:" in doc.output
    assert "[ok] store:" in doc.output
    assert "Kedger≠MoDeX" in doc.output
    assert "doctor: all checks passed" in doc.output
