"""Prefixed ULID identifiers for kedger.memory.v1."""

from __future__ import annotations

import os
import re
import time

_CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
_ID_RE = re.compile(r"^[a-z]{2,4}_[0-9A-HJKMNP-TV-Z]{26}$")


def _encode_ulid(ms: int, randomness: bytes) -> str:
    if len(randomness) != 10:
        raise ValueError("ULID randomness must be 10 bytes")
    value = (ms << 80) | int.from_bytes(randomness, "big")
    chars: list[str] = []
    for _ in range(26):
        chars.append(_CROCKFORD[value & 0x1F])
        value >>= 5
    return "".join(reversed(chars))


def new_id(prefix: str) -> str:
    """Return a prefixed ULID, e.g. anc_01HXYZ..."""
    prefix = prefix.rstrip("_")
    ms = int(time.time() * 1000)
    randomness = os.urandom(10)
    return f"{prefix}_{_encode_ulid(ms, randomness)}"


def is_valid_id(value: str, prefix: str | None = None) -> bool:
    if not _ID_RE.match(value):
        return False
    if prefix is None:
        return True
    return value.startswith(prefix.rstrip("_") + "_")
