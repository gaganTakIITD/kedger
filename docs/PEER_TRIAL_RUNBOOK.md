# Peer trial runbook (maintainer)

> **Stage 1 prep** — how to run the five human Alice→Bob trials without folklore.  
> **Log:** [`PEER_TRIALS.md`](PEER_TRIALS.md) (rows 1–5 stay empty until a real trial happens).  
> **Tip:** PyPI / git **0.2.6** — [`ROADMAP.md`](ROADMAP.md)

This is **not** a substitute for `bash scripts/peer_trial.sh` (mechanical smoke). M1–M5 already passed. These five rows need **real people**.

---

## Preflight (both machines)

Do this **before** DMing anyone. Do not skip Windows.

1. **Install the PyPI tip** (not a random git checkout unless you say so):

   ```bash
   pip install -U kedger
   kedger --version    # expect 0.2.6
   ```

2. **Same app repo.** Both people `cd` into clones of the **same git origin**. Kedger stores are keyed by repo fingerprint — different remotes → different stores → Bob will not see Alice’s pack.

3. **Init + doctor** in that repo:

   ```bash
   kedger init --name alice    # or bob
   kedger doctor
   ```

   **Success:** last line `doctor: all checks passed`. `[ok]` on `principal`, `store`, `share_mode: explicit_only`.  
   **Not a fail:** `[warn] store_encryption` / `raw_payloads` / `transcript_sidecars` on a plaintext store — plaintext SQLite is still the default.  
   **Is a fail:** any `[FAIL] …` line (exit 1). Fix before the trial.

4. **Windows PATH.** After `pip install kedger`, `kedger doctor` must **not** print `[warn] cli_path`. Store Python / user site-packages often omit `Scripts` from PATH — hooks then skip silently. Add the printed `Scripts` directory, or use Git Bash / WSL. `python -m kedger.cli.main` is a fallback, not the path hooks call.

5. **Windows scripts.** Use **Git Bash** (or WSL), not PowerShell alone, for `scripts/*.sh`. If you see `set: pipefail: invalid option name`, the tree was checked out CRLF — pull `main` (`.gitattributes` forces LF for `*.sh`) or re-clone.

6. **GitHub Release lag (warning only).** GitHub’s latest Release is still **v0.2.0**. PyPI tip is **0.2.6**. Do **not** create tags or GitHub Releases from this runbook. Install from PyPI (`pip install -U kedger`) and trust `kedger --version`, not the GitHub Releases page.

**Rehearsal (does not fill rows 1–5):**

```bash
bash scripts/peer_trial.sh
# expect: SMOKE_OK peer handoff path
```

---

## Alice → Bob sequence

Seed **at least one distinctive Anchor** on Alice so Bob can prove hydrate (canned smoke pair is fine if Alice’s store is empty).

### Bob (card)

```bash
cd /path/to/shared-app
kedger init --name bob          # skip if already inited
kedger peer card --out bob.kedger.json
```

**Success:** `wrote: …/bob.kedger.json`, `contains: public keys only (safe to Slack/email)`.  
Send **only** that JSON (Slack / email). It is public keys, not a pack.

### Alice (seed + send)

```bash
cd /path/to/shared-app
kedger init --name alice        # skip if already inited
kedger remember reject "Do not flip billing_v2" --reason finance
kedger remember constraint "Must send Idempotency-Key on charge create"
kedger peer send --to bob.kedger.json --out-dir ./xfer
```

**Success:** `granted: <bob principal>`, `pack: …/xfer/<id>.kxp` (optional `sidecar: …transcript.json`).  
Send the **`.kxp`** (and sidecar if present) like a private USB stick — Slack / Drive / USB. Not the peer card.

### Transfer

Anything that moves a file. Confirm Bob has the `.kxp` on disk before `open`. A 0-byte or truncated file is a break (file it).

### Bob (open + hydrate)

```bash
kedger peer open hf_….kxp       # actual filename from Alice
kedger hydrate --live
kedger doctor
```

**Success signals**

| Step | Expect |
|------|--------|
| `peer open` | `opened: hf_…`, `from: <alice principal>`, `anchors:` ≥ 1, lines like `[rejection] Do not flip billing_v2` |
| `hydrate --live` | `anchors:` ≥ 1, **same statements** Alice remembered (grep `idempotency` / `billing` for the canned pair) |
| `doctor` | `doctor: all checks passed` (plaintext `[warn]`s OK) |

Unauthorized open (wrong keys / other person’s pack) must fail closed: `error: not found` — no peek. Optional negative check; not required to fill a row.

**IDE (optional, not the pass bar):** new Cursor/Claude chat in a **trusted** workspace. SessionStart may drop; per-prompt inject is the reliable path — [`PROMPT_INJECT_VERIFY.md`](PROMPT_INJECT_VERIFY.md). A hydrate `--live` miss is a trial fail even if the IDE looks fine.

---

## Capture per trial → paste into `PEER_TRIALS.md`

Do **not** invent rows. After a real loop, fill one pending line:

| Column | What to write |
|--------|----------------|
| `#` | `1` … `5` (leave unused rows `pending`) |
| Date | ISO date (`2026-10-05`) |
| People | `alice@… → bob@…` (or first names + IDE) |
| Path | `card → send → open → hydrate` (note Windows / Git Bash if relevant) |
| Result | `pass` **or** `fail` — one line (`hydrate showed Idempotency-Key` / `open: not found`) |
| Issue | break issue URL, or `—` on a clean pass |

Example (do not copy into the table until it happened):

```text
| 1 | 2026-10-05 | Ada → Ben | card → send → Slack .kxp → open → hydrate | pass — Bob hydrate listed billing reject | — |
```

Mechanical M1–M5 stay as they are. Solo `KEDGER_HOME` two-home rehearsal is smoke, not a human row.

---

## Breaks — prefer issues over silent stars

File every fail (and any “worked but confusing”) with:

https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml

Template asks: role, where it broke, commands + exact error, expected, `kedger --version` / OS / IDE, optional `kedger doctor`, privacy checkbox.

A break issue **plus** a `fail` row still counts toward the five. A silent “eh, didn’t work” does not.

---

## Ask script (DM)

Copy-paste pack (DM + Windows addendum + LinkedIn pin + Discussion draft + how to log a row): [`PEER_ASK_PACK.md`](PEER_ASK_PACK.md).

From [`MARKETING.md`](MARKETING.md) § Peer dogfood protocol — send as-is:

> Can you spend 10 minutes on Kedger peer handoff with me? You `peer card`, I `peer send` a `.kxp`, you `peer open` + `hydrate --live`. File anything that breaks:  
> https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml

If they are on Windows, add: Git Bash, `kedger doctor` must not warn `cli_path`, `pip install -U kedger` (0.2.6).

---

## Redaction (hydrate / doctor / issue paste)

Treat a sent `.kxp` like a private handoff doc. Before pasting hydrate, doctor, or logs into GitHub / Slack / `PEER_TRIALS.md`:

- Strip API keys, tokens, passwords, `KEDGER_STORE_KEY`, `~/.kedger/keys/` material
- Strip customer names, private URLs, unreleased product names if they are not already public
- Keep kind + **short** statement (enough to prove the Anchor survived)
- Peer **cards** are public keys only — OK to Slack. Packs are not
- Check the issue template privacy box only after you actually redacted

Do not publish a raw hydrate dump as a “proof artifact” unredacted. Stage 2 wants redacted before/after; this runbook does not create those files.

---

## Exit

Stage 1 is green when rows 1–5 in [`PEER_TRIALS.md`](PEER_TRIALS.md) are filled (pass or fail-with-issue). Until then, do not start Stage 3 product bets ([`ROADMAP.md`](ROADMAP.md)).
