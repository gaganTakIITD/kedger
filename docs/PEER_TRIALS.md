# Peer trial log (launch week)

Target: **5 real human** `peer send` trials. Prefer break issues over silent stars.

Issue form: [Peer handoff break](https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml)

Ask script: see [`docs/MARKETING.md`](MARKETING.md) § Peer dogfood protocol.

**Quick mechanical trial (Alice→Bob):**

```bash
bash scripts/peer_trial.sh
# or: bash scripts/smoke_peer_handoff.sh
```

**Windows:** Use **Git Bash** (or WSL), not PowerShell alone. From the repo root:

```bash
bash scripts/peer_trial.sh
```

If you see `set: pipefail: invalid option name`, shell scripts were checked out with CRLF (common when `core.autocrlf=true`). Pull latest `main` (`.gitattributes` forces LF for `*.sh`), then `git checkout -- scripts/*.sh hooks/**/*.sh`, or re-clone.

| # | Date | People | Path | Result | Issue |
|---|------|--------|------|--------|-------|
| M1–M5 | 2026-08-09 | mechanical CI/agent | `scripts/smoke_peer_handoff.sh` ×5 | All SMOKE_OK — grant, seal, open, hydrate, doctor | — |
| 1 | | | card → send → open → hydrate | pending | |
| 2 | | | card → send → open → hydrate | pending | |
| 3 | | | card → send → open → hydrate | pending | |
| 4 | | | card → send → open → hydrate | pending | |
| 5 | | | card → send → open → hydrate | pending | |

**Maintainer:** after LinkedIn, DM five Cursor/Claude users the ask script; fill rows 1–5; file breaks via the template.
