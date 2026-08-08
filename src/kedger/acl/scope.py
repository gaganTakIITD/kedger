"""Inv-Scope: unauthorized reads collapse to not-found (MemClaw)."""

from __future__ import annotations

from typing import Any, Callable

from kedger.constants import NOT_FOUND_CODE, NOT_FOUND_MSG


class InvScopeError(LookupError):
    """Raised for any unauthorized or missing resource — CLI maps to 404."""

    code = NOT_FOUND_CODE

    def __init__(self, message: str = NOT_FOUND_MSG) -> None:
        super().__init__(message)


def require_visible(condition: bool) -> None:
    if not condition:
        raise InvScopeError()


def scope_get(fetcher: Callable[[], Any | None]) -> Any:
    """Fetch a resource; missing OR unauthorized → InvScopeError (same message)."""
    try:
        value = fetcher()
    except InvScopeError:
        raise
    except Exception:
        raise InvScopeError() from None
    if value is None:
        raise InvScopeError()
    return value
