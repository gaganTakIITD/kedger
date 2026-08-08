# Research batch + eval gate cadence

> **Program:** Research → Measure → Refine  
> **Phase F:** Closed unless an SLI/fixture gap explicitly requires an allowed slice in [`PHASE_F_DEFERRED.md`](../PHASE_F_DEFERRED.md).

## Research batch agent (Track 1)

Each batch (15–25 papers):

1. Fetch full HTML/PDF via `scripts/research/fetch_paper.py` → `/tmp/kedger-papers/full/{id}.html`  
2. Write mechanism cards (problem / write-read-forget / conflict / privacy / Kedger lessons)  
3. Tag `kedger_stages`, `metric_impact`, `refine_candidate`  
4. Append ledger delta under `docs/research/batches/`  
5. Merge into `CORPUS_INVENTORY.md` + rebuild queue (`python3 scripts/research/build_full_queue.py`)  
6. Emit ≤3 refine tickets tied to failing/missing metrics  
7. **Never** mark abstract-only as FULL; never invent unfetched content  

Running FULL total toward **500+** is cumulative across batches. Queue size ≥500 is the runway, not the FULL count.

## Eval agent (Track 2)

Before merging a refine PR:

```bash
pip install -e ".[dev]"
pytest -q
pytest -q tests/eval
```

Block merge on Inv-Scope regressions, budget violations, or `anchor_drop_violations != 0`.

Publish SLI samples to `artifacts/eval/` (gitignored scratch OK).

## Refine agent (Track 3)

For each ticket:

1. Cite paper id or fixture id  
2. Capture before SLI / fixture status  
3. One focused PR  
4. Re-measure; update stage matrix + inventory `refine_candidate`  

## Progress counters

| Counter | Where |
|---------|-------|
| FULL card count | `CORPUS_INVENTORY.md` §0 |
| Queue runway | `queue/full_queue.jsonl` (len ≥ 500) |
| Fixture / SLI green | `pytest -q tests/eval` |
| Refine citations | PR body + stage matrix |

## Phase F entry (only when)

Deterministic cognify fixtures plateau **and** a measured gap requires optional `--llm-distill`, MCP read tools, or SQLCipher — then open a dedicated PR series. Default remains: do not start F.
