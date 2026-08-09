# Changelog

All notable changes to Kedger are documented here.

## Unreleased

### Close memory gaps (Phase F closed)

- **Extract faithfulness** — `Idempotency-Key` intact; ASCII ` - ` policy splits; lead-said kept; vague verify-thing junked
- **`kedger consolidate`** — sleep-time near-dup Anchor merge via SUPERSEDES; skips ESCALATE conflicts; `--dry-run`; optional `cognify --consolidate`
- **Visible surface + kind quotas** — `VISIBLE_SURFACE_K`, `hydrate --surface-k`, `HYDRATE_KIND_CAPS` (+ purpose allowlist)
- **SessionStart inject honesty** — capped Evidence snippets + conflicts in `additionalContext` (≤ `INJECT_MAX_CHARS`); not a session clone
- **Promote recurrence** — `promote --mode normal` θ/heat path gated; conservative default unchanged
- Eval: `tests/eval/test_close_memory_gaps.py` + extract unit battery

### Performance P0 (Batch26 refine)

- **Seed IDF on PPR** — `seed_idf_scores` weights rare Anchors/entities before `associative_expand` / `notebook_walk` (HippoRAG-style; `PPR_DAMPING=0.5` kept)
- **Dual-path Evidence + Anchors** — separate Evidence byte/item quotas under `HANDOFF_MAX_BYTES=32768`; Evidence drops before policy Anchors; pack import restores Evidence
- **Delay-k soft-stale on L0** — `L0_DELAY_K=3` soft-marks overflow under warn; flush prefers soft_stale; Anchors never attention-evicted
- Eval gates: `tests/eval/test_p0_memory_perf.py` (IDF / dual-path / delay-k + Q1–Q3 accuracy SLIs)

### Research / performance (Batch26)

- Fresh arXiv scrape: **1674** agent-memory/efficiency IDs → **300** priority runway
- Deep-read load-bearing set → `BATCH26_COST_CONSOLIDATE_FULL.md` + `BATCH26_RETRIEVE_KV_PERF_FULL.md`
- Roadmap: [`docs/research/PERFORMANCE_PROGRESS_ROADMAP.md`](docs/research/PERFORMANCE_PROGRESS_ROADMAP.md) (alias `memory-perf-roadmap.md`)

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
