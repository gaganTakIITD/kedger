"""SLI recording helpers (importable without `tests` package on path)."""

from __future__ import annotations

import json
import time
from pathlib import Path

ARTIFACTS = Path(__file__).resolve().parents[2] / "artifacts" / "eval"


def sli_path(tmp_path: Path | None = None) -> Path:
    try:
        ARTIFACTS.mkdir(parents=True, exist_ok=True)
        path = ARTIFACTS / "slis.jsonl"
        path.touch(exist_ok=True)
        return path
    except OSError:
        if tmp_path is None:
            raise
        p = tmp_path / "slis.jsonl"
        p.touch()
        return p


def record_sli(path: Path, name: str, value: float, unit: str = "ms", **extra) -> None:
    row = {"name": name, "value": value, "unit": unit, "ts": time.time(), **extra}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, sort_keys=True) + "\n")
