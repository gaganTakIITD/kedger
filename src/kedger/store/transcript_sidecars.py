"""Encrypted transcript sidecars under ~/.kedger/projects/<fp>/packs/."""

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

TRANSCRIPT_MAGIC = b"TRN1"
TRANSCRIPT_INFO = b"kedger.transcript.v1/sidecar"
TRANSCRIPT_PLAIN_SUFFIX = ".transcript.json"
TRANSCRIPT_ENC_SUFFIX = ".transcript.enc"


class TranscriptSidecarError(RuntimeError):
    """Raised when a transcript sidecar cannot be read or written."""


def _derive_key(store_key: bytes) -> bytes:
    return hkdf(store_key, salt=b"", info=TRANSCRIPT_INFO, length=32)


def sidecar_filename(handoff_id: str, *, encrypted: bool) -> str:
    suffix = TRANSCRIPT_ENC_SUFFIX if encrypted else TRANSCRIPT_PLAIN_SUFFIX
    return f"{handoff_id}{suffix}"


def alternate_sidecar_path(path: Path) -> Path | None:
    name = path.name
    if name.endswith(TRANSCRIPT_PLAIN_SUFFIX):
        return path.with_name(name[: -len(TRANSCRIPT_PLAIN_SUFFIX)] + TRANSCRIPT_ENC_SUFFIX)
    if name.endswith(TRANSCRIPT_ENC_SUFFIX):
        return path.with_name(name[: -len(TRANSCRIPT_ENC_SUFFIX)] + TRANSCRIPT_PLAIN_SUFFIX)
    return None


def sidecar_candidates(root: Path, sidecar_name: str) -> list[Path]:
    """Resolve sidecar pointer to existing files (encrypted or plaintext)."""
    primary = root / sidecar_name
    paths: list[Path] = []
    if primary.exists():
        paths.append(primary)
    alt = alternate_sidecar_path(primary)
    if alt is not None and alt.exists() and alt not in paths:
        paths.append(alt)
    return paths or [primary]


def _encrypt_blob(plaintext: bytes, *, aad: bytes, store_key: bytes) -> bytes:
    nonce = os.urandom(24)
    key = _derive_key(store_key)
    ciphertext = crypto_aead_xchacha20poly1305_ietf_encrypt(
        plaintext, aad, nonce, key
    )
    return TRANSCRIPT_MAGIC + nonce + ciphertext


def _decrypt_blob(blob: bytes, *, aad: bytes, store_key: bytes, path: Path) -> bytes:
    if len(blob) < len(TRANSCRIPT_MAGIC) + 24 + 16 or blob[:4] != TRANSCRIPT_MAGIC:
        raise TranscriptSidecarError(f"corrupt encrypted transcript sidecar at {path}")
    nonce = blob[4:28]
    ciphertext = blob[28:]
    key = _derive_key(store_key)
    try:
        return crypto_aead_xchacha20poly1305_ietf_decrypt(
            ciphertext, aad, nonce, key
        )
    except CryptoError as e:
        raise TranscriptSidecarError(
            f"transcript sidecar decrypt failed at {path} (wrong store key?)"
        ) from e


def write_sidecar(
    path: Path,
    archive: dict[str, Any],
    *,
    store_key: bytes | None = None,
) -> Path:
    """Persist transcript archive JSON; encrypt with store key when set."""
    path.parent.mkdir(parents=True, exist_ok=True)
    plaintext = json.dumps(archive, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    encrypted = store_key is not None
    if encrypted:
        assert store_key is not None
        enc_path = path
        if path.name.endswith(TRANSCRIPT_PLAIN_SUFFIX):
            enc_path = path.with_name(
                path.name[: -len(TRANSCRIPT_PLAIN_SUFFIX)] + TRANSCRIPT_ENC_SUFFIX
            )
        path = enc_path
        aad = path.name.encode("utf-8")
        blob = _encrypt_blob(plaintext, aad=aad, store_key=store_key)
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
    return path


def read_sidecar(
    path: Path,
    *,
    store_key: bytes | None = None,
) -> dict[str, Any]:
    """Load transcript archive from plaintext or encrypted sidecar."""
    candidates: list[Path] = []
    if path.exists():
        candidates.append(path)
    alt = alternate_sidecar_path(path)
    if alt is not None and alt.exists() and alt not in candidates:
        candidates.append(alt)
    if not candidates:
        raise TranscriptSidecarError(f"transcript sidecar missing at {path}")

    last_error: Exception | None = None
    for candidate in candidates:
        blob = candidate.read_bytes()
        encrypted_file = candidate.name.endswith(TRANSCRIPT_ENC_SUFFIX) or (
            len(blob) >= 4 and blob[:4] == TRANSCRIPT_MAGIC
        )
        try:
            if encrypted_file:
                if store_key is None:
                    raise StoreEncryptionError(
                        "encrypted transcript sidecar requires store encryption key"
                    )
                plaintext = _decrypt_blob(
                    blob,
                    aad=candidate.name.encode("utf-8"),
                    store_key=store_key,
                    path=candidate,
                )
            else:
                plaintext = blob
            loaded = json.loads(plaintext.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            raise TranscriptSidecarError(
                f"invalid transcript sidecar JSON at {candidate}"
            ) from e
        except StoreEncryptionError:
            raise
        except TranscriptSidecarError as e:
            last_error = e
            continue
        if not isinstance(loaded, dict):
            raise TranscriptSidecarError(
                f"transcript sidecar must be a JSON object at {candidate}"
            )
        return loaded
    if last_error is not None:
        raise last_error
    raise TranscriptSidecarError(f"transcript sidecar missing at {path}")


def export_plaintext_sidecar(
    src: Path,
    dst: Path,
    *,
    store_key: bytes | None = None,
) -> Path:
    """Write a plaintext sidecar for pack export / peer send."""
    archive = read_sidecar(src, store_key=store_key)
    return write_sidecar(dst, archive, store_key=None)


def migrate_plaintext_to_encrypted(
    repo_fingerprint: str,
    *,
    store_key: bytes,
) -> int:
    """Re-wrap existing plaintext *.transcript.json sidecars with store-key AEAD."""
    packs_root = project_dir(repo_fingerprint) / "packs"
    if not packs_root.is_dir():
        return 0
    migrated = 0
    for path in sorted(packs_root.rglob(f"*{TRANSCRIPT_PLAIN_SUFFIX}")):
        try:
            archive = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            raise TranscriptSidecarError(
                f"invalid plaintext transcript sidecar at {path}"
            ) from e
        if not isinstance(archive, dict):
            raise TranscriptSidecarError(
                f"transcript sidecar must be a JSON object at {path}"
            )
        write_sidecar(path, archive, store_key=store_key)
        path.unlink()
        migrated += 1
    return migrated


def transcript_sidecar_encryption_label(store_key: bytes | None) -> str:
    if store_key is None:
        return "off (plaintext JSON in packs/)"
    return "on (XChaCha20-Poly1305 via store key)"
