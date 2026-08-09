# Kedger research program

This folder is the **Kedger** research corpus: deep-reads, inventories, pillar implementation memos, and Track 0 queues that feed measure → refine loops for the Kedger OSS memory product.

Older memos may use legacy product labels in prose. When porting lessons into code, use **Kedger** locks only (`kedger`, `~/.kedger/`, `.kxp`, `kedger.memory.v1`).

Kedger design locks: `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md`. Repository notes: `docs/KEDGER_NEW_REPO.md`.

## Tracks

| Track | Artifact | Role |
|-------|----------|------|
| 0 | `CORPUS_INVENTORY.md` | Honest FULL vs survey-indexed ledger + Kedger stage columns |
| 0 | `queue/FULL_QUEUE_500.md` + `full_queue.jsonl` | Prioritized ≥500 FULL deep-read runway |
| 0 | `scripts/research/build_full_queue.py` / `fetch_paper.py` | Rebuild queue; fetch bodies → `/tmp/kedger-papers/full/` |
| 1 | `KEDGER_STAGE_RESEARCH_MATRIX.md` | S1–S8 lit → code → experiment |
| 1 | `batches/` | FULL deep-read batch memos (Batch4+) |
| 2 | `EVAL_HARNESS.md` + `tests/eval/` | Governance, MAB/LoCoMo/HaluMem projections, SLIs |
| 3 | stage matrix `refine_candidate` | Evidence-gated code refinements |
| 4 | `RESEARCH_CADENCE.md` | Batch agent + eval gate; Phase F stays closed |

**Honesty rule:** never mark a paper `FULL` from title/abstract alone. `seed_placeholder` rows are fetch-needed pads, not deep-reads.

### Priority tiers (queued work)

1. eval/failure  
2. capture/compaction  
3. episode/boundary  
4. graph/conflict  
