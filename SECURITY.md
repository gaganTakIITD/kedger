# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| `0.1.1+` | Yes (tip / launch surface) |
| `0.1.0` | Limited — thinner CLI; upgrade to `>=0.1.1` |

## What Kedger protects

- Local principal keys under `~/.kedger/keys/` (Ed25519 + X25519)
- Sealed handoff packs (`.kxp`) for authorized recipients
- Inv-Scope: unauthorized hydrate returns a uniform not-found (no existence oracle)
- Redact-before-persist on ingest / transcript paths (best-effort patterns)

## What Kedger does **not** claim

- Insider recipients with a grant can still leak pack contents
- Pack metadata may be visible; revoke does **not** erase offline copies
- Recipient import is TOFU (trust on first use)
- The SQLite store is **not** encrypted at rest (Phase F deferred)
- Deterministic redaction is not a substitute for a DLP product

See also: `kedger doctor` crypto/share checks and `docs/PHASE_F_DEFERRED.md`.

## Reporting a vulnerability

Email the maintainer listed on the GitHub repo (or open a **private** GitHub security advisory on [gaganTakIITD/kedger](https://github.com/gaganTakIITD/kedger)).

Please include:

1. Kedger version (`kedger --version`)
2. Minimal repro (commands / hook payload; redact secrets)
3. Impact (key exposure, pack oracle, store leak, etc.)

Do **not** open a public issue for exploitable crypto / auth bugs until a fix is available.
