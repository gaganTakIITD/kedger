"""Entity upsert with normalized_key uniqueness per repo."""

from __future__ import annotations

from typing import Any

from kedger import SCHEMA_VERSION
from kedger.ids import new_id
from kedger.store.db import Store, utc_now


def upsert_entity(
    store: Store,
    *,
    entity_type: str,
    name: str,
    aliases: list[str] | None = None,
) -> dict[str, Any]:
    import json

    normalized = f"{entity_type}:{name}".lower()
    with store.connection() as conn:
        row = conn.execute(
            "SELECT record_json FROM entities WHERE normalized_key = ?",
            (normalized,),
        ).fetchone()
        now = utc_now()
        if row:
            rec = json.loads(row["record_json"])
            als = list(dict.fromkeys((rec.get("aliases") or []) + (aliases or [])))
            rec["aliases"] = als
            rec["updated_at"] = now
            conn.execute(
                "UPDATE entities SET aliases_json = ?, updated_at = ?, record_json = ? "
                "WHERE id = ?",
                (json.dumps(als), now, json.dumps(rec), rec["id"]),
            )
            return rec
        rec = {
            "schema_version": SCHEMA_VERSION,
            "id": new_id("ent"),
            "entity_type": entity_type,
            "name": name,
            "normalized_key": normalized,
            "repo_fingerprint": store.repo_fingerprint,
            "aliases": aliases or [],
            "created_at": now,
            "updated_at": now,
        }
        conn.execute(
            """
            INSERT INTO entities(
              id, entity_type, name, normalized_key, aliases_json,
              created_at, updated_at, record_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                rec["id"],
                entity_type,
                name,
                normalized,
                json.dumps(rec["aliases"]),
                now,
                now,
                json.dumps(rec),
            ),
        )
        return rec
