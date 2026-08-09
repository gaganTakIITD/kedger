#!/usr/bin/env bash
# Install Kedger IDE hook packs into the *current* repo (cwd / git root).
# Usage: ./hooks/install.sh [cursor|claude|both]
#
# Prefer: kedger hooks install
# This script delegates to the CLI when available; otherwise copies from
# this source tree into the caller's cwd/git root (not the Kedger source root).
set -euo pipefail

TARGET="${1:-both}"
SRC_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Install into the caller's working tree, not the Kedger checkout.
if git rev-parse --show-toplevel >/dev/null 2>&1; then
  DEST_ROOT="$(git rev-parse --show-toplevel)"
else
  DEST_ROOT="$(pwd)"
fi

if command -v kedger >/dev/null 2>&1; then
  exec kedger hooks install --target "$TARGET" --repo "$DEST_ROOT"
fi

# Fallback without kedger on PATH (source checkout only)
PACKS="$SRC_ROOT/hooks"
if [[ ! -f "$PACKS/cursor/hooks.json" ]]; then
  echo "error: hook packs not found at $PACKS; install kedger: pip install kedger" >&2
  exit 1
fi

chmod +x "$PACKS/cursor/"*.sh "$PACKS/claude_code/"*.sh 2>/dev/null || true

install_cursor() {
  mkdir -p "$DEST_ROOT/hooks/cursor" "$DEST_ROOT/.cursor"
  cp -R "$PACKS/cursor/." "$DEST_ROOT/hooks/cursor/"
  cp "$PACKS/cursor/hooks.json" "$DEST_ROOT/.cursor/hooks.json"
  chmod +x "$DEST_ROOT/hooks/cursor/"*.sh 2>/dev/null || true
  echo "installed: $DEST_ROOT/.cursor/hooks.json (+ hooks/cursor scripts)"
}

install_claude() {
  mkdir -p "$DEST_ROOT/hooks/claude_code" "$DEST_ROOT/.claude"
  cp -R "$PACKS/claude_code/." "$DEST_ROOT/hooks/claude_code/"
  chmod +x "$DEST_ROOT/hooks/claude_code/"*.sh 2>/dev/null || true
  DEST="$DEST_ROOT/.claude/settings.json"
  FRAG="$PACKS/claude_code/settings.hooks.json"
  if [[ ! -f "$DEST" ]]; then
    cp "$FRAG" "$DEST"
    echo "installed: $DEST"
  else
    cp "$FRAG" "$DEST_ROOT/.claude/kedger.hooks.json"
    echo "wrote: $DEST_ROOT/.claude/kedger.hooks.json — merge its \"hooks\" into settings.json"
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

echo "note: kedger not on PATH — install with: pip install 'kedger>=0.1.1'" >&2
