#!/usr/bin/env bash
# Smoke prompt-time inject: SessionStart + beforeSubmitPrompt emit additional_context
# after remember (see docs/PROMPT_INJECT_VERIFY.md).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [[ "${SMOKE_KEEP_HOME:-}" != "1" ]]; then
  KEDGER_HOME="$(mktemp -d /tmp/kedger-inject-smoke-XXXX)"
  export KEDGER_HOME
fi
WORKDIR="$(mktemp -d /tmp/kedger-inject-work-XXXX)"
cleanup() {
  if [[ "${SMOKE_KEEP_HOME:-}" != "1" ]]; then
    rm -rf "$KEDGER_HOME"
  fi
  rm -rf "$WORKDIR"
}
trap cleanup EXIT

cd "$WORKDIR"
git init -q
python3 -m pip install -q -e "$ROOT"

kedger keys init --name inject-smoke
kedger hooks install --target cursor --repo "$WORKDIR"

CONSTRAINT="Must send Idempotency-Key on charge create"
kedger remember constraint "$CONSTRAINT"

HOOK="$WORKDIR/hooks/cursor/kedger-hook.sh"
if [[ ! -x "$HOOK" ]]; then
  chmod +x "$HOOK"
fi

session_out="$(echo '{"session_id":"inject-smoke"}' | "$HOOK" sessionStart)"
python3 - <<'PY' "$session_out" "$CONSTRAINT"
import json, sys
out, needle = sys.argv[1], sys.argv[2]
data = json.loads(out)
assert data.get("ok") is True, out
ctx = data.get("additional_context") or data.get("additionalContext") or ""
assert needle in ctx, f"SessionStart missing constraint in additional_context: {out}"
effects = {s.get("effect") for s in data.get("side_effects") or []}
assert "hydrate_inject" in effects, f"SessionStart missing hydrate_inject side effect: {out}"
print("sessionStart inject ok")
PY

bsp_out="$(echo '{"session_id":"inject-smoke","prompt":"patch charges.py"}' | "$HOOK" beforeSubmitPrompt)"
python3 - <<'PY' "$bsp_out" "$CONSTRAINT"
import json, sys
out, needle = sys.argv[1], sys.argv[2]
data = json.loads(out)
assert data.get("ok") is True, out
ctx = data.get("additional_context") or data.get("additionalContext") or ""
assert needle in ctx, f"beforeSubmitPrompt missing constraint in additional_context: {out}"
effects = {s.get("effect") for s in data.get("side_effects") or []}
assert "hydrate_inject" in effects, f"beforeSubmitPrompt missing hydrate_inject: {out}"
assert "ingest" in effects, f"beforeSubmitPrompt missing ingest: {out}"
print("beforeSubmitPrompt inject ok")
PY

echo "SMOKE_OK prompt inject"
