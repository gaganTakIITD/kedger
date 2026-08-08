# Batch 4 — Ledger delta (for CORPUS_INVENTORY merge)

> **Date:** 2026-08-08  
> **Source memo:** `docs/research/batches/BATCH4_EVAL_SYSTEMS_FULL.md`  
> **Cache:** `/tmp/kedger-papers/full/{id}.txt`

Merge rule: set inventory depth to **FULL** if status is FULL; if RE-READ, keep prior FULL and add Batch4 memo pointer + Kedger-stage note.

| ID | Title | Status | Prior FULL? | Memo |
|----|-------|--------|-------------|------|
| 2512.22716 | Memento 2: Learning by Stateful Reflective Memory | **FULL** | no | BATCH4 |
| 2605.12493 | LongMemEval-V2 | **FULL** | no | BATCH4 |
| 2602.16313 | MemoryArena | **FULL** | no (was survey-queued) | BATCH4 |
| 2511.06449 | FLEX: Continuous Agent Evolution via Forward Learning from Experience | **FULL** | no (was survey-queued as “FLEX”) | BATCH4 |
| 2502.09597 | PrefEval | **FULL** | no | BATCH4 |
| 2310.17884 | ConfAIde / Can LLMs Keep a Secret? | **RE-READ** | yes (Batch2, P6) | BATCH4 (S6/S8 metrics) |
| 2506.21605 | MemBench | **RE-READ** | yes (BATCH_SYSTEMS) | BATCH4 |
| 2511.03506 | HaluMem | **RE-READ** | yes (BATCH_SYSTEMS) | BATCH4 |
| 2601.06966 | RealMem | **RE-READ** | yes (P5 ★) | BATCH4 |
| 2503.18813 | CaMeL | **RE-READ** | yes (P6 PDF); was “queued” in CORPUS next-batch list — mark inventory queue cleared | BATCH4 |
| 2507.05257 | MemoryAgentBench | **RE-READ** | yes (Batch2/P2) | BATCH4 (AR/TTL/LRU/SF→fixtures) |
| 2402.17753 | LoCoMo | **RE-READ** | yes (Batch2) | BATCH4 (temporal fixtures) |
| 2410.10813 | LongMemEval | **RE-READ** | yes (P2/P5/Batch2) | BATCH4 (abstention) |
| 2505.23643 | Fides IFC | **RE-READ** | yes (Batch2/P6) | BATCH4 |
| 2602.11510 | AgentLeak | **RE-READ** | yes (SHAREABLE/P6) | BATCH4 |
| 2606.29788 | MemLeak | **RE-READ** | yes (SHAREABLE/P6) | BATCH4 |

## Counts

| Bucket | N |
|--------|--:|
| FULL (new) | 5 |
| RE-READ | 11 |
| Total cards | 16 |
| Fetch failures inventing content | 0 |

## Inventory queue updates suggested

Mark done / remove from “Next FULL-read batches”:

1. CaMeL (2503.18813) — RE-READ complete  
2. Memento 2 (2512.22716) — FULL  
3. LongMemEval-V2 (2605.12493) — FULL  
4. MemoryArena — ID **2602.16313** (not 2604.xxx) — FULL  
5. FLEX — ID **2511.06449** — FULL  

## Cached but not carded this batch

| ID | Note |
|----|------|
| 2507.07957 | MIRIX — body cached; prior FULL in BATCH_SYSTEMS |
| 2510.17281 | MemoryBench (continual feedback) — body cached; prior FULL in Batch3 |

## Successfully FULL/RE-READ ID list

```
2512.22716
2605.12493
2602.16313
2511.06449
2502.09597
2310.17884
2506.21605
2511.03506
2601.06966
2503.18813
2507.05257
2402.17753
2410.10813
2505.23643
2602.11510
2606.29788
```
