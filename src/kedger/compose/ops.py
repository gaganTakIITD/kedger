"""Layer-1 OpSet vs Layer-2 projection (P4 parallel compose)."""

from __future__ import annotations

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
    # same kind, different statement — possible contradiction for constraints/rejections
    if a.get("kind") in {"constraint", "rejection", "decision"}:
        return "contradiction"
    return "temporal"


def kind_policy(conflict_type: str, left: dict[str, Any], right: dict[str, Any]) -> str:
    """Return ADD | NOOP | ESCALATE."""
    kinds = {left.get("kind"), right.get("kind")}
    if "constraint" in kinds:
        return "ESCALATE"
    if conflict_type == "duplicate":
        return "NOOP"
    if "rejection" in kinds:
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
