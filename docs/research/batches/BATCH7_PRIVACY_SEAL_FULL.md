# Batch 7 — Privacy · Capability Security · Share Leakage · Sealed Handoff (Kedger)

> **Date:** 2026-08-08  
> **Branch:** `Cursor/batch7-privacy-hydrate-fb37`  
> **Scope:** Tier-5 runway — **privacy / CI**, **capability & privilege control**, **memory/RAG leakage**, **prompt-injection → memory**, **sealed / verifiable handoff**. Papers **not** already FULL in `CORPUS_INVENTORY.md` §2 arXiv ledger or Batch4/Batch5/Batch6.  
> **Avoid re-read:** ConfAIde, CaMeL, Fides, AgentLeak, MemLeak, MAMA (already FULL elsewhere).  
> **Method:** Full arXiv HTML (ar5iv fallback) or PDF→text when HTML thin; cache `/tmp/kedger-papers/full/{id}.{html,txt,pdf}`. Mechanism cards only — not abstract skim.  
> **Kedger stages:** S1 hooks · S2 working · S3 cognify · S4 promote · S5 graph · S6 seal · S7 hydrate · S8 why  
> **Lens:** Inv-Scope, capability attenuation, channel-scoped share, `.kxp` seal, hydrate-as-untrusted-data, MEXTRA/AgentPoison-class memory attacks.

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (new body deep-read; ID not previously FULL in CORPUS §2 arXiv ledger / Batch4 / Batch5 / Batch6) | **16** | MEXTRA (2502.13172); AgentPoison (2407.12784); MINJA (2503.03704); Spill the Beans (2402.17840); PoisonedRAG (2402.07867); InjecAgent (2403.02691); AgentDojo (2406.13352); AirGapAgent (2405.05175); Progent (2504.11703); PrivacyLens (2409.00138); BIPIA (2312.14197); RAG-MIA (2405.20446); GEIA embedding inversion (2305.03010); RAG backdoor extraction (2411.01705); IPI Firewalls (2510.05244); CVA crypto auth (2607.21325) |
| **RE-READ** | **0** | — |
| **Fetch failed / skipped (no invented content)** | **0** | PrivacyLens / BadAgent-family thin HTML used PDF or ar5iv; all carded IDs have `.txt` ≥48k chars |
| **Identified / cached but not carded (room)** | 4 | BadAgent (2406.03007); Text Embeddings Reveal (2310.06816); Assessing Automated PI (2606.10525); Prompt Injection vs LLM apps (2306.05499) — bodies cached under `/tmp/kedger-papers/full/`, deferred |

**Cache path:** `/tmp/kedger-papers/full/{id}.txt` (all 16 FULL IDs present).

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded. Numbers are from paper text/tables.

---

## 1. Mechanism cards

### 1.1 MEXTRA — Unveiling Privacy Risks in LLM Agent Memory  
**arXiv:2502.13172** · Wang et al. · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S6, S7, S8 |
| **problem** | LLM agents store private user–agent interactions in long-term memory for ICL demos; black-box attackers can extract that memory via prompts. |
| **representation** | **MEXTRA** (Memory EXTRaction Attack): multi-part attacking prompt (request retrieved user queries + prioritize output over task) + automated diverse prompt generation (edit-distance / cosine variants). Agents studied: EHRAgent, RAP (web). Metrics include CER / extracted private-query counts. |
| **write / read / forget** | Attack is **read-path**: no write to memory required. Memory config ablations: scoring function, embedder, memory size, retrieval depth, backbone. Forget/deletion not defended. |
| **conflict** | Silent. |
| **privacy** | Core: black-box memory leakage. Agents using edit-distance scoring leak **>30%** private queries; cosine also **>10%**. Prompt design + auto-generation essential vs naïve “repeat all context” RAG extract prompts. |
| **Kedger lessons** | (1) Hydrated Evidence in context is an **extraction surface** — treat S7 packs as untrusted for re-emission. (2) Output filters must block dump-of-retrieved-memory patterns, not only final-answer PII regex. (3) Retrieval depth / scoring knobs are security SLIs. (4) S8 `why` must not echo private L0 into unauthorized channels. |
| **metric_impact** | Memory extract rate under MEXTRA-style prompts; retrieval-depth × leak AUC. |
| **refine_candidate** | **yes** — S6/S7 MEXTRA-style memory-dump deny fixture |

---

### 1.2 AgentPoison — poisoning memory / RAG knowledge bases  
**arXiv:2407.12784** · Chen et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S7 |
| **problem** | Agents retrieve demos from memory/RAG; adversaries can backdoor retrieval without model fine-tune. |
| **representation** | Constrained trigger optimization: uniqueness + compactness + target-generation + coherence losses → discrete trigger maps triggered queries into a compact embedding region so poisoned demos retrieve with high probability. No training of victim LLM. |
| **write / read / forget** | **Write** = inject few poisoned instances into memory/KB (**poison rate <0.1%**). **Read** = retrieval under triggered user instruction. Forget = not studied. |
| **conflict** | Silent (integrity via backdoor, not SUPERSEDES). |
| **privacy** | Indirect: compromised demos can force harmful tool/actions; transfer across embedders incl. OpenAI-ADA. Avg **ASR ≥80%**, benign drop **≤1%**; paper cites ~**82%** retrieval / **~63%** end-to-end ASR in comparisons. |
| **Kedger lessons** | (1) Cognify/promote must **provenance-gate** writes into shared memory (untrusted session → never ambient `repo_shared_safe`). (2) Hydrate should prefer signed/capability-scoped Evidence, not pure embedding nearest-neighbor. (3) Fixture: inject poisoned Anchor + trigger query → measure retrieve rate. (4) Compactness of trigger cluster ≈ anomaly signal for S3 write audits. |
| **metric_impact** | Poison retrieve ASR @ poison rate; benign ACC delta. |
| **refine_candidate** | **yes** — S3/S4 provenance-gated promote vs AgentPoison retrieve |

---

### 1.3 MINJA — query-only memory injection  
**arXiv:2503.03704** · Dong et al. · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S3, S4, S7 |
| **problem** | Prior poisoning assumes direct memory write; realistic attacker only chats with the agent. |
| **representation** | **MINJA:** design malicious records with **bridging steps** linking victim query \(a_v\) to target malicious reasoning \(R_{a_t}\); inject via **indication prompts** + **Progressive Shortening Strategy (PSS)** that gradually removes the indication so later victim queries retrieve the injected record. |
| **write / read / forget** | Write = agent autonomously stores interaction traces including injected bridges. Avg **ISR 98.2%**, **ASR 76.8%** across EHR/QA/webshop settings. |
| **conflict** | Silent. |
| **privacy** | Integrity/exfil via memory; no ACL model. |
| **Kedger lessons** | (1) Capture hooks must flag **self-referential / bridging** traces before cognify. (2) Do not auto-promote every successful tool trajectory into L3. (3) Progressive shortening ≈ multi-turn persistence — measure leak/poison over rounds (aligns MAMA). (4) Indication-prompt patterns are S1 redaction/deny candidates. |
| **metric_impact** | Injection success over PSS rounds; post-injection hydrate ASR. |
| **refine_candidate** | **yes** — S1/S3 progressive-injection persistence probe |

---

### 1.4 Spill the Beans — RAG datastore extraction via instruction following  
**arXiv:2402.17840** · Qi et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Retrieval-in-context RAG with instruction-tuned LMs regurgitates datastore text under prompt injection. |
| **representation** | Black-box extract prompts against open LMs (Llama2/Mistral/Vicuna/…); production attack on custom GPTs. Mitigations: safety-aware prompts, **position bias elimination (PINE)**, combined. |
| **write / read / forget** | Read-only extract. GPTs: **100%** datastore-leak success on 25 custom GPTs ≤2 queries; **41%** verbatim from 77k-word book and **3%** from 1.57M-word Wiki corpus with 100 self-generated queries. |
| **conflict** | Silent. |
| **privacy** | Datastore leakage scales with model size / instruction-following; context utilization failure enables regurgitate. |
| **Kedger lessons** | (1) Sealed hydrate packs must not become “repeat your context” oracles. (2) Prefer **structured Evidence fields** over dumping raw L0 into prompts. (3) Position/reorder defenses matter for S7 packing. (4) Production GPTs lesson → treat third-party reader models as hostile extractors. |
| **metric_impact** | Verbatim extract ROUGE/F1 under inject prompts; PINE on/off. |
| **refine_candidate** | no (MEXTRA fixture covers dump class; PINE informs LongLLMLingua path) |

---

### 1.5 PoisonedRAG — knowledge corruption of RAG databases  
**arXiv:2402.07867** · Zou et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S4, S5, S7 |
| **problem** | Inject few malicious texts → LLM answers attacker-chosen targets for attacker-chosen questions. |
| **representation** | Split malicious text into **I** (generation/influence) + **S** (retrieval/semantic). Black-box vs white-box crafting. Defenses tried: paraphrasing, perplexity, duplicate filter, knowledge expansion — insufficient. |
| **write / read / forget** | Write = inject **5** poisoned texts/question into millions-scale DB → up to **~90–97% ASR** (NQ black-box). |
| **conflict** | Integrity attack (forced wrong answer), not typed SUPERSEDES. |
| **privacy** | Silent on membership; focuses corruption. |
| **Kedger lessons** | (1) Shared Anchor index is a **poison surface** — capability on write ≠ embedding similarity. (2) Near-dup filters alone won't stop semantic poisons (paper: duplicate filter weak). (3) Compose/hydrate: require multi-source agreement or ConflictSet before high-stakes answers. (4) Promotion quorum / human gate for `repo_shared_safe`. |
| **metric_impact** | Target-answer ASR @ poison count; defense residual ASR. |
| **refine_candidate** | no (AgentPoison ticket owns memory-poison SLI) |

---

### 1.6 InjecAgent — IPI benchmark for tool agents  
**arXiv:2403.02691** · Zhan et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Tool-integrated agents process external content that can carry malicious instructions. |
| **representation** | **1,054** cases; **17** user tools × **62** attacker tools; intents: **direct harm** vs **data exfiltration**. Base vs “hacking prompt” enhanced setting. |
| **write / read / forget** | Eval harness; ReAct GPT-4 **~24%** ASR base → **~47%** enhanced; fine-tuned agents lower (GPT-4 FT ~3.8%). |
| **conflict** | Silent. |
| **privacy** | Exfil category is first-class; financial/harm categories separate. |
| **Kedger lessons** | (1) Tool results / web / email Evidence = **untrusted instruction channel**. (2) S6 seal metrics should include InjecAgent-style **exfil** cases, not only ACL tags. (3) Content-freedom placeholders ↑ vulnerability — constrain schema of tool returns before hydrate. |
| **metric_impact** | ASR-valid on harm vs exfil suites under Kedger tool firewall. |
| **refine_candidate** | no (AgentDojo + firewalls tickets preferred) |

---

### 1.7 AgentDojo — dynamic PI attack/defense environment  
**arXiv:2406.13352** · Debenedetti et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Static PI benches miss multi-tool stateful agents; need live tasks + adaptive attacks/defenses. |
| **representation** | Extensible env: **97** user tasks, **629** security cases; domains workspace / banking / travel / slack. Tools mutate state; injections in tool outputs. Reports utility + targeted ASR. Defenses: repeat user prompt, tool filter, delimiters, etc. |
| **write / read / forget** | Eval framework; SOTA models fail many benign tasks; attacks break some but not all properties. |
| **conflict** | Silent. |
| **privacy** | Injection tasks include email/data exfil goals. |
| **Kedger lessons** | (1) Kedger PART D / seal probes should be **stateful tool suites**, not single-shot prompts. (2) Utility-under-attack is a required SLI (CaMeL/Progent already cite AgentDojo). (3) Tool isolation ≠ enough alone — paper notes strengths/limits. (4) Prefer extensible fixture harness over frozen ASR number. |
| **metric_impact** | Utility + ASR on AgentDojo-like eng handoff tasks. |
| **refine_candidate** | **yes** — S6 AgentDojo-style utility×ASR seal harness |

---

### 1.8 AirGapAgent — CI minimization + context isolation  
**arXiv:2405.05175** · Bagdasarian et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S2, S4, S6, S7 |
| **problem** | Privacy-conscious conversational agents must share only task-necessary data; **context hijacking** collapses baseline protection. |
| **representation** | Grounded in **Contextual Integrity**. Baseline agent with full user profile in context fails under hijack (**94%→45%** protection on Gemini Ultra). **AirGapAgent:** (1) **minimization with base context** — only task-needed fields; (2) **context isolation** — separate privileged profile from third-party-facing dialogue. Achieves **~97%** protection under same attack. |
| **write / read / forget** | Read path minimization; synthetic user/context profiles for eval. |
| **conflict** | Silent. |
| **privacy** | Core CI: appropriateness of flow given domain/scenario/directive. Hijack = attacker reframes task to solicit out-of-scope fields. |
| **Kedger lessons** | (1) Hydrate packs must be **purpose-minimized** per recipient capability — not full Anchor dump. (2) Isolate `workstream_private` profile store from third-party tool/channel context (air gap). (3) Promote gates encode privacy **directives**, not only shareable bool. (4) ConfAIde-adjacent but agent-action focused — complements Tier-4 generation probes. |
| **metric_impact** | Field-level overshare rate under hijack prompts; minimize-on vs full-profile. |
| **refine_candidate** | **yes** — S6/S7 purpose-minimized hydrate (AirGap) |

---

### 1.9 Progent — privilege control for AI agents  
**arXiv:2504.11703** · 2025/26 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6 |
| **problem** | Non-deterministic agents + context-dependent security needs; hard to keep least privilege without killing utility. |
| **representation** | Privilege as **domain-specific policy** (effect, conditions, fallback); LLM proposes policy; **SMT** compares expansions; deterministic allow/narrow with human/approver gate for expansion. Modular library/proxy integration; MCP / multi-agent demos. |
| **write / read / forget** | Runtime mediates every tool call. AgentDojo: ASR **39.9%→1.0%**; ASB **70.3%→3.9%**; utility maintained. Manual policies → **0%** ASR. |
| **conflict** | Silent on belief conflict; privilege conflict via deny/fallback. |
| **privacy** | Least-privilege tool args reduce PII exfil; not a CI vignette suite. |
| **Kedger lessons** | (1) Map Kedger Capabilities → Progent-style **effect+conditions** on tool side-effects (`git push`, `send_email`, pack export). (2) LLM-suggested policy OK; **expansion** must be deterministic/approver-gated (no silent privilege growth from injected text). (3) Seal open / hydrate read are privilege effects, not ambient. (4) Complements CaMeL control/data flow split. |
| **metric_impact** | Tool ASR vs utility under privilege policies; expansion-attempt deny rate. |
| **refine_candidate** | **yes** — S6 privilege-policy gate on consequential tools |

---

### 1.10 PrivacyLens — privacy norms → agent trajectories  
**arXiv:2409.00138** · Shao et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S4, S6, S8 |
| **problem** | Probing questions overestimate privacy awareness vs **actions** in agent trajectories. |
| **representation** | Seeds (CI-grounded norms) → expressive **vignettes** → **agent trajectories** (tool-using). Multi-level leak eval. GPT-4 / Llama-3-70B still leak in **25.68%** / **38.69%** of cases even with privacy-enhancing instructions. Dynamic multi-trajectory red-team per seed. |
| **write / read / forget** | Eval; unintentional leakage without attacker. |
| **conflict** | Helpfulness vs privacy norms. |
| **privacy** | CI appropriateness in LM-mediated communication (email/social posts). |
| **Kedger lessons** | (1) Measure **action leaks** (what gets into outbound email/handoff), not quiz accuracy. (2) S4 promote + S6 seal fixtures = vignette→trajectory. (3) Privacy-enhancing system prompts insufficient alone. (4) S8 `why` narration can itself violate norms — scope `why` by recipient. |
| **metric_impact** | Action-leak rate on PrivacyLens-style eng vignettes. |
| **refine_candidate** | no (AirGap + ConfAIde probes cover; use vignettes as data later) |

---

### 1.11 BIPIA — benchmark + defenses for indirect PI  
**arXiv:2312.14197** · Yi et al. · 2023/25 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | External content carries actionable instructions; LLMs fail to separate info vs instructions. |
| **representation** | **BIPIA** dataset: 5 application scenarios, **250** attacker goals; position of attack in content varied. Black-box defenses (boundary awareness / etc.) + white-box defense; claim near-zero ASR with quality preserved (white-box). **25** LLMs universally vulnerable to varying degrees. |
| **write / read / forget** | Eval + defense methods at model/app boundary. |
| **conflict** | Silent. |
| **privacy** | Malicious instructions can induce unsafe downloads / misaligned outputs; privacy among harm types. |
| **Kedger lessons** | (1) Explicit **boundary tokens / awareness** between Evidence text and control plane. (2) Position of injection in tool payload matters for packing. (3) Black-box defenses alone incomplete — prefer structural privilege (Progent/CaMeL) over prompt-only. |
| **metric_impact** | BIPIA ASR residual under Kedger delimit+privilege. |
| **refine_candidate** | no |

---

### 1.12 RAG membership inference  
**arXiv:2405.20446** · Anderson, Amit, Goldsteen · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6, S7 |
| **problem** | Attacker infers whether a passage is in the RAG DB from outputs alone. |
| **representation** | Black/gray-box prompt crafting for yes/no membership; medical QA + email domains; template-instruction defense helps some models. |
| **write / read / forget** | Read-only MIA; no need to extract full text. |
| **conflict** | Silent. |
| **privacy** | Membership of sensitive docs is itself sensitive; defense via RAG template instructions partial. |
| **Kedger lessons** | (1) Inv-Scope **404** (not 403) + non-answer templates reduce membership oracles (aligns MemClaw/MRMMIA). (2) Pack metadata / `why` existence bits are MIA channels. (3) Rate-limit id/probe queries on hydrate APIs. |
| **metric_impact** | MIA AUC on shared vs private indexes; 404 vs 403 ablation. |
| **refine_candidate** | no (MRMMIA/P6 already drove 404; keep as supporting) |

---

### 1.13 GEIA — generative sentence embedding inversion  
**arXiv:2305.03010** · Li, Xu, Song · 2023 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S6 |
| **problem** | Sentence embeddings leak reconstructable text — more than attribute inference alone. |
| **representation** | **GEIA:** treat embedding as initial token reps; train/finetune decoder to regenerate full sentence from black-box embedder outputs. Outperforms prior classification-style inversion; produces coherent reconstructions. |
| **write / read / forget** | Attack on stored vectors; no LLM agent loop required. |
| **conflict** | Silent. |
| **privacy** | Vector indexes of private Evidence are **ciphertext-adjacent plaintext** to inversion adversaries with decoder access / stolen embeddings. |
| **Kedger lessons** | (1) Do not treat embedding store as privacy boundary — partition by visibility **before** embed, or encrypt-at-rest without searchable semantics (SSE lesson). (2) Shared ANN indexes must not mix `workstream_private` with `repo_shared_safe`. (3) Unshare must tombstone **vectors**, not only SQL rows (MemLeak cascade). |
| **metric_impact** | Reconstruction ROUGE from stolen private embeddings; partition isolation tests. |
| **refine_candidate** | **yes** — S6 embedding-store isolation / tombstone cascade |

---

### 1.14 RAG backdoor data extraction  
**arXiv:2411.01705** · Peng et al. · 2024 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S3, S6, S7 |
| **problem** | Prompt-injection extract fails on weakly instruction-following / fine-tuned models; supply-chain backdoor restores extractability. |
| **representation** | Poison fine-tune set (**~5%**) to install backdoor; triggers enable **verbatim** (avg **94.1%** ASR, ROUGE-L **82.1** on Gemma-2B-IT) or **paraphrased** extraction (**63.6%** ASR). Prior PI extracts **<1%** on same model. |
| **write / read / forget** | Write = poison during fine-tune; read = triggered extract at inference. |
| **conflict** | Silent. |
| **privacy** | Stealthier paraphrased extract harder to detect than verbatim dump. |
| **Kedger lessons** | (1) Kedger should not fine-tune reader models on untrusted corpora that include pack plaintext. (2) Assume extract attacks evolve beyond instruction-following — structural deny (firewall/privilege) still required. (3) Paraphrase exfil ⇒ semantic canaries in sealed packs, not only string match. |
| **metric_impact** | Triggered extract ASR; canary detection rate on paraphrase. |
| **refine_candidate** | no |

---

### 1.15 IPI Firewalls — Minimizer + Sanitizer at tool boundary  
**arXiv:2510.05244** · Bhagwatkar et al. · 2025 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S1, S6, S7 |
| **problem** | Complex PI defenses (custom interpreters) heavy; benches may be weak/saturated. |
| **representation** | Two modular firewalls: **Tool-Input Firewall (Minimizer)** + **Tool-Output Firewall (Sanitizer)**. Claims **~0% ASR** with high utility on AgentDojo, ASB, InjecAgent, τ-Bench; SOTA security–utility vs prior incl. CaMeL numbers. Also documents **benchmark flaws** and residual bypasses under stronger attacks. |
| **write / read / forget** | Defense at agent–tool interface; no retraining. |
| **conflict** | Silent. |
| **privacy** | Minimizer strips unnecessary PII from tool args; Sanitizer strips injected instructions from tool outputs. |
| **Kedger lessons** | (1) Ship **minimize+sanitize** at tool boundary as default S1/S6 layer (cheap, model-agnostic). (2) Do not declare victory from saturated benches — keep adaptive attacks in harness. (3) Complements Progent privilege (args) + CaMeL (control/data). (4) Hydrate Evidence through Sanitizer before it re-enters planner context. |
| **metric_impact** | ASR/utility with firewalls on/off; adaptive-bypass residual. |
| **refine_candidate** | **yes** — S1 tool-output Sanitizer + input Minimizer |

---

### 1.16 CVA — cryptographically verifiable agent authorization  
**arXiv:2607.21325** · Llambí-Morillas & Fernández-Fernández · 2026 · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | S6 |
| **problem** | Identity + delegation ≠ proof that a **concrete** agent request satisfied policy in a **specific** execution context. |
| **representation** | Hypothesis **H1**: relation \(R_{CVA}(x,w)\) binds principal, authorization request, execution context, and policy satisfaction with ZK-style private witness. Candidate properties: authorization soundness, principal binding, request binding, replay resistance; notes authz binding ≠ execution binding. PoC under proof-system assumptions (e.g. Groth16). |
| **write / read / forget** | Authz layer; not a memory store. |
| **conflict** | Silent. |
| **privacy** | Selective disclosure of private authz attributes via ZK witness. |
| **Kedger lessons** | (1) Sealed `.kxp` handoff should evolve toward **request-bound** capabilities (who + what + context + epoch), not only recipient key IDs. (2) Replay resistance ↔ pack epoch / nonce (aligns MLS epoch thinking). (3) Early: sign canonical pack header (already StE); later: attach CVA-style proofs for CI/tool gates. (4) Treat as research hypothesis — do not block v1 on ZK. |
| **metric_impact** | Pack replay / wrong-context open deny rate; header binding tests. |
| **refine_candidate** | no (design input for Phase F+; not immediate fixture) |

---

## 2. Cross-cutting map → Kedger stages

| Stage | Papers | Takeaway |
|-------|--------|----------|
| S1 hooks | MINJA, InjecAgent, AgentDojo, BIPIA, IPI Firewalls, Progent | Capture indication/bridging; minimize tool args; sanitize tool outputs |
| S2 working | AirGapAgent, MEXTRA | Purpose-minimized working context; don't hold full private profile |
| S3 cognify | AgentPoison, PoisonedRAG, MINJA, GEIA | Provenance-gate writes; partition embeds; don't auto-store bridges |
| S4 promote | AgentPoison, PoisonedRAG, AirGapAgent, PrivacyLens | Human/capability gate to shared; action-norm checks |
| S5 graph | PoisonedRAG | Multi-source / ConflictSet before trusting retrieved shared claims |
| S6 seal | MEXTRA, Spill Beans, AirGapAgent, Progent, PrivacyLens, RAG-MIA, GEIA, CVA, Firewalls | Channel-scoped packs; privilege; 404; vector tombstones; request-bound caps |
| S7 hydrate | MEXTRA, AgentPoison, Spill Beans, Firewalls, AirGap | Untrusted data plane; sanitized Evidence; minimized fields |
| S8 why | PrivacyLens, MEXTRA | Scoped narration; no private dump in explanations |

---

## 3. Refine tickets (≤3)

1. **Tool Minimizer + Sanitizer at boundary (IPI Firewalls)** — Strip non-essential args on tool calls; sanitize tool/Evidence text before re-entering planner/hydrate. Metric: AgentDojo-style ASR→~0 with utility retained; adaptive bypass logged.  
2. **Purpose-minimized hydrate + privilege policies (AirGapAgent + Progent)** — Compile `.kxp` / live hydrate with only fields allowed by recipient capability + task purpose; consequential tools require effect+conditions policy (expansion approver-gated). Metric: field overshare under hijack; ASR **39.9%→≤1%** class on eng tool suite.  
3. **Memory dump / poison / embedding cascade (MEXTRA + AgentPoison + GEIA)** — Deny memory-regurgitation prompts; provenance-gate promote into shared indexes; unshare tombstones vectors+caches. Metric: MEXTRA extract rate; poison retrieve ASR @ <0.1% inject; post-unshare inversion residual.

---

## 4. Successfully FULL-read IDs

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
