# Kedger Claude Code hook pack

Same CLI contract as Cursor. Map Claude Code hook names into `kedger hook --source claude_code`.

## Install (recommended)

From **your app repo**, after `pip install "kedger>=0.1.1"`:

```bash
kedger init --name me --hooks claude
# or later:
kedger hooks install --target claude
```

This writes:

| Path | Purpose |
|------|---------|
| `.claude/settings.json` | Created when missing (hooks fragment) |
| `.claude/kedger.hooks.json` | Written instead when `settings.json` already exists — **merge** its `"hooks"` into settings |
| `hooks/claude_code/kedger-hook.sh` | Adapter → `kedger hook --source claude_code` |

Paths in the fragment are relative to the repo root (`./hooks/claude_code/...`).

## Events

| Claude event | Kedger |
|--------------|--------|
| `SessionStart` | hydrate inject (`hookSpecificOutput.additionalContext`) |
| `UserPromptSubmit` | ingest |
| `PostToolUse` (`Edit\|Write`) | ingest `file_edit` |
| `PostToolUseFailure` | ingest `tool_fail` |
| `PreCompact` | cognify HARD |
| `Stop` | soft boundary |
| `SessionEnd` | cognify HARD |

## Manual smoke

```bash
echo '{"hook_event_name":"SessionStart","session_id":"demo"}' \
  | ./hooks/claude_code/kedger-hook.sh SessionStart
```
