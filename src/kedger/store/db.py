"""SQLite store for kedger.memory.v1 records."""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from kedger import SCHEMA_VERSION
from kedger.ids import new_id
from kedger.store.paths import ensure_layout

ANCHOR_KINDS = frozenset(
    {
        "decision",
        "rejection",
        "constraint",
        "gotcha",
        "goal",
        "next_step",
        "open_question",
    }
)

# CLI aliases → schema kinds
KIND_ALIASES = {
    "reject": "rejection",
    "rejection": "rejection",
    "decision": "decision",
    "constraint": "constraint",
    "gotcha": "gotcha",
    "goal": "goal",
    "next_step": "next_step",
    "next": "next_step",
    "open_question": "open_question",
    "question": "open_question",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_kind(kind: str) -> str:
    key = kind.strip().lower().replace("-", "_")
    if key not in KIND_ALIASES:
        raise ValueError(
            f"unknown anchor kind {kind!r}; "
            f"expected one of {sorted(KIND_ALIASES)}"
        )
    return KIND_ALIASES[key]


@dataclass
class Store:
    path: Path
    repo_fingerprint: str

    @classmethod
    def open(cls, repo_fingerprint: str) -> "Store":
        path = ensure_layout(repo_fingerprint)
        store = cls(path=path, repo_fingerprint=repo_fingerprint)
        store._init_schema()
        return store

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    @contextmanager
    def connection(self) -> Iterator[sqlite3.Connection]:
        conn = self._connect()
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _init_schema(self) -> None:
        with self.connection() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS meta (
                  key TEXT PRIMARY KEY,
                  value TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS anchors (
                  id TEXT PRIMARY KEY,
                  kind TEXT NOT NULL,
                  statement TEXT NOT NULL,
                  reason TEXT,
                  status TEXT NOT NULL,
                  visibility TEXT NOT NULL,
                  importance REAL NOT NULL,
                  valid_at TEXT NOT NULL,
                  invalid_at TEXT,
                  created_at TEXT NOT NULL,
                  updated_at TEXT NOT NULL,
                  supersedes_json TEXT NOT NULL DEFAULT '[]',
                  superseded_by TEXT,
                  provenance_json TEXT NOT NULL,
                  shareable INTEGER NOT NULL DEFAULT 0,
                  workstream_id TEXT,
                  about_json TEXT NOT NULL DEFAULT '[]',
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS edges (
                  id TEXT PRIMARY KEY,
                  edge_type TEXT NOT NULL,
                  from_id TEXT NOT NULL,
                  to_id TEXT NOT NULL,
                  valid_at TEXT NOT NULL,
                  invalid_at TEXT,
                  created_at TEXT NOT NULL,
                  meta_json TEXT NOT NULL DEFAULT '{}',
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS observations (
                  id TEXT PRIMARY KEY,
                  type TEXT NOT NULL,
                  ts TEXT NOT NULL,
                  session_id TEXT NOT NULL,
                  actor_principal_id TEXT NOT NULL,
                  summary TEXT NOT NULL,
                  visibility TEXT NOT NULL,
                  importance REAL,
                  workstream_id TEXT,
                  agent_tool TEXT,
                  payload_json TEXT NOT NULL,
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS workstreams (
                  id TEXT PRIMARY KEY,
                  name TEXT NOT NULL,
                  slug TEXT NOT NULL,
                  status TEXT NOT NULL,
                  member_json TEXT NOT NULL,
                  created_at TEXT NOT NULL,
                  updated_at TEXT NOT NULL,
                  record_json TEXT NOT NULL,
                  UNIQUE(slug)
                );

                CREATE TABLE IF NOT EXISTS capabilities (
                  id TEXT PRIMARY KEY,
                  grantee_principal_id TEXT NOT NULL,
                  issuer_principal_id TEXT NOT NULL,
                  workstream_id TEXT NOT NULL,
                  permissions_json TEXT NOT NULL,
                  created_at TEXT NOT NULL,
                  expires_at TEXT,
                  revoked_at TEXT,
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS working_states (
                  id TEXT PRIMARY KEY,
                  workstream_id TEXT NOT NULL UNIQUE,
                  record_json TEXT NOT NULL,
                  updated_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS known_principals (
                  principal_id TEXT PRIMARY KEY,
                  display_name TEXT NOT NULL,
                  public_key_b64 TEXT NOT NULL,
                  x25519_public_b64 TEXT NOT NULL,
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS handoffs (
                  id TEXT PRIMARY KEY,
                  workstream_id TEXT NOT NULL,
                  epoch INTEGER NOT NULL,
                  pack_path TEXT NOT NULL,
                  created_at TEXT NOT NULL,
                  from_principal_id TEXT NOT NULL,
                  recipient_json TEXT NOT NULL,
                  superseded INTEGER NOT NULL DEFAULT 0,
                  record_json TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_anchors_status ON anchors(status);
                CREATE INDEX IF NOT EXISTS idx_edges_type ON edges(edge_type);
                CREATE INDEX IF NOT EXISTS idx_obs_ts ON observations(ts);
                CREATE INDEX IF NOT EXISTS idx_caps_ws ON capabilities(workstream_id);
                """
            )
            conn.execute(
                "INSERT OR IGNORE INTO meta(key, value) VALUES (?, ?)",
                ("schema_version", SCHEMA_VERSION),
            )
            conn.execute(
                "INSERT OR IGNORE INTO meta(key, value) VALUES (?, ?)",
                ("repo_fingerprint", self.repo_fingerprint),
            )

    def remember(
        self,
        kind: str,
        statement: str,
        *,
        reason: str | None = None,
        principal_id: str,
        shareable: bool = False,
        workstream_id: str | None = None,
        session_id: str | None = None,
        importance: float = 0.9,
    ) -> dict[str, Any]:
        kind = normalize_kind(kind)
        statement = statement.strip()
        if not statement:
            raise ValueError("statement must be non-empty")
        if len(statement) > 240:
            raise ValueError("statement max 240 chars")
        if reason is not None and len(reason) > 480:
            raise ValueError("reason max 480 chars")

        # share_mode=explicit_only — never auto-promote
        visibility = "repo_shared_safe" if shareable else "workstream_private"
        if shareable and visibility != "repo_shared_safe":
            raise ValueError("shareable=true requires visibility=repo_shared_safe")

        now = utc_now()
        anc_id = new_id("anc")
        provenance = {
            "episode_id": None,
            "observation_ids": [],
            "actor_principal_id": principal_id,
            "session_id": session_id or "cli",
            "agent_tool": "other",
            "source": "explicit",
            "repo_fingerprint": self.repo_fingerprint,
            "branch": None,
            "workstream_id": workstream_id,
        }
        record = {
            "schema_version": SCHEMA_VERSION,
            "id": anc_id,
            "kind": kind,
            "statement": statement,
            "reason": reason,
            "status": "active",
            "about": [],
            "repo_fingerprint": self.repo_fingerprint,
            "workstream_id": workstream_id,
            "visibility": visibility,
            "importance": importance,
            "valid_at": now,
            "invalid_at": None,
            "created_at": now,
            "updated_at": now,
            "supersedes": [],
            "superseded_by": None,
            "provenance": provenance,
            "shareable": bool(shareable),
        }
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO anchors(
                  id, kind, statement, reason, status, visibility, importance,
                  valid_at, invalid_at, created_at, updated_at, supersedes_json,
                  superseded_by, provenance_json, shareable, workstream_id,
                  about_json, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    anc_id,
                    kind,
                    statement,
                    reason,
                    "active",
                    visibility,
                    importance,
                    now,
                    None,
                    now,
                    now,
                    "[]",
                    None,
                    json.dumps(provenance),
                    1 if shareable else 0,
                    workstream_id,
                    "[]",
                    json.dumps(record),
                ),
            )
        return record

    def forget(self, anchor_id: str, *, principal_id: str) -> dict[str, Any]:
        """Invalidate an anchor via SUPERSEDES — never hard-delete."""
        with self.connection() as conn:
            row = conn.execute(
                "SELECT * FROM anchors WHERE id = ?", (anchor_id,)
            ).fetchone()
            if row is None:
                raise KeyError(f"anchor not found: {anchor_id}")
            if row["status"] != "active":
                raise ValueError(
                    f"anchor {anchor_id} is already {row['status']}"
                )

            now = utc_now()
            tomb_id = new_id("anc")
            provenance = {
                "episode_id": None,
                "observation_ids": [],
                "actor_principal_id": principal_id,
                "session_id": "cli",
                "agent_tool": "other",
                "source": "explicit",
                "repo_fingerprint": self.repo_fingerprint,
                "branch": None,
                "workstream_id": row["workstream_id"],
            }
            tomb = {
                "schema_version": SCHEMA_VERSION,
                "id": tomb_id,
                "kind": row["kind"],
                "statement": f"[forgotten] {row['statement']}"[:240],
                "reason": f"Supersedes {anchor_id} via kedger forget",
                "status": "archived",
                "about": json.loads(row["about_json"]),
                "repo_fingerprint": self.repo_fingerprint,
                "workstream_id": row["workstream_id"],
                "visibility": row["visibility"],
                "importance": row["importance"],
                "valid_at": now,
                "invalid_at": now,
                "created_at": now,
                "updated_at": now,
                "supersedes": [anchor_id],
                "superseded_by": None,
                "provenance": provenance,
                "shareable": False,
            }
            conn.execute(
                """
                INSERT INTO anchors(
                  id, kind, statement, reason, status, visibility, importance,
                  valid_at, invalid_at, created_at, updated_at, supersedes_json,
                  superseded_by, provenance_json, shareable, workstream_id,
                  about_json, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    tomb_id,
                    tomb["kind"],
                    tomb["statement"],
                    tomb["reason"],
                    "archived",
                    tomb["visibility"],
                    tomb["importance"],
                    now,
                    now,
                    now,
                    now,
                    json.dumps([anchor_id]),
                    None,
                    json.dumps(provenance),
                    0,
                    row["workstream_id"],
                    row["about_json"],
                    json.dumps(tomb),
                ),
            )

            old = json.loads(row["record_json"])
            old["status"] = "superseded"
            old["invalid_at"] = now
            old["superseded_by"] = tomb_id
            old["updated_at"] = now
            conn.execute(
                """
                UPDATE anchors
                SET status = ?, invalid_at = ?, superseded_by = ?,
                    updated_at = ?, record_json = ?
                WHERE id = ?
                """,
                ("superseded", now, tomb_id, now, json.dumps(old), anchor_id),
            )

            edge_id = new_id("eg")
            edge = {
                "schema_version": SCHEMA_VERSION,
                "id": edge_id,
                "edge_type": "SUPERSEDES",
                "from_id": tomb_id,
                "to_id": anchor_id,
                "repo_fingerprint": self.repo_fingerprint,
                "workstream_id": row["workstream_id"],
                "valid_at": now,
                "invalid_at": None,
                "created_at": now,
                "meta": {"weight": 1.0, "note": "kedger forget"},
            }
            conn.execute(
                """
                INSERT INTO edges(
                  id, edge_type, from_id, to_id, valid_at, invalid_at,
                  created_at, meta_json, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    edge_id,
                    "SUPERSEDES",
                    tomb_id,
                    anchor_id,
                    now,
                    None,
                    now,
                    json.dumps(edge["meta"]),
                    json.dumps(edge),
                ),
            )
            return {"forgotten": old, "tombstone": tomb, "edge": edge}

    def list_anchors(self, *, active_only: bool = True) -> list[dict[str, Any]]:
        with self.connection() as conn:
            if active_only:
                rows = conn.execute(
                    "SELECT record_json FROM anchors WHERE status = 'active' "
                    "ORDER BY created_at ASC"
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT record_json FROM anchors ORDER BY created_at ASC"
                ).fetchall()
        return [json.loads(r["record_json"]) for r in rows]

    def get_anchor(self, anchor_id: str) -> dict[str, Any] | None:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM anchors WHERE id = ?", (anchor_id,)
            ).fetchone()
        if row is None:
            return None
        return json.loads(row["record_json"])

    def counts(self) -> dict[str, int]:
        with self.connection() as conn:
            active = conn.execute(
                "SELECT COUNT(*) AS c FROM anchors WHERE status = 'active'"
            ).fetchone()["c"]
            superseded = conn.execute(
                "SELECT COUNT(*) AS c FROM anchors WHERE status = 'superseded'"
            ).fetchone()["c"]
            total_anchors = conn.execute(
                "SELECT COUNT(*) AS c FROM anchors"
            ).fetchone()["c"]
            edges = conn.execute(
                "SELECT COUNT(*) AS c FROM edges"
            ).fetchone()["c"]
            observations = conn.execute(
                "SELECT COUNT(*) AS c FROM observations"
            ).fetchone()["c"]
            supersedes = conn.execute(
                "SELECT COUNT(*) AS c FROM edges WHERE edge_type = 'SUPERSEDES'"
            ).fetchone()["c"]
        return {
            "anchors_active": active,
            "anchors_superseded": superseded,
            "anchors_total": total_anchors,
            "edges": edges,
            "supersedes_edges": supersedes,
            "observations": observations,
        }

    def ingest_observation(self, payload: dict[str, Any], *, principal_id: str) -> dict[str, Any]:
        """Append an L0 observation from hook JSON."""
        now = utc_now()
        obs_id = payload.get("id") or new_id("obs")
        obs_type = payload.get("type") or payload.get("event") or "note"
        summary = (
            payload.get("summary")
            or payload.get("text")
            or payload.get("message")
            or json.dumps(payload, sort_keys=True)[:200]
        )
        session_id = payload.get("session_id") or "hook"
        visibility = payload.get("visibility") or "private_raw"
        importance = float(payload.get("importance", 0.5))
        record = {
            "schema_version": SCHEMA_VERSION,
            "id": obs_id,
            "type": obs_type,
            "ts": payload.get("ts") or now,
            "repo_fingerprint": self.repo_fingerprint,
            "workstream_id": payload.get("workstream_id"),
            "session_id": session_id,
            "actor_principal_id": payload.get("actor_principal_id") or principal_id,
            "agent_tool": payload.get("agent_tool") or "other",
            "summary": summary,
            "payload_ref": payload.get("payload_ref"),
            "entity_hints": payload.get("entity_hints") or [],
            "importance": importance,
            "redacted": bool(payload.get("redacted", False)),
            "visibility": visibility,
        }
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO observations(
                  id, type, ts, session_id, actor_principal_id, summary,
                  visibility, importance, workstream_id, agent_tool,
                  payload_json, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    obs_id,
                    obs_type,
                    record["ts"],
                    session_id,
                    record["actor_principal_id"],
                    summary,
                    visibility,
                    importance,
                    record["workstream_id"],
                    record["agent_tool"],
                    json.dumps(payload),
                    json.dumps(record),
                ),
            )
        return record

    def meta(self) -> dict[str, str]:
        with self.connection() as conn:
            rows = conn.execute("SELECT key, value FROM meta").fetchall()
        return {r["key"]: r["value"] for r in rows}

    # --- Phase B: workstreams, ACL, working state, handoffs ---

    SURVIVAL_RANK = {
        "constraint": 0,
        "rejection": 1,
        "decision": 2,
        "goal": 3,
        "next_step": 4,
        "open_question": 5,
        "gotcha": 6,
    }

    def ensure_workstream(
        self,
        *,
        slug: str = "default",
        name: str | None = None,
        principal_id: str,
    ) -> dict[str, Any]:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM workstreams WHERE slug = ?", (slug,)
            ).fetchone()
            if row:
                return json.loads(row["record_json"])
            now = utc_now()
            ws_id = new_id("ws")
            record = {
                "schema_version": SCHEMA_VERSION,
                "id": ws_id,
                "repo_fingerprint": self.repo_fingerprint,
                "name": name or slug,
                "slug": slug,
                "status": "active",
                "primary_branches": [],
                "member_principal_ids": [principal_id],
                "created_at": now,
                "updated_at": now,
                "visibility": "workstream_private",
            }
            conn.execute(
                """
                INSERT INTO workstreams(
                  id, name, slug, status, member_json, created_at, updated_at, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    ws_id,
                    record["name"],
                    slug,
                    "active",
                    json.dumps(record["member_principal_ids"]),
                    now,
                    now,
                    json.dumps(record),
                ),
            )
            # issuer grants self admin + hydrate
            cap_id = new_id("cap")
            cap = {
                "schema_version": SCHEMA_VERSION,
                "id": cap_id,
                "grantee_principal_id": principal_id,
                "issuer_principal_id": principal_id,
                "scope": {
                    "type": "workstream",
                    "workstream_id": ws_id,
                    "handoff_id": None,
                },
                "permissions": ["read_hydrate", "append", "admin"],
                "created_at": now,
                "expires_at": None,
                "revoked_at": None,
                "issuer_signature": "self",
            }
            conn.execute(
                """
                INSERT INTO capabilities(
                  id, grantee_principal_id, issuer_principal_id, workstream_id,
                  permissions_json, created_at, expires_at, revoked_at, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cap_id,
                    principal_id,
                    principal_id,
                    ws_id,
                    json.dumps(cap["permissions"]),
                    now,
                    None,
                    None,
                    json.dumps(cap),
                ),
            )
            return record

    def get_workstream(self, workstream_id: str) -> dict[str, Any] | None:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM workstreams WHERE id = ?", (workstream_id,)
            ).fetchone()
        return json.loads(row["record_json"]) if row else None

    def get_workstream_by_slug(self, slug: str) -> dict[str, Any] | None:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM workstreams WHERE slug = ?", (slug,)
            ).fetchone()
        return json.loads(row["record_json"]) if row else None

    def upsert_known_principal(
        self,
        *,
        principal_id: str,
        display_name: str,
        public_key_b64: str,
        x25519_public_b64: str,
    ) -> None:
        record = {
            "schema_version": SCHEMA_VERSION,
            "id": principal_id,
            "display_name": display_name,
            "public_key": public_key_b64,
            "x25519_public_b64": x25519_public_b64,
            "created_at": utc_now(),
        }
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO known_principals(
                  principal_id, display_name, public_key_b64, x25519_public_b64, record_json
                ) VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(principal_id) DO UPDATE SET
                  display_name=excluded.display_name,
                  public_key_b64=excluded.public_key_b64,
                  x25519_public_b64=excluded.x25519_public_b64,
                  record_json=excluded.record_json
                """,
                (
                    principal_id,
                    display_name,
                    public_key_b64,
                    x25519_public_b64,
                    json.dumps(record),
                ),
            )

    def get_known_principal(self, principal_id: str) -> dict[str, Any] | None:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM known_principals WHERE principal_id = ?",
                (principal_id,),
            ).fetchone()
        return json.loads(row["record_json"]) if row else None

    def grant(
        self,
        *,
        workstream_id: str,
        grantee_principal_id: str,
        issuer_principal_id: str,
        permissions: list[str] | None = None,
        grantee_public_key_b64: str | None = None,
        grantee_x25519_public_b64: str | None = None,
        grantee_name: str = "peer",
    ) -> dict[str, Any]:
        perms = permissions or ["read_hydrate"]
        ws = self.get_workstream(workstream_id)
        if ws is None:
            # Inv-Scope: do not reveal whether id exists vs unauthorized
            raise KeyError("not found")
        if not self.has_permission(workstream_id, issuer_principal_id, "admin"):
            raise KeyError("not found")

        if grantee_x25519_public_b64 and grantee_public_key_b64:
            self.upsert_known_principal(
                principal_id=grantee_principal_id,
                display_name=grantee_name,
                public_key_b64=grantee_public_key_b64,
                x25519_public_b64=grantee_x25519_public_b64,
            )

        now = utc_now()
        cap_id = new_id("cap")
        cap = {
            "schema_version": SCHEMA_VERSION,
            "id": cap_id,
            "grantee_principal_id": grantee_principal_id,
            "issuer_principal_id": issuer_principal_id,
            "scope": {
                "type": "workstream",
                "workstream_id": workstream_id,
                "handoff_id": None,
            },
            "permissions": perms,
            "created_at": now,
            "expires_at": None,
            "revoked_at": None,
            "issuer_signature": "local",
        }
        with self.connection() as conn:
            # revoke prior active caps for same grantee+ws then insert
            prior = conn.execute(
                """
                SELECT id, record_json FROM capabilities
                WHERE workstream_id = ? AND grantee_principal_id = ?
                  AND revoked_at IS NULL
                """,
                (workstream_id, grantee_principal_id),
            ).fetchall()
            for row in prior:
                rec = json.loads(row["record_json"])
                rec["revoked_at"] = now
                conn.execute(
                    "UPDATE capabilities SET revoked_at = ?, record_json = ? WHERE id = ?",
                    (now, json.dumps(rec), row["id"]),
                )
            conn.execute(
                """
                INSERT INTO capabilities(
                  id, grantee_principal_id, issuer_principal_id, workstream_id,
                  permissions_json, created_at, expires_at, revoked_at, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cap_id,
                    grantee_principal_id,
                    issuer_principal_id,
                    workstream_id,
                    json.dumps(perms),
                    now,
                    None,
                    None,
                    json.dumps(cap),
                ),
            )
            members = list(ws.get("member_principal_ids") or [])
            if grantee_principal_id not in members:
                members.append(grantee_principal_id)
                ws["member_principal_ids"] = members
                ws["updated_at"] = now
                conn.execute(
                    """
                    UPDATE workstreams
                    SET member_json = ?, updated_at = ?, record_json = ?
                    WHERE id = ?
                    """,
                    (json.dumps(members), now, json.dumps(ws), workstream_id),
                )
        return cap

    def revoke(
        self,
        *,
        workstream_id: str,
        grantee_principal_id: str,
        issuer_principal_id: str,
    ) -> dict[str, Any]:
        ws = self.get_workstream(workstream_id)
        if ws is None or not self.has_permission(
            workstream_id, issuer_principal_id, "admin"
        ):
            raise KeyError("not found")
        now = utc_now()
        with self.connection() as conn:
            rows = conn.execute(
                """
                SELECT id, record_json FROM capabilities
                WHERE workstream_id = ? AND grantee_principal_id = ?
                  AND revoked_at IS NULL
                """,
                (workstream_id, grantee_principal_id),
            ).fetchall()
            if not rows:
                raise KeyError("not found")
            for row in rows:
                rec = json.loads(row["record_json"])
                rec["revoked_at"] = now
                conn.execute(
                    "UPDATE capabilities SET revoked_at = ?, record_json = ? WHERE id = ?",
                    (now, json.dumps(rec), row["id"]),
                )
            # mark live handoffs superseded (reseal required)
            conn.execute(
                "UPDATE handoffs SET superseded = 1 WHERE workstream_id = ? AND superseded = 0",
                (workstream_id,),
            )
            members = [
                m
                for m in (ws.get("member_principal_ids") or [])
                if m != grantee_principal_id
            ]
            ws["member_principal_ids"] = members
            ws["updated_at"] = now
            conn.execute(
                """
                UPDATE workstreams
                SET member_json = ?, updated_at = ?, record_json = ?
                WHERE id = ?
                """,
                (json.dumps(members), now, json.dumps(ws), workstream_id),
            )
        return {"revoked": grantee_principal_id, "workstream_id": workstream_id, "at": now}

    def has_permission(
        self, workstream_id: str, principal_id: str, permission: str
    ) -> bool:
        with self.connection() as conn:
            rows = conn.execute(
                """
                SELECT permissions_json FROM capabilities
                WHERE workstream_id = ? AND grantee_principal_id = ?
                  AND revoked_at IS NULL
                """,
                (workstream_id, principal_id),
            ).fetchall()
        for row in rows:
            perms = json.loads(row["permissions_json"])
            if permission in perms or "admin" in perms:
                return True
        return False

    def active_recipient_ids(self, workstream_id: str) -> list[str]:
        with self.connection() as conn:
            rows = conn.execute(
                """
                SELECT DISTINCT grantee_principal_id FROM capabilities
                WHERE workstream_id = ? AND revoked_at IS NULL
                """,
                (workstream_id,),
            ).fetchall()
        return sorted(r["grantee_principal_id"] for r in rows)

    def get_working_state(self, workstream_id: str) -> dict[str, Any] | None:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM working_states WHERE workstream_id = ?",
                (workstream_id,),
            ).fetchone()
        return json.loads(row["record_json"]) if row else None

    def upsert_working_state(self, record: dict[str, Any]) -> dict[str, Any]:
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO working_states(id, workstream_id, record_json, updated_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(workstream_id) DO UPDATE SET
                  record_json=excluded.record_json,
                  updated_at=excluded.updated_at
                """,
                (
                    record["id"],
                    record["workstream_id"],
                    json.dumps(record),
                    record["updated_at"],
                ),
            )
        return record

    def ranked_active_anchors(
        self, *, workstream_id: str | None = None, shareable_only: bool = False
    ) -> list[dict[str, Any]]:
        anchors = self.list_anchors(active_only=True)
        if workstream_id is not None:
            anchors = [
                a
                for a in anchors
                if a.get("workstream_id") in (workstream_id, None)
            ]
        if shareable_only:
            anchors = [a for a in anchors if a.get("shareable")]
        anchors.sort(
            key=lambda a: (
                self.SURVIVAL_RANK.get(a["kind"], 99),
                -float(a.get("importance", 0)),
                a.get("created_at", ""),
            )
        )
        return anchors

    def record_handoff(
        self,
        *,
        handoff_id: str,
        workstream_id: str,
        epoch: int,
        pack_path: str,
        from_principal_id: str,
        recipient_ids: list[str],
        payload: dict[str, Any],
    ) -> None:
        now = utc_now()
        with self.connection() as conn:
            conn.execute(
                "UPDATE handoffs SET superseded = 1 WHERE workstream_id = ? AND superseded = 0",
                (workstream_id,),
            )
            conn.execute(
                """
                INSERT INTO handoffs(
                  id, workstream_id, epoch, pack_path, created_at,
                  from_principal_id, recipient_json, superseded, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?)
                """,
                (
                    handoff_id,
                    workstream_id,
                    epoch,
                    pack_path,
                    now,
                    from_principal_id,
                    json.dumps(recipient_ids),
                    json.dumps(payload),
                ),
            )

    def next_handoff_epoch(self, workstream_id: str) -> int:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT MAX(epoch) AS m FROM handoffs WHERE workstream_id = ?",
                (workstream_id,),
            ).fetchone()
        current = row["m"] if row and row["m"] is not None else 0
        return int(current) + 1

