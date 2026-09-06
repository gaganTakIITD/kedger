"""Tests for fail-soft MCP config install."""

from __future__ import annotations

import json
from pathlib import Path

from kedger.hooks.install_packs import install_hook_packs
from kedger.mcp.install_config import (
    KEDGER_MCP_SERVER_NAME,
    has_kedger_mcp_registration,
    install_mcp_configs,
    kedger_mcp_server_entry,
    merge_mcp_config,
)


def test_kedger_mcp_server_entry_shape() -> None:
    entry = kedger_mcp_server_entry()
    assert entry["args"] == ["mcp", "serve"]
    assert entry["command"]


def test_merge_mcp_config_adds_kedger() -> None:
    merged, status = merge_mcp_config({}, kedger_mcp_server_entry())
    assert status == "merged"
    assert KEDGER_MCP_SERVER_NAME in merged["mcpServers"]


def test_merge_mcp_config_skips_collision() -> None:
    existing = {"mcpServers": {KEDGER_MCP_SERVER_NAME: {"command": "other", "args": []}}}
    merged, status = merge_mcp_config(existing, kedger_mcp_server_entry())
    assert status == "name_collision"
    assert merged["mcpServers"][KEDGER_MCP_SERVER_NAME]["command"] == "other"


def test_install_mcp_configs_cursor_and_claude(tmp_path: Path) -> None:
    result = install_mcp_configs(target="both", repo_root=tmp_path)
    cursor_cfg = tmp_path / ".cursor" / "mcp.json"
    claude_cfg = tmp_path / ".mcp.json"
    assert cursor_cfg.is_file()
    assert claude_cfg.is_file()
    assert has_kedger_mcp_registration(cursor_cfg)
    assert has_kedger_mcp_registration(claude_cfg)
    assert len(result["written"]) == 2


def test_install_hook_packs_writes_mcp_json(tmp_path: Path) -> None:
    foreign = tmp_path / "app"
    foreign.mkdir()
    result = install_hook_packs(target="cursor", repo_root=foreign)
    mcp_path = foreign / ".cursor" / "mcp.json"
    assert mcp_path.is_file()
    cfg = json.loads(mcp_path.read_text(encoding="utf-8"))
    assert cfg["mcpServers"][KEDGER_MCP_SERVER_NAME]["args"] == ["mcp", "serve"]
    assert any("MCP" in n for n in result.get("notes") or [])


def test_install_mcp_skips_invalid_existing(tmp_path: Path) -> None:
    cursor_dir = tmp_path / ".cursor"
    cursor_dir.mkdir()
    bad = cursor_dir / "mcp.json"
    bad.write_text("{not json", encoding="utf-8")
    result = install_mcp_configs(target="cursor", repo_root=tmp_path)
    assert bad.read_text(encoding="utf-8") == "{not json"
    assert any("could not parse" in w for w in result.get("warnings") or [])
