# Kedger Implementation Status

> **Kedger ≠ MoDeX.**  
> Date: 2026-08-08

## Landed (this repo)

| Phase | Branch (suffix `-2e45`) | Contents |
|-------|-------------------------|----------|
| A scaffold | `Cursor/phase-a-scaffold-2e45` | store, keys, remember/forget, status, doctor, ingest |
| B scaffold | `Cursor/phase-b-sealed-handoff-2e45` | `.kxp` seal/hydrate, grant/revoke |
| A harden | `Cursor/phase-a-harden-2e45` | redact, L0 rotation, WorkingState budget, signed caps, `.kedger/` policy |
| B harden | `Cursor/phase-b-harden-2e45` | STREAM, share/unshare, PART D, auto-reseal |
| C | `Cursor/phase-c-cognify-2e45` | boundary + cognify + episodes |
| D | `Cursor/phase-d-graph-promote-2e45` | resolve, graph, promote, compose, why, live hydrate |
| E | `Cursor/phase-e-hooks-2e45` | Cursor/Claude hooks + `kedger hook` |
| F | deferred | see [`PHASE_F_DEFERRED.md`](PHASE_F_DEFERRED.md) |

## CLI surface (A–E)

```text
kedger keys init|show|export-recipient
kedger remember|forget|status|doctor|ingest
kedger handoff|hydrate|grant|revoke
kedger share|unshare|anchors
kedger cognify|promote|why|hook
```

## Product (v0.1.0)

- Cursor / Claude hook packs wired under `hooks/` + project install via `hooks/install.sh`
- Dogfood configs committed: `.cursor/hooks.json`, `.claude/settings.json`
- Demo GIF: `docs/assets/demo.gif`
- Release tag: `v0.1.0` · PyPI: https://pypi.org/project/kedger/0.1.0/

## Research → Measure → Refine

- Corpus runway: [`docs/research/queue/FULL_QUEUE_500.md`](research/queue/FULL_QUEUE_500.md) (500 slots)
- Stage matrix: [`docs/research/KEDGER_STAGE_RESEARCH_MATRIX.md`](research/KEDGER_STAGE_RESEARCH_MATRIX.md)
- Eval harness: [`docs/research/EVAL_HARNESS.md`](research/EVAL_HARNESS.md) + `tests/eval/`
- Cadence: [`docs/research/RESEARCH_CADENCE.md`](research/RESEARCH_CADENCE.md)
- Batch 4: [`docs/research/batches/BATCH4_EVAL_SYSTEMS_FULL.md`](research/batches/BATCH4_EVAL_SYSTEMS_FULL.md)

## Test gate

```bash
pip install -e ".[dev]"
pytest -q
```
