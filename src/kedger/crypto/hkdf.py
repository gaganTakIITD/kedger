"""HKDF-SHA256 (RFC 5869) — stdlib-only for Python 3.11+."""

from __future__ import annotations

import hashlib
import hmac


def hkdf(ikm: bytes, *, salt: bytes, info: bytes, length: int = 32) -> bytes:
    if length <= 0 or length > 255 * 32:
        raise ValueError("invalid HKDF length")
    if not salt:
        salt = b"\x00" * 32
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    okm = b""
    block = b""
    counter = 1
    while len(okm) < length:
        block = hmac.new(prk, block + info + bytes([counter]), hashlib.sha256).digest()
        okm += block
        counter += 1
    return okm[:length]
