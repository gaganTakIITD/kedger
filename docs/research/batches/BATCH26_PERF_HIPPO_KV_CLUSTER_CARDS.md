# Kedger mechanism cards — HippoRAG + KV-cache cluster

Deep-read from `/tmp/kedger-papers/full/{id}.txt`. Silent where the paper is silent. Numbers quoted from paper text only.

Kedger map (locked today): `associative_expand` PPR **d=0.5**, **no IDF yet**; L0 ring buffer (warn 0.70 / flush 0.85); **Anchors never attention-evicted**; HANDOFF **32KB**.

---

## Card: HippoRAG

| Field | Content |
|-------|---------|
| **arxiv_id** | 2405.14831 |
| **title** | HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models |
| **kedger_stages** | S5, S7 |
| **problem** | Standard RAG cannot integrate knowledge across passages in one step; iterative multi-hop retrieval is expensive and still fails path-finding multi-hop. |
| **representation** | Schemaless open KG from OpenIE triples (phrase nodes + relation edges) + synonym edges when \(\cos(M(e_i),M(e_j))>\tau\); passage occurrence matrix \(\mathbf{P}\) aggregates node mass → passages. |
| **write_read_forget** | **Write:** LLM OpenIE (named entities → triples with broader phrases) + synonym edges. **Read:** query NER → link to KG nodes → Personalized PageRank with equal reset mass on query seeds → rank passages by \(\vv{n}'\mathbf{P}\). **Node specificity (IDF-like):** \(s_i=\|P_i\|^{-1}\) multiplies each query-node reset probability before PPR. **Forget:** none (append-only index). |
| **conflict** | Silent (coexistence + rank). |
| **privacy** | Silent. |
| **numbers** | \(\tau=0.8\); PPR damping **0.5** (tuned on 100 MuSiQue train). Single-step HippoRAG (ColBERTv2): MuSiQue R@2/R@5 **40.9/51.9**, 2Wiki **70.7/89.1**, HotpotQA **60.5/77.7**, Avg **57.4/72.9**. Gains vs dense: ~**+11/+20** R@2/R@5 on 2Wiki, ~**+3** on MuSiQue. IRCoT+HippoRAG complementary (~**+4** MuSiQue / **+18** 2Wiki R@5). QA F1 up to **+3 / +17 / +1** (MuSiQue / 2Wiki / HotpotQA). Online retrieval **10–30×** cheaper and **6–13×** faster than IRCoT. Ablation w/o node specificity: Avg R@2/R@5 **54.7/70.9** (vs 57.4/72.9). |
| **kedger_lessons** | Map KG+PPR to hydrate **associative_expand** (d=0.5), not Anchor truth. **Seed IDF/node-specificity before PPR** — Kedger today uses uniform seed score `1.0` (`expand.py`); paper multiplies reset by \(s_i=\|P_i\|^{-1}\). Synonym/alias edges for file/API names. Never treat OpenIE triples as sealed Anchors. |
| **metric_impact** | multi-hop hydrate recall@budget; spectrum C01/C07; associative expand quality |
| **refine_candidate** | **yes** — ticket: **P0 Seed IDF on PPR** (weight seeds by rarity / entity document frequency; keep `PPR_DAMPING=0.5`) |

---

## Card: From RAG to Memory / HippoRAG 2

| Field | Content |
|-------|---------|
| **arxiv_id** | 2502.14802 |
| **title** | From RAG to Memory: Non-Parametric Continual Learning for Large Language Models (HippoRAG 2) |
| **kedger_stages** | S5, S7, S8 |
| **problem** | HippoRAG’s entity-centric seeding loses context and underperforms factual/sense-making vs strong embedding RAG; need one system for factual, sense-making, and associative memory. |
| **representation** | Phrase nodes + relation edges + **passage nodes** with `contains` edges; synonym edges retained (\(\tau=0.8\)). KG indexes retrieval; does **not** expand corpus with generative summaries (critique of GraphRAG/LightRAG). |
| **write_read_forget** | **Write:** OpenIE triples + synonym + passage nodes. **Read:** query→triple embedding match (default) → LLM **recognition memory** filter on top-**5** triples → PPR seeds (phrase + all passage nodes; passage reset × weight factor) → top-**5** passages for QA. Fallback: dense top passages if no triples. **Forget:** none. |
| **conflict** | Silent at graph level; recognition filter drops irrelevant triples before expand. |
| **privacy** | Silent. |
| **numbers** | PPR damping **0.5**; synonym \(\tau=0.8\); passage-node weight best **0.05** (MuSiQue recall@5 **80.5** on 1k-dev). QA F1 (Llama-3.3-70B reader): HippoRAG 2 Avg **59.8** (NQ 63.3, PopQA 56.2, MuSiQue 48.6, 2Wiki 71.0, HotpotQA 75.5, LV-Eval 12.9, NarrativeQA 25.9). Beats NV-Embed-v2 by **9.5%** F1 on 2Wiki and **3.1%** on LV-Eval. Multi-hop recall@5: MuSiQue **74.7**, 2Wiki **90.4**, HotpotQA **96.3**, Avg **87.1** (+**5.0** / +**13.9** R@5 on MuSiQue/2Wiki vs NV-Embed-v2). Ablations: w/o passage nodes Avg R@5 **81.0**; w/o filter **86.4**; query-to-triple **+12.5%** R@5 vs NER-to-node. |
| **kedger_lessons** | Keep PPR d=0.5; prefer query→(Anchor/Evidence) match over NER-only seeds; optional recognition filter before expand. KG routes to Evidence — do not generate summary corpus as L3 truth. Passage/reset weighting ≈ hydrate seed weights. Continual learning = append Evidence, not rewrite history. Seed IDF from HippoRAG v1 still missing in Kedger. |
| **metric_impact** | multi-hop + factual hydrate F1/recall@5; recognition filter false-expand rate |
| **refine_candidate** | **yes** — tickets: **P0 Seed IDF on PPR** (carry-forward from v1); optional **S7 recognition filter** before notebook/PPR expand (rules first; LLM Phase F) |

---

## Card: StreamingLLM

| Field | Content |
|-------|---------|
| **arxiv_id** | 2309.17453 |
| **title** | Efficient Streaming Language Models with Attention Sinks |
| **kedger_stages** | S1, S2 |
| **problem** | Dense KV grows without bound; pure window attention collapses once initial tokens leave the cache; sliding-window recompute is too slow for streaming. |
| **representation** | Rolling KV cache = **attention sinks** (first **4** tokens) + recent window; positions assigned **within cache**, not original text indices (RoPE/ALiBi). |
| **write_read_forget** | **Write:** standard decode KV. **Read:** attend sinks ∪ recent. **Forget/evict:** drop middle tokens beyond `{sinks ∪ recent}`; sinks never evicted. Optional pretrain: single learnable sink token. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **numbers** | Llama-2-13B PPL on PG19 book: window `0+1024` **5158.07** → `4+1020` **5.40** (linebreak sinks **5.60**). Four sinks suffice; 1–2 incomplete (Llama-2-7B `0+4096` PPL **3359.95** → `4+4092` **9.59**). Stable LM up to **4M** tokens. Up to **22.2×** per-token speedup vs sliding-window recompute. StreamEval: reasonable accuracy to **~120K** tokens; window/dense fail at cache/pretrain length. Learnable sink (160M): `1+1023` PPL **18.01** matches multi-sink vanilla. |
| **kedger_lessons** | **Anchors / system constitution / workstream header = sinks — never attention-evicted.** Sink ≠ semantic importance (Softmax dump). Apply eviction metaphor only to **L0 ring**, not L3. Pair with delay-k soft-stale (2608.00902): do not immediately flush mid-context just because attention mass is low. **Do not productize a Kedger KV-cache layer.** |
| **metric_impact** | L0 warn/flush SLI; sink-pin fixture; handoff survival of constraints |
| **refine_candidate** | **yes** — ticket: **P0 Delay-k soft-stale on L0 only** (with 2608.00902); keep Anchors outside eviction |

---

## Card: H₂O (Heavy-Hitter Oracle)

| Field | Content |
|-------|---------|
| **arxiv_id** | 2306.14048 |
| **title** | H₂O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models |
| **kedger_stages** | S1, S2 |
| **problem** | KV cache dominates generative memory (e.g. OPT-30B, batch 128, seq 1024 → **180GB** KV); need low-cost eviction with little quality loss. |
| **representation** | Size-limited KV set \(S_i\) per step; score = accumulated attention mass; retain **heavy hitters** + **recent** locals (budget split evenly). |
| **write_read_forget** | **Write:** accumulate attention scores over preceding tokens (local H₂ ≈ global). **Read:** attend retained KV only. **Forget:** greedy evict lowest cumulative-attention keys when \(\|S\|>k\) (dynamic submodular; near-optimal under mild assumptions). |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **numbers** | Attention matrices **>95%** sparse at inference → up to **~20×** theoretical KV reduction. Empirics at **20%** KV budget (~**5×** memory cut) match full KV on most tasks; can cut footprint **5–10×**. Throughput vs DeepSpeed / HF Accelerate / FlexGen up to **29× / 29× / 3×** (OPT-6.7B/30B). Same batch: latency down to **1.9×**. A100 OPT-6.7B `2048+2048` throughput FlexGen **494.1** → H₂O **918.9** tok/s (batch 24); batch 64 OOM→**1161**. Local-only collapses (e.g. LLaMA-13B XSUM / LLaMA-7B CNN at **60%** budget) while H₂O matches full at **20%**. H₂-only or local-only each drop **2.85–22.75%**. |
| **kedger_lessons** | Heat/access × recency for **L0/L1 pressure scoring** only — same family as MemoryOS Heat. **Never** treat cumulative attention as Anchor truth or productize KV eviction as Kedger memory. Anchors are never attention-evicted. |
| **metric_impact** | L0/L1 eviction under pressure; throughput is out-of-scope for symbolic memory |
| **refine_candidate** | **no** — reject product KV layer; Heat already covered for L1 shrink |

---

## Card: SnapKV

| Field | Content |
|-------|---------|
| **arxiv_id** | 2404.14469 |
| **title** | SnapKV: LLM Knows What You are Looking for Before Generation |
| **kedger_stages** | S2, S7 |
| **problem** | Prompt KV (not decode KV) dominates chatbot/agent latency and memory; prior eviction methods under-compress prompts or lose middle facts. |
| **representation** | Prefill KV split into prefix + **observation window** \(L_{\mathrm{obs}}\) at prompt end; per-head votes → top-\(k\) prefix indices with **1D pooling** clustering; concat selected prefix + full obs window. |
| **write_read_forget** | **Write:** one-shot compress after prefill (no finetune). Vote: \(\mathbf{C}=\sum_i \mathbf{W}_{\mathrm{obs}}[:,i,:]\); \(k=\lfloor p\cdot L_{\mathrm{prefix}}\rfloor\); pool then top-k. **Read:** generation on compressed KV (constant size). **Forget:** drop non-selected prefix KV. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **numbers** | At 16K input, batch 2: **~3.6×** generation speedup; **~8.2×** memory (OOM@16K → 131K). Needle: prompt KV **1024**, obs window **16**, pool kernel **5**, up to **380K** tokens on A100-80GB (~**380×** compression); correct before **140K**, small drop after; baseline OOM@**33K**. LongBench: avg input ~**13K**; SnapKV@1024 ≈ **92%** compression, @4096 ≈ **68%**, negligible accuracy drop across 16 datasets. Mistral SnapKV@1024 beats H2O@4096 on **11/16** benches. Command-R Needle: **9.866 → 9.819 (−0.5%)** at up to **32×** compression. RAG citation retains **~98.8%** of Command-R. Medusa+SnapKV: **1.3×** vs Medusa / **2.2×** vs native at 10K. |
| **kedger_lessons** | Query/obs-window vote is a **hydrate packing** metaphor (keep query-aligned spans under HANDOFF 32KB) — not a reason to store KV as memory. Pooling/clusters ≈ keep neighboring Evidence with hit Anchors. **Never productize SnapKV as Kedger memory.** |
| **metric_impact** | hydrate_pack_bytes ≤32768; query-aligned pack recall |
| **refine_candidate** | **no** — packing already survival-ranked; reject KV-layer productization |

---

## Card: Practical Online KV Cache Compaction for LLM Agents

| Field | Content |
|-------|---------|
| **arxiv_id** | 2608.00902 |
| **title** | Practical Online KV Cache Compaction for LLM Agents: An Empirical Study |
| **kedger_stages** | S1, S2, S3 |
| **problem** | Agent trajectories grow online; static/query-aware KV compaction assumes known future queries. Need **online** compaction with cheap **proxy queries** before future relevance is known. |
| **representation** | Per completed turn: Token Eviction (TE) or Attention Matching (AM). Proxies: boundary tokens, repeat-prefill, or **delayed** future assistant-generation queries (delay-\(k\)). Compact assistant gen and tool response separately; freeze after compact; preserve structural special tokens. |
| **write_read_forget** | **Write:** append turn KV. **Compact:** score positions by RMS attention mass from proxies; TE keeps original KV at top-\(m\); AM fits bias+values. **Delay-\(k\):** keep turn raw for \(k\) future turns, then compact using those queries. **Forget:** discard original KV after freeze. |
| **conflict** | Silent. |
| **privacy** | Silent (behavioral risk: redundant tool use after information loss). |
| **numbers** | Default compact ratio **0.2** (keep 20%). Qwen3.5-4B BrowseComp Acc: no compact **46.00**; TE repeat-prefill delay0 **32.75**; TE boundary delay0 **45.25**; TE assistant delay1 **44.00**. Immediate compaction often hurts; delay-1 recovers. Longer delays {1,3,5} often better; ratio 0.1 too aggressive. Qwen3.5-27B BrowseComp: no compact Acc **52.50** / peak KV **612.9K** / throughput **217** q/h → TE delay1 Acc **52.00** / peak **175.2K** / **717** q/h (**3.3×**); AM **51.00** / **172.8K** / **918** (**4.2×**). Gemma-4-31B: Acc **48.75→50.75** (TE), peak **272.1K→121.3K**, throughput **217→324** (**1.5×**). Abstract: TE preserves most accuracy while reducing KV **~80%**. Compaction raises search duplicate rate (TE-boundary **21.3%** vs **11.7%**). |
| **kedger_lessons** | **Delay-k / soft-stale on L0 only** — do not immediately flush mid-turn L0; wait for later boundaries/queries before aggressive drop. Immediate compact hurts; delayed proxies help. TE robustness > AM under bad proxies. **Anchors never attention-evicted.** **Never productize a Kedger KV-cache layer** — borrow the *timing* lesson only. |
| **metric_impact** | L0 soft-stale/delay-k fixture; agent-turn recovery after mid-context flush |
| **refine_candidate** | **yes** — ticket: **P0 Delay-k soft-stale on L0 only** (soft-mark after delay-k boundaries/idle; flush still by warn 0.70 / flush 0.85) |

---

## Card: InfLLM

| Field | Content |
|-------|---------|
| **arxiv_id** | 2402.04617 |
| **title** | InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory |
| **kedger_stages** | S2, S7 |
| **problem** | Short-pretrained LLMs fail on long streams (OOD positions + distraction); continual long training is costly; pure sliding window drops distant dependencies. |
| **representation** | Sliding window + external **block memory**: past KV → units of \(l_{bs}\) tokens; \(r_k\) representative tokens per block (local attention significance); lookup top-\(k_m\) units by query·repr similarity. Context = initial tokens + retrieved units + local window. Distant positions share encoding distance \(l_L\). CPU offload + GPU LRU. |
| **write_read_forget** | **Write:** encode chunk-by-chunk; evicted tokens → memory units. **Read:** each step lookup relevant units into window. **Forget:** none of units (offloaded); distractors ignored by not loading. Degenerates to StreamingLLM/LM-Infinite if lookup empty. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **numbers** | Defaults: chunk **512**, \(l_{bs}=128\), \(r_k=4\), local window **4K**, initial tokens **128**; Mistral loads **96** units/step, Llama-3 **32**. ∞-Bench avg len **145.1K** (95% quantile **214K**). Mistral InfLLM (16K window) Avg **57.7** vs Streaming **21.5**, Infinite **21.6**, H2O **18.7**. Llama-3 InfLLM (8K) Avg **45.0** vs Streaming **16.3**, H2O **2.1**. **100K** tokens with **26G** VRAM. vs full attention: **−34%** time and **34%** GPU memory; full OOM at **256K**, InfLLM to **1024K**. PassKey: **100%** accuracy at **1024K** tokens (Mistral). |
| **kedger_lessons** | Block+repr lookup ≈ episode/landmark hydrate, **not** a KV product layer. Local window ↔ WorkingState/L1; retrieved units ↔ L2 Evidence. Align block boundaries with episode boundaries. Training-free lookup matches Kedger v1 heuristic hydrate. **Reject productizing InfLLM-style KV memory as Kedger SoT.** |
| **metric_impact** | long-context hydrate with fixed working window; block/episode landmark recall |
| **refine_candidate** | **no** — metaphor already in associative_expand + notebook_walk; reject KV memory productization |

---

## Card: LLMs Know What to Drop (SAGE-KV)

| Field | Content |
|-------|---------|
| **arxiv_id** | 2503.08879 |
| **title** | LLMs Know What to Drop: Self-Attention Guided KV Cache Eviction for Efficient Long-Context Inference |
| **kedger_stages** | S2, S7 |
| **problem** | Static sinks+recent (StreamLLM) discard middle facts; dynamic per-step block selection (Quest/InfLLM) keeps full KV candidate pool and adds latency. |
| **representation** | After prefill, partition KV into sink / eviction region / recent / last token. **Single-pass** head-level top-\(k\) on eviction region using **last-token** query attention; concat \(\mathrm{Concat}(S, E_{\mathrm{top}k}, R, P_N)\). |
| **write_read_forget** | **Write:** full prefill KV then one compress. **Read:** decode on reduced cache; new tokens enter recent window (FIFO). **Forget:** non-selected mid tokens dropped once; no per-step reselect. |
| **conflict** | Silent. |
| **privacy** | Silent. |
| **numbers** | LongBench Avg (Llama3.1-8B-128k): Full **53.01**, SAGE-KV **52.49**, StreamLLM_R **51.13**, Quest **51.27**, InfLLM **50.29**. Llama-3-ProLong-512k: Full **47.74** → SAGE **47.64**. Qwen2.5-7B: Full **52.13** → SAGE **51.19** (HF StreamLLM collapses to **35.3**). Budget: SAGE@**2k** matches StreamLLM@**8k** (~**4×** memory); SAGE@**4k** matches Quest@**8k** (~**2×**). Hyperparams at \(B=8192\): sink \(B/4=2048\), \(k=B/(2G)\) (Llama \(k=1024\)), recent \(B/4\). |
| **kedger_lessons** | One-shot “what to drop” after a boundary ≈ cognify/hydrate drop order under 32KB — **not** ongoing attention eviction of Anchors. Head-level / last-token vote = query-conditioned pack filter. Complements StreamingLLM sinks but recovers middle. **Never productize SAGE-KV as Kedger memory.** |
| **metric_impact** | pack drop-order under HANDOFF_MAX_BYTES=32768; mid-context fact retention after compress |
| **refine_candidate** | **no** — drop order already in hydrate; reject KV-layer productization |

---

## Cross-cutting (this cluster)

| Kedger lock | Source | Action |
|-------------|--------|--------|
| `associative_expand` PPR **d=0.5**, **no IDF yet** | HippoRAG / HippoRAG 2 | **Pursue** seed IDF / node specificity |
| L0 ring buffer; delay-k soft-stale | StreamingLLM + 2608.00902 | **Pursue** soft-stale on L0 only |
| Anchors never attention-evicted | StreamingLLM sinks lesson (inverted) | **Maintain** |
| HANDOFF **32KB** | LeanMem/LightMem line + SnapKV packing metaphor | **Maintain** survival rank; no KV product |
| Never productize KV-cache as Kedger memory | H₂O, SnapKV, InfLLM, SAGE-KV, Online KV | **Reject** |
