# Kedger Cursor hook pack

Adapters call the `kedger` CLI. Core never imports Cursor types.

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

## Install (project)

From the repo root (after `pip install kedger` or `pip install -e .`):

```bash
# Merge into project hooks (paths relative to repo root)
cp hooks/cursor/hooks.json .cursor/hooks.json
chmod +x hooks/cursor/kedger-hook.sh
```

Or symlink:

```bash
mkdir -p .cursor
ln -sf ../hooks/cursor/hooks.json .cursor/hooks.json
```

Trust the workspace so project hooks run. Override workstream with `KEDGER_WORKSTREAM`.

## Manual smoke

```bash
echo '{"session_id":"demo"}' | ./hooks/cursor/kedger-hook.sh sessionStart
```

Stdout is JSON; SessionStart includes `additional_context` for hydrate inject.
