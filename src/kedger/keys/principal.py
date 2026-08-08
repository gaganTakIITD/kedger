"""Local Ed25519 principal keys under ~/.kedger/keys/."""

from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
from pathlib import Path

from nacl.signing import SigningKey, VerifyKey

from kedger.ids import new_id
from kedger.store.paths import keys_dir
from kedger.store.db import utc_now


class KeysError(RuntimeError):
    pass


@dataclass
class Principal:
    principal_id: str
    name: str
    public_key_b64: str
    created_at: str
    signing_key: SigningKey | None = None

    @property
    def public_key_hex(self) -> str:
        return base64.b64decode(self.public_key_b64).hex()


def _principal_path() -> Path:
    return keys_dir() / "principal.json"


def _secret_path() -> Path:
    return keys_dir() / "principal.ed25519"


def init_principal(name: str = "default", *, force: bool = False) -> Principal:
    keys_dir().mkdir(parents=True, exist_ok=True)
    meta_path = _principal_path()
    secret_path = _secret_path()
    if meta_path.exists() and not force:
        raise KeysError(
            "principal already exists; pass --force to rotate "
            f"(path={meta_path})"
        )

    signing = SigningKey.generate()
    verify = signing.verify_key
    principal_id = new_id("pr")
    created = utc_now()
    public_b64 = base64.b64encode(bytes(verify)).decode("ascii")

    meta = {
        "schema_version": "kedger.memory.v1",
        "principal_id": principal_id,
        "name": name,
        "public_key_b64": public_b64,
        "key_type": "ed25519",
        "created_at": created,
    }
    # write secret first with restrictive perms
    fd = os.open(
        secret_path,
        os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
        0o600,
    )
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(bytes(signing))
    except Exception:
        try:
            os.close(fd)
        except OSError:
            pass
        raise

    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    try:
        os.chmod(meta_path, 0o600)
    except OSError:
        pass

    return Principal(
        principal_id=principal_id,
        name=name,
        public_key_b64=public_b64,
        created_at=created,
        signing_key=signing,
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
    secret_path = _secret_path()
    if secret_path.exists():
        raw = secret_path.read_bytes()
        if len(raw) != 32:
            raise KeysError(f"corrupt signing key at {secret_path}")
        signing = SigningKey(raw)
        # sanity: public matches
        expected = base64.b64encode(bytes(signing.verify_key)).decode("ascii")
        if expected != meta.get("public_key_b64"):
            raise KeysError("principal public key does not match secret key")
    elif require_secret:
        raise KeysError(f"missing signing key at {secret_path}")

    return Principal(
        principal_id=meta["principal_id"],
        name=meta.get("name", "default"),
        public_key_b64=meta["public_key_b64"],
        created_at=meta.get("created_at", ""),
        signing_key=signing,
    )


def verify_key_from_principal(principal: Principal) -> VerifyKey:
    return VerifyKey(base64.b64decode(principal.public_key_b64))
