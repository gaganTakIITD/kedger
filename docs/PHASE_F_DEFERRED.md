# Phase F — Deferred (Do Not Start Until C–E Green)

> **Status:** Phase F **in progress** — at-rest encryption + OS keychain key shipped in 0.2.1–0.2.2  
> **Product:** Kedger  
> **Hard rule:** Phase F must not pull external demo stacks (Fivetran, ADK theater, BigQuery bus, judge dashboards) into Kedger core.

Phases A–E (store → sealed packs → cognify → graph/promote/compose → hooks) are the v1 spine. This document freezes what Phase F may add later and what it must never become.

### 0.2.1–0.2.2 shipped (at-rest encryption slices)

| Item | Status |
|------|--------|
| **At-rest DB encryption** | **Shipped (opt-in)** — SQLCipher via `kedger store encrypt` / `init --encrypt-store` |
| **OS keychain store key** | **Shipped (0.2.2)** — keyring default; env/file fallback; `--key-file` for headless |
| MCP tools (full Phase F) | Partial — `hydrate` / `anchors_get` only (0.2.0) |
| LLM episode distill | Not started |
| Sync service | Not started |

Plaintext SQLite remains the **default** for upgrade compatibility until operators opt in.

---

## 1. Allowed Phase F tracks

| Track | Intent | Invariants |
|-------|--------|------------|
| **MCP tools** | Optional adapter for agent tool APIs | Inv-Scope **404** on every tool; IDs ≠ capabilities; no ambient shared dump |
| **LLM episode distill** | Optional enrichment of Episode summaries | Deterministic cognify remains SoT; LLM never sole compressor; never LLM-every-turn |
| **Associative search UX** | Richer PPR / recognition retrieval | Budgeted; workstream-scoped; ranked hydrate laws unchanged |
| **Sync service** | Ciphertext + membership fanout | Sync sealed `.kxp` + ACL epochs only; no plaintext markdown SoT |
| **Community graph** | Cross-workstream / team facets | Share ladder stays `explicit_only` until a deliberate mode change |
| **At-rest DB encryption** | SQLCipher + OS keychain-wrapped store key | **0.2.1–0.2.2:** opt-in SQLCipher; keyring default with env/file fallback |
| **Biscuits / Macaroons** | Attenuable offline grant tokens | Complements Capabilities; does not replace `.kxp` AEAD |
| **PQ hybrid recipients** | Post-quantum recipient stanzas | Age-shaped multi-recipient pattern preserved |
| **Age CLI wire-compat** | Optional interop mode | Kedger-native `.kxp` remains default |
| **`share_mode=conservative_auto`** | Opt-in later | Default remains **`explicit_only`**; never recurrence-alone share |

---

## 2. Explicit non-goals (stay out of Kedger core)

- Fivetran connectors / Sheet mirrors  
- Google ADK multi-agent “specialist theater”  
- BigQuery as required memory bus  
- Hackathon judge dashboards / credential packs  
- External demo buses or judge dashboards as required dependencies  
- Markdown as canonical store or handoff format  
- Promoting every prompt to Anchor  
- Neo4j-required day-one infra  

---

## 3. Entry criteria before starting Phase F

1. Phases A–E merged or equivalently green on `main`  
2. PART D sealed-pack scenarios green  
3. Hook path still capability-gated after share policy changes  
4. No external demo-stack dependencies introduced in A–E  

---

## 4. Suggested first Phase F slice (when authorized)

1. MCP read tools with Inv-Scope middleware (`anchors_get`, `hydrate`, `why`) — deny 404 — **partial (0.2.0)**
2. Optional `kedger cognify --llm-distill` behind a flag, default off — **not started**
3. SQLCipher optional store with OS keychain key (`KEDGER_STORE_KEY` / keyring / `~/.kedger/keys/store.key`) — **shipped opt-in (0.2.1–0.2.2)**

Remaining Phase F tracks (sync, community graph, biscuits, PQ hybrid, etc.) are still deferred.
