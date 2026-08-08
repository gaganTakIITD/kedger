#!/usr/bin/env bash
# Claude Code SessionStart → Kedger authorized hydrate inject
set -euo pipefail
exec kedger hook --source claude_code --workstream "${KEDGER_WORKSTREAM:-default}"
