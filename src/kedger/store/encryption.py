"""Optional SQLCipher at-rest encryption for ~/.kedger store.sqlite."""

from __future__ import annotations

import base64
import json
import os
import secrets
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from kedger.store.paths import keys_dir, store_meta_path

ENCRYPTION_SQLCIPHER = "sqlcipher"
STORE_KEY_ENV = "KEDGER_STORE_KEY"
STORE_KEY_FILE = "store.key"


class StoreEncryptionError(RuntimeError):
    """Raised when encrypted store cannot be opened (fail-closed)."""


@dataclass(frozen=True)
class StoreEncryptionState:
    enabled: bool
    mode: str | None = None
    path: Path | None = None

    @property
    def label(self) -> str:
        if not self.enabled:
            return "off (plaintext SQLite)"
        return f"on ({self.mode})"


def _store_key_path() -> Path:
    return keys_dir() / STORE_KEY_FILE


def _write_secret(path: Path, data: bytes) -> None:
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
    except Exception:
        try:
            os.close(fd)
        except OSError:
            pass
        raise


def _parse_store_key(raw: str) -> bytes:
    text = raw.strip()
    if not text:
        raise StoreEncryptionError(f"{STORE_KEY_ENV} is empty")
    try:
        decoded = base64.b64decode(text, validate=True)
    except Exception:
        try:
            decoded = bytes.fromhex(text)
        except ValueError as e:
            raise StoreEncryptionError(
                f"{STORE_KEY_ENV} must be base64 or hex for 32 bytes"
            ) from e
    if len(decoded) != 32:
        raise StoreEncryptionError(
            f"{STORE_KEY_ENV} must decode to 32 bytes (got {len(decoded)})"
        )
    return decoded


def load_store_key(*, create: bool = False) -> bytes:
    """Load the store encryption key from env or ~/.kedger/keys/store.key."""
    env = os.environ.get(STORE_KEY_ENV)
    if env:
        return _parse_store_key(env)

    path = _store_key_path()
    if path.exists():
        raw = path.read_bytes()
        if len(raw) != 32:
            raise StoreEncryptionError(
                f"corrupt store key at {path} (expected 32 bytes, got {len(raw)})"
            )
        return raw

    if create:
        keys_dir().mkdir(parents=True, exist_ok=True)
        key = secrets.token_bytes(32)
        _write_secret(path, key)
        return key

    raise StoreEncryptionError(
        "store encryption key missing; set "
        f"{STORE_KEY_ENV} or run `kedger store encrypt` to create "
        f"{path}"
    )


def pragma_key_sql(key: bytes) -> str:
    """SQLCipher passphrase literal for PRAGMA key / ATTACH KEY."""
    passphrase = base64.b64encode(key).decode("ascii")
    return f"'{passphrase}'"


def read_store_meta(repo_fingerprint: str) -> dict[str, Any] | None:
    path = store_meta_path(repo_fingerprint)
    if not path.exists():
        return None
    try:
        meta = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise StoreEncryptionError(f"invalid store metadata at {path}: {e}") from e
    if not isinstance(meta, dict):
        raise StoreEncryptionError(f"invalid store metadata at {path}")
    return meta


def write_store_meta(repo_fingerprint: str, meta: dict[str, Any]) -> Path:
    path = store_meta_path(repo_fingerprint)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    return path


def sqlite_header_is_plaintext(path: Path) -> bool:
    if not path.exists():
        return True
    with path.open("rb") as f:
        header = f.read(16)
    return header.startswith(b"SQLite format 3\x00")


def encryption_state(repo_fingerprint: str, store_path: Path) -> StoreEncryptionState:
    meta = read_store_meta(repo_fingerprint)
    if meta and meta.get("encryption") == ENCRYPTION_SQLCIPHER:
        return StoreEncryptionState(
            enabled=True,
            mode=ENCRYPTION_SQLCIPHER,
            path=store_meta_path(repo_fingerprint),
        )
    if store_path.exists() and not sqlite_header_is_plaintext(store_path):
        return StoreEncryptionState(
            enabled=True,
            mode=ENCRYPTION_SQLCIPHER,
            path=store_meta_path(repo_fingerprint),
        )
    return StoreEncryptionState(enabled=False)


def _import_sqlcipher():
    try:
        from sqlcipher3 import dbapi2 as sqlcipher  # type: ignore[import-untyped]
    except ImportError as e:
        raise StoreEncryptionError(
            "sqlcipher3 is required for encrypted stores; "
            'install with `pip install "kedger[encrypted]"`'
        ) from e
    return sqlcipher


def connect_sqlite(path: Path, *, key: bytes | None = None) -> sqlite3.Connection:
    """Open a store database (plaintext or SQLCipher when key is set)."""
    if key is None:
        conn = sqlite3.connect(path)
        conn.row_factory = sqlite3.Row
    else:
        sqlcipher = _import_sqlcipher()
        conn = sqlcipher.connect(str(path))
        conn.execute(f"PRAGMA key = {pragma_key_sql(key)}")
        conn.row_factory = sqlcipher.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def verify_encrypted_open(path: Path, key: bytes) -> None:
    """Fail-closed probe: wrong/missing key must not silently open."""
    conn = connect_sqlite(path, key=key)
    try:
        conn.execute("SELECT count(*) FROM sqlite_master").fetchone()
    except Exception as e:
        raise StoreEncryptionError(
            "encrypted store open failed (wrong or missing store key)"
        ) from e
    finally:
        conn.close()


def create_encrypted_store(path: Path, key: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = connect_sqlite(path, key=key)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS _kedger_enc_init (id INTEGER PRIMARY KEY)"
        )
        conn.commit()
    finally:
        conn.close()


def migrate_plaintext_to_sqlcipher(
    store_path: Path,
    *,
    key: bytes,
    backup_suffix: str = ".plaintext.bak",
) -> Path:
    """Encrypt an existing plaintext store.sqlite in place (with backup)."""
    if not store_path.exists():
        raise StoreEncryptionError(f"store not found: {store_path}")
    if not sqlite_header_is_plaintext(store_path):
        raise StoreEncryptionError(f"store already encrypted: {store_path}")

    backup = store_path.with_name(store_path.name + backup_suffix)
    if backup.exists():
        raise StoreEncryptionError(f"backup already exists: {backup}")

    enc_path = store_path.with_suffix(".sqlite.enc.tmp")
    if enc_path.exists():
        enc_path.unlink()

    sqlcipher = _import_sqlcipher()
    conn = sqlcipher.connect(str(store_path))
    try:
        conn.execute(f"ATTACH DATABASE '{enc_path}' AS encrypted KEY {pragma_key_sql(key)}")
        conn.execute("SELECT sqlcipher_export('encrypted')")
        conn.commit()
    finally:
        conn.close()

    verify_encrypted_open(enc_path, key)
    store_path.rename(backup)
    enc_path.rename(store_path)
    return backup
