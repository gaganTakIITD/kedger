#!/usr/bin/env python3
"""Return routing engine — corrected reference implementation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class CategoryRule:
    category: str
    returnable: bool
    allowed_return_window_days: int


@dataclass
class ScoreRange:
    min: int
    max: int
    points: int


@dataclass
class ScoringRule:
    attribute: str
    ranges: list[ScoreRange]


@dataclass
class DecisionBand:
    min: int
    max: int
    decision: str
    reason: str | None


@dataclass
class ReturnRequest:
    request_id: str
    account_id: str
    category: str
    days_since_purchase: int
    order_value_usd: float
    account_age_days: int


class Engine:
    def __init__(
        self,
        categories: dict[str, CategoryRule],
        scoring_rules: list[ScoringRule],
        decision_bands: list[DecisionBand],
        account_profiles: dict[str, int],
        account_groups: dict[str, set[str]],
    ) -> None:
        self.categories = categories
        self.scoring_rules = scoring_rules
        self.decision_bands = decision_bands
        self.account_profiles = account_profiles
        self.account_groups = account_groups

    @classmethod
    def build(
        cls,
        categories: list[CategoryRule],
        scoring_rules: list[ScoringRule],
        decision_bands: list[DecisionBand],
        account_profiles: dict[str, int],
        links: list[tuple[str, str]],
    ) -> "Engine":
        # FIX: undirected edges (both directions)
        groups: dict[str, set[str]] = {}
        for primary, related in links:
            groups.setdefault(primary, set()).add(related)
            groups.setdefault(related, set()).add(primary)

        # Transitive closure so every member sees every other
        changed = True
        while changed:
            changed = False
            for account_id, members in list(groups.items()):
                expanded = set(members)
                for member in members:
                    for transitive in groups.get(member, ()):
                        if transitive != account_id and transitive not in expanded:
                            expanded.add(transitive)
                            changed = True
                groups[account_id] = expanded

        for account_id, members in groups.items():
            members.add(account_id)

        return cls(
            categories={c.category: c for c in categories},
            scoring_rules=scoring_rules,
            decision_bands=decision_bands,
            account_profiles=account_profiles,
            account_groups=groups,
        )

    def linked_return_history(self, account_id: str) -> int:
        members = self.account_groups.get(account_id)
        if members is None:
            return self.account_profiles.get(account_id, 0)
        return sum(self.account_profiles.get(m, 0) for m in members)

    def score_request(self, request: ReturnRequest, return_history_count: int) -> int:
        attrs = {
            "account_age_days": float(request.account_age_days),
            "return_history_count": float(return_history_count),
            "order_value_usd": float(request.order_value_usd),
        }
        score = 0
        for rule in self.scoring_rules:
            value = attrs.get(rule.attribute)
            if value is None:
                continue
            for rng in rule.ranges:
                if rng.min <= value <= rng.max:
                    score += rng.points
                    break
        return max(0, min(100, score))

    def route(self, request: ReturnRequest) -> dict[str, Any]:
        cat = self.categories.get(request.category)
        if cat is None or not cat.returnable:
            return {
                "request_id": request.request_id,
                "risk_score": None,
                "decision": "REJECT",
                "reason": "CATEGORY_NON_RETURNABLE",
            }

        if request.days_since_purchase > cat.allowed_return_window_days:
            return {
                "request_id": request.request_id,
                "risk_score": None,
                "decision": "REJECT",
                "reason": "RETURN_WINDOW_EXPIRED",
            }

        history = self.linked_return_history(request.account_id)
        risk_score = self.score_request(request, history)

        band = next(
            (b for b in self.decision_bands if b.min <= risk_score <= b.max),
            None,
        )
        if band is None:
            return {
                "request_id": request.request_id,
                "risk_score": risk_score,
                "decision": "REJECT",
                "reason": "HIGH_RISK_SCORE",
            }

        out: dict[str, Any] = {
            "request_id": request.request_id,
            "risk_score": risk_score,
            "decision": band.decision,
        }
        if band.reason:
            out["reason"] = band.reason
        return out


def load_engine(data_dir: Path) -> Engine:
    categories_doc = json.loads((data_dir / "category_rules.json").read_text())
    scoring_doc = json.loads((data_dir / "scoring_rules.json").read_text())
    bands_doc = json.loads((data_dir / "decision_bands.json").read_text())

    categories = [
        CategoryRule(
            category=c["category"],
            returnable=c["returnable"],
            allowed_return_window_days=c["allowed_return_window_days"],
        )
        for c in categories_doc["categories"]
    ]
    scoring_rules = [
        ScoringRule(
            attribute=r["attribute"],
            ranges=[ScoreRange(**rng) for rng in r["ranges"]],
        )
        for r in scoring_doc["rules"]
    ]
    bands = [
        DecisionBand(
            min=b["min"],
            max=b["max"],
            decision=b["decision"],
            reason=b["reason"],
        )
        for b in bands_doc["bands"]
    ]

    profiles: dict[str, int] = {}
    for line in (data_dir / "account_profiles.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        profiles[row["account_id"]] = int(row["return_history_count"])

    links: list[tuple[str, str]] = []
    for line in (data_dir / "account_links.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        links.append((row["primary_account_id"], row["related_account_id"]))

    return Engine.build(categories, scoring_rules, bands, profiles, links)


def load_requests(data_dir: Path) -> list[ReturnRequest]:
    requests: list[ReturnRequest] = []
    for line in (data_dir / "requests.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        requests.append(
            ReturnRequest(
                request_id=row["request_id"],
                account_id=row["account_id"],
                category=row["category"],
                days_since_purchase=int(row["days_since_purchase"]),
                order_value_usd=float(row.get("order_value_usd", 0)),
                account_age_days=int(row.get("account_age_days", 0)),
            )
        )
    return requests
