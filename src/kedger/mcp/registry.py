"""MCP tool registry — minimal read tools for agent pull fallback."""

from __future__ import annotations

import json
from typing import Any, Callable

from kedger.acl import InvScopeError
from kedger.hydrate import project_hydrate
from kedger.keys.principal import Principal
from kedger.store.db import Store
from kedger.workstream import resolve_workstream

ToolHandler = Callable[[Store, Principal, dict[str, Any]], dict[str, Any]]


def _tool_hydrate(store: Store, principal: Principal, args: dict[str, Any]) -> dict[str, Any]:
    workstream = str(args.get("workstream") or "default")
    resolved = resolve_workstream(store, principal=principal, explicit_slug=workstream)
    if resolved.workstream is None:
        return {"error": "not found", "code": 404}
    try:
        proj = project_hydrate(
            store,
            principal_id=principal.principal_id,
            workstream_id=resolved.workstream["id"],
            topic=args.get("topic"),
        )
    except InvScopeError:
        return {"error": "not found", "code": 404}
    return {
        "workstream_id": resolved.workstream["id"],
        "anchors": [
            {"id": a["id"], "kind": a["kind"], "statement": a["statement"]}
            for a in proj.anchors
        ],
        "conflicts": proj.conflicts,
        "used_bytes": proj.used_bytes,
        "working": proj.working,
    }


def _tool_anchors_get(
    store: Store, principal: Principal, args: dict[str, Any]
) -> dict[str, Any]:
    anchor_id = args.get("anchor_id") or args.get("id")
    if not anchor_id:
        return {"error": "anchor_id required", "code": 400}
    try:
        anc = store.get_anchor_scoped(str(anchor_id), principal_id=principal.principal_id)
    except KeyError:
        return {"error": "not found", "code": 404}
    return {"anchor": anc}


TOOL_SPECS: list[dict[str, Any]] = [
    {
        "name": "hydrate",
        "description": "Authorized ranked hydrate projection for a workstream.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "workstream": {"type": "string", "description": "Workstream slug"},
                "topic": {"type": "string", "description": "Optional topic hint"},
            },
        },
    },
    {
        "name": "anchors_get",
        "description": "GET one Anchor by id with Inv-Scope enforcement (404 when denied).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "anchor_id": {"type": "string", "description": "Anchor id"},
            },
            "required": ["anchor_id"],
        },
    },
]

TOOL_HANDLERS: dict[str, ToolHandler] = {
    "hydrate": _tool_hydrate,
    "anchors_get": _tool_anchors_get,
}


def call_tool(
    name: str,
    args: dict[str, Any],
    *,
    store: Store,
    principal: Principal,
) -> dict[str, Any]:
    handler = TOOL_HANDLERS.get(name)
    if handler is None:
        return {"error": f"unknown tool: {name}", "code": 404}
    if not isinstance(args, dict):
        return {"error": "arguments must be an object", "code": 400}
    return handler(store, principal, args)


def mcp_text_result(payload: dict[str, Any]) -> dict[str, Any]:
    """Shape tool output for MCP tools/call."""
    if payload.get("code") == 404:
        return {
            "content": [{"type": "text", "text": "not found"}],
            "isError": True,
        }
    if payload.get("error"):
        return {
            "content": [{"type": "text", "text": str(payload["error"])}],
            "isError": True,
        }
    return {
        "content": [{"type": "text", "text": json.dumps(payload, indent=2, sort_keys=True)}],
        "isError": False,
    }
