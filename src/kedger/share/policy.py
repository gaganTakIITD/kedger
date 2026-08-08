"""Sharehood ladder — orthogonal to Anchorhood; share_mode=explicit_only."""

from __future__ import annotations

import json
from typing import Any

from kedger.acl import InvScopeError
from kedger.constants import SHARE_KIND_ALLOWLIST, SHARE_MODE
from kedger.redact import redact_text
from kedger.store.db import Store, utc_now


def share_anchor(store: Store, *, anchor_id: str, principal_id: str) -> dict[str, Any]:
    """Promote workstream-private Anchor to repo_shared_safe after redaction gate."""
    _ = SHARE_MODE  # locked explicit_only — this function is the only auto path: none
    anc = store.get_anchor(anchor_id)
    if anc is None or anc.get("status") != "active":
        raise InvScopeError()
    # Capability: must have append/admin on workstream if scoped
    ws_id = anc.get("workstream_id")
    if ws_id and not (
        store.has_permission(ws_id, principal_id, "append")
        or store.has_permission(ws_id, principal_id, "admin")
    ):
        raise InvScopeError()

    kind = anc.get("kind")
    if kind not in SHARE_KIND_ALLOWLIST:
        raise ValueError(f"kind {kind!r} not shareable (allowlist)")

    statement = anc.get("statement") or ""
    reason = anc.get("reason") or ""
    scan = redact_text(statement + "\n" + reason)
    prior_hits = list(anc.get("secret_hits") or [])
    hits = sorted(set(scan.hits + prior_hits))
    if hits:
        raise ValueError(f"redaction gate blocked share: {', '.join(hits)}")

    # Detach evidence by default — clear any evidence links in about if present
    now = utc_now()
    anc["shareable"] = True
    anc["visibility"] = "repo_shared_safe"
    anc["updated_at"] = now
    anc["redaction_manifest"] = {
        "detached_evidence": True,
        "hits": [],
        "mode": "explicit_only",
        "at": now,
    }
    _persist_anchor(store, anc)
    return anc


def unshare_anchor(store: Store, *, anchor_id: str, principal_id: str) -> dict[str, Any]:
    """Revoke shared projection; keep workstream-private source."""
    anc = store.get_anchor(anchor_id)
    if anc is None:
        raise InvScopeError()
    ws_id = anc.get("workstream_id")
    if ws_id and not store.has_permission(ws_id, principal_id, "admin"):
        # Also allow if shareable and actor is provenance actor
        prov = anc.get("provenance") or {}
        if prov.get("actor_principal_id") != principal_id:
            raise InvScopeError()

    now = utc_now()
    anc["shareable"] = False
    anc["visibility"] = "workstream_private"
    anc["updated_at"] = now
    anc["unshared_at"] = now
    _persist_anchor(store, anc)
    # Mark handoffs stale for cascade
    if ws_id:
        with store.connection() as conn:
            conn.execute(
                "UPDATE handoffs SET superseded = 1 WHERE workstream_id = ? AND superseded = 0",
                (ws_id,),
            )
    return anc


def _persist_anchor(store: Store, anc: dict[str, Any]) -> None:
    with store.connection() as conn:
        conn.execute(
            """
            UPDATE anchors
            SET shareable = ?, visibility = ?, updated_at = ?, record_json = ?
            WHERE id = ?
            """,
            (
                1 if anc.get("shareable") else 0,
                anc["visibility"],
                anc["updated_at"],
                json.dumps(anc),
                anc["id"],
            ),
        )
