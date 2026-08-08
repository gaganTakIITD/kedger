#!/usr/bin/env python3
"""Fetch an arXiv abstract HTML page into /tmp/kedger-papers/full/{id}.html.

Uses urllib only. Be polite: small pause, identifiable User-Agent, no hammering.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

OUT_DIR = Path("/tmp/kedger-papers/full")
ARXIV_ID_RE = re.compile(r"^(\d{4}\.\d{4,5})(v\d+)?$")
USER_AGENT = "KedgerResearchBot/0.1 (+https://github.com/gaganTakIITD/kedger; research corpus; polite)"
DEFAULT_PAUSE_S = 1.0


def normalize_id(raw: str) -> str:
    s = raw.strip()
    s = s.removeprefix("arxiv:")
    s = s.removeprefix("arXiv:")
    s = s.removeprefix("https://arxiv.org/abs/")
    s = s.removeprefix("http://arxiv.org/abs/")
    s = s.removeprefix("https://arxiv.org/html/")
    s = s.removeprefix("http://arxiv.org/html/")
    s = s.split("?")[0].rstrip("/")
    m = ARXIV_ID_RE.match(s)
    if not m:
        raise ValueError(f"Not an arXiv-like id (YYMM.NNNNN): {raw!r}")
    return m.group(1)  # drop version for stable filename; URL may keep version


def fetch_html(arxiv_id: str, pause_s: float = DEFAULT_PAUSE_S) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{arxiv_id}.html"
    if out.exists() and out.stat().st_size > 0:
        print(f"already cached: {out}")
        return out

    # Prefer ar5iv/html experimental; fall back to abs page.
    urls = [
        f"https://arxiv.org/html/{arxiv_id}",
        f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}",
        f"https://arxiv.org/abs/{arxiv_id}",
    ]
    last_err: Exception | None = None
    for i, url in enumerate(urls):
        if i:
            time.sleep(pause_s)
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
            },
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
                ctype = resp.headers.get("Content-Type", "")
            if not body:
                raise RuntimeError(f"empty body from {url}")
            # Write even if abs-only HTML — caller can upgrade later.
            out.write_bytes(body)
            print(f"fetched {url} -> {out} ({len(body)} bytes, {ctype})")
            return out
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, RuntimeError) as e:
            last_err = e
            print(f"warn: {url}: {e}", file=sys.stderr)
            continue
    raise SystemExit(f"failed to fetch {arxiv_id}: {last_err}")


def main() -> int:
    p = argparse.ArgumentParser(description="Fetch arXiv abs/html into /tmp/kedger-papers/full/")
    p.add_argument("ids", nargs="+", help="arXiv id(s), e.g. 2501.13956")
    p.add_argument(
        "--pause",
        type=float,
        default=DEFAULT_PAUSE_S,
        help="seconds between attempts/URLs (default: 1.0)",
    )
    args = p.parse_args()
    for raw in args.ids:
        pid = normalize_id(raw)
        fetch_html(pid, pause_s=args.pause)
        time.sleep(args.pause)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
