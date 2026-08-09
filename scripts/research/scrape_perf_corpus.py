#!/usr/bin/env python3
"""Scrape arXiv for agent-memory + efficiency papers → perf corpus seeds.

Honest scope: API metadata index + abstract text for prioritization.
FULL deep-read is a separate step (fetch bodies + mechanism cards).
"""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "docs" / "research" / "queue"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
UA = "KedgerResearchBot/0.1 (+https://github.com/gaganTakIITD/kedger; corpus scrape)"

QUERIES = [
    'ti:"agent memory" OR abs:"agent memory"',
    'ti:"memory for LLM" OR abs:"LLM agents" AND abs:memory',
    'abs:"long-term memory" AND (abs:agent OR abs:LLM)',
    'ti:HippoRAG OR ti:MemGPT OR ti:LightMem OR ti:LeanMem OR ti:GraphReader',
    'abs:"KV cache" AND (abs:evict OR abs:compress OR abs:StreamingLLM)',
    'abs:"context compression" AND (abs:LLM OR abs:agent)',
    'abs:"retrieval augmented" AND abs:memory AND abs:agent',
    'ti:SnapKV OR ti:H2O OR ti:StreamingLLM OR ti:InfLLM OR ti:ShadowKV',
    'abs:"personalized PageRank" AND abs:retrieval',
    'abs:"working memory" AND abs:agent AND abs:LLM',
    'abs:cognify OR abs:"memory consolidation" AND abs:LLM',
    'abs:"offline" AND abs:memory AND abs:agent AND abs:LLM',
]

PERF_TERMS = re.compile(
    r"\b(kv|cache|compress|token|latency|throughput|budget|evict|ppr|"
    r"pagerank|retrieve|efficient|offline|online|32kb|context.?window|"
    r"handoff|hydrate|snapkv|streamingllm|hipporag|lightmem|leanmem|"
    r"graphreader|infllm|delay)\b",
    re.I,
)


def fetch_query(q: str, start: int, max_results: int = 100) -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "search_query": f"all:({q})" if not q.startswith("ti:") and "ti:" not in q and "abs:" not in q else q,
            "start": start,
            "max_results": max_results,
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )
    # Prefer structured field queries as given
    url = f"https://export.arxiv.org/api/query?{params}"
    # Fix: pass query raw when already fielded
    url = (
        "https://export.arxiv.org/api/query?"
        + urllib.parse.urlencode(
            {
                "search_query": q,
                "start": start,
                "max_results": max_results,
                "sortBy": "relevance",
                "sortOrder": "descending",
            }
        )
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = resp.read()
    root = ET.fromstring(data)
    out: list[dict] = []
    for entry in root.findall(f"{ATOM}entry"):
        id_url = (entry.findtext(f"{ATOM}id") or "").strip()
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", id_url)
        if not m:
            continue
        aid = m.group(1)
        title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
        summary = " ".join((entry.findtext(f"{ATOM}summary") or "").split())
        published = (entry.findtext(f"{ATOM}published") or "")[:10]
        cats = [c.get("term", "") for c in entry.findall(f"{ARXIV}primary_category")]
        cats += [c.get("term", "") for c in entry.findall(f"{ATOM}category")]
        out.append(
            {
                "arxiv_id": aid,
                "title": title,
                "abstract": summary,
                "published": published,
                "categories": sorted(set(cats)),
                "query": q[:80],
            }
        )
    return out


def perf_score(row: dict) -> float:
    blob = f"{row['title']} {row['abstract']}"
    hits = len(PERF_TERMS.findall(blob))
    year = 0
    try:
        year = int(row["published"][:4])
    except ValueError:
        pass
    recency = max(0, year - 2020) * 0.4
    # Prefer systems that mention agents + efficiency together
    bonus = 0.0
    low = blob.lower()
    if "agent" in low and ("memory" in low or "kv" in low):
        bonus += 2.0
    if any(k in low for k in ("hipporag", "lightmem", "leanmem", "streamingllm", "snapkv", "graphreader", "memgpt")):
        bonus += 3.0
    if any(k in low for k in ("evict", "compress", "budget", "latency", "token")):
        bonus += 1.5
    return hits + recency + bonus


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    by_id: dict[str, dict] = {}
    for q in QUERIES:
        print(f"query: {q[:70]}...")
        for start in (0, 100, 200):
            try:
                rows = fetch_query(q, start=start, max_results=100)
            except Exception as e:  # noqa: BLE001
                print(f"  fail start={start}: {e}")
                time.sleep(3)
                continue
            print(f"  start={start} got {len(rows)}")
            for r in rows:
                prev = by_id.get(r["arxiv_id"])
                if prev is None:
                    by_id[r["arxiv_id"]] = r
                else:
                    # keep longer abstract / merge queries
                    if len(r["abstract"]) > len(prev["abstract"]):
                        prev["abstract"] = r["abstract"]
                        prev["title"] = r["title"]
                    prev.setdefault("queries", [prev.get("query")])
                    if isinstance(prev.get("queries"), list):
                        prev["queries"].append(q[:80])
            time.sleep(3.2)  # polite
        time.sleep(1.0)

    seed_path = OUT_DIR / "perf_corpus_seed.jsonl"
    rows = sorted(by_id.values(), key=lambda r: -perf_score(r))
    with seed_path.open("w", encoding="utf-8") as f:
        for r in rows:
            r["perf_score"] = round(perf_score(r), 3)
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} → {seed_path}")

    # Priority 300
    prio = rows[:300]
    prio_path = OUT_DIR / "perf_priority_300.jsonl"
    with prio_path.open("w", encoding="utf-8") as f:
        for i, r in enumerate(prio, 1):
            rec = dict(r)
            rec["rank"] = i
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {len(prio)} → {prio_path}")

    # Also copy with names from the user's brief
    (OUT_DIR / "perf_corpus_seed_1174.jsonl").write_text(
        seed_path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    print("also wrote perf_corpus_seed_1174.jsonl (actual count may differ)")


if __name__ == "__main__":
    main()
