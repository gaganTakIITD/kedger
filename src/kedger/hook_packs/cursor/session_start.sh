#!/usr/bin/env bash
# Cursor SessionStart → Kedger authorized hydrate inject
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
exec "$ROOT/kedger-hook.sh" sessionStart
