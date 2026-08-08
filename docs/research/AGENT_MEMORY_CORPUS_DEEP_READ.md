# Agent Memory Corpus Deep-Read (MoDeX Engineering Memory)

> **Date:** 2026-08-08  
> **Scope:** Mechanism-level deep-reads of primary sources for MoDeX engineering-memory architecture (Anchors+Evidence, L0–L4, sealed handoff, workstreams).  
> **Method:** Full arXiv HTML or PDF text fetched and read (not abstract-only skim). Honesty marks below.  
> **MoDeX lens:** Map each paper onto Anchors+Evidence, L0 raw / L1 working / L2 episodes / L3 anchors / L4 sealed handoff, SUPERSEDES/CONTRADICTS, workstream isolation, promotion/privacy.

---

## 0. Honesty about coverage

| Status | Papers |
|--------|--------|
| **Full deep-read** (complete body text from arXiv HTML or PDF; mechanisms extracted) | Zep/Graphiti (2501.13956); HippoRAG (2405.14831); HippoRAG 2 (2502.14802); A-MEM (2502.12110); Nemori v1 HTML (2508.03341v1) + ACL rewrite “What Deserves Memory” (2508.03341v4); Mem0 (2504.19413); MemGPT (2310.08560); Generative Agents (2304.03442); RecMem (2605.16045); ES-Mem (2601.07582); EM-LLM (2407.09450); StateFuse (2607.05844); TOKI (2606.06240); LightRAG (2410.05779); GraphRAG (2404.16130); SSGM (2603.11768); *Memory in the Age of AI Agents* survey (2512.13564 PDF); Zhang et al. memory-mechanism survey (2404.13501 PDF) |
| **Secondary / supporting** | Survey “Second Half” (2602.06052) — full HTML available; used mainly as corroborating taxonomy pointer, not primary cited-paper inventory |
| **Not found as separate product paper** | Standalone “session/shared graph memory” product paper under that name — closest governance framing is **SSGM** (2603.11768); collaborative private/shared tiers covered in prior MoDeX privacy memo |

**Count of full deep-reads this session:** 18 primary texts (≥12 required).

**Do not invent:** Where a paper is silent (e.g., no privacy model), that silence is recorded.

---

## 1. MoDeX mapping cheat-sheet (used throughout)

| MoDeX concept | Typical academic analogue |
|---------------|---------------------------|
| L0 Observation | Raw messages / episodes / subconscious buffer / FIFO queue |
| L1 WorkingState | Working context / current mission / mutable projection |
| L2 Episode | Event segment / episodic narrative / community leaf |
| L3 Anchor | Semantic fact / claim / decision / invalidatable edge |
| L4 Handoff | Compiled context pack / projection / main-context boot |
| Evidence | Provenance pointers / episode↔entity edges / cited memories |
| SUPERSEDES | Edge invalidation / DELETE / ClaimRetracted / dual-row audit |
| Workstream | Namespace / session graph / community / scope key |

---

## 2. Per-paper deep extracts

### 2.1 Zep / Graphiti — Temporal KG for agent memory  
**arXiv:2501.13956** · Rasmussen et al. · 2025 · **FULL-READ**

**Problem setup.** Enterprise agents need dynamic memory over conversations *and* business data; static RAG corpora and flat chat history fail at temporal reasoning / cross-session synthesis. Zep’s engine is **Graphiti**, a temporally-aware dynamic KG.

**Memory representation.** Graph \(\mathcal{G}=(\mathcal{N},\mathcal{E},\phi)\) with three tiers:
1. **Episode subgraph** — non-lossy raw units (message / text / JSON) with reference timestamp \(t_{\mathrm{ref}}\); episodic edges link episodes → extracted entities.
2. **Semantic entity subgraph** — entity nodes + relationship edges (facts); embeddings on names/facts; hybrid cosine + full-text candidate search; LLM entity/edge resolution; hyper-edge style multi-entity facts.
3. **Community subgraph** — label-propagation communities with map-reduce-style summaries; community *names* embedded for retrieval (unlike GraphRAG’s map-reduce QFS at query time).

**Write / read / forget.**  
- **Write:** ingest episode → NER+reflection (n=4 prior messages) → entity resolve → fact extract → edge dedupe among same entity pair → **temporal extraction**.  
- **Bi-temporal model:** \(T\) = event/valid timeline; \(T'\) = ingestion/transaction timeline. Edges store \(t'_{\mathrm{created}}, t'_{\mathrm{expired}}, t_{\mathrm{valid}}, t_{\mathrm{invalid}}\).  
- **Forget = invalidate, don’t delete:** LLM compares new edge vs related edges; on temporally overlapping contradiction, set \(t_{\mathrm{invalid}}\) of loser to \(t_{\mathrm{valid}}\) of winner; **transactionally prefer newer writes**.  
- **Read:** search → rerank → context constructor; searches over edges, entities, communities; returns formatted context string.

**Compaction / consolidation.** Community dynamic extension (plurality neighbor community + summary update) defers full refresh; periodic full label-propagation still needed. Episodes remain non-lossy provenance.

**Conflict / supersession.** Explicit edge invalidation with temporal overlap check; history retained via timestamps.

**Privacy / sharing.** Not a first-class model in the paper (service-layer concern outside Graphiti mechanics).

**MoDeX design lessons (6):**
1. Keep L2/L0 **non-lossy** while L3 facts are invalidatable — matches Anchors+Evidence provenance.
2. Put **four timestamps** (or at least valid_from/valid_to + created/superseded) on Anchors/edges, not only “updated_at”.
3. SUPERSEDES should be **write-time LLM contradiction check among same entity-pair candidates**, not global fuzzy merge.
4. Prefer **invalidate + retain history** over DELETE for engineering decisions.
5. Community summaries ≈ optional L3 “community” layer for hydrate ranking — do not make them the sole truth.
6. Bi-temporal separation (when fact was true vs when MoDeX learned it) matters for branch/workstream races.

---

### 2.2 HippoRAG — Neurobiologically inspired associative retrieval  
**arXiv:2405.14831** · Gutiérrez et al. · 2024/2025 · **FULL-READ**

**Problem setup.** Standard RAG fails multi-hop / associative recall; need non-parametric continual integration of new passages without catastrophic forgetting.

**Memory representation.** OpenIE schemaless KG: noun-phrase nodes + relation edges from each passage; **synonymy edges** via encoder cosine > τ; passage↔phrase occurrence matrix \(\mathbf{P}\). Mapping: LLM≈neocortex, open KG≈hippocampal index, encoder≈PHR.

**Write / read / forget.**  
- **Write (offline indexing):** 2-step OpenIE (named entities → triples with broader phrases) → synonym edges.  
- **Read (online):** extract query named entities → link to KG nodes → **Personalized PageRank** with reset on query nodes → aggregate node mass onto passages → retrieve. Single-step multi-hop.  
- **Forget:** not a first-class operator (static corpus framing).

**Compaction.** Synonym edges compress lexical variants; no temporal consolidation loop.

**Conflict / supersession.** Silent — contradictory triples can coexist; retrieval ranks, does not adjudicate truth.

**Privacy / sharing.** None.

**MoDeX design lessons (5):**
1. Entity graph + associative walk (PPR-like) is the right *retrieval* substrate for cross-file / multi-hop engineering questions — distinct from Anchor *truth* store.
2. Synonym / alias edges between entity names reduce false misses (file paths, API names, library aliases).
3. Seed retrieval from **query entities**, then expand neighborhood — hydrate packs should expand ABOUT entities, not only cosine on Anchor text.
4. Do **not** treat KG triples as Anchors; triples are Evidence indices.
5. Pattern separation (atomic phrases) + pattern completion (graph walk) maps to Anchor atomicity + LINKED_TO expansion.

---

### 2.3 HippoRAG 2 — From RAG to non-parametric continual learning  
**arXiv:2502.14802** · Gutiérrez et al. · 2025 (ICML) · **FULL-READ**

**Problem setup.** HippoRAG’s entity-centric design loses context and underperforms factual/sense-making vs strong embedding RAG. Need one system good at factual, sense-making, *and* associative memory.

**Memory representation.** Phrase nodes + relation edges + **passage nodes** with `contains` context edges (dense–sparse integration). Synonym edges retained. KG aids retrieval; does **not** expand the corpus with LLM summaries (contrast GraphRAG/LightRAG).

**Write / read / forget.**  
- Indexing same OpenIE + synonym + passage nodes.  
- Retrieval: **query-to-triple** embedding match (default) → **recognition memory** LLM filter on top-k triples → PPR with seeds → passages for QA. Alternatives evaluated: NER→node, query→node.  
- Forget: none.

**Compaction.** Phrase nodes = sparse concepts; passage nodes = dense context; recognition filter reduces seed noise.

**Conflict / supersession.** Still retrieval-ranking, not belief revision.

**Privacy / sharing.** None.

**MoDeX design lessons (6):**
1. Store **both** sparse entities and dense episode/passage nodes in the graph (MoDeX Entity + Episode + ABOUT).
2. Prefer query→(Anchor/Evidence triple) matching over NER-only seeding for hydrate.
3. Add a **recognition filter** (cheap LLM or rules) before expensive graph expansion / pack compile — reduces wrong-community bleed.
4. Use KG for **routing to Evidence**, not as a second generative summary corpus (avoids summary-induced noise HippoRAG 2 criticizes in GraphRAG/LightRAG for QA).
5. Reset-probability / seed weighting ≈ hydrate importance weights on workstream entities.
6. Continual learning claim = append passages/episodes; MoDeX should append L0→L2 without rewriting historical Evidence.

---

### 2.4 A-MEM — Agentic Zettelkasten memory  
**arXiv:2502.12110** · Xu et al. · 2025 (NeurIPS) · **FULL-READ**

**Problem setup.** Fixed workflows + predefined graph schemas limit adaptation; need autonomous organization for long-term agent interaction.

**Memory representation.** Atomic note \(m_i=\{c_i,t_i,K_i,G_i,X_i,e_i,L_i\}\): content, timestamp, keywords, tags, contextual description, embedding, link set. Multi-box: a note may belong to multiple emergent “boxes” via links.

**Write / read / forget.**  
- **Write:** LLM generates \(K,G,X\) → embed concat → top-k similar notes → LLM decides links \(L\) → **memory evolution** LLM may rewrite neighbors’ \(X/K/G\).  
- **Read:** embed query → cosine top-k; linked co-box notes come along.  
- **Forget:** not specified as delete; evolution overwrites attributes in place.

**Compaction / consolidation.** Evolution creates higher-order patterns; no separate archival tier.

**Conflict / supersession.** Implicit via evolution rewrite — **no audit of superseded text**.

**Privacy / sharing.** None.

**MoDeX design lessons (6):**
1. Write-time **link generation** after insert mirrors MoDeX LINKED_TO / RELATES_TO at Anchor creation.
2. Atomic notes ≈ Anchors; generated keywords/tags ≈ entity hints + kind.
3. **Memory evolution of historical notes is dangerous for engineering truth** — prefer append new Anchor + SUPERSEDES over mutating Anchor statement in place.
4. If evolution is used, restrict to L1 WorkingState / non-sealed fields, never sealed pack contents.
5. Multi-box membership ≈ Anchors in multiple workstreams/communities without duplicating canonical ID.
6. Agency at *storage structure* (not only retrieval) is valuable — but MoDeX should keep schema-locked kinds (decision/rejection/…) rather than free-form tags only.

---

### 2.5 Nemori — Self-organizing agent memory (EST + predict–calibrate)  
**arXiv:2508.03341** · Nan, Ma, Wu, Chen · **FULL-READ** of v1 HTML (“Nemori: Self-Organizing…”) and v4 rewrite (“What Deserves Memory…”)

**Problem setup.** Arbitrary memory granularity + passive extraction prevent genuine learning. Two challenges: define chunk \(x\), design organizing function \(f\).

**Memory representation.** Dual store: **episodic narratives** (title ξ + body ζ + provenance to raw segment) and **semantic knowledge** statements. Buffer of role/content/timestamp messages per user.

**Write / read / forget.**  
- **Boundary Alignment:** LLM detector \((b_{\mathrm{boundary}}, c_{\mathrm{boundary}})\) on new message vs buffer; topic-coherent episodes (top-down EST, vs EM-LLM bottom-up surprise).  
- **Representation Alignment:** episode generator → rich narrative with temporal anchors.  
- **Predict–Calibrate:** (1) retrieve semantic K relevant to new episode title/content; (2) predict episode \(\hat{e}\) from K; (3) calibrate against **raw segmented messages M** (not the narrative) → distill \(K_{\mathrm{new}}\) from prediction gap; (4) integrate into semantic DB.  
- **Read:** unified dense Retrieve(q, D, m, σ_s) over episodic + semantic.  
- **Forget:** not primary; selection via “what deserves memory” = unpredicted residual.

**Compaction.** Episodes compress dialogue; semantic store grows from gaps only (non-redundant).

**Conflict / supersession.** Calibration adds knowledge; paper is light on explicit contradiction operators (later ACL framing emphasizes distillation agnostic to downstream management).

**Privacy / sharing.** Per-user buffers; no cross-principal ACL theory.

**MoDeX design lessons (7):**
1. **Segment L0→L2 by semantic boundaries**, not N-turn windows — EST aligns with MoDeX episode digests.
2. Promote to L3 Anchors preferentially from **prediction gaps** (what WorkingState/semantic base failed to foresee) — high-signal for decisions/rejections.
3. Calibrate against **raw Evidence**, not against the L2 summary (avoids summary-eating-summary drift).
4. Episode title+narrative is a good L2 schema; keep pointer to observation span.
5. Async predict–calibrate pipeline fits compaction boundaries (stop / pre_compact / workstream switch).
6. Top-down boundary detection > surprise-only for multi-party eng sessions with topic shifts.
7. “What deserves memory” ≠ importance heuristic alone — unpredictability/usefulness beats always-extract (see also RecMem).

---

### 2.6 Mem0 — Production long-term memory + graph variant  
**arXiv:2504.19413** · Chhikara et al. · 2025 · **FULL-READ**

**Problem setup.** Fixed context windows break multi-session coherence; full-context is costly and attention-degraded.

**Memory representation.**  
- **Mem0:** salient fact memories in vector DB + conversation summary S + recent window.  
- **Mem0\(^g\):** directed labeled graph \(G=(V,E,L)\); entity nodes (type, embedding, \(t_v\)); relationship triplets \((v_s,r,v_d)\); Neo4j.

**Write / read / forget.**  
- Ingest message pair \((m_{t-1},m_t)\) with context \(P=(S,\text{recent},m_{t-1},m_t)\).  
- Extract candidate facts Ω via LLM.  
- Update phase: retrieve top-s similar memories → LLM **tool-call** chooses **ADD / UPDATE / DELETE / NOOP**.  
- Graph path: entity extract → relation generate → similarity node match → **conflict detection**; update resolver marks obsolete relationships **invalid** (soft delete) for temporal reasoning.  
- Read: entity-centric subgraph expansion **and/or** semantic triplet embedding match.

**Compaction.** Async global conversation summary; fact consolidation via UPDATE; graph invalidation.

**Conflict / supersession.** Explicit four-way op; graph marks invalid rather than hard delete.

**Privacy / sharing.** Production product concerns; paper does not formalize multi-tenant ACL.

**MoDeX design lessons (6):**
1. Anchor upsert should be an explicit enum: ADD / UPDATE / SUPERSEDE(DELETE) / NOOP — matches Mem0 tool-call discipline.
2. Always retrieve similar existing Anchors before write (s≈10) to prevent duplicate decisions.
3. Soft-invalid graph edges ≈ AnchorStatus.superseded with retained row.
4. Dual retrieval (entity-walk + embedding) is the right hydrate strategy for packs.
5. Pair-level extraction is too chat-centric for coding agents — MoDeX should extract on **judgment boundaries** (decision/rejection signals), not every turn (RecMem/Nemori).
6. Global summary S ≈ L1 WorkingState digest; keep it async so capture path stays cheap.

---

### 2.7 MemGPT — OS-inspired virtual context  
**arXiv:2310.08560** · Packer et al. · 2023 · **FULL-READ**

**Problem setup.** Finite context + poor long-context utilization; need illusion of unbounded memory via hierarchical paging.

**Memory representation.**  
- **Main context (prompt tokens):** system instructions (RO) + **working context** (RW unstructured) + **FIFO queue** (messages + function IO) with recursive summary at queue head.  
- **External context:** **recall storage** (message DB) + **archival storage** (arbitrary text objects, vector search).

**Write / read / forget.** Entirely **self-directed via function calls**. Queue manager: append → infer → on warning token % insert memory-pressure alert → LLM may save to working/archival → on flush % evict ~50%, recompute recursive summary. Read: search archival/recall with pagination cognizant of token limits. `request_heartbeat` chains multi-step retrieval.

**Compaction.** FIFO eviction + recursive summary; working context holds key facts/persona.

**Conflict / supersession.** Unstructured overwrite of working context; no typed contradiction algebra.

**Privacy / sharing.** Single-agent persona setting; no multi-user governance.

**MoDeX design lessons (6):**
1. L1 WorkingState ↔ MemGPT working context; L4 handoff ↔ compiled main context boot pack.
2. **Memory-pressure warnings before eviction** — MoDeX pre_compact hooks should force Anchor extraction *before* L0 prune.
3. Archival vs recall split ≈ Evidence/raw vs searchable Episode index.
4. Self-directed memory tools are powerful but unsafe as sole capture for eng teams — MoDeX should **also** autocapture via hooks (don’t rely on agent remembering to write).
5. Recursive queue summary is lossy — never the sole L3; Anchors must be extracted first.
6. Pagination of retrieval is a hydrate-budget primitive for sealed packs.

---

### 2.8 Generative Agents — Memory stream, importance, reflection  
**arXiv:2304.03442** · Park et al. · 2023 · **FULL-READ** (focus: reflection/importance)

**Problem setup.** Believable long-horizon agent behavior needs memory beyond the context window.

**Memory representation.** Natural-language **memory stream** of observations; reflections and plans re-enter the stream. Reflection trees: leaves = observations; higher nodes = increasingly abstract insights with **citations** to supporting memories.

**Write / read / forget.**  
- Every perception appended.  
- **Retrieval score** = normalized weighted sum: \(\alpha_r\cdot\mathrm{recency}+\alpha_i\cdot\mathrm{importance}+\alpha_{rel}\cdot\mathrm{relevance}\).  
  - Recency: exponential decay over sandbox hours since last access.  
  - Importance: LLM poignancy 1–10 at creation (“mundane … extremely poignant”).  
  - Relevance: embedding similarity to query memory.  
- **Reflection trigger:** when sum of importance scores of recent events exceeds threshold (**150** in paper) → generate salient questions from last 100 records → retrieve → extract insights **with evidence pointers** → store reflections. ~2–3×/day in sim.

**Compaction.** Reflection synthesizes; raw observations remain.

**Conflict / supersession.** Not modeled; retrieval failures / embellishment are main error modes.

**Privacy / sharing.** Multi-agent sandbox; information diffusion is emergent dialogue, not ACL.

**MoDeX design lessons (6):**
1. Observation.importance ∈ [0,1] already in schema — calibrate with poignancy-style prompts for eng events (rejection, outage, API break = high).
2. Hydrate ranking = **recency × importance × relevance** (not cosine alone).
3. Reflection passes should emit Anchors **with Evidence citations** (reflection trees = DERIVES/SUPPORTS).
4. Trigger reflection/compaction on **accumulated importance**, not only wall-clock or token count.
5. Ablations show reflection critically improves judgment — MoDeX “why” Anchors need a reflection path, not only raw logs.
6. Common failure = retrieve miss + embellishment → sealed handoff must prefer structured Anchors over free-form regenerated prose.

---

### 2.9 RecMem — Recurrence-based consolidation  
**arXiv:2605.16045** · Dai et al. · 2026 · **FULL-READ**

**Problem setup.** Eager LLM consolidation every turn wastes tokens; most interactions don’t deserve extraction.

**Memory representation.** Three tiers: **subconscious** (raw interaction units + lightweight embeddings), **episodic** (event narratives, merge-first per topic), **semantic** (persistent facts via refinement).

**Write / read / forget.**  
- Always write subconscious.  
- **Consolidate only if** retrieved similar subconscious set size ≥ recurrence threshold.  
- Then LLM builds/merges episodic summary; **semantic refinement** re-reads raw units to recover omitted fine facts.  
- Query: budgeted retrieve from all three tiers.

**Compaction.** Recurrence gate + merge-first episodes (prevents parallel episode fragmentation on same topic).

**Conflict / supersession.** Merge-first updates narrative; not a full contradiction algebra.

**Privacy / sharing.** None.

**MoDeX design lessons (6):**
1. L0 can stay cheap/embed-only; don’t LLM-extract Anchors every hook event.
2. Promote L0→L2/L3 when **recurrence** across sessions/workstreams signals durable judgment (repeated rejection of same approach).
3. Semantic refinement after episodic summarize = Evidence pass that protects Anchor fidelity.
4. Merge-first episodes map to CONTINUES / SAME_WORKSTREAM episode chaining.
5. Subconscious retrieval remains available for rare one-off queries — don’t delete L0 until after promotion opportunity.
6. Token-cost discipline is a first-class architecture constraint for local-first MoDeX.

---

### 2.10 ES-Mem — Event segmentation memory  
**arXiv:2601.07582** · Zou et al. · 2026 · **FULL-READ**

**Problem setup.** Fixed-turn granularity fragments semantics; flat vector retrieval ignores discourse structure.

**Memory representation.** Hierarchical: **refined boundaries** (anchors), **event summaries**, **raw context**. Dynamic segmentation via topical coherence + intent-transition probabilities (two-stage).

**Write / read / forget.** Segment dialogue into events; store multi-layer. Retrieve: use **boundary semantics as cognitive anchors** to locate episode interval → fine rerank inside. Evaluated on LoCoMo / LongMemEval-S; segmenter also on DialSeg711/TIAGE/SuperDialSeg.

**Compaction.** Boundaries compress sequence into indices (EST claim: boundaries are access points).

**Conflict / supersession.** Not central.

**Privacy / sharing.** None.

**MoDeX design lessons (5):**
1. Treat episode **boundary records** as first-class indices in the graph (not only episode blobs).
2. Hydrate: retrieve by boundary/topic anchor → then pull Evidence inside span.
3. Intent-transition signals (goal change, rejection, plan shift) are natural eng segmenters for L2.
4. Flat cosine over mixed L0+L3 is insufficient; hierarchical locate-then-rerank matches sealed pack compile.
5. EST boundaries ≈ MoDeX compaction triggers (topic/workstream switch).

---

### 2.11 EM-LLM — Surprise-based episodic KV memory  
**arXiv:2407.09450** · Fountas et al. · 2024 · **FULL-READ**

**Problem setup.** Transformers fail beyond training length; fixed-size KV blocks (InfLLM) ignore event structure.

**Memory representation.** Token sequences → episodic **events** via (a) **Bayesian surprise** boundaries during inference, (b) graph-theoretic **boundary refinement** (attention-key similarity as adjacency; maximize within-event cohesion / cross-event separation). Context = initial tokens + contiguity buffer + similarity buffer + local context.

**Write / read / forget.** Online segmentation; retrieve via k-NN similarity **plus temporal contiguity/asymmetry**; refined events stored as memory units. No fine-tuning. Scales to ~10M tokens in passkey experiments.

**Compaction.** Event units replace fixed blocks; refinement consolidates related tokens.

**Conflict / supersession.** N/A (context organization, not belief store).

**Privacy / sharing.** None.

**MoDeX design lessons (5):**
1. Surprise/prediction-error is a complementary L0→L2 boundary signal (pair with Nemori/ES-Mem top-down).
2. Retrieve neighbors in **time** around a hit — eng debugging often needs contiguous episode windows, not isolated chunks.
3. Boundary refinement objective (cohesion/separation) can score candidate episode cuts.
4. Keep initial tokens / constitution (system Anchors) always in L4 pack — analogous to EM-LLM initial-token retention.
5. EM-LLM is KV/context architecture; don’t confuse with Anchor truth layer — use for session compaction heuristics only.

---

### 2.12 StateFuse — Conflict-preserving replicated memory contract  
**arXiv:2607.05844** · Volkov, Li, Luo · 2026 · **FULL-READ**

**Problem setup.** Multi-agent branches/retries accumulate conflicts; overwrite memory hides disagreement and blocks safe abstention/correction.

**Memory representation.** OpSet/CRDT substrate (set-union merge). Objects: **Evidence**, **Claim** keyed by `(namespace, subject, predicate)` with value/confidence/time/provenance, **Retraction**, **Decision**. Dual IDs: `claim_id` (exact) + `claim_ref` (semantic, predicate-contract derived).

**Write / read / forget.** Ops: EvidenceAdded, ClaimAdded, ClaimRetracted(target id/ref, reason, supersedes…), DecisionAdded. Merge = ∪. Materialize → ConflictSet for functional predicates with multiple active values. **Projection** `build_view` chooses/abstains; resolvers **cannot mutate base**. Forget = retraction (exact or semantic; unseen-target no-resurrection). Compaction must be **projection-equivalent**.

**Conflict / supersession.** First-class ConflictSet; explicit retraction; conservative resolver abstains on symmetric conflicts. Empirical claim is narrow: better contradiction surfacing/abstention, **not** universal accuracy gains.

**Privacy / sharing.** Authenticated sync can reject invalid signed claims — lightweight integrity, not full ACL.

**MoDeX design lessons (8):**
1. MoDeX Anchors should support **disputed** status with visible ConflictSet in hydrate, not silent last-write.
2. Dual handles: opaque `anc_` id + semantic claim_ref (kind+entities+normalized statement) for cross-replica SUPERSEDES.
3. Sealed handoff = **projection**, never rewrite store — matches L4 vs L3 separation.
4. Workstream = namespace in ClaimKey.
5. Evidence and Decision are distinct from Claims (truth vs planning metadata).
6. Retraction must cascade by semantic ref when pack replicas lack original ids.
7. Evaluations that collapse conflicts look accurate when gold=latest — eng memory must optimize **safe abstention**, not only EM.
8. Predicate registry (functional vs multi-valued) ≈ AnchorKind rules (one active decision per subject vs many open_questions).

---

### 2.13 TOKI — Bitemporal operator algebra for contradictions  
**arXiv:2606.06240** · Wang · 2026 · **FULL-READ**

**Problem setup.** Production memories use LWW / evidence-weighted merge / await-confirmation / per-rule policy without declaring isolation assumptions → replay inconsistency, belief-drift skew, audit erasure.

**Memory representation.** Dual-row bitemporal schema: **current row** + **audit row** preserving losing fact. Valid time vs system time. Contradiction resolution = **write-time concurrency control**.

**Write / read / forget.** Gate routes conflicts to typed operators (four heuristics as one operator family), each with isolation precondition + provenance annotation. Soundness theorems over isolation/schema/provenance; pipelines; n-ary conflict sets. Tightness: keyed logging of adjudicating LLM judge necessary for replay consistency (baselines omit this).

**Compaction.** Audit rows preserve losers; fold operators over conflict sets.

**Conflict / supersession.** Core contribution — typed operators, not ad-hoc prompts.

**Privacy / sharing.** Not focus; provenance/audit are the governance primitives.

**MoDeX design lessons (7):**
1. Every SUPERSEDES must write an **audit row** (losing Anchor retained, not erased).
2. Log the **judge prompt+output+model** keyed to the write (replay consistency).
3. Declare isolation level for concurrent workstream writers (branch A vs B editing same decision subject).
4. Encode LWW vs await-human-confirmation as **named operators**, not buried prompt text.
5. Bitemporal valid_time vs system_time mirrors Graphiti and MoDeX provenance needs.
6. Do not claim cross-system accuracy superiority without powered eval — TOKI itself refuses this; MoDeX docs should too.
7. n-ary conflict sets > pairwise only (three agents, three rejected approaches).

---

### 2.14 LightRAG — Dual-level graph RAG  
**arXiv:2410.05779** · Guo et al. · 2024 · **FULL-READ**

**Problem setup.** Flat RAG misses entity interdependence; need efficient graph RAG with incremental updates.

**What it stores vs retrieves.**  
- **Stores:** chunked docs → LLM entity+relation extraction → deduped KG; per entity/relation **(key, value)** where value summarizes relevant snippets; relations get extra global-theme keys.  
- **Retrieves:** **dual-level** — low-level (specific entities/relations) + high-level (themes); graph+vector lookup; merges subgraph context for generation.  
- **Incremental:** process new docs same pipeline; union nodes/edges — **no full rebuild**.

**Write / read / forget.** Index-time extraction; query-time dual retrieval. Forget/invalidation not first-class.

**Conflict / supersession.** Dedup/profile merges; not temporal belief revision.

**Privacy / sharing.** None in paper (known multi-tenant gaps in implementations — see prior MoDeX privacy memo).

**MoDeX design lessons (5):**
1. Dual-level hydrate: local (file/entity Anchors) + global (workstream/community themes).
2. Incremental subgraph union fits append-only eng memory.
3. Relation values as snippet summaries ≈ Evidence digests; keep separate from Anchor statements.
4. Do not rebuild entire repo graph on every session — incremental only.
5. LightRAG stores *retrieval indices*, not authoritative decisions — Anchors remain compact-native truth.

---

### 2.15 GraphRAG — Local-to-global query-focused summarization  
**arXiv:2404.16130** · Edge et al. (Microsoft) · 2024 · **FULL-READ**

**Problem setup.** Global sensemaking questions over corpora; vector RAG returns fragmented local chunks.

**What it stores vs retrieves.**  
- **Stores:** chunks → entities, relationships, **claims** (covariates) → KG → **Leiden hierarchical communities** → element summaries → community report summaries (bottom-up substitution when context overflows).  
- **Retrieves (query):** map-reduce over community summaries → partial answers → reduced global answer. Community hierarchy enables different resolution levels.  
- Graph is an **index for summarization**, not an online invalidating memory.

**Write / read / forget.** Batch index; query-time QFS. No bi-temporal invalidation.

**Conflict / supersession.** Claims extracted but not versioned as beliefs.

**Privacy / sharing.** None (static corpus assumption).

**MoDeX design lessons (5):**
1. Community reports are excellent for **dashboard / onboarding sensemaking**, weak as L3 truth — keep them derived views.
2. Claims-as-covariates ≈ Evidence supporting Anchors.
3. Hierarchical communities can index Entity/Anchor clusters for hydrate zoom levels.
4. Map-reduce QFS ≠ sealed handoff; handoff should prefer ranked Anchors first (MoDeX lock).
5. HippoRAG 2’s critique applies: generative community text can inject noise into factual eng Q&A — use carefully.

---

### 2.16 SSGM — Stability & Safety Governed Memory (framework)  
**arXiv:2603.11768** · Lam et al. · 2026 · **FULL-READ**

**Problem setup.** Adaptive agent memory creates compounding risks: poisoning at ingest, semantic/procedural drift at consolidation, hallucination/conflict at retrieval. Prior surveys under-emphasize governance.

**Memory representation.** Conceptual governance architecture: **decouple memory evolution from governance**. Evolution dims: content abstraction, structural reorganization (lists→graphs), policy optimization.

**Write / read / forget.** SSGM inserts consistency verification, temporal decay, dynamic access control **before consolidation**. Failure taxonomy: intrinsic drift vs extrinsic threats. Trade-offs: latency↔safety, stability↔plasticity, graph scalability.

**Compaction / consolidation.** Governed — not free agent self-rewrite.

**Conflict / supersession.** Consistency verification prior to solidification.

**Privacy / sharing.** Dynamic access control; topology-induced leakage called out (sensitive context solidified into LTM).

**MoDeX design lessons (6):**
1. **Promotion gates** (private→shareable Anchor) are governance, not just extraction quality.
2. Never let the coding agent unilaterally rewrite sealed L3 without verification/policy.
3. Temporal decay belongs on L0/Evidence budgets; Anchors decay only via explicit SUPERSEDES/archive.
4. Stability–plasticity: workstream-local plasticity, repo_shared_safe stability.
5. Taxonomy of evolution (content/structure/policy) matches MoDeX schema vs graph vs capability policy.
6. SSGM is a framework paper — use as checklist, not as drop-in store.

---

### 2.17 Survey — *Memory in the Age of AI Agents: Forms, Functions and Dynamics*  
**arXiv:2512.13564** · Hu, Liu, Yue, Zhang et al. · 2025/2026 · **FULL-READ** (PDF, ~64k words)

**Taxonomy (primary):**

| Axis | Categories |
|------|------------|
| **Forms** (what carries memory) | Token-level (flat 1D / planar 2D graphs / hierarchical 3D); Parametric (internal / external); Latent (generate / reuse / transform) |
| **Functions** (why) | **Factual** (user / environment); **Experiential** (case / strategy / skill / hybrid); **Working** (single-turn / multi-turn) |
| **Dynamics** (how) | **Formation** (summarization, distillation, structured construction, latent, parametric internalization); **Evolution** (consolidation, updating, forgetting); **Retrieval** (timing/intent, query construction, strategies, post-processing) |

**Scope clarifications:** Agent memory ≠ LLM KV memory ≠ static RAG ≠ context engineering — overlapping tech, different temporal/self-evolving roles. Lifecycle operators: Formation \(F\), Evolution \(E\), Retrieval \(R\) over unified state \(M_t\).

**Frontiers called out:** automated memory management; RL×memory; multimodal; **shared multi-agent memory**; trustworthy memory; cognitive connections.

**Cited papers → one-line contribution (representative map of the “200+” corpus):**

| Paper / system | One-line contribution |
|----------------|----------------------|
| Generative Agents (Park et al., 2023) | Memory stream + recency/importance/relevance retrieval + reflection trees |
| MemGPT / Letta (Packer et al., 2023) | OS-tiered main vs archival/recall; self-directed paging |
| Reflexion (Shinn et al., 2023) | Verbal reinforcement stored as reflective memory for next trials |
| Voyager (Wang et al., 2023) | Skill library as experiential/procedural memory |
| MemoryBank (Zhong et al., 2024) | Long-term personal memory with Ebbinghaus-style forgetting |
| SCM (Wang et al.) | Self-controlled memory stream + controller |
| A-MEM (Xu et al., 2025) | Zettelkasten notes with write-time linking + evolution |
| Mem0 (Chhikara et al., 2025) | Fact extract + ADD/UPDATE/DELETE/NOOP; graph variant |
| Zep/Graphiti (Rasmussen et al., 2025) | Bi-temporal KG episodes→entities→communities; invalidate edges |
| HippoRAG / HippoRAG 2 | OpenIE KG + Personalized PageRank associative retrieval |
| GraphRAG (Edge et al., 2024) | Leiden communities + map-reduce global summarization |
| LightRAG (Guo et al., 2024) | Dual-level entity/theme retrieval + incremental graph union |
| RAPTOR (Sarthi et al., 2024) | Hierarchical tree summaries via clustering |
| EM-LLM (Fountas et al., 2024) | Surprise + graph refinement episodic KV segmentation |
| Nemori (Nan et al., 2025) | EST boundaries + predict–calibrate semantic distillation |
| RecMem (Dai et al., 2026) | Subconscious buffer + recurrence-gated consolidation |
| ES-Mem (Zou et al., 2026) | EST segmentation + boundary-anchored hierarchical retrieval |
| MemoryOS (Kang et al., 2025) | Hierarchical OS-like memory management baseline in later evals |
| G-Memory / AriGraph | Graph-structured agent memory variants |
| MemAgent / MEM1 / Memory-R1 | RL-enabled / agentic memory managers |
| Memento / H2R | Self-evolving memory lines |
| Retroformer / Early Experience | Parametric memory adaptation |
| MemoryLLM / M+ / MemGen | Latent / parametric memory models |
| HiAgent / ReSum | Working-memory managers for multi-turn tasks |
| AgentGit | Git-like rollback/branch for agent workflows (complementary to StateFuse) |
| Collaborative Memory (2025) | Private∪shared tiers with provenance & bipartite permissions |
| LongMemEval / LoCoMo / MemoryAgentBench | Evaluation harnesses exposing temporal & conflict failures |

*(Survey body cites far more; table above is the mechanism-relevant spine for MoDeX mapping. Full living list: https://github.com/Shichun-Liu/Agent-Memory-Paper-List)*

**MoDeX design lessons (6):**
1. MoDeX is primarily **token-level hierarchical (3D) + factual/experiential functions** — not parametric.
2. Distinguish factual Anchors vs experiential skills/playbooks vs L1 working memory in product language.
3. Dynamics triad \(F/E/R\) should be explicit CLI verbs (capture/cognify/hydrate).
4. Shared multi-agent memory is a **frontier with trustworthiness debt** — align with sealed capability packs.
5. Short/long-term is emergent from operator schedules, not only module names — MoDeX L0–L4 already does this better.
6. Use survey resources section for benchmark selection (LoCoMo, LongMemEval, MemoryAgentBench conflict slices).

---

### 2.18 Survey — *A Survey on the Memory Mechanism of LLM-based Agents*  
**arXiv:2404.13501** · Zhang et al. · 2024 · **FULL-READ** (PDF)

**Contribution.** Earlier comprehensive survey: cognitive psychology framing; memory definitions (narrow vs broad); writing/reading/reflection operations; application domains; humanoid agents. Useful historical baseline; taxonomy superseded in granularity by 2512.13564 Forms–Functions–Dynamics, but still valuable for cognitive parallels (sensory/short-term/long-term; episodic/semantic).

**MoDeX lessons (3):** Keep cognitive dual episodic/semantic language in docs; treat 2024 survey as map of pre-Mem0/Graphiti era; prefer 2512.13564 for 2025–2026 corpus navigation.

---

## 3. Cross-cutting synthesis for MoDeX

### 3.1 What the corpus agrees on
1. **Raw ≠ durable:** always a cheap buffer (L0/subconscious/episodes) plus compacted semantic layer (L3).
2. **Invalidate > delete** for belief change (Graphiti, Mem0g, StateFuse, TOKI).
3. **Provenance is mandatory** for trust (episode↔fact edges, reflection citations, audit rows).
4. **Flat cosine retrieval is insufficient** for multi-hop eng reasoning — need structure (entities, boundaries, communities).
5. **Eager LLM extraction every turn is the wrong default** (RecMem, Nemori gap-learning).

### 3.2 Where papers disagree (design choices MoDeX already locked)
| Debate | MoDeX lock |
|--------|------------|
| Mutate historical notes (A-MEM) vs append+supersede | **Append + SUPERSEDES**; no silent mutation of sealed Anchors |
| KG as generative corpus (GraphRAG) vs KG as retrieval index (HippoRAG 2) | **Index + Evidence**; Anchors are compact-native truth |
| Self-directed memory only (MemGPT) vs autocapture | **Hooks + CLI autocapture**; agent tools optional |
| Collapse conflicts for accuracy vs surface them | **Surface (disputed)**; projection/handoff may abstain |
| Importance heuristics vs recurrence/prediction-gap | Combine: importance for ranking; recurrence/gap for promotion |

### 3.3 Mapping onto Anchors+Evidence / L0–L4 / sealed handoff / workstreams

```text
L0  hooks/events          ← subconscious (RecMem), FIFO (MemGPT), surprise tokens (EM-LLM)
L1  WorkingState          ← working context (MemGPT), mission brain, async summary (Mem0)
L2  Episodes              ← EST segments (Nemori/ES-Mem), Graphiti episodes, RecMem episodic
L3  Anchors (+Evidence)   ← semantic facts/claims/edges; invalidatable; audit-retained
L4  sealed handoff .mxp   ← MemGPT main-context compile; StateFuse projection; budgeted hydrate
Workstream namespace       ← ClaimKey.namespace; Graphiti subgraph; community optional
```

### 3.4 Highest-priority mechanism imports (implementation order)
1. **Bi-temporal fields + SUPERSEDES audit rows** (Graphiti + TOKI).
2. **ConflictSet / disputed projection** for hydrate (StateFuse).
3. **Recurrence- or gap-gated Anchor promotion** (RecMem + Nemori).
4. **Entity graph + associative expand** for pack compile (HippoRAG 2).
5. **Importance×recency×relevance ranking** (Generative Agents).
6. **Governance before shareable promotion** (SSGM + prior privacy memo).

---

## 4. CORPUS INDEX

| paper | year | deep-read? | one-paragraph insight | MoDeX relevance |
|-------|------|------------|----------------------|-----------------|
| Zep / Graphiti (2501.13956) | 2025 | **FULL** | Temporally-aware KG with episode→entity→community tiers; bi-temporal edge invalidation prefers newer writes while retaining history. | Blueprint for L2/L3 graph + SUPERSEDES timestamps + non-lossy Evidence provenance. |
| HippoRAG (2405.14831) | 2024 | **FULL** | OpenIE KG + synonym edges + Personalized PageRank turns multi-hop QA into one associative retrieval step. | Hydrate/entity expansion algorithm; not a truth store. |
| HippoRAG 2 (2502.14802) | 2025 | **FULL** | Adds passage nodes, query-to-triple seeding, recognition-memory filter; KG indexes retrieval rather than generating summary corpora. | Best associative retrieval design to pair with Anchors. |
| A-MEM (2502.12110) | 2025 | **FULL** | Zettelkasten atomic notes with LLM keywords/tags/context, write-time linking, and neighbor evolution. | Link-on-write yes; in-place evolution no for sealed Anchors. |
| Nemori (2508.03341v1/v4) | 2025–26 | **FULL** | EST topic boundaries → episodic narratives; predict–calibrate distills semantic memory from prediction gaps vs raw dialogue. | L0→L2 segmentation + promotion-from-gaps for L3. |
| Mem0 / Mem0g (2504.19413) | 2025 | **FULL** | Extract facts then LLM tool-call ADD/UPDATE/DELETE/NOOP; graph variant soft-invalidates conflicting edges. | Upsert enum + dual entity/embedding retrieval. |
| MemGPT (2310.08560) | 2023 | **FULL** | OS paging: working context + FIFO + archival/recall; memory-pressure warnings; self-directed function IO. | L1/L4 compile + pre_compact extraction mandate. |
| Generative Agents (2304.03442) | 2023 | **FULL** | Memory stream ranked by recency×importance×relevance; reflection trees with cited evidence when importance sum exceeds threshold. | Importance scoring + reflection→Anchor with Evidence. |
| RecMem (2605.16045) | 2026 | **FULL** | Subconscious embed store; LLM consolidate only under recurrence; semantic refinement recovers omitted facts. | Anti-eager extraction; recurrence promotion; cheap L0. |
| ES-Mem (2601.07582) | 2026 | **FULL** | Dynamic EST segmentation + hierarchical boundary→summary→raw retrieval. | Episode boundary indices + locate-then-rerank hydrate. |
| EM-LLM (2407.09450) | 2024 | **FULL** | Bayesian surprise + graph boundary refinement for episodic KV units; similarity+contiguity retrieval. | Compaction heuristics; contiguous Evidence windows. |
| StateFuse (2607.05844) | 2026 | **FULL** | OpSet memory contract: immutable Evidence/Claim/Retraction/Decision; ConflictSet at projection; dual correction handles. | Disputed Anchors; L4 projection authority bounds; workstream namespaces. |
| TOKI (2606.06240) | 2026 | **FULL** | Types LWW/merge/await/policy as bitemporal operators with audit rows; proves judge logging needed for replay. | SUPERSEDES operators + audit + isolation for concurrent writers. |
| LightRAG (2410.05779) | 2024 | **FULL** | Graph index with dual-level local/global retrieval and incremental union updates. | Incremental graph; dual hydrate levels; Evidence snippet values. |
| GraphRAG (2404.16130) | 2024 | **FULL** | Entities/claims→Leiden communities→hierarchical summaries; query via map-reduce community QFS. | Optional community views; not Anchor source of truth. |
| SSGM (2603.11768) | 2026 | **FULL** | Governance framework decoupling evolution from policy; drift/poisoning taxonomy; access control before consolidation. | Shareable promotion gates; agent must not unilaterally rewrite L3. |
| Memory in the Age of AI Agents (2512.13564) | 2025 | **FULL** | Forms×Functions×Dynamics taxonomy; formal F/E/R lifecycle; huge curated corpus + benchmarks. | Vocabulary alignment + cited-paper map for MoDeX. |
| Memory Mechanism Survey (2404.13501) | 2024 | **FULL** | Pre-2025 survey of agent memory write/read/reflect and cognitive framing. | Historical baseline; superseded taxonomy-wise by 2512.13564. |
| Survey “Second Half” (2602.06052) | 2026 | **FULL text on disk; light use** | Self-evolving / long-horizon survey framing. | Corroborating pointer only this session. |

---

## 5. Gaps relative to MoDeX (honest)

- Almost no paper solves **engineering-judgment memory** (decisions/rejections/gotchas) as first-class typed Anchors.
- **Sealed, capability-gated handoff packs** are closer to ocaps / MemClaw (prior privacy memo) than to these RAG/memory systems.
- **Workstream isolation + shareable promotion** are underspecified in HippoRAG/GraphRAG/Mem0/A-MEM; SSGM/StateFuse/TOKI supply partial machinery.
- Evaluation suites (LoCoMo/LongMemEval) are chat-personal-memory; MoDeX needs conflict-bearing **eng** fixtures (MemoryAgentBench conflict slice is a start).

---

## 6. Source fetch log

| ID | Fetch path |
|----|------------|
| 2501.13956, 2405.14831, 2502.14802, 2502.12110, 2504.19413, 2605.16045, 2601.07582, 2407.09450, 2607.05844, 2606.06240, 2410.05779, 2404.16130, 2603.11768, 2508.03341* | `arxiv.org/html` → plaintext |
| 2310.08560, 2304.03442, 2602.06052 | `ar5iv.labs.arxiv.org/html` → plaintext |
| 2512.13564, 2404.13501 | `arxiv.org/pdf` → `pdftotext` |
| Nemori title note | v1 HTML title “Nemori: Self-Organizing…”; v4 HTML/PDF title “What Deserves Memory…” (same lineage) |

---

*End of memo. Mechanism detail preferred over buzzwords; no invented experimental results.*
