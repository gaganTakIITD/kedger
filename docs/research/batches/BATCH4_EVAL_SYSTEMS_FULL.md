# Batch 4 — Eval & Systems Deep-Read (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/research-measure-refine-fb37`  
> **Scope:** Evaluation suites + privacy/IFC + experience-library systems that close CORPUS_INVENTORY “next batch” gaps for Kedger metrics (S1–S8).  
> **Method:** Full arXiv HTML bodies (or PDF→text when HTML thin) fetched under `/tmp/kedger-papers/full/`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** Anchors+Evidence, SUPERSEDES, workstream capability, `.kxp` seal, Inv-Scope, `kedger why`.

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read for this memo; not previously claimed FULL in Batch2/3/P5/P6 for this ID) | **5** | Memento 2 (2512.22716); LongMemEval-V2 (2605.12493); MemoryArena (2602.16313); FLEX (2511.06449); PrefEval (2502.09597) |
| **RE-READ** (prior FULL elsewhere; re-extracted for Kedger S1–S8 / fixture mapping) | **11** | ConfAIde (2310.17884); MemBench (2506.21605); HaluMem (2511.03506); RealMem (2601.06966); CaMeL (2503.18813); MemoryAgentBench (2507.05257); LoCoMo (2402.17753); LongMemEval (2410.10813); Fides (2505.23643); AgentLeak (2602.11510); MemLeak (2606.29788) |
| **FULL+RE-READ cards this batch** | **16** | All listed above |
| **Fetch failed / skipped (no invented content)** | **0** | CaMeL HTML was thin (~844 B); **PDF extract used** (358k chars) → counted as RE-READ |
| **Identified but not carded (room)** | — | MIRIX (2507.07957) and MemoryBench (2510.17281) bodies cached; prior FULL in Batch3 / BATCH_SYSTEMS — deferred to avoid double-counting |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt` (all 16 IDs present, each >50k chars).

**Do not invent:** Where a paper is silent (typed SUPERSEDES, capability ACL, sealed packs), silence is recorded. Numbers are from paper text/tables.

---

## 1. Mechanism cards

### 1.1 Memento 2 — Learning by Stateful Reflective Memory  
**arXiv:2512.22716** · Wang · 2025/2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S4, S7, S8 |
| **problem** | Continual adaptation of frozen LLM agents without gradient fine-tuning; unify CBR/RAG heuristics with RL theory. |
| **representation** | **Stateful Reflective Decision Process (SRDP):** episodic memory \(M_t=\{m_i=(s_i,a_i,r_i,s'_i)\}\); reflected MDP augments state with memory; action = (retrieve case, LLM act). |
| **write / read / forget** | **Write** = policy evaluation (store interaction outcomes); **Read** = policy improvement (retrieve cases → reflective decision). Two-timescale online memory rewriting with convergence claims. Forget = not first-class typed invalidation. |
| **conflict** | Implicit via reward-labeled cases / denser coverage → better policy; no ConflictSet. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Map write→async cognify/promote of failure+success Evidence; read→hydrate of case Anchors. (2) Keep **failure cases** (not only wins) as first-class Evidence for `why`. (3) Treat reflection as closed loop: hooks capture → write → next session read — not one-shot RAG. (4) Do not import soft policy-iteration math into v1 CLI; import the **read=improve / write=eval** contract. |
| **metric_impact** | Fixture: eng “case bank” with reward labels (test pass/fail); measure hydrate-of-failure before retry. |
| **refine_candidate** | **yes** — S3/S7 case-bank + failure Evidence retention metric |

---

### 1.2 LongMemEval-V2 — Toward Experienced Colleagues  
**arXiv:2605.12493** · Wu, Ji, Kawatkar, et al. · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7, S8 |
| **problem** | Memory benches over chat/user history miss **environment-specific experience** that makes an agent an “experienced colleague.” |
| **representation** | Eval API: `Insert(trajectory)` + `Query(question)→compact multimodal evidence`. 451 questions; abilities: **static state recall, dynamic state tracking, workflow knowledge, environment gotchas, premise awareness**. Haystacks: Small=100 traj (~25M tok), Medium=500 traj (~115M tok). Domains: WebArena/WorkArena (Magento, Postmill, ServiceNow). |
| **write / read / forget** | Baselines: **AgentRunbook-R** (3 pools: raw observations, state-transition events, strategy notes); **AgentRunbook-C** (trajectories as files + coding-agent gather). Best: AgentRunbook-C **72.5%** avg acc vs strongest RAG **48.5%**. |
| **conflict** | Dynamic state / gotchas imply stale workflows; not typed SUPERSEDES. |
| **privacy** | Dataset ethics appendix; not capability model. |
| **Kedger lessons** | (1) Add eng-colleague abilities: **gotchas** (trap doors) + **workflows** as Anchor kinds, not only facts. (2) Hydrate should return **budgeted evidence packs**, then fixed reader — matches `.kxp` / `--live` split. (3) Dual store: raw L0 files + cognified strategy notes (R pools ≈ L0/L2/L3). (4) Premise-awareness questions ≈ `why` must surface assumptions. |
| **metric_impact** | Metric family: Static / Dynamic / Workflow / Gotcha / Premise accuracy @ evidence-token budget. |
| **refine_candidate** | **yes** — S7 evidence-budget + gotcha/workflow fixtures |

---

### 1.3 ConfAIde — Contextual integrity privacy  
**arXiv:2310.17884** · Mireshghallah et al. · 2023/24 · **RE-READ** (Batch2 FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S7, S8 |
| **problem** | LLMs violate **contextual integrity** (appropriate flow), not just secrecy. |
| **representation** | Four tiers: (1) out-of-context sensitivity; (2) flow vignettes; (3) ToM secret-sharing; (4) meeting transcript private-secret vs public action items. |
| **write / read / forget** | N/A (benchmark). Tier-4 error = leak secret **or** drop public item. |
| **conflict** | Helpfulness vs privacy incentive conflicts increase leakage. |
| **privacy** | Core: CI parameters (sender, recipient, subject, type, transmission principle). Free-form leakage persists when binary privacy Q looks OK; CoT not reliable mitigation. |
| **Kedger lessons** | (1) S6 seal metrics must include **generation probes**, not only ACL tags. (2) S4 promote never auto-shares on recurrence. (3) Pack compile = Tier-4 tradeoff: keep public decisions, strip workstream_private. (4) S8 `why` must not narrate private Evidence to unauthorized principals. |
| **metric_impact** | S6: free-form leak rate + public-item retention on share/handoff fixtures. |
| **refine_candidate** | **yes** — S6/S8 ConfAIde-style generation probes |

---

### 1.4 MemBench — Multi-level / multi-scenario memory eval  
**arXiv:2506.21605** · Tan, Zhang, et al. · 2025 · **RE-READ** (BATCH_SYSTEMS FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S3, S5, S7 |
| **problem** | Prior memory evals too narrow; need factual vs reflective levels + participation vs observation scenarios + effectiveness/efficiency/capacity. |
| **representation** | Synthetic multi-scenario dialogues; **factual memory** vs **reflective memory**; user relation graphs; multi-metric scoring. |
| **write / read / forget** | Systems under test; capacity stress as memory grows. |
| **conflict** | Reflective updates can drift from facts — capacity/effectiveness tradeoff. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Split metrics: **fact Anchors** vs **reflective digests** (don’t grade them the same). (2) Observation-only hooks (IDE telemetry) vs participation (CLI remember) need separate fixtures. (3) Track capacity curves (latency/accuracy vs store size) for cognify. |
| **metric_impact** | Effectiveness × efficiency × capacity triad for S3/S7. |
| **refine_candidate** | no (taxonomy support; constants already covered by AR/SF suite) |

---

### 1.5 HaluMem — Operation-level memory hallucination  
**arXiv:2511.03506** · Chen, Niu, et al. · 2025/26 · **RE-READ** (BATCH_SYSTEMS FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7, S8 |
| **problem** | End-to-end QA cannot localize whether hallucination arose in extract / update / QA. |
| **representation** | ~15k memory points; ~3.5k questions; Medium/Long (1.5k / 2.6k turns; >1M tokens). Tasks: **extraction**, **updating**, **QA**. Metrics: Memory Integrity (anti-amnesia), Memory Accuracy (anti-hallucination), **False Memory Resistance (FMR)**, Extraction F1; update consistency; QA faithfulness. Eval **after each session**. |
| **write / read / forget** | Gold update maps \(m_{old}\to m_{new}\); systems create/update/delete. |
| **conflict** | Update-stage gold catches wrong overwrite / unresolved conflict. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Instrument Kedger at ops: ingest extract P/R, promote/update correctness, hydrate QA faithfulness. (2) Session-boundary grading after cognify. (3) Error codes: fabricated / outdated / unresolved-conflict / wrong-retrieval. (4) Prefer SUPERSEDES+audit over opaque merge (cuts update hallucinations). |
| **metric_impact** | Per-op hallucination suite for S3/S4/S7. |
| **refine_candidate** | **yes** — operation-level HaluMem-style metrics |

---

### 1.6 RealMem — Project-oriented memory interaction  
**arXiv:2601.06966** · Bian, Yao, Hu, et al. · 2026 · **RE-READ** (P5 ★)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S3, S4, S7 |
| **problem** | Casual / task dialogue benches miss **long-term project-oriented** interaction with evolving goals. |
| **representation** | >2,000 cross-session dialogues; **11** scenarios; query types: **Temporal Reasoning, Static Retrieval, Dynamic Updating, Proactive Alignment**. Synthesis: Project Foundation → Multi-Agent Dialogue → Memory & Schedule Management. Natural user queries interleaved in sessions (not post-hoc external QA only). |
| **write / read / forget** | Dynamic project-state sync; schedule conflict resolution; proactive intent alignment. |
| **conflict** | Schedule/state conflicts via temporal reasoning + dynamic updating (not typed edges). |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Eng fixtures should be **project threads** (incident→mitigation→revert), not isolated needles. (2) Interleaved in-session queries ≈ hydrate during hooks, not only end-of-history QA. (3) Proactive Alignment ↔ SessionStart hydrate injecting constraints without explicit ask. (4) Dynamic Updating ↔ SUPERSEDES on project state Anchors. |
| **metric_impact** | Four RealMem query types as Kedger project-fixture rubric. |
| **refine_candidate** | no (feeds fixture design; HaluMem/MAB own the metric tickets) |

---

### 1.7 MemoryArena — Multi-session Memory–Agent–Environment loops  
**arXiv:2602.16313** · He, Wang, Zhi, et al. · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S4, S7 |
| **problem** | Memorization benches and single-session agent benches isolate recall from action; real agents acquire memory **while acting**. |
| **representation** | Gym with interdependent subtasks across sessions. Domains: bundled web shopping, group travel (preference constraints), progressive web search, sequential formal reasoning. Avg **~57 action steps**; traces **>40k tokens**; ~766 tasks / 6.9 interdependent ST (table). Metrics: Success Rate + Process Score. |
| **write / read / forget** | Agents distill experience mid-loop; later sessions underspecified without prior memory. Finding: near-saturated LoCoMo agents **fail** here; external memory/RAG not universally helpful. |
| **conflict** | Latent constraints from earlier sessions; preference conflicts in travel. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) Don’t declare win from LoCoMo/LongMemEval alone — need **action-coupled** fixtures. (2) Cross-session latent constraints ≈ workstream decisions that must survive handoff. (3) Process Score idea: grade intermediate memory use, not only final SR. (4) Dogfood: multi-session IDE tasks where later edit depends on earlier sealed decision. |
| **metric_impact** | Interdependent multi-session SR + process score for S1→S7 loops. |
| **refine_candidate** | **yes** — multi-session interdependent fixture (≤1 of refine tickets) |

---

### 1.8 CaMeL — Capabilities for Machine Learning (prompt-injection by design)  
**arXiv:2503.18813** · Debenedetti, Shumailov, et al. (Google) · 2025 · **RE-READ** (P6 PDF FULL; this pass PDF 358k)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Prompt injection lets untrusted tool/memory data hijack **control flow** and exfiltrate. |
| **representation** | Dual-LLM pattern: trusted query → extract **control + data flows**; quarantined LLM consumes untrusted data under schema; **capabilities** (security sense) gate tool calls / unauthorized flows. AgentDojo: **77%** tasks with provable security vs **84%** undefended utility. |
| **write / read / forget** | Memory/tool results are **data plane**, never control plane. |
| **conflict** | Security vs utility / user-fatigue on declassification. |
| **privacy** | Capability policies prevent private data over unauthorized sinks. |
| **Kedger lessons** | (1) Hydrated Anchors cannot authorize `send`/`push` — need purpose-bound capability. (2) Hook adapters: trusted user/IDE intent owns control flow; ingest payload is untrusted data. (3) Quarantined schema extract ≈ cognify JSON without free-prose secret echo. (4) Align with Kedger `explicit_only` share + Inv-Scope. |
| **metric_impact** | S6: injection+memory→tool exfil deny rate (AgentDojo-style). |
| **refine_candidate** | no (design lock already; ConfAIde owns S6 metric ticket) |

---

### 1.9 FLEX — Forward Learning from Experience (semantic gating)  
**arXiv:2511.06449** · Cai, Guo, Pei, et al. · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | Frozen agents can’t grow; gradient fine-tune is costly / closed-source / catastrophic-forgetting. |
| **representation** | Actor \(\pi\) + updater \(\mu\) + experience library \(\mathcal{E}\). Library: hierarchical (strategy / pattern / instance) × **golden zone** (success) + **warning zone** (failure diagnostics). |
| **write / read / forget** | Updater: identical→discard; **semantically similar→selective merge** (keep higher-quality); else insert by granularity. Retrieve: hierarchical top-\(k\) (**\(k=5\)** typical), contextual not pure cosine. |
| **conflict** | Selective merge is soft conflict resolve — no audit SUPERSEDES. |
| **privacy** | Silent; library inheritance across agents is a share surface. |
| **Kedger lessons** | (1) Cognify merge gate: semantic-sim → merge vs new Evidence (threshold tunable; start with Nemori-like \(\tau\approx0.7\)). (2) Keep **warning zone** = failure Anchors. (3) Sealed pack inheritance ≈ experience inheritance — but capability-gated. (4) Do not silent-merge sealed eng constraints; map merge→propose SUPERSEDES. |
| **metric_impact** | Cognify: duplicate-rate ↓ + warning-zone recall on retry tasks. |
| **refine_candidate** | no (informs S3 merge policy; HaluMem/LME-V2 tickets first) |

---

### 1.10 MemoryAgentBench — AR / TTL / LRU / SF  
**arXiv:2507.05257** · Hu, Wang, McAuley · 2025/26 · **RE-READ** (Batch2 / P2 FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S2, S3, S4, S7 |
| **problem** | Long-context QA ≠ incremental memory; no prior bench covers all four competencies. |
| **representation** | Competencies: **AR** (Accurate Retrieval), **TTL** (Test-Time Learning), **LRU** (Long-Range Understanding ≥100k), **SF** (Selective Forgetting via FactConsolidation). Protocol: stream chunks as turns; absorb; then QA. Chunk **512** for SH/MH-Doc, LME(S*), FactConsolidation; **4096** for other / Mem0/Zep/MIRIX cost path. SF: facts by serial; **newer = larger serial**. |
| **write / read / forget** | Agents under test; SF mandates newest-wins conflict resolve. |
| **conflict** | FactConsolidation SH/MH from MQUAKE counterfactuals — primary SF slice. |
| **privacy** | Silent. |
| **Kedger lessons (fixture map)** | | Competency | Kedger fixture | |
| |---|---|---|
| | AR | needle/fact retrieve after incremental `ingest` |
| | TTL | absorb playbook/demo → apply on new task (procedural Anchor) |
| | LRU | ≥100k L0 stream → cognify → hydrate summary QA |
| | SF | ordered edit pairs → SUPERSEDES → answer on final state |
| **metric_impact** | Master eval matrix AR/TTL/LRU/SF for Kedger. |
| **refine_candidate** | **yes** — AR/TTL/LRU/SF fixture mapping ticket |

---

### 1.11 LoCoMo — Very long-term conversational memory  
**arXiv:2402.17753** · Maharana et al. · 2024 · **RE-READ** (Batch2 FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S5, S7, S8 |
| **problem** | Prior dialogue memory evals too short (~≤5 sessions). |
| **representation** | Personas + **temporal event graphs**; ~300 turns, ~19 sessions, ~9k tokens, up to **35** sessions. QA types: single-hop, multi-hop, **temporal**, open-domain, **adversarial** (unanswerable). Also event summarization + multimodal. |
| **write / read / forget** | Generative agents use STM/LTM; consumers bring own store. |
| **conflict** | Adversarial probes refusal; causal event change over time. |
| **privacy** | Life-fact personas — hygiene for local copies. |
| **Kedger lessons** | (1) Temporal fixtures: timestamped eng events with month-scale gaps. (2) Adversarial/unanswerable → abstain (pair with LongMemEval ABS). (3) Event-graph gold ≈ Evidence chain for `why`. (4) Regression for multi-hop hydrate — not eng-judgment gold alone. |
| **metric_impact** | Temporal + adversarial slices in S7/S8. |
| **refine_candidate** | no (covered under LongMemEval abstention + MAB) |

---

### 1.12 LongMemEval — Five abilities incl. abstention  
**arXiv:2410.10813** · Wu et al. · 2024/25 · **RE-READ** (P2/P5 / Batch2 eval)

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S7, S8 |
| **problem** | Chat assistants fail sustained multi-session memory (~30% drop claimed). |
| **representation** | **500** questions; abilities: information extraction, multi-session reasoning, **temporal reasoning**, **knowledge updates**, **abstention**. Indexing / retrieval / reading design study (session decomposition, fact-augmented keys, time-aware query expansion). |
| **write / read / forget** | Online parse of sessions; knowledge-update questions require preferring new facts. |
| **conflict** | Knowledge updates = soft SF. |
| **privacy** | Silent. |
| **Kedger lessons** | (1) **Abstention** metric: if Evidence absent → `I don't know` / empty hydrate, never invent Anchor. (2) Knowledge-update fixtures share DNA with SUPERSEDES. (3) Time-aware query expansion for hydrate. (4) S8 `why` must refuse fabricated provenance. |
| **metric_impact** | ABS accuracy + knowledge-update accuracy for S7/S8. |
| **refine_candidate** | **yes** — abstention / no-invent metric |

---

### 1.13 PrefEval — Preference following in long context  
**arXiv:2502.09597** · Zhao et al. · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S4, S7 |
| **problem** | LLMs fail to infer/memorize/adhere to user preferences over long multi-session chat. |
| **representation** | **3,000** preference–query pairs; **20** topics; explicit + implicit forms; generation + classification; contexts up to **100k**. Finding: zero-shot preference accuracy **<10%** by ~10 turns (~3k tokens) for most models; RAG/prompting still degrade. |
| **write / read / forget** | Preference memory must persist and apply; dynamic preference changes tested. |
| **conflict** | Dynamic preference following = update old prefs. |
| **privacy** | Preferences can be sensitive — share gating applies. |
| **Kedger lessons** | (1) Persona/preference Anchors need **always-on hydrate channel** (don’t rely on similarity alone). (2) Dynamic pref change → SUPERSEDES. (3) Eng analog: coding-style / reject-list constraints must survive 10+ sessions. |
| **metric_impact** | Preference-adherence @ N sessions for constraint Anchors. |
| **refine_candidate** | no |

---

### 1.14 Fides — IFC for AI agent planners  
**arXiv:2505.23643** · Costa, Köpf, et al. · 2025 · **RE-READ** (Batch2/P6 FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Planner design determines information flow; need deterministic IFC vs probabilistic PIA defenses. |
| **representation** | Labels: confidentiality × integrity lattice; dynamic tracking; policy engine; selective hide/reveal; quarantined LLM + constrained decoding. Goals: **integrity noninterference** (PIA ↛ consequential actions); **explicit secrecy** for confidentiality. |
| **write / read / forget** | Selective variable introduction to limit label inflation. |
| **conflict** | Policy deny vs utility. |
| **privacy** | First-class IFC — closest formal twin to Kedger capabilities / Inv-Scope. |
| **Kedger lessons** | (1) Label every hydrated row; pack plaintext = join of included labels. (2) Deny external tools when conf too high / integrity too low. (3) Document Kedger guarantee: explicit secrecy + integrity NI on share. |
| **metric_impact** | Label-join + deny tests on seal/hydrate. |
| **refine_candidate** | no |

---

### 1.15 AgentLeak — Internal-channel privacy leakage  
**arXiv:2602.11510** · El Yagoubi et al. · 2026 · **RE-READ** (P6/SHAREABLE FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S5, S6, S7 |
| **problem** | Multi-agent systems leak via **internal channels** (messages, shared memory, tool args) that output-only audits miss. |
| **representation** | **7** leakage pathways; 1,000 scenarios (healthcare/finance/legal/corporate); 4,979 traces; five production LLMs. Multi-agent can **reduce** final-output leakage (C1 27.2% vs 43.2% single-agent) while shifting risk into shared memory/messages. |
| **write / read / forget** | Shared memory is a leak sink; need least-privilege per agent. |
| **conflict** | Security–utility tradeoff analyzed. |
| **privacy** | Core contribution — channel taxonomy. |
| **Kedger lessons** | (1) Audit **pack contents + hydrate inject + hook stdout**, not only final chat. (2) Workstream shared memory needs attenuated facets (no ambient search). (3) Tool-arg exfil tests for grant/share. |
| **metric_impact** | Internal-channel leak rate for S6. |
| **refine_candidate** | no (ConfAIde ticket covers generation; AgentLeak informs channels) |

---

### 1.16 MemLeak — Deletion residual / multimodal forget failures  
**arXiv:2606.29788** · Wang, Zhang · 2026 · **RE-READ** (P6 FULL)

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S5, S6, S8 |
| **problem** | “Forget” that deletes text still leaves facts recoverable from correlated text/images. |
| **representation** | **Information Provenance Graph (IPG)** by deletion affordance. MemLeak: 113 profiles × 20 facts; cascade: direct probe <1%, correlated text **18.3%**, images **12.0%** (47% of image leaks not text-recoverable); semantic deletion → image residual **2.0%**. |
| **write / read / forget** | Fact-level erasure ≠ record delete; need provenance-aware semantic deletion. |
| **conflict** | Linked nodes retain forgotten facts. |
| **privacy** | Forgetting residual = privacy failure. |
| **Kedger lessons** | (1) `kedger forget` must SUPERSEDES **and** scrub linked Evidence / artifacts, not only Anchor row. (2) S8 `why` after forget must not resurrect deleted fact via neighbors. (3) Measure deletion residual probes post-forget. |
| **metric_impact** | Post-forget recoverability (text + linked Evidence) for SF/privacy. |
| **refine_candidate** | no (pairs with MAB SF fixture) |

---

## 2. Cross-cutting Kedger stage map

| Stage | Load-bearing papers | Metric idea |
|-------|---------------------|------------|
| S1 hooks | MemoryArena, RealMem, CaMeL | Incremental absorb; untrusted ingest data plane |
| S2 working | MemBench, PrefEval, Memento 2 | Working prefs/constraints always available |
| S3 cognify | FLEX, HaluMem, LME-V2, Memento 2 | Op-level extract; selective merge; gotchas/workflows |
| S4 promote | ConfAIde, HaluMem, PrefEval, MemLeak | No auto-share; update correctness; forget residual |
| S5 graph | LME-V2, MemLeak, AgentLeak, MemBench | Provenance links; shared-memory topology |
| S6 seal | ConfAIde, CaMeL, Fides, AgentLeak | Generation probes; capability IFC; channel audits |
| S7 hydrate | MemoryAgentBench, LME-V2, MemoryArena, LoCoMo | AR/TTL/LRU/SF; evidence budget; action-coupled |
| S8 why | LongMemEval ABS, ConfAIde, MemLeak, Memento 2 | Abstain; no private narration; failure provenance |

---

## 3. Refine tickets

≤3 concrete bullets tied to metrics:

1. **AR/TTL/LRU/SF fixture matrix (MemoryAgentBench)** — Add Kedger integration tests that stream chunked L0 (512-token fact / 4096 narrative), then score: AR exact/substring, TTL playbook apply, LRU ≥100k cognify→QA, SF FactConsolidation-style ordered edits with SUPERSEDES newest-wins.  
2. **Operation-level hallucination + abstention (HaluMem ∪ LongMemEval)** — After each cognify session, score extract F1 / update consistency / QA faithfulness / FMR; add ABS cases where `hydrate`/`why` must abstain (no invented Anchors).  
3. **S6 seal generation probes + multi-session interdependence (ConfAIde Tier-4 ∪ MemoryArena)** — On `handoff`/`share`, measure free-form private leak vs public-decision retention; add a 2–3 session dogfood fixture where session \(n+1\) is underspecified unless sealed decisions from session \(n\) hydrate correctly (process score, not only final SR).

---

## 4. Ledger IDs (summary)

| ID | Title | Status |
|----|-------|--------|
| 2512.22716 | Memento 2 | FULL |
| 2605.12493 | LongMemEval-V2 | FULL |
| 2602.16313 | MemoryArena | FULL |
| 2511.06449 | FLEX | FULL |
| 2502.09597 | PrefEval | FULL |
| 2310.17884 | ConfAIde | RE-READ |
| 2506.21605 | MemBench | RE-READ |
| 2511.03506 | HaluMem | RE-READ |
| 2601.06966 | RealMem | RE-READ |
| 2503.18813 | CaMeL | RE-READ |
| 2507.05257 | MemoryAgentBench | RE-READ |
| 2402.17753 | LoCoMo | RE-READ |
| 2410.10813 | LongMemEval | RE-READ |
| 2505.23643 | Fides | RE-READ |
| 2602.11510 | AgentLeak | RE-READ |
| 2606.29788 | MemLeak | RE-READ |

**Successfully FULL/RE-READ IDs (16):**  
`2512.22716`, `2605.12493`, `2602.16313`, `2511.06449`, `2502.09597`, `2310.17884`, `2506.21605`, `2511.03506`, `2601.06966`, `2503.18813`, `2507.05257`, `2402.17753`, `2410.10813`, `2505.23643`, `2602.11510`, `2606.29788`
