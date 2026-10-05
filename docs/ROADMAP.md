# Kedger proveability roadmap

> **Status:** Stage 0 **done** (merged). Stage 1 **in motion** (ask pack + runbook; [`PEER_TRIALS.md`](PEER_TRIALS.md) rows 1–5 still empty). Stage 2 **started** ([`EVAL_EVIDENCE.md`](EVAL_EVIDENCE.md)).  
> **Product:** Kedger **0.2.6** beta (`pyproject.toml` + [PyPI](https://pypi.org/project/kedger/0.2.6/))  
> **Audience:** maintainers and strangers who should see the same tip truth as git/PyPI

This is the **go-ahead plan** for community proveability. It is not a feature wishlist and not a substitute for [`CHANGELOG.md`](../CHANGELOG.md) or [`PHASE_F_DEFERRED.md`](PHASE_F_DEFERRED.md).

---

## Thesis

Kedger is **judgment handoff**, not an ambient wiki.

The object that must survive compact and travel to the next agent is compact-native **Anchors** (decisions, rejects, constraints) plus ops, sealed into a recipient-bound **`.kxp`**. Share stays **`explicit_only`**: someone chooses to send a pack. Same-person device transfer is a separate file (`.kxs`), not a team brain.

If a design does not make Alice→Bob (or you-tomorrow) hydrate with the *why*, it is out of scope for this roadmap.

## Current state (through 0.2.6)

Mechanical proof is **strong**: CI, strict handoff evals, smoke scripts (`smoke_transfer`, `smoke_peer_handoff`, `smoke_wheel_install`, `smoke_prompt_inject`). Phase A–E spine is on `main`. Phase F is **partial** (opt-in SQLCipher + keychain + encrypted `raw/` + transcript sidecars; opt-in LLM distill; sync export/import). Live sync service is still deferred. Public eval pointer: [`EVAL_EVIDENCE.md`](EVAL_EVIDENCE.md) (mechanical proof, not a field study — no invented SLI numbers).

Field proveability is **not**. [`PEER_TRIALS.md`](PEER_TRIALS.md) rows 1–5 are empty. That gap does not close by shipping more Phase F or by growing the research corpus. Recruitment copy: [`PEER_ASK_PACK.md`](PEER_ASK_PACK.md).

**Gate:** human peer trials + claim hygiene. Not more encryption slices, not more papers.

**Still true (do not walk back):**

- Beta OSS, not “proven in production”
- Mechanical tests ≠ published user study
- Revoke does **not** erase old offline `.kxp` copies
- Plaintext SQLite remains the **default**; SQLCipher is opt-in
- Inline episode JSON in SQLite is still plaintext even when sidecars encrypt

---

## Stages

### Stage 0 — Tip / claim alignment (**done**)

Merged: strangers reading README / Marketing / Publish / Contributing see the **same tip** as `pyproject.toml` and PyPI: **0.2.6**. Claim shipped Phase F **slices**; do not claim live sync, full Phase F, or a field study.

Unlocks Stage 1 by stopping the “is 0.2.0 still pending?” confusion that makes dogfood asks look unshipped.

### Stage 1 — Five human peer trials (**in motion**)

Run five real Cursor/Claude `peer card` → `peer send` → send `.kxp` → `peer open` → `hydrate --live` loops.

- Maintainer sequence: [`PEER_TRIAL_RUNBOOK.md`](PEER_TRIAL_RUNBOOK.md)
- Copy-paste recruitment (DM, Windows addendum, LinkedIn pin, Discussion draft): [`PEER_ASK_PACK.md`](PEER_ASK_PACK.md)
- Fill rows 1–5 in [`PEER_TRIALS.md`](PEER_TRIALS.md) — **still empty**; do not invent rows
- File every break via the [peer handoff](https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml) template
- Prefer a break issue over a silent star

**Exit:** five filled rows (pass or fail-with-issue). Mechanical M1–M5 already count as CI dogfood, not as these five.

### Stage 2 — Eval SLI evidence + install→hydrate DX (**started**)

Stage 1 is in motion (ask pack + runbook; human rows still empty). Publish what CI already measures so a stranger can reproduce “mechanical proof” without spelunking.

- **Started:** public evidence page [`EVAL_EVIDENCE.md`](EVAL_EVIDENCE.md) — points at [`research/EVAL_HARNESS.md`](research/EVAL_HARNESS.md) / `tests/eval/` / `artifacts/eval/slis.jsonl` (reproduce via `pytest`; do not invent SLI numbers)
- Remaining: harden **install → init → hooks → doctor-clean → hydrate** so a new machine gets a green doctor without folklore
- Keep DX changes fail-soft (hooks must not block prompts)

### Stage 3 — Product bets (only after Stage 1 green)

Do not start product bets to paper over empty trial rows.

| Bet | When | Not |
|-----|------|-----|
| MCP `why` (beyond `hydrate` / `anchors_get`) | Stage 1 green **and** an SLI/break demands pull-not-push | MCP-as-primary |
| Hydrate quality (packing, surface-k, retrieve) | Stage 1 green + eval regress or peer “hydrate was noise” | Vector DB / GraphRAG rebuilds |
| Live sync protocol | Explicitly **deferred** — `.kxs` export/import is the slice | Cloud bus, ambient team sync |

---

## Explicit non-goals

Stay out of core, and do not treat these as proveability work:

- Ambient share / `conservative_auto` as default
- Neo4j-as-brain (SQLite + edges remain v1)
- LLM-every-turn distill (heuristics stay SoT; `--llm-distill` stays opt-in)
- Wiki-as-SoT (markdown in git is not memory)
- More research-corpus volume as a substitute for field proof
- “Encrypted by default” / full at-rest of every inline blob
- Claiming revoke wipes offline packs

---

## Proof artifacts

What “Kedger is proveable” looks like on disk.

| Artifact | Role | Status at 0.2.6 |
|----------|------|-----------------|
| Filled [`PEER_TRIALS.md`](PEER_TRIALS.md) rows 1–5 | Human Alice→Bob (or equivalent) | Empty — Stage 1 in motion (ask pack + runbook; no invented rows) |
| Redacted hydrate before/after | Show cold start vs post-open hydrate without leaking secrets | Not published |
| Inject verify dumps | SessionStart vs per-prompt inject — [`PROMPT_INJECT_VERIFY.md`](PROMPT_INJECT_VERIFY.md) | Checklist exists; no public dumps |
| Eval SLIs | `tests/eval/` + `artifacts/eval/slis.jsonl` | Measured in CI; public pointer [`EVAL_EVIDENCE.md`](EVAL_EVIDENCE.md) — mechanical proof, not a field study |
| Doctor-clean install | `pip install` → `kedger init` → `kedger doctor` with no `[fail]` | Smoke exists; Windows PATH is a known warn (0.2.6) |
| Dogfood-on-self | Maintainer uses Kedger on this repo | Configs present (`.cursor/hooks.json`); not a published log |
| Tip version matrix | Git / PyPI / GitHub Release agree | Git + PyPI **0.2.6**; GitHub Release latest still **v0.2.0**; notes drafted [`RELEASES/v0.2.6.md`](../RELEASES/v0.2.6.md); PyPI **skipped 0.2.2**. `release.yml` skips Publish when the version is already on PyPI — tag `v0.2.6` after that skip is on `main`. |

---

## Pointers

| Doc | Role |
|-----|------|
| [`CHANGELOG.md`](../CHANGELOG.md) | What shipped, including honest gaps |
| [`RELEASES/v0.2.6.md`](../RELEASES/v0.2.6.md) | GitHub Release body for the PyPI tip (tag deferred) |
| [`PHASE_F_DEFERRED.md`](PHASE_F_DEFERRED.md) | Phase F slices vs remaining deferrals |
| [`PUBLISH.md`](PUBLISH.md) | PyPI matrix + claim guardrails |
| [`MARKETING.md`](MARKETING.md) | Positioning + public-copy locks |
| [`PEER_ASK_PACK.md`](PEER_ASK_PACK.md) | Stage 1 copy-paste recruitment |
| [`PEER_TRIAL_RUNBOOK.md`](PEER_TRIAL_RUNBOOK.md) | Stage 1 maintainer sequence |
| [`PEER_TRIALS.md`](PEER_TRIALS.md) | Stage 1 log (rows 1–5 empty) |
| [`EVAL_EVIDENCE.md`](EVAL_EVIDENCE.md) | Stage 2 mechanical eval pointer |
| [`IMPLEMENTATION_STATUS.md`](IMPLEMENTATION_STATUS.md) | Landed surface |
