"""Drop obvious hook noise before L0 persist (SeCom / Selective Context)."""

from __future__ import annotations

import re

# Formatter/linter/tool spam — not engineering judgment
_NOISE = re.compile(
    r"(?i)^(format(ter)? only|ran eslint|ran prettier|no changes|"
    r"applying patch|saved file|lint (passed|ok)|auto-?format)\b"
)


def denoise_summary(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return t
    if _NOISE.search(t):
        return ""
    return t
