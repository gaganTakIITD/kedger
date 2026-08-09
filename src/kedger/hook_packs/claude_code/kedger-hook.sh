#!/usr/bin/env bash
# Claude Code → kedger adapter. Payload already includes hook_event_name.
# Usage: kedger-hook.sh [override-type]
# Env: KEDGER_WORKSTREAM (default: default)
set -euo pipefail

OVERRIDE="${1:-}"
WORKSTREAM="${KEDGER_WORKSTREAM:-default}"

if ! command -v kedger >/dev/null 2>&1; then
  echo '{"ok":false,"error":"kedger not on PATH; pip install kedger"}' >&2
  exit 1
fi

export KEDGER_HOOK_OVERRIDE="$OVERRIDE"
exec python3 -c '
import json, os, sys, subprocess
raw = sys.stdin.read()
payload = json.loads(raw) if raw.strip() else {}
if not isinstance(payload, dict):
    payload = {"raw": payload}
override = os.environ.get("KEDGER_HOOK_OVERRIDE") or ""
if override:
    payload["type"] = override
# Prefer Claude field if present
if "hook_event_name" in payload and "type" not in payload:
    payload["type"] = payload["hook_event_name"]
proc = subprocess.run(
    ["kedger", "hook", "--source", "claude_code", "--workstream", sys.argv[1]],
    input=json.dumps(payload),
    text=True,
)
sys.exit(proc.returncode)
' "$WORKSTREAM"
