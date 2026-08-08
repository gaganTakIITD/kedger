"""Workstream identity resolver — never silent merge (WORKSTREAM_AND_PROMOTION_V1)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from kedger.constants import WS_AMBIGUOUS_GAP, WS_CREATE_THRESHOLD, WS_JOIN_THRESHOLD
from kedger.ids import new_id
from kedger.keys.principal import Principal
from kedger.store.db import Store


@dataclass
class ResolveResult:
    workstream: dict[str, Any] | None
    action: str  # join | create | ambiguous | explicit
    score: float
    candidates: list[tuple[float, dict[str, Any]]]


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (s or "workstream")[:48]


def resolve_workstream(
    store: Store,
    *,
    principal: Principal,
    explicit_slug: str | None = None,
    branch: str | None = None,
    files_in_focus: list[str] | None = None,
    goal_text: str | None = None,
    create_if_missing: bool = True,
) -> ResolveResult:
    if explicit_slug:
        ws = store.ensure_workstream(
            slug=explicit_slug,
            principal_id=principal.principal_id,
            signing_key=principal.signing_key,
        )
        return ResolveResult(workstream=ws, action="explicit", score=99.0, candidates=[])

    # Score existing workstreams
    with store.connection() as conn:
        rows = conn.execute("SELECT record_json FROM workstreams").fetchall()
    scored: list[tuple[float, dict[str, Any]]] = []
    files = set(files_in_focus or [])
    for row in rows:
        import json

        ws = json.loads(row["record_json"])
        score = 0.0
        branches = set(ws.get("primary_branches") or [])
        if branch and branch in branches:
            score += 3.0
        # file Jaccard vs working state
        working = store.get_working_state(ws["id"])
        ws_files = set((working or {}).get("files_in_flight") or [])
        if files and ws_files:
            j = len(files & ws_files) / max(1, len(files | ws_files))
            score += 2.0 * j
        # handoff HEAD
        with store.connection() as conn:
            head = conn.execute(
                "SELECT id FROM handoffs WHERE workstream_id = ? AND superseded = 0 LIMIT 1",
                (ws["id"],),
            ).fetchone()
        if head:
            score += 1.5
        if goal_text and goal_text.lower() in (ws.get("name") or "").lower():
            score += 1.0
        if principal.principal_id in (ws.get("member_principal_ids") or []):
            score += 0.5
        scored.append((score, ws))

    scored.sort(key=lambda x: -x[0])
    if not scored:
        if not create_if_missing:
            return ResolveResult(None, "ambiguous", 0.0, [])
        slug = _slugify(goal_text or branch or "default")
        ws = store.ensure_workstream(
            slug=slug,
            name=goal_text or slug,
            principal_id=principal.principal_id,
            signing_key=principal.signing_key,
        )
        if branch:
            _add_branch(store, ws, branch)
        return ResolveResult(ws, "create", 0.0, [])

    best_score, best = scored[0]
    second = scored[1][0] if len(scored) > 1 else -1.0
    if best_score >= WS_JOIN_THRESHOLD and (best_score - second) >= WS_AMBIGUOUS_GAP:
        return ResolveResult(best, "join", best_score, scored[:3])
    if best_score < WS_CREATE_THRESHOLD and create_if_missing:
        slug = _slugify(goal_text or branch or new_id("ws")[3:10])
        ws = store.ensure_workstream(
            slug=slug,
            name=goal_text or slug,
            principal_id=principal.principal_id,
            signing_key=principal.signing_key,
        )
        if branch:
            _add_branch(store, ws, branch)
        return ResolveResult(ws, "create", best_score, scored[:3])
    # Ambiguous — do not silent merge
    return ResolveResult(None, "ambiguous", best_score, scored[:3])


def _add_branch(store: Store, ws: dict[str, Any], branch: str) -> None:
    import json

    from kedger.store.db import utc_now

    branches = list(ws.get("primary_branches") or [])
    if branch not in branches:
        branches.append(branch)
        ws["primary_branches"] = branches
        ws["updated_at"] = utc_now()
        with store.connection() as conn:
            conn.execute(
                "UPDATE workstreams SET record_json = ?, updated_at = ? WHERE id = ?",
                (json.dumps(ws), ws["updated_at"], ws["id"]),
            )
