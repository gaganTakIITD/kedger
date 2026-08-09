# Kedger Cursor hook pack

Adapters call the `kedger` CLI. Core never imports Cursor types.

## Install (recommended)

From **your app repo** (not the Kedger source tree), after `pip install "kedger>=0.1.1"`:

```bash
kedger init --name me --hooks cursor
# or later:
kedger hooks install --target cursor
```

This writes:

| Path | Purpose |
|------|---------|
| `.cursor/hooks.json` | Cursor project hooks config |
| `hooks/cursor/kedger-hook.sh` | Adapter → `kedger hook --source cursor` |
| `hooks/cursor/session_start.sh` | Thin sessionStart wrapper |

Then **trust the workspace** in Cursor so project hooks run. Restart the agent session.

Override workstream with `KEDGER_WORKSTREAM`.

## Events (minimum 8)

| Cursor event | Kedger action |
|--------------|---------------|
| `sessionStart` | authorized hydrate inject → `additional_context` |
| `beforeSubmitPrompt` | `ingest` |
| `afterAgentResponse` | `ingest` |
| `afterFileEdit` | `ingest` |
| `postToolUseFailure` | `ingest` |
| `preCompact` | HARD cognify + reseal |
| `stop` | soft boundary |
| `sessionEnd` | HARD cognify + reseal |

## Manual smoke

```bash
echo '{"session_id":"demo"}' | ./hooks/cursor/kedger-hook.sh sessionStart
```
