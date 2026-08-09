# Marketing Kedger — launch narrative & distribution

Stars follow **clarity + demo + distribution**. This doc locks positioning, claim guardrails, LinkedIn paste pack, and peer-trial protocol.

## Positioning lock (say this every time)

**Problem:** Code is versioned. Agent judgment (decisions, rejects, constraints) dies with the chat. Teams cold-start and relitigate.

**Category:** casual local-first **engineering judgment memory** + **person-to-person sealed handoff**  
**Not:** living codebase wiki / ambient team brain / cloud sync-by-default

**One line:** Kedger keeps the *why* from coding-agent sessions as Anchors, then lets you hand it off in a sealed `.kxp` — only when you choose.

| | Kedger | Wiki-memory / ambient sync tools |
|---|---|---|
| Object | Session judgment + ops | Repo docs / always-on shared brain |
| Durability | `~/.kedger/` + sealed `.kxp` | Markdown in git or cloud memory bus |
| Share | `explicit_only` — send a pack | Ambient / repo-visible by default |
| Team help | Handoff when someone passes a file | Everyone sees the same wiki/sync |

**Why no ambient contact sharing:** session judgment is sensitive; auto-sync is a leak surface. Friction (send a `.kxp`) is the privacy feature.

**Proof (honest):** `pip install kedger` works; CI + strict handoff evals. Alpha — not a field study.

## Claim guardrails (non-negotiable)

**Do claim**

- Local-first store under `~/.kedger/`
- Redact-before-persist on ingest
- Share is explicit and crypto-bound to recipient keys
- Peer flow: `peer card` → `peer send` → send `.kxp` → `peer open` → `hydrate --live`
- Alpha OSS with mechanical handoff tests (CI, strict benches, smoke scripts)

**Do not claim**

- LLM distill every turn, cloud sync, team dashboard, MCP-as-primary (Phase F — [`PHASE_F_DEFERRED.md`](PHASE_F_DEFERRED.md))
- “Living wiki of the whole codebase”
- “Proven in production” / “beats mex” / “makes agents smarter” (no field study)
- That revoke erases old offline `.kxp` copies (it does not)

**Honesty line (use on every public post):**  
*Alpha OSS. Mechanically tested handoff. Not yet a published user study.*

## Privacy (one paragraph for posts)

Memory stays local. Ingest redacts secret-shaped strings. Sharing is opt-in: Bob’s public peer card → Alice grants + seals → only Bob’s keys open the `.kxp`. Easy continuity for people on the task; hard/no continuity for everyone else. Treat a sent `.kxp` like a private handoff doc.

## GitHub surface

| Item | Status |
|------|--------|
| Description | Code is versioned; agent judgment isn't. Anchors + sealed `.kxp` — explicit share |
| Homepage | https://pypi.org/project/kedger/ |
| Topics | cli, python, agents, cursor, claude-code, memory, handoff, local-first, sealed-packs, developer-tools |
| Wiki | Off |
| Social preview | **Maintainer:** Settings → General → Social preview → upload [`docs/assets/social.png`](assets/social.png) |

Refresh About (needs repo admin `gh`):

```bash
bash scripts/set_github_about.sh
```

## LinkedIn — paste pack (Day 0)

**Attach:** [`docs/assets/peer-story.png`](assets/peer-story.png)  
**Alt text:** Alice seals a .kxp; Bob opens it and hydrates — local-first agent handoff.  
**Optional carousel:** [`before-after.png`](assets/before-after.png) then peer-story.

### Post body (copy all)

```text
Code is versioned. Agent judgment isn’t.

You and Claude just settled “no Redis — use Postgres.” New chat tomorrow? Cold. Teammate’s agent? Also cold. Slack paste loses the why.

I built Kedger — a casual, local-first CLI that keeps the why as Anchors (decisions, rejects, constraints) and lets you hand it off in a sealed .kxp. Only when you choose. No ambient team sync. No cloud memory bus.

How team help actually works (handoff, not contact-sharing):
1. Bob sends a peer card (public keys only)
2. Alice runs kedger peer send → grant + seal .kxp
3. She sends the file (Slack / Drive / USB)
4. Bob peer open → hydrate --live → new chat continues with her Anchors + ops

Privacy tradeoff on purpose: ~/.kedger/ local store, redact-on-ingest, explicit_only share. Easy for people on the task. Hard for everyone else.

Alpha OSS — CI + strict handoff evals. Not a field study. Tip 0.1.1.

pip install kedger
https://github.com/gaganTakIITD/kedger

#Cursor #ClaudeCode #OpenSource #DeveloperTools
```

### Pin under your own post (follow-up comment)

```text
60-second start:
pip install "kedger>=0.1.1"
cd your-app && kedger init --name alice

Peer path: peer card → peer send → send .kxp → peer open → hydrate --live
Break reports: https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml
```

## Other post templates

### X / Bluesky

```text
Your teammate’s agent doesn’t inherit your Cursor chat.

Kedger: sealed .kxp handoff (local-first, explicit_only)
peer card → peer send → peer open → hydrate --live

Alpha. Mechanically tested. Not a field study.
pip install kedger
https://github.com/gaganTakIITD/kedger
```

Attach `peer-story.png`.

### Show HN

**Title:** Show HN: Kedger – sealed .kxp handoff between coding agents (local-first)

**Body sketch:**

- Problem: teammate / next-chat cold start (not “docs drift”)
- What: hooks + Anchors + sealed packs; peer card/send/open
- Privacy: `~/.kedger/`, redact-on-ingest, `explicit_only`
- Try: `pip install kedger && kedger init --name alice`
- Honest: alpha; CI + strict evals; no cloud sync / MCP yet

## Peer dogfood protocol (target: 5 real trials)

Ask five Cursor/Claude users to run one peer send. Prefer break reports over silent stars.

### Script for the ask

> Can you spend 10 minutes on Kedger peer handoff with me? You `peer card`, I `peer send` a `.kxp`, you `peer open` + `hydrate --live`. File anything that breaks:  
> https://github.com/gaganTakIITD/kedger/issues/new?template=peer_handoff.yml

### Local mechanical dogfood (maintainer / CI)

```bash
pip install -e ".[dev]"
./scripts/smoke_peer_handoff.sh
./scripts/smoke_transfer.sh
```

Track trials in the checklist below; open an issue per real human break.

## Maintainer launch checklist

- [x] PyPI `0.1.1` + GitHub Release `v0.1.1`
- [x] GitHub About description / homepage / topics
- [ ] Upload `docs/assets/social.png` as Social preview (UI only)
- [ ] Post LinkedIn paste pack + peer-story image
- [ ] Optional: Show HN / X with same narrative
- [ ] 5 peer-send trials → issues via `peer_handoff.yml`
- [ ] Zero Phase F or “proven in prod” claims on any channel

## Brand rules

- Wordmark: **Kedger** in prose
- Palette: ink `#071018` + cyan `#5eead4`
- Name the artifact: **`.kxp`**
- Lead with **handoff to a person**, not only “agents forget”
- Never claim Phase F as shipped
