#!/usr/bin/env bash
# Set GitHub repo About (description, homepage, topics). Requires repo admin + gh auth.
set -euo pipefail

REPO="${1:-gaganTakIITD/kedger}"

# Pitch: problem first — judgment isn't versioned; Kedger hands the why via sealed packs.
gh repo edit "$REPO" \
  --description "Code is versioned; agent judgment isn't. Local-first CLI: Anchors + sealed .kxp handoff for Cursor/Claude — explicit share, no cloud memory bus." \
  --homepage "https://pypi.org/project/kedger/" \
  --add-topic cli \
  --add-topic python \
  --add-topic agents \
  --add-topic cursor \
  --add-topic claude-code \
  --add-topic memory \
  --add-topic handoff \
  --add-topic local-first \
  --add-topic sealed-packs \
  --add-topic developer-tools \
  --enable-wiki=false

echo "About updated for https://github.com/${REPO}"
echo "Social preview: GitHub → Settings → General → Social preview → upload docs/assets/social.png"
