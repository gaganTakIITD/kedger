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
from kedger.constants import (
    FILES_IN_FLIGHT_MAX,
    L0_DELAY_K,
    L0_FLUSH_RATIO,
    L0_MAX_AGE_HOURS,
    L0_MAX_ROWS_PER_WORKSTREAM,
    L0_WARN_RATIO,
    WORKING_MAX_BYTES,
)
from kedger.ids import new_id
from kedger.redact.denoise import denoise_summary
from kedger.redact import redact_text
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

                CREATE TABLE IF NOT EXISTS entities (
                  id TEXT PRIMARY KEY,
                  entity_type TEXT NOT NULL,
                  name TEXT NOT NULL,
                  normalized_key TEXT NOT NULL,
                  aliases_json TEXT NOT NULL DEFAULT '[]',
                  created_at TEXT NOT NULL,
                  updated_at TEXT NOT NULL,
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS episodes (
                  id TEXT PRIMARY KEY,
                  workstream_id TEXT NOT NULL,
                  time_start TEXT NOT NULL,
                  time_end TEXT NOT NULL,
                  summary TEXT NOT NULL,
                  created_at TEXT NOT NULL,
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS evidence (
                  id TEXT PRIMARY KEY,
                  supports_anchor_id TEXT NOT NULL,
                  snippet TEXT NOT NULL,
                  source_ref TEXT NOT NULL,
                  weight REAL NOT NULL,
                  created_at TEXT NOT NULL,
                  visibility TEXT NOT NULL,
                  record_json TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS promotion_candidates (
                  id TEXT PRIMARY KEY,
                  workstream_id TEXT,
                  tier TEXT NOT NULL,
                  kind TEXT NOT NULL,
                  statement TEXT NOT NULL,
                  status TEXT NOT NULL,
                  heat REAL NOT NULL DEFAULT 0,
                  recurrence INTEGER NOT NULL DEFAULT 0,
                  created_at TEXT NOT NULL,
                  record_json TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_anchors_status ON anchors(status);
                CREATE INDEX IF NOT EXISTS idx_edges_type ON edges(edge_type);
                CREATE INDEX IF NOT EXISTS idx_obs_ts ON observations(ts);
                CREATE INDEX IF NOT EXISTS idx_caps_ws ON capabilities(workstream_id);
                CREATE INDEX IF NOT EXISTS obs_ws_ts ON observations(workstream_id, ts);
                CREATE INDEX IF NOT EXISTS anc_ws_status_kind ON anchors(workstream_id, status, kind);
                CREATE INDEX IF NOT EXISTS anc_valid ON anchors(valid_at, invalid_at);
                CREATE UNIQUE INDEX IF NOT EXISTS ent_repo_key ON entities(normalized_key);
                CREATE INDEX IF NOT EXISTS edge_src_type ON edges(from_id, edge_type);
                CREATE INDEX IF NOT EXISTS cap_grantee_ws ON capabilities(grantee_principal_id, workstream_id);
                CREATE INDEX IF NOT EXISTS ep_ws_created ON episodes(workstream_id, created_at);
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
        # Redact before Anchor persist; retain hit flags for share gate canary
        stmt_red = redact_text(statement)
        statement = stmt_red.text
        reason_hits: list[str] = []
        if reason is not None:
            reason_red = redact_text(reason)
            reason = reason_red.text
            reason_hits = reason_red.hits
        secret_hits = sorted(set(stmt_red.hits + reason_hits))
        if shareable and secret_hits:
            raise ValueError(
                f"cannot mark shareable: redaction gate hits {', '.join(secret_hits)}"
            )

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
            "secret_hits": secret_hits,
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

    def upsert_anchor_record(self, record: dict[str, Any]) -> dict[str, Any]:
        """Insert a full Anchor record (pack import). No-op if id already exists."""
        anc_id = record["id"]
        if self.get_anchor(anc_id) is not None:
            return self.get_anchor(anc_id)  # type: ignore[return-value]
        kind = record.get("kind") or "gotcha"
        statement = (record.get("statement") or "").strip()
        if not statement:
            raise ValueError("statement must be non-empty")
        reason = record.get("reason")
        status = record.get("status") or "active"
        visibility = record.get("visibility") or "workstream_private"
        importance = float(record.get("importance") or 0.5)
        now = utc_now()
        created = record.get("created_at") or now
        updated = record.get("updated_at") or now
        valid_at = record.get("valid_at") or created
        workstream_id = record.get("workstream_id")
        shareable = bool(record.get("shareable"))
        about = record.get("about") or []
        supersedes = record.get("supersedes") or []
        provenance = record.get("provenance") or {}
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
                    statement[:240],
                    reason,
                    status,
                    visibility,
                    importance,
                    valid_at,
                    record.get("invalid_at"),
                    created,
                    updated,
                    json.dumps(supersedes),
                    record.get("superseded_by"),
                    json.dumps(provenance),
                    1 if shareable else 0,
                    workstream_id,
                    json.dumps(about),
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

    def get_anchor_scoped(
        self,
        anchor_id: str,
        *,
        principal_id: str,
        require_shared: bool = False,
    ) -> dict[str, Any]:
        """Inv-Scope GET-by-id: missing/unauthorized → KeyError('not found')."""
        anc = self.get_anchor(anchor_id)
        if anc is None:
            raise KeyError("not found")
        if require_shared or anc.get("shareable"):
            if anc.get("shareable") and anc.get("visibility") == "repo_shared_safe":
                return anc
            if require_shared:
                raise KeyError("not found")
        ws_id = anc.get("workstream_id")
        if ws_id is None:
            # repo-global private — only provenance actor
            prov = anc.get("provenance") or {}
            if prov.get("actor_principal_id") != principal_id:
                raise KeyError("not found")
            return anc
        if not self.has_permission(ws_id, principal_id, "read_hydrate"):
            raise KeyError("not found")
        return anc

    def list_shared_anchors(self) -> list[dict[str, Any]]:
        with self.connection() as conn:
            rows = conn.execute(
                "SELECT record_json FROM anchors "
                "WHERE shareable = 1 AND status = 'active' ORDER BY created_at ASC"
            ).fetchall()
        return [json.loads(r["record_json"]) for r in rows]

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
        """Append an L0 observation from hook JSON (redact-before-persist)."""
        now = utc_now()
        obs_id = payload.get("id") or new_id("obs")
        obs_type = payload.get("type") or payload.get("event") or "note"
        raw_summary = (
            payload.get("summary")
            or payload.get("text")
            or payload.get("message")
            or json.dumps(payload, sort_keys=True)[:200]
        )
        red = redact_text(str(raw_summary))
        summary = denoise_summary(red.text) or red.text
        # Never persist raw secrets in payload_json — store redacted copy
        safe_payload = dict(payload)
        if "summary" in safe_payload:
            safe_payload["summary"] = summary
        if "text" in safe_payload and isinstance(safe_payload["text"], str):
            safe_payload["text"] = redact_text(safe_payload["text"]).text
        if "message" in safe_payload and isinstance(safe_payload["message"], str):
            safe_payload["message"] = redact_text(safe_payload["message"]).text
        session_id = payload.get("session_id") or "hook"
        visibility = payload.get("visibility") or "private_raw"
        importance = float(payload.get("importance", 0.5))
        workstream_id = payload.get("workstream_id")
        record = {
            "schema_version": SCHEMA_VERSION,
            "id": obs_id,
            "type": obs_type,
            "ts": payload.get("ts") or now,
            "repo_fingerprint": self.repo_fingerprint,
            "workstream_id": workstream_id,
            "session_id": session_id,
            "actor_principal_id": payload.get("actor_principal_id") or principal_id,
            "agent_tool": payload.get("agent_tool") or "other",
            "summary": summary,
            "payload_ref": payload.get("payload_ref"),
            "entity_hints": payload.get("entity_hints") or [],
            "importance": importance,
            "redacted": red.redacted or bool(payload.get("redacted", False)),
            "visibility": visibility,
            "secret_hits": red.hits,
        }
        if payload.get("edit_stats"):
            record["edit_stats"] = payload["edit_stats"]
        if payload.get("lines_added") is not None:
            record["lines_added"] = payload.get("lines_added")
        if payload.get("lines_removed") is not None:
            record["lines_removed"] = payload.get("lines_removed")
        # Keep a slim payload pointer for ops compile (file edit stats, etc.)
        record["payload"] = {
            k: safe_payload[k]
            for k in (
                "file_path",
                "path",
                "files",
                "edits",
                "lines_added",
                "lines_removed",
                "edit_stats",
                "edit_count",
                "tool_name",
            )
            if k in safe_payload
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
                    workstream_id,
                    record["agent_tool"],
                    json.dumps(safe_payload),
                    json.dumps(record),
                ),
            )
        pressure = self.rotate_observations(workstream_id=workstream_id)
        record["l0_pressure"] = pressure
        # Soft-patch L1 for state-changing observations
        if obs_type in {"user_prompt", "file_edit", "note", "agent_response", "tool_result", "tool_fail"} and workstream_id:
            self.soft_patch_working(
                workstream_id=workstream_id,
                summary=summary,
                files=payload.get("files") or [
                    h.get("name")
                    for h in (payload.get("entity_hints") or [])
                    if isinstance(h, dict) and h.get("entity_type") == "file"
                ],
                session_id=session_id,
                obs_type=obs_type,
                edit_stats=payload.get("edit_stats"),
            )
        return record

    def _l0_pressure_key(self, workstream_id: str | None) -> str:
        return f"l0_pressure_events:{workstream_id or '_'}"

    def _get_meta(self, key: str, default: str = "0") -> str:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT value FROM meta WHERE key = ?", (key,)
            ).fetchone()
        return str(row["value"]) if row else default

    def _set_meta(self, key: str, value: str) -> None:
        with self.connection() as conn:
            conn.execute(
                "INSERT INTO meta(key, value) VALUES (?, ?) "
                "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
                (key, value),
            )

    def rotate_observations(self, *, workstream_id: str | None = None) -> dict[str, Any]:
        """Enforce L0 FIFO/age caps with delay-k soft-stale; return pressure stats.

        Soft-stale marks L0 rows eligible for flush-first after ``L0_DELAY_K``
        pressure boundaries at warn. Hard delete still uses warn/flush ratios.
        Anchors are never touched here.
        """
        from datetime import datetime, timedelta, timezone

        cutoff = (
            datetime.now(timezone.utc) - timedelta(hours=L0_MAX_AGE_HOURS)
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        warn_n = int(L0_MAX_ROWS_PER_WORKSTREAM * L0_WARN_RATIO)
        flush_n = int(L0_MAX_ROWS_PER_WORKSTREAM * L0_FLUSH_RATIO)
        soft_stale_marked = 0
        pressure_events = int(self._get_meta(self._l0_pressure_key(workstream_id), "0"))

        with self.connection() as conn:
            if workstream_id:
                conn.execute(
                    "DELETE FROM observations WHERE workstream_id = ? AND ts < ?",
                    (workstream_id, cutoff),
                )
                rows = conn.execute(
                    "SELECT id, record_json FROM observations "
                    "WHERE workstream_id = ? ORDER BY ts ASC",
                    (workstream_id,),
                ).fetchall()
            else:
                conn.execute("DELETE FROM observations WHERE ts < ?", (cutoff,))
                rows = conn.execute(
                    "SELECT id, record_json FROM observations ORDER BY ts ASC"
                ).fetchall()
            count = len(rows)
            flushed = 0
            warn = count >= warn_n

            if warn:
                pressure_events += 1
                # Delay-k: only after k pressure boundaries, soft-mark oldest
                # overflow zone (rows past warn capacity) — do not hard-delete yet.
                if pressure_events >= L0_DELAY_K and count > warn_n:
                    overflow = rows[: max(0, count - warn_n)]
                    now = utc_now()
                    for row in overflow:
                        rec = json.loads(row["record_json"])
                        if rec.get("soft_stale"):
                            continue
                        rec["soft_stale"] = True
                        rec["soft_stale_at"] = now
                        rec["soft_stale_reason"] = "delay_k_pressure"
                        conn.execute(
                            "UPDATE observations SET record_json = ? WHERE id = ?",
                            (json.dumps(rec), row["id"]),
                        )
                        soft_stale_marked += 1
            else:
                # Recover pressure counter when under warn (room again)
                pressure_events = 0

            if count > L0_MAX_ROWS_PER_WORKSTREAM or count >= flush_n:
                # Prefer soft_stale rows first (delay-k), then oldest FIFO
                parsed = [(r, json.loads(r["record_json"])) for r in rows]
                ordered = sorted(
                    parsed,
                    key=lambda pair: (
                        0 if pair[1].get("soft_stale") else 1,
                        pair[1].get("ts") or "",
                    ),
                )
                drop_n = max(count - L0_MAX_ROWS_PER_WORKSTREAM, count // 2)
                for row, _rec in ordered[:drop_n]:
                    conn.execute("DELETE FROM observations WHERE id = ?", (row["id"],))
                    flushed += 1

        self._set_meta(self._l0_pressure_key(workstream_id), str(pressure_events))
        return {
            "count": max(0, count - flushed),
            "warn": warn,
            "flushed": flushed,
            "max_rows": L0_MAX_ROWS_PER_WORKSTREAM,
            "soft_stale_marked": soft_stale_marked,
            "pressure_events": pressure_events,
            "delay_k": L0_DELAY_K,
        }

    def soft_patch_working(
        self,
        *,
        workstream_id: str,
        summary: str,
        files: list[str] | None = None,
        session_id: str = "hook",
        obs_type: str | None = None,
        edit_stats: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Mutable L1 UPSERT — tiny working cursor + ops activity."""
        from kedger.cognify.activity import merge_file_stat, summarize_file_edit

        existing = self.get_working_state(workstream_id)
        now = utc_now()
        if existing is None:
            record = {
                "schema_version": SCHEMA_VERSION,
                "id": new_id("wk"),
                "workstream_id": workstream_id,
                "repo_fingerprint": self.repo_fingerprint,
                "goal": summary[:200] if obs_type == "user_prompt" else "",
                "last_user_ask": summary[:240] if obs_type == "user_prompt" else "",
                "last_agent_action": summary[:240]
                if obs_type in {"agent_response", "file_edit", "tool_result"}
                else "",
                "files_in_flight": (files or [])[:FILES_IN_FLIGHT_MAX],
                "open_questions": [],
                "blockers": [],
                "active_branch": None,
                "active_anchor_ids": [],
                "activity": {
                    "schema": "kedger.activity.v1",
                    "layer": "activity",
                    "totals": {
                        "files": 0,
                        "edits": 0,
                        "lines_added": 0,
                        "lines_removed": 0,
                        "agent_turns": 0,
                        "user_turns": 0,
                        "tool_results": 0,
                        "tool_fails": 0,
                    },
                    "files": [],
                    "recent_actions": [],
                },
                "updated_at": now,
                "updated_by_session_id": session_id,
                "visibility": "workstream_private",
            }
        else:
            record = dict(existing)
            if obs_type == "user_prompt":
                record["last_user_ask"] = summary[:240]
                if not record.get("goal"):
                    record["goal"] = summary[:200]
            elif obs_type in {"agent_response", "file_edit", "tool_result", "tool_fail"}:
                record["last_agent_action"] = summary[:240]
            if files:
                merged = list(record.get("files_in_flight") or [])
                for f in files:
                    if f and f not in merged:
                        merged.append(f)
                record["files_in_flight"] = merged[:FILES_IN_FLIGHT_MAX]
            record["updated_at"] = now
            record["updated_by_session_id"] = session_id

        # Incremental ops-layer patch (full recompile happens on cognify)
        activity = dict(record.get("activity") or {})
        totals = dict(activity.get("totals") or {})
        file_map = {
            f["path"]: dict(f)
            for f in (activity.get("files") or [])
            if isinstance(f, dict) and f.get("path")
        }
        actions = list(activity.get("recent_actions") or [])
        if obs_type == "user_prompt":
            totals["user_turns"] = int(totals.get("user_turns") or 0) + 1
        elif obs_type == "agent_response":
            totals["agent_turns"] = int(totals.get("agent_turns") or 0) + 1
            if summary:
                actions.append(summary[:160])
        elif obs_type == "tool_result":
            totals["tool_results"] = int(totals.get("tool_results") or 0) + 1
            if summary:
                actions.append(f"tool: {summary[:140]}")
        elif obs_type == "tool_fail":
            totals["tool_fails"] = int(totals.get("tool_fails") or 0) + 1
            if summary:
                actions.append(f"tool_fail: {summary[:120]}")
        elif obs_type == "file_edit":
            stats = edit_stats or {
                "path": (files or [None])[0],
                "edits": 1,
                "lines_added": 0,
                "lines_removed": 0,
            }
            merge_file_stat(file_map, stats)
            actions.append(summarize_file_edit(stats))

        file_list = sorted(
            file_map.values(),
            key=lambda f: (
                -(f.get("edits") or 0),
                -((f.get("lines_added") or 0) + (f.get("lines_removed") or 0)),
                f.get("path") or "",
            ),
        )[:FILES_IN_FLIGHT_MAX]
        totals["files"] = len(file_list)
        totals["edits"] = sum(int(f.get("edits") or 0) for f in file_list)
        totals["lines_added"] = sum(int(f.get("lines_added") or 0) for f in file_list)
        totals["lines_removed"] = sum(int(f.get("lines_removed") or 0) for f in file_list)
        activity.update(
            {
                "schema": "kedger.activity.v1",
                "layer": "activity",
                "totals": totals,
                "files": file_list,
                "recent_actions": actions[-12:],
            }
        )
        record["activity"] = activity
        if file_list:
            paths = [f["path"] for f in file_list if f.get("path")]
            merged = list(dict.fromkeys((record.get("files_in_flight") or []) + paths))
            record["files_in_flight"] = merged[:FILES_IN_FLIGHT_MAX]
        return self.upsert_working_state(record)

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
        signing_key: Any | None = None,
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
        # issuer grants self admin + hydrate (signed when key available)
        self.grant(
            workstream_id=ws_id,
            grantee_principal_id=principal_id,
            issuer_principal_id=principal_id,
            permissions=["read_hydrate", "append", "admin"],
            signing_key=signing_key,
            _bootstrap=True,
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
        signing_key: Any | None = None,
        _bootstrap: bool = False,
    ) -> dict[str, Any]:
        from kedger.keys.sign import sign_capability_body

        perms = permissions or ["read_hydrate"]
        ws = self.get_workstream(workstream_id)
        if ws is None:
            # Inv-Scope: do not reveal whether id exists vs unauthorized
            raise KeyError("not found")
        if not _bootstrap and not self.has_permission(
            workstream_id, issuer_principal_id, "admin"
        ):
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
            "issuer_signature": "",
        }
        if signing_key is not None:
            cap["issuer_signature"] = sign_capability_body(signing_key, cap)
        else:
            cap["issuer_signature"] = "unsigned"
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
        files = list(record.get("files_in_flight") or [])[:FILES_IN_FLIGHT_MAX]
        record = dict(record)
        record["files_in_flight"] = files
        raw = json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")
        if len(raw) > WORKING_MAX_BYTES:
            # Trim files / questions until under budget (never drop goal)
            while len(raw) > WORKING_MAX_BYTES and record.get("files_in_flight"):
                record["files_in_flight"].pop()
                raw = json.dumps(record, sort_keys=True, separators=(",", ":")).encode(
                    "utf-8"
                )
            while len(raw) > WORKING_MAX_BYTES and record.get("open_questions"):
                record["open_questions"].pop()
                raw = json.dumps(record, sort_keys=True, separators=(",", ":")).encode(
                    "utf-8"
                )
            if len(raw) > WORKING_MAX_BYTES:
                record["last_user_ask"] = (record.get("last_user_ask") or "")[:80]
                raw = json.dumps(record, sort_keys=True, separators=(",", ":")).encode(
                    "utf-8"
                )
            if len(raw) > WORKING_MAX_BYTES:
                raise ValueError(
                    f"WorkingState exceeds {WORKING_MAX_BYTES} bytes after trim"
                )
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

    def list_observations(
        self, *, workstream_id: str | None = None
    ) -> list[dict[str, Any]]:
        with self.connection() as conn:
            if workstream_id:
                rows = conn.execute(
                    "SELECT record_json FROM observations WHERE workstream_id = ? "
                    "ORDER BY ts ASC",
                    (workstream_id,),
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT record_json FROM observations ORDER BY ts ASC"
                ).fetchall()
        return [json.loads(r["record_json"]) for r in rows]

    def latest_episode(self, workstream_id: str) -> dict[str, Any] | None:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM episodes WHERE workstream_id = ? "
                "ORDER BY created_at DESC LIMIT 1",
                (workstream_id,),
            ).fetchone()
        return json.loads(row["record_json"]) if row else None

    def list_episodes(
        self, workstream_id: str, *, limit: int = 3
    ) -> list[dict[str, Any]]:
        with self.connection() as conn:
            rows = conn.execute(
                "SELECT record_json FROM episodes WHERE workstream_id = ? "
                "ORDER BY created_at DESC LIMIT ?",
                (workstream_id, limit),
            ).fetchall()
        return [json.loads(r["record_json"]) for r in rows]

    def insert_episode(self, episode: dict[str, Any]) -> dict[str, Any]:
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO episodes(
                  id, workstream_id, time_start, time_end, summary, created_at, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    episode["id"],
                    episode["workstream_id"],
                    episode["time_start"],
                    episode["time_end"],
                    episode["summary"],
                    episode["created_at"],
                    json.dumps(episode),
                ),
            )
        return episode

    def insert_evidence(
        self,
        *,
        supports_anchor_id: str,
        snippet: str,
        source_ref: str,
        weight: float = 1.0,
        visibility: str = "workstream_private",
        evidence_id: str | None = None,
    ) -> dict[str, Any]:
        """Attach a supporting Evidence snippet to an Anchor (CoN / why path)."""
        from kedger.constants import EVIDENCE_SNIPPET_MAX

        snip = (snippet or "").strip()
        if len(snip) > EVIDENCE_SNIPPET_MAX:
            snip = snip[:EVIDENCE_SNIPPET_MAX]
        now = utc_now()
        ev_id = evidence_id or new_id("ev")
        existing = None
        with self.connection() as conn:
            row = conn.execute(
                "SELECT id FROM evidence WHERE id = ?", (ev_id,)
            ).fetchone()
            if row:
                existing = ev_id
        if existing:
            return self.get_evidence(ev_id) or {
                "id": ev_id,
                "supports_anchor_id": supports_anchor_id,
                "snippet": snip,
            }
        record = {
            "schema_version": SCHEMA_VERSION,
            "id": ev_id,
            "supports_anchor_id": supports_anchor_id,
            "snippet": snip,
            "source_ref": source_ref,
            "weight": float(weight),
            "created_at": now,
            "visibility": visibility,
        }
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO evidence(
                  id, supports_anchor_id, snippet, source_ref, weight,
                  created_at, visibility, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    ev_id,
                    supports_anchor_id,
                    snip,
                    source_ref,
                    float(weight),
                    now,
                    visibility,
                    json.dumps(record),
                ),
            )
        return record

    def get_evidence(self, evidence_id: str) -> dict[str, Any] | None:
        with self.connection() as conn:
            row = conn.execute(
                "SELECT record_json FROM evidence WHERE id = ?", (evidence_id,)
            ).fetchone()
        return json.loads(row["record_json"]) if row else None

    def list_evidence_for_anchors(
        self, anchor_ids: list[str]
    ) -> list[dict[str, Any]]:
        """Evidence rows supporting the given Anchor ids (dual-path pack/hydrate)."""
        if not anchor_ids:
            return []
        placeholders = ",".join("?" for _ in anchor_ids)
        with self.connection() as conn:
            rows = conn.execute(
                f"SELECT record_json FROM evidence "
                f"WHERE supports_anchor_id IN ({placeholders}) "
                f"ORDER BY weight DESC, created_at DESC",
                tuple(anchor_ids),
            ).fetchall()
        return [json.loads(r["record_json"]) for r in rows]

    def insert_edge(
        self,
        *,
        edge_type: str,
        from_id: str,
        to_id: str,
        workstream_id: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        now = utc_now()
        edge = {
            "schema_version": SCHEMA_VERSION,
            "id": new_id("eg"),
            "edge_type": edge_type,
            "from_id": from_id,
            "to_id": to_id,
            "repo_fingerprint": self.repo_fingerprint,
            "workstream_id": workstream_id,
            "valid_at": now,
            "invalid_at": None,
            "created_at": now,
            "meta": meta or {"weight": 1.0},
        }
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO edges(
                  id, edge_type, from_id, to_id, valid_at, invalid_at,
                  created_at, meta_json, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    edge["id"],
                    edge_type,
                    from_id,
                    to_id,
                    now,
                    None,
                    now,
                    json.dumps(edge["meta"]),
                    json.dumps(edge),
                ),
            )
        return edge

    def prune_observation_payloads(self, obs_ids: list[str]) -> int:
        """Clear payload bodies after cognify; keep provenance ids/summaries."""
        if not obs_ids:
            return 0
        n = 0
        with self.connection() as conn:
            for oid in obs_ids:
                row = conn.execute(
                    "SELECT record_json FROM observations WHERE id = ?", (oid,)
                ).fetchone()
                if not row:
                    continue
                rec = json.loads(row["record_json"])
                rec["payload_ref"] = rec.get("payload_ref") or f"pruned://{oid}"
                rec["payload_pruned"] = True
                conn.execute(
                    "UPDATE observations SET payload_json = ?, record_json = ? WHERE id = ?",
                    (json.dumps({"pruned": True}), json.dumps(rec), oid),
                )
                n += 1
        return n

    def insert_promotion_candidate(self, cand: dict[str, Any]) -> dict[str, Any]:
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO promotion_candidates(
                  id, workstream_id, tier, kind, statement, status, heat,
                  recurrence, created_at, record_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cand["id"],
                    cand.get("workstream_id"),
                    cand["tier"],
                    cand["kind"],
                    cand["statement"],
                    cand["status"],
                    float(cand.get("heat") or 0),
                    int(cand.get("recurrence") or 0),
                    cand["created_at"],
                    json.dumps(cand),
                ),
            )
        return cand

