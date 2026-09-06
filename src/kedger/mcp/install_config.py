"""Fail-soft MCP config snippets for Cursor (.cursor/mcp.json) and Claude Code (.mcp.json)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any, Literal

KEDGER_MCP_SERVER_NAME = "kedger"


def kedger_mcp_server_entry() -> dict[str, Any]:
    """Stdio MCP server entry for `kedger mcp serve`."""
    exe = shutil.which("kedger")
    command = exe if exe else "kedger"
    return {"command": command, "args": ["mcp", "serve"]}


def _mcp_servers(cfg: dict[str, Any]) -> dict[str, Any]:
    servers = cfg.get("mcpServers")
    return servers if isinstance(servers, dict) else {}


def _is_kedger_mcp_entry(entry: Any) -> bool:
    if not isinstance(entry, dict):
        return False
    args = entry.get("args") or []
    if isinstance(args, list) and any("mcp" in str(a) for a in args):
        return True
    cmd = str(entry.get("command") or "")
    return "kedger" in cmd and "mcp" in cmd


def merge_mcp_config(
    existing: dict[str, Any], kedger_entry: dict[str, Any]
) -> tuple[dict[str, Any], str]:
    """Merge Kedger MCP server into an mcp.json-shaped dict when safe."""
    merged = dict(existing)
    servers = dict(_mcp_servers(existing))
    current = servers.get(KEDGER_MCP_SERVER_NAME)
    if current is not None:
        if _is_kedger_mcp_entry(current):
            return merged, "already_present"
        return merged, "name_collision"
    servers[KEDGER_MCP_SERVER_NAME] = kedger_entry
    merged["mcpServers"] = servers
    return merged, "merged"


def _write_mcp_json(path: Path, kedger_entry: dict[str, Any]) -> tuple[str, str | None]:
    """Write or merge MCP config at path. Returns (status, warning)."""
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return "skipped_invalid", (
                f"could not parse {path.name} — left unchanged; "
                f"add Kedger MCP manually (see docs/PROMPT_INJECT_VERIFY.md)"
            )
        if not isinstance(existing, dict):
            existing = {}
        merged, status = merge_mcp_config(existing, kedger_entry)
        if status == "already_present":
            return status, None
        if status == "name_collision":
            return status, (
                f"{path.name} already defines mcpServers.{KEDGER_MCP_SERVER_NAME} "
                "with a different server — left unchanged"
            )
        path.write_text(json.dumps(merged, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return status, None

    payload = {"mcpServers": {KEDGER_MCP_SERVER_NAME: kedger_entry}}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return "created", None


Target = Literal["cursor", "claude", "both"]


def install_mcp_configs(
    *,
    target: Target = "both",
    repo_root: Path,
    install_mcp: bool = True,
) -> dict[str, Any]:
    """Optionally write Cursor/Claude MCP config snippets (fail-soft)."""
    if not install_mcp:
        return {"written": [], "notes": [], "warnings": []}

    root = repo_root.resolve()
    kedger_entry = kedger_mcp_server_entry()
    written: list[str] = []
    notes: list[str] = []
    warnings: list[str] = []

    if target in {"cursor", "both"}:
        path = root / ".cursor" / "mcp.json"
        status, warn = _write_mcp_json(path, kedger_entry)
        if status in {"created", "merged"}:
            written.append(str(path))
            notes.append(
                "Cursor MCP: wrote .cursor/mcp.json — reload window or enable in Settings > MCP"
            )
        elif status == "already_present":
            notes.append("Cursor MCP: kedger already registered in .cursor/mcp.json")
        if warn:
            warnings.append(f"Cursor MCP: {warn}")

    if target in {"claude", "both"}:
        path = root / ".mcp.json"
        status, warn = _write_mcp_json(path, kedger_entry)
        if status in {"created", "merged"}:
            written.append(str(path))
            notes.append(
                "Claude Code MCP: wrote .mcp.json — restart Claude Code or run `claude mcp list`"
            )
        elif status == "already_present":
            notes.append("Claude Code MCP: kedger already registered in .mcp.json")
        if warn:
            warnings.append(f"Claude Code MCP: {warn}")

    return {"written": written, "notes": notes, "warnings": warnings}


def has_kedger_mcp_registration(cfg_path: Path) -> bool:
    """True when cfg_path exists and registers the Kedger MCP server."""
    if not cfg_path.exists():
        return False
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    if not isinstance(cfg, dict):
        return False
    entry = _mcp_servers(cfg).get(KEDGER_MCP_SERVER_NAME)
    return _is_kedger_mcp_entry(entry)
