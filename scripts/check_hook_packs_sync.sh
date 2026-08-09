#!/usr/bin/env bash
# Fail if repo hooks/ drifts from the wheel-shipped src/kedger/hook_packs/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
diff -rq "$ROOT/hooks/cursor" "$ROOT/src/kedger/hook_packs/cursor"
diff -rq "$ROOT/hooks/claude_code" "$ROOT/src/kedger/hook_packs/claude_code"
echo "hook packs in sync"
