# Kedger

Local-first CLI for durable engineering memory and sealed session handoff.

**Kedger ≠ MoDeX.** MoDeX is a separate hackathon product. Kedger is its own OSS engine: hooks → CLI → Anchors → sealed packs (`.kxp`).

| Lock | Value |
|------|--------|
| CLI | `kedger` |
| Private store | `~/.kedger/` |
| Repo policy | `<repo>/.kedger/` |
| Packs | `*.kxp` |
| Schema | `kedger.memory.v1` |

## Install

```bash
pip install -e ".[dev]"
# or: uv sync --extra dev
```

## Quick start

```bash
kedger keys init --name me
kedger remember reject "Do not use cookie sessions" --reason "CSRF"
kedger status --list
kedger doctor
```

## CLI

| Command | Behavior |
|---------|----------|
| `kedger keys init [--name] [--force]` | Ed25519 + X25519 principal under `~/.kedger/keys/` |
| `kedger keys show` | Show principal id + public keys |
| `kedger keys export-recipient` | Export recipient JSON for grants |
| `kedger remember <kind> "..."` | Create Anchor |
| `kedger forget <anc_…>` | Invalidate via SUPERSEDES (never hard-delete) |
| `kedger status [--list]` | Fingerprint, store path, counts |
| `kedger doctor` | Health checks |
| `kedger ingest --from-hook` | L0 observation from stdin JSON |
| `kedger handoff [--workstream]` | Compile Anchors → sealed `.kxp` |
| `kedger hydrate --pack …` | Authorized open (404 on deny) |
| `kedger grant --to … --recipient-file …` | Workstream capability + recipient key |
| `kedger revoke --from …` | Revoke capability (reseal required) |

Override the home directory with `KEDGER_HOME` (used by tests).

## Docs

Start with [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md) (§0A identity lock).

## License

Apache-2.0
