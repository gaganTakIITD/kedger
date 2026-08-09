# Batch 26 — Retrieve · PPR · KV Compaction Lessons (Kedger)

> **Date:** 2026-08-09  
> **Branch:** `Cursor/batch26-perf-roadmap-fb37`  
> **Scope:** Retrieval graphs (HippoRAG), GraphReader-style walks, and **online KV compaction** papers — extract lessons for Kedger hydrate/L0 **without** productizing a KV-cache memory layer.  
> **Companion:** [`BATCH26_COST_CONSOLIDATE_FULL.md`](BATCH26_COST_CONSOLIDATE_FULL.md) · [`BATCH26_PERF_HIPPO_KV_CLUSTER_CARDS.md`](BATCH26_PERF_HIPPO_KV_CLUSTER_CARDS.md) (extra-detailed numbers) · [`PERFORMANCE_PROGRESS_ROADMAP.md`](../PERFORMANCE_PROGRESS_ROADMAP.md)

---

## 0. Honesty table

| Status | Count | Notes |
|--------|------:|-------|
| **FULL** new/re-read bodies this memo | **14** | HippoRAG, HippoRAG2, StreamingLLM, H2O, SnapKV, Online KV Agents, InfLLM (reuse), Know-What-to-Drop, ShadowKV, EpiCache, AnchorKV, SCBench, GraphReader (reuse), CacheGen |
| **Thin HTML skipped as FULL** | 2 | `2410.02603`, `2505.23416` abs-thin — not marked FULL |
| **Prior Batch8 FULL reused** | FLARE, IRCoT, CoN, MemoRAG, xRAG, Gist, CCM, ReadAgent | cost/retrieve already carded |

---

## 1. Mechanism cards

### 1.1 HippoRAG — Neurobiologically Inspired LTM  
**arXiv:2405.14831** · Jiménez Gutiérrez et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Multi-hop knowledge integration; passages encoded in isolation fail associative recall. |
| **representation** | LLM → schemaless KG (hippocampal index); query concepts as PPR seeds; Personalized PageRank explores paths; synonym edges via embedding similarity. |
| **write / read / forget** | Offline index build; online PPR retrieve. |
| **conflict** | Silent on SUPERSEDES. |
| **privacy** | Silent. |
| **numbers** | Up to **~20 points** over strong RAG on multi-hop QA; ~**3** and **~20** point gains on two popular multi-hop benchmarks (paper abstract/body). Discusses **IDF** as global importance prior for node activation. |
| **kedger_lessons** | (1) Kedger `associative_expand` uses PPR **d=0.5** but **uniform seed=1.0** — add **seed IDF**. (2) Synonym/ALIAS already τ=0.8. (3) Do not replace Anchors with passage corpus. |
| **metric_impact** | Multi-hop recall@budget; QA F1. |
| **refine_candidate** | **yes** — **P0 seed IDF on PPR** |

---

### 1.2 From RAG to Memory (HippoRAG 2 line)  
**arXiv:2502.14802** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Continual non-parametric memory beyond one-shot RAG. |
| **representation** | Extends HippoRAG-style indexing toward continual memory integration. |
| **write / read / forget** | Continual index updates; PPR-style read. |
| **conflict** | Continual update vs forgetting. |
| **privacy** | Silent. |
| **kedger_lessons** | Supports offline graph refresh on cognify boundaries — not SessionStart rebuilds. |
| **metric_impact** | Continual multi-hop. |
| **refine_candidate** | yes — tied to seed-IDF / offline graph refresh |

---

### 1.3 GraphReader — Graph-based Agent for Long Context  
**arXiv:2406.14550** · 2024 · **FULL** (reuse + confirm)

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S7 |
| **problem** | Long context → agent should walk a graph with a notebook, not dump text. |
| **representation** | Coarse-to-fine walk; notebook of facts; call budget. |
| **kedger_lessons** | **Maintain** `notebook_walk` + `--notebook-calls`. |
| **refine_candidate** | no |

---

### 1.4 StreamingLLM — Attention Sinks  
**arXiv:2309.17453** · Xiao et al. · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2 |
| **problem** | Window attention collapses when early KV evicted; need streaming with finite cache. |
| **representation** | Keep **attention sink** (initial tokens’ KV) + sliding window; up to **4M** tokens streaming; up to **22.2×** vs sliding-window recomputation. |
| **write / read / forget** | Evict middle KV; keep sinks + recent. |
| **kedger_lessons** | (1) Sinks ≠ semantic importance — **do not** map sink logic onto Anchors. (2) L0 may soft-stale middle observations; Anchors stay. (3) **Reject** product KV layer in Kedger. |
| **refine_candidate** | **yes** — P0 delay-k / soft-stale L0 only |

---

### 1.5 H₂O — Heavy-Hitter Oracle  
**arXiv:2306.14048** · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1 |
| **problem** | KV grows with sequence; evict low-attention tokens. |
| **representation** | Retain heavy-hitter tokens by cumulative attention. |
| **kedger_lessons** | Attention mass ≠ Anchor importance; survival rank stays symbolic. Optional L0 priority heuristic only. |
| **refine_candidate** | no (L0 delay-k covers intent) |

---

### 1.6 SnapKV — Prefill-aware KV Selection  
**arXiv:2404.14469** · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7 |
| **problem** | Select important KV before generation. |
| **representation** | Observation window → cluster/select KV for decode. |
| **kedger_lessons** | Prefill selection analogy: hydrate should select under budget **before** inject — already true; don’t import SnapKV into store. |
| **refine_candidate** | no |

---

### 1.7 Practical Online KV Cache Compaction for LLM Agents  
**arXiv:2608.00902** · Liu et al. · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3 |
| **problem** | Agent trajectories inflate KV; most compaction assumes static future queries. |
| **representation** | Online compaction across token eviction & attention matching; proxies: boundary, repeat-prefill, **delayed future-generation** queries. |
| **numbers** | BrowseComp-Plus / WideSearch: **immediate compaction often hurts**; **delaying** compaction to use agent’s future queries recovers performance (paper abstract/body). |
| **kedger_lessons** | (1) **Delay-k** before hard L0 flush. (2) Boundary-triggered cognify already “delay” — extend soft-stale. (3) Still **reject** shipping KV compaction as Kedger feature. |
| **refine_candidate** | **yes** — **P0 delay-k soft-stale L0** |

---

### 1.8 InfLLM — Training-Free Long-Context Extrapolation  
**arXiv:2402.04617** · 2024 · **FULL** (cached)

| Field | Content |
|-------|---------|
| **kedger_stages** | S7 |
| **problem** | Long context without training. |
| **representation** | Block-level memory + lookup. |
| **kedger_lessons** | Block lookup ≈ episode digests; maintain L2. |
| **refine_candidate** | no |

---

### 1.9 LLMs Know What to Drop  
**arXiv:2503.08879** · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S7 |
| **problem** | Self-attention guided KV eviction. |
| **representation** | Model-internal importance for drop decisions. |
| **kedger_lessons** | For Kedger, drop order is **SURVIVAL_RANK** — keep symbolic. |
| **refine_candidate** | no |

---

### 1.10 ShadowKV · EpiCache · AnchorKV · SCBench · CacheGen  
**arXiv:** 2410.21465 · 2509.17396 · 2606.17872 · 2412.10319 · 2310.07240 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1 (infra) |
| **problem** | Serving-side KV throughput / episodic KV / safety-aware compression / benchmarks / KV streaming. |
| **kedger_lessons** | Useful as **negative space**: these optimize GPU serving. Kedger optimizes **symbolic handoff bytes**. Do not merge roadmaps. AnchorKV name collision ≠ Kedger Anchors. |
| **refine_candidate** | no — **REJECT** product KV |

---

## 2. Batch refine tickets

| ID | Ticket | Priority |
|----|--------|----------|
| B26-R1 | Seed IDF weighting in `associative_expand` / notebook seeds | **P0** |
| B26-R2 | Delay-k soft-stale on L0 observations only | **P0** |
| B26-R3 | Document REJECT: no Kedger KV-cache product surface | docs |

---

## 3. Cross-link to prior FULL (reuse)

FLARE (active retrieve), IRCoT (interleave), Chain-of-Note (evidence notes), MemoRAG/xRAG (retrieve compress), Gist (instruction compress ≠ Anchor compress), CCM — see Batch8. All reinforce: **budgeted retrieve + don’t gist-compress Anchor statements**.
