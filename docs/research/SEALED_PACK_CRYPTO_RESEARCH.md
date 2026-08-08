# Research Memo: Sealed `.mxp` Crypto + Key UX for MoDeX

> **Date:** 2026-08-08  
> **Scope:** Library choice (libsodium vs age-compatible), seal pipeline, multi-recipient revoke, key UX.  
> **Method:** Deep-read of primary specs/docs/papers (full pages/PDFs), not keyword skim.  
> **Depends on:** `MEMORY_SCHEMAS_V1.md` algo intent (`X25519+XChaCha20Poly1305`, recipient-sealed-box, sender signature).

---

## 1. Honesty about coverage

| Source | Depth |
|--------|-------|
| C2SP `age.md` format spec | **Full** |
| FiloSottile/age README + keygen/PQ notes | **Full** |
| libsodium sealed boxes / `crypto_box` / Ed25519 signatures | **Full pages** |
| Magic Wormhole client-protocol + security docs | **Full** |
| MLS RFC 9420 (intro, Update/Remove, §16.6 FS/PCS) + RFC 9750 arch | **Substantial sections** (not entire RFC body) |
| Eclipse Biscuit intro + DESIGN + specifications | **Full** |
| Macaroons NDSS 2014 PDF | **Substantial** (construction + revocation sections) |
| Paragonie sealed-report recipe; Latacora right answers; Tink HybridEncrypt; Anderson robustness excerpt | **As listed** |
| Miller Capability Myths; Spritely ocaps | Covered in shareable-anchor memo; used for possession model |

---

## 2. Per-source mechanism insights

### 2.1 age format (C2SP)

- Two-layer file: header wraps a fresh **128-bit file key** for N recipients; payload encrypted under derived payload key.
- X25519 stanza: ephemeral share → shared secret → HKDF wrap of file key with ChaCha20-Poly1305 (fixed zero nonce for wrap).
- Payload STREAM: 64 KiB chunks, counter + last-chunk flag → truncation resistance.
- Header MAC over recipient list using file key — recipients who unwrap can authenticate the stanza set.
- `scrypt` passphrase stanza **must be alone** (cannot mix with pubkey recipients).
- PQ hybrid `mlkem768x25519` exists; mixing PQ + classical recipients on same file is discouraged.
- **No native sender signatures** — confidentiality/integrity under file key only.

### 2.2 libsodium sealed boxes / box / sign

- `crypto_box_seal`: anonymous send-to-pubkey; **sender authenticity is not provided**.
- Construction: X25519 + **XSalsa20**-Poly1305 (not XChaCha20).
- Single-recipient primitive; multi-recipient requires reinventing age’s file-key header.
- Sender cannot decrypt later (ephemeral sk wiped) — bad for “seal and keep a copy for myself” unless sender is also a recipient stanza.
- Ed25519 detached signatures fit archive envelopes; verifiers need TOFU/trusted pk store.
- Paragonie recipe for attributable sealed reports: **sign plaintext → seal** (StE), because AEAD provides encrypt-then-MAC inside.

### 2.3 Sign-then-encrypt engineering consensus

- Anderson: sign before encrypt so the signer is committed to plaintext knowledge.
- Tink HybridEncrypt: secrecy without sender authenticity — add signatures separately.
- Latacora: prefer boring NaCl/libsodium compositions over freelanced RSA.
- Nuance: EtS can provide public ciphertext authentication but risks “surrogate signer” / no plaintext awareness.
- **Recipient binding:** signed material should include sorted intended recipient ids to prevent surreptitious rewrap under attacker key without resigning.

### 2.4 Magic Wormhole (SPAKE2)

- Short code → high-entropy session key; default ~16-bit code ⇒ one online guess / 65536.
- Phases: PAKE → encrypted VERSION (key confirmation) → app messages; bulk via Transit.
- Ideal for **human-mediated first key exchange**, not for batch reseal of many packs.
- Metadata (size, timing, IPs) still leaks; mailbox is DoS-friendly.

### 2.5 MLS (RFC 9420) — steal semantics, not the tree

- Group keying with forward secrecy + post-compromise security via epochs.
- **Remove** = Commit that injects entropy into a new epoch secret unknown to the removed member.
- Critical mapping: **revoking a peer without resealing is theater**. Old ciphertext remains readable to anyone who already held a decrypt key.
- Architecture split: Authentication Service (identity↔keys) vs Delivery Service (fanout) ≈ MoDeX trust store vs USB/wormhole/git-LFS distribution.

### 2.6 Biscuits vs Macaroons (authorization, not encryption)

| | Macaroons | Biscuits |
|--|-----------|----------|
| Crypto | Nested HMAC; verifier holds root key | Ed25519 chain; verifier needs root **public** key |
| Attenuation | Append caveats offline | Append Datalog blocks offline |
| Revocation | TTL, freshness, external check, split credentials | Per-block revocation ids |
| Fit for MoDeX | Fast local ACL attenuation | Offline-verifiable grants across tools/CI |

Neither encrypts payload. Both gate **who may grant/reseal/hydrate**, complementary to `.mxp` AEAD.

---

## 3. Comparison: sealed box vs age multi-recipient wrap

| Dimension | libsodium `seal` | age multi-recipient |
|-----------|------------------|---------------------|
| Recipients | One per ciphertext | N stanzas, one file key |
| Sender auth | None | None (add Ed25519) |
| AEAD family | XSalsa20-Poly1305 | ChaCha20-Poly1305 STREAM |
| Matches schema “XChaCha20” | No | No |
| Streaming large packs | Whole message | Native 64 KiB STREAM |
| Passphrase path | DIY | First-class scrypt (exclusive) |
| PQ path | Not in seal API | Native hybrid + labels |
| Interop / vectors | libsodium | C2SP testkit |
| Revoke | Reseal new blob | Drop stanza + **new file key** |

**Conclusion:** sealed boxes are a *primitive*; age is a *file-format pattern*. MoDeX multi-recipient packs need the age pattern whether or not bytes are age-wire-compatible.

---

## 4. Threats crypto does / does not solve

**Does (if pipeline correct):** confidentiality vs non-recipients; ciphertext integrity; sender authenticity to parties trusting `pk_sender`; independent multi-recipient decrypt; PAKE-bootstrap online-guess limits.

**Does not:** revoke already-distributed ciphertext; FS across epochs without deleting old keys; malicious authorized recipient; TOFU wrong-key mistakes; metadata (size, recipient count, filenames); endpoint malware; authorization policy (“CI-only”); quantum threat without PQ hybrid; sender anonymity if headers name the signer.

---

## 5. Recommended v1 direction (feeds design lock)

1. **Age-shaped multi-recipient envelope** (file key + per-recipient wraps + STREAM/AEAD payload).
2. **Libsodium (or equivalent) primitives** if MoDeX insists on XChaCha20-Poly1305 exactly; treat full age wire-compat as optional.
3. **Ed25519 sign-then-encrypt** with domain-separated context binding `pack_id`, `epoch`, `sender_id`, `sorted_recipient_ids`.
4. **Revoke = reseal to new epoch** (MLS lesson); capability ACL alone is insufficient.
5. **Wormhole-like PAKE** for bootstrap key exchange only; thereafter static recipient files.
6. **Biscuits later** for attenuable grant tokens; v1 can use signed Capability records already in schemas.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial deep-read memo for `.mxp` crypto + key UX sources. |
