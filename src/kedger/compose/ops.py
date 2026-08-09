"""Layer-1 OpSet vs Layer-2 projection (P4 parallel compose)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ConflictSet:
    conflicts: list[dict[str, Any]] = field(default_factory=list)

    def add(
        self,
        *,
        kind: str,
        left: dict[str, Any],
        right: dict[str, Any],
        action: str,
    ) -> None:
        self.conflicts.append(
            {
                "type": kind,
                "left_id": left.get("id"),
                "right_id": right.get("id"),
                "action": action,
                "left_kind": left.get("kind"),
                "right_kind": right.get("kind"),
            }
        )


_STOP = frozenset(
    {
        "a",
        "an",
        "the",
        "and",
        "or",
        "for",
        "to",
        "of",
        "in",
        "on",
        "is",
        "are",
        "be",
        "with",
        "from",
        "that",
        "this",
        "into",
        "must",
        "use",
        "using",
        "should",
        "do",
        "not",
        "dont",
        "never",
        "avoid",
        "keep",
        "add",
        "via",
    }
)

# Same-family hits → true alternative/conflict; disjoint families → complementary.
_FAMILIES: tuple[frozenset[str], ...] = (
    frozenset({"jwt", "cookie", "cookies", "session", "sessions", "bearer", "oauth", "auth"}),
    frozenset({"redis", "memcached", "cache", "caching", "ttl"}),
    frozenset({"deploy", "deployment", "region", "us", "east", "eu", "west"}),
    frozenset({"postgres", "mysql", "sqlite", "database", "db"}),
    frozenset({"rate", "limit", "throttle", "quota"}),
    frozenset({"payment", "payments", "stripe", "webhook", "webhooks", "idempotency"}),
    frozenset({"pii", "secret", "secrets", "token", "tokens", "password"}),
    frozenset({"ci", "retry", "flaky", "test", "tests"}),
    frozenset({"worker", "workers", "queue", "job", "jobs"}),
    frozenset({"library", "client", "sdk", "dependency"}),
    frozenset({"feature", "flag", "flags", "kill", "switch"}),
)


def _tokens(text: str) -> set[str]:
    raw = re.sub(r"[^a-z0-9\s-]+", " ", (text or "").lower())
    parts = re.split(r"[\s-]+", raw)
    return {p for p in parts if len(p) > 1 and p not in _STOP}


def _skeleton(text: str) -> str:
    """Replace concrete alternatives with SLOT so 'must use JWT' ~ 'must use cookies'."""
    s = re.sub(r"[^a-z0-9\s-]+", " ", (text or "").lower())
    s = re.sub(r"\b(us|eu)-[a-z]+-\d+\b", "slot", s)
    s = re.sub(r"\b\d+[smhd]?\b", "slot", s)
    # multi-word tech first
    for word in sorted({w for fam in _FAMILIES for w in fam}, key=len, reverse=True):
        s = re.sub(rf"\b{re.escape(word)}\b", "slot", s)
    return re.sub(r"\s+", " ", s).strip()


def _family_ids(tokens: set[str]) -> set[int]:
    hits: set[int] = set()
    for i, fam in enumerate(_FAMILIES):
        if tokens & fam:
            hits.add(i)
    return hits


def _likely_same_slot_conflict(sa: str, sb: str, *, kind: str) -> bool:
    """True when two same-kind Anchors are alternatives, not parallel policies."""
    if not sa or not sb:
        return False
    if _skeleton(sa) == _skeleton(sb) and sa != sb:
        return True
    ta, tb = _tokens(sa), _tokens(sb)
    if not ta or not tb:
        return False
    inter = ta & tb
    union = ta | tb
    jacc = len(inter) / len(union) if union else 0.0
    if jacc >= 0.4:
        return True
    fam_inter = _family_ids(ta) & _family_ids(tb)
    # Decisions in the same domain family are usually alternatives (Redis vs JWT).
    if kind == "decision" and fam_inter:
        return True
    # Constraints/rejections only conflict when family overlap is also lexical.
    if kind in {"constraint", "rejection"} and fam_inter and jacc >= 0.25:
        return True
    return False


def classify(a: dict[str, Any], b: dict[str, Any]) -> str:
    """Classify before near-dup rejection (MemClaw ordering)."""
    sa = (a.get("statement") or "").strip().lower()
    sb = (b.get("statement") or "").strip().lower()
    if sa == sb and a.get("kind") == b.get("kind"):
        return "duplicate"
    if sa in sb or sb in sa:
        return "refinement"
    if a.get("kind") != b.get("kind"):
        return "complementary"
    # same kind, different statement — only some are true contradictions
    if a.get("kind") in {"constraint", "rejection", "decision"}:
        if _likely_same_slot_conflict(sa, sb, kind=str(a.get("kind"))):
            return "contradiction"
        return "complementary"
    return "temporal"


def kind_policy(conflict_type: str, left: dict[str, Any], right: dict[str, Any]) -> str:
    """Return ADD | NOOP | ESCALATE."""
    kinds = {left.get("kind"), right.get("kind")}
    if conflict_type == "duplicate":
        return "NOOP"
    if conflict_type == "complementary":
        return "ADD"
    if conflict_type == "refinement":
        return "ADD"
    if "constraint" in kinds and conflict_type == "contradiction":
        return "ESCALATE"
    if "rejection" in kinds and conflict_type == "contradiction":
        return "ESCALATE"
    if conflict_type == "contradiction" and "decision" in kinds:
        # user>agent: prefer explicit source
        src_l = (left.get("provenance") or {}).get("source")
        src_r = (right.get("provenance") or {}).get("source")
        if src_l == "explicit" and src_r != "explicit":
            return "NOOP"  # keep left
        if src_r == "explicit" and src_l != "explicit":
            return "ADD"  # prefer right via caller
        return "ESCALATE"
    if conflict_type in {"complementary", "refinement", "temporal"}:
        return "ADD"
    return "ESCALATE"


def compose_view(anchors: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], ConflictSet]:
    """Layer-2 projection — does not mutate base anchors."""
    cs = ConflictSet()
    kept: list[dict[str, Any]] = []
    for anc in anchors:
        if anc.get("status") != "active":
            continue
        action = "ADD"
        for existing in kept:
            ctype = classify(existing, anc)
            if ctype == "complementary":
                continue
            policy = kind_policy(ctype, existing, anc)
            if policy == "NOOP":
                action = "NOOP"
                cs.add(kind=ctype, left=existing, right=anc, action=policy)
                break
            if policy == "ESCALATE":
                action = "ESCALATE"
                cs.add(kind=ctype, left=existing, right=anc, action=policy)
                break
            if policy == "ADD":
                continue
        if action == "ADD":
            kept.append(anc)
    return kept, cs


def merge_working_states(
    primary: dict[str, Any], secondary: dict[str, Any]
) -> dict[str, Any]:
    """Field-wise merge for parallel hydrate."""
    out = dict(primary)
    files = list(dict.fromkeys((primary.get("files_in_flight") or []) + (secondary.get("files_in_flight") or [])))
    out["files_in_flight"] = files[:40]
    qs = list(dict.fromkeys((primary.get("open_questions") or []) + (secondary.get("open_questions") or [])))
    out["open_questions"] = qs
    if primary.get("goal") and secondary.get("goal") and primary["goal"] != secondary["goal"]:
        out.setdefault("open_questions", []).append(
            f"Conflict goals: {primary['goal']!r} vs {secondary['goal']!r}"
        )
        out.setdefault("conflicts", []).append({"field": "goal", "action": "ESCALATE"})
    return out
