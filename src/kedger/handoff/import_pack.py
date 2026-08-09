"""Import sealed handoff memory into the local store (cross-session transfer).

Opening a `.kxp` is not enough for the next agent: Anchors, activity, and the
zlib transcript archive must land in the durable store so `--live` / hooks work
after compact, on a peer machine, or after L0 prune.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from kedger import SCHEMA_VERSION
from kedger.handoff.transcript import (
    archive_meta,
    resolve_transcript_archive,
    write_transcript_sidecar,
)
from kedger.ids import new_id
from kedger.keys.principal import Principal
from kedger.compose.similarity import near_duplicate as _near_duplicate
from kedger.store.db import Store, utc_now
from kedger.store.paths import project_dir


def import_handoff_memory(
    store: Store,
    *,
    principal: Principal,
    payload: dict[str, Any],
    pack_path: Path | None = None,
    workstream_slug: str = "default",
) -> dict[str, Any]:
    """Merge pack layers into the local workstream.

    Returns stats: anchors_imported, anchors_skipped, activity, transcript, ws_id.
    Idempotent on anchor id — existing rows are left alone.
    """
    ws = store.ensure_workstream(
        slug=workstream_slug,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    ws_id = ws["id"]
    now = utc_now()

    anchors_in = list(payload.get("anchors") or [])
    imported = 0
    skipped = 0
    for anc in anchors_in:
        if not isinstance(anc, dict) or not anc.get("statement"):
            skipped += 1
            continue
        anc_id = anc.get("id") or new_id("anc")
        existing = store.get_anchor(anc_id)
        if existing is not None:
            skipped += 1
            continue
        # Same statement+kind already active on this workstream → skip duplicate
        dup = next(
            (
                a
                for a in store.ranked_active_anchors(workstream_id=ws_id)
                if a.get("kind") == anc.get("kind")
                and _near_duplicate(a.get("statement") or "", anc.get("statement") or "")
            ),
            None,
        )
        if dup is not None:
            skipped += 1
            continue
        record = dict(anc)
        record["id"] = anc_id
        record["schema_version"] = record.get("schema_version") or SCHEMA_VERSION
        record["status"] = "active"
        record["workstream_id"] = ws_id
        record["repo_fingerprint"] = store.repo_fingerprint
        record["updated_at"] = now
        record.setdefault("created_at", now)
        record.setdefault("valid_at", now)
        record.setdefault("visibility", "workstream_private")
        record.setdefault("shareable", False)
        record.setdefault("importance", 0.85)
        record.setdefault("about", [])
        record.setdefault("supersedes", [])
        record.setdefault("superseded_by", None)
        record.setdefault("invalid_at", None)
        prov = dict(record.get("provenance") or {})
        prov["source"] = "pack_import"
        prov["handoff_id"] = payload.get("id")
        prov["imported_at"] = now
        prov["actor_principal_id"] = principal.principal_id
        prov["workstream_id"] = ws_id
        prov["repo_fingerprint"] = store.repo_fingerprint
        record["provenance"] = prov
        store.upsert_anchor_record(record)
        imported += 1

    # Dual-path Evidence: import fidelity snippets for packed Anchors
    evidence_in = list(payload.get("evidence") or [])
    evidence_imported = 0
    evidence_skipped = 0
    for ev in evidence_in:
        if not isinstance(ev, dict) or not ev.get("snippet"):
            evidence_skipped += 1
            continue
        aid = ev.get("supports_anchor_id")
        if not aid or store.get_anchor(aid) is None:
            evidence_skipped += 1
            continue
        try:
            store.insert_evidence(
                supports_anchor_id=str(aid),
                snippet=str(ev.get("snippet") or ""),
                source_ref=str(ev.get("source_ref") or f"pack:{payload.get('id')}"),
                weight=float(ev.get("weight") or 1.0),
                evidence_id=ev.get("id"),
            )
            evidence_imported += 1
        except Exception:  # noqa: BLE001
            evidence_skipped += 1

    # Resolve zlib transcript (inline or sidecar next to pack)
    sidecar_root = pack_path.parent if pack_path is not None else None
    archive = resolve_transcript_archive(payload, sidecar_root=sidecar_root)
    tmeta = archive_meta(archive) or payload.get("transcript_meta")

    # Persist pack + HEAD + transcript under local packs dir so sessionStart
    # auto-import can recover after a later empty-Anchor boot.
    packs_dir = project_dir(store.repo_fingerprint) / "packs" / ws_id
    packs_dir.mkdir(parents=True, exist_ok=True)
    local_sidecar = None
    local_pack = None
    handoff_id = payload.get("id") or new_id("hf")
    if pack_path is not None and Path(pack_path).exists():
        local_pack_path = packs_dir / f"{handoff_id}.kxp"
        try:
            if Path(pack_path).resolve() != local_pack_path.resolve():
                shutil.copy2(pack_path, local_pack_path)
            else:
                local_pack_path = Path(pack_path)
            (packs_dir / "HEAD").write_text(handoff_id + "\n", encoding="utf-8")
            local_pack = str(local_pack_path)
        except OSError:
            local_pack = None
    if archive and archive.get("blob_b64"):
        local_name = f"{handoff_id}.transcript.json"
        write_transcript_sidecar(packs_dir / local_name, archive)
        local_sidecar = local_name
        if tmeta is None:
            tmeta = archive_meta(archive) or {}
        else:
            tmeta = dict(tmeta)
        tmeta["sidecar"] = local_sidecar
        tmeta["inline"] = False

    activity = payload.get("activity")
    working_src = payload.get("working") if isinstance(payload.get("working"), dict) else {}
    working = store.get_working_state(ws_id) or {
        "schema_version": SCHEMA_VERSION,
        "id": new_id("wk"),
        "workstream_id": ws_id,
        "repo_fingerprint": store.repo_fingerprint,
        "goal": "",
        "last_user_ask": "",
        "files_in_flight": [],
        "open_questions": [],
        "blockers": [],
        "active_branch": None,
        "active_anchor_ids": [],
        "updated_at": now,
        "updated_by_session_id": "pack_import",
        "visibility": "workstream_private",
    }
    working = dict(working)
    working["workstream_id"] = ws_id
    working["repo_fingerprint"] = store.repo_fingerprint
    working["updated_at"] = now
    working["updated_by_session_id"] = "pack_import"
    # Prefer pack working cursor fields when present
    for key in (
        "goal",
        "last_user_ask",
        "last_agent_action",
        "files_in_flight",
        "open_questions",
        "blockers",
        "active_branch",
    ):
        if working_src.get(key):
            working[key] = working_src[key]
    if activity:
        working["activity"] = activity
        paths = [
            f["path"]
            for f in (activity.get("files") or [])
            if isinstance(f, dict) and f.get("path")
        ]
        if paths:
            merged = list(
                dict.fromkeys((working.get("files_in_flight") or []) + paths)
            )
            working["files_in_flight"] = merged[:40]
    if tmeta:
        working["transcript_meta"] = tmeta
    # Keep imported handoff pointer for transcript CLI resolve
    working["last_imported_handoff_id"] = payload.get("id")
    active_ids = [a["id"] for a in store.ranked_active_anchors(workstream_id=ws_id)[:20]]
    working["active_anchor_ids"] = active_ids
    store.upsert_working_state(working)

    # Optional episode digest so list_episodes / seal still see transfer context
    if payload.get("episode_digests") or archive or activity:
        ep = {
            "schema_version": SCHEMA_VERSION,
            "id": new_id("ep"),
            "repo_fingerprint": store.repo_fingerprint,
            "workstream_id": ws_id,
            "session_ids": payload.get("session_ids") or [],
            "time_start": now,
            "time_end": now,
            "branch": working.get("active_branch"),
            "summary": (
                f"Imported handoff {handoff_id} "
                f"(anchors={imported}, activity={'yes' if activity else 'no'}, "
                f"transcript={'yes' if archive else 'no'})"
            )[:1200],
            "failed_approaches": [],
            "next_steps": [],
            "files_touched": list(working.get("files_in_flight") or [])[:40],
            "anchor_ids": active_ids,
            "entity_ids": [],
            "observation_span": {"from_ts": now, "to_ts": now, "count": 0},
            "salient_evidence_ids": [],
            "importance": 0.7,
            "visibility": "workstream_private",
            "created_at": now,
            "heat": 1.0,
            "boundary": {"kind": "hard", "reason": "pack_import"},
            "digest_v1": True,
            "activity": activity,
            "transcript": archive,
            "transcript_meta": tmeta,
            "layers": {
                "base": "anchors",
                "activity": "agent_ops" if activity else "none",
                "transcript": "zlib_archive" if archive else "none",
            },
            "imported_from_handoff_id": handoff_id,
        }
        store.insert_episode(ep)

    return {
        "workstream_id": ws_id,
        "workstream_slug": workstream_slug,
        "anchors_imported": imported,
        "anchors_skipped": skipped,
        "evidence_imported": evidence_imported,
        "evidence_skipped": evidence_skipped,
        "activity": bool(activity),
        "transcript": bool(archive),
        "transcript_meta": tmeta,
        "local_sidecar": local_sidecar,
        "local_pack": local_pack,
        "handoff_id": handoff_id,
    }
