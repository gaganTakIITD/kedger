"""Map Cursor/Claude hook payloads → ObservationType + side effects."""

from __future__ import annotations

from typing import Any

# Minimum 8 events (PARALLEL_COMPOSE_AND_HOOKS_V1)
# Keys are lowercased with hyphens/spaces stripped (underscores kept).
EVENT_MAP = {
    # SESSION_START
    "sessionstart": "session_start",
    "session_start": "session_start",
    # USER_PROMPT — Claude UserPromptSubmit / Cursor beforeSubmitPrompt
    "userpromptsubmit": "user_prompt",
    "user_prompt": "user_prompt",
    "beforesubmitprompt": "user_prompt",
    "before_submit_prompt": "user_prompt",
    "prompt": "user_prompt",
    # AGENT_RESPONSE — Cursor afterAgentResponse / Claude Stop last message
    "agent_response": "agent_response",
    "afteragentresponse": "agent_response",
    "after_agent_response": "agent_response",
    "assistant": "agent_response",
    # FILE_EDIT — Cursor afterFileEdit (Claude PostToolUse handled below by tool_name)
    "afterfileedit": "file_edit",
    "after_file_edit": "file_edit",
    "file_edit": "file_edit",
    "edit": "file_edit",
    # TOOL_FAIL — Cursor postToolUseFailure / Claude PostToolUseFailure
    "posttoolusefailure": "tool_fail",
    "post_tool_use_failure": "tool_fail",
    "posttooluse_failure": "tool_fail",
    "tool_fail": "tool_fail",
    "tool_error": "tool_fail",

    # TURN_STOP
    "stop": "stop",
    "turn_stop": "stop",
    # PRE_COMPACT
    "precompact": "pre_compact",
    "pre_compact": "pre_compact",
    # SESSION_END
    "sessionend": "session_end",
    "session_end": "session_end",
}

HARD_COGNIFY = frozenset({"pre_compact", "session_end"})
HYDRATE_INJECT = frozenset({"session_start"})


def normalize_hook_event(payload: dict[str, Any], *, source: str = "generic") -> dict[str, Any]:
    """Return normalized observation + side_effects list."""
    raw_type = (
        payload.get("type")
        or payload.get("event")
        or payload.get("hook_event_name")
        or payload.get("name")
        or "note"
    )
    key = str(raw_type).lower().replace("-", "_").replace(" ", "")
    # also try without underscores collapsed
    obs_type = EVENT_MAP.get(key) or EVENT_MAP.get(str(raw_type).lower())
    if obs_type is None and key in {"posttooluse", "post_tool_use"}:
        # Claude PostToolUse: only Edit/Write → file_edit (matcher should filter too)
        tool = str(payload.get("tool_name") or payload.get("tool") or "").lower()
        if tool in {"edit", "write", "multiedit", "notebookedit"}:
            obs_type = "file_edit"
        else:
            obs_type = "note"
    if obs_type is None:
        obs_type = "note"

    summary = (
        payload.get("summary")
        or payload.get("prompt")
        or payload.get("text")
        or payload.get("message")
        or payload.get("content")
        or json_preview(payload)
    )
    files = []
    for key_name in ("file_path", "path", "file"):
        if payload.get(key_name):
            files.append(str(payload[key_name]))
    for f in payload.get("files") or []:
        files.append(str(f))

    side_effects: list[str] = ["ingest"]
    if obs_type in HYDRATE_INJECT:
        side_effects = ["hydrate_inject", "ingest"]
    if obs_type in HARD_COGNIFY:
        side_effects = ["ingest", "cognify_hard"]
    if obs_type == "stop":
        side_effects = ["ingest", "boundary_soft"]

    entity_hints = [
        {"entity_type": "file", "name": f} for f in files if f
    ]

    return {
        "observation": {
            "type": obs_type,
            "summary": str(summary)[:500],
            "session_id": payload.get("session_id") or payload.get("conversation_id") or "hook",
            "agent_tool": "cursor" if source == "cursor" else ("claude_code" if source == "claude_code" else "other"),
            "entity_hints": entity_hints,
            "workstream_id": payload.get("workstream_id"),
            "importance": float(payload.get("importance", 0.55)),
            "visibility": "private_raw",
        },
        "side_effects": side_effects,
        "source": source,
        "raw_type": raw_type,
    }


def json_preview(payload: dict[str, Any]) -> str:
    import json

    return json.dumps(payload, sort_keys=True)[:200]
