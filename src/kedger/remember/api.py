"""Explicit Anchor remember/forget (Tier A1 promotion path)."""

from __future__ import annotations

from typing import Any

from kedger.keys.principal import Principal
from kedger.store.db import Store


def remember_anchor(
    store: Store,
    *,
    principal: Principal,
    kind: str,
    statement: str,
    reason: str | None = None,
    shareable: bool = False,
    workstream_id: str | None = None,
) -> dict[str, Any]:
    return store.remember(
        kind,
        statement,
        reason=reason,
        principal_id=principal.principal_id,
        shareable=shareable,
        workstream_id=workstream_id,
    )


def forget_anchor(
    store: Store, *, principal: Principal, anchor_id: str
) -> dict[str, Any]:
    return store.forget(anchor_id, principal_id=principal.principal_id)
