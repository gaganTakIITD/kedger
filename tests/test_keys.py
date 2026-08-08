from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.keys import load_principal


def test_keys_init_and_show(kedger_env: Path, runner: CliRunner) -> None:
    result = runner.invoke(main, ["keys", "init", "--name", "ci"])
    assert result.exit_code == 0, result.output
    assert "principal_id: pr_" in result.output
    assert "public_key:" in result.output

    principal = load_principal()
    assert principal.name == "ci"
    assert principal.signing_key is not None
    assert (kedger_env / "keys" / "principal.json").exists()
    assert (kedger_env / "keys" / "principal.ed25519").exists()

    # second init without force fails
    again = runner.invoke(main, ["keys", "init", "--name", "ci"])
    assert again.exit_code != 0
    assert "already exists" in again.output

    show = runner.invoke(main, ["keys", "show"])
    assert show.exit_code == 0, show.output
    assert principal.principal_id in show.output
    assert principal.public_key_b64 in show.output
