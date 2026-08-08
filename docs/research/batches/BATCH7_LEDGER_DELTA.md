# Batch 7 — Ledger delta (for CORPUS_INVENTORY merge)

> **Date:** 2026-08-08  
> **Source memo:** `docs/research/batches/BATCH7_PRIVACY_SEAL_FULL.md`  
> **Cache:** `/tmp/kedger-papers/full/{id}.txt`

Merge rule: set inventory depth to **FULL** for every row below (all new FULL for CORPUS §2 arXiv ledger; none were Batch4/Batch5/Batch6 FULL; avoided ConfAIde/CaMeL/Fides/AgentLeak/MemLeak/MAMA).

| ID | Title | Status | Prior FULL? | Memo |
|----|-------|--------|-------------|------|
| 2502.13172 | Unveiling Privacy Risks in LLM Agent Memory (MEXTRA) | **FULL** | no | BATCH7 |
| 2407.12784 | AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases | **FULL** | no | BATCH7 |
| 2503.03704 | Memory Injection Attacks on LLM Agents via Query-Only Interaction (MINJA) | **FULL** | no | BATCH7 |
| 2402.17840 | Follow My Instruction and Spill the Beans (RAG datastore extraction) | **FULL** | no | BATCH7 |
| 2402.07867 | PoisonedRAG: Knowledge Corruption Attacks to RAG | **FULL** | no | BATCH7 |
| 2403.02691 | InjecAgent: Benchmarking Indirect Prompt Injections in Tool Agents | **FULL** | no | BATCH7 |
| 2406.13352 | AgentDojo: Dynamic Environment for PI Attacks/Defenses | **FULL** | no | BATCH7 |
| 2405.05175 | AirGapAgent: Protecting Privacy-Conscious Conversational Agents | **FULL** | no | BATCH7 |
| 2504.11703 | Progent: Securing AI Agents with Privilege Control | **FULL** | no | BATCH7 |
| 2409.00138 | PrivacyLens: Evaluating Privacy Norm Awareness of LMs in Action | **FULL** | no | BATCH7 |
| 2312.14197 | BIPIA: Benchmarking and Defending Against Indirect Prompt Injection | **FULL** | no | BATCH7 |
| 2405.20446 | Is My Data in Your Retrieval Database? (RAG MIA) | **FULL** | no | BATCH7 |
| 2305.03010 | Sentence Embedding Leaks More Information than You Expect (GEIA) | **FULL** | no | BATCH7 |
| 2411.01705 | Data Extraction Attacks in RAG via Backdoors | **FULL** | no | BATCH7 |
| 2510.05244 | Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks? | **FULL** | no | BATCH7 |
| 2607.21325 | Toward cryptographically verifiable authorization for autonomous AI agents (CVA) | **FULL** | no | BATCH7 |

## Counts

| Bucket | N |
|--------|--:|
| FULL (new) | 16 |
| RE-READ | 0 |
| Total cards | 16 |
| Fetch failures inventing content | 0 |

## Inventory queue updates suggested

Mark done / remove from “Next FULL-read” / survey-seed placeholders where applicable:

1. MEXTRA / agent memory extraction (`2502.13172`) — FULL  
2. AgentPoison + MINJA + PoisonedRAG memory/RAG poison cluster — FULL  
3. Spill the Beans + RAG backdoor extract + RAG MIA + GEIA leakage cluster — FULL  
4. InjecAgent + AgentDojo + BIPIA + IPI Firewalls PI bench/defense cluster — FULL  
5. AirGapAgent + PrivacyLens CI/action norms — FULL  
6. Progent privilege control + CVA verifiable authz — FULL  

## Cached but not carded this batch

| ID | Note |
|----|------|
| 2406.03007 | BadAgent — body cached |
| 2310.06816 | Text Embeddings Reveal (Almost) As Much As Text — body cached |
| 2606.10525 | Assessing Automated Prompt Injection Attacks in Agentic Environments — body cached |
| 2306.05499 | Prompt Injection attack against LLM-integrated Applications — body cached |

## Successfully FULL ID list

```
2502.13172
2407.12784
2503.03704
2402.17840
2402.07867
2403.02691
2406.13352
2405.05175
2504.11703
2409.00138
2312.14197
2405.20446
2305.03010
2411.01705
2510.05244
2607.21325
```
