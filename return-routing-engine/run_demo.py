#!/usr/bin/env python3
"""Run the sample requests and write data/results.jsonl."""

from __future__ import annotations

import json
from pathlib import Path

from engine import load_engine, load_requests


def main() -> None:
    data_dir = Path(__file__).resolve().parent / "data"
    engine = load_engine(data_dir)
    requests = load_requests(data_dir)

    out_path = data_dir / "results.jsonl"
    lines: list[str] = []
    print("request_id  decision           score  reason")
    print("-" * 56)
    for req in requests:
        result = engine.route(req)
        line = json.dumps(result, separators=(",", ":"))
        lines.append(line)
        score = result["risk_score"]
        reason = result.get("reason", "")
        print(
            f"{result['request_id']:<11} {result['decision']:<17} "
            f"{str(score):<6} {reason}"
        )

    out_path.write_text("\n".join(lines) + "\n")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
