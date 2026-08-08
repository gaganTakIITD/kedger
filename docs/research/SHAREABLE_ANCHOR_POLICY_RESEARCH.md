# Research Memo: Shareable-Anchor / Selective Disclosure Policy for MoDeX

> **Date:** 2026-08-08  
> **Scope:** When/how engineering judgments may be promoted from `workstream_private` → `repo_shared_safe` (`shareable=true`).  
> **Method:** Deep-read of primary papers/docs (arXiv HTML/PDF where available), not keyword skim.  
> **Audience:** MoDeX architecture lock for shareable-anchor policy.

---

## 1. Honesty about coverage

### Fully deep-read (full HTML/PDF body, mechanisms + failure modes)

| Source | Coverage |
|--------|----------|
| **MemClaw / Governed Shared Memory** (arXiv:2606.24535) | Full HTML — fleet-memory formalism, Inv-Scope, four failure modes, ArgusFleet results, GET-by-id gap, dedup/contradiction ordering |
| **AgentLeak** (arXiv:2602.11510v2) | Full HTML — 7 channels, C2/C5 internal leakage, data minimization formalization |
| **MAMA / Topology Matters** (ACL Findings 2026) | Full PDF text — Engram/Resonance, topology × centrality × leakage |
| **MemLeak** (arXiv:2606.29788) | Full HTML — deletion residual via correlated text/images, IPG |
| **PRISM** (arXiv:2605.10614) | Full PDF — propagation amplification across agent boundaries |
| **Capability Myths Demolished** (Miller, Yee, Shapiro) | Full PDF — Properties A/D, confused deputy, revocation via forwarders |
| **Spritely core + OcapPub proxying** | Full HTML / README — attenuation, caretaker/revoker facets |
| **RFC 2693 SPKI Certificate Theory** | Full RFC text — auth certs vs ACL, local names, delegation |
| **Generative Agents** (Park et al., arXiv:2304.03442) | Full arXiv HTML — importance scoring, reflection threshold, reflection trees |
| **MemGPT** (arXiv:2310.08560) | Full HTML — main/working vs archival/recall tiers |
| **RecMem** (arXiv:2605.16045) | Full HTML — subconscious → episodic → semantic via recurrence |
| **Collaborative Memory** (arXiv:2505.18279) | Full PDF — private/shared tiers, bipartite permission graphs, provenance |
| **VAULT** (eKNOW 2025) | Full PDF — KG_ONLY/CHUNKS/FULL/DOCUMENT_BASED tiers |
| **LightRAG issue #2373 + multi-tenant notes** | Issue + secondary course notes — workspace isolation gaps |
| **XACML4G / graph ACL papers** | Full ACM HTML + Springer extract — path-pattern ACLs on edges |
| **MoDeX docs** | `OPEN_SOURCE_MEMORY_ARCHITECTURE.md`, `WORKSTREAM_AND_PROMOTION_V1.md`, `MEMORY_SCHEMAS_V1.md` |
| **ADR / institutional memory** | AWS ADR guide PDF excerpts; ThoughtWorks-style ops essays; COMPEL handoff article |
| **Design rationale (QOC / DRed / Gruber)** | Full PDFs of Gruber KSL-92-59; Design Society capture lessons |

### Partial / secondary

| Source | Coverage |
|--------|----------|
| **Fides IFC** (arXiv:2505.23643) | **FULL** in `AGENT_MEMORY_CORPUS_DEEP_READ_BATCH2.md` (PDF); this memo originally abstract-only |
| **ConfAIde** (arXiv:2310.17884) | **FULL** in BATCH2; CI tiers + leakage results |
| **CaMeL / MEXTRA** | CaMeL (2503.18813) still stub; MEXTRA via MemClaw/AgentLeak citations |
| **GraphRAG official privacy paper** | No dedicated privacy paper found; relied on VAULT + multi-tenant architecture notes |
| **Patent US11120150 / US20260178391** | Patent abstracts + claims sections (not peer-reviewed theory) |
| **Letta docs** | Official docs on core vs archival (post-MemGPT productization) |

### Not found as standalone “personal vs shared schema” consolidation paper

RecMem and Generative Agents distinguish *tiers of abstraction*, not *personal vs shared schema*. Collaborative Memory is the closest peer-reviewed dual-tier private/shared model. MoDeX’s visibility classes are ahead of most agent-memory papers on this axis.

---

## 2. Per-source detailed insights

### A) Agent memory privacy / governed shared memory

**MemClaw (2606.24535)** formalizes fleet memory as \(M = (A, S, G, P, T)\): agents, substrate, governance, provenance, temporal supersession. Write = \((agent, content, scope, time, provenance)\); retrieval must satisfy **Inv-Scope**: no agent receives a row outside `auth(agent, G, scope)`. Four failure modes map cleanly to MoDeX:

1. **Unauthorized leakage** — semantic similarity ≠ entitlement. Live finding: tenant isolation held, but **GET-by-id ignored fleet/agent scope** (classic confused deputy: identity resolved then discarded). Remediation returned **404** (no existence disclosure), not 403.
2. **Stale propagation** — write-to-visible is part of the latency budget; strong mode paid consistency on write (~0.8s visibility).
3. **Contradiction persistence** — supersession works *only when both writes admit*; synchronous near-duplicate gate **starved** async contradiction detector (409 before supersedes_id).
4. **Provenance collapse** — depth-4 chains reconstructable with writer identity is the auditability floor.

Policy-governed propagation ≠ administrative redistribute: MemClaw conflated fleet-internal share with trust≥3 migration. **Lesson:** promotion and re-homing need distinct privilege surfaces. Retrieval pipeline must be: candidates → **policy filter on every path** → temporal resolve → provenance → rank. Partial filter on search only is insufficient.

**AgentLeak:** Internal channels dominate. Inter-agent messages (C2) leaked ~68.8% vs final output (C1) ~27.2%; shared memory (C5) ~46.7%. Output-only audits miss ~41.7% of violations. Formalizes **data minimization**: vault \(\mathcal{V}\), allowed set \(\mathcal{A}\); leak iff \(v \notin \mathcal{A}\) appears in any channel. **Lesson for MoDeX:** hydrating a shareable Anchor into an agent context, then that agent messaging peers / writing tools, is a distinct leakage surface—`repo_shared_safe` content must be treated as **channel-scoped**, not “safe once in store.”

**MAMA:** Leakage rises with density, short attacker–target distance, and target centrality; early rounds dominate then plateau. Prefer sparse/hierarchical topologies; restrict hubs. **Lesson:** don’t make every agent a hub that can retrieve all `repo_shared_safe` Anchors into every handoff; capability-gated packs already align with sparse topology.

**MemLeak:** “Delete” of text is not forget. Correlated retained text (~18%) and images (~12%) recover facts; 47% of image leaks not text-recoverable. Need provenance-cascaded tombstones. **Lesson for unshare:** demoting `shareable` must cascade to evidence snippets, embeddings, hydrate caches, and pack replicas—not flip a boolean.

**PRISM:** Formalizes **propagation amplification**—sensitive content repeatedly re-exposed across agent boundaries increases leak risk even without adversarial intent. Generation-time risk scoring beats post-hoc scrubbing. **Lesson:** promotion gates should run at **write/promote time**, not only at final user output.

**Collaborative Memory (2505.18279):** Dual tiers `M_private ∪ M_shared`; immutable provenance `(time, user, agents, resources)`; bipartite `G_UA(t)`, `G_AR(t)`; separate \(\pi^{write/private}\), \(\pi^{write/shared}\), \(\pi^{read}\). Shared writes may anonymize/redact. Cross-user retrieval only if provenance permits. **Closest academic twin of MoDeX’s promotion path.**

### B) KG / RAG sharing & privacy

**LightRAG / GraphRAG practice:** Core GraphRAG is not multi-tenant-safe by default. Isolation must hold at **ingest, graph build, embedding store, and query**—one leaked stage nullifies others. LightRAG issue #2373 documents cross-workspace retrieval bleed when workspace is not enforced end-to-end. Index-time partitioning > query-time metadata filter alone.

**VAULT:** Four disclosure tiers—`KG_ONLY` → `CHUNKS` → `FULL` → `DOCUMENT_BASED`—enforce **before** LLM query processing. Separates structural knowledge (nodes/edges) from source chunks and community summaries. Empirically, restricted users get “I don’t have that,” not soft leakage. **Lesson:** `repo_shared_safe` Anchors may expose **statement + kind + entities** while keeping Evidence / episode digests / private_raw behind higher bars (MoDeX already separates Evidence visibility).

**XACML4G / dynamic KG ACL:** Policies need constraints on **path edges**, not only subject/resource endpoints. Designation of a node without authority to traverse supporting edges enables inference leaks. Patents (US11120150) explore radius-based access—dangerous for MoDeX if “related Anchors” auto-expand share scope.

### C) Capability security / non-discoverability

**Miller et al.:** ACL ≠ capabilities. Key properties:

- **A: No Designation Without Authority** — knowing a name/id must not suffice to open.
- **D: No Ambient Authority** — subject must *select* which authority to exercise.
- Revocation myth false: **revoking facet + forwarding facet** (caretaker) disables access without reclaiming copies.
- Confused deputy: ambient authority + separable designators → BILL overwrite. Cure: capability *is* the designator; purpose-bound keys.

**Spritely / ocaps:** Proxies implement attenuation (read-only, append-only, use-count), logging caretakers, and owner-held revocation switches. Selective disclosure = give attenuated facet, never the editor/admin facet.

**SPKI/SDSI vs ACL:** Authorization via local-name delegation chains; subject presents proof. ACLs force huge central name→permission tables and ambient “who are you?” checks. SPKI still risks confused deputy if auth cert doesn’t designate the resource (Miller note). **For MoDeX:** sealed `.mxp` + capability IDs already match possession model; `repo_shared_safe` must not reintroduce ambient “anyone who can `grep` the repo” authority unless that is the explicit product choice.

### D) Human/team knowledge management

**ADRs (Nygard / AWS / ThoughtWorks practice):**

- Repo-local `docs/adr/` = **team-visible institutional memory** by default (git ACL = team ACL).
- Lifecycle: Proposed → Accepted → Deprecated/Superseded; Accepted treated as immutable; changes via new ADR + SUPERSEDES.
- Public-vs-private: store architecture decisions with code; keep sensitive process/personnel/legal notes out of public repos (`_devprocess`, private wikis).
- Handoff literature: ADR corpus + decision log + evidence pack are continuity artifacts; **rationale is the high-value shareable unit**, not the full deliberation transcript.

**Design rationale (MacLean QOC, DRed, Gruber):** Capture Questions / Options / Criteria (or IBIS issues/answers/pros/cons), not full chat. Experts prioritize: alternatives considered, pros/cons, agreements, and links from rationale → artifact. Capture cost kills practice unless tied to workflow (PR, CAD link). **Lesson:** promote the **compact Anchor statement + reason + SUPERSEDES**, not episode digests or private_raw.

### E) Promotion / consolidation

**Generative Agents:** Importance ∈ [1,10] at write; **reflection when Σ importance ≥ 150**; reflections cite evidence and form trees (observations → higher abstractions). Reflection improves *synthesis*, not automatic *publication*. Ablations show reflection needed for deep inference—but reflections can also over-cooperate / absorb others’ goals (instruction-tuning bias). **Lesson:** importance/reflection may create **candidates**, never silent `repo_shared_safe`.

**MemGPT/Letta:** Working/core = always-visible, small, high-priority; archival = unlimited, search-gated, not ambient. Analogy:

| MemGPT | MoDeX |
|--------|-------|
| Working/core | WorkingState + hot Anchors in hydrate |
| Recall (messages) | Episodes / observations |
| Archival | Long-lived Anchors / Evidence |
| Self-directed page-in | Capability-gated hydrate |

Core≠shared. An agent putting a fact in “core” does not make it fleet-shared. **Promotion across principals is a separate policy.**

**RecMem:** Defer LLM consolidation until **recurrence in a semantic cluster**; subconscious layer stays cheap. Episodic narrative ≠ semantic atomic facts. Recurrence is a signal for *worth extracting*, not *worth broadcasting*. MoDeX’s Tier B recurrence (≥3 episodes) matches RecMem’s intuition—but must stay workstream-scoped unless share gate passes.

---

## 3. Concrete shareable-anchor promotion policy (MoDeX)

### 3.1 What may auto-promote vs must be explicit

**Constitutional rule (strengthen existing lock):**  
`shareable=true` ∧ `visibility=repo_shared_safe` is a **second graduation**, orthogonal to becoming an Anchor. Anchor promotion ≠ repo promotion.

| Anchor kind / signal | Auto → `repo_shared_safe`? | Rationale |
|----------------------|----------------------------|-----------|
| Explicit `modex share` / `modex remember … --shareable` | **Yes (user)** | Human intent = highest confidence (MemClaw trust; ADR ownership) |
| Stable **constraint** / **rejection** with Tier A language + entities ⊆ public code surface + passes redaction | **Candidate only** (surface for accept); optional auto in `share_mode=aggressive` after θ≥2 independent workstreams | ADR-like institutional value; still needs human accept by default |
| Recurrence ≥3 episodes **within one workstream** | **No** — stays `workstream_private` | RecMem/GenAgents: recurrence ≠ cross-boundary appropriateness (ConfAIde/contextual integrity) |
| Tool-verified test failure → rejection | **No** auto-share | May embed proprietary URLs, fixture data, customer names |
| Reflection / importance threshold | **Never** auto-share | Creates candidates only |
| `goal` / `next_step` / `open_question` | **Never** repo-share | Ephemeral task state |
| Speculative agent brainstorm | **Never** | Tier C |
| Secrets, tokens, PII, personal gotchas | **Hard deny** | AgentLeak vault \ \(\mathcal{A}\) |

**Recommended default:** `share_mode=explicit_only` (aligns with architecture §11.8). Optional later: `share_mode=conservative_auto` for constraints/rejections that (a) appear in ≥2 workstreams OR are ADR-linked, (b) pass redaction, (c) have no private Evidence attachments.

### 3.2 Redaction requirements before share

Before flipping visibility:

1. **Schema + kind allowlist** (constraint, rejection, decision, gotcha only).  
2. **Secret/PII scanners** on `statement`, `reason`, entity paths, Evidence snippets.  
3. **Strip or detach Evidence** by default; shareable Anchor may keep `evidence_ids` as capability-gated pointers, not inline snippets.  
4. **Normalize statement** to durable, code-facing form (QOC decision sentence), drop conversational debris.  
5. **Provenance retained** (actor, workstream_id of origin, timestamps) for audit—but **origin workstream membership must not grant ambient read of private siblings**.  
6. **Contradiction/supersession check** against existing `repo_shared_safe` set (MemClaw: don’t let near-dup gate block legitimate supersession—run structural conflict first).  
7. **Allowed-set check** (AgentLeak): fields needed for team continuity only—paths, library names, decision text; not credentials, customer data, unmerged branch secrets.

Emit a `redaction_manifest` (already in `.mxp` sketch) stored with the share event.

### 3.3 Discoverability rules for `repo_shared_safe`

From Miller Property A + MemClaw Inv-Scope + MoDeX §11.7:

1. **Listing:** `modex anchors --shared` lists shareable Anchors to **repo memory principals** only (members with repo-memory capability), not the world.  
2. **No ambient semantic search across private tiers.** Search indices must be **partitioned**: `private_raw` / `workstream_private` / `repo_shared_safe` separate collections (GraphRAG isolation lesson).  
3. **IDs are not capabilities.** Knowing `anchor_id` must not allow GET of non-entitled rows (MemClaw GET-by-id bug). Return **404** on deny.  
4. **Git opt-in:** If team commits shareable Anchors, commit **redacted statements only**; never Evidence or packs. Default: store in local/shared sealed store, not git.  
5. **Hydrate inclusion:** Shared Anchors enter packs only if pack compile policy includes `repo_shared` facet—and pack remains capability-sealed for workstream-private payload.  
6. **Hub restriction (MAMA):** CI bots / fleet orchestrators get **attenuated read** facets (Spritely), not full repo-memory admin.

### 3.4 Revocation / unshare semantics

Adopt caretaker pattern (Miller/Spritely), not “delete the boolean and hope”:

| Mechanism | Behavior |
|-----------|----------|
| `modex unshare <anchor>` | Set `shareable=false`, `visibility→workstream_private` (or tombstone `repo_shared` projection); bump `updated_at`; write audit event |
| **Projection vs source** | Keep workstream-private source; revoke the **shared facet** (forwarder) so holders of old ids lose usefulness |
| **Cascade (MemLeak)** | Invalidate embeddings in shared index; purge from hydrate caches; mark pack snapshots stale; optional re-seal notice to capability holders |
| **Supersession** | Prefer `SUPERSEDES` + new shared Anchor over silent edit (ADR immutability) |
| **TTL** | Optional `share_expires_at` on aggressive auto-shares |
| **Forget** | Hard delete requires cascading Evidence + correlated artifacts; acknowledge residual risk in embeddings |

Revocation does **not** encrypt away copies already decrypted into an agent’s `ephemeral_render`—document that session renders die with session TTL.

### 3.5 Multi-agent confused-deputy risks when shareable facts exist

1. **Ambient retrieve:** Agent with repo-memory read + tool that writes external tickets dumps shared constraints into public channels (AgentLeak C3/C7). Mitigate: purpose-bound capabilities per tool; no ambient “all shared anchors” in tool env.  
2. **ID oracle:** Parallel agent learns `anchor_id` from logs and GETs (MemClaw). Mitigate: enforce scope on every path; 404.  
3. **Pack deputy:** Handoff compiler includes all `repo_shared_safe` into every pack “to be helpful,” expanding blast radius (PRISM amplification). Mitigate: compile policy = workstream Anchors + **opt-in** shared set (relevance-ranked, budget-capped).  
4. **Hub agent:** Orchestrator with high centrality (MAMA) becomes leakage concentrator. Mitigate: attenuated facets; sparse topology.  
5. **Near-dup / contradiction:** Shared Anchor A and private supersession B; agents see A only → stale propagation. Mitigate: shared supersession must be co-promoted or A marked outdated in shared index when B supersedes.  
6. **Reflection oversharing:** Agent reflects private episode into statement resembling shareable constraint and auto-writes. Mitigate: share gate never trusts agent-inferred-alone (confidence <0.4).

---

## 4. Mapping research → MoDeX visibility classes

| MoDeX class | Research analogues | Governance rule |
|-------------|--------------------|-----------------|
| **`private_raw`** | RecMem subconscious; MemGPT recall messages; AgentLeak vault; MemLeak residual surface | Never searchable across principals; never in packs by default; delete cascades |
| **`workstream_private`** | Collaborative Memory `M_private`; MemClaw agent/fleet scope; sealed handoff; ADR “in progress” deliberation | Membership + capability; Inv-Scope on every API; default for Anchors |
| **`repo_shared_safe`** | Collaborative Memory `M_shared` after \(\pi^{write/shared}\); ADR Accepted; VAULT KG_ONLY-style statements; MemClaw tenant-global **with** policy filter | Explicit (or ultra-conservative) promotion; redaction; partitioned index; shareable⇔visibility invariant |
| **`ephemeral_render`** | MemGPT main context / working; Generative Agents prompt subset; PRISM generation surface | Session-scoped; TTL delete; not a persistence tier; must not be re-ingested as private_raw without scrub |

**Handoffs:** remain capability-gated sealed packs (ocaps). Shared Anchors may be *referenced* inside packs for recipients who also hold repo-memory capability; ciphertext still principal-sealed.

---

## 5. Evaluation scenarios for shareable policy

Design an **ArgusFleet-style** harness (predict → measure → remediate) over MoDeX APIs:

1. **Inv-Scope matrix:** For each visibility class × principal role (outsider, same-repo non-member, workstream member, repo-memory principal), probe list/search/GET-by-id/hydrate. Expect deny+404 for non-entitled; zero cross-workstream private hits.  
2. **Promotion abuse:** Agent-inferred reflection tries auto-share; must stay candidate. Explicit user share of constraint succeeds only post-redaction.  
3. **Secret canary:** Plant token in episode; ensure no path promotes/shares it; AgentLeak-style canary across C2 (agent messages), C5 (memory), C7 (artifacts).  
4. **GET-by-id after gossip:** Principal B learns id from log; without capability → 404 (MemClaw regression).  
5. **Unshare cascade:** Share → embed → hydrate cache → unshare; verify shared index, caches, and new packs omit statement; measure residual (MemLeak).  
6. **Supersession race:** Private rejection supersedes shared decision; shared readers must not keep stale active decision (MemClaw contradiction + stale propagation).  
7. **Pack compile deputy:** Orchestrator builds packs for two workstreams; shared set inclusion must be policy-bounded; no private bleed.  
8. **Topology hub:** Star orchestrator with only attenuated shared-read facet cannot escalate to workstream_private (MAMA + ocaps).  
9. **ADR happy path:** User marks Accepted decision shareable; teammates discover via `anchors --shared`; outsiders cannot.  
10. **Propagation amplification:** Multi-agent chain discusses shared constraint; ensure tool/log channels don’t amplify Evidence that was never shared (PRISM/AgentLeak).

**Metrics:** `leak_rate` / `miss_rate` (MemClaw), channel-conditioned allowed-set violations (AgentLeak), time-to-unshare completeness, false-auto-share precision, supersession staleness rate.

---

## 6. Bottom-line design lock (mechanism-level)

1. **Two ladders:** (Anchor probation → active) ⊥ (workstream_private → repo_shared_safe).  
2. **Default share_mode = explicit_only**; recurrence/importance never cross the share boundary alone.  
3. **Every read path enforces visibility** (search, GET, hydrate, MCP, git export)—Inv-Scope.  
4. **Share = issue attenuated facet** after redaction; **unshare = revoke facet + cascade indexes**.  
5. **No ambient authority** for agents over shared Anchors: select capability / compile policy per task.  
6. **Audit provenance** on all promotions; prefer SUPERSEDES over mute edits.

These six locks are directly entailed by MemClaw’s live failures, AgentLeak’s internal-channel results, Miller/Spritely capability mechanics, ADR/rationale practice, and Collaborative Memory’s dual-tier write policies—translated into MoDeX’s four visibility classes.
