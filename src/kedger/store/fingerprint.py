"""Repo fingerprint from git remote URL (fallback toplevel/cwd)."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path


def _run_git(*args: str, cwd: Path) -> str | None:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None
    if proc.returncode != 0:
        return None
    out = proc.stdout.strip()
    return out or None


def normalize_remote_url(url: str) -> str:
    """Canonicalize common git remote URL shapes for stable fingerprints.

    Credentials / userinfo are stripped so tokens never enter fingerprints
    or status output.
    """
    u = url.strip().rstrip("/")
    if u.startswith("git@"):
        # git@host:owner/repo
        host_path = u[4:]
        if ":" in host_path:
            host, path = host_path.split(":", 1)
            u = f"{host}/{path}"
    elif "://" in u:
        # https://user:token@host/owner/repo
        _, rest = u.split("://", 1)
        if "@" in rest:
            rest = rest.rsplit("@", 1)[1]
        u = rest
    elif "@" in u and ":" in u:
        # user@host:owner/repo (non-git@ form)
        u = u.split("@", 1)[1].replace(":", "/", 1)
    u = u.lower().rstrip("/")
    if u.endswith(".git"):
        u = u[: -len(".git")]
    return u


def repo_fingerprint(cwd: Path | None = None) -> str:
    """
    Fingerprint for the current project.

    Preference order:
    1. git remote get-url origin (normalized)
    2. git rev-parse --show-toplevel
    3. absolute cwd
    """
    root = (cwd or Path.cwd()).resolve()
    remote = _run_git("remote", "get-url", "origin", cwd=root)
    if remote:
        material = normalize_remote_url(remote)
    else:
        toplevel = _run_git("rev-parse", "--show-toplevel", cwd=root)
        material = str(Path(toplevel).resolve()) if toplevel else str(root)
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()[:16]
    return f"rf_{digest}"


def repo_material(cwd: Path | None = None) -> str:
    """Human-readable material used for fingerprinting (for status/doctor)."""
    root = (cwd or Path.cwd()).resolve()
    remote = _run_git("remote", "get-url", "origin", cwd=root)
    if remote:
        return normalize_remote_url(remote)
    toplevel = _run_git("rev-parse", "--show-toplevel", cwd=root)
    if toplevel:
        return str(Path(toplevel).resolve())
    return str(root)
