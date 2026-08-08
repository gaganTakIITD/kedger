# Kedger research program

This folder is the **Kedger** research corpus: deep-reads, inventories, pillar implementation memos, and Track 0 queues that feed measure → refine loops for the Kedger OSS memory product.

## MoDeX ≠ Kedger (historical labeling)

- **MoDeX** — the hackathon product in this repository. Keep its name, demo stack, and brand intact.
- **Kedger** — a **separate** OSS product (new repo). Different CLI, paths, packs, and identity.

Memos here often say “MoDeX” because they were written during the MoDeX project / architecture exploration. That is **historical labeling**, not a decision that MoDeX becomes Kedger.

When porting lessons into Kedger:

1. Copy useful mechanisms into Kedger docs/code under the **Kedger** name  
2. Do **not** rename MoDeX product docs, README, or submission materials to Kedger  
3. Do **not** describe Kedger as “MoDeX OSS” or “MoDeX v2”

Kedger design locks live under `docs/OPEN_SOURCE_MEMORY_ARCHITECTURE.md` and siblings; migration plan: `docs/KEDGER_NEW_REPO.md`.

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
5. privacy/capability  
6. eng-judgment  

```bash
python3 scripts/research/build_full_queue.py
python3 scripts/research/fetch_paper.py 2501.13956
```
