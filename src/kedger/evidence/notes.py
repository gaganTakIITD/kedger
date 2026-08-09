"""Chain-of-Note (CoN) style deterministic reading notes for Evidence.

Lit: Yu et al. 2311.09210 — per-doc note: support / context / unknown.
Kedger v1: lexical overlap only (no LLM distill — Phase F closed).
"""

from __future__ import annotations

import re
from typing import Any

_TOKEN = re.compile(r"[a-z0-9_]{3,}")
_STOP = frozenset(
    {
        "the",
        "and",
        "for",
        "are",
        "but",
        "not",
        "you",
        "all",
        "can",
        "had",
        "her",
        "was",
        "one",
        "our",
        "out",
        "has",
        "his",
        "how",
        "its",
        "may",
        "new",
        "now",
        "old",
        "see",
        "way",
        "who",
        "boy",
        "did",
        "get",
        "let",
        "put",
        "say",
        "she",
        "too",
        "use",
        "that",
        "this",
        "with",
        "from",
        "have",
        "been",
        "were",
        "will",
        "into",
        "your",
        "their",
        "about",
        "when",
        "what",
        "which",
        "while",
        "where",
        "there",
        "then",
        "than",
        "also",
        "just",
        "only",
        "over",
        "such",
        "same",
        "using",
        "used",
    }
)


def _tokens(text: str) -> set[str]:
    return {t for t in _TOKEN.findall((text or "").lower()) if t not in _STOP}


def note_evidence(
    evidence: dict[str, Any],
    *,
    anchor_statement: str,
    topic: str | None = None,
) -> dict[str, Any]:
    """Return relevance note for one Evidence row against an Anchor (+ optional topic).

    Labels:
    - support: strong overlap with Anchor statement
    - context: weak overlap or topic-only hit
    - unknown: no meaningful overlap (abstain path)
    """
    snippet = str(evidence.get("snippet") or evidence.get("text") or "")
    src = str(evidence.get("source_ref") or "")
    blob = f"{snippet} {src}"
    ev_toks = _tokens(blob)
    anc_toks = _tokens(anchor_statement)
    topic_toks = _tokens(topic or "")

    if not ev_toks:
        label = "unknown"
        overlap = 0.0
    else:
        anc_hits = len(ev_toks & anc_toks)
        topic_hits = len(ev_toks & topic_toks) if topic_toks else 0
        denom = max(1, len(anc_toks) if anc_toks else len(ev_toks))
        overlap = anc_hits / denom
        if anc_hits >= 2 or overlap >= 0.35:
            label = "support"
        elif anc_hits >= 1 or topic_hits >= 1:
            label = "context"
        else:
            label = "unknown"

    return {
        "relevance": label,
        "overlap": round(overlap, 3),
        "text": (
            f"[{label}] evidence overlaps Anchor"
            if label != "unknown"
            else "[unknown] evidence not clearly relevant to Anchor"
        ),
    }


def attach_notes(
    evidence_rows: list[dict[str, Any]],
    *,
    anchor_statement: str,
    topic: str | None = None,
) -> tuple[list[dict[str, Any]], bool]:
    """Annotate Evidence list; abstain=True when non-empty and all unknown."""
    annotated: list[dict[str, Any]] = []
    for ev in evidence_rows:
        note = note_evidence(ev, anchor_statement=anchor_statement, topic=topic)
        annotated.append({**ev, "note": note})
    abstain = bool(annotated) and all(
        (e.get("note") or {}).get("relevance") == "unknown" for e in annotated
    )
    return annotated, abstain
