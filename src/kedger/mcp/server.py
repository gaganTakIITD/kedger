"""Minimal MCP stdio server (JSON-RPC 2.0, Content-Length framing)."""

from __future__ import annotations

import json
import sys
from typing import Any

from kedger.keys import KeysError, load_principal
from kedger.mcp.registry import TOOL_SPECS, call_tool, mcp_text_result
from kedger.store import Store, repo_fingerprint

PROTOCOL_VERSION = "2024-11-05"
SERVER_INFO = {"name": "kedger", "version": "0.2.4"}


def _read_message() -> dict[str, Any] | None:
    """Read one MCP-framed JSON-RPC message from stdin."""
    headers: dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        decoded = line.decode("utf-8", errors="replace").strip()
        if not decoded:
            break
        if ":" in decoded:
            key, value = decoded.split(":", 1)
            headers[key.strip().lower()] = value.strip()
    length = int(headers.get("content-length", "0"))
    if length <= 0:
        return None
    body = sys.stdin.buffer.read(length)
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def _write_message(payload: dict[str, Any]) -> None:
    data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(data)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()


def _respond(req_id: Any, result: dict[str, Any]) -> None:
    _write_message({"jsonrpc": "2.0", "id": req_id, "result": result})


def _respond_error(req_id: Any, code: int, message: str) -> None:
    _write_message(
        {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": code, "message": message},
        }
    )


def handle_request(
    msg: dict[str, Any],
    *,
    store: Store,
    principal: Any,
) -> None:
    req_id = msg.get("id")
    method = msg.get("method")
    params = msg.get("params") or {}

    if method == "initialize":
        _respond(
            req_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            },
        )
        return

    if method == "notifications/initialized":
        return

    if method == "tools/list":
        _respond(req_id, {"tools": TOOL_SPECS})
        return

    if method == "tools/call":
        name = (params.get("name") or "").strip()
        arguments = params.get("arguments") or {}
        payload = call_tool(name, arguments, store=store, principal=principal)
        _respond(req_id, mcp_text_result(payload))
        return

    if req_id is not None:
        _respond_error(req_id, -32601, f"Method not found: {method}")


def serve() -> None:
    try:
        principal = load_principal()
    except KeysError as e:
        print(f"error: {e}", file=sys.stderr)
        raise SystemExit(1) from e
    store = Store.open(repo_fingerprint())
    while True:
        msg = _read_message()
        if msg is None:
            break
        handle_request(msg, store=store, principal=principal)
