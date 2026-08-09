#!/usr/bin/env bash
# Two-person dogfood: Alice sends a pack; Bob opens it on a fresh home.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
APP="$(mktemp -d /tmp/kedger-peer-app-XXXX)"
ALICE_HOME="$(mktemp -d /tmp/kedger-peer-alice-XXXX)"
BOB_HOME="$(mktemp -d /tmp/kedger-peer-bob-XXXX)"
XFER="$(mktemp -d /tmp/kedger-peer-xfer-XXXX)"
cleanup() { rm -rf "$APP" "$ALICE_HOME" "$BOB_HOME" "$XFER"; }
trap cleanup EXIT

python3 -m pip install -q -e "$ROOT"
cd "$APP"
git init -q

export KEDGER_HOME="$ALICE_HOME"
kedger init --name alice --hooks none
kedger remember reject "Do not flip billing_v2" --reason finance
kedger remember constraint "Must send Idempotency-Key on charge create"

export KEDGER_HOME="$BOB_HOME"
kedger init --name bob --hooks none
kedger peer card --out "$XFER/bob.kedger.json"

export KEDGER_HOME="$ALICE_HOME"
kedger peer send --to "$XFER/bob.kedger.json" --out-dir "$XFER" --no-promote
shopt -s nullglob
packs=("$XFER"/*.kxp)
[[ ${#packs[@]} -ge 1 ]] || { echo "SMOKE_FAIL no pack" >&2; exit 1; }

export KEDGER_HOME="$BOB_HOME"
kedger peer open "${packs[0]}"
kedger hydrate --live > /tmp/kedger-peer-live.txt
grep -qiE 'idempotency|billing' /tmp/kedger-peer-live.txt
kedger doctor
echo "SMOKE_OK peer handoff path"
