"""Install IDE hook packs into a target repository (Cursor / Claude Code)."""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any, Literal

from kedger.mcp.install_config import install_mcp_configs


Target = Literal["cursor", "claude", "both"]


def hook_packs_root() -> Path:
    """Locate bundled hook packs (wheel) or repo checkout hooks/."""
    spec = importlib.util.find_spec("kedger")
    if spec and spec.origin:
        bundled = Path(spec.origin).resolve().parent / "hook_packs"
        if (bundled / "cursor" / "hooks.json").exists():
            return bundled
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


def _hook_commands(entries: Any) -> set[str]:
    cmds: set[str] = set()
    if not isinstance(entries, list):
        return cmds
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        cmd = entry.get("command")
        if isinstance(cmd, str) and "kedger-hook.sh" in cmd:
            cmds.add(cmd)
        hooks = entry.get("hooks")
        if isinstance(hooks, list):
            for h in hooks:
                if isinstance(h, dict):
                    c = h.get("command")
                    if isinstance(c, str) and "kedger-hook.sh" in c:
                        cmds.add(c)
    return cmds


def _append_unique_hooks(existing: list[Any], kedger: list[Any]) -> list[Any]:
    out = list(existing)
    seen = _hook_commands(existing)
    for entry in kedger:
        cmds = _hook_commands([entry])
        if cmds and cmds <= seen:
            continue
        out.append(entry)
        seen |= cmds
    return out


def merge_claude_settings(
    existing: dict[str, Any], kedger_frag: dict[str, Any]
) -> tuple[dict[str, Any], str]:
    """Merge Kedger hooks into an existing Claude settings.json when safe."""
    merged = dict(existing)
    ex_hooks = dict(existing.get("hooks") or {})
    ked_hooks = kedger_frag.get("hooks") or {}
    if not isinstance(ked_hooks, dict):
        return merged, "skipped_invalid_fragment"

    for event, ked_entries in ked_hooks.items():
        if not isinstance(ked_entries, list):
            continue
        if event not in ex_hooks:
            ex_hooks[event] = ked_entries
            continue
        ex_list = ex_hooks[event]
        if not isinstance(ex_list, list):
            ex_hooks[event] = ked_entries
            continue
        ex_cmds = _hook_commands(ex_list)
        ked_cmds = _hook_commands(ked_entries)
        if ked_cmds and ked_cmds <= ex_cmds:
            continue
        ex_hooks[event] = _append_unique_hooks(ex_list, ked_entries)

    merged["hooks"] = ex_hooks
    return merged, "merged"


def install_hook_packs(
    *,
    target: Target = "both",
    repo_root: Path | None = None,
    install_mcp: bool = True,
) -> dict[str, Any]:
    """Copy hook scripts + IDE configs into repo_root (cwd/git root)."""
    root = detect_repo_root(repo_root)
    packs = hook_packs_root()
    written: list[str] = []
    notes: list[str] = []
    warnings: list[str] = []

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
        frag_path = claude_src / "settings.hooks.json"
        frag = json.loads(frag_path.read_text(encoding="utf-8"))
        dest = claude_dir / "settings.json"
        if not dest.exists():
            shutil.copy2(frag_path, dest)
            written.append(str(dest))
            notes.append("Claude Code: wrote .claude/settings.json")
        else:
            try:
                existing = json.loads(dest.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                existing = {}
            if not isinstance(existing, dict):
                existing = {}
            merged, status = merge_claude_settings(existing, frag)
            if status == "merged":
                dest.write_text(
                    json.dumps(merged, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                written.append(str(dest))
                notes.append(
                    "Claude Code: merged Kedger hooks into existing .claude/settings.json"
                )
            else:
                merge = claude_dir / "kedger.hooks.json"
                shutil.copy2(frag_path, merge)
                written.append(str(merge))
                warnings.append(
                    "Claude Code: could not auto-merge — wrote .claude/kedger.hooks.json; "
                    'manually merge its "hooks" into settings.json'
                )

    mcp_result = install_mcp_configs(target=target, repo_root=root, install_mcp=install_mcp)
    written.extend(mcp_result.get("written") or [])
    notes.extend(mcp_result.get("notes") or [])
    warnings.extend(mcp_result.get("warnings") or [])

    return {
        "repo_root": str(root),
        "packs_root": str(packs),
        "target": target,
        "written": written,
        "notes": notes,
        "warnings": warnings,
    }
