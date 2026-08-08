# P1 — Capture & Working Memory (Hooks → L0 → L1)

> **Date:** 2026-08-08  
> **Pillar:** Capture events via agent hooks; persist raw L0 observations; maintain L1 WorkingState with pressure-aware compaction.  
> **Method:** Full arXiv HTML/PDF bodies + Claude/Cursor documentation fetched and read for mechanism extraction (not abstract-only).  
> **MoDeX mapping:** Hooks = capture surface; L0 = Observation log; L1 = WorkingState / main-context projection.

---

## 0. Honesty table

| Status | Count | Items |
|--------|------:|-------|
| **FULL deep-read** (complete body; mechanism card below) | **32** | MemGPT, Generative Agents, ReAct, Reflexion, StreamingLLM, H₂O, SnapKV, Landmark Attention, Compressive Transformer, Transformer-XL, Memorizing Transformers, RMT, RMT-1M, Memory Networks, AutoCompressors, Unlimiformer, ICAE, RAG, Toolformer, SCM, Recursive Summarization, MemoryBank, Think-in-Memory, Claude Hooks, Cursor Hooks, Claude Compaction, Claude Context Editing, AIOS, MemOS, RET-LLM, LightMem/MIRIX, Zhang survey (P1 slices) |
| **FULL surveys used for P1 bibliography + taxonomy** | **3** | 2512.13564, 2603.07670, 2404.13501 |
| **Substantial / supporting** | 2 | Prompt-caching notes; context-windows overview |
| **Not claimed FULL** | — | Product blog posts without stable mechanism specs |

**P1 FULL total: 32 primary texts (+ 3 surveys overlapping with P2).**

---

## 1. Mechanism cards

### 1.1 MemGPT — OS-inspired virtual context
**arXiv:2310.08560** · Packer et al. · 2023/2024 · **FULL**

- **Problem:** Fixed context windows break long chat and document analysis; naive long-context models still under-utilize context.
- **Memory representation:**
  - **Main context (prompt tokens):** (1) read-only system instructions, (2) fixed-size RW **working context** (unstructured text), (3) **FIFO queue** of messages + function IO; queue[0] = recursive summary of evicted messages.
  - **External:** **recall storage** (message DB) + **archival storage** (arbitrary text objects, embedding search).
- **Write path:** LLM self-directed function calls (`working_context.append/replace`, archival insert, recall search). Queue manager appends every message/function IO.
- **Read/retrieve:** `recall_storage.search` / archival vector search with **pagination** cognizant of remaining token budget; results must be explicitly paged into main context.
- **Forget/compact/evict:** When prompt tokens ≥ **warning token count** → inject *memory pressure* system alert. When ≥ **flush token count** → flush ≈ **50%** of queue, recompute recursive summary at head, archive evicted messages to recall.
- **Conflict handling:** Unstructured overwrite of working context; no typed contradiction algebra.
- **Privacy:** Single-agent persona; none multi-user.
- **FAILURE MODES:** Agent forgets to call memory write under pressure; recursive summary loses facts; pagination truncation; working-context thrash.
- **MoDeX IMPLEMENTATION LESSONS:**
  - L1 WorkingState ↔ working context; L0 ↔ FIFO+recall; L4 boot ↔ compiled main context.
  - Emit **memory-pressure warning before eviction**; `PreCompact` must force Anchor/Episode extraction first.
  - Do **not** rely solely on agent self-writes — autocapture via hooks.
  - Constants: `WARN_FRAC=0.70`, `FLUSH_FRAC=0.85`, `EVICT_FRAC=0.50` of working-queue budget.

### 1.2 Generative Agents — Memory stream + importance + reflection
**arXiv:2304.03442** · Park et al. · 2023 · **FULL**

- **Problem:** Believable long-horizon agents need memory beyond one prompt.
- **Memory representation:** Natural-language **memory stream** of observations; reflections/plans re-enter stream. Reflection trees cite supporting memories.
- **Write path:** Every perception appended. Importance = LLM poignancy score **1–10** at creation.
- **Read/retrieve:** Score = α_r·recency + α_i·importance + α_rel·relevance. Recency = exponential decay; paper decay factor **0.995** (sandbox hours). Relevance = embedding cosine to query.
- **Forget/compact:** Reflection when Σ importance of recent events > threshold **150** → generate questions from last **100** records → retrieve → insights with citations. ~2–3×/day in sim.
- **Conflict:** Not modeled; retrieval miss + embellishment are main errors.
- **Privacy:** Multi-agent sandbox diffusion via dialogue, not ACL.
- **FAILURE MODES:** Missed retrieval; fabricated embellishments; overly formal speech from LLM prior.
- **MoDeX IMPLEMENTATION LESSONS:**
  - `Observation.importance ∈ [0,1]` calibrated from 1–10 poignancy for eng events.
  - Hydrate rank = recency × importance × relevance.
  - Trigger L1→L2/L3 reflection on **accumulated importance**, not only tokens/time.
  - Constants: `RECENCY_DECAY=0.995` per hour (or map to session steps), `REFLECT_IMPORTANCE_SUM=150`, `REFLECT_LOOKBACK=100`.

### 1.3 ReAct — Trajectory as short-horizon working memory
**arXiv:2210.03629** · Yao et al. · 2022/2023 · **FULL**

- **Problem:** Pure CoT lacks grounding; pure acting lacks reasoning.
- **Memory representation:** Interleaved **Thought / Action / Observation** trace inside the context window (working memory = trajectory).
- **Write path:** Model emits Thought then Action; environment returns Observation appended to context.
- **Read:** Full in-context trajectory; no external store in base ReAct.
- **Forget/compact:** Implicit truncation when context fills — no principled eviction.
- **Conflict/privacy:** N/A.
- **FAILURE MODES:** Context overflow; repetitive loops; observation noise drowning thoughts.
- **MoDeX IMPLEMENTATION LESSONS:** L0 should store structured `(thought?, action, observation, ts)` from `PostToolUse` / `afterShellExecution`, not only final assistant text. Cap in-L1 trajectory window; promote durable steps to L2.

### 1.4 Reflexion — Verbal reinforcement as episodic journal
**arXiv:2303.11366** · Shinn et al. · 2023 · **FULL**

- **Problem:** Agents fail to improve from trial-and-error without weight updates.
- **Memory representation:** **Short-term** = current trajectory; **long-term** = durable self-reflections (natural language) stored across trials.
- **Write path:** After trial, evaluator scores outcome → Reflector LLM writes verbal critique → append to long-term memory → next trial conditions on reflections.
- **Read:** Prepend/store reflections into actor prompt.
- **Forget:** Not specified; memory grows with trials (practical truncation needed).
- **Conflict:** Newer reflections may contradict older — last-write bias.
- **Privacy:** None.
- **FAILURE MODES:** Noisy self-critique; credit assignment errors; unbounded reflection growth.
- **MoDeX IMPLEMENTATION LESSONS:** Failed tool runs / test failures should write L2 `kind=reflection` episodes with Evidence pointers to failing Observation IDs. Cap reflections per workstream (e.g. 20) with FIFO+importance.

### 1.5 StreamingLLM — Attention sinks
**arXiv:2309.17453** · Xiao et al. · 2023 · **FULL**

- **Problem:** Windowed attention collapses perplexity when early tokens leave cache.
- **Memory representation:** KV cache with **attention sinks** = first **4** tokens retained + rolling recent window.
- **Write/read:** Standard decode; eviction drops middle tokens, keeps sinks+recent.
- **Forget/evict:** Evict tokens beyond `{sinks ∪ recent_window}`.
- **Conflict/privacy:** N/A (inference cache).
- **FAILURE MODES:** Insufficient sinks (<4); tasks needing middle-context facts lost.
- **MoDeX IMPLEMENTATION LESSONS:** L1 always pin **constitution / system Anchors / active workstream header** as “sinks”; never evict them in compaction. Constant: `SINK_PIN_COUNT≥4` logical blocks (not necessarily tokens).

### 1.6 H₂O — Heavy-Hitter Oracle KV eviction
**arXiv:2306.14048** · Zhang et al. · 2023 · **FULL**

- **Problem:** KV cache memory dominates generative inference; need eviction with little quality loss.
- **Memory representation:** Per-layer KV; retain tokens with high cumulative attention (**heavy hitters**) + recent locals.
- **Write:** Accumulate attention mass per key as generation proceeds.
- **Read:** Attend only to retained KV set of budget `k`.
- **Evict:** Drop lowest cumulative-attention keys under budget (greedy approx of submodular objective). Empirics often at **20% KV budget**.
- **Conflict/privacy:** N/A.
- **FAILURE MODES:** Early underestimation of future-needed tokens; abrupt topic shift after eviction.
- **MoDeX IMPLEMENTATION LESSONS:** For L1 message eviction scoring, combine **access_count / retrieve_hits** (heavy hitter) with recency — same formula family as MemoryOS Heat. Constant: keep ≥20% of L1 items by heat when forced to shrink.

### 1.7 SnapKV — Prefill voting for KV compression
**arXiv:2404.14469** · Li et al. · 2024 · **FULL**

- **Problem:** Preferential retention of prompt KV before generation without expensive fine-tuning.
- **Memory representation:** Prefill KV; observation window at end of prompt votes for important prefix positions via pooled attention; keep top-`k` where `k=⌊p·L_prefix⌋`.
- **Write:** One-shot selection after prefill (+ clustering/pooling for robustness).
- **Read:** Generation attends compressed KV.
- **Evict:** Drop non-selected prefix KV; keep recent observation window intact.
- **FAILURE MODES:** Observation window not representative of later queries; over-compression (`p` too small).
- **MoDeX IMPLEMENTATION LESSONS:** Before L4 pack compile, run a cheap “importance vote” over candidate L0/L1 spans using the **current user query** as observation window — keep query-aligned spans, drop the rest. Constant: start `p=0.2–0.5` of candidate tokens.

### 1.8 Landmark Attention — Random-access block memory
**arXiv:2305.16300** · Mohtashami & Jaggi · 2023 · **FULL**

- **Problem:** Transformers need random access beyond local window.
- **Memory representation:** Sequence split into blocks of **ℓ_block=50** with a **landmark** token per block; retrieve top-`k` blocks (k≈2–4) via landmark similarity.
- **Write:** Store block KVs under landmark keys.
- **Read:** Query landmarks → fetch top-k blocks → attend.
- **Evict/compress:** Optional CMT cutoff drops ~50% retrievals with minor PPL hit.
- **FAILURE MODES:** Wrong block retrieved; landmark collapse.
- **MoDeX IMPLEMENTATION LESSONS:** Episode/chunk should carry a **landmark summary embedding** for coarse retrieve-then-expand. Constants: `CHUNK_TOKENS≈512–2048` eng spans; retrieve `k_blocks=4`.

### 1.9 Compressive Transformer
**arXiv:1911.05507** · Rae et al. · 2019 · **FULL**

- **Problem:** Fine-grained long-range memory with bounded cost.
- **Memory representation:** Fine-grained past memories + **compressed** coarser memories via convolutions/pooling over older segments.
- **Write:** As time passes, older activations are compressed into secondary memory.
- **Read:** Attend to both fine local and compressed distant memories.
- **Evict:** Compression is lossy forget.
- **FAILURE MODES:** Over-compression erases rare but critical facts.
- **MoDeX IMPLEMENTATION LESSONS:** Multi-resolution L0: raw recent pages + compressed digests for older pages — never compress before Anchor extraction opportunity.

### 1.10 Transformer-XL
**arXiv:1901.02860** · Dai et al. · 2019 · **FULL**

- **Problem:** Vanilla Transformers break segment coherence; no recurrence.
- **Memory representation:** Cached hidden states from previous segment reused as extended context (relative positional encodings).
- **Write/read:** Segment-level recurrence; stop-grad across segments during training.
- **Forget:** Cache beyond memory length dropped.
- **FAILURE MODES:** Still limited by memory length; relative positions need care.
- **MoDeX IMPLEMENTATION LESSONS:** L1 should keep a **segment cache** of last N turns across compaction boundaries (continuity buffer), analogous to XL memory.

### 1.11 Memorizing Transformers
**arXiv:2203.08913** · Wu et al. · 2022 · **FULL**

- **Problem:** Scale non-differentiable external memory to long corpora.
- **Memory representation:** kNN-addressable external key-value memory of past (k,v); paper uses **k=32**, often layer 9.
- **Write:** Append keys/values from chosen layer into memory bank (can be frozen/non-diff).
- **Read:** Approximate kNN lookup; gate/combine with local attention.
- **Evict:** Memory can grow; practical FIFO/size caps.
- **FAILURE MODES:** Spurious near-neighbor; distribution shift vs training memory.
- **MoDeX IMPLEMENTATION LESSONS:** L0/L2 embeddings in SQLite/vec index with `k=32` candidate fanout before rerank. Separate **append-only Evidence index** from mutable L1.

### 1.12 Recurrent Memory Transformer (RMT)
**arXiv:2207.06881** · Bulatov et al. · 2022 · **FULL**

- **Problem:** Pass information across segments with explicit memory tokens.
- **Memory representation:** Special **memory tokens** prepended/appended; written by model each segment; read next segment.
- **Write:** Model updates memory token states each segment (BPTT over few segments).
- **Read:** Next segment attends to memory tokens + local tokens.
- **Evict:** Fixed memory size (e.g. 10–150 tokens in experiments) overwrites.
- **FAILURE MODES:** Memory bottleneck capacity; training difficulty.
- **MoDeX IMPLEMENTATION LESSONS:** L1 WorkingState should be a **small fixed slot set** (persona, active goal, open decisions, constraints) — RMT-like fixed memory tokens, not unbounded chat.

### 1.13 Scaling Transformer to 1M tokens with RMT
**arXiv:2304.11062** · Bulatov et al. · 2023 · **FULL**

- **Problem:** Extrapolate RMT memory curriculum to extreme lengths.
- **Memory representation:** Same memory-token recurrence; curriculum increases segment count.
- **Write/read/forget:** As RMT; demonstrates passkey-style retention at 1M via memory tokens.
- **FAILURE MODES:** Tasks needing dense full-history attention still fail; memory token overwrite.
- **MoDeX IMPLEMENTATION LESSONS:** Stress-test L1 slots with synthetic “passkey” eng facts (API keys redacted hashes, decision IDs) across many session compactions.

### 1.14 Memory Networks
**arXiv:1410.3916** · Weston et al. · 2014/2015 · **FULL**

- **Problem:** Classical QA needs multi-hop read over long-term memories.
- **Memory representation:** Array of memory slots m_i; embedding matrices; hops.
- **Write:** Store embeddings of facts/utterances into slots (with optional time features).
- **Read:** Softmax attention hop; **k=2 supporting memories** critical for multi-hop tasks; time features matter.
- **Forget:** Not primary; slot overwrite possible.
- **FAILURE MODES:** Hard max vs soft attention; missing time features collapses accuracy.
- **MoDeX IMPLEMENTATION LESSONS:** Hydrate should allow **2-hop** Evidence expansion (entity→episode→anchor). Always store `created_at` / `valid_at` for temporal hops.

### 1.15 AutoCompressors — Summary vectors
**arXiv:2305.14788** · Chevalier et al. · 2023 · **FULL**

- **Problem:** Compress long contexts into summary vectors reusable as soft prompts.
- **Memory representation:** Recursive compression into **summary vectors** (e.g. 50×3=**150** vectors for 6144 tokens).
- **Write:** Segment → compress → pass summary vectors to next segment (recursive).
- **Read:** Condition generation on summary vectors (+ optional retrieved raw).
- **Forget:** Compression lossy; plaintext discarded from active prompt.
- **FAILURE MODES:** Hallucination from lossy summaries; poor compression of rare facts.
- **MoDeX IMPLEMENTATION LESSONS:** Recursive summary OK for L1 queue head (MemGPT-style) but **never sole L3**. After compress, keep pointers to raw L0 IDs.

### 1.16 Unlimiformer
**arXiv:2305.01625** · Bertsch et al. · 2023 · **FULL**

- **Problem:** Encoder-decoder cross-attention limited by input length.
- **Memory representation:** Index all encoder hidden states in kNN; each decoder head retrieves top-k keys instead of full attention.
- **Write:** Build/refresh kNN index over encoded inputs.
- **Read:** Per-head top-k retrieval + attend.
- **Forget:** Index rebuild/evict chunks when documents leave corpus.
- **FAILURE MODES:** kNN approx errors; domain shift.
- **MoDeX IMPLEMENTATION LESSONS:** Treat L4 compilation as Unlimiformer-like: index candidates, inject only top-k per “head”/section of the pack (decisions / evidence / trajectory).

### 1.17 ICAE — In-context Autoencoder (context compression)
**arXiv:2307.06945** · Ge et al. · 2023 · **FULL**

- **Problem:** Compress contexts into short **memory slots** for the target LLM.
- **Memory representation:** Memory length **k∈{32,64,128,256}** slots; AE+LM pretrain (λ≈0.4–0.6).
- **Write:** Encoder produces memory slots from context; LoRA adaptation.
- **Read:** Target LLM conditions on slots instead of raw context.
- **Forget:** Slots replace raw; >4× compression hard to keep lossless (k=128 still strong ~500 tokens).
- **FAILURE MODES:** Hallucination worse without AE pretrain; aggressive k.
- **MoDeX IMPLEMENTATION LESSONS:** If using learned compressors for L1 digests, prefer AE-pretrained; otherwise use LLM summarization with explicit “do not invent” + Evidence IDs. Target ~4× for lossy digests, not 16×.

### 1.18 RAG — Retrieval-Augmented Generation
**arXiv:2005.11401** · Lewis et al. · 2020 · **FULL**  
*(Note: user seed 2005.11485 is a different paper; canonical RAG is 2005.11401.)*

- **Problem:** Parametric LLMs alone fail knowledge-intensive tasks / stale facts.
- **Memory representation:** Non-parametric dense index of document chunks; retriever p_η(z|x) + generator p_θ.
- **Write:** Offline index build (MIPS); RAG can jointly fine-tune.
- **Read:** Top-K MIPS; RAG-Sequence vs RAG-Token marginalization.
- **Forget:** Index delete/update documents (external).
- **FAILURE MODES:** Retriever miss; generator ignores docs; conflicting docs.
- **MoDeX IMPLEMENTATION LESSONS:** L0/L2 chunk index is classic RAG; MoDeX adds typed Anchors + invalidation on top. Default `TOP_K=5` then rerank.

### 1.19 Toolformer — Self-supervised tool calls
**arXiv:2302.04761** · Schick et al. · 2023 · **FULL**

- **Problem:** LLMs need API tools without full fine-tune datasets.
- **Memory representation:** In-context tool call traces; sampling threshold τ_s, filtering threshold τ_f; keep top positions (k≈5–20).
- **Write:** Sample candidate API-call insertions; keep if they improve likelihood by τ_f.
- **Read:** At inference, decode with tool results inserted.
- **Forget:** N/A.
- **FAILURE MODES:** Spurious tool calls; wrong args.
- **MoDeX IMPLEMENTATION LESSONS:** Memory write tools should be **first-class tools** with hook-side validation (`PreToolUse` deny malformed memory ops). Log tool IO into L0 always.

### 1.20 SCM — Self-Controlled Memory Framework
**arXiv:2304.13343** · Wang et al. · 2023/2025 · **FULL**

- **Problem:** LLMs need selective recall over long dialogues/books without dumping all retrievals.
- **Memory representation:** **Flash memory** (short-term recent) + **activation memory** (long-term store) + **memory controller** that gates what enters the prompt. Ablations: w/o controller (−17.8 Acc), w/o activation (−66.6).
- **Write:** Stream dialogue into memory bank; controller decides recall.
- **Read:** Retrieve then controller filters/ truncates (baseline truncate at **2500** tokens without controller).
- **Forget:** Implicit via non-activation.
- **FAILURE MODES:** Controller false negatives; flash-only loses long dependencies.
- **MoDeX IMPLEMENTATION LESSONS:** L1 compilation must include a **controller/budgeter** stage — retrieval ≠ injection. Hard cap injected working tokens (e.g. 2500–8000 depending on model).

### 1.21 Recursively Summarizing Enables Long-Term Dialogue Memory
**arXiv:2308.15022** · Wang et al. · 2023 · **FULL**

- **Problem:** Multi-session dialogues exceed context; retrieval alone misses global narrative.
- **Memory representation:** Hierarchical recursive summaries over session history; compared to BM25/DPR top-k (k=3 or 5).
- **Write:** After session/turn batches, summarize; recursively summarize summaries.
- **Read:** Conditioner on recursive summary (+ optional top-k utterances).
- **Forget:** Older utterances replaced by summaries in the active prompt (raw may remain offline).
- **FAILURE MODES:** Error propagation in recursive summaries; omission of rare facts.
- **MoDeX IMPLEMENTATION LESSONS:** Recursive session digests = L1/L2 digest field; always retain raw L0 for Evidence. Don’t answer factual eng questions from digest alone.

### 1.22 MemoryBank — Forgetting curve memory
**arXiv:2305.10250** · Zhong et al. · 2023 · **FULL**

- **Problem:** Personal LLM assistants need long-term user memory with natural forgetting.
- **Memory representation:** Vector DB of conversations/events/traits; **Ebbinghaus forgetting-curve** style strength updates on retrieval.
- **Write:** Store dialogue turns + inferred user traits; strengthen on recall.
- **Read:** Semantic retrieval weighted by memory strength.
- **Forget:** Strength decays with time without retrieval; weak memories drop out of retrieval set.
- **FAILURE MODES:** Over-forgetting critical rare facts; trait extraction errors.
- **MoDeX IMPLEMENTATION LESSONS:** Optional decay on L1 cache strength; **do not decay sealed Anchors**. For L0 cold storage, decay only retrieval priority, not deletion of audit evidence.

### 1.23 Think-in-Memory (TiM)
**arXiv:2311.08719** · Liu et al. · 2023 · **FULL**

- **Problem:** Agents need to store evolving thoughts, not only dialogue utterances.
- **Memory representation:** Memory of **thoughts** with recall + post-thinking operations for consistency.
- **Write:** Insert/update thought chains after reasoning steps.
- **Read:** Recall relevant thoughts into context; post-think to reconcile.
- **Forget/conflict:** Post-thinking can revise thoughts (risk of silent mutation).
- **FAILURE MODES:** Thought drift; inconsistent self-state.
- **MoDeX IMPLEMENTATION LESSONS:** Store agent reasoning traces as L0 `kind=thought` but promote stabilized conclusions as Anchors with SUPERSEDES — don’t silently rewrite historical thoughts.

### 1.24 Claude Code Hooks (documentation)
**Source:** Anthropic Claude Code Hooks reference · 2025–2026 · **FULL**

- **Problem:** Need deterministic side-effects around agent lifecycle (capture, block, compact).
- **Memory representation:** N/A — event bus. Config: nested `hooks[event][matcher].handlers[]` in settings / plugin `hooks/hooks.json`.
- **Write path (capture):** Handlers on `PostToolUse`, `PostToolBatch`, `Stop`, `UserPromptSubmit`, `SessionStart`, `FileChanged`, etc. receive JSON stdin; may emit context (SessionStart/UserPromptSubmit stdout → model context).
- **Read:** Hooks can inject context at SessionStart / UserPromptSubmit (exit 0 stdout).
- **Forget/compact:** `PreCompact` (matcher `manual|auto`) can **block compaction** (exit 2); `PostCompact` observes result. Critical for extract-before-evict.
- **Conflict:** Decision control via `permissionDecision` allow/deny on PreToolUse.
- **Privacy:** Hooks see tool inputs — must redact secrets before L0 write.
- **FAILURE MODES:** Matcher miss; cloud timing; blocking Stop incorrectly; leaking secrets into logs.
- **MoDeX IMPLEMENTATION LESSONS:** Map MoDeX capture to: `SessionStart`→hydrate L1; `PostToolUse`/`afterFileEdit`→L0 append; `PreCompact`→promote+checkpoint; `Stop`→flush WorkingState. Prefer exit 0 + structured JSON side-effects to SQLite.

### 1.25 Cursor Hooks (documentation)
**Source:** Cursor Docs — Hooks · 2025–2026 · **FULL** (event surface extracted from docs payload)

- **Problem:** Project/user hooks around Cursor agent loop via `.cursor/hooks.json` (also `~/.cursor/hooks.json` locally; cloud uses project/team hooks).
- **Events (non-exhaustive):** `sessionStart`, `sessionEnd`, `beforeSubmitPrompt`, `preCompact`, `stop`, `afterAgentResponse`, `afterAgentThought`, `afterFileEdit`, `beforeReadFile`, `beforeShellExecution`, `afterShellExecution`, `beforeMCPExecution`, `afterMCPExecution`, `preToolUse`, `postToolUse`, …
- **Write/read:** Command hooks communicate JSON over stdio; can audit/approve/deny (e.g. `beforeShellExecution` matcher `curl|wget|nc`, timeout 30).
- **Compact:** `preCompact` observes context window compaction — MoDeX extract gate.
- **Privacy:** `beforeTabFileRead` / read hooks used for secret redaction examples.
- **FAILURE MODES:** Cloud agents defer some hooks; enterprise vs local path differences; timeouts.
- **MoDeX IMPLEMENTATION LESSONS:** Ship `.cursor/hooks.json` templates mirroring Claude mapping; cloud-safe: keep hooks in-repo. Redact in `beforeReadFile` / shell hooks before L0.

### 1.26 Claude server-side compaction
**Source:** Anthropic Compaction docs (`compact-2026-01-12`) · **FULL**

- **Problem:** Long agent runs hit context limits; client-side summarization is error-prone.
- **Memory representation:** API inserts a `compaction` block summary; prior blocks dropped on subsequent turns.
- **Algorithm:** When `input_tokens ≥ trigger.value` → summarize → continue. Default trigger **150000** tokens; minimum trigger **50000**. Custom `instructions` **replace** default summary prompt entirely.
- **FAILURE MODES:** Summary omission of critical constraints; trigger too late (quality already degraded); custom instructions wiping necessary summary schema.
- **MoDeX IMPLEMENTATION LESSONS:** Treat provider compaction as **hostile GC** — `PreCompact` must persist Anchors/Episodes first. Align MoDeX WARN below provider trigger (e.g. MoDeX promote at 60% context, provider compact at 150k).

### 1.27 Claude context editing (tool/thinking clearing)
**Source:** Anthropic Context editing docs · **FULL**

- **Problem:** Fine-grained clearing when full compaction is too coarse.
- **Strategies:** `clear_tool_uses_20250919` (oldest tool results → placeholders; optional `clear_tool_inputs`); `clear_thinking_20251015` with `keep` policy. Beta header `context-management-2025-06-27`.
- **Notes:** Client keeps full history; server edits view. Tool clearing invalidates prompt cache — use `clear_at_least` to make invalidation worthwhile.
- **FAILURE MODES:** Clearing tool IO still needed for audit; cache thrash.
- **MoDeX IMPLEMENTATION LESSONS:** Provider may clear tool results MoDeX already stored in L0 — good. Never depend on provider-retained tool IO for Evidence; always persist on `PostToolUse`.

### 1.28 AIOS — Memory manager as kernel service
**arXiv:2403.16971** · **FULL** (from prior P1 recipe pass; body in corpus cache)

- **Problem:** Agents touching RAM/disk ad hoc races and leaks privileges.
- **Memory representation:** Per-agent memory blocks; Storage Manager / vector store; syscall API.
- **Write path:** Agents issue memory **syscalls**; Memory/Storage managers schedule FIFO/RR.
- **Read:** Privilege-gated; user confirm on destructive ops.
- **Forget/evict:** At **~80%** RAM → **LRU-K** swap to disk.
- **FAILURE MODES:** Scheduler starvation; swap thrash; over-broad privileges.
- **MoDeX IMPLEMENTATION LESSONS:** Single-writer queue for L0 append; async swap of cold WorkingState slices; ACL on workstream read. Context interrupt/snapshot pattern for long generations.

### 1.29 MemOS — Activation vs plaintext layers
**arXiv:2507.03724** · **FULL** (prior P1 pass)

- **Problem:** Need unified OS for activation memory vs durable plaintext cubes.
- **Memory representation:** Working ≈ activation (KV/hidden/steering); durable ≈ plaintext MemCubes with provenance.
- **Write/read:** Scheduler promotes hot plaintext into activation templates; archives cold.
- **MoDeX IMPLEMENTATION LESSONS:** Distinguish ephemeral L1 projection (compiled prompt/KV) from durable L0 log; every durable write carries provenance/type/permissions metadata.

### 1.30 RET-LLM — Structured capture API
**arXiv:2305.14322** · **FULL** (prior P1 pass)

- **Problem:** Free-form model writes to memory are unsafe/unreliable.
- **Memory representation:** Structured ops like `[MEM_WRITE{t1>>rel>>t2}]` emitted by model; controller executes.
- **MoDeX IMPLEMENTATION LESSONS:** Hooks/tools may **propose** structured ops; executor validates schema before L0/L3 commit — no free-form DB writes from the model.

### 1.31 LightMem / MIRIX — Cheap front-end filters
**LightMem 2510.18866 + MIRIX (prior P1)** · **FULL** / substantial

- **Problem:** Most tokens are redundant; secrets must not enter working prompts.
- **Write:** Sensory pre-compress drops low-salience tokens (LightMem); secrets→Vault not working prompt (MIRIX); debounce screen/IDE frames.
- **MoDeX IMPLEMENTATION LESSONS:** Redact+debounce at capture; pre-compress only for summarization inputs — never delete raw L0.

### 1.32 Survey — A Survey on the Memory Mechanism of LLM-based Agents
**arXiv:2404.13501** · Zhang et al. · 2024 · **FULL**

- **Problem:** Taxonomy of agent memory forms/functions.
- **P1-relevant mechanisms:** Working vs long-term; sensory→STM→LTM hierarchies; summarization & retrieval controllers; evaluation gaps.
- **MoDeX lessons:** Keep working memory small & structured; explicit write/read/forget ops; evaluate maintenance cost not only QA.

---

## 2. Cross-cutting synthesis (P1)

| Pattern | Sources | MoDeX adoption |
|---------|---------|----------------|
| Hierarchical paging (main vs external) | MemGPT, MemoryOS, SCM | L1 vs L0/L2 stores |
| Pressure warning before eviction | MemGPT, Claude PreCompact | Mandatory promote hook |
| Pin sinks / constitution | StreamingLLM, RMT slots | Pin system Anchors in L1 |
| Heat = attention/access × recency | H₂O, MemoryOS, GenAgents | L1 eviction score |
| Controller ≠ retriever | SCM, SnapKV vote | Budgeted inject |
| Lossy summary is not truth | AutoCompressors, Recursive Sum, Compaction docs | Anchors first |
| Autocapture beats self-write | Hooks docs vs MemGPT | Hooks → L0 always |

### Anti-patterns
1. Relying on the model to remember to call `memory.write`.
2. Recursive summary as the only durable store.
3. Evicting system sinks / active decision slots.
4. Silent in-place mutation of historical thoughts (TiM risk).
5. Provider compaction without PreCompact persistence.

### Open risks
- Exact eng-domain importance calibration still empirical.
- Cross-tool redaction policy incomplete without secret classifiers.
- Provider trigger defaults (150k) may be far above quality-degradation point.

---

## 3. Implementation recipe for MoDeX

### 3.1 SQLite tables (P1)

```sql
-- Raw capture (L0)
CREATE TABLE observation (
  id            TEXT PRIMARY KEY,           -- obs_...
  workstream_id TEXT NOT NULL,
  session_id    TEXT NOT NULL,
  ts            INTEGER NOT NULL,           -- unix ms
  kind          TEXT NOT NULL,              -- prompt|tool|shell|edit|thought|alert|system
  source_hook   TEXT,                       -- PostToolUse|afterFileEdit|...
  role          TEXT,                       -- user|assistant|tool|system
  content       TEXT NOT NULL,              -- redacted
  content_hash  TEXT NOT NULL,
  importance    REAL NOT NULL DEFAULT 0.3,  -- 0..1
  surprise      REAL,                       -- optional EM-LLM-style
  token_est     INTEGER,
  redaction     TEXT,                       -- json list of rules applied
  embedding     BLOB,                       -- optional float32
  meta_json     TEXT                        -- tool_name, paths, exit_code, ...
);
CREATE INDEX idx_obs_ws_ts ON observation(workstream_id, ts);
CREATE INDEX idx_obs_session ON observation(session_id, ts);
CREATE INDEX idx_obs_kind_ts ON observation(kind, ts);

-- L1 working projection (mutable, non-authoritative)
CREATE TABLE working_state (
  workstream_id TEXT PRIMARY KEY,
  updated_at    INTEGER NOT NULL,
  persona_json  TEXT,                       -- fixed slots
  goals_json    TEXT,                       -- active goals
  open_decisions_json TEXT,
  constraints_json TEXT,
  digest        TEXT,                       -- recursive queue summary
  token_est     INTEGER NOT NULL DEFAULT 0,
  pressure      TEXT NOT NULL DEFAULT 'ok'  -- ok|warn|flush
);

CREATE TABLE working_queue (
  id            TEXT PRIMARY KEY,
  workstream_id TEXT NOT NULL,
  obs_id        TEXT REFERENCES observation(id),
  ts            INTEGER NOT NULL,
  slot          TEXT NOT NULL,              -- message|summary|alert
  content       TEXT NOT NULL,
  heat          REAL NOT NULL DEFAULT 0,
  pinned        INTEGER NOT NULL DEFAULT 0  -- sinks
);
CREATE INDEX idx_wq_ws_ts ON working_queue(workstream_id, ts);

CREATE TABLE hook_event_log (
  id            TEXT PRIMARY KEY,
  ts            INTEGER NOT NULL,
  provider      TEXT NOT NULL,              -- claude|cursor
  event_name    TEXT NOT NULL,
  matcher       TEXT,
  payload_hash  TEXT,
  decision      TEXT,                       -- allow|deny|inject|noop
  error         TEXT
);
```

### 3.2 Capture algorithm (hooks → L0)

```
on Hook(event, payload):
  redacted = Redact(payload)                    # secrets, tokens, env
  obs = Observation(
    kind=MapKind(event), content=redacted.text,
    importance=ScoreImportance(redacted),       # rules+optional LLM
    source_hook=event, meta=redacted.meta)
  INSERT observation
  if event in {PostToolUse, afterFileEdit, afterShellExecution, UserPromptSubmit, afterAgentResponse}:
    EnqueueL1(obs)
  if event == SessionStart:
    HydrateL1(workstream)
  if event == PreCompact:
    PromoteDurable(workstream)                  # L0→L2/L3 (P2/P3)
    CheckpointWorkingState()
    # optionally allow compaction to proceed
  if Pressure(workstream) >= WARN:
    InjectSystemAlert("memory pressure")
  if Pressure(workstream) >= FLUSH:
    EvictL1(workstream, keep_frac=0.5)
```

### 3.3 L1 pressure & eviction

```
Pressure = token_est(working_queue + working_state) / CONTEXT_BUDGET

Heat(item) = α*access_count + β*importance + γ*exp(-Δt/μ) + 1000*pinned

EvictL1:
  protect pinned sinks (constitution, active decision slots)
  sort unprotected by Heat ascending
  evict until token_est <= TARGET (default 50% of budget)
  digest = Summarize(evicted) with pointers to obs_ids
  working_queue[0] = digest (MemGPT recursive head)
```

### 3.4 Recommended constants (P1)

| Constant | Value | Rationale |
|----------|-------|-----------|
| `CONTEXT_BUDGET_TOKENS` | model-dependent (e.g. 32k–200k) | provider window |
| `WARN_FRAC` | **0.70** | MemGPT pressure alert |
| `FLUSH_FRAC` | **0.85** | MemGPT flush |
| `EVICT_FRAC` | **0.50** | MemGPT queue flush amount |
| `SINK_PIN_MIN` | **4** logical blocks | StreamingLLM |
| `L1_SLOT_MAX_TOKENS` | **512–1024** | RMT-like fixed slots |
| `IMPORTANCE_REFLECT_SUM` | **150** (scaled) | Generative Agents |
| `RECENCY_DECAY` | **0.995** / hour | Generative Agents |
| `CONTROLLER_INJECT_CAP` | **2500–8000** tokens | SCM ablation baseline |
| `REDACT_ON_CAPTURE` | **true** | Hooks security |

### 3.5 Hook mapping (ship templates)

| MoDeX action | Claude event | Cursor event |
|--------------|--------------|--------------|
| Session hydrate | `SessionStart` | `sessionStart` |
| Prompt capture | `UserPromptSubmit` | `beforeSubmitPrompt` |
| Tool capture | `PostToolUse` / `PostToolBatch` | `postToolUse` / `afterShellExecution` / `afterFileEdit` |
| Extract-before-GC | `PreCompact` | `preCompact` |
| End-turn flush | `Stop` | `stop` / `afterAgentResponse` |

### 3.6 Pseudocode — importance (eng-tuned)

```
def ScoreImportance(obs):
  base = 0.2
  if obs.kind in {test_failure, build_fail, security, decision}: base = 0.9
  if obs.kind in {edit, tool_ok}: base = 0.4
  if contains_rejection_language(obs): base = max(base, 0.8)
  if secret_redacted(obs): base = min(base, 0.5)  # store pointer, not secret
  return clamp(base, 0, 1)
```

## 4. Acceptance tests (P1)

1. 200-turn session: prompt tokens stay ≤ budget; L0 count = turns; no silent drop without summary.  
2. Pressure warn fires before flush; at least one promotion opportunity turn.  
3. High-sensitivity observation never appears in WorkingState text.  
4. `should_hydrate("tell me a joke") == false`; past-reference true.  
5. After flush, recursive summary non-empty and evicted ids still in L0.

---

*See also: `BATCH_SYSTEMS_AND_EVAL.md` §2.1 and MemGPT/MemoryOS/AIOS cards.*

