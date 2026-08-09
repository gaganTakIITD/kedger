"""Operational agent-activity layer — compact-native ops digest for handoff.

Dual-layer handoff:
  BASE     — L3 Anchors (judgments from user + agent text)
  ACTIVITY — what the agent did (files, edits, line deltas, tool fails)

Activity must survive preCompact even when the chat window is compacted away.
"""

from __future__ import annotations

import re
from typing import Any

from kedger.constants import FILES_IN_FLIGHT_MAX

_EDIT_RE = re.compile(
    r"(?i)edited\s+(\S+).*?(?:\((\+|plus)\s*(\d+)\s*/\s*(?:-|minus)\s*(\d+)\)|"
    r"\+(\d+)/-(\d+))"
)
_EDIT_PATH_RE = re.compile(r"(?i)edited\s+(\S+)")


def line_delta(old: str | None, new: str | None) -> tuple[int, int]:
    """Approximate lines added/removed from old→new text (hook payloads)."""
    old_lines = (old or "").splitlines()
    new_lines = (new or "").splitlines()
    # Cheap set-diff approximation — good enough for activity budgets
    old_set = set(old_lines)
    new_set = set(new_lines)
    added = max(0, len(new_lines) - len(old_set & new_set))
    removed = max(0, len(old_lines) - len(old_set & new_set))
    if not old_lines and new_lines:
        added = len(new_lines)
        removed = 0
    if old_lines and not new_lines:
        added = 0
        removed = len(old_lines)
    # Prefer count delta when strings are wholesale replacements
    if abs(len(new_lines) - len(old_lines)) > max(added, removed):
        if len(new_lines) >= len(old_lines):
            return len(new_lines) - len(old_lines), 0
        return 0, len(old_lines) - len(new_lines)
    return added, removed


def edit_stats_from_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Pull path + line deltas from Cursor/Claude file-edit hook shapes."""
    path = (
        payload.get("file_path")
        or payload.get("path")
        or payload.get("file")
        or ""
    )
    if not path:
        files = payload.get("files") or []
        if files:
            path = str(files[0])
    added = int(payload.get("lines_added") or payload.get("additions") or 0)
    removed = int(payload.get("lines_removed") or payload.get("deletions") or 0)

    edits = payload.get("edits") or payload.get("diff_edits") or []
    if isinstance(edits, list) and edits and (added == 0 and removed == 0):
        for e in edits:
            if not isinstance(e, dict):
                continue
            a, r = line_delta(e.get("old_string") or e.get("old"), e.get("new_string") or e.get("new"))
            added += a
            removed += r
            if not path and e.get("path"):
                path = str(e["path"])

    if added == 0 and removed == 0:
        old = payload.get("old_string") or payload.get("before")
        new = payload.get("new_string") or payload.get("after") or payload.get("content")
        if isinstance(old, str) or isinstance(new, str):
            added, removed = line_delta(
                old if isinstance(old, str) else None,
                new if isinstance(new, str) else None,
            )

    n_edits = int(payload.get("edit_count") or 0) or (
        len(edits) if isinstance(edits, list) and edits else (1 if path else 0)
    )
    return {
        "path": str(path) if path else "",
        "edits": n_edits,
        "lines_added": max(0, added),
        "lines_removed": max(0, removed),
    }


def summarize_file_edit(stats: dict[str, Any]) -> str:
    path = stats.get("path") or "unknown"
    a = int(stats.get("lines_added") or 0)
    r = int(stats.get("lines_removed") or 0)
    return f"Edited {path} (+{a}/-{r})"


def _file_entry(path: str) -> dict[str, Any]:
    return {
        "path": path,
        "edits": 0,
        "lines_added": 0,
        "lines_removed": 0,
    }


def merge_file_stat(
    files: dict[str, dict[str, Any]], stats: dict[str, Any]
) -> None:
    path = (stats.get("path") or "").strip()
    if not path:
        return
    ent = files.setdefault(path, _file_entry(path))
    ent["edits"] += int(stats.get("edits") or 1)
    ent["lines_added"] += int(stats.get("lines_added") or 0)
    ent["lines_removed"] += int(stats.get("lines_removed") or 0)


def parse_edit_summary(summary: str) -> dict[str, Any] | None:
    """Recover stats from an already-rendered 'Edited path (+a/-r)' summary."""
    m = _EDIT_RE.search(summary or "")
    if m:
        path = m.group(1).rstrip("—-")
        a = int(m.group(3) or m.group(5) or 0)
        r = int(m.group(4) or m.group(6) or 0)
        return {"path": path, "edits": 1, "lines_added": a, "lines_removed": r}
    m2 = _EDIT_PATH_RE.search(summary or "")
    if m2:
        return {
            "path": m2.group(1).rstrip("—-"),
            "edits": 1,
            "lines_added": 0,
            "lines_removed": 0,
        }
    return None


def compile_activity(span: list[dict[str, Any]]) -> dict[str, Any]:
    """Build compact operational digest from an L0 observation span."""
    files: dict[str, dict[str, Any]] = {}
    agent_turns = 0
    tool_results = 0
    tool_fails = 0
    user_turns = 0
    actions: list[str] = []

    for obs in span:
        otype = obs.get("type") or ""
        summary = (obs.get("summary") or "").strip()
        if otype == "user_prompt":
            user_turns += 1
        elif otype == "agent_response":
            agent_turns += 1
            if summary:
                actions.append(summary[:160])
        elif otype == "tool_result":
            tool_results += 1
            if summary:
                actions.append(f"tool: {summary[:140]}")
        elif otype == "tool_fail":
            tool_fails += 1
            if summary:
                actions.append(f"tool_fail: {summary[:120]}")
        elif otype == "file_edit":
            stats = None
            # Prefer structured payload if still present on the observation
            payload = obs.get("payload") or {}
            if isinstance(payload, dict) and (
                payload.get("file_path")
                or payload.get("path")
                or payload.get("lines_added") is not None
                or payload.get("edits")
            ):
                stats = edit_stats_from_payload(payload)
            if stats is None:
                stats = parse_edit_summary(summary)
            if stats is None:
                for h in obs.get("entity_hints") or []:
                    if isinstance(h, dict) and h.get("entity_type") == "file" and h.get("name"):
                        stats = {
                            "path": h["name"],
                            "edits": 1,
                            "lines_added": 0,
                            "lines_removed": 0,
                        }
                        break
            if stats:
                merge_file_stat(files, stats)
                actions.append(summarize_file_edit(stats))

        # Entity hints on any turn still count as touched files
        for h in obs.get("entity_hints") or []:
            if isinstance(h, dict) and h.get("entity_type") == "file" and h.get("name"):
                path = str(h["name"])
                if path not in files:
                    files[path] = _file_entry(path)

    file_list = sorted(
        files.values(),
        key=lambda f: (-(f["edits"]), -(f["lines_added"] + f["lines_removed"]), f["path"]),
    )[:FILES_IN_FLIGHT_MAX]

    totals = {
        "files": len(file_list),
        "edits": sum(f["edits"] for f in file_list),
        "lines_added": sum(f["lines_added"] for f in file_list),
        "lines_removed": sum(f["lines_removed"] for f in file_list),
        "agent_turns": agent_turns,
        "user_turns": user_turns,
        "tool_results": tool_results,
        "tool_fails": tool_fails,
    }
    return {
        "schema": "kedger.activity.v1",
        "layer": "activity",
        "totals": totals,
        "files": file_list,
        "recent_actions": actions[-12:],
    }


def activity_inject_lines(activity: dict[str, Any] | None) -> list[str]:
    """Render ops layer for sessionStart hydrate inject."""
    if not activity:
        return []
    totals = activity.get("totals") or {}
    lines = [
        "",
        "# Agent activity (ops layer — survives compact)",
        (
            f"- turns: user={totals.get('user_turns', 0)} agent={totals.get('agent_turns', 0)} "
            f"tools={totals.get('tool_results', 0)} fails={totals.get('tool_fails', 0)}"
        ),
        (
            f"- edits: {totals.get('files', 0)} files, {totals.get('edits', 0)} edits, "
            f"+{totals.get('lines_added', 0)}/-{totals.get('lines_removed', 0)} lines"
        ),
    ]
    for f in (activity.get("files") or [])[:8]:
        lines.append(
            f"  - {f.get('path')}  edits={f.get('edits', 0)} "
            f"(+{f.get('lines_added', 0)}/-{f.get('lines_removed', 0)})"
        )
    return lines


def patch_working_activity(
    working: dict[str, Any], activity: dict[str, Any]
) -> dict[str, Any]:
    """Merge activity into L1 working cursor (budget-trimmed elsewhere)."""
    out = dict(working)
    out["activity"] = activity
    # Keep files_in_flight aligned with activity paths
    paths = [f["path"] for f in (activity.get("files") or []) if f.get("path")]
    if paths:
        merged = list(dict.fromkeys((out.get("files_in_flight") or []) + paths))
        out["files_in_flight"] = merged[:FILES_IN_FLIGHT_MAX]
    return out
