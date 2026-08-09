"""Budgeted associative expand + GraphReader-style notebook walk."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from kedger.constants import PPR_DAMPING
from kedger.store.db import Store


def associative_expand(
    store: Store,
    seed_ids: list[str],
    *,
    budget: int = 12,
    damping: float = PPR_DAMPING,
    max_hops: int = 2,
) -> list[str]:
    """Return related ids via edge walks; damped scores, budgeted.

    GraphReader-style call budget: ``budget`` caps returned nodes; ``max_hops``
    caps expansion iterations (walk depth).
    """
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
    hops = max(0, int(max_hops))
    for _ in range(hops):
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


@dataclass
class WalkEntry:
    node_id: str
    hop: int
    via_edge: str | None
    fact: str
    score: float


@dataclass
class WalkNotebook:
    """GraphReader-style notebook of supporting facts (deterministic, no LLM)."""

    entries: list[WalkEntry] = field(default_factory=list)
    call_count: int = 0
    max_calls: int = 10
    terminated: str = "budget"  # budget | topic_satisfied | empty

    def node_ids(self) -> list[str]:
        out: list[str] = []
        for e in self.entries:
            if e.node_id not in out:
                out.append(e.node_id)
        return out

    def as_dicts(self) -> list[dict[str, Any]]:
        return [
            {
                "node_id": e.node_id,
                "hop": e.hop,
                "via_edge": e.via_edge,
                "fact": e.fact,
                "score": e.score,
            }
            for e in self.entries
        ]


def notebook_walk(
    store: Store,
    seed_ids: list[str],
    *,
    topic_terms: set[str] | None = None,
    max_calls: int = 10,
    budget: int = 12,
    max_hops: int = 2,
) -> WalkNotebook:
    """Coarse-to-fine walk: seed → score neighbors → append notebook facts.

    Caps **calls** (neighbor inspections) separately from node ``budget``.
    Stops early when topic terms are covered by notebook facts.
    """
    topic_terms = topic_terms or set()
    max_calls = max(0, int(max_calls))
    budget = max(1, int(budget))
    nb = WalkNotebook(max_calls=max_calls)

    if not seed_ids or max_calls == 0:
        nb.terminated = "empty"
        return nb

    # adjacency with edge type
    with store.connection() as conn:
        rows = conn.execute(
            "SELECT from_id, to_id, edge_type, invalid_at FROM edges"
        ).fetchall()
    adj: dict[str, list[tuple[str, str]]] = {}
    for r in rows:
        if r["invalid_at"] is not None:
            continue
        adj.setdefault(r["from_id"], []).append((r["to_id"], r["edge_type"]))
        adj.setdefault(r["to_id"], []).append((r["from_id"], r["edge_type"]))

    def fact_for(nid: str) -> str:
        if nid.startswith("anc_"):
            try:
                a = store.get_anchor(nid)
                return str(a.get("statement") or nid)
            except Exception:  # noqa: BLE001
                return nid
        # entity or other
        try:
            with store.connection() as conn:
                row = conn.execute(
                    "SELECT record_json FROM entities WHERE id = ?", (nid,)
                ).fetchone()
            if row:
                import json

                rec = json.loads(row["record_json"])
                return str(rec.get("name") or rec.get("normalized_key") or nid)
        except Exception:  # noqa: BLE001
            pass
        return nid

    def score_node(nid: str, hop: int) -> float:
        fact = fact_for(nid).lower()
        rel = 0.0
        if topic_terms:
            hits = sum(1 for t in topic_terms if t in fact)
            rel = hits / max(1, len(topic_terms))
        return rel * 2.0 + max(0.0, 1.0 - 0.2 * hop)

    visited: set[str] = set()
    frontier: list[tuple[str, int, str | None]] = [
        (sid, 0, None) for sid in seed_ids[:5]
    ]

    covered = set(topic_terms)

    while frontier and nb.call_count < max_calls and len(nb.node_ids()) < budget:
        # pick highest scoring frontier item
        frontier.sort(key=lambda x: -score_node(x[0], x[1]))
        nid, hop, via = frontier.pop(0)
        nb.call_count += 1
        if nid in visited:
            continue
        visited.add(nid)
        sc = score_node(nid, hop)
        fact = fact_for(nid)
        nb.entries.append(
            WalkEntry(node_id=nid, hop=hop, via_edge=via, fact=fact, score=round(sc, 3))
        )
        # topic coverage
        fl = fact.lower()
        for t in list(covered):
            if t in fl:
                covered.discard(t)
        if topic_terms and not covered:
            nb.terminated = "topic_satisfied"
            break
        if hop >= max_hops:
            continue
        for dst, etype in adj.get(nid, []):
            if dst not in visited:
                frontier.append((dst, hop + 1, etype))

    if nb.terminated == "budget" and not nb.entries:
        nb.terminated = "empty"
    elif nb.terminated == "budget" and nb.call_count >= max_calls:
        nb.terminated = "budget"
    return nb
