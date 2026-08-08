"""Kedger home / project path resolution."""

from __future__ import annotations

import os
from pathlib import Path


def kedger_home() -> Path:
    override = os.environ.get("KEDGER_HOME")
    if override:
        return Path(override).expanduser().resolve()
    return (Path.home() / ".kedger").resolve()


def keys_dir() -> Path:
    return kedger_home() / "keys"


def project_dir(repo_fingerprint: str) -> Path:
    return kedger_home() / "projects" / repo_fingerprint


def store_path(repo_fingerprint: str) -> Path:
    return project_dir(repo_fingerprint) / "store.sqlite"


def ensure_layout(repo_fingerprint: str) -> Path:
    """Create private store layout; return path to store.sqlite."""
    home = kedger_home()
    (home / "keys").mkdir(parents=True, exist_ok=True)
    root = project_dir(repo_fingerprint)
    (root / "raw").mkdir(parents=True, exist_ok=True)
    (root / "packs").mkdir(parents=True, exist_ok=True)
    (root / "acl").mkdir(parents=True, exist_ok=True)
    return store_path(repo_fingerprint)
