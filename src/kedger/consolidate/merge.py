"""Sleep-time near-dup Anchor consolidate (offline; never SessionStart).

Clusters active Anchors by near-duplicate / compose duplicate|refinement,
keeps the survival-rank winner, and forgets losers via SUPERSEDES.
True contradictions (ESCALATE) are left alone.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from kedger.compose.ops import classify, kind_policy
from kedger.compose.similarity import near_duplicate
from kedger.constants import SURVIVAL_RANK
from kedger.keys.principal import Principal
from kedger.store.db import Store


@dataclass
class MergeAction:
    keep_id: str
    drop_id: str
    reason: str
    keep_statement: str
    drop_statement: str


@dataclass
class ConsolidateResult:
    workstream_id: str
    scanned: int = 0
    clusters: int = 0
    merged: int = 0
    skipped_escalate: int = 0
    dry_run: bool = False
    actions: list[MergeAction] = field(default_factory=list)


def _ts(created_at: str | None) -> float:
    if not created_at:
        return 0.0
    try:
        ts = created_at
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        return datetime.fromisoformat(ts).timestamp()
    except ValueError:
        return 0.0


def _winner(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    """Higher survival (lower rank), then importance, then length, then recency."""

    def key(x: dict[str, Any]) -> tuple:
        return (
            SURVIVAL_RANK.get(x.get("kind", ""), 9),
            -float(x.get("importance") or 0.5),
            -len(x.get("statement") or ""),
            -_ts(x.get("created_at")),
        )

    return a if key(a) <= key(b) else b


def _mergeable_pair(a: dict[str, Any], b: dict[str, Any]) -> str | None:
    """Return merge reason or None if must not merge.

    Near-duplicate paraphrases merge even when compose would call them a
    same-slot contradiction (e.g. Redis wording variants). True alternatives
    with low lexical overlap (us-east vs eu-west) stay ESCALATE and are skipped.
    """
    sa = a.get("statement") or ""
    sb = b.get("statement") or ""
    ctype = classify(a, b)
    if ctype in {"duplicate", "refinement"}:
        return ctype
    if a.get("kind") == b.get("kind") and near_duplicate(sa, sb):
        # High lexical/theme overlap → paraphrase debt, not a real fork
        return "near_duplicate"
    action = kind_policy(ctype, a, b)
    if action == "ESCALATE" or ctype == "contradiction":
        return None
    return None


def consolidate_workstream(
    store: Store,
    *,
    principal: Principal,
    workstream_id: str,
    dry_run: bool = False,
) -> ConsolidateResult:
    """Offline pass: merge near-dup active Anchors via forget/SUPERSEDES."""
    anchors = store.ranked_active_anchors(workstream_id=workstream_id)
    result = ConsolidateResult(
        workstream_id=workstream_id, scanned=len(anchors), dry_run=dry_run
    )
    if len(anchors) < 2:
        return result

    n = len(anchors)
    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[rj] = ri

    escalate_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            reason = _mergeable_pair(anchors[i], anchors[j])
            if reason is None:
                ctype = classify(anchors[i], anchors[j])
                if kind_policy(ctype, anchors[i], anchors[j]) == "ESCALATE":
                    escalate_pairs += 1
                continue
            union(i, j)

    result.skipped_escalate = escalate_pairs
    clusters: dict[int, list[dict[str, Any]]] = {}
    for i, anc in enumerate(anchors):
        clusters.setdefault(find(i), []).append(anc)

    for members in clusters.values():
        if len(members) < 2:
            continue
        result.clusters += 1
        keep = members[0]
        for m in members[1:]:
            keep = _winner(keep, m)
        for m in members:
            if m["id"] == keep["id"]:
                continue
            reason = _mergeable_pair(keep, m) or "near_duplicate"
            action = MergeAction(
                keep_id=keep["id"],
                drop_id=m["id"],
                reason=reason,
                keep_statement=str(keep.get("statement") or ""),
                drop_statement=str(m.get("statement") or ""),
            )
            result.actions.append(action)
            if dry_run:
                continue
            try:
                store.forget(m["id"], principal_id=principal.principal_id)
                result.merged += 1
            except (KeyError, ValueError):
                continue

    if dry_run:
        result.merged = 0
    return result
