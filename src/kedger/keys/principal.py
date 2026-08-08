"""Local Ed25519 + X25519 principal keys under ~/.kedger/keys/."""

from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
from pathlib import Path

from nacl.public import PrivateKey
from nacl.signing import SigningKey, VerifyKey

from kedger.ids import new_id
from kedger.store.db import utc_now
from kedger.store.paths import keys_dir


class KeysError(RuntimeError):
    pass


@dataclass
class Principal:
    principal_id: str
    name: str
    public_key_b64: str
    x25519_public_b64: str
    created_at: str
    signing_key: SigningKey | None = None
    x25519_private: PrivateKey | None = None

    @property
    def public_key_hex(self) -> str:
        return base64.b64decode(self.public_key_b64).hex()

    @property
    def x25519_public(self) -> bytes:
        return base64.b64decode(self.x25519_public_b64)


def _principal_path() -> Path:
    return keys_dir() / "principal.json"


def _secret_path() -> Path:
    return keys_dir() / "principal.ed25519"


def _x25519_secret_path() -> Path:
    return keys_dir() / "principal.x25519"


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


def init_principal(name: str = "default", *, force: bool = False) -> Principal:
    keys_dir().mkdir(parents=True, exist_ok=True)
    meta_path = _principal_path()
    if meta_path.exists() and not force:
        raise KeysError(
            "principal already exists; pass --force to rotate "
            f"(path={meta_path})"
        )

    signing = SigningKey.generate()
    x25519 = PrivateKey.generate()
    principal_id = new_id("pr")
    created = utc_now()
    public_b64 = base64.b64encode(bytes(signing.verify_key)).decode("ascii")
    x25519_pub_b64 = base64.b64encode(bytes(x25519.public_key)).decode("ascii")

    meta = {
        "schema_version": "kedger.memory.v1",
        "principal_id": principal_id,
        "name": name,
        "public_key_b64": public_b64,
        "x25519_public_b64": x25519_pub_b64,
        "key_type": "ed25519+x25519",
        "created_at": created,
    }
    _write_secret(_secret_path(), bytes(signing))
    _write_secret(_x25519_secret_path(), bytes(x25519))
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    try:
        os.chmod(meta_path, 0o600)
    except OSError:
        pass

    return Principal(
        principal_id=principal_id,
        name=name,
        public_key_b64=public_b64,
        x25519_public_b64=x25519_pub_b64,
        created_at=created,
        signing_key=signing,
        x25519_private=x25519,
    )


def load_principal(*, require_secret: bool = False) -> Principal:
    meta_path = _principal_path()
    if not meta_path.exists():
        raise KeysError(
            "no principal found; run `kedger keys init` first "
            f"(looked in {meta_path})"
        )
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    signing: SigningKey | None = None
    x25519: PrivateKey | None = None

    secret_path = _secret_path()
    if secret_path.exists():
        raw = secret_path.read_bytes()
        if len(raw) != 32:
            raise KeysError(f"corrupt signing key at {secret_path}")
        signing = SigningKey(raw)
        expected = base64.b64encode(bytes(signing.verify_key)).decode("ascii")
        if expected != meta.get("public_key_b64"):
            raise KeysError("principal public key does not match secret key")
    elif require_secret:
        raise KeysError(f"missing signing key at {secret_path}")

    x_path = _x25519_secret_path()
    if x_path.exists():
        raw = x_path.read_bytes()
        if len(raw) != 32:
            raise KeysError(f"corrupt x25519 key at {x_path}")
        x25519 = PrivateKey(raw)
        expected_x = base64.b64encode(bytes(x25519.public_key)).decode("ascii")
        if meta.get("x25519_public_b64") and expected_x != meta["x25519_public_b64"]:
            raise KeysError("principal x25519 public key does not match secret")
    elif require_secret:
        raise KeysError(f"missing x25519 key at {x_path}")

    # migrate older Phase A principals that lack X25519
    if x25519 is None and signing is not None:
        x25519 = PrivateKey.generate()
        meta["x25519_public_b64"] = base64.b64encode(bytes(x25519.public_key)).decode(
            "ascii"
        )
        meta["key_type"] = "ed25519+x25519"
        _write_secret(x_path, bytes(x25519))
        meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    if "x25519_public_b64" not in meta:
        raise KeysError("principal missing x25519 public key; re-run keys init --force")

    return Principal(
        principal_id=meta["principal_id"],
        name=meta.get("name", "default"),
        public_key_b64=meta["public_key_b64"],
        x25519_public_b64=meta["x25519_public_b64"],
        created_at=meta.get("created_at", ""),
        signing_key=signing,
        x25519_private=x25519,
    )


def verify_key_from_principal(principal: Principal) -> VerifyKey:
    return VerifyKey(base64.b64decode(principal.public_key_b64))


def export_recipient(principal: Principal) -> dict[str, str]:
    return {
        "principal_id": principal.principal_id,
        "name": principal.name,
        "public_key_b64": principal.public_key_b64,
        "x25519_public_b64": principal.x25519_public_b64,
    }
