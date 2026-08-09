#!/usr/bin/env bash
# Tip-to-tip: build wheel → install into an isolated prefix → foreign repo init → transfer.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$(mktemp -d /tmp/kedger-wheel-build-XXXX)"
PREFIX="$(mktemp -d /tmp/kedger-wheel-prefix-XXXX)"
APP="$(mktemp -d /tmp/kedger-wheel-app-XXXX)"
HOME_ISO="$(mktemp -d /tmp/kedger-wheel-home-XXXX)"
XFER="$(mktemp -d /tmp/kedger-wheel-xfer-XXXX)"
cleanup() {
  rm -rf "$BUILD" "$PREFIX" "$APP" "$HOME_ISO" "$XFER"
}
trap cleanup EXIT

export KEDGER_HOME="$HOME_ISO"
python3 -m pip install -q -e "$ROOT[dev]"
rm -rf "$ROOT/dist" "$ROOT/build"
(cd "$ROOT" && python3 -m build -o "$BUILD")
shopt -s nullglob
wheels=("$BUILD"/kedger-*.whl)
[[ ${#wheels[@]} -ge 1 ]] || { echo "SMOKE_FAIL no wheel" >&2; exit 1; }
WHL="${wheels[0]}"

# Isolated install without requiring python3-venv (prefix + PATH/PYTHONPATH).
python3 -m pip install -q --upgrade --target "$PREFIX" "$WHL"
export PATH="$PREFIX/bin:$PATH"
export PYTHONPATH="$PREFIX${PYTHONPATH:+:$PYTHONPATH}"
hash -r
command -v kedger >/dev/null
python3 -c "import kedger; assert kedger.__version__ == '0.1.1', kedger.__version__"

cd "$APP"
git init -q
kedger init --name wheel-smoke --hooks both
test -f "$APP/.cursor/hooks.json"
test -f "$APP/.claude/settings.json"
kedger remember reject "Do not ship without Idempotency-Key" --reason "payments"
kedger cognify --force --promote --no-reseal
kedger pack-export --out-dir "$XFER"
packs=("$XFER"/*.kxp)
[[ ${#packs[@]} -ge 1 ]] || { echo "SMOKE_FAIL no pack" >&2; exit 1; }
STATUS="$(kedger status)"
FP="$(printf '%s\n' "$STATUS" | sed -n 's/^repo_fingerprint:[[:space:]]*//p' | sed -n '1p')"
[[ -n "$FP" ]] || { echo "SMOKE_FAIL could not parse repo_fingerprint" >&2; exit 1; }
rm -rf "$KEDGER_HOME/projects/$FP"
kedger hydrate --pack "${packs[0]}"
kedger hydrate --live > /tmp/kedger-wheel-live.txt
grep -qi 'idempotency' /tmp/kedger-wheel-live.txt
kedger doctor
echo "SMOKE_OK wheel install path ($WHL)"
