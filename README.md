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
| Share mode | `explicit_only` |

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
kedger handoff
kedger hydrate --live
```

## CLI

| Command | Behavior |
|---------|----------|
| `kedger keys init\|show\|export-recipient` | Ed25519 + X25519 principal under `~/.kedger/keys/` |
| `kedger remember` / `forget` | Anchors; forget via SUPERSEDES |
| `kedger status` / `doctor` | Fingerprint, counts, health |
| `kedger ingest --from-hook` | L0 observation (redact-before-persist) |
| `kedger handoff` / `hydrate` | Seal `.kxp` / authorized open or `--live` rank |
| `kedger grant` / `revoke` | Workstream capability; revoke auto-reseals |
| `kedger share` / `unshare` / `anchors` | Explicit share ladder; Inv-Scope 404 |
| `kedger cognify` / `promote` / `why` | Episodes, promotion, provenance |
| `kedger hook` | IDE adapter entrypoint (Cursor / Claude Code) |

Override home with `KEDGER_HOME` (tests).

## Docs

- Constitution: [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md) (§0A)
- Status: [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md)
- Phase F (deferred): [`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md)

## Tests

```bash
pytest -q
```

## License

Apache-2.0
