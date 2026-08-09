"""Launch surface: kedger init + hooks install into a foreign repo."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from click.testing import CliRunner

from kedger import __version__
from kedger.cli.main import main
from kedger.hooks.install_packs import hook_packs_root, install_hook_packs
from kedger.keys import load_principal
from kedger.store.paths import keys_dir


def test_version_is_launch_surface() -> None:
    assert __version__ == "0.1.1"


def test_hook_packs_root_resolves() -> None:
    root = hook_packs_root()
    assert (root / "cursor" / "hooks.json").is_file()
    assert (root / "claude_code" / "settings.hooks.json").is_file()


def test_install_hook_packs_into_foreign_repo(tmp_path: Path) -> None:
    foreign = tmp_path / "app"
    foreign.mkdir()
    subprocess.run(["git", "init"], cwd=foreign, check=True, capture_output=True)

    result = install_hook_packs(target="both", repo_root=foreign)
    assert Path(result["repo_root"]) == foreign.resolve()
    assert (foreign / ".cursor" / "hooks.json").is_file()
    assert (foreign / "hooks" / "cursor" / "kedger-hook.sh").is_file()
    assert (foreign / "hooks" / "claude_code" / "kedger-hook.sh").is_file()
    assert (foreign / ".claude" / "settings.json").is_file()
    hooks = json.loads((foreign / ".cursor" / "hooks.json").read_text(encoding="utf-8"))
    assert hooks  # non-empty IDE config


def test_hooks_install_cli_foreign_repo(
    kedger_env: Path, runner: CliRunner, tmp_path: Path
) -> None:
    foreign = tmp_path / "other"
    foreign.mkdir()
    res = runner.invoke(
        main,
        ["hooks", "install", "--target", "cursor", "--repo", str(foreign)],
    )
    assert res.exit_code == 0, res.output
    assert (foreign / ".cursor" / "hooks.json").is_file()
    assert (foreign / "hooks" / "cursor" / "kedger-hook.sh").is_file()
    assert not (foreign / ".claude").exists()


def test_init_keys_policy_hooks_none(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch
) -> None:
    work = tmp_path / "proj"
    work.mkdir()
    monkeypatch.chdir(work)
    # Isolate from the Kedger checkout git root
    subprocess.run(["git", "init"], cwd=work, check=True, capture_output=True)

    res = runner.invoke(main, ["init", "--name", "launch", "--hooks", "none"])
    assert res.exit_code == 0, res.output
    assert "principal:" in res.output
    assert "hooks:        skipped" in res.output
    principal = load_principal()
    assert principal.name == "launch" or principal.principal_id
    assert keys_dir().exists()
    assert (work / ".kedger").is_dir()
    assert not (work / ".cursor").exists()


def test_init_with_hooks_into_cwd(
    kedger_env: Path, runner: CliRunner, tmp_path: Path, monkeypatch
) -> None:
    work = tmp_path / "withhooks"
    work.mkdir()
    monkeypatch.chdir(work)
    subprocess.run(["git", "init"], cwd=work, check=True, capture_output=True)

    res = runner.invoke(main, ["init", "--name", "hooky", "--hooks", "both"])
    assert res.exit_code == 0, res.output
    assert (work / ".cursor" / "hooks.json").is_file()
    assert (work / ".claude" / "settings.json").is_file()
