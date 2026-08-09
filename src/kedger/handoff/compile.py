"""Compile HandoffPack from active Anchors and seal/hydrate `.kxp` packs."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
from typing import Any

from nacl.signing import VerifyKey

from kedger import SCHEMA_VERSION
from kedger.constants import HANDOFF_MAX_BYTES
from kedger.crypto.kxp import (
    KxpError,
    LocalIdentity,
    Recipient,
    open_kxp,
    seal_kxp,
)
from kedger.handoff.transcript import (
    archive_meta,
    attach_transcript_for_pack,
)
from kedger.ids import new_id
from kedger.keys.principal import Principal
from kedger.store.db import Store, utc_now
from kedger.store.paths import project_dir


def _slim_episode_for_pack(ep: dict[str, Any]) -> dict[str, Any]:
    """Episode digests in packs keep meta; full zlib blob lives on pack.transcript."""
    slim = dict(ep)
    if slim.get("transcript") and isinstance(slim["transcript"], dict):
        slim["transcript_meta"] = archive_meta(slim["transcript"]) or slim.get(
            "transcript_meta"
        )
        slim.pop("transcript", None)
    return slim


def _principal_to_identity(principal: Principal) -> LocalIdentity:
    if principal.signing_key is None or principal.x25519_private is None:
        raise RuntimeError("principal secrets required for seal/hydrate")
    return LocalIdentity(
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
        x25519_private=principal.x25519_private,
        verify_key=principal.signing_key.verify_key,
    )


def compile_handoff_pack(
    store: Store,
    *,
    workstream: dict[str, Any],
    principal: Principal,
    max_bytes: int = HANDOFF_MAX_BYTES,
    include_shared: bool = False,
    purpose: str | None = None,
    sidecar_dir: Path | None = None,
) -> dict[str, Any]:
    """Build structured HandoffPack plaintext from active Anchors (+ working)."""
    from kedger.hydrate.purpose import minimize_anchors

    ws_id = workstream["id"]
    anchors = store.ranked_active_anchors(workstream_id=ws_id)
    # share_mode=explicit_only: shared facet is opt-in ranked only (anti pack-deputy)
    if include_shared:
        shared = store.ranked_active_anchors(shareable_only=True)
        seen = {a["id"] for a in anchors}
        for a in shared:
            if a["id"] not in seen:
                anchors.append(a)
                seen.add(a["id"])
    # AirGap: third_party/export packs never pull shared facet by default unless explicit
    if purpose in {"third_party", "export"}:
        include_shared = False
        anchors = store.ranked_active_anchors(workstream_id=ws_id)
    working = store.get_working_state(ws_id)
    if working is None:
        # tiny default working cursor
        working = {
            "schema_version": SCHEMA_VERSION,
            "id": new_id("wk"),
            "workstream_id": ws_id,
            "repo_fingerprint": store.repo_fingerprint,
            "goal": workstream.get("name") or workstream.get("slug") or "",
            "last_user_ask": "",
            "files_in_flight": [],
            "open_questions": [],
            "blockers": [],
            "active_branch": None,
            "active_anchor_ids": [a["id"] for a in anchors[:12]],
            "updated_at": utc_now(),
            "updated_by_session_id": "cli",
            "visibility": "workstream_private",
        }

    handoff_id = new_id("hf")
    created = utc_now()
    episodes_raw = store.list_episodes(ws_id, limit=3)
    # Prefer newest episode's full transcript for cross-session transfer
    transcript_archive = None
    for ep in episodes_raw:
        if isinstance(ep.get("transcript"), dict) and ep["transcript"].get("blob_b64"):
            transcript_archive = ep["transcript"]
            break
    episodes = [_slim_episode_for_pack(ep) for ep in episodes_raw]
    pack: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "id": handoff_id,
        "repo_fingerprint": store.repo_fingerprint,
        "workstream_id": ws_id,
        "branch": working.get("active_branch"),
        "session_ids": [],
        "from_principal_id": principal.principal_id,
        "to_scope": "workstream",
        "created_at": created,
        "parent_handoff_id": None,
        "related_handoff_ids": [],
        "relations": [],
        "anchors": [],
        "working": working,
        "episode_digests": episodes,
        # Dual-layer handoff: base=anchors, activity=agent ops (compact-safe)
        "activity": (working or {}).get("activity")
        or ((episodes_raw[0].get("activity") if episodes_raw else None)),
        "transcript": None,
        "transcript_meta": (working or {}).get("transcript_meta")
        or ((episodes_raw[0].get("transcript_meta") if episodes_raw else None)),
        "layers": {
            "base": "anchors",
            "activity": "agent_ops",
            "transcript": "pending",
        },
        "evidence": [],
        "budget": {
            "max_bytes": max_bytes,
            "used_bytes": 0,
            "dropped": [],
        },
        "content_hash": "",
    }

    dropped: list[str] = []
    selected: list[dict[str, Any]] = []
    # Drop order when over budget: evidence (already empty) → older episodes → gotchas…
    for anc in anchors:
        trial = dict(pack)
        trial["anchors"] = selected + [anc]
        raw = json.dumps(trial, sort_keys=True, separators=(",", ":")).encode("utf-8")
        if len(raw) > max_bytes and selected:
            # never drop active constraint/rejection/decision while budget remains for them
            if anc["kind"] in {"constraint", "rejection", "decision"}:
                # drop a gotcha/open_question instead if present
                for i, s in enumerate(selected):
                    if s["kind"] in {"gotcha", "open_question", "next_step"}:
                        dropped.append(s["id"])
                        selected.pop(i)
                        break
                else:
                    dropped.append(anc["id"])
                    continue
            else:
                dropped.append(anc["id"])
                continue
        selected.append(anc)
    pack["anchors"] = minimize_anchors(selected, purpose)
    pack["purpose"] = purpose
    # Trim older episodes if still over budget
    while True:
        raw = json.dumps(pack, sort_keys=True, separators=(",", ":")).encode("utf-8")
        if len(raw) <= max_bytes or not pack["episode_digests"]:
            break
        dropped.append(pack["episode_digests"][-1]["id"])
        pack["episode_digests"] = pack["episode_digests"][:-1]
    pack["budget"]["dropped"] = dropped

    # Transcript last: inline zlib if it fits; else sidecar (semantic layers win budget)
    pack = attach_transcript_for_pack(
        transcript_archive,
        pack=pack,
        max_bytes=max_bytes,
        sidecar_dir=sidecar_dir,
        handoff_id=handoff_id,
    )
    # Keep working cursor aware of transfer meta without bloating blob into L1
    if isinstance(pack.get("working"), dict) and pack.get("transcript_meta"):
        wk = dict(pack["working"])
        wk["transcript_meta"] = pack["transcript_meta"]
        pack["working"] = wk

    pack["budget"]["used_bytes"] = len(
        json.dumps(pack, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )
    core = {
        "id": pack["id"],
        "anchors": pack["anchors"],
        "working": pack["working"],
        "episode_digests": pack["episode_digests"],
        "workstream_id": pack["workstream_id"],
        "created_at": pack["created_at"],
        "transcript_meta": pack.get("transcript_meta"),
    }
    pack["content_hash"] = "sha256:" + hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return pack


def seal_handoff(
    store: Store,
    *,
    principal: Principal,
    workstream_slug: str = "default",
    output: Path | None = None,
    include_shared: bool = False,
) -> tuple[Path, dict[str, Any]]:
    """Compile + seal a `.kxp` for the workstream's current recipient set."""
    # ensure local principal is registered
    store.upsert_known_principal(
        principal_id=principal.principal_id,
        display_name=principal.name,
        public_key_b64=principal.public_key_b64,
        x25519_public_b64=principal.x25519_public_b64,
    )
    ws = store.ensure_workstream(
        slug=workstream_slug,
        principal_id=principal.principal_id,
        signing_key=principal.signing_key,
    )
    if not store.has_permission(ws["id"], principal.principal_id, "read_hydrate"):
        raise KeyError("not found")

    packs_dir = project_dir(store.repo_fingerprint) / "packs" / ws["id"]
    packs_dir.mkdir(parents=True, exist_ok=True)
    pack = compile_handoff_pack(
        store,
        workstream=ws,
        principal=principal,
        include_shared=include_shared,
        sidecar_dir=packs_dir,
    )
    recipient_ids = store.active_recipient_ids(ws["id"])
    if principal.principal_id not in recipient_ids:
        recipient_ids = sorted(set(recipient_ids) | {principal.principal_id})

    recipients: list[Recipient] = []
    for rid in recipient_ids:
        known = store.get_known_principal(rid)
        if known is None and rid == principal.principal_id:
            known = {
                "id": principal.principal_id,
                "x25519_public_b64": principal.x25519_public_b64,
            }
        if known is None or not known.get("x25519_public_b64"):
            raise RuntimeError(
                f"missing recipient key material for {rid}; "
                "grant with --recipient-file first"
            )
        recipients.append(
            Recipient(
                key_id=rid,
                x25519_public=base64.b64decode(known["x25519_public_b64"]),
            )
        )

    epoch = store.next_handoff_epoch(ws["id"])
    identity = _principal_to_identity(principal)
    context = {
        "handoff_id": pack["id"],
        "workstream_id": ws["id"],
        "repo_fingerprint": store.repo_fingerprint,
        "created_at": pack["created_at"],
    }
    blob = seal_kxp(
        payload=pack,
        context=context,
        sender=identity,
        recipients=recipients,
        epoch=epoch,
    )

    out = output or (packs_dir / f"{pack['id']}.kxp")
    out.write_bytes(blob)
    head = packs_dir / "HEAD"
    head.write_text(pack["id"] + "\n", encoding="utf-8")

    store.record_handoff(
        handoff_id=pack["id"],
        workstream_id=ws["id"],
        epoch=epoch,
        pack_path=str(out),
        from_principal_id=principal.principal_id,
        recipient_ids=[r.key_id for r in recipients],
        payload=pack,
    )
    return out, pack


def hydrate_pack(
    store: Store,
    *,
    principal: Principal,
    pack_path: Path,
    trusted_keys: dict[str, VerifyKey] | None = None,
    import_memory: bool = True,
    workstream_slug: str = "default",
) -> dict[str, Any]:
    """
    Authorized hydrate only.

    Any failure (missing file, not a recipient, bad crypto) → KxpError('pack not found')
    so CLI can return 404 without an existence oracle.

    When import_memory=True (default), merge Anchors + activity + zlib transcript
    into the local durable store so the next agent session can `--live` / hook-inject.
    """
    from kedger.handoff.import_pack import import_handoff_memory
    from kedger.handoff.transcript import resolve_transcript_archive

    try:
        blob = pack_path.read_bytes()
    except OSError as e:
        raise KxpError("pack not found") from e

    identity = _principal_to_identity(principal)
    opened = _open_with_store_trust(
        blob, store=store, identity=identity, principal=principal, trusted_keys=trusted_keys
    )

    payload = opened["payload"]
    # Crypto recipient membership is the pack-epoch capability gate.
    # If the workstream exists locally and the principal is explicitly denied
    # (no active cap while others exist), treat as 404 (Inv-Scope).
    ws_id = payload.get("workstream_id")
    if ws_id and store.get_workstream(ws_id) is not None:
        recipients = store.active_recipient_ids(ws_id)
        if recipients and principal.principal_id not in recipients:
            raise KxpError("pack not found")

    # Attach resolved transcript onto payload for callers / import
    archive = resolve_transcript_archive(payload, sidecar_root=pack_path.parent)
    if archive is not None:
        payload = dict(payload)
        payload["transcript"] = archive
        opened["payload"] = payload

    import_stats = None
    if import_memory:
        import_stats = import_handoff_memory(
            store,
            principal=principal,
            payload=payload,
            pack_path=pack_path,
            workstream_slug=workstream_slug,
        )
    else:
        # Legacy ephemeral path — working cursor only
        working = payload.get("working")
        if isinstance(working, dict) and working.get("workstream_id"):
            store.upsert_working_state(working)

    opened["import"] = import_stats
    return opened


def _open_with_store_trust(
    blob: bytes,
    *,
    store: Store,
    identity: LocalIdentity,
    principal: Principal,
    trusted_keys: dict[str, VerifyKey] | None,
) -> dict[str, Any]:
    from kedger.crypto import kxp as kxp_mod
    import json
    import struct

    # Extract sender id only after we can unwrap — so try decrypt with local key first
    # using open_kxp, but inject verify key from store when sender ≠ self.
    # Strategy: attempt unwrap path manually enough to learn sender, or pass None
    # and let open_kxp accept self; for peers pre-load all known verify keys...
    # Simplest robust approach: monkey-patch by reading header (header is not secret
    # — contains from_principal_id in clear). Header disclosure of sender id is OK;
    # Inv-Scope is about Anchor/pack *payload* existence for unauthorized parties.
    if len(blob) < 8 or blob[:4] != kxp_mod.MAGIC:
        raise KxpError("pack not found")
    (header_len,) = struct.unpack(">I", blob[4:8])
    try:
        header = json.loads(blob[8 : 8 + header_len].decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        raise KxpError("pack not found") from e

    sender_id = header.get("from_principal_id")
    verify: VerifyKey | None = None
    if trusted_keys and sender_id in trusted_keys:
        verify = trusted_keys[sender_id]
    elif sender_id == principal.principal_id:
        verify = principal.signing_key.verify_key if principal.signing_key else None
    else:
        known = store.get_known_principal(sender_id) if sender_id else None
        if known and known.get("public_key"):
            verify = VerifyKey(base64.b64decode(known["public_key"]))

    return open_kxp(blob, identity=identity, trusted_sender_verify_key=verify)
