# Phase F — Deferred (Do Not Start Until C–E Green)

> **Status:** Specified, intentionally unimplemented in core  
> **Product:** Kedger  
> **Hard rule:** **Kedger ≠ MoDeX.** Phase F must not pull MoDeX hackathon demo stack (Fivetran, ADK theater, BigQuery bus, judge dashboards) into Kedger core.

Phases A–E (store → sealed packs → cognify → graph/promote/compose → hooks) are the v1 spine. This document freezes what Phase F may add later and what it must never become.

---

## 1. Allowed Phase F tracks

| Track | Intent | Invariants |
|-------|--------|------------|
| **MCP tools** | Optional adapter for agent tool APIs | Inv-Scope **404** on every tool; IDs ≠ capabilities; no ambient shared dump |
| **LLM episode distill** | Optional enrichment of Episode summaries | Deterministic cognify remains SoT; LLM never sole compressor; never LLM-every-turn |
| **Associative search UX** | Richer PPR / recognition retrieval | Budgeted; workstream-scoped; ranked hydrate laws unchanged |
| **Sync service** | Ciphertext + membership fanout | Sync sealed `.kxp` + ACL epochs only; no plaintext markdown SoT |
| **Community graph** | Cross-workstream / team facets | Share ladder stays `explicit_only` until a deliberate mode change |
| **At-rest DB encryption** | SQLCipher / OS keychain-wrapped store key | Keys remain under `~/.kedger/keys/`; no repo payloads |
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
- Renaming MoDeX → Kedger or branding Kedger as “MoDeX OSS / v2”  
- Markdown as canonical store or handoff format  
- Promoting every prompt to Anchor  
- Neo4j-required day-one infra  

---

## 3. Entry criteria before starting Phase F

1. Phases A–E merged or equivalently green on `main`  
2. PART D sealed-pack scenarios green  
3. Hook path still capability-gated after share policy changes  
4. No MoDeX demo dependencies introduced in A–E  

---

## 4. Suggested first Phase F slice (when authorized)

1. MCP read tools with Inv-Scope middleware (`anchors_get`, `hydrate`, `why`) — deny 404  
2. Optional `kedger cognify --llm-distill` behind a flag, default off  
3. SQLCipher optional store URI via `KEDGER_STORE_KEY` from OS keychain  

Do not begin those slices in this PR series.
