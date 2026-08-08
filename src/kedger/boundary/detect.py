"""Episode boundary detector — HARD vs SOFT (P2 / WORKSTREAM locks)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from kedger.constants import IDLE_BOUNDARY_MINUTES, SEGMENT_THETA


HARD_TYPES = frozenset(
    {"pre_compact", "session_end", "cognify", "handoff"}
)
SOFT_TYPES = frozenset(
    {"workstream_switch", "idle", "turn_stop", "file_cluster", "surprise"}
)


@dataclass
class Boundary:
    kind: str  # hard | soft
    reason: str
    obs_type: str | None = None
    force: bool = False


def _parse_ts(ts: str | None) -> datetime | None:
    if not ts:
        return None
    try:
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        return datetime.fromisoformat(ts)
    except ValueError:
        return None


def detect_boundary(
    *,
    event_type: str | None = None,
    force: bool = False,
    last_obs_ts: str | None = None,
    now: datetime | None = None,
    workstream_changed: bool = False,
    segment_score: float | None = None,
    min_span: int = 1,
    span_count: int = 0,
) -> Boundary | None:
    """Return a Boundary if cognify should run; never creates a workstream."""
    if force or (event_type or "").lower() in HARD_TYPES:
        return Boundary(
            kind="hard",
            reason=event_type or "force",
            obs_type=event_type,
            force=force,
        )

    et = (event_type or "").lower()
    if workstream_changed or et == "workstream_switch":
        if span_count >= min_span:
            return Boundary(kind="soft", reason="workstream_switch", obs_type=et)

    now = now or datetime.now(timezone.utc)
    last = _parse_ts(last_obs_ts)
    if last is not None:
        idle_min = (now - last.astimezone(timezone.utc)).total_seconds() / 60.0
        if idle_min >= IDLE_BOUNDARY_MINUTES and span_count >= min_span:
            return Boundary(kind="soft", reason="idle", obs_type="idle")

    if segment_score is not None and segment_score < SEGMENT_THETA and span_count >= min_span:
        return Boundary(kind="soft", reason="segment_score", obs_type=et)

    if et in SOFT_TYPES and span_count >= min_span:
        return Boundary(kind="soft", reason=et, obs_type=et)

    return None


def observations_since(
    observations: list[dict[str, Any]], *, since_ts: str | None
) -> list[dict[str, Any]]:
    if not since_ts:
        return list(observations)
    return [o for o in observations if (o.get("ts") or "") > since_ts]
