"""Install IDE hook packs into a target repository (Cursor / Claude Code)."""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
from pathlib import Path
from typing import Any, Literal


Target = Literal["cursor", "claude", "both"]


def hook_packs_root() -> Path:
    """Locate bundled hook packs (wheel) or repo checkout hooks/."""
    # Wheel force-include: kedger/hook_packs/{cursor,claude_code}/...
    spec = importlib.util.find_spec("kedger")
    if spec and spec.origin:
        bundled = Path(spec.origin).resolve().parent / "hook_packs"
        if (bundled / "cursor" / "hooks.json").exists():
            return bundled
    # Editable / source checkout: <repo>/hooks
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "hooks"
        if (candidate / "cursor" / "hooks.json").exists():
            return candidate
    raise FileNotFoundError(
        "Kedger hook packs not found (expected package hook_packs/ or repo hooks/)"
    )


def detect_repo_root(start: Path | None = None) -> Path:
    """Prefer git toplevel; else start (cwd)."""
    start = (start or Path.cwd()).resolve()
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            check=False,
            capture_output=True,
            text=True,
        )
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip()).resolve()
    except OSError:
        pass
    return start


def _copy_tree(src: Path, dst: Path) -> list[str]:
    dst.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    for path in src.rglob("*"):
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        if target.suffix == ".sh":
            target.chmod(target.stat().st_mode | 0o111)
        written.append(str(target))
    return written


def install_hook_packs(
    *,
    target: Target = "both",
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Copy hook scripts + IDE configs into repo_root (cwd/git root)."""
    root = detect_repo_root(repo_root)
    packs = hook_packs_root()
    written: list[str] = []
    notes: list[str] = []

    if target in {"cursor", "both"}:
        cursor_src = packs / "cursor"
        written.extend(_copy_tree(cursor_src, root / "hooks" / "cursor"))
        cursor_cfg = root / ".cursor"
        cursor_cfg.mkdir(parents=True, exist_ok=True)
        hooks_json = cursor_cfg / "hooks.json"
        shutil.copy2(cursor_src / "hooks.json", hooks_json)
        written.append(str(hooks_json))
        notes.append("Cursor: trust workspace for project hooks (.cursor/hooks.json)")

    if target in {"claude", "both"}:
        claude_src = packs / "claude_code"
        written.extend(_copy_tree(claude_src, root / "hooks" / "claude_code"))
        claude_dir = root / ".claude"
        claude_dir.mkdir(parents=True, exist_ok=True)
        frag = claude_src / "settings.hooks.json"
        dest = claude_dir / "settings.json"
        if not dest.exists():
            shutil.copy2(frag, dest)
            written.append(str(dest))
            notes.append("Claude Code: wrote .claude/settings.json")
        else:
            merge = claude_dir / "kedger.hooks.json"
            shutil.copy2(frag, merge)
            written.append(str(merge))
            notes.append(
                "Claude Code: wrote .claude/kedger.hooks.json — merge its "
                '"hooks" into settings.json'
            )

    return {
        "repo_root": str(root),
        "packs_root": str(packs),
        "target": target,
        "written": written,
        "notes": notes,
    }
