"""Agent hook helpers and install packs."""

from __future__ import annotations

from kedger.hooks.install_packs import (
    detect_repo_root,
    hook_packs_root,
    install_hook_packs,
)
from kedger.hooks.normalize import normalize_hook_event

__all__ = [
    "detect_repo_root",
    "hook_packs_root",
    "install_hook_packs",
    "normalize_hook_event",
]
