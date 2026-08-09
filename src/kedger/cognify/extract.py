"""Deterministic multi-claim extraction from messy L0 turns.

Gate for capture quality: never promote a whole rambling observation as one
Anchor. Split → classify → normalize → theme-dedupe. No LLM (Phase F closed).
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Iterable

from kedger.constants import ANCHOR_STATEMENT_MAX

CLAIM_SOFT_MAX = 140
CLAIM_MIN = 18
MAX_PER_KIND = {
    "constraint": 3,
    "rejection": 4,
    "decision": 3,
    "next_step": 2,
    "open_question": 2,
    "gotcha": 2,
}

LABEL_RE = re.compile(
    r"(?i)\b("
    r"lead\s+constraint|constraint|rejection|reject|"
    r"decision|decided|gotcha|next\s+step|next|"
    r"open\s+question|must\s+remember|blocker|"
    r"important|note|policy"
    r")\s*:\s*"
)

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|\s+[—–]\s+|\s+;\s+")

CONSTRAINT_RE = re.compile(
    r"(?i)\b(must|always|require|shall|cap\b|at\s+most|no\s+longer\s+than|"
    r"longer\s+than|<=|≤|never\s+cache|never\s+log|pii\s+ttl|ttl\s+cap)\b"
)
REJECTION_RE = re.compile(
    r"(?i)\b(reject|don't|do\s+not|never|avoid|instead\s+of|leave\s+\w+\s+alone|"
    r"out\s+of\s+scope|don'?t\s+touch|do\s+not\s+touch)\b"
)
DECISION_RE = re.compile(
    r"(?i)\b(decide[d]?|adopt|go\s+with|we'll|we\s+will|keep\s+\w+|"
    r"for\s+this\s+session|use\s+(?:the\s+)?(?:existing|short-lived|opaque|namespaced)|"
    r"add\s+namespaced|invalidate\s+on)\b"
)
NEXT_RE = re.compile(
    r"(?i)\b(next(?:\s+step)?|todo|then\s+(?:fix|patch|migrate)|patch\s+cache)\b"
)
OPEN_RE = re.compile(
    r"(?i)\b(open\s+question|whether|should\s+we)\b"
)
GOTCHA_RE = re.compile(
    r"(?i)\b(gotcha|looks\s+like|careful|watch\s+out|stampede|missing\s+cache\s+key)\b"
)

META_RE = re.compile(
    r"(?i)^(i('ll| will)\s+(inspect|look|check|edit|park)|"
    r"looks\s+ok|hmm+|hey\s+so|can\s+you\s+(?:just\s+)?(?:look|check|also)|"
    r"whatever\s+you\s+think|save\s+that\s+for\s+later|"
    r"i\s+gotta\s+jump|will\s+remember\s+that|will\s+edit|"
    r"actually\s+never\s+mind|or\s+maybe\s+its|or\s+maybe\s+it's|"
    r"my\s+lead\s+said|just\s+don'?t\s+forget|parking\s+)\b"
)

JUNK_RE = re.compile(
    r"(?i)\b(never\s+mind|gotta\s+jump|drives\s+me\s+crazy|"
    r"sounds\s+right-ish|whatever\s+you\s+think|safe\s+to\s+treat)\b"
)

LABEL_KIND = {
    "lead constraint": "constraint",
    "constraint": "constraint",
    "must remember": "constraint",
    "policy": "constraint",
    "important": "constraint",
    "blocker": "constraint",
    "rejection": "rejection",
    "reject": "rejection",
    "decision": "decision",
    "decided": "decision",
    "gotcha": "gotcha",
    "note": "gotcha",
    "next step": "next_step",
    "next": "next_step",
    "open question": "open_question",
}

KIND_TIER = {
    "constraint": "A",
    "rejection": "A",
    "decision": "A",
    "next_step": "A",
    "open_question": "A",
    "gotcha": "B",
}

# Theme buckets for near-dup collapse across paraphrases.
THEME_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("pii_ttl", re.compile(r"(?i)\b(pii|ttl|cache\s+pii|longer\s+than\s+\d+)\b")),
    ("ci_retry", re.compile(r"(?i)\b(silently\s+retry|retry.*\bci\b|flaky\s+.*(?:ci|test))\b")),
    ("deploy", re.compile(r"(?i)\bdeploy\b")),
    ("cache_lib", re.compile(r"(?i)\b(cache\s+library|redis\s+client|new\s+library)\b")),
    ("worker", re.compile(r"(?i)\bworker\b")),
    ("cache_ttl_keep", re.compile(r"(?i)\b(cache_ttl|bump\s+ttl|keep\s+cache_ttl)\b")),
    ("rename_stale", re.compile(r"(?i)\b(rename|stale|key\s+version)\b")),
    ("get_user_cache", re.compile(r"(?i)\b(get_user|caching\s+get_user|live-?reads)\b")),
    ("staging_redis", re.compile(r"(?i)\b(staging\s+redis|redis\s+flush)\b")),
    ("rate_limit", re.compile(r"(?i)\b(rate\s*limit|throttle|quota)\b")),
    ("idempotency", re.compile(r"(?i)\b(idempotenc|idempotent)\b")),
    ("webhook", re.compile(r"(?i)\bwebhook\b")),
    ("feature_flag", re.compile(r"(?i)\b(feature\s*flag|kill\s*switch)\b")),
    ("payment", re.compile(r"(?i)\b(payment|stripe|charge)\b")),
]


@dataclass(frozen=True)
class Claim:
    kind: str
    statement: str
    tier: str
    source_type: str
    source_obs_id: str | None = None
    labeled: bool = False


def _norm_key(text: str) -> str:
    t = re.sub(r"[^a-z0-9\s]+", " ", (text or "").lower())
    return re.sub(r"\s+", " ", t).strip()


def _token_set(text: str) -> set[str]:
    return {t for t in _norm_key(text).split() if len(t) > 2}


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def _theme_keys(text: str) -> set[str]:
    return {name for name, pat in THEME_PATTERNS if pat.search(text)}


def _clean_statement(text: str) -> str:
    s = (text or "").strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(
        r"^(and|but|also|so|then|oh|wait|okay|ok|cool)\b[\s,]+",
        "",
        s,
        flags=re.I,
    )
    s = s.strip(" \t-—–:;")
    # Normalize common eng-memory phrasings into imperative Anchor form.
    s = re.sub(r"(?i)^i will avoid\b", "Do not touch", s)
    s = re.sub(r"(?i)^avoid\b", "Do not", s)
    s = re.sub(r"(?i)^leave (the )?(\w+) alone\b", r"Do not change the \2", s)
    s = re.sub(r"(?i)^don'?t forget\b", "Must keep", s)
    s = re.sub(r"(?i)^just don'?t forget\b", "Must keep", s)
    if len(s) > CLAIM_SOFT_MAX:
        cut = s[:CLAIM_SOFT_MAX]
        for sep in (", ", "; ", " — ", " - "):
            idx = cut.rfind(sep)
            if idx >= CLAIM_MIN:
                cut = cut[:idx]
                break
        s = cut.rstrip(" ,;")
    if len(s) > ANCHOR_STATEMENT_MAX:
        s = s[: ANCHOR_STATEMENT_MAX - 1].rstrip() + "…"
    s = s.rstrip(".")
    if s and s[0].islower():
        s = s[0].upper() + s[1:]
    return s


def _expand_policy_list(body: str) -> list[str]:
    """Split 'never A; never B; reject C' style multi-policy bodies."""
    body = (body or "").strip()
    if not body:
        return []
    # Prefer semicolon / em-dash lists when multiple policy verbs appear
    verbs = len(re.findall(r"(?i)\b(never|do\s+not|don't|reject|avoid|must)\b", body))
    if verbs >= 2 or ";" in body:
        parts = re.split(r"\s*;\s*|\s+[—–]\s*", body)
        out = [p.strip() for p in parts if p.strip()]
        if len(out) >= 2:
            return out
    return [body]


def _split_labeled_units(label: str, body: str) -> list[str]:
    """Emit `label: unit` clauses; re-label follow-on units by content."""
    body = (body or "").strip()
    if not body:
        return []
    # Sentence-split first so "Open question: … For this session: …" separates.
    units = [u.strip() for u in SENTENCE_SPLIT_RE.split(body) if u.strip()]
    expanded: list[str] = []
    for u in units:
        bits = _expand_policy_list(u)
        expanded.extend(bits if bits else [u])

    out: list[str] = []
    for i, unit in enumerate(expanded):
        unit = unit.strip()
        if not unit:
            continue
        if i == 0:
            out.append(f"{label}: {unit}")
            continue
        # Follow-on units: classify on their own (don't inherit open_question etc.)
        uk, ubody, _ = classify_clause_unlabeled(unit)
        if uk:
            # Map kind back to a synthetic label for _kind_from_label
            synth = {
                "constraint": "constraint",
                "rejection": "rejection",
                "decision": "decision",
                "next_step": "next",
                "open_question": "open question",
                "gotcha": "gotcha",
            }[uk]
            out.append(f"{synth}: {ubody}")
        else:
            out.append(unit)
    return out


def _split_clauses(text: str) -> list[str]:
    raw = (text or "").strip()
    if not raw:
        return []
    parts: list[str] = []
    matches = list(LABEL_RE.finditer(raw))
    if matches:
        for i, m in enumerate(matches):
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
            body = raw[start:end].strip()
            label = m.group(1).lower()
            if not body:
                continue
            parts.extend(_split_labeled_units(label, body))
        preface = raw[: matches[0].start()].strip()
        if preface:
            parts = [preface, *parts]
    else:
        parts = [raw]

    out: list[str] = []
    for p in parts:
        if re.match(
            r"(?i)^(lead\s+constraint|constraint|rejection|reject|decision|decided|"
            r"gotcha|next\s+step|next|open\s+question|must\s+remember|blocker|"
            r"important|note|policy)\s*:",
            p,
        ):
            out.append(p.strip())
            continue
        bits = SENTENCE_SPLIT_RE.split(p)
        for b in bits:
            b = b.strip()
            if not b:
                continue
            if len(b) > CLAIM_SOFT_MAX and " also " in b.lower():
                out.extend(x.strip() for x in re.split(r"(?i)\balso\b", b) if x.strip())
            else:
                out.append(b)
    return out


def _kind_from_label(clause: str) -> tuple[str | None, str, bool]:
    m = re.match(
        r"(?i)^(lead\s+constraint|constraint|rejection|reject|decision|decided|"
        r"gotcha|next\s+step|next|open\s+question|must\s+remember|blocker|"
        r"important|note|policy)\s*:\s*(.+)$",
        clause.strip(),
        flags=re.DOTALL,
    )
    if not m:
        return None, clause, False
    label = m.group(1).lower()
    body = m.group(2).strip()
    kind = LABEL_KIND.get(label)
    # "must remember: never silently retry…" → reclassify unit by content
    if label in {"must remember", "important", "policy"}:
        unit_kind, _, _ = classify_clause_unlabeled(body)
        if unit_kind:
            return unit_kind, body, True
    return kind, body, bool(kind)


def classify_clause_unlabeled(body: str) -> tuple[str | None, str, bool]:
    body = body.strip()
    if CONSTRAINT_RE.search(body) and REJECTION_RE.search(body):
        if re.search(r"(?i)\b(pii|ttl|secret|token|password|longer\s+than|cap)\b", body):
            return "constraint", body, False
    if CONSTRAINT_RE.search(body):
        return "constraint", body, False
    if REJECTION_RE.search(body):
        return "rejection", body, False
    if DECISION_RE.search(body):
        return "decision", body, False
    if NEXT_RE.search(body) and not OPEN_RE.search(body):
        return "next_step", body, False
    if OPEN_RE.search(body) or (body.endswith("?") and re.search(r"(?i)\b(should|whether)\b", body)):
        return "open_question", body, False
    if GOTCHA_RE.search(body):
        return "gotcha", body, False
    return None, body, False


def classify_clause(clause: str) -> tuple[str | None, str, bool]:
    kind, body, labeled = _kind_from_label(clause)
    body = body.strip()
    if kind:
        # If labeled constraint body is clearly a rejection unit, prefer rejection
        if kind == "constraint" and labeled:
            uk, _, _ = classify_clause_unlabeled(body)
            if uk in {"rejection", "decision", "next_step", "open_question"} and not CONSTRAINT_RE.search(
                body
            ):
                return uk, body, True
        return kind, body, True
    return classify_clause_unlabeled(body)


def _accept_source(obs_type: str, kind: str, labeled: bool) -> bool:
    if obs_type in {"user_prompt", "agent_response", "note"}:
        return True
    if obs_type == "file_edit":
        return kind in {"next_step", "gotcha"} and labeled
    if obs_type == "tool_result":
        return labeled or kind in {"constraint", "rejection"}
    return labeled


def _is_junk(stmt: str, kind: str, labeled: bool) -> bool:
    if META_RE.search(stmt) or JUNK_RE.search(stmt):
        return True
    if not labeled and kind == "open_question":
        # Soft chat questions without whether/should we
        if not re.search(r"(?i)\b(whether|should\s+we|open\s+question)\b", stmt):
            return True
        # Anaphoric questions with no durable noun ("should we raise it?")
        if re.search(r"(?i)\b(it|that|this|them)\s*\?*$", stmt) and not re.search(
            r"(?i)\b(rate|limit|cache|flag|webhook|payment|ttl|sdk|deploy|worker)\b",
            stmt,
        ):
            return True
    if not labeled and kind == "next_step" and re.search(r"(?i)^will\s+edit\b", stmt):
        return True
    if not labeled and kind == "constraint" and re.search(
        r"(?i)^(my\s+lead\s+said|just\s+don'?t\s+forget)\b", stmt
    ):
        # Prefer crisp agent-labeled constraint; keep only if unique theme later
        return False  # theme dedupe handles
    return False


def extract_claims_from_text(
    text: str,
    *,
    source_type: str = "note",
    source_obs_id: str | None = None,
) -> list[Claim]:
    claims: list[Claim] = []
    for clause in _split_clauses(text):
        kind, body, labeled = classify_clause(clause)
        if kind is None:
            continue
        if not _accept_source(source_type, kind, labeled):
            continue
        stmt = _clean_statement(body)
        if len(stmt) < CLAIM_MIN:
            continue
        if _is_junk(stmt, kind, labeled):
            continue
        if kind != "open_question" and stmt.endswith("?") and not labeled:
            if OPEN_RE.search(stmt):
                kind = "open_question"
            else:
                continue
        tier = KIND_TIER.get(kind, "C")
        claims.append(
            Claim(
                kind=kind,
                statement=stmt,
                tier=tier,
                source_type=source_type,
                source_obs_id=source_obs_id,
                labeled=labeled,
            )
        )
    return claims


def dedupe_claims(claims: Iterable[Claim], *, jaccard_tau: float = 0.55) -> list[Claim]:
    """Keep labeled/short claims; collapse paraphrases by theme + Jaccard."""
    kind_rank = {
        "constraint": 0,
        "rejection": 1,
        "decision": 2,
        "next_step": 3,
        "open_question": 4,
        "gotcha": 5,
    }

    def _priority(c: Claim) -> tuple:
        themes = _theme_keys(c.statement)
        # Prefer claims that map to known eng-memory themes
        theme_boost = 0 if themes else 1
        return (
            0 if c.labeled else 1,
            theme_boost,
            kind_rank.get(c.kind, 9),
            0 if c.source_type == "agent_response" else 1,
            len(c.statement),
        )

    ordered = sorted(claims, key=_priority)
    kept: list[Claim] = []
    kept_tokens: list[set[str]] = []
    kept_keys: list[str] = []
    kept_themes: list[tuple[str, frozenset[str]]] = []
    covered_themes: set[str] = set()
    per_kind: dict[str, int] = {}

    for c in ordered:
        key = _norm_key(c.statement)
        if not key:
            continue
        toks = _token_set(c.statement)
        themes = _theme_keys(c.statement)
        dup = False
        for k, t, (knd, th) in zip(kept_keys, kept_tokens, kept_themes):
            if key == k or key in k or k in key:
                dup = True
                break
            if _jaccard(toks, t) >= jaccard_tau:
                dup = True
                break
            if c.kind == knd and themes and th and (themes & th):
                dup = True
                break
        if dup:
            continue
        # Soft cap: allow +1 when claim introduces a new uncovered theme
        cap = MAX_PER_KIND.get(c.kind, 3)
        if per_kind.get(c.kind, 0) >= cap:
            if not (themes - covered_themes):
                continue
            if per_kind.get(c.kind, 0) >= cap + 2:
                continue
        kept.append(c)
        kept_keys.append(key)
        kept_tokens.append(toks)
        kept_themes.append((c.kind, frozenset(themes)))
        covered_themes |= themes
        per_kind[c.kind] = per_kind.get(c.kind, 0) + 1
    return kept


def extract_claims_from_span(span: list[dict[str, Any]]) -> list[Claim]:
    """Extract + dedupe durable claims across an observation span."""
    raw: list[Claim] = []
    for obs in span:
        text = (obs.get("summary") or "").strip()
        if not text:
            continue
        raw.extend(
            extract_claims_from_text(
                text,
                source_type=str(obs.get("type") or "note"),
                source_obs_id=obs.get("id"),
            )
        )
    return dedupe_claims(raw)
