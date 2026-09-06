from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

from kedger.doctor.checks import diagnose_cli_path


def test_diagnose_cli_path_warns_when_scripts_missing_from_path() -> None:
    scripts_root = Path("/fake/python/Scripts")
    with patch.object(sys, "platform", "win32"), patch(
        "shutil.which", return_value=None
    ), patch(
        "sysconfig.get_path", return_value=str(scripts_root)
    ), patch.object(
        Path,
        "exists",
        lambda self: self.name in {"kedger.exe", "Scripts"},
    ), patch.object(
        Path,
        "glob",
        lambda self, pattern: [self / "kedger.exe"]
        if self == scripts_root
        else [],
    ):
        warnings = diagnose_cli_path()
    assert len(warnings) == 1
    assert "not on PATH" in warnings[0]
    assert "Scripts" in warnings[0]


def test_diagnose_cli_path_silent_when_kedger_on_path() -> None:
    with patch.object(sys, "platform", "win32"), patch(
        "shutil.which", return_value="/usr/bin/kedger"
    ):
        assert diagnose_cli_path() == []


def test_diagnose_cli_path_silent_on_non_windows() -> None:
    with patch.object(sys, "platform", "linux"):
        assert diagnose_cli_path() == []
