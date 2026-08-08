#!/usr/bin/env bash
# Install Kedger IDE hook packs into the current repo.
# Usage: ./hooks/install.sh [cursor|claude|both]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-both}"
cd "$ROOT"

chmod +x "$ROOT/hooks/cursor/"*.sh "$ROOT/hooks/claude_code/"*.sh 2>/dev/null || true

install_cursor() {
  mkdir -p "$ROOT/.cursor"
  cp "$ROOT/hooks/cursor/hooks.json" "$ROOT/.cursor/hooks.json"
  echo "installed: .cursor/hooks.json (trust workspace for project hooks)"
}

install_claude() {
  mkdir -p "$ROOT/.claude"
  # Merge-friendly: write fragment; user may already have settings.json
  DEST="$ROOT/.claude/settings.json"
  FRAG="$ROOT/hooks/claude_code/settings.hooks.json"
  if [[ ! -f "$DEST" ]]; then
    cp "$FRAG" "$DEST"
    echo "installed: .claude/settings.json"
  else
    cp "$FRAG" "$ROOT/.claude/kedger.hooks.json"
    echo "wrote: .claude/kedger.hooks.json — merge its \"hooks\" into settings.json"
  fi
}

case "$TARGET" in
  cursor) install_cursor ;;
  claude|claude_code) install_claude ;;
  both)
    install_cursor
    install_claude
    ;;
  *)
    echo "usage: $0 [cursor|claude|both]" >&2
    exit 2
    ;;
esac

if ! command -v kedger >/dev/null 2>&1; then
  echo "note: kedger not on PATH — install with: pip install kedger" >&2
fi
