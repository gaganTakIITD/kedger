<p align="center">
  <img src="docs/assets/kedger-banner.png" alt="Kedger — your next agent remembers" width="100%">
</p>

<p align="center">
  <b>Kedger</b> is local-first <b>sealed session handoff</b> for coding agents.<br/>
  Hooks capture the session. Anchors keep the decisions. A sealed <code>.kxp</code> hands context to the next agent — on your machine or a teammate’s.<br/>
  <i>Not a living repo wiki — share is explicit and encrypted.</i>
</p>

<p align="center">
  <a href="https://github.com/gaganTakIITD/kedger/actions/workflows/ci.yml"><img src="https://github.com/gaganTakIITD/kedger/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/kedger/"><img src="https://img.shields.io/pypi/v/kedger" alt="PyPI"></a>
  <a href="https://pypi.org/project/kedger/"><img src="https://img.shields.io/pypi/pyversions/kedger" alt="Python"></a>
  <a href="https://pypi.org/project/kedger/"><img src="https://img.shields.io/pypi/dm/kedger" alt="Downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-0a1622.svg?labelColor=071018&color=5eead4" alt="Apache-2.0"></a>
  <a href="https://github.com/gaganTakIITD/kedger/stargazers"><img src="https://img.shields.io/github/stars/gaganTakIITD/kedger?style=flat&labelColor=071018&color=5eead4" alt="Stars"></a>
</p>

<p align="center">
  <a href="#install-60-seconds"><b>Install</b></a> ·
  <a href="#what-it-looks-like"><b>See it</b></a> ·
  <a href="#two-people-two-agents"><b>Peer handoff</b></a> ·
  <a href="docs/MARKETING.md"><b>Launch playbook</b></a>
</p>

## The problem

Your teammate’s agent doesn’t inherit your last Cursor / Claude chat. New chats restart cold. Slack summaries go lossy. A repo wiki is a different product.

<p align="center">
  <img src="docs/assets/before-after.png" alt="Without Kedger: cold start. With Kedger: hydrate --live shows rejects, decisions, ops." width="100%">
</p>

## What Kedger does

<p align="center">
  <img src="docs/assets/idea-flow.png" alt="Session → Memory → Pack → Next agent" width="100%">
</p>

1. **Session** — Cursor / Claude hooks ingest turns (redacted) into `~/.kedger/`
2. **Memory** — cognify promotes durable **Anchors** (constraints, rejections, decisions) plus an **ops** layer (files, `+/-`, tool fails)
3. **Pack** — seal a `.kxp` (optional zlib transcript for lossless restore)
4. **Next** — hydrate into a new chat, or send a pack to a teammate

No cloud sync required. Keys stay local unless you explicitly send a pack (`share_mode=explicit_only`). Redact-on-ingest; treat a sent `.kxp` like a private handoff doc.

## What it looks like

<p align="center">
  <img src="docs/assets/demo.gif" alt="Kedger terminal demo" width="720">
</p>

```bash
kedger remember reject "no Redis — use Postgres"
kedger cognify --force --promote
kedger hydrate --live
# → Anchors + ops the next agent will see
```

## Install (60 seconds)

```bash
pip install "kedger>=0.1.1"
cd /path/to/your-app
kedger init --name alice
```

`init` writes keys, `.kedger/` policy, and IDE hook packs (Cursor + Claude). Trust the workspace / merge Claude settings once, then start a **new** chat.

## Two people, two agents

<p align="center">
  <img src="docs/assets/peer-story.png" alt="Alice seals a .kxp; Bob opens it and hydrates" width="100%">
</p>

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

Same person / new machine: `pack-export` → `hydrate --pack` (no peer card).

## CLI

<p align="center">
  <img src="docs/assets/cli-listing.png" alt="Kedger CLI command listing" width="100%">
</p>

```bash
kedger doctor                 # health + product locks
kedger remember reject "…"    # durable policy Anchor
kedger cognify --force --promote
kedger hydrate --live         # what the next agent will see
```

## Product locks

| Lock | Value |
|------|--------|
| CLI | `kedger` |
| Tip | `0.1.1` on [PyPI](https://pypi.org/project/kedger/) |
| Store | `~/.kedger/` |
| Packs | `*.kxp` · schema `kedger.memory.v1` |
| Share | `explicit_only` |

**Shipped:** IDE hooks, claim extract, dual-layer handoff, zlib transcript, sealed packs, peer card/send/open.

**Not yet (do not claim):** LLM distill every turn, sync service, MCP, at-rest DB encryption — [`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md).

**Proof posture:** Alpha OSS. Mechanically tested handoff (CI + strict evals + smoke scripts). Not a published user study.

## Contributing & launch

- Star + share if peer handoff solves a pain you’ve hit
- Break a peer trial? → [Peer handoff issue](https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml)
- [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) · [`SECURITY.md`](SECURITY.md)
- Launch narrative / LinkedIn paste pack: [`docs/MARKETING.md`](docs/MARKETING.md)
- Peer trial log: [`docs/PEER_TRIALS.md`](docs/PEER_TRIALS.md)
- Publish / About: [`docs/PUBLISH.md`](docs/PUBLISH.md)
- Architecture: [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md)

```bash
pip install -e ".[dev]"
pytest -q
./scripts/smoke_transfer.sh && ./scripts/smoke_wheel_install.sh && ./scripts/smoke_peer_handoff.sh
```

## License

Apache-2.0 — [`LICENSE`](LICENSE).
