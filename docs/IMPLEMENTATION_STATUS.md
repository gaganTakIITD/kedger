# Kedger Implementation Status

> **Kedger ≠ MoDeX.**  
> Date: 2026-08-09 · Version tip: **0.1.1**

## Landed (eng-memory CLI)

| Area | Status |
|------|--------|
| Store / keys / remember / forget | Done |
| Sealed `.kxp` handoff + grant/revoke | Done |
| Cognify + promote + why + live hydrate | Done |
| IDE hooks (Cursor / Claude) + `kedger hook` | Done |
| Dual-layer handoff (Anchors + activity) | Done |
| Zlib transcript archive + CLI | Done |
| Durable pack import + HEAD install | Done |
| `kedger init` / `kedger hooks install` | Done |
| Strict evals + smoke_transfer | Done |
| Phase F (LLM / sync / MCP) | Deferred — [`PHASE_F_DEFERRED.md`](PHASE_F_DEFERRED.md) |

## CLI surface (0.1.1)

```text
kedger init
kedger hooks install
kedger keys init|show|export-recipient|import-recipient
kedger remember|forget|status|doctor|ingest
kedger handoff|pack-export|hydrate
kedger transcript stats|show|decompress
kedger grant|revoke|share|unshare|anchors
kedger cognify [--promote]|promote|why|hook
```

## Product

- Hook packs: keep `hooks/` and `src/kedger/hook_packs/` in sync (wheel ships the latter)
- Install into **caller** repo: `kedger hooks install` or `./hooks/install.sh`
- Dogfood configs in this repo: `.cursor/hooks.json`, `.claude/settings.json`
- Demo GIF: `docs/assets/demo.gif`
- PyPI: https://pypi.org/project/kedger/ — use **`>=0.1.1`** for this surface

## Test gate

```bash
pip install -e ".[dev]"
bash scripts/check_hook_packs_sync.sh
pytest -q
./scripts/smoke_transfer.sh
./scripts/smoke_wheel_install.sh
```

## Launch remaining (maintainer)

1. Merge PR tip → `main` (CI green)
2. Configure PyPI Trusted Publisher + GitHub `pypi` environment
3. Tag `v0.1.1` → Release workflow (or manual twine)
4. Confirm PyPI shows `0.1.1`

## Research program

- Corpus / matrix / eval harness under `docs/research/` (ongoing; not a launch blocker)
