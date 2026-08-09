#!/usr/bin/env python3
"""Extract structured deep-read evidence from cached paper bodies.

Not a FULL card by itself — feeds honest mechanism card writing.
Outputs JSONL with sections, numbers, memory ops signals.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CACHE = Path("/tmp/kedger-papers/full")
OUT = Path("/tmp/kedger-deep-extract")
IDS_FILE = Path("docs/research/queue/batch500_selected_ids.txt")

SECTION_PATS = [
    ("abstract", r"(?:^|\n)\s*Abstract\b[:\s]*(.+?)(?=\n\s*(?:1\s+)?Introduction\b|\n\s*Keywords\b|\n\s*1\s)"),
    ("intro", r"(?:^|\n)\s*(?:1[\.\s]+)?Introduction\b[:\s]*(.+?)(?=\n\s*(?:2[\.\s]+)?(?:Related|Background|Preliminar|Method|Approach|Model|Framework))"),
    ("method", r"(?:^|\n)\s*(?:\d[\.\s]+)?(?:Method|Approach|Methodology|Proposed|Our (?:Method|Approach|Framework|Model)|Architecture|Framework)\b[:\s]*(.+?)(?=\n\s*(?:\d[\.\s]+)?(?:Experiment|Evaluation|Result|Ablation|Discussion))"),
    ("results", r"(?:^|\n)\s*(?:\d[\.\s]+)?(?:Experiments?|Evaluation|Results?)\b[:\s]*(.+?)(?=\n\s*(?:\d[\.\s]+)?(?:Ablation|Discussion|Related|Conclusion|Limitations|Appendix))"),
    ("conclusion", r"(?:^|\n)\s*(?:\d[\.\s]+)?Conclusions?\b[:\s]*(.+?)(?=\n\s*(?:Acknowledg|Reference|Appendix|Bibliography)|$)"),
]

NUM_RE = re.compile(
    r"(?:(?:\d+(?:\.\d+)?%|\+\s*\d+(?:\.\d+)?%|\d+(?:\.\d+)?\s*(?:points?|pp)|"
    r"F1[=:\s]+\d+(?:\.\d+)?|EM[=:\s]+\d+(?:\.\d+)?|"
    r"accuracy[=:\s]+\d+(?:\.\d+)?%?|"
    r"Recall@\d+\s*[=:\s]*\d+(?:\.\d+)?|"
    r"pass\^\d+\s*[<≈=~]?\s*\d+(?:\.\d+)?%?|"
    r"\b\d{2,4}\s+(?:tasks?|questions?|episodes?|sessions?|papers?|agents?|APIs?)\b))",
    re.I,
)

WRITE_RE = re.compile(r"\b(write|store|insert|update|append|memorize|save|encode into memory|memory write|promotion|consolidat)\b", re.I)
READ_RE = re.compile(r"\b(retriev|recall|hydrat|read from|query memory|lookup|fetch|search)\b", re.I)
FORGET_RE = re.compile(r"\b(forget|evict|delet|invalidat|expir|prune|tombstone|decay|unshare)\b", re.I)
CONFLICT_RE = re.compile(r"\b(conflict|contradict|supersed|inconsist|revision|counter.?memor|resolve)\b", re.I)
PRIVACY_RE = re.compile(r"\b(privacy|leak|membership|secret|confidential|differential.?privacy|capability|injection|poison|adversar)\b", re.I)


def clean(s: str, limit: int) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


def extract(pid: str) -> dict:
    path = CACHE / f"{pid}.txt"
    if not path.exists():
        return {"id": pid, "ok": False, "error": "missing"}
    text = path.read_text(errors="ignore")
    # Prefer later half for method if HTML junk at start
    body = text
    if "Abstract" in text:
        idx = text.find("Abstract")
        body = text[idx:]
    sections: dict[str, str] = {}
    for name, pat in SECTION_PATS:
        m = re.search(pat, body, re.I | re.S)
        if m:
            sections[name] = clean(m.group(1), 3500 if name == "method" else 2000)

    # Title from start
    title_m = re.search(r"\]\s*([^[]{8,160}?)(?:function detectColorScheme|Contact:|Skip to main|Abstract)", text[:2500])
    title = clean(title_m.group(1), 160) if title_m else pid

    # Numbers from results or whole
    search_zone = sections.get("results", "") + " " + sections.get("method", "") + " " + body[:15000]
    nums = list(dict.fromkeys(NUM_RE.findall(search_zone)))[:12]

    blob = (sections.get("method", "") + " " + sections.get("intro", "") + " " + sections.get("abstract", "")).lower()
    signals = {
        "write": bool(WRITE_RE.search(blob)),
        "read": bool(READ_RE.search(blob)),
        "forget": bool(FORGET_RE.search(blob)),
        "conflict": bool(CONFLICT_RE.search(blob)),
        "privacy": bool(PRIVACY_RE.search(blob)),
    }

    # Method bullets: sentences with architecture keywords
    method = sections.get("method", "") or sections.get("intro", "")
    sents = re.split(r"(?<=[.!?])\s+", method)
    key_sents = [
        s for s in sents
        if re.search(r"propos|introduc|we (?:present|design|build|use)|framework|module|pipeline|architecture|consist|memory|retriev|agent", s, re.I)
        and len(s) > 40
    ][:6]

    year = "20" + pid[:2] if int(pid[:2]) < 50 else "19" + pid[:2]
    return {
        "id": pid,
        "ok": True,
        "title": title,
        "year": year,
        "txt_len": len(text),
        "abstract": sections.get("abstract", "")[:900],
        "intro_snip": sections.get("intro", "")[:1200],
        "method_snip": sections.get("method", "")[:3000],
        "results_snip": sections.get("results", "")[:2000],
        "conclusion_snip": sections.get("conclusion", "")[:800],
        "key_sents": key_sents,
        "numbers": nums,
        "signals": signals,
        "has_method": bool(sections.get("method")),
        "has_results": bool(sections.get("results")),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    ids = [ln.strip() for ln in IDS_FILE.read_text().splitlines() if ln.strip()]
    out_path = OUT / "extracts.jsonl"
    with out_path.open("w") as f:
        for i, pid in enumerate(ids):
            rec = extract(pid)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if (i + 1) % 20 == 0:
                print(f"extracted {i+1}/{len(ids)}", file=sys.stderr)
    ok = sum(1 for line in out_path.read_text().splitlines() if json.loads(line).get("ok"))
    print(json.dumps({"ids": len(ids), "ok": ok, "out": str(out_path)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
