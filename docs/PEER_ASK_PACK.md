# Peer ask pack (Stage 1 recruitment)

> **Copy-paste ready.** Send these as-is. Do **not** invent [`PEER_TRIALS.md`](PEER_TRIALS.md) rows 1–5.  
> **Tip:** PyPI / git **0.2.6** — install with `pip install -U kedger`, then `kedger --version` (expect `0.2.6`).  
> **Runbook:** [`PEER_TRIAL_RUNBOOK.md`](PEER_TRIAL_RUNBOOK.md) · **Stages:** [`ROADMAP.md`](ROADMAP.md)

This pack is for **recruiting real people**. Mechanical M1–M5 already passed in CI (`scripts/smoke_peer_handoff.sh`) and **do not count** as the five human rows.

---

## Tip install (both of you, before the DM lands)

```bash
pip install -U kedger
kedger --version    # expect 0.2.6
```

GitHub’s latest Release is still **v0.2.0**. Ignore the Releases page for install. PyPI is the tip.

Break reports (prefer an issue over a silent star):  
https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml

---

## Short DM

From [`MARKETING.md`](MARKETING.md) § Peer dogfood protocol — send as-is:

```text
Can you spend 10 minutes on Kedger peer handoff with me? You `peer card`, I `peer send` a `.kxp`, you `peer open` + `hydrate --live`. File anything that breaks:
https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml
```

---

## Windows addendum

Paste after the DM if they are on Windows (or send it with the first ping):

```text
Windows: use Git Bash (or WSL), not PowerShell alone, for the trial scripts. After `pip install -U kedger`, run `kedger doctor` — it must not warn `[warn] cli_path`. If it does, add the printed `Scripts` folder to PATH (Store Python / user site-packages often skip it) or use Git Bash/WSL. Expect `kedger --version` → 0.2.6. If you see `set: pipefail: invalid option name`, pull latest `main` (scripts are LF-only) or re-clone.
```

Runbook Windows preflight is the longer version: [`PEER_TRIAL_RUNBOOK.md`](PEER_TRIAL_RUNBOOK.md) § Preflight.

---

## LinkedIn follow-up / pin

Use as a comment under the Day 0 post (or pin on the repo README social thread). Tip is **0.2.6**, not the GitHub Release latest.

```text
60-second start (PyPI tip 0.2.6 — GitHub Release latest is still v0.2.0):
pip install -U kedger
kedger --version   # expect 0.2.6
cd your-app && kedger init --name alice

Peer path: peer card → peer send → send .kxp → peer open → hydrate --live
10-minute dogfood: DM me. Break reports:
https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml

Beta OSS. Mechanically tested handoff. Not a field study.
```

Full LinkedIn Day 0 post body stays in [`MARKETING.md`](MARKETING.md).

---

## GitHub Discussion body (draft — paste; posting is optional)

**Where:** repo Discussions → **General** (or Q&A). Do not require this to be posted for Stage 1 to count; DMs are enough.

**Title:** `10-minute peer handoff trial (Cursor / Claude) — tip 0.2.6`

**Body:**

~~~markdown
Looking for five real Cursor / Claude users to run one Alice→Bob Kedger handoff (~10 minutes).

**What:** judgment handoff, not an ambient wiki. You `peer card` (public keys), I `peer send` a sealed `.kxp`, you `peer open` + `hydrate --live`. Share is `explicit_only`.

**Install (PyPI tip — ignore GitHub Release latest, still v0.2.0):**

```bash
pip install -U kedger
kedger --version    # expect 0.2.6
```

**Sequence:** [PEER_TRIAL_RUNBOOK.md](https://github.com/gaganTakIITD/kedger/blob/main/docs/PEER_TRIAL_RUNBOOK.md)

**Windows:** Git Bash or WSL; `kedger doctor` must not warn `cli_path`.

**If it breaks:** file a [peer handoff](https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml) issue (prefer that over a silent star).

Beta OSS. CI + strict evals already pass. This ask is the **human** loop — mechanical smokes (M1–M5) are not these five trials. Not a published user study.
~~~

---

## After a real trial — log it in `PEER_TRIALS.md`

Do **not** fill a row because the smoke script passed, because you rehearsed two `KEDGER_HOME`s on one machine, or because you “would have” run it. Log **after** a real person completed card → send → transfer `.kxp` → open → `hydrate --live`.

1. Confirm tip: both people `kedger --version` → **0.2.6**.
2. Capture the loop (redact first — runbook § Redaction): people, path (note Windows / Git Bash), one-line result.
3. Open [`PEER_TRIALS.md`](PEER_TRIALS.md). Edit **one** pending human row (`1` … `5`). Leave unused rows `pending`.
4. Columns:

   | Column | Write |
   |--------|--------|
   | `#` | `1` … `5` |
   | Date | ISO (`2026-10-05`) |
   | People | `Ada → Ben` (or emails / IDE) |
   | Path | `card → send → Slack .kxp → open → hydrate` |
   | Result | `pass` **or** `fail` — one line of evidence (`hydrate showed Idempotency-Key` / `open: not found`) |
   | Issue | break URL, or `—` on a clean pass |

5. File every fail (and any “worked but confusing”) via the [peer handoff](https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml) template. A `fail` row **plus** an issue still counts toward the five.
6. Commit the log row on `main` (or a tiny docs PR). Do not invent the other four.

Example (**do not copy into the table until it happened**):

```text
| 1 | 2026-10-05 | Ada → Ben | card → send → Slack .kxp → open → hydrate | pass — Bob hydrate listed billing reject | — |
```

---

## Guardrails

- **Do not invent trial rows.** Empty pending rows are honest. Fake names are not.
- **Mechanical M1–M5 ≠ human rows 1–5.** `bash scripts/peer_trial.sh` / `smoke_peer_handoff.sh` stay in the M1–M5 line.
- **Do not claim** a field study, “proven in production,” live sync, or full Phase F. Honesty line: *Beta OSS. Mechanically tested handoff. Not yet a published user study.*
- **Do not re-upload to PyPI.** Tip **0.2.6** is already published.
- Treat a sent `.kxp` like a private handoff doc. Peer **cards** are public keys (OK to Slack). Packs are not.

Stage 1 is green when rows 1–5 are filled (pass or fail-with-issue). Until then, do not start Stage 3 product bets ([`ROADMAP.md`](ROADMAP.md)).
