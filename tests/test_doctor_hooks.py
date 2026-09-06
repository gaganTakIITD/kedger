from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from kedger.cli.main import main
from kedger.doctor.checks import diagnose_ide_hooks


def test_doctor_warns_session_start_only_cursor(tmp_path: Path) -> None:
    cursor = tmp_path / ".cursor"
    cursor.mkdir()
    cfg = {
        "hooks": {
            "sessionStart": [
                {"command": "./hooks/cursor/kedger-hook.sh sessionStart"}
            ]
        }
    }
    (cursor / "hooks.json").write_text(json.dumps(cfg), encoding="utf-8")
    (tmp_path / "hooks" / "cursor").mkdir(parents=True)
    (tmp_path / "hooks" / "cursor" / "kedger-hook.sh").write_text(
        "#!/bin/sh\n", encoding="utf-8"
    )
    warns = diagnose_ide_hooks(tmp_path)
    assert any("beforeSubmitPrompt" in w for w in warns)


def test_doctor_warns_claude_unmerged_hooks(tmp_path: Path) -> None:
    claude = tmp_path / ".claude"
    claude.mkdir()
    (claude / "kedger.hooks.json").write_text('{"hooks":{}}', encoding="utf-8")
    (tmp_path / "hooks" / "claude_code").mkdir(parents=True)
    (tmp_path / "hooks" / "claude_code" / "kedger-hook.sh").write_text(
        "#!/bin/sh\n", encoding="utf-8"
    )
    warns = diagnose_ide_hooks(tmp_path)
    assert any("kedger.hooks.json" in w for w in warns)


def test_doctor_warns_missing_mcp_when_hooks_present(tmp_path: Path) -> None:
    cursor = tmp_path / ".cursor"
    cursor.mkdir()
    cfg = {
        "hooks": {
            "sessionStart": [
                {"command": "./hooks/cursor/kedger-hook.sh sessionStart"}
            ],
            "beforeSubmitPrompt": [
                {"command": "./hooks/cursor/kedger-hook.sh beforeSubmitPrompt"}
            ],
        }
    }
    (cursor / "hooks.json").write_text(json.dumps(cfg), encoding="utf-8")
    hooks_dir = tmp_path / "hooks" / "cursor"
    hooks_dir.mkdir(parents=True)
    (hooks_dir / "kedger-hook.sh").write_text("#!/bin/sh\n", encoding="utf-8")
    warns = diagnose_ide_hooks(tmp_path)
    assert any("Cursor MCP" in w and "mcp.json" in w for w in warns)
