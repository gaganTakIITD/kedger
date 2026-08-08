# Batch 8 — Ledger delta (for CORPUS_INVENTORY merge)

> **Date:** 2026-08-08  
> **Source memo:** `docs/research/batches/BATCH8_COMPRESS_RETRIEVE_FULL.md`  
> **Cache:** `/tmp/kedger-papers/full/{id}.txt`

Merge rule: set inventory depth to **FULL** for every row below (all new FULL for CORPUS §2 arXiv ledger; none were Batch4–Batch7 FULL; skipped duplicate Selective Context ID `2310.06201` already FULL as `2304.12102` in Batch6).

| ID | Title | Status | Prior FULL? | Memo |
|----|-------|--------|-------------|------|
| 2305.06983 | Active Retrieval Augmented Generation (FLARE) | **FULL** | no | BATCH8 |
| 2605.17301 | ConflictRAG — conflict-aware RAG framework | **FULL** | no | BATCH8 |
| 2212.10509 | Interleaving Retrieval with Chain-of-Thought (IRCoT) | **FULL** | no | BATCH8 |
| 2304.08467 | Learning to Compress Prompts with Gist Tokens | **FULL** | no | BATCH8 |
| 2310.06816 | Text Embeddings Reveal (Almost) As Much As Text | **FULL** | no | BATCH8 |
| 2311.09210 | Chain-of-Note (CoN) — robust RALM reading notes | **FULL** | no | BATCH8 |
| 2306.05499 | Prompt Injection attack against LLM-integrated Applications (HouYi) | **FULL** | no | BATCH8 |
| 2312.03414 | Compressed Context Memory for Online LM Interaction (CCM) | **FULL** | no | BATCH8 |
| 2409.05591 | MemoRAG — global memory-enhanced retrieval | **FULL** | no | BATCH8 |
| 2405.13792 | xRAG — extreme context compression with one token | **FULL** | no | BATCH8 |
| 2402.09727 | ReadAgent — human-inspired reading agent with gist memory | **FULL** | no | BATCH8 |
| 2406.03007 | BadAgent — backdoor attacks on LLM agents | **FULL** | no | BATCH8 |
| 2606.10525 | Assessing Automated Prompt Injection Attacks in Agentic Environments | **FULL** | no | BATCH8 |
| 2101.06804 | What Makes Good In-Context Examples for GPT-3 (KATE) | **FULL** | no | BATCH8 |
| 2402.03367 | RAG-Fusion — multi-query RRF retrieval | **FULL** | no | BATCH8 |
| adr-qoc-design-rationale | ADR / QOC / IBIS design-rationale practice (Nygard, MacLean, Gruber) | **FULL** | no | BATCH8 · eng-judgment |

## Counts

| Bucket | N |
|--------|--:|
| FULL (new arXiv) | 15 |
| FULL (eng-judgment non-arXiv) | 1 |
| **FULL total** | **16** |
| SKIPPED (duplicate ID) | 1 (`2310.06201` = Selective Context, already `2304.12102` BATCH6) |
| RE-READ | 0 |
| Fetch failures inventing content | 0 |

## Inventory queue updates suggested

Mark done / remove from “Next FULL-read” where applicable:

1. Batch6/Batch7 cache leftovers: FLARE, IRCoT, Gist, Chain-of-Note, ConflictRAG, MemoRAG, xRAG, ReadAgent, Text Embeddings Reveal, Prompt Injection apps — **FULL**  
2. Tier-6 compress/context: CCM (`2312.03414`), Gist (`2304.08467`) — **FULL**  
3. Hydrate/retrieve runway: KATE (`2101.06804`), RAG-Fusion (`2402.03367`) — **FULL**  
4. Agent integrity: BadAgent, automated PI in AgentDojo (`2606.10525`) — **FULL**  
5. Eng-judgment: ADR/QOC rationale capture — **FULL** (non-arXiv slug)

## Cached but skipped (duplicate / not new FULL)

| ID | Note |
|----|------|
| 2310.06201 | Same Selective Context paper as `2304.12102` (BATCH6 FULL) — body fetched, not re-marked |

## Successfully FULL ID list

```
2305.06983
2605.17301
2212.10509
2304.08467
2310.06816
2311.09210
2306.05499
2312.03414
2409.05591
2405.13792
2402.09727
2406.03007
2606.10525
2101.06804
2402.03367
adr-qoc-design-rationale
```
