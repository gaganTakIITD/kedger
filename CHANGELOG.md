# Changelog

All notable changes to Kedger are documented here.

## Unreleased

### Docs / launch

- README rewrite: casual problem pitch — *code is versioned; judgment isn’t*
- Why use us / team help as handoff / why `explicit_only` (no ambient share)
- Anchors + ops + graph pitched in-README (not docs-only)
- About description + MARKETING positioning aligned to judgment-memory wedge
- LinkedIn paste pack + claim guardrails + peer dogfood protocol
- Issue template: peer handoff breaks; social preview reminder script

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
