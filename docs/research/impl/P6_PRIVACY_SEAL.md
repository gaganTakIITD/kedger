# P6 — Privacy / Seal (Implementation Clarity)

> **Date:** 2026-08-08  
> **Pillar:** Capabilities + Inv-Scope + shareable promotion + `.mxp` crypto + key UX  
> **Depends on:** `SEALED_PACKS_AND_SHAREABLE_ANCHORS_V1.md`, `SHAREABLE_ANCHOR_POLICY_RESEARCH.md`, `SEALED_PACK_CRYPTO_RESEARCH.md`, schemas §9–12  
> **Method:** Full-body deep-reads of primary HTML/PDF/RFC/spec texts. New vs prior memos marked ★.

---

## 1. Honesty table

| Bucket | Count | Notes |
|--------|------:|-------|
| **FULL deep-read** (this pillar pass) | **22** | Papers + specs/PDFs with full bodies |
| Re-deep from prior shareable/crypto memos | 10 | MemClaw, AgentLeak, CollabMem, PRISM, MemLeak, Miller, age, libsodium, Wormhole, MLS |
| ★ New FULL this pass | 12 | MAMA arXiv, ConfAIde, CaMeL, Fides, SSE leakage, DP-RAG, MRMMIA, Biscuits, SPKI, SQLCipher, Macaroons PDF, + CaMeL/Fides PDFs |
| Abstract-only | 0 counted as FULL | |
| **Combined with P5 FULL this session** | **≥48** | See inventory |

### FULL ledger (P6)

| ID / Source | Title | ★ |
|-------------|-------|---|
| 2606.24535 | MemClaw / Governed Shared Memory | re-deep |
| 2602.11510 | AgentLeak | re-deep |
| 2505.18279 | Collaborative Memory | re-deep |
| 2605.10614 | PRISM | re-deep |
| 2606.29788 | MemLeak | re-deep |
| 2512.04668 | Topology Matters (MAMA) | ★ arXiv FULL |
| 2310.17884 | ConfAIde (Can LLMs Keep a Secret?) | ★ |
| 2503.18813 | CaMeL — Defeating Prompt Injections by Design | ★ PDF FULL |
| 2505.23643 | Fides — Securing AI Agents with IFC | ★ PDF FULL |
| — | Capability Myths Demolished (Miller et al.) | re-deep PDF |
| — | Macaroons (NDSS 2014) | re-deep PDF |
| biscuit DESIGN.md | Biscuits authorization | FULL |
| C2SP age.md | age format | FULL |
| libsodium docs | sealed box / box / sign | FULL |
| RFC 9420 | MLS | Substantial→FULL sections used |
| RFC 2693 | SPKI Certificate Theory | FULL |
| Magic Wormhole docs | PAKE bootstrap | FULL |
| 2309.04697 | Leakage-Abuse Attacks on SSE | ★ |
| 2510.06719 | DP Synthetic Text for RAG | ★ |
| 2605.27825 | MRMMIA (membership inference on memory) | ★ |
| SQLCipher README/design | Encrypted SQLite | ★ |
| VAULT / Spritely | Via prior shareable memo + design lock | prior FULL |

---

## 2. Mechanism cards (FULL)

### 2.1 MemClaw (2606.24535) — Inv-Scope

- Fleet memory \(M=(A,S,G,P,T)\). Write carries `(agent, content, scope, time, provenance)`.
- **Inv-Scope:** no agent receives a row outside `auth(agent, G, scope)`.
- Four failures: unauthorized leakage, stale propagation, contradiction persistence, provenance collapse.
- Live bug: **GET-by-id ignored sub-tenant scope** after identity resolve (confused deputy). Fix: **404**, not 403.
- Pipeline must be: candidates → **policy on every path** → temporal resolve → provenance → rank.
- Near-dup gate must not starve supersession (ordering).

### 2.2 AgentLeak (2602.11510) — channel matrix

- Seven leakage channels; **internal** dominate: inter-agent messages ~68.8% vs final output ~27.2%; shared memory ~46.7%.
- Data minimization: vault \(\mathcal{V}\), allowed \(\mathcal{A}\); leak iff \(v\notin\mathcal{A}\) appears in **any** channel.
- **MoDeX:** Hydrate → agent message → tool artifact is a distinct surface; `repo_shared_safe` ≠ “safe in all channels.”

### 2.3 Collaborative Memory (2505.18279)

- \(M_{\mathrm{private}}\cup M_{\mathrm{shared}}\); immutable provenance; bipartite user–agent / agent–resource graphs; separate \(\pi^{\mathrm{write/private}}\), \(\pi^{\mathrm{write/shared}}\), \(\pi^{\mathrm{read}}\).
- Closest academic twin of MoDeX promotion ladder.

### 2.4 PRISM (2605.10614)

- Propagation amplification across agent boundaries; generation-time risk scoring ≫ post-hoc scrub.
- **MoDeX:** Redaction/share gates at promote/compile time; don’t dump full shared set into packs.

### 2.5 MemLeak (2606.29788)

- Delete ≠ forget; residual via correlated text (~18%) and images (~12%); need provenance-cascaded tombstones.
- **MoDeX unshare:** cascade embeddings, hydrate caches, pack staleness — not boolean flip.

### 2.6 MAMA / Topology Matters (2512.04668) ★

- Leakage rises with density, short attacker–target distance, target centrality; early rounds dominate.
- Prefer sparse/hierarchical topologies; restrict hubs.
- **MoDeX:** CI/orchestrator principals get attenuated `read_hydrate` only; no hub with ambient all-shared search.

### 2.7 ConfAIde (2310.17884) ★

- Contextual integrity tiers for LLM secrecy; models leak when social norms vs utility conflict.
- **MoDeX:** Recurrence/importance never alone cross share boundary (contextual inappropriateness).

### 2.8 CaMeL (2503.18813) ★

- Extract **control + data flows** from trusted user query; untrusted tool/memory data cannot hijack control flow.
- Capabilities (security sense) on values; policies enforced at tool calls via custom interpreter; 77% AgentDojo tasks with provable security.
- **MoDeX:** Treat hydrated memory as **untrusted data plane** relative to tool side-effects; purpose-bound Capabilities on pack open / tool write; never let retrieved Anchor text become ambient authority to `send_email`/`git push`.

### 2.9 Fides (2505.23643) ★

- Planner IFC: confidentiality + integrity labels; policy engine allow/deny consequential actions; selective hide/reveal primitives; deterministic vs probabilistic PIA defenses.
- **MoDeX:** Map visibility classes → confidentiality labels; capability permissions → integrity/action policy. Pack plaintext inherits label of most sensitive included row; seal does not lower label for non-recipients.

### 2.10 Miller Capability Myths

- **Property A:** No designation without authority (id ≠ capability).  
- **Property D:** No ambient authority.  
- Revocation via forwarders/caretakers works; confused deputy cured when capability *is* the designator.

### 2.11 Macaroons (NDSS 2014)

- Nested HMAC caveats; attenuation offline; discharge for third-party caveats; TTL/freshness/revocation patterns.
- AuthZ only — complements `.mxp` encryption.

### 2.12 Biscuits

- Ed25519 block chain; Datalog attenuation; offline verify with root **public** key; per-block revocation ids.
- Better cross-tool/CI story than Macaroons for MoDeX Phase F+.

### 2.13 age (C2SP)

- File key + N recipient stanzas; STREAM 64 KiB chunks; header MAC; scrypt exclusive; no native signatures.
- Pattern for MoDeX multi-recipient `.mxp`.

### 2.14 libsodium

- `crypto_box_seal`: anonymous, single-recipient, XSalsa20-Poly1305 — no sender auth.  
- Signatures: Ed25519 detached.  
- StE (sign-then-encrypt) for attributable sealed payloads.

### 2.15 MLS RFC 9420

- Group epochs; Remove = Commit with new entropy → FS/PCS.  
- **Revoke without reseal is theater.**

### 2.16 SPKI RFC 2693

- Auth certs vs ACLs; local names; delegation chains; subject presents proof.
- Aligns with signed Capability records in schemas §9.

### 2.17 Magic Wormhole

- SPAKE2 short code → session key; bootstrap only; metadata still leaks; mailbox DoS-friendly.

### 2.18 SSE leakage-abuse (2309.04697) ★

- Even “forward/backward private” searchable encryption leaks via volume/access patterns; attacks recover keywords.
- **MoDeX:** Do **not** build encrypted semantic search over ciphertext as v1 security boundary. Partition plaintext indexes by visibility **under** process that already passed Inv-Scope; seal packs for transit/at-rest handoff.

### 2.19 DP synthetic text for RAG (2510.06719) ★

- DP synthetic corpora can reduce memorization in RAG training/indexing settings.
- **MoDeX v1:** Out of scope for local engineering memory; optional later for published shared corpora. Not a substitute for capabilities.

### 2.20 MRMMIA (2605.27825) ★

- Membership inference against chat-agent memory stores.
- **MoDeX:** 404 on deny; constant-time-ish absence; don’t return “exists but forbidden”; rate-limit id probes; minimize pack metadata.

### 2.21 SQLCipher ★

- Page-level AES; PBKDF2; per-page HMAC; encrypts DB files at rest.
- **MoDeX:** Optional for local `store.sqlite` cold disk; **orthogonal** to `.mxp` (handoff) and Inv-Scope (API). SQLCipher does not enforce workstream membership.

---

## 3. MoDeX implementation recipe — seal pipeline

Aligned with design lock Part A; expanded to runnable pseudocode.

### 3.1 Keys

```text
Principal:
  sk_sign, pk_sign   # Ed25519 identity
  sk_box,  pk_box    # X25519 recipient
Store: OS keychain or passphrase-wrapped key file
Export: recipient string only by default
```

### 3.2 Seal pseudocode

```python
DOMAIN = b"modex.mxp.v1"

def seal_mxp(payload: HandoffPack, sender: Principal, recipients: list[Principal]) -> bytes:
    assert sender in recipients  # keep a copy for yourself
    P = canonical_json(payload)
    content_hash = sha256(P)

    C = canonical_json({
        "schema_version": "modex.pack.v1",
        "handoff_id": payload.id,
        "workstream_id": payload.workstream_id,
        "repo_fingerprint": payload.repo_fingerprint,
        "epoch": payload.epoch,
        "created_at": payload.created_at,
        "from_principal_id": sender.id,
        "recipient_key_ids": sorted(r.id for r in recipients),
        "content_hash": content_hash.hex(),
    })

    # Sign-then-encrypt (Anderson / Paragonie / design lock)
    sig = ed25519_sign(sender.sk_sign, DOMAIN + C + content_hash)

    body = canonical_msgpack({
        "context": C,
        "payload": payload,          # structured HandoffPack
        "signature": sig,
    })

    file_key = random_bytes(32)      # age-shaped
    ciphertext = xchacha20poly1305_stream_encrypt(file_key, body)  # 64KiB chunks

    stanzas = []
    for r in recipients:
        eph_sk, eph_pk = x25519_keypair()
        shared = x25519(eph_sk, r.pk_box)
        wrap_key = hkdf(shared, info=b"modex-mxp-wrap-v1", length=32)
        wrapped = aead_encrypt(wrap_key, nonce=zeros(24), plaintext=file_key)
        stanzas.append({"recipient": r.id, "eph_pk": eph_pk, "wrapped_key": wrapped})

    header = {
        "magic": "MXP1",
        "algo": {
            "encrypt": "X25519+XChaCha20Poly1305",
            "sign": "Ed25519",
            "kdf": "recipient-sealed-box",
            "hash": "sha256",
        },
        "stanzas": stanzas,
        "meta": json.loads(C),
    }
    header_mac = mac(file_key, canonical_json({k: header[k] for k in header if k != "header_mac"}))
    header["header_mac"] = header_mac

    return encode_mxp(header, ciphertext)


def open_mxp(blob: bytes, opener: Principal, trust_store: TrustStore) -> HandoffPack:
    header, ciphertext = decode_mxp(blob)
    stanza = find_stanza(header, opener.id)
    if stanza is None:
        raise Forbidden404()  # no existence oracle beyond local file

    shared = x25519(opener.sk_box, stanza["eph_pk"])
    wrap_key = hkdf(shared, info=b"modex-mxp-wrap-v1", length=32)
    file_key = aead_decrypt(wrap_key, stanza["wrapped_key"])
    verify_mac(file_key, header)

    body = xchacha20poly1305_stream_decrypt(file_key, ciphertext)
    sender_pk = trust_store.get(body["context"]["from_principal_id"])
    ed25519_verify(sender_pk, DOMAIN + body["context"] + sha256(canonical_json(body["payload"])),
                   body["signature"])

    # Recipient binding
    assert sorted(header["meta"]["recipient_key_ids"]) == sorted(json.loads(body["context"])["recipient_key_ids"])

    payload = body["payload"]
    # Still enforce Inv-Scope after decrypt (defense in depth)
    assert inv_scope(opener, payload)
    return payload
```

### 3.3 Revoke / reseal (MLS lesson)

```python
def revoke_and_reseal(ws, removed: Principal):
    ws.acl.remove(removed)
    ws.epoch += 1
    live = load_head_pack(ws)
    recipients = current_recipient_set(ws)  # excludes removed
    new_pack = seal_mxp(live.payload.with_epoch(ws.epoch), ws.owner, recipients)
    mark_epoch_superseded(ws, live.epoch)
    write_head(ws, new_pack)
    # Old .mxp files remain decryptable by removed if they kept sk — document this
```

### 3.4 What crypto does not solve

Insider recipients, metadata (size, recipient count), already-hydrated `ephemeral_render`, TOFU wrong keys, quantum (without PQ hybrid), authorization policy (needs Capabilities / Biscuits).

---

## 4. MoDeX implementation recipe — Inv-Scope middleware

### 4.1 Visibility → auth

```text
private_raw         → principal == owner OR admin  (never search-default)
workstream_private  → membership(ws) ∧ capability(read_*)
repo_shared_safe    → repo_memory_principal ∧ capability(repo_shared|read)
ephemeral_render    → session principal only; TTL
```

IDs are **not** capabilities (Miller A; MemClaw GET-by-id).

### 4.2 Middleware pseudocode

```python
# Apply to: search, list, GET-by-id, hydrate, MCP tools, export, pack compile

@dataclass
class AuthContext:
    principal_id: str
    capabilities: list[Capability]  # verified signatures, not expired/revoked
    repo_fingerprint: str

def inv_scope(ctx: AuthContext, row) -> bool:
    if row.repo_fingerprint != ctx.repo_fingerprint:
        return False
    vis = row.visibility

    if vis == "private_raw":
        return row.owner_principal_id == ctx.principal_id or has_perm(ctx, "admin")

    if vis == "workstream_private":
        return (
            is_member(ctx, row.workstream_id)
            and has_cap(ctx, scope=("workstream", row.workstream_id),
                       perms={"read_hydrate", "append", "admin"})
        )

    if vis == "repo_shared_safe":
        return (
            row.shareable is True
            and has_cap(ctx, scope=("repo_shared",), perms={"read_hydrate", "repo_shared"})
        )

    if vis == "ephemeral_render":
        return row.session_principal_id == ctx.principal_id and not row.expired()

    return False


def require_row(ctx, row_id, loader):
    row = loader.unchecked_get(row_id)  # internal
    if row is None or not inv_scope(ctx, row):
        raise HTTPException(404, "not found")  # never 403 for existence
    return row


def search(ctx, query, tier: str):
    # Partitioned indexes — do not query foreign tiers then filter
    idx = index_for(tier)
    hits = idx.search(query, filter=prefilter_for(ctx, tier))
    return [h for h in hits if inv_scope(ctx, h)]  # defense in depth


def hydrate(ctx, pack_path):
    # Path 1: sealed recipient
    if pack_path:
        payload = open_mxp(read(pack_path), ctx.principal, trust_store)
        # open_mxp already checks recipient stanza + Inv-Scope
        return render_ephemeral(payload, ttl=SESSION_TTL)

    # Path 2: live compile
    if not has_cap(ctx, scope=("workstream", ctx.ws), perms={"read_hydrate"}):
        raise HTTPException(404, "not found")
    pack = compile_handoff(ctx.ws, ctx.principal)  # P5 — filters Inv-Scope internally
    return render_ephemeral(pack, ttl=SESSION_TTL)
```

### 4.3 CaMeL / Fides overlay for tool calls

```python
def tool_call(ctx, tool, args, memory_citations: list[Row]):
    # Labels from Fides-style IFC
    conf = max_confidentiality(memory_citations + args)
    integ = min_integrity(memory_citations + args)

    # CaMeL: control flow from trusted user intent; memory is data
    if tool.side_effect in {"network_send", "repo_write_public", "exfil_channel"}:
        if conf > allowed_sink[tool] or integ < required_integrity[tool]:
            deny()
        if not purpose_capability(ctx, tool):  # attenuated facet
            deny()
    return execute(tool, args)
```

---

## 5. MoDeX implementation recipe — share redaction pipeline

Two ladders remain orthogonal (design lock B1). Default `share_mode=explicit_only`.

### 5.1 Redaction pipeline pseudocode

```python
ALLOWED_KINDS = {"constraint", "rejection", "decision", "gotcha"}

def share_anchor(ctx, anchor_id, mode="explicit"):
    a = require_row(ctx, anchor_id, loader)  # workstream_private source
    assert has_cap(ctx, scope=("workstream", a.workstream_id), perms={"admin", "share"})

    if mode != "explicit" and share_mode != "conservative_auto":
        raise PolicyDeny("share_mode=explicit_only")

    # 1) kind allowlist
    if a.kind not in ALLOWED_KINDS:
        raise PolicyDeny("kind not shareable")

    # 2) secret / PII scanners
    blob = a.statement + "\n" + (a.reason or "") + "\n" + " ".join(entity_names(a))
    findings = run_secret_scanners(blob) + run_pii_scanners(blob)
    if findings:
        raise PolicyDeny("redaction_failed", findings=findings)

    # 3) detach Evidence by default
    evidence_ids = a.evidence_ids
    a_shared = copy(a)
    a_shared.evidence_ids = []          # pointers only if policy allows later
    a_shared.visibility = "repo_shared_safe"
    a_shared.shareable = True

    # 4) normalize to durable code-facing sentence (ADR/QOC)
    a_shared.statement = normalize_decision_sentence(a.statement)
    a_shared.reason = truncate(a.reason, 480)

    # 5) structural conflict BEFORE near-dup (MemClaw ordering)
    conflicts = find_shared_conflicts(a_shared)
    if conflicts:
        resolve_or_supersede(conflicts, a_shared)  # may require human

    # 6) AgentLeak allowed-set: only continuity fields
    allowed = project_allowed_fields(a_shared, ALLOWED_SHARE_FIELDS)
    deny_if_extra_fields(a_shared, allowed)

    # 7) write shared facet (caretaker) — keep private source
    facet = issue_shared_facet(source_id=a.id, body=allowed)
    index_shared.add(facet)
    audit("share", actor=ctx.principal_id, anchor=a.id, manifest=redaction_manifest(...))
    return facet


def unshare_anchor(ctx, anchor_id):
    a = require_row(ctx, anchor_id, loader)
    revoke_shared_facet(a.id)                 # Miller caretaker
    a.shareable = False
    a.visibility = "workstream_private"
    index_shared.delete(a.id)
    hydrate_cache.invalidate(anchor_id=a.id)
    mark_packs_stale(referencing=a.id)        # MemLeak cascade
    # optional: reseal notice to capability holders
    audit("unshare", ...)
```

### 5.2 Pack compile interaction (anti pack-deputy / PRISM)

```text
shared_facet_include =
  opt_in
  ∧ relevance-ranked under S(x)
  ∧ sub-budget ≤ 8 KiB (boot) / 0 for ci_bot unless allowlisted
  ∧ never auto-include entire repo_shared_safe set
```

---

## 6. Anti-patterns

| Anti-pattern | Source | MoDeX response |
|--------------|--------|----------------|
| Filter scope on search only | MemClaw | Middleware on **all** paths |
| 403 on deny | MemClaw / MRMMIA | **404** |
| Encrypted search as ACL | SSE attacks | Partition plaintext indexes + Inv-Scope |
| Revoke ACL without reseal | MLS | reseal new epoch |
| Raw `crypto_box_seal` multi-recipient | libsodium | age-shaped file key |
| Encrypt without sign / sign after encrypt blindly | StE literature | Sign-then-encrypt + recipient binding |
| Auto-share on reflection/recurrence | ConfAIde / GenAgents | explicit_only |
| Hub orchestrator with full shared search | MAMA | attenuated facets |
| SQLCipher alone as multi-tenant security | SQLCipher scope | disk encryption ≠ Inv-Scope |
| Post-hoc output scrubbing only | PRISM / AgentLeak | promote-time + channel matrix tests |

---

## 7. Open risks

1. Biscuits/Macaroons attenuation grammar for MoDeX Capability v1 vs signed JSON records.  
2. PQ hybrid recipient stanzas (age mlkem768x25519) — deferred.  
3. Residual membership signal via pack size metadata.  
4. Fides-level IFC in IDE agents requires tool broker integration beyond CLI.  
5. DP for shared public dumps — product decision, not v1 core.

---

## 8. Validation scenarios (implement as tests)

1. Multi-recipient seal/open; outsider with file copy fails.  
2. Revoke + reseal; old epoch documented still openable; new not.  
3. Rewrap without resign → fail.  
4. GET-by-id gossip → 404.  
5. Search partition: private never in shared index.  
6. Share redaction blocks secret canary.  
7. Unshare cascades cache + stale packs.  
8. Pack deputy cannot include full shared set.  
9. CaMeL-style: hydrated private fact cannot authorize external send tool.  
10. Topology: star orchestrator with attenuated cap cannot escalate.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-08 | Initial P6 implementation memo from 22 FULL deep-reads + seal / Inv-Scope / redaction recipes. |
