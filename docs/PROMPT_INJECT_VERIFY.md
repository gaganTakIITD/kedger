# Prompt-time memory inject — verification checklist

Use this after `pip install kedger` and `kedger init --hooks cursor` (or `claude_code`) in your app repo.

## Cursor

1. Trust the workspace so project hooks run (`.cursor/hooks.json` → `hooks/cursor/kedger-hook.sh`).
2. Seed memory: `kedger remember constraint "Must send Idempotency-Key"` and optionally `kedger cognify --force --promote`.
3. **SessionStart path** — new agent chat:
   ```bash
   echo '{"session_id":"verify"}' | ./hooks/cursor/kedger-hook.sh sessionStart | jq .
   ```
   Expect `additional_context` containing your constraint.
4. **beforeSubmitPrompt fallback** (fires every prompt; survives dropped SessionStart):
   ```bash
   echo '{"session_id":"verify","prompt":"patch charges.py"}' \
     | ./hooks/cursor/kedger-hook.sh beforeSubmitPrompt | jq .
   ```
   Expect `additional_context` **and** `side_effects` with both `hydrate_inject` and `ingest`.
5. In Cursor: submit a prompt in a trusted project — Kedger memory should appear in agent context even if sessionStart was deferred.

## Claude Code

1. Install hooks: `kedger hooks install --target claude_code`.
2. Seed memory as above.
3. **UserPromptSubmit fallback**:
   ```bash
   echo '{"hook_event_name":"UserPromptSubmit","prompt":"what constraints?"}' \
     | ./hooks/claude_code/kedger-hook.sh UserPromptSubmit | jq .
   ```
   Expect `hookSpecificOutput.additionalContext` with your anchors.

## MCP pull fallback (when hooks miss)

```bash
kedger mcp tools-list
kedger mcp call hydrate --args-json '{}'
kedger mcp call anchors_get --args-json '{"anchor_id":"<id from hydrate>"}'
```

For IDE MCP wiring, run `kedger mcp serve` (stdio JSON-RPC) and register it in your client’s MCP config.

## Fail-soft guarantee

With `kedger` **not** on PATH, hooks must exit 0 and never block prompts:

```bash
PATH=/empty ./hooks/cursor/kedger-hook.sh beforeSubmitPrompt <<< '{"prompt":"hi"}'
# → {"ok":true,"skipped":true,"reason":"kedger not on PATH"}
```

## Known risk

Cursor **SessionStart** `additional_context` is fire-and-forget and may be dropped (especially cloud agents). **beforeSubmitPrompt** / **UserPromptSubmit** inject is the reliable fallback; MCP `hydrate` is the manual pull path when both miss.
