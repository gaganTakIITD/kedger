# Kedger — Open-Source Engineering Memory Architecture

> **Status:** Design lock (conversation synthesis)  
> **Product:** **Kedger** (locked)  
> **Date:** 2026-08-08  
> **Purpose:** Constitution for **Kedger** — an open-source local-first memory + handoff product for coding agents.  
> **Audience:** Future implementers (including future chat sessions) who must not lose context.

---

## 0. Why this document exists

Chat context is ephemeral. This file is the durable constitution for:

1. The **problem** worth solving
2. The **non-goals** (hackathon scaffolding to drop)
3. The **locked stack** (hooks + CLI engine)
4. The **locked store** (compact-native Anchors + Evidence)
5. The **memory graph** orchestration
6. The **handoff** model across sessions, branches, agents, and parallel tasks
7. **Privacy / access control** for handoff (not world-discoverable)
8. **Sealed structured storage** (markdown is not the source of truth)
9. Research influences and phased build plan
10. The **product identity** (name, CLI, paths, pack format)

If a future session contradicts this file, update this file deliberately — do not silently drift.

---

## 0A. Product identity lock

| Field | Kedger lock |
|-------|-------------|
| **Product name** | **Kedger** |
| **CLI binary** | `kedger` |
| **Schema family** | `kedger.memory.v1` |
| **User-private store** | `~/.kedger/` |
| **Repo policy dir** | `<repo>/.kedger/` (pointers/policy only; no private payloads) |
| **Sealed pack extension** | `.kxp` (Kedger sealed exchange pack) |
| **Share mode** | `explicit_only` |

**Etymology / metaphor:** a *kedge* is a small working anchor used to warp a vessel into position; a **kedger** does that work. Product reading: place Anchors carefully, pull continuity forward — without dragging the whole transcript sea.

**Availability note (checked 2026-08-08):** GitHub username, npm, PyPI, crates.io, and `kedger.dev` / `.sh` / `.io` were clear at lock time.

---

## 1. Background: the problem

### 1.1 The genuine problem

> **Engineering teams now produce critical reasoning inside AI agent sessions, but that reasoning is never durable, shareable, or loadable the way code is.**

Git stores **what** changed.  
Agent chats store **why** temporarily — then it dies.

Surface symptoms:

1. New agent sessions start cold
2. Teams/agents relitigate rejected approaches
3. “Why did we do it this way?” lives in lost chats
4. Onboarding / context rebuild burns time every session
5. Switching tools (Cursor → Claude Code → Antigravity) resets memory

### 1.2 Problem clusters (priority)

| ID | Problem | Priority |
|----|---------|----------|
| A | Session continuity / handoff | **Core** |
| B | Decision / rejection memory | **Core** |
| C | Cross-tool portability | Important (emerges if store is tool-agnostic) |
| D | Team shared brain / dashboards / lineage | Later |
| E | Full every-prompt surveillance capture | Optional dense mode only |

### 1.3 Crisp problem statement

> AI coding agents now do real engineering work, but their reasoning disappears when the session ends. Teams keep re-deriving context, relitigating settled decisions, and repeating dead ends. Code is versioned; judgment is not. We should make engineering judgment — decisions, rejections, and session context — as durable and handoff-ready as code itself.

### 1.4 Out of scope for Kedger core (Phase F / demo stacks)

| Layer | Why teams sometimes build it | In Kedger core? |
|-------|------------------------------|-----------------|
| Fivetran connectors / Sheet mirror | Enterprise sync demos | No |
| Multi-agent specialist theater | Judge UX | No |
| Cloud Run chatbot frontends | Demo platform | No |
| BigQuery as required bus | Cloud track demos | No |
| MCP-only capture | IDE story | Optional adapter later, not sole core |

### 1.5 Design lessons Kedger keeps

- Append-only session events → compress → hydrate
- Deterministic context structuring (not only vague LLM summary)
- Decision / rejected / files-in-flight as first-class ideas
- Handoff CLI (`pack-export` / `hydrate` / `status`)
- **Negative knowledge** (rejections) is gold

---

## 2. Product direction: Kedger as OSS, local-first

### 2.1 Yes — Kedger is its own OSS project

Fits OSS because:

- Universal pain for AI-coding users
- Natural form is local CLI + repo-local store (git-like)
- Inspectable, forkable, offline-friendly
- Dedicated OSS repository and CLI identity

### 2.2 Product wedge (narrow)

Ship one loop first:

> **Capture judgments + working state → compress into durable Anchors → hand off a boot pack so the next session/agent/teammate does not cold-start.**

Do **not** start as “enterprise shared brain + connectors + dashboard.”

### 2.3 Elevator pitch (OSS)

> **Kedger** — open-source memory/handoff layer for AI coding agents. Local-first CLI engine + IDE hooks. Makes decisions, rejections, and session context durable across tools, sessions, branches, and teammates.

---

## 3. Interface theory (what we supervise)

### 3.1 Pipeline

```text
Human / Agent works
        │
        ▼
   CAPTURE  →  STORE  →  COMPRESS/COGNIFY  →  HYDRATE / HANDOFF
```

### 3.2 Doors into the system

| Door | Role | Adoption reality |
|------|------|------------------|
| **CLI engine** | Core runtime + power user / CI / hooks callee | People will not live here daily |
| **IDE hooks** | Default autocapture UX | **Primary adoption path** |
| **MCP** | Agent tool API for read/write | Useful later; unreliable as sole capture |
| **Team handoff bus** | Why capture exists | Packs + shared Anchors |

### 3.3 Supervision layers

**Must supervise (core):**

1. Memory schema (Anchors, Evidence, Episodes)
2. Pack / handoff format
3. Privacy defaults
4. Promotion / invalidation laws
5. Hydrate budget / ranking

**Supervise later (adapters):**

6. MCP tools
7. More IDE hook packs
8. Hosted sync

### 3.4 Learning / build order (historical thinking)

1. CLI + local store
2. snapshot/hydrate loop
3. decision/reject logging
4. MCP wrapper (parked for after hooks+store+handoff)
5. Hooks for automation

**Updated adoption lock:** hooks are default UX; CLI is engine underneath.

---

## 4. Locked runtime architecture

### 4.1 Locked for v1

```text
IDE hooks  ──(auto)──►  CLI engine  ──►  Memory store (Anchors+Evidence+graph)
                              │
                              └── compile HandoffPack → .kedger/handoff/...
```

| Piece | Lock |
|-------|------|
| Primary UX | IDE hooks |
| Primary runtime | CLI / library engine |
| Primary team feature | Handoff packs |
| Not primary | Manual CLI habits, MCP-first capture, agent-launcher wrapper |

### 4.2 Why not CLI-only daily UX

- People skip manual logging → holes → trust dies
- People will not relaunch agents through our CLI
- IDEs already own agent lifecycle; hooks are the native sensor

### 4.3 Why not MCP-first capture

- Agents forget to call tools
- Capture becomes probabilistic
- Bad for memory truth

### 4.4 Parked for future

- Full MCP server as main surface
- Agent-launcher CLI wrapper
- Hosted team sync service
- Dense every-prompt default
- Multi-agent orchestration theater
- Neo4j-required infra on day 1

### 4.5 Product spine

```text
capture (hooks) → store (core design) → handoff (why it exists)
```

---

## 5. Capture philosophy (before store lock matured)

### 5.1 Memory ≠ transcript

- Every prompt saved forever ⇒ noisy log
- Judgments + foundations saved well ⇒ memory

### 5.2 Two early memory grades (superseded by Anchor model, still useful)

- **Base memory:** decisions, rejections, constraints, invariants, hard gotchas
- **Detailed / working memory:** current goal, files in flight, recent attempts, rich session context

### 5.3 Meaningful capture triggers

Capture/promote when:

1. Judgment formed (decide / reject / constrain)
2. Base shifted (architecture / invariant change)
3. Work boundary (session end, compact, handoff, PR boundary)
4. Hard lesson (costly gotcha)
5. Intent change (user goal materially changed)

### 5.4 Frequency — rejected as primary UX

Early idea: user profiles `manual | boundary | balanced | dense`.

**Lock update:** remove capture-frequency as primary setting.

ChatGPT-like lesson:

> Observe freely into a short-lived buffer; architecture routes into layers automatically.

Remaining tiny knobs only:

- `privacy: normal | strict`
- `promotion: conservative | normal`

---

## 6. Research synthesis (influences)

### 6.1 Frontier product memory patterns

| System | Pattern adopted |
|--------|-----------------|
| **ChatGPT** | Multi-layer memory, auto distillation, inject small slice at session start |
| **Claude / Anthropic** | Compaction ≠ durable memory; external notes; clear stale tool junk |
| **Claude Code** | Auto memory files, PreCompact externalization, SessionStart inject, load size caps |
| **Grok** | Session window + distilled persistent facts; transparent/editable memories |
| **Cursor rules/memories** | Stable project truth vs generated memories vs handoff files |

### 6.2 Agent memory systems / papers

| System / paper | Pattern adopted |
|----------------|-----------------|
| **MemGPT / Letta** | Hot core vs archival; memory hierarchy like OS RAM/disk |
| **Mem0** | Extract facts; ADD-oriented history; entity linking; fused retrieval |
| **Graphiti / Zep** | Episodes → entities → temporal facts; invalidate don’t delete; provenance |
| **AriGraph** | Semantic graph + episodic vertices linked together |
| **A-MEM** | Atomic notes, write-time linking, memory evolution |
| **HippoRAG** | Entity graph + associative multi-hop retrieval (PageRank-like) |
| **GraphRAG** | Communities + hierarchical summaries |
| **LightRAG** | Dual local/global retrieval; incremental subgraph updates |
| **Generative Agents** | Memory stream, importance, reflection promotion |
| **Nemori** | Event segmentation into episodes; predict/calibrate semantic facts |
| **GAM** | Local episodic graph first; later consolidate to global (avoid contamination) |
| **Cognee** | remember → cognify(graph) → recall |
| **Surveys (2024–2026)** | Working / episodic / semantic / procedural taxonomy; consolidate/retrieve/compress ops |

### 6.3 Critical research lesson for compaction

Compaction of the model context window is **lossy**.

Therefore:

> Anything that must survive must already live outside the transcript in compact structured form **before** destructive compact.

---

## 7. LOCKED STORE ARCHITECTURE

### 7.1 Constitutional lock

> **Durable memory must be compact-native, not compact-rescued.**

Do not store fat transcripts and hope summarization preserves meaning.  
Store memory as already-compact **Anchors** with optional **Evidence**.  
Under compaction pressure, Anchors are guaranteed; Evidence is budgeted.

### 7.2 The memory atom: Anchor + Evidence

#### Anchor (always survive)

Tiny, typed, high-trust memory unit.

```text
Anchor
- id
- kind            # decision | rejection | constraint | gotcha | goal | next_step | open_question
- statement       # one-sentence canonical meaning
- reason          # short why (preferred)
- about[]         # entities: files, libs, services, modules
- status          # active | superseded | disputed | archived
- valid_at
- invalid_at      # null if active
- provenance      # episode_id + actor + source (+ observation refs)
- importance      # 0..1
- repo_scope
- workstream_id?  # null for repo-global anchors
```

**Hard rule:** if context must shrink to almost nothing, Anchors still hydrate.

#### Evidence (budgeted)

```text
Evidence
- id
- supports_anchor_id
- snippet
- source_ref
- weight
```

**Hard rule:** losing Evidence must not erase Anchor meaning.

### 7.3 Compact-pressure survival order (non-negotiable)

When storage/hydrate/context is tight, keep in this order:

1. active constraints  
2. active rejections  
3. active decisions  
4. current goal  
5. next_step  
6. open questions  
7. latest episode digest (short)  
8. evidence snippets  
9. older episodes  
10. raw observations ← first to die  

### 7.4 Store layout (logical)

```text
memory =
  Anchor Store          # canonical, tiny, temporal
+ Evidence Store        # optional, ranked
+ Episode Digests       # medium, compressible
+ Raw Buffer            # ephemeral observations
+ Working State         # mutable per workstream
+ Handoff projections   # compiled boot images
```

### 7.5 Operational rule under compact

```text
on pre_compact / session_stop / handoff:
  1) extract/upsert Anchors from recent work
  2) attach Evidence links
  3) only then allow working-context compact/summary
  4) compile handoff from Anchors first
```

Never reverse this order.

### 7.6 What “good store” means

A second agent, after hydrate, can answer without guessing:

1. What was decided  
2. What was rejected and why  
3. Which files/tasks are hot  
4. What the last human actually asked / next step  

---

## 8. Layered architecture (compatible with Anchor lock)

Layers are projections / pipelines over the store — not a competing product.

```text
L0 RAW OBSERVATION BUFFER     ephemeral high-volume hook events
L1 WORKING STATE              current mission brain per workstream
L2 EPISODE DIGESTS            compressed chapters of work
L3 BASE / ANCHORS             durable team/repo/workstream truth
L4 HANDOFF SURFACE            compiled pack for next consumer
```

### 8.1 L0 Raw buffer

- Always append from hooks (no frequency UX)
- Size/time capped ring buffer
- Not shared by default
- Not “memory” until cognified

### 8.2 L1 Working state

Mutable per workstream:

- goal
- last_user_ask
- files_in_flight[]
- open_questions[]
- blockers[]
- active_branch
- updated_at

Upsert on state deltas only. Keep tiny.

### 8.3 L2 Episodes

Boundary-created digests:

- time_range
- summary
- decisions/rejections touched
- files touched
- failed approaches
- next_steps
- salient evidence (short)

### 8.4 L3 Anchors (base)

Repo/workstream durable facts with temporal invalidation.

### 8.5 L4 Handoff

Projection compiled from ranked Anchors + working + recent episodes.

### 8.6 Automatic routing (replaces frequency)

```text
hook event
  → always L0
  → maybe patch L1 (state-changing)
  → maybe L3 candidate (judgment-grade)
  → on boundary: compact to L2 + promote + compile L4
```

Boundary examples:

- session stop / end
- pre-compact / context pressure
- idle gap
- workstream switch
- explicit `handoff`
- cumulative importance threshold

---

## 9. Memory graph orchestration (core idea detail)

### 9.1 Graph thesis

> Raw logs are not memory. Memory is a graph of linked, graded, time-aware knowledge that can be compacted, retrieved, and handed off.

### 9.2 Cognitive types mapped

| Type | Product meaning | Graph role |
|------|-----------------|------------|
| Working | current goal / hot files / open loops | Working node + hot edges |
| Episodic | what happened in a work chapter | Episode nodes |
| Semantic | durable judgments | Anchor/fact nodes + validity |
| Procedural (later) | reusable playbooks | Skill/pattern nodes |
| Handoff | boot image for next consumer | Compiled projection node |

### 9.3 Node types

```text
EpisodeNode
EntityNode          # file, module, service, library, person, workstream, error-class
AnchorNode          # decision | rejection | constraint | gotcha | goal | next_step | open_question
WorkingNode         # mutable current-state per workstream
CommunityNode       # optional theme cluster (auth, billing, ...)
HandoffNode         # immutable compiled pack version
ObservationRef      # pointer into L0 (not full payload in hot graph)
```

### 9.4 Edge types

```text
MENTIONS            Episode → Entity
DERIVES             Episode → Anchor
RELATES_TO          Entity ↔ Entity
ABOUT               Anchor → Entity
SUPERSEDES          Anchor → Anchor
SUPPORTS            Evidence/Anchor → Anchor
CONTRADICTS         Anchor → Anchor
NEXT_IN             Episode → Episode
IN_WORKSTREAM       * → Workstream
IN_COMMUNITY        Entity/Anchor → Community
COMPILED_INTO       Anchor/Episode/Working → Handoff
LINKED_TO           Anchor ↔ Anchor
CONTINUES           Handoff → Handoff
PARALLEL_WITH       Handoff ↔ Handoff
BRANCH_OF           Handoff → branch facet
```

### 9.5 Temporal model (non-negotiable)

Every semantic Anchor carries:

```text
created_at
valid_at
invalid_at
expired_at?
status: active | superseded | disputed | archived
```

**Law:** contradictions invalidate; they do not erase history.

### 9.6 Provenance model

Every Anchor must answer:

- which Episode produced it?
- which ObservationRefs support it?
- which actor / session / repo / workstream?

No anonymous team truth.

### 9.7 Engineering ontology (prescribed)

Entity types:

```text
Repo, Workstream, Person, AgentTool
File, Module, Service, API, Table
Library, Pattern, ErrorClass, Test
PR, Commit (optional later)
```

Relation examples:

```text
decided_for / rejected_for
depends_on / replaces / conflicts_with
owns / touched / blocked_by
implements / tested_by
```

### 9.8 Four runtime loops

#### Loop A — Encode (hooks, always on)

```text
event → redact → L0 append → cheap entity tags
     → maybe patch WorkingNode
     → importance score
     → maybe mark for link pass
```

#### Loop B — Segment + Cognify (boundary)

```text
1) segment L0 span → Episode
2) extract entities + candidate Anchors
3) write Episode + MENTIONS + DERIVES
4) link to related historical Anchors
5) temporal resolve (invalidate conflicts)
6) optional community update
7) prune L0 span
8) compile HandoffNode
```

#### Loop C — Reflect / Consolidate (less frequent)

```text
when enough episodes accumulate:
  reflect higher-level insights
  promote repeated patterns to Anchors
  evolve old note contexts
  refresh small community summaries
```

#### Loop D — Retrieve + Hydrate

- Default: compile budgeted handoff subgraph
- Later: query-time associative retrieval (entity seeds + neighborhood / PPR-like)

### 9.9 Cognify pseudo-spec

```text
function cognify(episode_span):
  episode = summarize_structured(span)          # deterministic first
  entities = upsert_entities(extract(span))
  candidates = extract_anchor_candidates(span)

  for anchor in candidates:
      related = find_related_anchors(anchor)
      conflicts = detect_conflicts(anchor, related)
      if conflicts:
          invalidate(conflicts, at=anchor.valid_at)
          mark supersession edges
      upsert_anchor(anchor)
      link relationships + ABOUT entities
      link episode DERIVES anchor

  link episode MENTIONS entities
  refresh working node
  compile handoff under budget
  return handoff
```

### 9.10 Failure modes to prevent

- Memory contamination (don’t promote every prompt to Anchor)
- Semantic drift (isolate by workstream/community)
- Catastrophic overwrite (invalidate, don’t delete)
- Context rot on hydrate (strict budget + ranking)
- Orphan facts (require provenance)

### 9.11 Local persistence shape (v1 friendly) — revised

> **Lock update:** plain markdown / world-readable json under the git repo is **not** the canonical store.

Preferred v1 shape:

```text
~/.kedger/                                 # user-private by default (not in git)
  keys/                                   # local keyring material (or OS keychain refs)
  projects/<repo_fingerprint>/
    store.sqlite                          # canonical structured store (optionally SQLCipher)
    raw/events.ring                       # ephemeral observations
    packs/<workstream>/<handoff_id>.kxp   # sealed handoff packs
    packs/<workstream>/HEAD               # pointer to current pack id
    acl/<workstream>.json                 # membership / capability policy (local)

<repo>/.kedger/                            # optional, minimal, mostly pointers/policy
  project.json                            # repo id, policies, no private payloads
  .gitignore                              # deny packs/raw/store by default
```

Canonical meaning lives in **structured store + sealed packs**, not in `.md` files.  
No Neo4j required for v1.

---

## 9A. How memory actually works (detailed runtime)

This section explains the adopted model as one system: **layers are the pipeline; the graph is the meaning structure; Anchors are what survive.**

### 9A.1 One-picture model

```text
HOOK EVENT
   │
   ▼
┌────────────── L0 RAW BUFFER ──────────────┐
│ append-only observations (ephemeral)      │
└───────┬───────────────────────┬───────────┘
        │ state delta?          │ judgment?
        ▼                       ▼
   L1 WORKING NODE         L3 ANCHOR CANDIDATE
   (per workstream)        (not committed yet)
        │                       │
        └──────────┬────────────┘
                   │ boundary? (stop/compact/idle/handoff)
                   ▼
            COGNIFY PASS
                   │
       ┌───────────┼────────────┐
       ▼           ▼            ▼
  L2 EPISODE   GRAPH LINKS   L3 ANCHORS
  (chapter)    (edges)       (active/superseded)
                   │
                   ▼
            L4 HANDOFF PACK (.kxp sealed)
                   │
                   ▼
            AUTHORIZED HYDRATE
```

Important:

- Layers are **not five separate databases fighting each other**
- They are stages/projections over one graph-backed store
- L0 is sensor tape
- L1 is live mission cursor
- L2 is chapter history
- L3 is durable judgment graph
- L4 is the portable sealed projection for the next consumer

### 9A.2 What each layer is doing in practice

#### L0 — Raw Observation Buffer (sensor tape)

**Writes when:** every hook event (prompt, edit, tool, stop, etc.)  
**Form:** append-only event records  
**Lifetime:** continuous, automatic  
**Lifetime:** short (ring buffer by size/time)  
**Shared?** no  

Example events:

```text
t1 user_prompt: "auth keeps failing with CSRF on cookies"
t2 file_edit: auth/session.ts
t3 tool_call: run tests
t4 agent_response: "cookie sessions are brittle here..."
t5 user_prompt: "ok reject cookie sessions, use JWT"
t6 stop
```

L0 alone is not memory. It is evidence material.

#### L1 — Working State (live mission brain)

**Writes when:** state actually changes  
**Form:** one mutable WorkingNode per workstream  
**Keeps only:**

- current goal
- last user ask
- files in flight
- blockers / open questions
- active branch

After t5 above, L1 might be:

```text
workstream: auth-refactor
goal: replace cookie sessions with JWT
last_user_ask: reject cookie sessions, use JWT
files_in_flight: [auth/session.ts, auth/middleware.ts]
open_questions: [refresh-token rotation]
branch: feat/auth
```

L1 is tiny on purpose. It answers “what is true right now?”

#### L2 — Episode Digest (chapter memory)

**Writes when:** boundary hits (stop / compact / idle / handoff / workstream switch)  
**Form:** EpisodeNode + links  
**Job:** compress a span of L0+L1 into durable chapter meaning

Episode example:

```text
Episode e12
summary: Moved auth away from cookie sessions toward JWT
files: auth/session.ts, auth/middleware.ts
failed_approaches: cookie sessions (CSRF brittleness)
next_steps: implement refresh-token rotation
time_range: t1..t6
```

After episode write, old L0 rows for that span can be pruned.  
Meaning remains in Episode + Anchors.

#### L3 — Anchors (durable judgment graph)

**Writes when:**

- explicit `kedger remember ...`, or
- strong judgment signals promoted during cognify, or
- reflection finds repeated pattern across episodes

From the example, cognify creates:

```text
Anchor A1 kind=rejection
statement: Do not use cookie sessions for auth
reason: CSRF brittleness / failing tests
about: [Library:cookies, File:auth/session.ts]
status: active

Anchor A2 kind=decision
statement: Use JWT access tokens for auth sessions
reason: more reliable for current API surface
about: [File:auth/session.ts, File:auth/middleware.ts]
status: active

Anchor A3 kind=next_step
statement: Implement refresh-token rotation next
status: active
workstream: auth-refactor
```

These are the compact-native survivors.

#### L4 — Handoff surface (sealed projection)

**Writes when:** after cognify / explicit handoff  
**Form:** sealed `.kxp` compiled from:

1. ranked active Anchors (first)
2. L1 working snapshot
3. latest episode digest(s)
4. relation pointers (parent/parallel handoffs)

L4 is not a second brain. It is the boot image.

### 9A.3 Where the graph sits

The graph is the connective tissue across L1–L4 (and refs into L0):

```text
[Episode e12]
   MENTIONS → File:auth/session.ts
   MENTIONS → File:auth/middleware.ts
   DERIVES  → Anchor A1 (reject cookies)
   DERIVES  → Anchor A2 (use JWT)
   DERIVES  → Anchor A3 (next: refresh rotation)
   NEXT_IN  → (previous episode e11)

[Anchor A1]
   ABOUT → File:auth/session.ts
   ABOUT → Library:cookies
   SUPPORTS ← Evidence snip "CSRF failures in tests"
   LINKED_TO → Anchor A2
   IN_WORKSTREAM → Workstream:auth-refactor

[Anchor A2]
   ABOUT → File:auth/session.ts
   SUPERSEDES → (older decision "use cookie sessions", now invalid)
   IN_WORKSTREAM → Workstream:auth-refactor

[WorkingNode auth-refactor]
   points at current goal/files/open questions

[Handoff h77]
   COMPILED_INTO ← A1,A2,A3, WorkingNode, Episode e12
   CONTINUES → h76
```

So when someone asks “why JWT?”, retrieval is not keyword hope over chat.  
It is graph neighborhood around `auth/session.ts` / auth workstream.

### 9A.4 Exact write path (one event → memory)

Take event t5: user says reject cookies, use JWT.

```text
1) INGEST
   redact secrets
   append to L0 as observation o55

2) ROUTE
   detect state delta → update L1 goal/next/files
   detect judgment language → create Anchor candidates:
     reject cookie sessions
     decide JWT

3) (no boundary yet)
   candidates may stay pending if promotion=conservative
   or auto-commit if explicit/strong and promotion=normal

4) BOUNDARY (session stop)
   cognify(span):
     create Episode e12
     upsert entities File:auth/session.ts, Library:cookies, ...
     commit Anchors A1/A2/A3 with provenance episode=e12, obs=o55
     link MENTIONS / DERIVES / ABOUT / LINKED_TO
     if old cookie-session decision exists:
        mark old invalid + SUPERSEDES edge
     refresh WorkingNode
     compile sealed Handoff h77 from anchors-first budget
     prune L0 span t1..t6 (keep ObservationRefs as needed)
```

### 9A.5 Exact read path (hydrate / continue)

Authorized principal starts next session on same workstream:

```text
1) resolve workstream = auth-refactor
2) authorize capability
3) open sealed handoff HEAD (h77) + active anchor store slice
4) rank under budget:
     constraints/rejects/decisions → goal/next_step → latest episode → evidence
5) inject structured memory into agent context
6) agent starts warm:
     knows cookies rejected, JWT chosen, refresh rotation next, hot files
```

If another agent is on `billing-tax` in parallel:

- different WorkingNode
- different Episode stream
- different Handoff HEAD
- may still see repo-global shareable constraints only if permitted
- cannot read `auth-refactor` sealed packs without capability

### 9A.6 How compaction pressure is handled

There are two “compacts”:

1. **Model/context compact** (IDE/agent window pressure)  
2. **Store compact** (our cognify/prune)

Our law for both:

```text
externalize Anchors first
then compress chapters into Episodes
then drop raw L0
never depend on a prose summary as sole memory
```

Under extreme budget, hydrate may include only:

```text
A1 rejection (cookies)
A2 decision (JWT)
A3 next_step (refresh rotation)
L1 goal + hot files
```

and still be useful. That is why Anchors are compact-native.

### 9A.7 How layers and graph divide responsibility

| Concern | Owner |
|---------|--------|
| Capture everything cheaply | L0 |
| Know current mission | L1 WorkingNode |
| Remember what a chapter meant | L2 EpisodeNode |
| Remember durable judgments | L3 AnchorNodes + temporal edges |
| Package continuity for next consumer | L4 HandoffNode/pack |
| Explain relationships / why | Graph edges |
| Survive compact | Anchors first |
| Stay private | sealed L4 + ACL on workstream |

### 9A.8 What we explicitly did *not* adopt as core

- Flat vector DB of chat chunks as the brain  
- Markdown files as canonical memory  
- One giant summary blob per repo  
- Promoting every prompt into durable graph nodes  
- Requiring Neo4j on day one  

We adopted:

> **Layered pipeline + temporal Anchor graph + sealed handoff projection.**

### 9A.9 Minimal success trace (should be demonstrable)

```text
Session A:
  reject Mongo/cookies/... as Anchor
  decide alternative as Anchor
  stop → episode + sealed handoff

Session B (authorized, same workstream):
  hydrate
  agent does not re-propose rejected approach
  agent continues next_step with hot files known
```

If this trace fails, the memory architecture is not working — regardless of UI.

---

## 10. LOCKED HANDOFF ARCHITECTURE (next primary goal)

### 10.1 Handoff is bigger than cold start

Handoff must cover:

- zero → warm (new agent)
- warm → warmer (continuing sessions)
- across multiple sessions with lineage
- across branches
- across different agent tools
- multiple agents on one machine on different tasks
- multiple agents on same task (parallel)
- relational links between handoffs/sessions

### 10.2 Key abstraction: Workstream

```text
Repo
 └── Workstream (logical task thread, e.g. auth-refactor)
      ├── Session 1
      ├── Session 2
      ├── Parallel session/agent
      ├── Branch tips
      └── Handoff lineage
```

**Agents/sessions are ephemeral. Workstreams are durable.**  
Handoff belongs to a workstream first; branch/session/agent are facets.

### 10.3 HandoffPack schema (conceptual)

```text
HandoffPack
- handoff_id
- schema_version
- repo
- workstream_id
- branch
- session_ids[]
- from_actor
- to_scope                 # self | teammate | any-agent | workstream
- created_at
- parent_handoff_id
- related_handoff_ids[]
- anchors[]                # guaranteed compact memory
- working                  # goal, next_step, files_in_flight, open_questions
- episode_digests[]
- relations
- budget_stats
```

### 10.4 Handoff relation graph

```text
CONTINUES
PARALLEL_WITH
RELATES_TO
BRANCH_OF
SUPERSEDES
DERIVES_FROM_SESSIONS
SAME_WORKSTREAM
MERGES_TO
```

### 10.5 Scenario matrix

| Scenario | Behavior |
|----------|----------|
| Same agent, next day | hydrate latest workstream pack (`CONTINUES`) |
| New agent, same branch | agent-agnostic pack + repo anchors |
| Different branch, same task | branch tip pack + shared workstream/repo anchors |
| Two agents, different tasks | isolated workstreams; share only repo-global anchors |
| Two agents, same task | `PARALLEL_WITH` packs; pin or compose |
| After compact | Anchors intact; pack still coherent |
| Multi-session history | lineage explains evolution; not only latest blob |

### 10.6 Branch rules

- Branch is a facet, not sole identity
- Branch-local working state may differ
- Repo-global active Anchors (especially rejections/constraints) usually transcend branches
- Prefer: current branch tip pack → else workstream latest → always include ranked global Anchors

### 10.7 Multi-agent same machine rules

```text
One active WorkingState per workstream
Multiple workstreams can run in parallel
Never silently mix working states across workstreams
Shared layer = repo-level active Anchors only
```

### 10.8 Parallel same-task rules

- Allow multiple packs under one workstream from different actors
- Relation: `PARALLEL_WITH`
- Compose policy: union Anchors via store supersession truth; working-state conflicts become open_questions / conflict markers

### 10.9 Handoff runtime

```text
boundary (stop | compact | switch | explicit)
  1. externalize Anchors to store
  2. refresh WorkingState for workstream
  3. compile HandoffPack (anchors-first budget)
  4. write current + history
  5. link parent/parallel relations
  6. next consumer uses hydrate router
```

### 10.10 Hydrate router

```text
inputs: repo, branch, actor, files_focus, explicit workstream?

resolve workstream:
  explicit > branch map > file map > last active on machine

select:
  1) repo-global active Anchors (always)
  2) workstream current pack
  3) optional related packs if budget allows

compile injection under hard budget
```

Hydrate modes:

- `latest` (default)
- `since:<handoff_id>`
- `lineage`
- `merge` / `compose`
- `pin:<actor|handoff_id>`

### 10.11 Handoff locked statements

1. Store is Anchor-canonical; handoff is a projection  
2. Workstream is the primary handoff key  
3. Handoffs form a relation graph  
4. Multi-agent safety = workstream isolation + shared repo anchors  
5. Hydrate is routed, ranked, and budgeted — never dump all memory  
6. **Handoff is capability-gated, not world-discoverable**  
7. **Markdown is not the canonical handoff format**  

### 10.12 One-sentence handoff lock

> Handoff is a workstream-scoped, relational, **sealed** boot pack compiled from compact Anchors — carrying continuity across sessions, branches, and authorized agents, while keeping parallel tasks isolated and linking related sessions instead of flattening them into one blob.

### 10.13 Why markdown is the wrong canonical format

Markdown is fine as an **ephemeral render** after authorized hydrate (for pasting into an agent).  
It is a bad **source of truth** for handoff because:

| Problem | Why it hurts |
|---------|--------------|
| No access control | Anyone with repo/fs access can read it |
| Git-leakage | Easy to commit/push secrets + private reasoning |
| Weak structure | Meaning drifts; hard to validate/rank/merge |
| No integrity | Tamper/corruption not detectable |
| Bad multi-agent merge | Diffing prose packs is lossy and unsafe |
| Discoverability | World-readable filenames advertise active workstreams |

**Lock:** canonical handoff storage is a **sealed structured pack** (`.kxp`), not `.md`.

---

## 11. Privacy, access control, and sealed storage

This section is now a first-class product lock, not an afterthought.

### 11.1 Privacy thesis

> Continuity is for **authorized developers of a workstream**, not for everyone who can see the repo.

Handoff without access control becomes accidental surveillance + IP leakage.

### 11.2 Threats we explicitly care about

1. Random teammate / outsider reads another task’s private reasoning  
2. Public git history leaks handoff contents  
3. Parallel agent on same machine reads the wrong workstream  
4. Shared CI/runner disk exposes packs  
5. “Helpful” plaintext markdown gets committed  
6. Lost laptop exposes unencrypted memory store  

### 11.3 Visibility classes (locked)

| Class | Contents | Default audience |
|-------|----------|------------------|
| `private_raw` | L0 observations, full prompts/tool dumps | local actor only |
| `workstream_private` | working state, episode digests, handoff packs | workstream members only |
| `repo_shared_safe` | carefully promoted Anchors marked shareable (e.g. stable constraints) | repo memory principals |
| `ephemeral_render` | temporary hydrate text for an agent | current authorized session only |

**Default:** handoffs are `workstream_private`.  
They are **not** globally discoverable inside the repo.

### 11.4 Access model: membership + capability (not broadcast)

Handoff access requires **both**:

1. **Principal identity** (developer/agent actor key)  
2. **Capability for that workstream/pack**

```text
Principal
- principal_id
- public_key
- display_name
- device_id?

Capability
- capability_id
- workstream_id and/or handoff_id
- grantee_principal_id
- permissions: read_hydrate | append | admin
- expires_at?
- issuer_signature
```

Sharing is explicit:

```text
kedger grant --workstream auth-refactor --to gagan
kedger handoff --share gagan          # seal pack to grantee key(s)
kedger revoke --workstream auth-refactor --from gagan
```

No capability ⇒ pack cannot be decrypted/hydrated, even if the file is copied.

This is the privacy tradeoff lock:

- Easy continuity for people **on the task**
- Hard/no continuity for everyone else

### 11.5 Sealed pack format (`.kxp`) — canonical handoff storage

Replace plaintext markdown/json handoff files with a sealed envelope:

```text
.kxp (Kedger Pack)
├─ header (plaintext, minimal)
│   - magic / schema_version
│   - handoff_id / workstream_id / repo_fingerprint
│   - created_at / from_actor
│   - content_hash
│   - recipient_key_ids[]          # who can open
│   - algo suite
├─ signature                      # authenticity from from_actor
└─ ciphertext                     # encrypted payload
    └─ payload (structured)
        - anchors[]               # compact meaning first
        - working
        - episode_digests[]
        - relations
        - evidence? (optional, higher sensitivity)
        - redaction_manifest
```

Properties:

- **Secure:** encrypted for recipients only  
- **Meaningful:** structured Anchors preserve judgment under compact budgets  
- **Handoff-easy:** one file can be copied/sent; recipient `kedger hydrate --pack x.kxp`  
- **Not broadly discoverable:** header reveals ids, not private reasoning  
- **Integrity:** hash + signature  

Optional later: also encrypt local `store.sqlite` at rest (SQLCipher / OS keychain-wrapped key).

### 11.6 Markdown policy (strict)

| Use | Allowed? |
|-----|----------|
| Canonical store | **No** |
| Canonical handoff | **No** |
| Git-committed project memory | **No** (by default) |
| Ephemeral hydrate render for current agent | Yes, temp only |
| `kedger inspect --render md` for authorized user | Yes, explicit, local |

```text
hydrate flow:
  authorize principal
  → open sealed pack / store
  → compile ranked structured view
  → inject into agent via hook/MCP/temp file
  → temp render deleted or kept only in secure session cache
```

### 11.7 Discoverability rules

By default:

- Do **not** list other principals’ private workstreams to unauthorized users  
- `kedger status` shows only workstreams you can access  
- Pack filenames should not require revealing sensitive titles in shared dirs  
- Repo `.kedger/` may store project policy only; private packs live under user store or sealed exchange  

Authorized listing:

```text
kedger workstreams          # only visible memberships
kedger handoff list         # only decryptable/readable packs
```

### 11.8 What may be broadly shared vs must stay sealed

| Memory kind | Default share posture |
|-------------|-----------------------|
| Raw prompts / tool dumps | never |
| Working state / in-flight details | workstream members only |
| Episode digests | workstream members only |
| Handoff packs | sealed to recipients |
| Stable repo constraints (explicitly marked `shareable`) | optional repo-shared |
| Personal gotchas | private unless promoted |

Promotion to `repo_shared_safe` must be explicit (or very conservative auto policy).

### 11.9 Team bus for v1 (privacy-preserving)

Not “commit markdown to git.”

v1 exchange options:

1. **Local same-machine principals** via shared user store + ACL  
2. **Sealed pack file transfer** (chat/drive/USB) encrypted to recipient keys  
3. Later: sync service with server-side ciphertext and membership

Git may store:

- public policy stubs  
- maybe shareable stable anchors if team opts in  

Git must not store by default:

- raw events  
- private handoff packs  
- working state  

### 11.10 Privacy tradeoff statement (locked)

> We optimize for **authorized continuity**, not public memory broadcasting.  
> If a person is not a workstream principal (or holder of a pack capability), they should not be able to discover or read that handoff’s meaning.

This is intentional friction — and necessary trust.

### 11.11 Trust primitives checklist

- [ ] Principal identity keys  
- [ ] Workstream ACL / capabilities  
- [ ] Sealed `.kxp` encrypt+sign  
- [ ] Redaction on ingest  
- [ ] Default deny discoverability  
- [ ] `grant` / `revoke`  
- [ ] `forget` / pack tombstones  
- [ ] No plaintext markdown canonical files  
- [ ] Temp hydrate render only after auth  

---

## 12. CLI surface (engine + human)

### 12.1 Daily / human

```text
kedger status
kedger handoff                 # compile sealed pack for current workstream
kedger hydrate                 # authorized hydrate only
kedger remember decision|reject|constraint "..."
kedger forget <id>
kedger why <entity|topic>
kedger grant --workstream <id> --to <principal>
kedger revoke --workstream <id> --from <principal>
```

### 12.2 Engine / hooks

```text
kedger ingest --from-hook
kedger cognify --boundary auto|stop|compact|idle
kedger doctor
kedger graph export|stats
```

### 12.3 Power

```text
kedger graph path <a> <b>
kedger graph neighbors <entity> --depth 2
kedger hydrate --workstream <id>
kedger hydrate --pack <file.kxp>
kedger hydrate --pin <handoff_id>
kedger inspect --render md     # explicit authorized local render only
kedger keys ...
```

### 12.4 Design rule

All doors (hooks now, MCP later) call the same engine modules:

```text
ingest → redact → router → store/graph → compact/cognify → promote → seal/compile → authorize → hydrate
```

---

## 13. Compression philosophy

### Must keep during compaction/cognify

- goal trajectory / current goal
- decisions / rejects / constraints touched
- files that mattered
- failed approaches
- next concrete step
- provenance for new Anchors

### Can drop

- full tool JSON dumps
- trivial edits
- repeated chatter
- raw prompt floods

### Compressor modes

1. **v1:** deterministic structured extraction (default, trustworthy)
2. **later:** optional LLM distill for richer episode summaries

Never make LLM summarizer the only path in v1.

---

## 14. Hydrate budget targets

Inspired by Claude Code load caps:

Target package roughly:

```text
~2–6KB working state
+ top N anchors (constraints/rejects first)
+ 1–3 episode digests
= hard cap (example target: 25–40KB)
```

If over budget, follow §7.3 survival order.

---

## 15. Evaluation criteria

Memory/handoff is working when:

1. Rejection becomes an active Anchor with provenance  
2. Contradicting later judgment supersedes cleanly  
3. Teammate/agent B hydrate includes that Anchor without raw chat  
4. `why <entity>` returns a connected explanation path  
5. Hydrate stays under budget and still enables warm start  
6. L0 rotation does not destroy Anchors  
7. Parallel workstreams do not contaminate each other  
8. Multi-session lineage remains queryable via handoff relations  
9. Unauthorized principal cannot list/decrypt another workstream handoff  
10. Canonical packs are sealed `.kxp`; no plaintext markdown source-of-truth  

Suggested fixture tests:

- handoff continuity Q&A
- no-relitigation test
- budget ceiling test
- loss/rotation test
- contradiction/supersession test
- privacy redaction test
- parallel workstream isolation test

---

## 16. Phased implementation plan

### Phase A — Store skeleton + identity

- private user store layout (not git-canonical)
- L0 append + rotation + redaction
- L1 working upsert
- explicit Anchor remember/forget
- principal key bootstrap (`kedger keys`)
- CLI: ingest, remember, status, doctor

### Phase B — Sealed handoff

- compile structured HandoffPack
- seal to `.kxp` (encrypt+sign)
- workstream ACL grant/revoke
- authorized hydrate only
- ephemeral render path (no markdown SoT)

### Phase C — Automatic chapterization

- boundary detector
- L2 episode cognify (deterministic)
- L0 prune after episode
- auto sealed recompile

### Phase D — Graph association + promotion

- entity/anchor edges
- conflict invalidation
- ranked hydrate budget
- `kedger why`

### Phase E — Hook packs

- major IDE adapters calling same CLI
- SessionStart authorized hydrate inject

### Phase F — later

- MCP tools
- optional LLM episode distill
- associative search / PPR-like retrieval
- sync service for ciphertext + membership
- richer community graph
- at-rest DB encryption defaults

---

## 17. Explicit locks checklist

Use this as the quick constitution:

- [x] Genuine problem = durable engineering judgment + handoff  
- [x] OSS local-first direction  
- [x] Product identity = **Kedger** (`kedger` CLI, `~/.kedger/`, `.kxp`)  

- [x] v1 UX = IDE hooks; runtime = CLI engine  
- [x] MCP / hosted sync / ADK / Fivetran not core  
- [x] No user-facing capture-frequency matrix  
- [x] Store = compact-native **Anchors + Evidence**  
- [x] Anchors guaranteed under compaction; Evidence budgeted  
- [x] Temporal invalidation (no silent overwrite)  
- [x] Provenance required on Anchors  
- [x] Workstream is primary handoff key  
- [x] Handoffs are relational (lineage/parallel/branch)  
- [x] Multi-agent isolation by workstream  
- [x] Hydrate is ranked + budgeted projection  
- [x] Handoff is capability-gated / not world-discoverable  
- [x] Canonical storage is sealed structured packs + private store (not markdown)  
- [x] Markdown allowed only as ephemeral authorized render  
- [x] Exact v1 schemas locked in `docs/MEMORY_SCHEMAS_V1.md`  
- [x] Handoff budget defaults + drop order locked in schemas doc  
- [x] Workstream identity + promotion signals locked in `docs/WORKSTREAM_AND_PROMOTION_V1.md`  
- [x] Parallel compose + hook event mapping locked in `docs/PARALLEL_COMPOSE_AND_HOOKS_V1.md`  
- [x] `.kxp` crypto/key UX + shareable-anchor policy locked in `docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md`  
- [x] Deep-read research memos + corpus inventory under `docs/research/`  

---

## 18. Next design locks needed (not done yet)

1. ~~Exact JSON schemas~~ → **done:** `docs/MEMORY_SCHEMAS_V1.md`  
2. ~~`.kxp` implementation choice~~ → **done:** `docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md` (age-shaped + libsodium XChaCha + Ed25519 StE)  
3. ~~Workstream identity algorithm~~ → **done:** `docs/WORKSTREAM_AND_PROMOTION_V1.md`  
4. ~~Promotion signal list~~ → **done:** same doc (Tier A/B/C + probation gate)  
5. ~~Hydrate ranking / budgets~~ → defaults locked in schemas; may refine with benchmarks  
6. ~~Conflict/compose rules~~ → **done:** `docs/PARALLEL_COMPOSE_AND_HOOKS_V1.md`  
7. ~~IDE hook event minimum set~~ → **done:** same doc (8-event min set)  
8. ~~Shareable-anchor policy~~ → **done:** `docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md` (`explicit_only`, Inv-Scope, unshare cascade)  
9. **Optional remaining:** Antigravity/Windsurf adapter tables; Biscuits grant tokens; PQ recipient defaults; at-rest DB encryption  
10. **Implementation Phase A** against locked schemas (private store, keys, remember/forget/status)  
11. **Implementation recipes from literature** → `docs/IMPLEMENTATION_FROM_LITERATURE.md` + `docs/research/impl/P1…P6_*.md` (deep-read driven; corpus seed ~783 arXiv IDs)

---

## 19. Canonical summary sentences

**Problem**

> Code is versioned; agent judgment is not.

**Store**

> Under compaction, only Anchors are guaranteed memory; everything else is ranked evidence around them.

**Runtime**

> Hooks observe; CLI engine cognifies; frequency is a property of layers, not a user lifestyle setting.

**Handoff**

> Handoff is a workstream-scoped relational **sealed** boot pack compiled from compact Anchors for continuity across sessions, branches, and **authorized** agents.

**Privacy**

> Continuity for task principals; non-discoverability for everyone else.

**Storage**

> Structured sealed packs preserve meaning; markdown is only an ephemeral render.

**Spine**

> `hooks → CLI engine → Anchor store/graph → seal handoff → authorize → hydrate`

---

## 20. Glossary

| Term | Meaning |
|------|---------|
| Anchor | Compact durable memory atom (decision/reject/constraint/etc.) |
| Evidence | Optional supporting snippet linked to an Anchor |
| Episode | Compressed chapter of work from a boundary |
| Workstream | Logical task thread that owns continuity |
| HandoffPack | Compiled boot image for next consumer |
| Kedger | Separate OSS memory/handoff product (`kedger` CLI) — not MoDeX |
| MoDeX | Separate hackathon product — keep brand/stack distinct from Kedger |
| `.kxp` | Sealed Kedger Pack envelope (encrypt + sign + structured payload) |
| Principal | Authenticated developer/agent identity that can hold capabilities |
| Capability | Grant to read/hydrate/append a workstream or pack |
| Cognify | Transform raw/working span into graph + anchors + episode |
| Hydrate | Authorized injection of ranked memory into a session |
| Compact-native | Designed to remain meaningful when storage/context is tight |
| Invalidation | Mark old Anchor inactive when superseded; preserve history |
| Ephemeral render | Temporary markdown/text view generated after auth; not source of truth |

---

## 21. Document maintenance

When architecture decisions change:

1. Update the relevant section here  
2. Add a short changelog entry below  
3. Do not keep critical locks only in chat  

### Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial synthesis from architecture/design conversation: problem framing, hooks+CLI lock, Anchor store lock, memory graph orchestration, handoff/workstream model, phased plan. |
| 2026-08-08 | Privacy/access lock: capability-gated handoffs, non-discoverability defaults, sealed `.kxp` packs, reject markdown as canonical storage, private user store layout, grant/revoke CLI, phase plan reordered for sealed handoff. |
| 2026-08-08 | Added §9A detailed runtime walkthrough: how L0–L4 and the temporal Anchor graph operate together on write, cognify, compact, and hydrate paths. |
| 2026-08-08 | Locked exact v1 record schemas in `docs/MEMORY_SCHEMAS_V1.md` (Observation→Capability, HandoffPack, `.kxp`, budgets, invariants). |
| 2026-08-08 | Locked workstream identity resolver + Anchor promotion signal catalog in `docs/WORKSTREAM_AND_PROMOTION_V1.md` (research-informed). |
| 2026-08-08 | Locked parallel compose operators + IDE hook event mapping in `docs/PARALLEL_COMPOSE_AND_HOOKS_V1.md`. |
| 2026-08-08 | Deep-read research pass: agent-memory corpus, sealed-pack crypto, shareable-anchor privacy (`docs/research/`); locked `.kxp` + shareable policy in `docs/SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md`. |
| 2026-08-08 | Pillar deep-read campaign for implementation clarity: `IMPLEMENTATION_FROM_LITERATURE.md` + `research/impl/P1–P6` (MemoryOS/MIRIX/MemOS/Graphiti/Mem0/…); ~783-ID survey seed inventoried for continued FULL expansion. |
| 2026-08-08 | **Product identity lock: Kedger** (`kedger`, `~/.kedger/`, `.kxp`, `kedger.memory.v1`). **Kedger ≠ MoDeX** — MoDeX stays a separate hackathon product; Kedger is not a rename. See §0A and `docs/KEDGER_NEW_REPO.md`. |
