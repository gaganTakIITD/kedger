"""IDE hook normalization — adapters call CLI; core never imports IDE types."""

from kedger.hooks.normalize import normalize_hook_event

__all__ = ["normalize_hook_event"]
