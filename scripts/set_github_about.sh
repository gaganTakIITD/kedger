#!/usr/bin/env bash
# Set GitHub repo About (description, homepage, topics). Requires repo admin + gh auth.
set -euo pipefail

REPO="${1:-gaganTakIITD/kedger}"

gh repo edit "$REPO" \
  --description "Local-first eng-memory CLI for coding agents — hooks → Anchors → sealed .kxp handoff" \
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
