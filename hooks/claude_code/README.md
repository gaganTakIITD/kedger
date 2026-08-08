# Kedger Claude Code hook pack

Same CLI contract as Cursor. Map Claude Code hook names into `kedger hook --source claude_code`.

| Claude-ish event | Kedger |
|------------------|--------|
| SessionStart | hydrate inject |
| UserPromptSubmit | ingest |
| PostToolUse (failure) | ingest tool_fail |
| PreCompact | cognify HARD |
| Stop / SessionEnd | cognify |

```bash
kedger hook --source claude_code --workstream default < event.json
```
