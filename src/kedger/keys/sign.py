"""Ed25519 signatures for Capability records and similar attestations."""

from __future__ import annotations

import base64
import hashlib
import json
from typing import Any

from nacl.signing import SigningKey, VerifyKey


def canonical_bytes(obj: dict[str, Any]) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sign_capability_body(signing_key: SigningKey, body: dict[str, Any]) -> str:
    """Sign capability fields excluding issuer_signature itself."""
    material = {k: v for k, v in body.items() if k != "issuer_signature"}
    digest = hashlib.sha256(canonical_bytes(material)).digest()
    sig = signing_key.sign(b"kedger.cap.v1\0" + digest).signature
    return base64.b64encode(sig).decode("ascii")


def verify_capability_signature(
    verify_key: VerifyKey, body: dict[str, Any], signature_b64: str
) -> bool:
    material = {k: v for k, v in body.items() if k != "issuer_signature"}
    digest = hashlib.sha256(canonical_bytes(material)).digest()
    try:
        verify_key.verify(
            b"kedger.cap.v1\0" + digest, base64.b64decode(signature_b64.encode("ascii"))
        )
        return True
    except Exception:  # noqa: BLE001
        return False
