#!/usr/bin/env bash
# Cursor SessionStart → Kedger authorized hydrate inject
set -euo pipefail
exec kedger hook --source cursor --workstream "${KEDGER_WORKSTREAM:-default}"
