"""Segment continuity score for soft boundaries (SeCom / MemoryOS θ)."""

from __future__ import annotations

from typing import Any


def _files_from_obs(obs: dict[str, Any]) -> set[str]:
    out: set[str] = set()
    for h in obs.get("entity_hints") or []:
        if isinstance(h, dict) and h.get("entity_type") == "file" and h.get("name"):
            out.add(str(h["name"]).lower())
    return out


def segment_continuity_score(span: list[dict[str, Any]]) -> float | None:
    """Return similarity in [0,1] between first and second halves of a span.

    Low score → topic/file cluster shift → soft boundary candidate (SEGMENT_THETA).
    Returns None when span too small to score.
    """
    if len(span) < 4:
        return None
    mid = len(span) // 2
    first = span[:mid]
    second = span[mid:]
    f_files: set[str] = set()
    s_files: set[str] = set()
    for o in first:
        f_files |= _files_from_obs(o)
    for o in second:
        s_files |= _files_from_obs(o)
    if f_files or s_files:
        union = f_files | s_files
        if not union:
            return None
        return len(f_files & s_files) / len(union)
    # Text fallback: token overlap on summaries
    f_tok = set()
    s_tok = set()
    for o in first:
        f_tok |= {t for t in (o.get("summary") or "").lower().split() if len(t) > 3}
    for o in second:
        s_tok |= {t for t in (o.get("summary") or "").lower().split() if len(t) > 3}
    if not f_tok and not s_tok:
        return None
    union = f_tok | s_tok
    return len(f_tok & s_tok) / len(union) if union else None
