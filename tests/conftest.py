"""Shared fixtures — isolate KEDGER_HOME and cwd per test."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from click.testing import CliRunner


@pytest.fixture()
def kedger_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    home = tmp_path / "kedger-home"
    home.mkdir()
    work = tmp_path / "work"
    work.mkdir()
    monkeypatch.setenv("KEDGER_HOME", str(home))
    monkeypatch.chdir(work)
    # Ensure no ambient git remote affects fingerprint unless tests create one
    return home


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()
