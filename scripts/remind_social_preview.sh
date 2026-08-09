#!/usr/bin/env bash
# Print GitHub Social preview instructions (API cannot set OG image).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ASSET="${ROOT}/docs/assets/social.png"

echo "GitHub About (description/topics) — run if empty:"
echo "  bash scripts/set_github_about.sh"
echo
echo "Social preview (maintainer UI — not available via API):"
echo "  1. Open https://github.com/gaganTakIITD/kedger/settings"
echo "  2. General → Social preview → Edit"
echo "  3. Upload: ${ASSET}"
echo "  4. Save"
if [[ -f "$ASSET" ]]; then
  echo
  echo "Asset OK: $(wc -c < "$ASSET") bytes · $(file -b "$ASSET" 2>/dev/null || echo png)"
else
  echo "MISSING asset — run: python3 scripts/render_brand_assets.py" >&2
  exit 1
fi
