"""Out-of-line L0 observation payloads under ~/.kedger/projects/<fp>/raw/."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from nacl.bindings import (
    crypto_aead_xchacha20poly1305_ietf_decrypt,
    crypto_aead_xchacha20poly1305_ietf_encrypt,
)
from nacl.exceptions import CryptoError

from kedger.crypto.hkdf import hkdf
from kedger.store.encryption import StoreEncryptionError
from kedger.store.paths import project_dir

RAW_REF_PREFIX = "raw://"
RAW_MAGIC = b"RAW1"
RAW_INFO = b"kedger.raw.v1/payload"
RAW_INLINE_MAX_BYTES = 512


class RawPayloadError(RuntimeError):
    """Raised when a raw payload cannot be read or written."""


def raw_dir(repo_fingerprint: str) -> Path:
    return project_dir(repo_fingerprint) / "raw"


def payload_ref(obs_id: str) -> str:
    return f"{RAW_REF_PREFIX}{obs_id}"


def parse_payload_ref(ref: str | None) -> str | None:
    if not ref or not ref.startswith(RAW_REF_PREFIX):
        return None
    obs_id = ref[len(RAW_REF_PREFIX) :].strip()
    return obs_id or None


def _payload_path(repo_fingerprint: str, obs_id: str, *, encrypted: bool) -> Path:
    suffix = ".enc" if encrypted else ".json"
    return raw_dir(repo_fingerprint) / f"{obs_id}{suffix}"


def _derive_key(store_key: bytes) -> bytes:
    return hkdf(store_key, salt=b"", info=RAW_INFO, length=32)


def should_spill_payload(data: dict[str, Any]) -> bool:
    """Spill full payload bodies to raw/ when non-trivial."""
    if not data:
        return False
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return len(encoded) > RAW_INLINE_MAX_BYTES


def write_payload(
    repo_fingerprint: str,
    obs_id: str,
    data: dict[str, Any],
    *,
    store_key: bytes | None = None,
) -> str:
    """Persist payload JSON to raw/; encrypt with store key when set."""
    directory = raw_dir(repo_fingerprint)
    directory.mkdir(parents=True, exist_ok=True)
    plaintext = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    encrypted = store_key is not None
    path = _payload_path(repo_fingerprint, obs_id, encrypted=encrypted)
    if encrypted:
        assert store_key is not None
        nonce = os.urandom(24)
        key = _derive_key(store_key)
        aad = obs_id.encode("utf-8")
        ciphertext = crypto_aead_xchacha20poly1305_ietf_encrypt(
            plaintext, aad, nonce, key
        )
        blob = RAW_MAGIC + nonce + ciphertext
    else:
        blob = plaintext
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(blob)
    except Exception:
        try:
            os.close(fd)
        except OSError:
            pass
        raise
    return payload_ref(obs_id)


def read_payload(
    repo_fingerprint: str,
    ref: str,
    *,
    store_key: bytes | None = None,
) -> dict[str, Any]:
    obs_id = parse_payload_ref(ref)
    if obs_id is None:
        raise RawPayloadError(f"invalid payload_ref: {ref!r}")
    for encrypted in (True, False):
        path = _payload_path(repo_fingerprint, obs_id, encrypted=encrypted)
        if not path.exists():
            continue
        blob = path.read_bytes()
        if encrypted:
            if store_key is None:
                raise StoreEncryptionError(
                    "encrypted raw payload requires store encryption key"
                )
            if len(blob) < len(RAW_MAGIC) + 24 + 16 or blob[:4] != RAW_MAGIC:
                raise RawPayloadError(f"corrupt encrypted raw payload at {path}")
            nonce = blob[4:28]
            ciphertext = blob[28:]
            key = _derive_key(store_key)
            try:
                plaintext = crypto_aead_xchacha20poly1305_ietf_decrypt(
                    ciphertext, obs_id.encode("utf-8"), nonce, key
                )
            except CryptoError as e:
                raise RawPayloadError(
                    f"raw payload decrypt failed at {path} (wrong store key?)"
                ) from e
        else:
            plaintext = blob
        try:
            loaded = json.loads(plaintext.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            raise RawPayloadError(f"invalid raw payload JSON at {path}") from e
        if not isinstance(loaded, dict):
            raise RawPayloadError(f"raw payload must be a JSON object at {path}")
        return loaded
    raise RawPayloadError(f"raw payload missing for {ref}")


def delete_payload(
    repo_fingerprint: str,
    ref: str | None,
) -> None:
    obs_id = parse_payload_ref(ref)
    if obs_id is None:
        return
    for encrypted in (True, False):
        path = _payload_path(repo_fingerprint, obs_id, encrypted=encrypted)
        if path.exists():
            path.unlink()


def migrate_plaintext_to_encrypted(
    repo_fingerprint: str,
    *,
    store_key: bytes,
) -> int:
    """Re-wrap existing plaintext raw/*.json payloads with store-key AEAD."""
    directory = raw_dir(repo_fingerprint)
    if not directory.is_dir():
        return 0
    migrated = 0
    for path in sorted(directory.glob("*.json")):
        obs_id = path.stem
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            raise RawPayloadError(f"invalid plaintext raw payload at {path}") from e
        if not isinstance(data, dict):
            raise RawPayloadError(f"raw payload must be a JSON object at {path}")
        write_payload(repo_fingerprint, obs_id, data, store_key=store_key)
        path.unlink()
        migrated += 1
    return migrated


def raw_encryption_label(store_key: bytes | None) -> str:
    if store_key is None:
        return "off (plaintext JSON in raw/)"
    return "on (XChaCha20-Poly1305 via store key)"
