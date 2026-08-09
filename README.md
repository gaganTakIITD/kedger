# Kedger

Local-first CLI for durable engineering memory and sealed session handoff.

**Kedger ≠ MoDeX.** MoDeX is a separate hackathon product. Kedger is its own OSS eng-memory engine: hooks → CLI → Anchors → sealed packs (`.kxp`).

![Kedger demo](docs/assets/demo.gif)

| Lock | Value |
|------|--------|
| CLI | `kedger` |
| Version | `0.1.1` |
| Private store | `~/.kedger/` |
| Repo policy | `<repo>/.kedger/` |
| Packs | `*.kxp` |
| Schema | `kedger.memory.v1` |
| Share mode | `explicit_only` |

## Install (60 seconds)

Python 3.11+. In **your app repo**:

```bash
cd /path/to/your-app
pip install "kedger>=0.1.1"
kedger init --name alice
```

That one command creates keys, repo policy (`.kedger/`), and IDE hook packs:

| Written | Purpose |
|---------|---------|
| `~/.kedger/keys/` | Your principal (private; stays on your machine) |
| `.kedger/` | Repo policy |
| `.cursor/hooks.json` + `hooks/cursor/*` | Cursor adapters |
| `.claude/settings.json` + `hooks/claude_code/*` | Claude Code adapters |

Then:

1. **Cursor:** trust this workspace for project hooks → start a **new** chat  
2. **Claude Code:** if you already had `.claude/settings.json`, merge `.claude/kedger.hooks.json` once  
3. Work normally — hooks ingest turns; session start injects memory when it exists

> PyPI `0.1.0` is thinner (no `init` / `peer` / transcript). Use **`>=0.1.1`**.  
> Dev tip: `pip install -e ".[dev]"` from this repo.

Verify:

```bash
kedger doctor
kedger remember reject "Do not use cookie sessions" --reason CSRF
kedger cognify --force --promote
kedger hydrate --live
```

## Two people, two agents (least friction)

Alice’s agent builds memory. Bob’s agent should continue **without** re-deriving the constraints.

```text
Alice machine                         Bob machine
─────────────                         ───────────
kedger init --name alice              kedger init --name bob
…agent works, memory grows…           kedger peer card --out bob.kedger.json
                                      ── send bob.kedger.json ──►
kedger peer send --to bob.kedger.json --out-dir ./xfer
── send ./xfer/*.kxp (+ sidecar) ──►
                                      kedger peer open hf_….kxp
                                      kedger hydrate --live
                                      → new IDE chat (sessionStart inject)
```

### Commands

| Who | Command | What |
|-----|---------|------|
| Bob | `kedger peer card` | Public card only (safe to Slack/email) |
| Alice | `kedger peer send --to bob.kedger.json --out-dir ./xfer` | Grant + seal + export pack |
| Bob | `kedger peer open hf_….kxp` | Import Anchors + activity + transcript |
| Bob | `kedger hydrate --live` | Preview what the next agent gets |

Same person, new machine / wiped store (no peer card needed):

```bash
kedger cognify --force --promote
kedger pack-export --out-dir ./xfer
# later / elsewhere, same keys:
kedger hydrate --pack ./xfer/hf_….kxp
kedger hydrate --live
```

Pack layers:

| Layer | What | Transfer |
|-------|------|----------|
| Base | Anchors (constraints, rejections, decisions) | Lossy, inject-default |
| Activity | Files edited, `+/-` lines, tool fails | Lossy ops digest |
| Transcript | Full redacted turn tape, **zlib** | Lossless restore |

## IDE hooks

Hooks ship **inside the wheel**. Prefer the CLI (no Kedger git clone required):

```bash
kedger hooks install --target both                 # cwd / git root
kedger hooks install --target cursor --repo ~/app
```

Source checkout fallback: `./hooks/install.sh both` (installs into **your** repo, not the Kedger tree).

## CLI

| Command | Behavior |
|---------|----------|
| `kedger init` | Keys + policy + IDE hooks |
| `kedger hooks install` | Copy Cursor/Claude packs into a repo |
| `kedger peer card\|add\|send\|open` | Two-person sealed handoff |
| `kedger keys …` | Principal + low-level recipient export/import |
| `kedger remember` / `forget` | Anchors; forget via SUPERSEDES |
| `kedger status` / `doctor` | Fingerprint, layers, HEAD/queue health |
| `kedger handoff` / `pack-export` / `hydrate` | Seal / export / open+import or `--live` |
| `kedger transcript …` | Zlib turn-tape |
| `kedger grant` / `revoke` | Capability (used by `peer send`) |
| `kedger cognify [--promote]` / `promote` / `why` | Episodes + provenance |
| `kedger hook` | IDE adapter entrypoint |

Override home with `KEDGER_HOME` (tests).

## Scope (honest)

**Supported:** eng-memory via IDE hooks, deterministic claim extract, dual-layer handoff, zlib transcript, sealed `.kxp`, local peer grant/revoke.

**Deferred (Phase F):** LLM distill every turn, sync service, MCP, at-rest DB encryption — [`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md).

## Docs

- Constitution: [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md)
- Status: [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md)
- Security: [`SECURITY.md`](SECURITY.md)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Publish: [`docs/PUBLISH.md`](docs/PUBLISH.md)

## Tests

```bash
pip install -e ".[dev]"
pytest -q
./scripts/smoke_transfer.sh
./scripts/smoke_wheel_install.sh
./scripts/smoke_peer_handoff.sh
```

## License

Apache-2.0
