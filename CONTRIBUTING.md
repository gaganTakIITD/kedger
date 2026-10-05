# Contributing to Kedger

Thanks for helping. Keep naming, paths, and product story aligned with the locks in [`docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`](docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md).

## Dev setup

```bash
git clone https://github.com/gaganTakIITD/kedger.git
cd kedger
pip install -e ".[dev]"
bash scripts/check_hook_packs_sync.sh
pytest -q
./scripts/smoke_transfer.sh
./scripts/smoke_wheel_install.sh
./scripts/smoke_peer_handoff.sh
```

When editing IDE packs, update **both** `hooks/` and `src/kedger/hook_packs/`.

Python 3.11+ required. Override store location with `KEDGER_HOME`.

## Branch / PR norms

- Feature branches: `Cursor/<descriptive-name>-fb37` (lowercase)
- Prefer small, focused PRs with tests for behavior changes
- Do not open remaining Phase F (live sync service, MCP-as-primary, LLM-every-turn) unless an SLI clearly demands it — see [`docs/ROADMAP.md`](docs/ROADMAP.md)
- Keep Inv-Scope: unauthorized hydrate → uniform `not found` (404), no existence oracle

## What to test

- Unit / eval: `pytest -q`
- Cross-session path: `./scripts/smoke_transfer.sh`
- Hook install into a foreign temp repo (see `tests/test_init_hooks_install.py`)

## Public claims / launch copy

When writing README blurbs, issues, or social posts, follow [`docs/MARKETING.md`](docs/MARKETING.md) claim guardrails:

- Category is **sealed person-to-person agent handoff**, not a living repo wiki
- Share is **`explicit_only`**
- Proof line: beta + mechanical tests — never “proven in production” / field study
- Claim shipped Phase F **slices** (opt-in SQLCipher, opt-in LLM distill, `.kxs` export/import, minimal MCP). Do not list live sync, full Phase F, MCP-as-primary, or “encrypted by default” as shipped

Peer break reports: use the **Peer handoff break** issue template.

## Docs

- Product locks: `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`
- Proveability / go-ahead: `docs/ROADMAP.md`
- Launch narrative: `docs/MARKETING.md`
- Deferred work: `docs/PHASE_F_DEFERRED.md`
- Changelog: `CHANGELOG.md`

## License

Contributions are under Apache-2.0 (see `LICENSE`).
