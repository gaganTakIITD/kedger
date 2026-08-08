"""Compile HandoffPack from active Anchors and seal/hydrate `.kxp` packs."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
from typing import Any

from nacl.signing import VerifyKey

from kedger import SCHEMA_VERSION
from kedger.crypto.kxp import (
    KxpError,
    LocalIdentity,
    Recipient,
    open_kxp,
    seal_kxp,
)
from kedger.ids import new_id
from kedger.keys.principal import Principal
from kedger.store.db import Store, utc_now
from kedger.store.paths import project_dir


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
    max_bytes: int = 32768,
    include_shared: bool = False,
) -> dict[str, Any]:
    """Build structured HandoffPack plaintext from active Anchors (+ working)."""
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
    episodes = store.list_episodes(ws_id, limit=3)
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
    pack["anchors"] = selected
    # Trim older episodes if still over budget
    while True:
        raw = json.dumps(pack, sort_keys=True, separators=(",", ":")).encode("utf-8")
        if len(raw) <= max_bytes or not pack["episode_digests"]:
            break
        dropped.append(pack["episode_digests"][-1]["id"])
        pack["episode_digests"] = pack["episode_digests"][:-1]
    pack["budget"]["dropped"] = dropped
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

    pack = compile_handoff_pack(
        store,
        workstream=ws,
        principal=principal,
        include_shared=include_shared,
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

    packs_dir = project_dir(store.repo_fingerprint) / "packs" / ws["id"]
    packs_dir.mkdir(parents=True, exist_ok=True)
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
) -> dict[str, Any]:
    """
    Authorized hydrate only.

    Any failure (missing file, not a recipient, bad crypto) → KxpError('pack not found')
    so CLI can return 404 without an existence oracle.
    """
    try:
        blob = pack_path.read_bytes()
    except OSError as e:
        raise KxpError("pack not found") from e

    identity = _principal_to_identity(principal)
    # Peek is intentionally not done — open_kxp already collapses errors.
    # Resolve sender verify key from known principals when possible.
    opened = None
    # First attempt with self-trust if sender is self; open_kxp handles that.
    # For peer packs, supply trusted key from store.
    try:
        # Temporary open via raw parse of header for sender id would be an oracle
        # if we branched on errors — open_kxp already returns uniform error.
        # Provide known verify keys by trying store lookup inside a wrapper:
        opened = _open_with_store_trust(
            blob, store=store, identity=identity, principal=principal, trusted_keys=trusted_keys
        )
    except KxpError:
        raise

    payload = opened["payload"]
    # Crypto recipient membership is the pack-epoch capability gate.
    # If the workstream exists locally and the principal is explicitly denied
    # (no active cap while others exist), treat as 404 (Inv-Scope).
    ws_id = payload.get("workstream_id")
    if ws_id and store.get_workstream(ws_id) is not None:
        recipients = store.active_recipient_ids(ws_id)
        if recipients and principal.principal_id not in recipients:
            raise KxpError("pack not found")

    # Apply working state (ephemeral render path — not markdown SoT)
    working = payload.get("working")
    if isinstance(working, dict) and working.get("workstream_id"):
        store.upsert_working_state(working)

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
