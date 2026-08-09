# Marketing Kedger — get stars, users, and signal

This is a practical launch playbook. Stars follow **clarity + demo + distribution**, not logos alone.

## Positioning (say this every time)

**One line:** Local-first memory for coding agents — your next agent remembers.

**Pain:** New chats / teammates restart cold after context compact.

**Fix:** Hooks → Anchors → sealed `.kxp` handoff. No cloud required.

**Proof:** `pip install kedger` → `kedger init` → `hydrate --live` in under a minute.

**Not:** “another vector DB”, “cloud memory SaaS”, or “MoDeX”.

## GitHub surface (do first)

Empty About kills conversion. On a maintainer machine:

```bash
bash scripts/set_github_about.sh
```

Then **Settings → General → Social preview** → upload `docs/assets/social.png`.

Checklist:

| Item | Target |
|------|--------|
| Description | Local-first eng-memory CLI for coding agents — hooks → Anchors → sealed .kxp handoff |
| Homepage | https://pypi.org/project/kedger/ |
| Topics | cli, python, agents, cursor, claude-code, memory, handoff, local-first, sealed-packs, developer-tools |
| README above the fold | Banner + problem panel + Install CTA |
| Release | Tag `v0.1.1` with CHANGELOG body |
| Pin | Pin the release announcement issue or README |

## Content that earns stars

Ship **show, don’t tell** assets (already in `docs/assets/`):

| Asset | Use |
|-------|-----|
| `before-after.png` | Tweet / HN / Reddit — cold start vs hydrate |
| `peer-story.png` | Two-dev handoff story |
| `demo.gif` | README + short posts |
| `social.png` | Social preview + LinkedIn / X card |
| `idea-flow.png` | Explain pipeline once |

Refresh anytime:

```bash
python3 scripts/render_brand_assets.py
```

## Distribution channels (order of leverage)

### Day 0 — own channels

1. **GitHub Release** for `v0.1.1` with install + peer GIF/PNG
2. **X / LinkedIn** post (template below)
3. **PyPI** already live — link it every time
4. Ask 5–10 friends who use Cursor/Claude to try + star if useful

### Day 1–3 — communities (read rules first)

| Place | Angle |
|-------|--------|
| [Hacker News](https://news.ycombinator.com/submit) | “Show HN: Kedger – local-first memory CLI for coding agents” |
| r/LocalLLaMA, r/cursor, r/ClaudeAI, r/Python | Demo GIF + install, no spam |
| Cursor Forum / Discord | Hook-install story |
| Awesome lists | PR into awesome-cursor / awesome-claude / awesome-cli if they accept memory tools |

### Week 1 — narrative posts

Write one short post answering: *“My Cursor agent forgot our architecture decision. Here’s what I built.”*

Include:

1. Before/after screenshot
2. Three commands
3. Link to repo + PyPI

### Ongoing

- Reply to tweets about “agent context loss”, “handoff between agents”, “Claude forgot”
- Ship small visible wins (demo polish, one new hook) weekly — release notes drive stars
- Collect 2–3 user quotes → put in README later

## Post templates

### X / Bluesky (short)

```text
Coding agents forget. New chats restart cold.

Kedger is a local-first CLI:
hooks → Anchors → sealed .kxp → next agent hydrates

pip install kedger
kedger init --name alice

https://github.com/gaganTakIITD/kedger
```

Attach `docs/assets/before-after.png` or `demo.gif`.

### Show HN

**Title:** Show HN: Kedger – local-first eng-memory CLI for coding agents

**Body sketch:**

- Problem: context compact / teammate cold start  
- What: hooks + Anchors + sealed packs (`.kxp`)  
- Why local: keys under `~/.kedger/`, share is explicit  
- Try: `pip install kedger && kedger init --name alice`  
- Honest scope: no cloud sync / MCP yet  

### LinkedIn

Lead with the peer story (Alice → Bob), then install. Engineers share “two-agent handoff” more than CLI dumps.

## Star growth reality check

| Tactic | Effect |
|--------|--------|
| Clear README + demo above the fold | Highest conversion from visitors → stars |
| Show HN / launch posts | Spike; need follow-up |
| Topics + social preview | Discoverability from GitHub search / shares |
| Weekly tiny releases | Compound; beats one big silent launch |
| Buying stars / spam | Damages trust — don’t |

Aim for **useful first users**, not vanity counts. Ten people who `peer send` weekly beat 500 drive-by stars.

## Metrics to watch

1. GitHub traffic → Referrers (which post worked)
2. PyPI downloads after a post
3. Issues / Discussions that say “I tried this”
4. Clone → `kedger init` (ask early users)

## Brand rules (keep consistent)

- Wordmark: **Kedger** (not KEDGER in prose; assets may be caps)
- Palette: ink `#071018` + cyan `#5eead4`
- Promise: local-first, explicit share, next-agent memory
- Never claim Phase F (LLM distill / sync / MCP) as shipped

## Maintainer checklist (launch week)

- [ ] `bash scripts/set_github_about.sh`
- [ ] Upload `docs/assets/social.png` as social preview
- [ ] Post Show HN + one community thread
- [ ] Share before/after image on X/LinkedIn
- [ ] Ask 5 Cursor/Claude users for a genuine try
- [ ] Pin a “Start here” comment on the latest Release
