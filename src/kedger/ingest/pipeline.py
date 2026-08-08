"""Observation ingest pipeline — redact → append → L1 soft patch → rotate."""

from __future__ import annotations

from typing import Any

from kedger.keys.principal import Principal
from kedger.store.db import Store


def ingest_from_hook(
    store: Store, payload: dict[str, Any], *, principal: Principal
) -> dict[str, Any]:
    return store.ingest_observation(payload, principal_id=principal.principal_id)
