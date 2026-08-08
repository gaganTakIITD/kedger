"""Inv-Scope access control — deny with 404, never 403 existence oracle."""

from kedger.acl.scope import InvScopeError, require_visible, scope_get

__all__ = ["InvScopeError", "require_visible", "scope_get"]
