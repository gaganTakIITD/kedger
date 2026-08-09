#!/usr/bin/env bash
# Tip-to-tip: build wheel → install into a foreign temp repo → init → transfer.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$(mktemp -d /tmp/kedger-wheel-build-XXXX)"
VENV="$(mktemp -d /tmp/kedger-wheel-venv-XXXX)"
APP="$(mktemp -d /tmp/kedger-wheel-app-XXXX)"
HOME_ISO="$(mktemp -d /tmp/kedger-wheel-home-XXXX)"
XFER="$(mktemp -d /tmp/kedger-wheel-xfer-XXXX)"
cleanup() {
  rm -rf "$BUILD" "$VENV" "$APP" "$HOME_ISO" "$XFER"
}
trap cleanup EXIT

export KEDGER_HOME="$HOME_ISO"
python3 -m pip install -q -e "$ROOT[dev]"
rm -rf "$ROOT/dist" "$ROOT/build"
(cd "$ROOT" && python3 -m build -o "$BUILD")
WHL="$(printf '%s\n' "$BUILD"/kedger-*.whl | head -n 1)"
# head above is fine: single match, or use glob
shopt -s nullglob
wheels=("$BUILD"/kedger-*.whl)
[[ ${#wheels[@]} -ge 1 ]] || { echo "SMOKE_FAIL no wheel"; exit 1; }
WHL="${wheels[0]}"

python3 -m venv "$VENV"
# shellcheck disable=SC1091
source "$VENV/bin/activate"
pip install -q -U pip
pip install -q "$WHL"

cd "$APP"
git init -q
kedger init --name wheel-smoke --hooks both
test -f "$APP/.cursor/hooks.json"
test -f "$APP/.claude/settings.json"
kedger remember reject "Do not ship without Idempotency-Key" --reason "payments"
kedger cognify --force --promote --no-reseal
kedger pack-export --out-dir "$XFER"
shopt -s nullglob
packs=("$XFER"/*.kxp)
[[ ${#packs[@]} -ge 1 ]] || { echo "SMOKE_FAIL no pack"; exit 1; }
FP="$(kedger status | awk -F': *' '/repo_fingerprint/{print $2; exit}')"
rm -rf "$KEDGER_HOME/projects/$FP"
kedger hydrate --pack "${packs[0]}"
kedger hydrate --live > /tmp/kedger-wheel-live.txt
grep -qi 'idempotency' /tmp/kedger-wheel-live.txt
kedger doctor
echo "SMOKE_OK wheel install path ($WHL)"
