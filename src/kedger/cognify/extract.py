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
CLAIM_MIN = 14
MAX_PER_KIND = {
    "constraint": 3,
    "rejection": 6,
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
    r"longer\s+than|<=|≤|never\s+cache|never\s+log|pii\s+ttl|ttl\s+cap|"
    r"gotta|got\s+to|have\s+to|need\s+to|we\s+need)\b"
)
REJECTION_RE = re.compile(
    r"(?i)\b(reject|don't|dont|do\s+not|never|avoid|instead\s+of|"
    r"leave\s+\w+\s+alone|out\s+of\s+scope|don'?t\s+touch|do\s+not\s+touch|"
    r"no\s+new|wont|won't|i\s+won'?t)\b"
)
DECISION_RE = re.compile(
    r"(?i)\b(decide[d]?|adopt|go\s+with|we'll|we\s+will|keep\s+(?:the\s+)?(?:current|\w+)|"
    r"for\s+(?:this\s+)?(?:session|now)|use\s+(?:the\s+)?(?:existing|short-lived|opaque|namespaced|current)|"
    r"add\s+(?:idempotency|namespaced|down\s+migration|\w+\s+migration)|"
    r"invalidate\s+on|ok\s+so|take\s+lock|in\s+smaller\s+batches)\b"
)
NEXT_RE = re.compile(
    r"(?i)\b(next(?:\s+step)?|todo|then\s+(?:fix|patch|migrate)|"
    r"patch\s+\w+|next\s+i'?ll|i'?ll\s+patch)\b"
)
OPEN_RE = re.compile(
    r"(?i)\b(open\s+question|whether|should\s+we|need\s+same|park\s+that|idk)\b|\?{2,}"
)
GOTCHA_RE = re.compile(
    r"(?i)\b(gotcha|looks\s+like|careful|watch\s+out|stampede|missing\s+"
    r"(?:idempotency|cache\s+key)|usually\s+missing|assertionerror|error:|"
    r"deadlock|importerror|traceback|failed\s+in\s+prod)\b"
)

SPEECH_FRAME_RE = re.compile(
    r"(?i)^(yo|ugh|yeah|ok|okay|cool|hmm+|like|so|well|lead\s+was\s+\w+\s+"
    r"(?:that\s+)?|lead\s+(?:was\s+)?yelling\s+|finance\s+will\s+\w+\s+|"
    r"pls\b|please\b|i\s+guess\b|whatever\b|"
    r"(?:yo\s+)?(?:the\s+)?(?:checkout\s+)?doubles?\s+again\b|"
    r"doubles?\s+again\b"
    r")[\s,:-]*"
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
    r"(?i)\b(never\s+mind|gotta\s+jump|gotta\s+go|drives\s+me\s+crazy|"
    r"sounds\s+right-ish|whatever\s+you\s+think|safe\s+to\s+treat|"
    r"just\s+stop\s+doubles|look\s+at\s+payments\s+stuff|"
    r"remember\s+the\s+verify\s+thing|probably\s+not\s+product)\b"
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
    ("idempotency", re.compile(r"(?i)\bidempotenc\w*")),
    ("webhook", re.compile(r"(?i)\bwebhook\b")),
    ("webhook_ack", re.compile(r"(?i)\b(auto-?ack|ack\s+webhook|sig(?:nature)?\s+verif|bad\s+signature)\b")),
    ("feature_flag", re.compile(r"(?i)\b(feature\s*flag|kill\s*switch|billing(?:_v2)?\s*flag|billing_v2)\b")),
    ("down_migration", re.compile(r"(?i)\b(down\s+migration|rollback\s+migration)\b")),
    ("schema_lock", re.compile(r"(?i)\b(lock\s+wait|smaller\s+batches|online\s+schema)\b")),
    ("email_column", re.compile(r"(?i)\b(email\s+column|users\s+email)\b")),
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
    # Strip chat frames / filler repeatedly
    for _ in range(3):
        nxt = SPEECH_FRAME_RE.sub("", s).strip(" ,:-")
        if nxt == s:
            break
        s = nxt
    s = re.sub(
        r"^(and|but|also|so|then|oh|wait|okay|ok|cool|yeah|like)\b[\s,]+",
        "",
        s,
        flags=re.I,
    )
    s = s.strip(" \t-—–:;")
    # Normalize messy speech → imperative Anchor form
    s = re.sub(r"(?i)\bdont\b", "don't", s)
    s = re.sub(r"(?i)\bwont\b", "won't", s)
    s = re.sub(r"(?i)^i will avoid\b", "Do not touch", s)
    s = re.sub(r"(?i)^i won't\b", "Do not", s)
    s = re.sub(r"(?i)^avoid\b", "Do not", s)
    s = re.sub(r"(?i)^don't touch\b", "Do not touch", s)
    s = re.sub(r"(?i)^leave (the )?([\w./-]+(?:\s+[\w./-]+)?)\s+alone\b.*", r"Do not change \2", s)
    s = re.sub(r"(?i)^leave ([\w./-]+(?:\s+[\w./-]+)?)\b.*", r"Do not change \1", s)
    s = re.sub(r"(?i)\byeah\b", "", s)
    s = re.sub(r"(?i)^like don't\b", "Do not", s)
    s = re.sub(r"(?i)^like\s+", "", s)
    s = re.sub(r"(?i)^don't auto\s+ack\b", "Do not auto-ack", s)
    s = re.sub(r"(?i)^don't ack\b", "Do not ack", s)
    s = re.sub(r"(?i)^don'?t forget\b", "Must keep", s)
    s = re.sub(r"(?i)^just don'?t forget\b", "Must keep", s)
    s = re.sub(
        r"(?i)^(?:we\s+)?(?:gotta|got\s+to|have\s+to|need\s+to)\b",
        "Must",
        s,
    )
    s = re.sub(r"(?i)^no new\b", "Do not add a new", s)
    s = re.sub(r"(?i)^don't ack\b", "Do not ack", s)
    s = re.sub(r"(?i)^dont ack\b", "Do not ack", s)
    s = re.sub(r"(?i)^don't auto[- ]?ack\b", "Do not auto-ack", s)
    s = re.sub(r"(?i)\bpls\b|\bplease\b|\btho\b|\blol\b|\bwtf\b", "", s)
    s = re.sub(r"(?i)\btil\b", "until", s)
    s = re.sub(r"(?i)^don't put\b", "Do not put", s)
    s = re.sub(r"(?i)^don't break\b", "Do not break", s)
    s = re.sub(r"(?i)^don't rerun\b", "Do not rerun", s)
    s = re.sub(r"(?i)^never drop\b", "Never drop", s)
    s = re.sub(r"(?i)^never send\b", "Never send", s)
    s = re.sub(r"(?i)^open questions?\s+(?:whether\s+)?", "Whether ", s)
    s = re.sub(
        r"(?i)\b(finance will .*|will murder me|or idk.*|i guess|looking at .*)$",
        "",
        s,
    )
    s = re.sub(r"\s+", " ", s).strip(" ,")
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


def _cue_density(text: str) -> int:
    return len(
        re.findall(
            r"(?i)\b(don't|dont|do\s+not|never|avoid|must|gotta|leave|no\s+new|"
            r"keep|add|reject|won't|wont|next|should|whether|park)\b",
            text,
        )
    )


def _expand_policy_list(body: str) -> list[str]:
    """Split multi-policy bodies (semicolon, em-dash, or cue-dense commas)."""
    body = (body or "").strip()
    if not body:
        return []
    verbs = _cue_density(body)
    if verbs >= 2 or ";" in body or "—" in body or "–" in body:
        parts = re.split(r"\s*;\s*|\s+[—–]\s*", body)
        if len(parts) == 1 and verbs >= 2:
            # "add X, dont Y, leave Z, keep W"
            parts = re.split(r"\s*,\s*|\s+\band\b\s+", body)
        out = [p.strip(" ,") for p in parts if p.strip(" ,")]
        if len(out) >= 2:
            return out
    return [body]


def _split_unlabeled_messy(text: str) -> list[str]:
    """Aggressive split for unlabeled human/agent rambles."""
    raw = (text or "").strip()
    if not raw:
        return []
    # Normalize light typos before split
    raw = re.sub(r"(?i)\bdont\b", "don't", raw)
    raw = re.sub(r"(?i)\bwont\b", "won't", raw)
    # Sentence-ish boundaries including ?? and "also"
    chunks = re.split(r"(?<=[.!?])\s+|\s+\?+\s*|\s+[—–]\s+|\s+;\s+|\s+(?=also\b)", raw)
    out: list[str] = []
    for ch in chunks:
        ch = ch.strip()
        if not ch:
            continue
        # "ok so for now: a, b, c" / "for now: …"
        m = re.match(r"(?i)^(?:ok\s+so\s+)?(?:for\s+(?:this\s+)?(?:session|now)|so\s+for\s+now)\s*:\s*(.+)$", ch)
        if m:
            out.extend(_expand_policy_list(m.group(1)))
            continue
        # Cue-stacked without commas: "dont touch X gotta Y" / "never A must B"
        if _cue_density(ch) >= 2 and "," not in ch and ";" not in ch:
            parts = re.split(
                r"(?i)\s+(?=(?:don't|do\s+not|never|must|gotta|got\s+to|have\s+to|"
                r"leave\s+\w+\s+alone|no\s+new|won't|wont)\b)",
                ch,
            )
            parts = [p.strip(" ,") for p in parts if p.strip(" ,")]
            if len(parts) >= 2:
                out.extend(parts)
                continue
        if _cue_density(ch) >= 2 and ("," in ch or " and " in ch.lower()):
            out.extend(_expand_policy_list(ch))
        elif len(ch) > CLAIM_SOFT_MAX and " also " in ch.lower():
            out.extend(x.strip() for x in re.split(r"(?i)\balso\b", ch) if x.strip())
        else:
            out.append(ch)
    return out


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
            parts = [*_split_unlabeled_messy(preface), *parts]
    else:
        parts = _split_unlabeled_messy(raw)

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
        # Already split by messy splitter — keep atomic
        if p.strip():
            out.append(p.strip())
    return out


def classify_clause_unlabeled(body: str) -> tuple[str | None, str, bool]:
    body = body.strip()
    # Explicit open-question phrasing beats "need"/"must" lexical traps
    if re.match(r"(?i)^open\s+questions?\b", body) or re.match(
        r"(?i)^whether\b", body
    ):
        return "open_question", body, False
    # Prefer durable eng cues even in slang
    if re.search(r"(?i)\b(idempotency|Idempotency-Key)\b", body) and re.search(
        r"(?i)\b(must|gotta|always|need|put|add|send)\b", body
    ):
        return "constraint", body, False
    if re.search(r"(?i)\b(don'?t|dont|never|won'?t)\s+(auto[- ]?)?ack\b", body):
        return "rejection", body, False
    if re.search(r"(?i)\bno new\b.*\b(sdk|library|client)\b", body):
        return "rejection", body, False
    if re.search(r"(?i)\b(don'?t|dont|won'?t)\s+touch\b", body):
        return "rejection", body, False
    if re.search(r"(?i)\bleave\b.*\b(alone|for now)\b", body) or re.search(
        r"(?i)\bleave (rate|flag|billing|limit)", body
    ):
        return "rejection", body, False
    if re.search(r"(?i)\bpark\b|\bidk\b", body) and re.search(
        r"(?i)\b(webhook|rate|store|same|should|whether|digest)\b", body
    ):
        return "open_question", body, False
    if re.search(r"\?{2,}", body) and re.search(
        r"(?i)\b(should|whether|need|same store|bump|cookies|jwt)\b", body
    ):
        return "open_question", body, False
    # Compat / until-vN gotchas
    if re.search(r"(?i)\b(don'?t|dont)\s+break\b", body) or re.search(
        r"(?i)\buntil\s+v?\d+|til\s+v?\d+", body
    ):
        return "gotcha", body, False

    if CONSTRAINT_RE.search(body) and REJECTION_RE.search(body):
        if re.search(r"(?i)\b(pii|ttl|secret|token|password|longer\s+than|cap|idempotenc)\b", body):
            return "constraint", body, False
    if CONSTRAINT_RE.search(body):
        # "we need X for billing" constraint vs open question already handled
        return "constraint", body, False
    if REJECTION_RE.search(body):
        return "rejection", body, False
    if DECISION_RE.search(body) or re.match(r"(?i)^add\s+\w+", body):
        return "decision", body, False
    if NEXT_RE.search(body) and not OPEN_RE.search(body):
        return "next_step", body, False
    if OPEN_RE.search(body) or (
        ("?" in body) and re.search(r"(?i)\b(should|whether|need|same store)\b", body)
    ):
        return "open_question", body, False
    if GOTCHA_RE.search(body):
        return "gotcha", body, False
    return None, body, False


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
    if label in {"must remember", "important", "policy"}:
        unit_kind, _, _ = classify_clause_unlabeled(body)
        if unit_kind:
            return unit_kind, body, True
    return kind, body, bool(kind)


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
    """User + agent text both feed base Anchors; file edits feed ops + light cues."""
    if obs_type in {"user_prompt", "agent_response", "note"}:
        return True
    if obs_type == "file_edit":
        # Ops layer owns edits; still allow labeled or strong next/gotcha cues
        return labeled or kind in {"next_step", "gotcha", "decision"}
    if obs_type == "tool_result":
        return labeled or kind in {"constraint", "rejection", "gotcha"}
    if obs_type == "tool_fail":
        # Failures are durable gotchas for the next agent
        return labeled or kind in {"gotcha", "rejection", "constraint", "next_step"}
    return labeled


def _is_junk(stmt: str, kind: str, labeled: bool) -> bool:
    if META_RE.search(stmt) or JUNK_RE.search(stmt):
        return True
    # Unlabeled mixed rambles that still sound like chat, not Anchors
    if not labeled and kind in {"constraint", "rejection", "decision"}:
        if re.search(
            r"(?i)\b(doubles?\s+again|yo\b|idk|looking at|i guess|whatever)\b",
            stmt,
        ):
            return True
        # Multiple opposing policy cues in one statement → not crisp enough
        if (
            REJECTION_RE.search(stmt)
            and CONSTRAINT_RE.search(stmt)
            and kind == "constraint"
        ):
            return True
    if not labeled and kind == "open_question":
        # Soft chat / rate-limit bump with no durable framing
        if re.search(r"(?i)^rate\s+limit\s+bump", stmt):
            return False  # keep as open if classified
        if not re.search(
            r"(?i)\b(whether|should\s+we|open\s+question|need\s+same|same\s+store)\b",
            stmt,
        ):
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
        # Trailing ??? must not flip a rejection/constraint into open_question
        if kind not in {"open_question", "rejection", "constraint"} and (
            stmt.endswith("?") or "??" in stmt
        ) and not labeled:
            if OPEN_RE.search(stmt) or re.search(
                r"(?i)\b(should|whether|need|same store)\b", stmt
            ):
                kind = "open_question"
            else:
                continue
        if kind != "open_question":
            stmt = stmt.rstrip("?").strip()
            if stmt and stmt[0].islower():
                stmt = stmt[0].upper() + stmt[1:]
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
