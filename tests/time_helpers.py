"""Test helpers for observation timestamps within L0 TTL."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone


def recent_ts(minutes_ago: int = 0, second: int = 0) -> str:
    """UTC ISO timestamp within the L0 72h window (default: now minus minutes_ago)."""
    dt = datetime.now(timezone.utc) - timedelta(minutes=minutes_ago)
    return dt.replace(second=second % 60, microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
