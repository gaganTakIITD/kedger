"""Dual-path Evidence + Anchors packing under byte quotas (LeanMem / LightMem).

Anchors carry policy (survive under tight budgets). Evidence carries fidelity
snippets that support selected Anchors — packed under a separate byte/item
quota and dropped before Anchors when over budget.
"""

from __future__ import annotations

import json
import re
from typing import Any

from kedger.constants import (
    HANDOFF_EVIDENCE_BUDGET_BYTES,
    HANDOFF_EVIDENCE_MAX_ITEMS,
    HANDOFF_MAX_BYTES,
)
from kedger.store.db import Store

_TOKEN_RE = re.compile(r"[a-z0-9_]{3,}")


def _tokens(text: str) -> set[str]:
    return set(_TOKEN_RE.findall((text or "").lower()))


def slim_evidence(ev: dict[str, Any]) -> dict[str, Any]:
    """Pack-facing Evidence row (no full record_json bloat)."""
    return {
        "id": ev.get("id"),
        "supports_anchor_id": ev.get("supports_anchor_id"),
        "snippet": ev.get("snippet") or "",
        "source_ref": ev.get("source_ref") or "",
        "weight": float(ev.get("weight") or 1.0),
    }


def score_evidence(
    ev: dict[str, Any],
    *,
    topic_terms: set[str],
    selected_anchor_ids: set[str],
) -> float:
    aid = ev.get("supports_anchor_id")
    if aid not in selected_anchor_ids:
        return -1.0
    snip = (ev.get("snippet") or "").lower()
    rel = 0.0
    if topic_terms:
        hits = sum(1 for t in topic_terms if t in snip)
        rel = hits / max(1, len(topic_terms))
    return float(ev.get("weight") or 1.0) + 2.0 * rel


def select_evidence_dual_path(
    store: Store,
    *,
    anchor_ids: list[str],
    topic: str | None = None,
    working: dict[str, Any] | None = None,
    max_bytes: int = HANDOFF_EVIDENCE_BUDGET_BYTES,
    max_items: int = HANDOFF_EVIDENCE_MAX_ITEMS,
) -> list[dict[str, Any]]:
    """Pick Evidence snippets for selected Anchors under byte/item quotas."""
    if not anchor_ids or max_bytes <= 0 or max_items <= 0:
        return []
    topic_terms: set[str] = set()
    if topic:
        topic_terms |= _tokens(topic)
    if working:
        topic_terms |= _tokens(str(working.get("goal") or ""))
        topic_terms |= _tokens(str(working.get("last_user_ask") or ""))
        for f in working.get("files_in_flight") or []:
            topic_terms |= _tokens(str(f).split("/")[-1].split(".")[0])

    selected_ids = set(anchor_ids)
    rows = store.list_evidence_for_anchors(list(selected_ids))
    ranked = sorted(
        rows,
        key=lambda e: -score_evidence(
            e, topic_terms=topic_terms, selected_anchor_ids=selected_ids
        ),
    )
    out: list[dict[str, Any]] = []
    used = 0
    for ev in ranked:
        if score_evidence(
            ev, topic_terms=topic_terms, selected_anchor_ids=selected_ids
        ) < 0:
            continue
        slim = slim_evidence(ev)
        raw = json.dumps(slim, sort_keys=True, separators=(",", ":")).encode("utf-8")
        if used + len(raw) > max_bytes and out:
            continue
        if len(out) >= max_items:
            break
        out.append(slim)
        used += len(raw)
    return out


def evidence_budget_for(max_bytes: int = HANDOFF_MAX_BYTES) -> int:
    """Evidence reserve scales down under tight caps; Anchors keep the rest."""
    if max_bytes <= 2048:
        return 0
    # Cap at configured budget; never exceed ~25% of pack
    return min(HANDOFF_EVIDENCE_BUDGET_BYTES, max(0, max_bytes // 4))
