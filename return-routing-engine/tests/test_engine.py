#!/usr/bin/env python3
"""Unit checks for the return routing fix."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine import (  # noqa: E402
    CategoryRule,
    DecisionBand,
    Engine,
    ReturnRequest,
    ScoreRange,
    ScoringRule,
    load_engine,
    load_requests,
)


def tiny_engine(links: list[tuple[str, str]], profiles: dict[str, int]) -> Engine:
    categories = [
        CategoryRule("ELECTRONICS", True, 30),
        CategoryRule("DIGITAL_GOODS", False, 0),
    ]
    scoring = [
        ScoringRule(
            "return_history_count",
            [
                ScoreRange(0, 2, 0),
                ScoreRange(3, 5, 15),
                ScoreRange(6, 10, 30),
                ScoreRange(11, 1000000, 50),
            ],
        ),
        ScoringRule(
            "account_age_days",
            [
                ScoreRange(0, 29, 25),
                ScoreRange(30, 179, 10),
                ScoreRange(180, 1000000, 0),
            ],
        ),
        ScoringRule(
            "order_value_usd",
            [
                ScoreRange(0, 50, 0),
                ScoreRange(51, 200, 10),
                ScoreRange(201, 500, 20),
                ScoreRange(501, 1000000, 35),
            ],
        ),
    ]
    bands = [
        DecisionBand(0, 49, "AUTO_APPROVE", None),
        DecisionBand(50, 74, "MANUAL_REVIEW", "MEDIUM_RISK_SCORE"),
        DecisionBand(75, 100, "REJECT", "HIGH_RISK_SCORE"),
    ]
    return Engine.build(categories, scoring, bands, profiles, links)


class EngineTests(unittest.TestCase):
    def test_one_way_link_is_bidirectional(self) -> None:
        """u201 -> u202 must also let u202 see u201 history."""
        engine = tiny_engine(
            links=[("u201", "u202")],
            profiles={"u201": 1, "u202": 12},
        )
        # From related side (the old bug): must still sum both
        self.assertEqual(engine.linked_return_history("u202"), 13)
        self.assertEqual(engine.linked_return_history("u201"), 13)

    def test_transitive_group(self) -> None:
        engine = tiny_engine(
            links=[("u101", "u102"), ("u101", "u103")],
            profiles={"u101": 2, "u102": 8, "u103": 4},
        )
        self.assertEqual(engine.linked_return_history("u102"), 14)
        self.assertEqual(engine.linked_return_history("u103"), 14)

    def test_category_reject(self) -> None:
        engine = tiny_engine([], {"u1": 0})
        result = engine.route(
            ReturnRequest("r1", "u1", "DIGITAL_GOODS", 1, 10, 100)
        )
        self.assertEqual(result["decision"], "REJECT")
        self.assertEqual(result["reason"], "CATEGORY_NON_RETURNABLE")
        self.assertIsNone(result["risk_score"])

    def test_window_reject(self) -> None:
        engine = tiny_engine([], {"u1": 0})
        result = engine.route(
            ReturnRequest("r1", "u1", "ELECTRONICS", 45, 10, 100)
        )
        self.assertEqual(result["decision"], "REJECT")
        self.assertEqual(result["reason"], "RETURN_WINDOW_EXPIRED")
        self.assertIsNone(result["risk_score"])

    def test_auto_approve_omits_reason(self) -> None:
        engine = tiny_engine([], {"u1": 0})
        result = engine.route(
            ReturnRequest("r1", "u1", "ELECTRONICS", 5, 40, 200)
        )
        # age 200 => 0, history 0 => 0, order 40 => 0 => score 0
        self.assertEqual(result["risk_score"], 0)
        self.assertEqual(result["decision"], "AUTO_APPROVE")
        self.assertNotIn("reason", result)

    def test_sample_fixture_expectations(self) -> None:
        data_dir = ROOT / "data"
        engine = load_engine(data_dir)
        by_id = {r.request_id: engine.route(r) for r in load_requests(data_dir)}

        self.assertEqual(by_id["r102"]["reason"], "CATEGORY_NON_RETURNABLE")
        self.assertEqual(by_id["r103"]["reason"], "RETURN_WINDOW_EXPIRED")

        # u202 linked to u201 => history 13; age 15=>25; order 600=>35; hist=>50
        # total 110 clamped to 100 => REJECT HIGH_RISK_SCORE
        self.assertEqual(by_id["r104"]["risk_score"], 100)
        self.assertEqual(by_id["r104"]["decision"], "REJECT")
        self.assertEqual(by_id["r104"]["reason"], "HIGH_RISK_SCORE")

        # Without bidirectional fix, looking up u202 alone would score too low.
        # Prove group sum is used:
        self.assertEqual(engine.linked_return_history("u202"), 13)


if __name__ == "__main__":
    unittest.main()
