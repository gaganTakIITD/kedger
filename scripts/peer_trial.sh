#!/usr/bin/env bash
# One-command Alice→Bob peer handoff smoke (see docs/PEER_TRIALS.md).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/smoke_peer_handoff.sh" "$@"
