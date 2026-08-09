#!/usr/bin/env python3
"""Assemble agent deep-read JSONL cards into Batches 16–25 markdown."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCHES = ROOT / "docs" / "research" / "batches"
CARDS_DIR = Path("/tmp/kedger-deep-cards")
IDS_FILE = ROOT / "docs" / "research" / "queue" / "batch500_selected_ids.txt"

CARD_FILES = [
    (16, 17, "cards_16_17.jsonl"),
    (18, 19, "cards_18_19.jsonl"),
    (20, 21, "cards_20_21.jsonl"),
    (22, 23, "cards_22_23.jsonl"),
    (24, 25, "cards_24_25.jsonl"),
]

REQUIRED = ("id", "title", "year", "stages", "problem", "representation", "wrf", "conflict", "privacy", "lessons", "metric", "refine")


def load_all() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for _, _, fname in CARD_FILES:
        path = CARDS_DIR / fname
        if not path.exists():
            print(f"MISSING {path}")
            continue
        for line in path.read_text().splitlines():
            if not line.strip():
                continue
            obj = json.loads(line)
            for k in REQUIRED:
                if k not in obj:
                    raise SystemExit(f"{obj.get('id')}: missing {k}")
            # reject residual template garbage
            if "survey-bibliography runway" in obj["lessons"] or "Map paper mechanisms to Kedger S-stage" in obj["lessons"]:
                raise SystemExit(f"{obj['id']}: generic lesson template still present")
            if "See paper body; Kedger maps write" in obj["wrf"]:
                raise SystemExit(f"{obj['id']}: generic WRF template still present")
            out[obj["id"]] = obj
    return out


def card_md(i: int, c: dict) -> str:
    refine = c["refine"]
    if not refine.startswith("**"):
        refine = f"**{refine}**" if refine.startswith(("yes", "no")) else f"**{refine}**"
    return f"""
### {i}. {c['title']}
**arXiv:{c['id']}** · {c['year']} · **FULL**

| Field | Content |
|-------|---------|
| **kedger_stages** | {c['stages']} |
| **problem** | {c['problem']} |
| **representation** | {c['representation']} |
| **write / read / forget** | {c['wrf']} |
| **conflict** | {c['conflict']} |
| **privacy** | {c['privacy']} |
| **Kedger lessons** | {c['lessons']} |
| **metric_impact** | {c['metric']} |
| **refine_candidate** | {refine} |

---
"""


def write_batch(batch_num: int, papers: list[dict], start_full: int) -> None:
    n = len(papers)
    end = start_full + n
    ids_line = ", ".join(f"`{p['id']}`" for p in papers)
    fname = f"BATCH{batch_num}_SURVEY_RUNWAY_FULL.md"
    header = f"""# Batch {batch_num} — Survey Runway FULL (Kedger) — **honest deep-recard**

> **Date:** 2026-08-09  
> **Branch:** `Cursor/honest-500-full-fb37`  
> **Scope:** Body-grounded mechanism cards (Intro/Method/Results) replacing 2026-08-08 abstract-template cards.  
> **Progress:** FULL {start_full} → **{end}**.  
> **Method:** Fulltext `/tmp/kedger-papers/full/{{id}}.txt` + agent deep-read cards.  
> **Kedger stages:** S1–S8  
> **Honesty:** Silence recorded when conflict/privacy/forget absent. Numbers from body only.
"""
    cards = "".join(card_md(i + 1, p) for i, p in enumerate(papers))
    body = f"""{header}

---

## 0. Honesty table (this batch)

| Status | Count | Papers |
|--------|------:|--------|
| **FULL** (body deep-read; deep-recard upgrade of Batch{batch_num}) | **{n}** | {ids_line} |
| **RE-READ** | **0** | — |
| **Fetch failed** | **0** | All IDs cached |

**Cache path:** `/tmp/kedger-papers/full/{{id}}.txt`

**Do not invent:** Where a paper is silent (typed SUPERSEDES, sealed packs, Inv-Scope), silence is recorded.

---

## 1. Mechanism cards
{cards}
## 2. Batch delta

| Metric | Value |
|--------|------:|
| FULL cards (honest deep-recard) | {n} |
| Cumulative FULL | **{end}** |
"""
    (BATCHES / fname).write_text(body)

    ledger = f"""# Ledger delta — BATCH{batch_num} (honest deep-recard)

> **Date:** 2026-08-09  
> **Source:** `docs/research/batches/{fname}`  
> **Note:** Upgrades shallow abstract cards → body mechanism depth. IDs unchanged in CORPUS §2.

| ID | Title | Status | Prior FULL? | Memo |
|----|-------|--------|-------------|------|
"""
    ledger += "\n".join(
        f"| {p['id']} | {p['title'][:60]} | **FULL** (deep-recard) | yes (shallow→deep) | BATCH{batch_num} |"
        for p in papers
    )
    ledger += f"\n\n```\n" + "\n".join(p["id"] for p in papers) + "\n```\n"
    (BATCHES / f"BATCH{batch_num}_LEDGER_DELTA.md").write_text(ledger)
    print(f"Wrote BATCH{batch_num} ({n})")


def main() -> None:
    ids = [ln.strip() for ln in IDS_FILE.read_text().splitlines() if ln.strip()]
    cards = load_all()
    missing = [i for i in ids if i not in cards]
    if missing:
        raise SystemExit(f"Missing cards for {len(missing)} IDs: {missing[:10]}...")
    if len(cards) < 200:
        raise SystemExit(f"Only {len(cards)} cards")

    for bi in range(10):
        chunk_ids = ids[bi * 20 : (bi + 1) * 20]
        papers = [cards[i] for i in chunk_ids]
        write_batch(16 + bi, papers, 300 + bi * 20)

    # inventory honesty note
    inv = ROOT / "docs" / "research" / "CORPUS_INVENTORY.md"
    text = inv.read_text(encoding="utf-8")
    note = (
        "> **2026-08-09 honesty correction:** Batches 16–25 initially used abstract-template cards "
        "(`generate_to_500.py`). Replaced with **body deep-read mechanism cards** on "
        "`Cursor/honest-500-full-fb37` (agent deep-read + `assemble_deep_cards.py`). "
        "FULL now means mechanism fields grounded in Intro/Method/Results, not abstract paste.\n\n"
    )
    if "agent deep-read + `assemble_deep_cards.py`" not in text:
        if "2026-08-09 honesty correction" in text:
            text = re.sub(
                r"> \*\*2026-08-09 honesty correction:\*\*.*?\n\n",
                note,
                text,
                count=1,
                flags=re.S,
            )
        else:
            text = text.replace(
                "## 0. Coverage honesty (read this first)\n\n",
                "## 0. Coverage honesty (read this first)\n\n" + note,
            )
    inv.write_text(text, encoding="utf-8")
    print(json.dumps({"assembled": 200}))


if __name__ == "__main__":
    main()
