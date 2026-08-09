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
- Do not open Phase F (LLM distill / sync / MCP) unless an SLI clearly demands it
- Keep Inv-Scope: unauthorized hydrate → uniform `not found` (404), no existence oracle

## What to test

- Unit / eval: `pytest -q`
- Cross-session path: `./scripts/smoke_transfer.sh`
- Hook install into a foreign temp repo (see `tests/test_init_hooks_install.py`)

## Public claims / launch copy

When writing README blurbs, issues, or social posts, follow [`docs/MARKETING.md`](docs/MARKETING.md) claim guardrails:

- Category is **sealed person-to-person agent handoff**, not a living repo wiki
- Share is **`explicit_only`**
- Proof line: alpha + mechanical tests — never “proven in production” / field study
- Never list Phase F (LLM distill / sync / MCP / at-rest DB encryption) as shipped

Peer break reports: use the **Peer handoff break** issue template.

## Docs

- Product locks: `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`
- Launch narrative: `docs/MARKETING.md`
- Deferred work: `docs/PHASE_F_DEFERRED.md`
- Changelog: `CHANGELOG.md`

## License

Contributions are under Apache-2.0 (see `LICENSE`).
