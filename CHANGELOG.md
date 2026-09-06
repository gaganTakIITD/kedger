# Changelog

All notable changes to Kedger are documented here.

## Unreleased

## [0.2.2] — 2026-09-06

Second Phase F slice: **OS keychain storage for the store encryption key** (opt-in SQLCipher unchanged; plaintext still default).

### Added

- Store encryption key stored in OS keychain by default when `keyring` is available (Windows Credential Locker, macOS Keychain, Linux Secret Service/KWallet)
- Key resolution precedence: `KEDGER_STORE_KEY` env → OS keyring → `~/.kedger/keys/store.key`
- `kedger store status` and `kedger doctor` report where the store key was resolved from
- `--key-file` on `kedger store encrypt` and `kedger init --encrypt-store` to force file-based key storage (headless/CI fallback)
- `keyring` added to `kedger[encrypted]` optional dependency

### Upgrade notes (0.2.1 → 0.2.2)

```bash
pip install -U "kedger[encrypted]>=0.2.2"
```

Existing file-based keys keep working. New encrypt operations prefer OS keychain when available.

### Honest gaps (still true at 0.2.2)

- Phase F is **not** complete — at-rest DB encryption + OS keychain key only; no LLM distill or sync
- `raw/` observation payloads and `.kxp` pack files on disk are not encrypted by this slice
- Human peer trials rows 1–5 pending — [`docs/PEER_TRIALS.md`](docs/PEER_TRIALS.md)

## [0.2.1] — 2026-09-06

First Phase F slice: **optional SQLCipher at-rest encryption** for `~/.kedger/` store.sqlite (opt-in; plaintext remains default for upgrade compatibility).

### Added

- `kedger store encrypt` — migrate plaintext `store.sqlite` → SQLCipher (creates `~/.kedger/keys/store.key`)
- `kedger store status` — report encryption state for current repo
- `kedger init --encrypt-store` — create encrypted store on first run
- `KEDGER_STORE_KEY` env override (base64 or hex, 32 bytes) for containers/CI
- Optional extra: `pip install "kedger[encrypted]"` (pulls `sqlcipher3`)
- Doctor: reports encryption state; warns on plaintext; **fail-closed** when encrypted store key is missing

### Upgrade notes (0.2.0 → 0.2.1)

```bash
pip install -U "kedger[encrypted]>=0.2.1"
```

Encryption is **off by default**. Existing plaintext stores keep working unchanged.

To enable:

```bash
kedger store encrypt          # migrate current repo store
# or on fresh init:
kedger init --encrypt-store
```

### Honest gaps (still true at 0.2.1)

- Phase F is **not** complete — only at-rest DB encryption slice; no LLM distill, sync, or full MCP Phase F
- OS keychain integration for store key deferred (file + env for now)
- `raw/` observation payloads and pack files on disk are not encrypted by this slice
- Human peer trials rows 1–5 pending — [`docs/PEER_TRIALS.md`](docs/PEER_TRIALS.md)

## [0.2.0] — 2026-09-05 (beta)

Production-path beta: P0–P3 (#32–#34) + MCP/inject hardening (#36) — trustworthy tests, prompt-time inject, capture/promote honesty, handoff/retrieve quality.

### P0 — Trustworthy tests & fail-soft hooks (#32)

- `tests/time_helpers.recent_ts()` — unfreeze time-dependent L0-TTL eval fixtures
- Hook adapters exit 0 when `kedger` is missing from PATH (never block prompts)
- Dynamic timestamps in `scripts/smoke_transfer.sh`

### P1 — Prompt-time inject + minimal MCP (#32)

- `beforeSubmitPrompt` / `UserPromptSubmit` hydrate inject (reliable fallback when SessionStart drops)
- Wider SessionStart inject: evidence snippets + unresolved conflicts
- `kedger mcp serve|call` with `hydrate` and `anchors_get` tools
- Verification checklist: [`docs/PROMPT_INJECT_VERIFY.md`](docs/PROMPT_INJECT_VERIFY.md)
- MCP/inject hardening (#36): fail-soft MCP config merge on init and hooks install; `scripts/smoke_prompt_inject.sh`; doctor warns when hooks lack MCP registration

### P2 — Capture & promote honesty (#33)

- Claim extract honesty: Idempotency-Key cues, ASCII dash splits, lead-said policy, junk filters
- `kedger consolidate` + `cognify --consolidate` for near-dup Anchor merge
- Surface-K hydrate (`--surface-k`), kind quotas, evidence on projection
- Cursor `postToolUse` hook; Claude PostToolUse for Shell/Bash
- Safe auto-merge of Claude `settings.json` on `hooks install`; warn on failure

### P3 — Handoff & retrieve quality (#34)

- HippoRAG-style `seed_idf_scores` on PPR expand / notebook walk
- Dual-path Evidence + Anchors packing (`handoff/dual_path.py`) under separate byte quotas
- Delay-k L0 soft-stale eviction (Anchors never touched)
- Doctor: warns on unmerged Claude hooks, SessionStart-only inject, empty L0 with hooks, clock skew
- `scripts/peer_trial.sh` — one-command Alice→Bob smoke; log in [`docs/PEER_TRIALS.md`](docs/PEER_TRIALS.md)

### Upgrade notes (0.1.x → 0.2.0)

```bash
pip install -U "kedger>=0.2.0"
```

1. **Re-install hooks** in each app repo after upgrade:
   ```bash
   kedger hooks install --target cursor    # or claude_code
   ```
   P2 adds `postToolUse`; P1 adds `beforeSubmitPrompt` / `UserPromptSubmit` inject paths.
2. **Verify inject** with [`docs/PROMPT_INJECT_VERIFY.md`](docs/PROMPT_INJECT_VERIFY.md) — SessionStart may drop on cloud agents; rely on per-prompt inject or MCP `hydrate`.
3. **No schema migration** — `kedger.memory.v1` store and `.kxp` packs remain compatible.
4. **New CLI surface:** `kedger consolidate`, `kedger cognify --consolidate`, `kedger hydrate --surface-k`, `kedger mcp serve|call|tools-list`.
5. **Development status** moves from Alpha → **Beta** (mechanical CI + strict evals; not a field study).

### Honest gaps (still true at 0.2.0)

- Human peer trials rows 1–5 pending — [`docs/PEER_TRIALS.md`](docs/PEER_TRIALS.md)
- Inject platform limits (SessionStart fire-and-forget) — see PROMPT_INJECT_VERIFY
- Phase F (encryption at rest, LLM distill, sync) deferred — [`docs/PHASE_F_DEFERRED.md`](docs/PHASE_F_DEFERRED.md)

### Research / performance (Batch26)

- Fresh arXiv scrape: **1674** agent-memory/efficiency IDs → **300** priority runway
- Deep-read load-bearing set → `BATCH26_COST_CONSOLIDATE_FULL.md` + `BATCH26_RETRIEVE_KV_PERF_FULL.md`
- Roadmap: [`docs/research/PERFORMANCE_PROGRESS_ROADMAP.md`](docs/research/PERFORMANCE_PROGRESS_ROADMAP.md) (alias `memory-perf-roadmap.md`)
- P0 tickets: seed IDF on PPR · dual-path 32KB packing · delay-k L0 soft-stale

### Docs / launch

- README: **L0–L4 memory layers** panel + why this architecture (research lessons table)
- Honest **500 FULL ledger** research signal linked from README / About
- New asset: `docs/assets/memory-layers.png`
- Casual problem pitch, explicit_only privacy, LinkedIn paste pack, peer trial template

## [0.1.1] — 2026-08-09

Launch-ready eng-memory CLI surface (supersedes thinner PyPI `0.1.0`).

### Added
- `kedger init` — keys + repo policy + optional IDE hook install
- `kedger hooks install` — copy Cursor/Claude packs into **caller** repo (cwd/git root)
- `kedger peer card|add|send|open` — least-friction two-person agent handoff
- `grant --to` optional when recipient card carries `principal_id`
- Dual-layer handoff: Anchors + agent activity (`+/-` lines, files, tool fails)
- Lossless zlib transcript archive + `kedger transcript stats|show|decompress`
- `kedger pack-export` — export `.kxp` (+ sidecar) for transfer
- Durable `hydrate --pack` import (Anchors + activity + transcript + local HEAD)
- `cognify --promote`, preCompact auto-promote+reseal, hot soft-boundary promote
- `keys import-recipient` for peer TOFU
- Strict handoff quality benches + wipe/import dogfood + `scripts/smoke_transfer.sh`
- Doctor: activity/transcript layers, promotion queue, handoff HEAD
- GitHub Actions CI (`pytest -q`)

### Fixed
- Hook `install.sh` no longer writes into the Kedger source tree when run from another repo
- Messy unlabeled capture (never-log, secrets-in-logs, cue-stacked rambles)
- Theme-aware promote/import near-dup dedupe
- Empty sessionStart no longer pollutes transcript / burns empty hydrate context
- `smoke_transfer.sh` no longer trips `pipefail` SIGPIPE on CI (`ls \| head`)

### Docs / community
- `SECURITY.md`, issue templates, Trusted Publisher `release.yml`
- `scripts/smoke_wheel_install.sh` tip-to-tip wheel dogfood
- GitHub launch surface: pixel CLI banner/listing/idea-flow assets, CoC, PR template, About checklist
- Brand renderer `scripts/render_brand_assets.py`

### Honest scope
- Phase F (LLM distill, sync, MCP) remains deferred — see `docs/PHASE_F_DEFERRED.md`

## [0.1.0] — 2026-08-08

Initial PyPI claim: keys, remember/forget, cognify, sealed `.kxp`, basic hooks.
