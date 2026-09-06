"""Shared fixtures — isolate KEDGER_HOME and cwd per test."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from click.testing import CliRunner

_LOCAL_BIN = Path.home() / ".local" / "bin"
if _LOCAL_BIN.is_dir():
    _path = os.environ.get("PATH", "")
    if str(_LOCAL_BIN) not in _path.split(os.pathsep):
        os.environ["PATH"] = f"{_LOCAL_BIN}{os.pathsep}{_path}"


@pytest.fixture()
def kedger_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    home = tmp_path / "kedger-home"
    home.mkdir()
    work = tmp_path / "work"
    work.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(home))
    monkeypatch.chdir(work)
    # Default tests use file/env key paths; keyring tests opt in via fake_keyring.
    monkeypatch.setattr("kedger.store.encryption._keyring_usable", lambda: False)
    return home


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()
