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

- Hook packs: `hooks/` (also bundled as `kedger/hook_packs` in the wheel)
- Install into **caller** repo: `kedger hooks install` or `./hooks/install.sh`
- Dogfood configs in this repo: `.cursor/hooks.json`, `.claude/settings.json`
- Demo GIF: `docs/assets/demo.gif`
- PyPI: https://pypi.org/project/kedger/ — use **`>=0.1.1`** for this surface

## Test gate

```bash
pip install -e ".[dev]"
pytest -q
./scripts/smoke_transfer.sh
```

## Research program

- Corpus / matrix / eval harness under `docs/research/` (ongoing; not a launch blocker)
