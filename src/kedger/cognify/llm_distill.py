"""Optional LLM episode distill (OpenAI-compatible chat completions).

Default cognify stays deterministic regex/heuristic extract. When enabled via
``--llm-distill`` or ``KEDGER_LLM_DISTILL=1`` **and** ``KEDGER_LLM_API_KEY`` is
set, Kedger may ask an LLM to refine the episode summary and suggest supplemental
claims. Any missing config, parse error, or HTTP failure falls back silently to
heuristics — LLM is never the sole compressor.
"""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Callable

from kedger.cognify.extract import (
    KIND_TIER,
    Claim,
    _clean_statement,
    classify_clause_unlabeled,
)
from kedger.constants import EPISODE_SUMMARY_MAX

HttpPost = Callable[[str, dict[str, str], bytes, float], tuple[int, str]]

API_KEY_ENV = "KEDGER_LLM_API_KEY"
DISTILL_FLAG_ENV = "KEDGER_LLM_DISTILL"
BASE_URL_ENV = "KEDGER_LLM_BASE_URL"
MODEL_ENV = "KEDGER_LLM_MODEL"
DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TIMEOUT_S = 45.0

VALID_KINDS = frozenset(KIND_TIER)


@dataclass(frozen=True)
class LlmDistillConfig:
    api_key: str
    base_url: str = DEFAULT_BASE_URL
    model: str = DEFAULT_MODEL
    timeout_s: float = DEFAULT_TIMEOUT_S


@dataclass
class LlmDistillResult:
    summary: str
    supplemental_claims: list[Claim] = field(default_factory=list)
    model: str = DEFAULT_MODEL


def llm_distill_requested(*, flag: bool = False) -> bool:
    """True when operator opted in via CLI flag or KEDGER_LLM_DISTILL env."""
    if flag:
        return True
    raw = os.environ.get(DISTILL_FLAG_ENV, "").strip().lower()
    return raw in {"1", "true", "yes", "on"}


def resolve_llm_config() -> LlmDistillConfig | None:
    """Resolve OpenAI-compatible endpoint config from env. None when no API key."""
    api_key = os.environ.get(API_KEY_ENV, "").strip()
    if not api_key:
        return None
    base_url = os.environ.get(BASE_URL_ENV, DEFAULT_BASE_URL).strip().rstrip("/")
    model = os.environ.get(MODEL_ENV, DEFAULT_MODEL).strip() or DEFAULT_MODEL
    return LlmDistillConfig(api_key=api_key, base_url=base_url, model=model)


def _default_http_post(
    url: str, headers: dict[str, str], body: bytes, timeout: float
) -> tuple[int, str]:
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        return exc.code, payload


def _span_turn_lines(span: list[dict[str, Any]], *, max_chars: int = 6000) -> str:
    lines: list[str] = []
    used = 0
    for obs in span:
        text = (obs.get("summary") or "").strip()
        if not text:
            continue
        obs_type = obs.get("type") or "note"
        line = f"[{obs_type}] {text}"
        if used + len(line) + 1 > max_chars:
            remain = max_chars - used - 4
            if remain > 40:
                lines.append(line[:remain] + "…")
            break
        lines.append(line)
        used += len(line) + 1
    return "\n".join(lines)


def _heuristic_claim_lines(claims: list[Claim], *, limit: int = 12) -> str:
    if not claims:
        return "(none yet)"
    out: list[str] = []
    for c in claims[:limit]:
        out.append(f"- [{c.kind}] {c.statement}")
    return "\n".join(out)


def _build_prompt(
    *,
    span: list[dict[str, Any]],
    heuristic_summary: str,
    heuristic_claims: list[Claim],
) -> str:
    return (
        "You distill engineering-session memory for a local-first CLI (Kedger).\n"
        "Given conversation turns and heuristic claims already extracted, produce:\n"
        "1) A concise episode summary (<= 400 chars) capturing decisions, rejects, "
        "constraints, next steps, and files touched.\n"
        "2) Optional supplemental claims ONLY for durable engineering judgment "
        "missed by heuristics (constraints, rejections, decisions, next_step, "
        "open_question, gotcha).\n\n"
        "Rules:\n"
        "- Do NOT invent facts not supported by the turns.\n"
        "- Do NOT duplicate heuristic claims.\n"
        "- Return JSON only: "
        '{"summary":"...","claims":[{"kind":"constraint","statement":"..."}]}\n'
        "- claims may be [] when heuristics are sufficient.\n\n"
        f"Heuristic summary:\n{heuristic_summary}\n\n"
        f"Heuristic claims:\n{_heuristic_claim_lines(heuristic_claims)}\n\n"
        f"Turns:\n{_span_turn_lines(span)}\n"
    )


def _parse_llm_json(content: str) -> dict[str, Any] | None:
    text = (content or "").strip()
    if not text:
        return None
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", text, flags=re.I)
    if fence:
        text = fence.group(1).strip()
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        return None
    return obj if isinstance(obj, dict) else None


def _claims_from_llm_payload(
    payload: Any,
    *,
    heuristic_claims: list[Claim],
    span: list[dict[str, Any]],
) -> list[Claim]:
    if not isinstance(payload, list):
        return []
    existing = {(c.kind, c.statement.lower()) for c in heuristic_claims}
    source_obs_id = span[-1].get("id") if span else None
    out: list[Claim] = []
    for item in payload[:8]:
        if not isinstance(item, dict):
            continue
        kind = str(item.get("kind") or "").strip().lower()
        if kind not in VALID_KINDS:
            uk, body, _ = classify_clause_unlabeled(str(item.get("statement") or ""))
            if uk:
                kind = uk
            else:
                continue
        stmt = _clean_statement(str(item.get("statement") or ""))
        if len(stmt) < 8:
            continue
        key = (kind, stmt.lower())
        if key in existing:
            continue
        existing.add(key)
        out.append(
            Claim(
                kind=kind,
                statement=stmt,
                tier=KIND_TIER.get(kind, "C"),
                source_type="llm_distill",
                source_obs_id=source_obs_id,
                labeled=False,
            )
        )
    return out


def _chat_completion_content(
    response_body: str,
) -> str | None:
    try:
        data = json.loads(response_body)
    except json.JSONDecodeError:
        return None
    choices = data.get("choices")
    if not isinstance(choices, list) or not choices:
        return None
    message = choices[0].get("message") if isinstance(choices[0], dict) else None
    if not isinstance(message, dict):
        return None
    content = message.get("content")
    return content if isinstance(content, str) else None


def distill_episode(
    span: list[dict[str, Any]],
    *,
    heuristic_summary: str,
    heuristic_claims: list[Claim],
    config: LlmDistillConfig,
    http_post: HttpPost | None = None,
) -> LlmDistillResult | None:
    """Call an OpenAI-compatible chat API. Returns None on any failure."""
    if not span and not heuristic_summary:
        return None
    post = http_post or _default_http_post
    prompt = _build_prompt(
        span=span,
        heuristic_summary=heuristic_summary,
        heuristic_claims=heuristic_claims,
    )
    url = f"{config.base_url}/chat/completions"
    body = json.dumps(
        {
            "model": config.model,
            "temperature": 0.2,
            "response_format": {"type": "json_object"},
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You extract durable engineering judgment for agent memory. "
                        "Respond with valid JSON only."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        }
    ).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.api_key}",
    }
    try:
        status, raw = post(url, headers, body, config.timeout_s)
    except OSError:
        return None
    if status < 200 or status >= 300:
        return None
    content = _chat_completion_content(raw)
    if not content:
        return None
    parsed = _parse_llm_json(content)
    if not parsed:
        return None
    summary = str(parsed.get("summary") or "").strip()
    if not summary:
        return None
    summary = summary[:EPISODE_SUMMARY_MAX]
    supplemental = _claims_from_llm_payload(
        parsed.get("claims"),
        heuristic_claims=heuristic_claims,
        span=span,
    )
    return LlmDistillResult(
        summary=summary,
        supplemental_claims=supplemental,
        model=config.model,
    )
