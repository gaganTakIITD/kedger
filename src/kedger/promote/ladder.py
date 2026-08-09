"""Promotion into Anchorhood — orthogonal to share (explicit_only)."""

from __future__ import annotations

import json
from typing import Any

from kedger.constants import HEAT_TAU, RECURRENCE_PROMOTE_THETA
from kedger.keys.principal import Principal
from kedger.redact import redact_text
from kedger.store.db import Store


def promote_candidates(
    store: Store,
    *,
    principal: Principal,
    workstream_id: str,
    mode: str = "conservative",
) -> list[dict[str, Any]]:
    """
    Commit Tier A candidates; leave Tier B as candidates unless normal mode + thresholds.
    Never sets shareable.
    """
    with store.connection() as conn:
        rows = conn.execute(
            "SELECT record_json FROM promotion_candidates "
            "WHERE workstream_id = ? AND status = 'candidate' ORDER BY created_at ASC",
            (workstream_id,),
        ).fetchall()
    promoted: list[dict[str, Any]] = []
    for row in rows:
        cand = json.loads(row["record_json"])
        tier = cand.get("tier")
        commit = False
        if tier == "A":
            commit = True
        elif tier == "B" and mode == "normal":
            if (
                int(cand.get("recurrence") or 0) >= RECURRENCE_PROMOTE_THETA
                or float(cand.get("heat") or 0) >= HEAT_TAU
            ):
                commit = True
        # Tier C never
        if not commit:
            continue
        # Pre-commit gate
        scan = redact_text(cand.get("statement") or "")
        if scan.blocked_for_share and mode == "conservative":
            # still allow private Anchor, but record hits
            pass
        if not cand.get("statement"):
            continue
        # Dedupe against active anchors
        existing = store.list_anchors(active_only=True)
        if any(
            a.get("statement", "").lower() == cand["statement"].lower()
            and a.get("workstream_id") == workstream_id
            for a in existing
        ):
            _mark(store, cand, "noop_duplicate")
            continue
        anc = store.remember(
            cand["kind"],
            cand["statement"],
            reason=f"promoted tier {tier}",
            principal_id=principal.principal_id,
            shareable=False,
            workstream_id=workstream_id,
        )
        src_obs = cand.get("source_observation_id")
        if src_obs:
            try:
                store.insert_evidence(
                    supports_anchor_id=anc["id"],
                    snippet=(cand.get("statement") or "")[:280],
                    source_ref=f"{cand.get('source_type') or 'observation'}:{src_obs}",
                    weight=1.0,
                )
            except Exception:  # noqa: BLE001 — evidence is best-effort on promote
                pass
        _mark(store, cand, "promoted", anc_id=anc["id"])
        promoted.append(anc)
    return promoted


def _mark(
    store: Store, cand: dict[str, Any], status: str, *, anc_id: str | None = None
) -> None:
    cand = dict(cand)
    cand["status"] = status
    if anc_id:
        cand["promoted_anchor_id"] = anc_id
    with store.connection() as conn:
        conn.execute(
            "UPDATE promotion_candidates SET status = ?, record_json = ? WHERE id = ?",
            (status, json.dumps(cand), cand["id"]),
        )
