# Batch 6 — Ledger delta (for CORPUS_INVENTORY merge)

> **Date:** 2026-08-08  
> **Source memo:** `docs/research/batches/BATCH6_CAPTURE_GRAPH_FULL.md`  
> **Cache:** `/tmp/kedger-papers/full/{id}.txt`

Merge rule: set inventory depth to **FULL** for every row below (all new FULL for CORPUS §2 arXiv ledger; none were Batch4/Batch5 FULL).

| ID | Title | Status | Prior FULL? | Memo |
|----|-------|--------|-------------|------|
| 2406.14550 | GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of LLMs | **FULL** | no (was queued) | BATCH6 |
| 2512.04668 | Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs (MAMA) | **FULL** | SHAREABLE/P6 under `ACL'26` slug only — arXiv ID newly ledgered | BATCH6 |
| 2310.05736 | LLMLingua: Compressing Prompts for Accelerated Inference of LLMs | **FULL** | no | BATCH6 |
| 2310.06839 | LongLLMLingua | **FULL** | no | BATCH6 |
| 2403.12968 | LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression | **FULL** | no | BATCH6 |
| 2310.04408 | RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation | **FULL** | no | BATCH6 |
| 2305.17118 | Scissorhands: Persistence of Importance for LLM KV Cache Compression | **FULL** | no | BATCH6 |
| 2406.02069 | PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | **FULL** | no | BATCH6 |
| 2406.10774 | Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference | **FULL** | no | BATCH6 |
| 2304.12102 | Selective Context (self-information content filtering) | **FULL** | no | BATCH6 |
| 2401.03462 | Activation Beacon / Long Context Compression with Activation Beacon | **FULL** | no | BATCH6 |
| 2305.08371 | SuperDialseg: A Large-scale Dataset for Supervised Dialogue Segmentation | **FULL** | no | BATCH6 |
| 2502.05589 | On Memory Construction and Retrieval for Personalized Conversational Agents (SeCom) | **FULL** | no | BATCH6 |
| 2308.10144 | ExpeL: LLM Agents Are Experiential Learners | **FULL** | no | BATCH6 |
| 2307.07697 | Think-on-Graph: Deep and Responsible Reasoning of LLM on Knowledge Graph | **FULL** | no | BATCH6 |
| 2310.00935 | Resolving Knowledge Conflicts in Large Language Models | **FULL** | no | BATCH6 |

## Counts

| Bucket | N |
|--------|--:|
| FULL (new) | 16 |
| RE-READ | 0 |
| Total cards | 16 |
| Fetch failures inventing content | 0 |

## Inventory queue updates suggested

Mark done / remove from “Next FULL-read” / survey-seed placeholders where applicable:

1. GraphReader (`2406.14550`) — FULL  
2. Topology Matters / MAMA (`2512.04668`) — FULL (replace `ACL'26` slug row with arXiv ID)  
3. Prompt compression cluster: LLMLingua / LongLLMLingua / LLMLingua-2 / RECOMP / Selective Context  
4. KV cluster: Scissorhands / PyramidKV / Quest / Activation Beacon  
5. SuperDialseg + SeCom (dialogue segmentation / segment memory)  
6. ExpeL, Think-on-Graph, Resolving Knowledge Conflicts  

## Cached but not carded this batch

| ID | Note |
|----|------|
| 2304.08467 | Gist Tokens — body cached |
| 2409.05591 | MemoRAG — body cached |
| 2305.06983 | Active Retrieval / FLARE — body cached |
| 2212.10509 | IRCoT — body cached |
| 2405.13792 | xRAG — body cached |
| 2311.09210 | Chain-of-Note — body cached |
| 2605.17301 | ConflictRAG — body cached |
| 2402.09727 | Reading Agent (gist memory) — PDF extract cached |

## Successfully FULL ID list

```
2406.14550
2512.04668
2310.05736
2310.06839
2403.12968
2310.04408
2305.17118
2406.02069
2406.10774
2304.12102
2401.03462
2305.08371
2502.05589
2308.10144
2307.07697
2310.00935
```
