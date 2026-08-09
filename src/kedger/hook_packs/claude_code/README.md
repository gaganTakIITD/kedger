# Kedger Claude Code hook pack

Same CLI contract as Cursor. Map Claude Code hook names into `kedger hook --source claude_code`.

| Claude event | Kedger |
|--------------|--------|
| `SessionStart` | hydrate inject (`hookSpecificOutput.additionalContext`) |
| `UserPromptSubmit` | ingest |
| `PostToolUse` (`Edit\|Write`) | ingest `file_edit` |
| `PostToolUseFailure` | ingest `tool_fail` |
| `PreCompact` | cognify HARD |
| `Stop` | soft boundary |
| `SessionEnd` | cognify HARD |

## Install (project)

Merge the fragment into `.claude/settings.json` (or user `~/.claude/settings.json`):

```bash
chmod +x hooks/claude_code/kedger-hook.sh
# Copy hooks block from settings.hooks.json into .claude/settings.json
```

Example merge target: `.claude/settings.json` → top-level `"hooks"` key from [`settings.hooks.json`](settings.hooks.json).

Paths in the fragment are relative to the repo root (`./hooks/claude_code/...`).

## Manual smoke

```bash
echo '{"hook_event_name":"SessionStart","session_id":"demo"}' \
  | ./hooks/claude_code/kedger-hook.sh SessionStart
```
