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
    workstream_slug: str = "default",
) -> dict[str, Any]:
    ws_id = workstream_id
    if ws_id is None:
        ws = store.ensure_workstream(
            slug=workstream_slug,
            principal_id=principal.principal_id,
            signing_key=principal.signing_key,
        )
        ws_id = ws["id"]
    # share_mode=explicit_only — ignore accidental shareable unless explicit CLI flag
    return store.remember(
        kind,
        statement,
        reason=reason,
        principal_id=principal.principal_id,
        shareable=shareable,
        workstream_id=ws_id,
    )


def forget_anchor(
    store: Store, *, principal: Principal, anchor_id: str
) -> dict[str, Any]:
    return store.forget(anchor_id, principal_id=principal.principal_id)
