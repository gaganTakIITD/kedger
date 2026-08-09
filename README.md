<p align="center">
  <img src="docs/assets/kedger-banner.svg" alt="Kedger — local memory CLI" width="100%">
</p>

<p align="center">
  <strong>Kedger</strong> — local-first engineering memory for coding agents.<br/>
  Hooks capture the session. Anchors keep the decisions. Sealed <code>.kxp</code> packs hand off to the next agent — including a teammate’s.
</p>

<p align="center">
  <a href="https://github.com/gaganTakIITD/kedger/actions/workflows/ci.yml"><img src="https://github.com/gaganTakIITD/kedger/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/kedger/"><img src="https://img.shields.io/pypi/v/kedger" alt="PyPI"></a>
  <a href="https://pypi.org/project/kedger/"><img src="https://img.shields.io/pypi/pyversions/kedger" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License"></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/tip-0.1.1-0d1f2d.svg" alt="Tip 0.1.1"></a>
</p>

**Kedger ≠ MoDeX.** MoDeX is a separate hackathon product. This repo is the OSS eng-memory CLI: `~/.kedger/`, `.kxp`, `kedger.memory.v1`.

<p align="center">
  <img src="docs/assets/demo.gif" alt="Kedger demo: init, remember, handoff" width="720">
</p>

## Install (60 seconds)

```bash
cd /path/to/your-app
pip install "kedger>=0.1.1"
kedger init --name alice
```

One command → keys, repo policy, and IDE hooks:

| Lands in your repo | For |
|--------------------|-----|
| `.cursor/hooks.json` + `hooks/cursor/*` | Cursor |
| `.claude/settings.json` + `hooks/claude_code/*` | Claude Code |
| `.kedger/` | Repo policy |

Then **trust the workspace** in Cursor (or merge Claude’s `kedger.hooks.json` if you already had settings) and start a **new** chat.

```bash
kedger doctor
```

> Tip `0.1.1` is the launch surface. PyPI may still show `0.1.0` until the maintainer publishes — use a git install if needed:  
> `pip install "kedger @ git+https://github.com/gaganTakIITD/kedger.git@main"`

## Why it exists

Coding agents forget. Compact drops context. Teammates restart cold.

Kedger keeps **durable eng-memory** on your machine and ships a **sealed pack** the next session (or the next person) can open — Anchors for policy, an ops layer for files/`+/-`, and a zlib transcript when you need the raw turns.

## Two people, two agents

```text
Alice                                         Bob
─────                                         ───
kedger init --name alice                      kedger init --name bob
…agent works…                                 kedger peer card --out bob.kedger.json
                                         ◄──── send card (public keys only)
kedger peer send --to bob.kedger.json --out-dir ./xfer
────── send ./xfer/*.kxp ─────────────────►
                                              kedger peer open hf_….kxp
                                              kedger hydrate --live
                                              → new IDE chat
```

Same person, new machine: `pack-export` → `hydrate --pack` (no peer card).

## Everyday loop

```bash
# while you work — hooks ingest automatically
kedger cognify --force --promote   # or let preCompact do it
kedger hydrate --live              # preview next-agent context
kedger peer send --to bob.kedger.json --out-dir ./xfer
```

## Product locks

| | |
|--|--|
| CLI | `kedger` |
| Store | `~/.kedger/` |
| Packs | `*.kxp` |
| Schema | `kedger.memory.v1` |
| Share | `explicit_only` |

## Scope

**Shipped:** IDE hooks, deterministic claim extract, dual-layer handoff, zlib transcript, sealed packs, `peer card/send/open`.

**Not yet (Phase F):** LLM distill every turn, sync service, MCP, at-rest DB encryption — see [`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md).

## Contributing & community

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — setup, tests, PR norms
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- [`SECURITY.md`](SECURITY.md) — private reports for crypto/auth issues
- Issues: bug report + handoff-quality templates
- Launch/publish (PyPI + GitHub About): [`docs/PUBLISH.md`](docs/PUBLISH.md)
- Architecture: [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md)

```bash
pip install -e ".[dev]"
pytest -q
./scripts/smoke_transfer.sh
./scripts/smoke_wheel_install.sh
./scripts/smoke_peer_handoff.sh
```

## License

Apache-2.0 — see [`LICENSE`](LICENSE).
