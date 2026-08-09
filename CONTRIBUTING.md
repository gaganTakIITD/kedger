# Contributing to Kedger

Thanks for helping. Kedger is **not** MoDeX — keep naming, paths, and product story separate.

## Dev setup

```bash
git clone https://github.com/gaganTakIITD/kedger.git
cd kedger
pip install -e ".[dev]"
pytest -q
./scripts/smoke_transfer.sh
```

Python 3.11+ required. Override store location with `KEDGER_HOME`.

## Branch / PR norms

- Feature branches: `Cursor/<descriptive-name>-fb37` (lowercase)
- Prefer small, focused PRs with tests for behavior changes
- Do not open Phase F (LLM distill / sync / MCP) unless an SLI clearly demands it
- Keep Inv-Scope: unauthorized hydrate → uniform `not found` (404), no existence oracle

## What to test

- Unit / eval: `pytest -q`
- Cross-session path: `./scripts/smoke_transfer.sh`
- Hook install into a foreign temp repo (see `tests/test_hooks_install.py`)

## Docs

- Product locks: `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`
- Deferred work: `docs/PHASE_F_DEFERRED.md`
- Changelog: `CHANGELOG.md`

## License

Contributions are under Apache-2.0 (see `LICENSE`).
