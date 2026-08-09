#!/usr/bin/env bash
# Cursor → kedger adapter. Injects event type (Cursor payloads omit it), then runs CLI.
# Usage: kedger-hook.sh <EventName>
# Env: KEDGER_WORKSTREAM (default: default)
set -euo pipefail

EVENT="${1:?usage: kedger-hook.sh <EventName>}"
WORKSTREAM="${KEDGER_WORKSTREAM:-default}"

if ! command -v kedger >/dev/null 2>&1; then
  echo '{"ok":false,"error":"kedger not on PATH; pip install kedger"}' >&2
  exit 1
fi

# Merge type into stdin JSON so normalize can map Cursor camelCase events.
export KEDGER_HOOK_EVENT="$EVENT"
exec python3 -c '
import json, os, sys, subprocess
raw = sys.stdin.read()
payload = json.loads(raw) if raw.strip() else {}
if not isinstance(payload, dict):
    payload = {"raw": payload}
payload.setdefault("type", os.environ["KEDGER_HOOK_EVENT"])
payload.setdefault("event", os.environ["KEDGER_HOOK_EVENT"])
proc = subprocess.run(
    ["kedger", "hook", "--source", "cursor", "--workstream", sys.argv[1]],
    input=json.dumps(payload),
    text=True,
)
sys.exit(proc.returncode)
' "$WORKSTREAM"
