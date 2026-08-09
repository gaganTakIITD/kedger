"""Ranked hydrate projection (P5) — Inv-Scope → expand → score → drop order."""

from __future__ import annotations

import json
import math
import time
from dataclasses import dataclass, field
from typing import Any

from kedger.compose import compose_view
from kedger.constants import HANDOFF_MAX_BYTES, RECENCY_MU_SECONDS, SURVIVAL_RANK
from kedger.graph.expand import associative_expand, notebook_walk, seed_idf_scores
from kedger.handoff.dual_path import evidence_budget_for, select_evidence_dual_path
from kedger.hydrate.purpose import minimize_anchors
from kedger.store.db import Store


@dataclass
class HydrateProjection:
    anchors: list[dict[str, Any]]
    working: dict[str, Any] | None
    conflicts: list[dict[str, Any]] = field(default_factory=list)
    used_bytes: int = 0
    dropped: list[str] = field(default_factory=list)
    walk_ids: list[str] = field(default_factory=list)
    walk_budget: int = 0
    purpose: str | None = None
    notebook: list[dict[str, Any]] = field(default_factory=list)
    notebook_calls: int = 0
    notebook_terminated: str | None = None
    evidence: list[dict[str, Any]] = field(default_factory=list)


def _recency_score(created_at: str | None) -> float:
    if not created_at:
        return 0.0
    try:
        # ISO Z
        from datetime import datetime, timezone

        ts = created_at
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        dt = datetime.fromisoformat(ts)
        age = max(0.0, time.time() - dt.timestamp())
        return math.exp(-age / RECENCY_MU_SECONDS)
    except ValueError:
        return 0.0


def score_anchor(
    anc: dict[str, Any],
    *,
    topic_terms: set[str],
    notebook_boost: set[str] | None = None,
) -> float:
    kind_w = 1.0 - (SURVIVAL_RANK.get(anc.get("kind", ""), 9) / 10.0)
    imp = float(anc.get("importance") or 0.5)
    rec = _recency_score(anc.get("created_at"))
    stmt = (anc.get("statement") or "").lower()
    rel = 0.0
    if topic_terms:
        hits = sum(1 for t in topic_terms if t in stmt)
        rel = hits / max(1, len(topic_terms))
    boost = 0.5 if notebook_boost and anc.get("id") in notebook_boost else 0.0
    return 3.0 * kind_w + 2.0 * imp + 1.5 * rec + 2.0 * rel + boost


def project_hydrate(
    store: Store,
    *,
    principal_id: str,
    workstream_id: str,
    max_bytes: int = HANDOFF_MAX_BYTES,
    topic: str | None = None,
    walk_budget: int = 16,
    walk_hops: int = 2,
    purpose: str | None = None,
    notebook_max_calls: int = 10,
) -> HydrateProjection:
    if not store.has_permission(workstream_id, principal_id, "read_hydrate"):
        from kedger.acl import InvScopeError

        raise InvScopeError()

    working = store.get_working_state(workstream_id)
    topic_terms: set[str] = set()
    if topic:
        topic_terms |= {t for t in topic.lower().split() if len(t) > 2}
    if working:
        topic_terms |= {
            t
            for t in (working.get("goal") or "").lower().split()
            if len(t) > 2
        }
        for f in working.get("files_in_flight") or []:
            topic_terms.add(str(f).lower().split("/")[-1].split(".")[0])

    anchors = store.ranked_active_anchors(workstream_id=workstream_id)
    seed_ids = [a["id"] for a in anchors[:5]]
    idf = seed_idf_scores(store, seed_ids)

    # GraphReader-style budgeted associative expand from active anchor seeds
    walk_budget = max(0, int(walk_budget))
    expanded_ids = associative_expand(
        store,
        seed_ids,
        budget=walk_budget or 1,
        max_hops=walk_hops,
        seed_scores=idf,
    )
    if walk_budget == 0:
        expanded_ids = list(seed_ids)

    # Notebook walk (beyond hop budget): call-capped supporting facts
    nb = notebook_walk(
        store,
        seed_ids,
        topic_terms=topic_terms,
        max_calls=max(0, int(notebook_max_calls)),
        budget=max(walk_budget, 1),
        max_hops=walk_hops,
        seed_scores=idf,
    )
    notebook_boost = {e.node_id for e in nb.entries if e.node_id.startswith("anc_")}

    by_id = {a["id"]: a for a in anchors}
    for eid in list(expanded_ids) + list(notebook_boost):
        if eid.startswith("anc_") and eid not in by_id:
            try:
                a = store.get_anchor_scoped(eid, principal_id=principal_id)
                by_id[a["id"]] = a
            except KeyError:
                continue
            except Exception:  # noqa: BLE001 — Inv-Scope / missing
                continue
    pool = list(by_id.values())
    pool.sort(
        key=lambda a: -score_anchor(
            a, topic_terms=topic_terms, notebook_boost=notebook_boost
        )
    )

    composed, conflicts = compose_view(pool)

    # Primacy/recency layout: constraints first, then middle bulk, gotchas near end
    head = [a for a in composed if a["kind"] in {"constraint", "rejection", "decision"}]
    tail = [a for a in composed if a["kind"] in {"gotcha", "open_question"}]
    mid = [a for a in composed if a not in head and a not in tail]
    ordered = head + mid + tail

    ev_budget = evidence_budget_for(max_bytes)
    anchor_ceiling = max(512, max_bytes - ev_budget)

    selected: list[dict[str, Any]] = []
    dropped: list[str] = []
    for anc in ordered:
        trial = selected + [anc]
        raw = json.dumps(
            {"anchors": trial, "working": working, "evidence": []},
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        if len(raw) > anchor_ceiling and selected:
            if anc["kind"] in {"constraint", "rejection", "decision"}:
                # drop lower-survival from selected
                for i in range(len(selected) - 1, -1, -1):
                    if selected[i]["kind"] in {"gotcha", "open_question", "next_step"}:
                        dropped.append(selected[i]["id"])
                        selected.pop(i)
                        break
                else:
                    dropped.append(anc["id"])
                    continue
            else:
                dropped.append(anc["id"])
                continue
        selected.append(anc)

    # AirGap purpose minimization (field projection after selection)
    selected = minimize_anchors(selected, purpose)

    evidence = select_evidence_dual_path(
        store,
        anchor_ids=[a["id"] for a in selected],
        topic=topic
        or (
            (working or {}).get("last_user_ask")
            or (working or {}).get("goal")
            if working
            else None
        ),
        working=working,
        max_bytes=ev_budget,
    )
    # Drop Evidence before Anchors if over total max_bytes
    while True:
        used_trial = len(
            json.dumps(
                {"anchors": selected, "working": working, "evidence": evidence},
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        )
        if used_trial <= max_bytes or not evidence:
            break
        dropped.append(evidence[-1]["id"])
        evidence = evidence[:-1]

    used = len(
        json.dumps(
            {"anchors": selected, "working": working, "evidence": evidence},
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )
    return HydrateProjection(
        anchors=selected,
        working=working,
        conflicts=conflicts.conflicts,
        used_bytes=used,
        dropped=dropped,
        walk_ids=list(expanded_ids),
        walk_budget=walk_budget,
        purpose=purpose,
        notebook=nb.as_dicts(),
        notebook_calls=nb.call_count,
        notebook_terminated=nb.terminated,
        evidence=evidence,
    )
