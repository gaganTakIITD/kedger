<p align="center">
  <img src="docs/assets/kedger-banner.png" alt="Kedger — code is versioned; judgment isn't" width="100%">
</p>

<p align="center">
  <b>Kedger</b> — casual local-first memory for coding agents.<br/>
  Git remembers <i>what</i> changed. Agent chats remember <i>why</i>… until they don’t.<br/>
  Kedger keeps the <b>why</b> — decisions, rejects, constraints — and lets you hand it to the next agent.
</p>

<p align="center">
  <a href="https://github.com/gaganTakIITD/kedger/actions/workflows/ci.yml"><img src="https://github.com/gaganTakIITD/kedger/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/kedger/"><img src="https://img.shields.io/pypi/v/kedger" alt="PyPI"></a>
  <a href="https://pypi.org/project/kedger/"><img src="https://img.shields.io/pypi/pyversions/kedger" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-0a1622.svg?labelColor=071018&color=5eead4" alt="Apache-2.0"></a>
  <a href="https://github.com/gaganTakIITD/kedger/stargazers"><img src="https://img.shields.io/github/stars/gaganTakIITD/kedger?style=flat&labelColor=071018&color=5eead4" alt="Stars"></a>
</p>

<p align="center">
  <a href="#why-use-this"><b>Why</b></a> ·
  <a href="#how-it-helps-a-team"><b>Team</b></a> ·
  <a href="#memory-model-casual-version"><b>Memory</b></a> ·
  <a href="#privacy-tradeoff-why-no-ambient-sharing"><b>Privacy</b></a> ·
  <a href="#install-60-seconds"><b>Install</b></a>
</p>

---

## The problem we’re actually solving

Engineering teams now do real work *inside* Cursor / Claude sessions.

Then the chat ends. Context compacts. A teammate opens the same repo.

Their agent starts **cold**.

You already lived through:

- “Wait, why not Redis?”
- “Didn’t we reject cookie sessions?”
- “Which files did the last agent actually touch?”
- Slack paste that loses half the judgment

**Code is versioned. Judgment isn’t.**

That’s the gap Kedger exists for — not another living wiki of the whole codebase, and not a cloud “team brain” that syncs everything by default.

<p align="center">
  <img src="docs/assets/before-after.png" alt="Without Kedger: cold start. With Kedger: hydrate shows rejects, decisions, ops." width="100%">
</p>

## Why use this

Use Kedger if you want the **next agent** (you tomorrow, or a teammate today) to boot with:

1. **What we decided**  
2. **What we rejected** (negative knowledge is gold)  
3. **What constraints still bind**  
4. **What files / ops were in flight**

…without dumping the whole transcript into git, and without putting session memory on someone else’s server.

Skip Kedger if you mainly want a **repo documentation wiki** that drifts with the code graph — different product, different job.

## How it helps a team

Team help here is **handoff**, not ambient contact sharing.

```text
Alice’s agent learns the hard parts
        │
        ▼
   Anchors + ops land in her local store
        │
        ▼
   she seals a .kxp for Bob (on purpose)
        │
        ▼
   Bob opens it → hydrate → new chat continues
```

<p align="center">
  <img src="docs/assets/peer-story.png" alt="Alice seals a .kxp; Bob opens and hydrates" width="100%">
</p>

So the team benefit is: **judgment can move with the work**, the same way a branch moves — when someone chooses to pass it.

Same person / new laptop works the same way (`pack-export` → `hydrate --pack`). No peer card required.

## Why this shape (and not ambient sharing)

We deliberately chose **`share_mode=explicit_only`**.

| Tempting design | Why we didn’t |
|-----------------|---------------|
| Auto-sync everyone’s agent memory to a shared cloud | Session judgment is sensitive; sync becomes a leak surface |
| Commit memory into the repo as Markdown by default | Mixes private reasoning with code review; wiki drift ≠ session handoff |
| “Always-on team brain” day one | Forces trust + governance before the core loop even works |

**Kedger’s bet:** make capture + Anchors + sealed handoff excellent first.  
Share is a **sealed file** (`.kxp`) you send like a private USB stick — Slack, Drive, USB — encrypted to the recipient’s keys.

No ambient contact graph. No “everyone in the org can read your chat memory.”  
Easy continuity for people **on the task**. Hard/no continuity for everyone else.

## Memory model (casual version)

Kedger does **not** treat “the raw chat log” as memory.

```text
session turns  →  redact  →  local store
                      ↓
                 cognify / promote
                      ↓
              Anchors (survive compact)
              + ops layer (files, +/- , tool fails)
              + optional transcript sidecar
                      ↓
                 seal .kxp  →  hydrate
```

<p align="center">
  <img src="docs/assets/idea-flow.png" alt="Session → Memory → Pack → Next" width="100%">
</p>

### Anchors — the thing that must survive

Tiny typed judgments. Under pressure, these stay; fluff dies.

| Kind | Example |
|------|---------|
| **rejection** | “Do not use Redis — use Postgres” |
| **decision** | “Use Argon2id for password hashing” |
| **constraint** | “Must send Idempotency-Key on charge create” |
| goal / next_step / gotcha / open_question | the rest of the working set |

If the next agent only gets a handful of lines, those lines should still be the **policy**, not a random transcript middle.

### Ops layer — what the agent *did*

Files touched, edit totals, tool fails. So hydrate isn’t only philosophy — it’s also “here’s the mess on disk.”

### Graph (lightweight, not a science project)

Memory links **Anchors ↔ entities ↔ episodes** (files, modules, workstreams, validity over time).  
Retrieval for hydrate walks that graph under a budget — it doesn’t dump the whole store into the prompt.

Deep lock: [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md).

## Privacy tradeoff

**Defaults that are true today**

- Store lives under `~/.kedger/` (not the source of truth in git)
- Redact-before-persist on ingest
- Share only when you seal + send a `.kxp`
- Peer **card** = public keys only (safe to Slack)
- Unauthorized open fails closed (`not found`) — no “yes that pack exists, here’s a peek”

**Tradeoff we accept**

- You must **actively** send a pack (friction by design)
- Revoke + reseal stops *new* packs; old offline `.kxp` files stay readable to old keys (crypto reality — we say it out loud)
- Full DB at-rest encryption is later ([`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md))

If you didn’t send a pack, they don’t get your session. That’s the product.

## What it looks like

<p align="center">
  <img src="docs/assets/demo.gif" alt="Kedger terminal demo" width="720">
</p>

```bash
kedger remember reject "no Redis — use Postgres"
kedger cognify --force --promote
kedger hydrate --live
# → what the next agent will see
```

## Install (60 seconds)

```bash
pip install "kedger>=0.1.1"
cd /path/to/your-app
kedger init --name alice
```

`init` writes keys, repo policy, and Cursor / Claude hook packs. Trust the workspace once, start a **new** chat, keep working. Kedger captures in the background.

## Two people, two agents

```text
Alice                                         Bob
─────                                         ───
kedger init --name alice                      kedger init --name bob
…agent works…                                 kedger peer card --out bob.kedger.json
                                         ◄──── card (public keys only)
kedger peer send --to bob.kedger.json --out-dir ./xfer
────── send ./xfer/*.kxp ─────────────────►
                                              kedger peer open hf_….kxp
                                              kedger hydrate --live
                                              → new IDE chat with Alice’s Anchors
```

## CLI

<p align="center">
  <img src="docs/assets/cli-listing.png" alt="Kedger CLI listing" width="100%">
</p>

```bash
kedger doctor                 # health + locks (share_mode=explicit_only)
kedger remember reject "…"    # durable Anchor
kedger cognify --force --promote
kedger hydrate --live         # next-agent preview
kedger peer card|send|open    # person-to-person sealed handoff
```

## Product locks

| Lock | Value |
|------|--------|
| CLI | `kedger` |
| Tip | `0.1.1` on [PyPI](https://pypi.org/project/kedger/) |
| Store | `~/.kedger/` |
| Packs | `*.kxp` · `kedger.memory.v1` |
| Share | `explicit_only` |

**Shipped:** hooks, claim extract, Anchors + ops, zlib transcript, sealed packs, peer card/send/open.  
**Not yet:** LLM-every-turn distill, sync service, MCP — [`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md).  
**Proof:** Alpha. Mechanically tested (CI + strict handoff evals). Not a published user study.

## Contributing

- Peer break? → [issue template](https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml)
- [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`SECURITY.md`](SECURITY.md) · [`docs/MARKETING.md`](docs/MARKETING.md)
- Architecture constitution: [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md)

```bash
pip install -e ".[dev]"
pytest -q
./scripts/smoke_transfer.sh && ./scripts/smoke_wheel_install.sh && ./scripts/smoke_peer_handoff.sh
```

## License

Apache-2.0 — [`LICENSE`](LICENSE).
