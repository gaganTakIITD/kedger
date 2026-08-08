"""Age-shaped multi-recipient `.kxp` seal/open (Kedger-native bytes)."""

from __future__ import annotations

import base64
import hashlib
import json
import os
import struct
from dataclasses import dataclass
from typing import Any

from nacl.bindings import (
    crypto_aead_xchacha20poly1305_ietf_decrypt,
    crypto_aead_xchacha20poly1305_ietf_encrypt,
    crypto_scalarmult,
)
from nacl.exceptions import CryptoError
from nacl.public import PrivateKey
from nacl.signing import SigningKey, VerifyKey

from kedger.crypto.hkdf import hkdf

MAGIC = b"KXP1"
DOMAIN_SEP = b"kedger.kxp.v1/sign-then-encrypt\0"
WRAP_INFO = b"kedger.kxp.v1/X25519"
HEADER_MAC_INFO = b"kedger.kxp.v1/header-mac"
PACK_SCHEMA = "kedger.pack.v1"


class KxpError(RuntimeError):
    """Generic pack error — callers map unauthorized to 404 (Inv-Scope)."""


@dataclass
class Recipient:
    key_id: str  # usually principal_id
    x25519_public: bytes  # 32 bytes


@dataclass
class LocalIdentity:
    principal_id: str
    signing_key: SigningKey
    x25519_private: PrivateKey
    verify_key: VerifyKey | None = None


def _b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def _unb64(data: str) -> bytes:
    return base64.b64decode(data.encode("ascii"))


def _canonical_context(ctx: dict[str, Any]) -> bytes:
    """Deterministic JSON for signed context binding."""
    return json.dumps(ctx, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _x25519_shared(secret: PrivateKey, peer_public: bytes) -> bytes:
    return crypto_scalarmult(secret.encode(), peer_public)


def _wrap_file_key(file_key: bytes, recipient_pk: bytes) -> tuple[bytes, bytes]:
    """X25519 + HKDF + XChaCha20-Poly1305 wrap of file_key."""
    ephemeral = PrivateKey.generate()
    shared = _x25519_shared(ephemeral, recipient_pk)
    # salt binds ephemeral + recipient pks (partitioning hygiene)
    salt = bytes(ephemeral.public_key) + recipient_pk
    wrap_key = hkdf(shared, salt=salt, info=WRAP_INFO, length=32)
    nonce = os.urandom(24)
    wrapped = crypto_aead_xchacha20poly1305_ietf_encrypt(
        file_key, None, nonce, wrap_key
    )
    # store nonce || ciphertext
    return bytes(ephemeral.public_key), nonce + wrapped


def _unwrap_file_key(
    ephemeral_pk: bytes, wrapped_blob: bytes, recipient_sk: PrivateKey
) -> bytes:
    if len(wrapped_blob) < 24 + 16:
        raise KxpError("stanza too short")
    nonce, ct = wrapped_blob[:24], wrapped_blob[24:]
    shared = _x25519_shared(recipient_sk, ephemeral_pk)
    salt = ephemeral_pk + bytes(recipient_sk.public_key)
    wrap_key = hkdf(shared, salt=salt, info=WRAP_INFO, length=32)
    try:
        return crypto_aead_xchacha20poly1305_ietf_decrypt(ct, None, nonce, wrap_key)
    except CryptoError as e:
        raise KxpError("unwrap failed") from e


def _header_mac(file_key: bytes, header_without_mac: dict[str, Any]) -> bytes:
    material = _canonical_context(header_without_mac)
    mac_key = hkdf(file_key, salt=b"", info=HEADER_MAC_INFO, length=32)
    return hmac_sha256(mac_key, material)


def hmac_sha256(key: bytes, data: bytes) -> bytes:
    import hmac

    return hmac.new(key, data, hashlib.sha256).digest()


def seal_kxp(
    *,
    payload: dict[str, Any],
    context: dict[str, Any],
    sender: LocalIdentity,
    recipients: list[Recipient],
    epoch: int = 1,
) -> bytes:
    """
    Sign-then-encrypt HandoffPack into Kedger-native `.kxp` bytes.

    Pipeline (docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md):
      sig = Ed25519.Sign(sk, domain || C || hash(P))
      body = {context, payload, signature}
      file_key wrap via X25519 stanzas; payload via XChaCha20-Poly1305
    """
    if not recipients:
        raise KxpError("at least one recipient required")

    # bind sorted recipient ids into context
    recipient_ids = sorted({r.key_id for r in recipients})
    sender_pub_b64 = _b64(bytes(sender.signing_key.verify_key))
    ctx = {
        "schema_version": PACK_SCHEMA,
        "handoff_id": context["handoff_id"],
        "workstream_id": context["workstream_id"],
        "repo_fingerprint": context["repo_fingerprint"],
        "epoch": epoch,
        "created_at": context["created_at"],
        "from_principal_id": sender.principal_id,
        "from_public_key_b64": sender_pub_b64,
        "recipient_key_ids": recipient_ids,
    }
    payload_bytes = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    content_hash = "sha256:" + hashlib.sha256(payload_bytes).hexdigest()
    ctx["content_hash"] = content_hash

    to_sign = DOMAIN_SEP + _canonical_context(ctx) + hashlib.sha256(payload_bytes).digest()
    signature = sender.signing_key.sign(to_sign).signature

    body = {
        "context": ctx,
        "payload": payload,
        "signature": _b64(signature),
    }
    body_bytes = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")

    file_key = os.urandom(32)
    nonce = os.urandom(24)
    ciphertext = crypto_aead_xchacha20poly1305_ietf_encrypt(
        body_bytes, None, nonce, file_key
    )

    stanzas = []
    for r in recipients:
        eph_pk, wrapped = _wrap_file_key(file_key, r.x25519_public)
        stanzas.append(
            {
                "recipient_key_id": r.key_id,
                "ephemeral_pk_b64": _b64(eph_pk),
                "wrapped_key_b64": _b64(wrapped),
            }
        )
    # stable stanza order by recipient id
    stanzas.sort(key=lambda s: s["recipient_key_id"])

    header: dict[str, Any] = {
        "magic": "KXP1",
        "schema_version": PACK_SCHEMA,
        "handoff_id": ctx["handoff_id"],
        "workstream_id": ctx["workstream_id"],
        "repo_fingerprint": ctx["repo_fingerprint"],
        "epoch": epoch,
        "created_at": ctx["created_at"],
        "from_principal_id": sender.principal_id,
        "from_public_key_b64": sender_pub_b64,
        "recipient_key_ids": recipient_ids,
        "algo": {
            "encrypt": "X25519+XChaCha20Poly1305",
            "sign": "Ed25519",
            "kdf": "HKDF-SHA256",
            "hash": "sha256",
        },
        "content_hash": content_hash,
        "nonce_b64": _b64(nonce),
        "stanzas": stanzas,
    }
    header["header_mac_b64"] = _b64(_header_mac(file_key, header))

    header_bytes = json.dumps(header, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return MAGIC + struct.pack(">I", len(header_bytes)) + header_bytes + ciphertext


def open_kxp(
    blob: bytes,
    *,
    identity: LocalIdentity,
    trusted_sender_verify_key: VerifyKey | None = None,
) -> dict[str, Any]:
    """
    Unwrap `.kxp` if local identity is a recipient; verify header MAC + Ed25519.

    Raises KxpError on any failure (callers should surface as 404 for Inv-Scope).
    """
    try:
        return _open_kxp_inner(
            blob,
            identity=identity,
            trusted_sender_verify_key=trusted_sender_verify_key,
        )
    except (KxpError, CryptoError, KeyError, ValueError, struct.error, json.JSONDecodeError):
        # Collapse all failures — no existence/oracle differentiation
        raise KxpError("pack not found") from None


def _open_kxp_inner(
    blob: bytes,
    *,
    identity: LocalIdentity,
    trusted_sender_verify_key: VerifyKey | None,
) -> dict[str, Any]:
    if len(blob) < 8 or blob[:4] != MAGIC:
        raise KxpError("bad magic")
    (header_len,) = struct.unpack(">I", blob[4:8])
    header_bytes = blob[8 : 8 + header_len]
    ciphertext = blob[8 + header_len :]
    header = json.loads(header_bytes.decode("utf-8"))

    # Find a stanza for this principal
    stanza = None
    for s in header.get("stanzas", []):
        if s.get("recipient_key_id") == identity.principal_id:
            stanza = s
            break
    if stanza is None:
        raise KxpError("not a recipient")

    file_key = _unwrap_file_key(
        _unb64(stanza["ephemeral_pk_b64"]),
        _unb64(stanza["wrapped_key_b64"]),
        identity.x25519_private,
    )

    # Verify header MAC (strip mac field)
    mac = _unb64(header["header_mac_b64"])
    header_wo = {k: v for k, v in header.items() if k != "header_mac_b64"}
    expected = _header_mac(file_key, header_wo)
    if not hmac_compare(mac, expected):
        raise KxpError("header mac mismatch")

    nonce = _unb64(header["nonce_b64"])
    try:
        body_bytes = crypto_aead_xchacha20poly1305_ietf_decrypt(
            ciphertext, None, nonce, file_key
        )
    except CryptoError as e:
        raise KxpError("decrypt failed") from e

    body = json.loads(body_bytes.decode("utf-8"))
    ctx = body["context"]
    payload = body["payload"]
    signature = _unb64(body["signature"])

    payload_bytes = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    content_hash = "sha256:" + hashlib.sha256(payload_bytes).hexdigest()
    if content_hash != ctx.get("content_hash") or content_hash != header.get(
        "content_hash"
    ):
        raise KxpError("content hash mismatch")

    # Recipient binding: local principal must be listed
    if identity.principal_id not in ctx.get("recipient_key_ids", []):
        raise KxpError("recipient binding failed")

    to_verify = (
        DOMAIN_SEP
        + _canonical_context(ctx)
        + hashlib.sha256(payload_bytes).digest()
    )
    # Prefer explicit trust store; else header-embedded key (bound into signed ctx).
    if trusted_sender_verify_key is not None:
        verify_key = trusted_sender_verify_key
    elif ctx.get("from_public_key_b64"):
        verify_key = VerifyKey(_unb64(ctx["from_public_key_b64"]))
    elif identity.verify_key is not None:
        verify_key = identity.verify_key
    else:
        verify_key = identity.signing_key.verify_key
    # Header claim must match signed context
    if header.get("from_public_key_b64") != ctx.get("from_public_key_b64"):
        raise KxpError("sender key mismatch")
    try:
        verify_key.verify(to_verify, signature)
    except Exception as e:  # noqa: BLE001
        raise KxpError("signature invalid") from e

    return {
        "header": header,
        "context": ctx,
        "payload": payload,
    }


def hmac_compare(a: bytes, b: bytes) -> bool:
    import hmac

    return hmac.compare_digest(a, b)
