# Kedger Cursor hook pack

Adapters call the `kedger` CLI / `kedger hook` entrypoint. Core never imports Cursor types.

## Events (minimum 8)

| Cursor-ish event | Kedger action |
|------------------|---------------|
| SessionStart | authorized hydrate inject → `additionalContext` |
| UserPromptSubmit | `ingest` |
| Agent response / stop | `ingest` + soft boundary |
| AfterFileEdit | `ingest` |
| Tool failure | `ingest` |
| PreCompact | HARD cognify + reseal |
| SessionEnd | HARD cognify + reseal |

## Install sketch

Point Cursor hooks at:

```bash
kedger hook --source cursor --workstream default < event.json
```

Stdout is JSON including `additionalContext` for SessionStart.
