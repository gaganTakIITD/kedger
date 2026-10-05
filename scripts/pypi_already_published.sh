#!/usr/bin/env bash
# Query PyPI JSON for kedger==VERSION.
#   0 — already published (skip upload)
#   1 — not on PyPI (should publish)
#   2 — unexpected HTTP / network error (fail closed; do not upload)
set -euo pipefail

VERSION="${1:-}"
if [[ -z "${VERSION}" ]]; then
  echo "usage: $0 <version>" >&2
  exit 2
fi

URL="https://pypi.org/pypi/kedger/${VERSION}/json"
BODY="$(mktemp)"
trap 'rm -f "${BODY}"' EXIT

set +e
CODE="$(curl -sS -L --max-time 30 \
  -A "kedger-release-check" \
  -o "${BODY}" -w "%{http_code}" \
  "${URL}")"
CURL_RC=$?
set -e

if [[ "${CURL_RC}" -ne 0 ]]; then
  echo "error: curl failed (exit ${CURL_RC}) fetching ${URL}" >&2
  exit 2
fi

if [[ "${CODE}" == "200" ]]; then
  echo "skip: already on PyPI (kedger==${VERSION})"
  exit 0
fi

if [[ "${CODE}" == "404" ]]; then
  echo "not on PyPI yet (kedger==${VERSION}); publish"
  exit 1
fi

echo "error: unexpected PyPI response HTTP ${CODE} for ${URL}" >&2
head -c 500 "${BODY}" >&2 || true
echo >&2
exit 2
