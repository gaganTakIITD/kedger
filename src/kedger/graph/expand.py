"""Budgeted associative expand (recognition + lightweight PPR)."""

from __future__ import annotations

from typing import Any

from kedger.constants import PPR_DAMPING
from kedger.store.db import Store


def associative_expand(
    store: Store,
    seed_ids: list[str],
    *,
    budget: int = 12,
    damping: float = PPR_DAMPING,
) -> list[str]:
    """Return related ids via edge walks; damped scores, budgeted."""
    import json

    scores: dict[str, float] = {sid: 1.0 for sid in seed_ids}
    with store.connection() as conn:
        rows = conn.execute(
            "SELECT from_id, to_id, edge_type, invalid_at FROM edges"
        ).fetchall()
    edges = [
        (r["from_id"], r["to_id"])
        for r in rows
        if r["invalid_at"] is None
    ]
    # 2 iterations of personalized PageRank-ish expansion
    for _ in range(2):
        nxt = dict(scores)
        for src, dst in edges:
            if src in scores:
                nxt[dst] = nxt.get(dst, 0.0) + damping * scores[src]
            if dst in scores:
                nxt[src] = nxt.get(src, 0.0) + damping * 0.5 * scores[dst]
        scores = nxt
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    out: list[str] = []
    for nid, _ in ranked:
        if nid not in out:
            out.append(nid)
        if len(out) >= budget:
            break
    return out
