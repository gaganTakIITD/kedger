"""Doctor diagnostics — hook/inject health and L0 sanity checks."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from kedger.hooks.install_packs import _hook_commands, detect_repo_root
from kedger.store.db import Store


def _has_kedger_hook(cmds: set[str]) -> bool:
    return any("kedger-hook.sh" in c for c in cmds)


def _cursor_hooks(cfg: dict[str, Any]) -> dict[str, list[Any]]:
    hooks = cfg.get("hooks")
    return hooks if isinstance(hooks, dict) else {}


def _claude_hooks(cfg: dict[str, Any]) -> dict[str, list[Any]]:
    hooks = cfg.get("hooks")
    return hooks if isinstance(hooks, dict) else {}


def diagnose_ide_hooks(repo_root: Path | None = None) -> list[str]:
    """Return non-fatal warnings about hook install / inject path health."""
    root = detect_repo_root(repo_root)
    warnings: list[str] = []

    kedger_frag = root / ".claude" / "kedger.hooks.json"
    if kedger_frag.exists():
        warnings.append(
            "Claude: .claude/kedger.hooks.json exists — merge its hooks into "
            ".claude/settings.json (kedger init could not auto-merge)"
        )

    cursor_script = root / "hooks" / "cursor" / "kedger-hook.sh"
    cursor_cfg_path = root / ".cursor" / "hooks.json"
    if cursor_script.exists() and not cursor_cfg_path.exists():
        warnings.append(
            "Cursor: hook scripts present but .cursor/hooks.json missing — "
            "run kedger init --hooks cursor"
        )

    claude_script = root / "hooks" / "claude_code" / "kedger-hook.sh"
    claude_settings_path = root / ".claude" / "settings.json"
    if claude_script.exists() and not claude_settings_path.exists():
        warnings.append(
            "Claude: hook scripts present but .claude/settings.json missing — "
            "run kedger init --hooks claude"
        )

    if cursor_cfg_path.exists():
        try:
            cfg = json.loads(cursor_cfg_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            cfg = {}
        ch = _cursor_hooks(cfg)
        ss = ch.get("sessionStart") or []
        bsp = ch.get("beforeSubmitPrompt") or []
        ss_ok = _has_kedger_hook(_hook_commands(ss))
        bsp_ok = _has_kedger_hook(_hook_commands(bsp))
        if ss_ok and not bsp_ok:
            warnings.append(
                "Cursor inject: sessionStart only — beforeSubmitPrompt fallback "
                "missing (cloud agents may not inject; see docs/PROMPT_INJECT_VERIFY.md)"
            )
        elif not ss_ok and not bsp_ok and cursor_script.exists():
            warnings.append(
                "Cursor: .cursor/hooks.json has no kedger-hook.sh entries — "
                "inject path unproven"
            )

    if claude_settings_path.exists():
        try:
            cfg = json.loads(claude_settings_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            cfg = {}
        ch = _claude_hooks(cfg)
        ss = ch.get("SessionStart") or []
        ups = ch.get("UserPromptSubmit") or []
        ss_ok = _has_kedger_hook(_hook_commands(ss))
        ups_ok = _has_kedger_hook(_hook_commands(ups))
        if ss_ok and not ups_ok:
            warnings.append(
                "Claude inject: SessionStart only — UserPromptSubmit fallback "
                "missing (inject may be unreliable in some environments)"
            )
        elif not ss_ok and not ups_ok and claude_script.exists():
            warnings.append(
                "Claude: settings.json has no kedger-hook.sh entries — inject path unproven"
            )

    return warnings


def diagnose_l0_health(store: Store, *, workstream_id: str | None) -> list[str]:
    """Cheap L0 emptiness / clock-skew warnings."""
    warnings: list[str] = []
    if workstream_id is None:
        return warnings

    obs = store.list_observations(workstream_id=workstream_id)
    if not obs:
        root = detect_repo_root()
        hooks_likely = (
            (root / ".cursor" / "hooks.json").exists()
            or (root / ".claude" / "settings.json").exists()
            or (root / "hooks" / "cursor" / "kedger-hook.sh").exists()
        )
        if hooks_likely:
            warnings.append(
                "L0 empty but IDE hooks appear configured — trust workspace / "
                "open the repo root where hooks were installed?"
            )
        return warnings

    now = datetime.now(timezone.utc)
    future = 0
    for o in obs[-50:]:
        ts = o.get("ts")
        if not ts:
            continue
        try:
            t = ts[:-1] + "+00:00" if str(ts).endswith("Z") else str(ts)
            dt = datetime.fromisoformat(t)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            if dt > now:
                future += 1
        except ValueError:
            continue
    if future:
        warnings.append(
            f"L0 clock skew: {future} observation(s) have future timestamps — "
            "recency scoring may be wrong"
        )

    soft = sum(1 for o in obs if o.get("soft_stale"))
    if soft and len(obs) >= int(0.7 * 5000):
        warnings.append(
            f"L0 pressure: {soft} soft-stale row(s) — delay-k marking before flush"
        )

    return warnings
