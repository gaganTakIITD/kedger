#!/usr/bin/env bash
# Smoke the cross-session transfer path for a fresh checkout.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export KEDGER_HOME="${KEDGER_HOME:-$(mktemp -d /tmp/kedger-smoke-XXXX)}"
WORKDIR="$(mktemp -d /tmp/kedger-work-XXXX)"
XFER="$(mktemp -d /tmp/kedger-xfer-XXXX)"
cleanup() { rm -rf "$KEDGER_HOME" "$WORKDIR" "$XFER"; }
trap cleanup EXIT

cd "$WORKDIR"
git init -q
python3 -m pip install -q -e "$ROOT"

kedger keys init --name smoke
kedger remember reject "Do not flip billing_v2" --reason "finance"
kedger remember constraint "Must send Idempotency-Key on charge create"
# Simulate agent edits via ingest
python3 - <<'PY'
import json, sys
from kedger.store import Store, repo_fingerprint
from kedger.keys import load_principal
store = Store.open(repo_fingerprint())
p = load_principal()
ws = store.ensure_workstream(slug="default", principal_id=p.principal_id, signing_key=p.signing_key)
for i, t in enumerate([
  {"type":"user_prompt","summary":"yo doubles again dont touch billing_v2 gotta idempotency key"},
  {"type":"agent_response","summary":"Constraint: must send Idempotency-Key. Rejection: do not flip billing_v2. Next: patch charges.py"},
  {"type":"file_edit","summary":"Edited src/payments/charges.py (+11/-2)","entity_hints":[{"entity_type":"file","name":"src/payments/charges.py"}],
   "edit_stats":{"path":"src/payments/charges.py","edits":2,"lines_added":11,"lines_removed":2}},
]):
    store.ingest_observation({**t,"session_id":"smoke","workstream_id":ws["id"],"agent_tool":"cursor",
      "ts":f"2026-08-09T23:00:{i:02d}Z"}, principal_id=p.principal_id)
print("ingested")
PY

kedger cognify --force --promote --no-reseal
kedger pack-export --out-dir "$XFER"
PACK="$(ls "$XFER"/*.kxp | head -1)"

# Wipe project store, keep keys
FP="$(kedger status | awk -F': *' '/repo_fingerprint/{print $2; exit}')"
rm -rf "$KEDGER_HOME/projects/$FP"

kedger hydrate --pack "$PACK"
kedger hydrate --live | tee /tmp/kedger-smoke-live.txt
grep -qiE 'idempotency|billing' /tmp/kedger-smoke-live.txt
kedger transcript stats --live
kedger doctor
echo "SMOKE_OK transfer path"
