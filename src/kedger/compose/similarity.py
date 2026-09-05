"""Shared near-duplicate / theme similarity for promote, import, consolidate.

Token/theme helpers are imported lazily to avoid cognify ↔ handoff import cycles.
"""

from __future__ import annotations


def near_duplicate(a: str, b: str, *, jaccard_tau: float = 0.55) -> bool:
    """Same theme or high token overlap → treat as already-anchored / mergeable."""
    # Lazy import: kedger.cognify.extract → engine → handoff → this module.
    from kedger.cognify.extract import _theme_keys, _token_set

    la = (a or "").strip().lower()
    lb = (b or "").strip().lower()
    if not la or not lb:
        return False
    if la == lb:
        return True
    ta = _theme_keys(la)
    tb = _theme_keys(lb)
    if ta and tb and (ta & tb):
        if la in lb or lb in la:
            return True
        sa, sb = _token_set(la), _token_set(lb)
        if sa and sb:
            inter = len(sa & sb)
            union = len(sa | sb) or 1
            if inter / union >= jaccard_tau:
                return True
    sa, sb = _token_set(la), _token_set(lb)
    if sa and sb:
        inter = len(sa & sb)
        union = len(sa | sb) or 1
        if inter / union >= 0.72:
            return True
    return False
