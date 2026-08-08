"""Create/update <repo>/.kedger/ pointers — never store private payloads here."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


def _git_toplevel(cwd: Path | None = None) -> Path | None:
    root = (cwd or Path.cwd()).resolve()
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None
    if proc.returncode != 0:
        return None
    return Path(proc.stdout.strip())


def repo_policy_dir(cwd: Path | None = None) -> Path | None:
    top = _git_toplevel(cwd)
    if top is None:
        return None
    return top / ".kedger"


def ensure_repo_policy(
    *,
    repo_fingerprint: str,
    cwd: Path | None = None,
) -> Path | None:
    """Write minimal project.json + .gitignore under <repo>/.kedger/."""
    policy = repo_policy_dir(cwd)
    if policy is None:
        return None
    policy.mkdir(parents=True, exist_ok=True)
    project = {
        "schema_version": "kedger.memory.v1",
        "repo_fingerprint": repo_fingerprint,
        "share_mode": "explicit_only",
        "note": "Pointers/policy only — private store lives under ~/.kedger/",
    }
    (policy / "project.json").write_text(
        json.dumps(project, indent=2) + "\n", encoding="utf-8"
    )
    gitignore = policy / ".gitignore"
    if not gitignore.exists():
        gitignore.write_text(
            "# Never commit private Kedger payloads from repo policy dir\n"
            "*.kxp\n"
            "*.sqlite\n"
            "raw/\n"
            "packs/\n"
            "keys/\n",
            encoding="utf-8",
        )
    return policy
