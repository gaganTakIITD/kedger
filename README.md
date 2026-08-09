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

## Install

```bash
pip install "kedger>=0.1.1"
```

From this repository (development tip):

```bash
pip install -e ".[dev]"
```

Requires Python 3.11+.

> **Note:** PyPI `0.1.0` is an earlier release without `pack-export` / `transcript` / `init`. Use **`>=0.1.1`** for the launch surface documented here.

## First run (any git repo)

```bash
cd /path/to/your-app
pip install "kedger>=0.1.1"
kedger init --name me          # keys + .kedger/ policy + IDE hooks
# Cursor: trust this workspace for project hooks, then start a new chat
kedger remember reject "Do not use cookie sessions" --reason "CSRF"
kedger cognify --force --promote
kedger hydrate --live
kedger doctor
```

`kedger init` installs into **this** repo:

| Written | IDE |
|---------|-----|
| `.cursor/hooks.json` + `hooks/cursor/*` | Cursor |
| `.claude/settings.json` (or `kedger.hooks.json` to merge) + `hooks/claude_code/*` | Claude Code |
| `.kedger/` policy | both |

List anchors and explain one:

```bash
kedger anchors
kedger why <anchor_id>         # use an id from `kedger anchors`
```

## Cross-session handoff

Three layers in a sealed pack:

| Layer | What | Transfer |
|-------|------|----------|
| Base | Anchors (constraints, rejections, decisions) | Lossy, inject-default |
| Activity | Files edited, `+/-` lines, tool fails | Lossy ops digest |
| Transcript | Full redacted turn tape, **zlib** | Lossless restore |

```bash
# Session A
kedger cognify --force --promote
kedger pack-export --out-dir /tmp/kedger-xfer

# Session B (new machine / wiped store / peer with grant)
kedger hydrate --pack /tmp/kedger-xfer/hf_….kxp
kedger hydrate --live
kedger transcript show --live
```

Peer handoff: `keys export-recipient` → peer `keys import-recipient` → `grant` → reseal/`pack-export` → peer `hydrate --pack`.

Smoke the wipe→restore path:

```bash
./scripts/smoke_transfer.sh
```

## IDE hooks (Cursor / Claude Code)

```bash
kedger hooks install --target both
# or: ./hooks/install.sh both   (installs into *your* repo cwd/git root)
```

Adapters call `kedger hook --source cursor|claude_code` with stdin JSON. Core never imports IDE types. Session start injects authorized hydrate context when memory exists.

## CLI

| Command | Behavior |
|---------|----------|
| `kedger init` | First-run: keys + policy + optional hooks |
| `kedger hooks install` | Copy Cursor/Claude packs into a repo |
| `kedger keys init\|show\|export-recipient\|import-recipient` | Principal + peer TOFU |
| `kedger remember` / `forget` | Anchors; forget via SUPERSEDES |
| `kedger status` / `doctor` | Fingerprint, layers, HEAD/queue health |
| `kedger ingest --from-hook` | L0 observation (redact-before-persist) |
| `kedger handoff` / `pack-export` / `hydrate` | Seal / export pack+sidecar / open+**import** or `--live` |
| `kedger transcript stats\|show\|decompress` | Zlib turn-tape transfer |
| `kedger grant` / `revoke` | Workstream capability; revoke auto-reseals |
| `kedger share` / `unshare` / `anchors` | Explicit share ladder; Inv-Scope 404 |
| `kedger cognify [--promote]` / `promote` / `why` | Episodes, promotion, provenance |
| `kedger hook` | IDE adapter entrypoint |

Override home with `KEDGER_HOME` (tests).

## Scope (honest)

**Supported now:** eng-memory capture via IDE hooks, deterministic claim extract, dual-layer handoff (Anchors + activity), zlib transcript transfer, sealed `.kxp` packs, local grant/revoke.

**Deferred (Phase F):** LLM distill every turn, sync service, MCP tools, at-rest DB encryption — see [`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md).

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
./scripts/smoke_wheel_install.sh   # wheel → foreign repo → init → transfer
```

## License

Apache-2.0
