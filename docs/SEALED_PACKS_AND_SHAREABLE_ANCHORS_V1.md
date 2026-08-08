# Kedger Sealed Packs (`.kxp`) & Shareable Anchors v1

> **Status:** Design lock (deep-read, research-informed)  
> **Product:** Kedger  
> **Date:** 2026-08-08  
> **Depends on:** `OPEN_SOURCE_MEMORY_ARCHITECTURE.md`, `MEMORY_SCHEMAS_V1.md`, `WORKSTREAM_AND_PROMOTION_V1.md`, `PARALLEL_COMPOSE_AND_HOOKS_V1.md`  
> **Research memos:** `docs/research/SEALED_PACK_CRYPTO_RESEARCH.md`, `docs/research/SHAREABLE_ANCHOR_POLICY_RESEARCH.md`, `docs/research/CORPUS_INVENTORY.md`  
> **Honesty note:** Locks below come from **full deep-reads** of primary crypto/capability/privacy sources + agent-memory corpus memos — not keyword skim. See corpus inventory for FULL vs survey-indexed coverage.

---

## PART A — `.kxp` implementation choice + key UX

### A1. Library / format decision (locked)

| Choice | Decision |
|--------|----------|
| Envelope pattern | **Age-shaped multi-recipient file-key wrap** (N recipient stanzas → one file key → STREAM/AEAD payload) |
| Wire compatibility | **Kedger-native `.kxp`** for v1 (not required to decrypt with stock `age` CLI) |
| Primitives | **libsodium / libsodium-compatible**: X25519 recipient wrap, **XChaCha20-Poly1305** payload AEAD (matches schema intent), **Ed25519** signatures |
| Why not pure age bytes | age uses ChaCha20 (not XChaCha20) STREAM and has **no native signatures** |
| Why not raw `crypto_box_seal` alone | Single-recipient + anonymous (no sender auth) + no streaming multi-recipient header |

### A2. Seal pipeline (locked)

```text
plaintext payload P = structured HandoffPack JSON (schemas v1)
context C = canonical(
  schema_version, handoff_id, workstream_id, repo_fingerprint,
  epoch, created_at, from_principal_id, sorted(recipient_key_ids)
)

1. sig = Ed25519.Sign(sk_sender, domain_sep || C || hash(P))   # sign-then-encrypt
2. body = encode({ context: C, payload: P, signature: sig })
3. file_key = random(32)
4. ciphertext = XChaCha20-Poly1305 STREAM(file_key → body)    # chunked for large packs
5. for each recipient R_i:
     stanza_i = X25519_wrap(file_key → R_i.public_key)        # ephemeral per stanza
6. header_mac = MAC(header_without_mac, file_key)
7. .kxp = magic || header(stanzas, meta, header_mac) || ciphertext
```

**Open order:** unwrap file_key → verify header MAC → decrypt → verify Ed25519 against **trusted** sender pk → accept.

**Invariants:**
- Sender must also be listed as a recipient if they need to re-open their own pack later.
- Signed context binds recipients (anti rewrap without resign).
- Stanza ciphertext lengths checked before decrypt (partitioning-oracle hygiene from age).

### A3. Revocation / grant semantics (MLS lesson)

> **Revoke without reseal is theater.**

| Action | Required crypto effect |
|--------|------------------------|
| `kedger grant` | Add principal to workstream ACL **and** include their X25519 key on next seal |
| `kedger handoff --share` | Seal/reseal pack with current recipient set (new `file_key`, `epoch++`) |
| `kedger revoke` | Remove from ACL; **reseal** live packs excluding them; mark old epochs `superseded` |
| Device loss | Revoke device keys; issue new principal keys; reseal; accept that offline copies encrypted to lost device remain readable to thief |

Old `.kxp` files remain decryptable by anyone who still holds an old recipient private key. Product UX must say this clearly.

### A4. Key UX flows (locked for v1)

```text
kedger keys init                 # Ed25519 identity + X25519 recipient; store in OS keychain / passphrase-wrapped file
kedger keys export --recipient   # print/share age-like recipient string (mxp1… or age1… encoding TBD)
kedger keys import --from <file|wormhole>
kedger grant --workstream W --to <principal|recipient>
kedger revoke --workstream W --from <principal>
kedger handoff                   # compile + seal to current member recipient set
kedger hydrate --pack x.kxp      # unwrap if local sk ∈ recipients
```

| Flow | UX |
|------|-----|
| Bootstrap between two humans | Optional **Wormhole-style PAKE** code exchange for first recipient-key import; then static recipient roster |
| Team roster | `recipients.txt`-style file under private store (not git by default) |
| Offline USB | Passphrase-wrapped identity **or** encrypt pack to carried recipient key; not mixed scrypt+multi-recipient in one file (age rule) |
| CI / agent principal | Separate principal keys; attenuated Capability (read_hydrate only); never ambient admin |
| Passphrase-only pack | Allowed as exclusive mode for personal cold storage; not for multi-recipient team packs |

**Deferred (Phase F+):** Biscuits/Macaroons for attenuable offline grant tokens; PQ hybrid recipients; full MLS ratchet groups.

### A5. What crypto does not solve (product copy)

Document in `kedger doctor` / docs:
- Insider recipients can leak plaintext
- Metadata (size, recipient count, timestamps, filenames) is visible
- Unshare/revoke cannot erase already-hydrated ephemeral renders
- TOFU wrong-key import is user error — verify via known channel

---

## PART B — Shareable-anchor policy

### B1. Two ladders (locked)

```text
Ladder 1 — Anchorhood:     candidate → active Anchor (promotion Tier A/B/C)
Ladder 2 — Sharehood:      workstream_private → repo_shared_safe (shareable=true)
```

These are **orthogonal**. Becoming an Anchor never implies repo share.  
Invariant (schemas): `shareable=true` ⇒ `visibility=repo_shared_safe`.

### B2. Default share mode

```text
share_mode = explicit_only   # v1 default
```

| Signal | Auto → `repo_shared_safe`? |
|--------|----------------------------|
| Explicit `kedger share` / `remember … --shareable` | **Yes** (after redaction gate) |
| Recurrence ≥3 episodes (Tier B) | **No** — workstream only |
| Importance / reflection threshold | **Never** — candidates only |
| `goal` / `next_step` / `open_question` | **Never** |
| Secrets / PII / personal gotchas | **Hard deny** |
| Stable constraint/rejection + public code entities | **Candidate for human accept** only; optional later `conservative_auto` if seen in ≥2 workstreams |

### B3. Redaction gate before share

1. Kind allowlist: `constraint | rejection | decision | gotcha`  
2. Secret/PII scanners on statement, reason, entities, evidence  
3. **Detach Evidence** by default (keep capability-gated pointers)  
4. Normalize to durable code-facing sentence (ADR/QOC style)  
5. Retain provenance for audit; do **not** grant ambient read of origin workstream private siblings  
6. Run structural conflict/supersession against existing shared set **before** near-dup rejection (MemClaw ordering lesson)  
7. Emit `redaction_manifest` on the share event

### B4. Discoverability (Inv-Scope on every path)

From MemClaw live failure + Miller Property A:

1. Enforce visibility on **search, GET-by-id, hydrate, MCP, export** — not search-only.  
2. Deny with **404** (no existence oracle), not 403.  
3. Partition indexes: `private_raw` / `workstream_private` / `repo_shared_safe`.  
4. IDs are not capabilities.  
5. `kedger anchors --shared` lists only to repo-memory principals.  
6. Git opt-in: redacted statements only; never Evidence or packs by default.  
7. Pack compile includes shared Anchors only via **opt-in ranked facet**, budget-capped (anti PRISM amplification / pack deputy).

### B5. Unshare / revoke shared facet

| Step | Behavior |
|------|----------|
| `kedger unshare <id>` | Clear `shareable`; demote visibility; audit event |
| Facet model | Revoke **shared projection**; keep workstream-private source |
| Cascade | Drop shared embeddings, hydrate caches; mark packs stale; optional reseal notice |
| Prefer | `SUPERSEDES` + new shared Anchor over silent edit |
| Limit | Cannot erase already-decrypted `ephemeral_render` copies |

### B6. Confused-deputy mitigations

1. No ambient “all shared anchors” in agent tool env — purpose-bound capabilities.  
2. Scope check on GET-by-id (MemClaw regression test).  
3. Hub orchestrators get attenuated read facets (MAMA + Spritely).  
4. When private Anchor supersedes a shared one, co-promote supersession or mark shared stale.  
5. Never trust agent-inferred-alone share (confidence floor).

---

## PART C — Defaults to implement

```text
mxp.envelope = age_shaped_multi_recipient
mxp.payload_aead = XChaCha20-Poly1305-STREAM
mxp.recipient_wrap = X25519-HKDF
mxp.sign = Ed25519_sign_then_encrypt
mxp.recipient_binding = true
mxp.revoke = reseal_new_epoch
keys.bootstrap = keygen + optional_wormhole
keys.store = os_keychain_or_passphrase_wrap
share.mode = explicit_only
share.evidence_default = detach
share.deny_on_missing_capability = 404
share.pack_include = opt_in_ranked
```

---

## PART D — Validation scenarios

1. **Multi-recipient seal:** A seals to {A,B}; B hydrates; C with file copy cannot.  
2. **Revoke reseal:** Revoke B; reseal epoch+1; B opens old file still (documented), cannot open new.  
3. **Sign binding:** Attacker rewraps ciphertext to E without resign → signature/context fail.  
4. **Explicit share:** User shares constraint → appears in `--shared` for repo-memory principal.  
5. **Recurrence no-share:** Tier B recurrence does not flip `shareable`.  
6. **GET-by-id:** Outsider with gossiped id → 404.  
7. **Unshare cascade:** Shared index + new packs omit statement after unshare.  
8. **Pack deputy:** Compiler does not dump entire shared set into unrelated workstream pack.  
9. **Secret canary:** Token in episode never survives redaction gate.  
10. **Hook path:** `SESSION_START` hydrate still capability-gated after share policy changes.

---

## PART E — Still deferred

- Age CLI wire-compat mode / `age-inspect` interoperability  
- PQ hybrid recipients as default  
- Biscuits for offline attenuable grants  
- Full MLS groups for live multi-device sync  
- `share_mode=conservative_auto`  
- At-rest SQLCipher defaults (Phase F)

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial design lock for `.kxp` crypto/key UX and shareable-anchor policy from deep-read research memos. |
