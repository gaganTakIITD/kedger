"""kedger why — explain an Anchor via provenance + SUPERSEDES chain."""

from __future__ import annotations

import json
from typing import Any

from kedger.acl import InvScopeError
from kedger.store.db import Store


def explain_anchor(
    store: Store, *, anchor_id: str, principal_id: str
) -> dict[str, Any]:
    try:
        anc = store.get_anchor_scoped(anchor_id, principal_id=principal_id)
    except KeyError as e:
        raise InvScopeError() from e

    chain: list[dict[str, Any]] = []
    cur: dict[str, Any] | None = anc
    seen: set[str] = set()
    while cur and cur["id"] not in seen:
        seen.add(cur["id"])
        chain.append(
            {
                "id": cur["id"],
                "kind": cur["kind"],
                "status": cur["status"],
                "statement": cur["statement"],
                "superseded_by": cur.get("superseded_by"),
            }
        )
        # walk SUPERSEDES edges to older
        with store.connection() as conn:
            row = conn.execute(
                "SELECT to_id FROM edges WHERE edge_type = 'SUPERSEDES' AND from_id = ? "
                "AND invalid_at IS NULL",
                (cur["id"],),
            ).fetchone()
        if not row:
            break
        cur = store.get_anchor(row["to_id"])

    supporting: list[dict[str, Any]] = []
    with store.connection() as conn:
        rows = conn.execute(
            "SELECT record_json FROM evidence WHERE supports_anchor_id = ?",
            (anchor_id,),
        ).fetchall()
    for r in rows:
        supporting.append(json.loads(r["record_json"]))

    return {
        "anchor": anc,
        "supersedes_chain": chain,
        "provenance": anc.get("provenance"),
        "evidence": supporting,
    }
