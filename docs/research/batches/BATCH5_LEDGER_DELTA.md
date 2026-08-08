# Batch 5 — Ledger delta (for CORPUS_INVENTORY merge)

> **Date:** 2026-08-08  
> **Source memo:** `docs/research/batches/BATCH5_EVAL_FAILURE_FULL.md`  
> **Cache:** `/tmp/kedger-papers/full/{id}.txt` (PDF for LongBench / LongBench v2)

Merge rule: set inventory depth to **FULL** for every row below (all new FULL; no RE-READ this batch).

| ID | Title | Status | Prior FULL? | Memo |
|----|-------|--------|-------------|------|
| 2308.03688 | AgentBench: Evaluating LLMs as Agents | **FULL** | no | BATCH5 |
| 2311.12983 | GAIA: a benchmark for General AI Assistants | **FULL** | no | BATCH5 |
| 2307.13854 | WebArena: A Realistic Web Environment for Building Autonomous Agents | **FULL** | no | BATCH5 |
| 2406.04744 | CRAG — Comprehensive RAG Benchmark | **FULL** | no | BATCH5 |
| 2401.15884 | Corrective Retrieval Augmented Generation | **FULL** | no | BATCH5 |
| 2401.15391 | MultiHop-RAG | **FULL** | no | BATCH5 |
| 2305.13300 | Adaptive Chameleon or Stubborn Sloth (knowledge conflicts / ConflictQA lineage) | **FULL** | no | BATCH5 |
| 2310.03214 | FreshLLMs / FreshQA | **FULL** | no | BATCH5 |
| 2308.14508 | LongBench | **FULL** | no | BATCH5 (PDF) |
| 2412.15204 | LongBench v2 | **FULL** | no | BATCH5 (PDF) |
| 2404.06654 | RULER | **FULL** | no | BATCH5 |
| 2402.13718 | ∞Bench (InfiniteBench) | **FULL** | no | BATCH5 |
| 2310.11511 | Self-RAG | **FULL** | no | BATCH5 |
| 2309.01431 | RGB — Retrieval-Augmented Generation Benchmark | **FULL** | no | BATCH5 |
| 2402.16288 | PerLTQA | **FULL** | no | BATCH5 |
| 2407.11963 | NeedleBench | **FULL** | no | BATCH5 |
| 1809.09600 | HotpotQA | **FULL** | no | BATCH5 |
| 2011.01060 | 2WikiMultiHopQA | **FULL** | no | BATCH5 |

## Counts

| Bucket | N |
|--------|--:|
| FULL (new) | 18 |
| RE-READ | 0 |
| Total cards | 18 |
| Fetch failures inventing content | 0 |

## Inventory queue updates suggested

Mark done / remove from tier-1 seed placeholders once queue rebuild runs:

1. AgentBench → `2308.03688`  
2. GAIA → `2311.12983`  
3. WebArena → `2307.13854`  
4. RGB → `2309.01431`  
5. CRAG (Comprehensive) → `2406.04744`  
6. MultiHop-RAG → `2401.15391`  
7. HotpotQA → `1809.09600`  
8. 2WikiMultiHopQA → `2011.01060`  
9. ConflictQA / knowledge conflict → `2305.13300`  
10. FreshQA → `2310.03214`  
11. PerLTQA → `2402.16288`  
12. Needle / NIAH protocols → `2407.11963` (+ RULER `2404.06654`)  
13. RULER → `2404.06654`  
14. ∞Bench → `2402.13718`  
15. LongBench / LongBench-v2 → `2308.14508` / `2412.15204`  
16. Self-RAG / corrective retrieval → `2310.11511` + `2401.15884`

## Successfully FULL ID list

```
2308.03688
2311.12983
2307.13854
2406.04744
2401.15884
2401.15391
2305.13300
2310.03214
2308.14508
2412.15204
2404.06654
2402.13718
2310.11511
2309.01431
2402.16288
2407.11963
1809.09600
2011.01060
```
