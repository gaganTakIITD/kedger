"""Secret/token scanners run before any L0 persist or share gate."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# High-signal patterns — fail closed on match for share; mask for L0 summary.
_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github_pat", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("github_token", re.compile(r"ghs_[A-Za-z0-9_]{20,}")),
    # OpenAI / Stripe-style secret keys (ConfAIde share probe — Batch4/5)
    ("openai_sk", re.compile(r"(?i)\bsk-[A-Za-z0-9]{20,}\b")),
    ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")),
    ("pem_private", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("generic_api_key", re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[^\s'\"]{12,}")),
    # "token sk-..." / "token ghs_..." without '=' (chat prose)
    ("token_prose", re.compile(r"(?i)\b(api[_-]?key|secret|password|token)\s+[A-Za-z0-9_\-]{16,}")),
    ("bearer", re.compile(r"(?i)bearer\s+[A-Za-z0-9\-\._~\+\/]+=*")),
]


@dataclass
class RedactionResult:
    text: str
    redacted: bool
    hits: list[str] = field(default_factory=list)

    @property
    def blocked_for_share(self) -> bool:
        return bool(self.hits)


def scan_secrets(text: str) -> list[str]:
    hits: list[str] = []
    for name, pat in _PATTERNS:
        if pat.search(text or ""):
            hits.append(name)
    return hits


def redact_text(text: str, *, placeholder: str = "[REDACTED]") -> RedactionResult:
    original = text or ""
    hits = scan_secrets(original)
    out = original
    for name, pat in _PATTERNS:
        out = pat.sub(placeholder, out)
    return RedactionResult(text=out, redacted=out != original, hits=hits)
