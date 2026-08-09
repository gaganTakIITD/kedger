#!/usr/bin/env python3
"""Render Kedger CLI-theme brand assets (pixel terminal look for GitHub README)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets"

# Demo-frame palette (ink + cyan terminal)
BG = (7, 16, 24)
PANEL = (10, 22, 34)
GRID = (19, 42, 56)
CYAN = (94, 234, 212)
CYAN_DIM = (125, 211, 199)
MUTED = (159, 184, 196)
WHITE = (232, 255, 251)
DIM = (90, 122, 136)
LINE = (45, 90, 110)

# 5x7 uppercase bitmap font (1 = on). Covers branding + CLI listing.
FONT: dict[str, list[str]] = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10001", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "11011", "10001"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    ",": ["00000", "00000", "00000", "00000", "01100", "00100", "01000"],
    ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
    "/": ["00001", "00010", "00100", "01000", "10000", "00000", "00000"],
    ">": ["10000", "01000", "00100", "00010", "00100", "01000", "10000"],
    "(": ["00100", "01000", "10000", "10000", "10000", "01000", "00100"],
    ")": ["00100", "00010", "00001", "00001", "00001", "00010", "00100"],
    "'": ["01100", "01100", "00100", "00000", "00000", "00000", "00000"],
    "=": ["00000", "00000", "11111", "00000", "11111", "00000", "00000"],
    "_": ["00000", "00000", "00000", "00000", "00000", "00000", "11111"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
}


def draw_text(
    img: Image.Image,
    x: int,
    y: int,
    text: str,
    *,
    color: tuple[int, int, int],
    scale: int = 3,
    tracking: int = 1,
) -> int:
    """Draw bitmap text; return width used."""
    px = x
    for ch in text.upper():
        glyph = FONT.get(ch, FONT[" "])
        for row, bits in enumerate(glyph):
            for col, bit in enumerate(bits):
                if bit == "1":
                    for dy in range(scale):
                        for dx in range(scale):
                            img.putpixel((px + col * scale + dx, y + row * scale + dy), color)
        px += (5 + tracking) * scale
    return px - x


def text_width(text: str, scale: int = 3, tracking: int = 1) -> int:
    return len(text) * (5 + tracking) * scale


def paint_grid(img: Image.Image, step: int = 16) -> None:
    d = ImageDraw.Draw(img)
    w, h = img.size
    for x in range(0, w, step):
        d.line([(x, 0), (x, h)], fill=GRID)
    for y in range(0, h, step):
        d.line([(0, y), (w, y)], fill=GRID)


def chrome(img: Image.Image, title: str = "KEDGER") -> None:
    d = ImageDraw.Draw(img)
    w, _ = img.size
    d.rectangle([0, 0, w, 52], fill=PANEL)
    d.line([(0, 52), (w, 52)], fill=CYAN, width=2)
    draw_text(img, 20, 16, title, color=CYAN, scale=3, tracking=1)
    draw_text(img, w - text_width("LOCAL MEMORY CLI", 2) - 24, 20, "LOCAL MEMORY CLI", color=CYAN_DIM, scale=2)


def render_banner() -> None:
    w, h = 1440, 420
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 24)
    chrome(img)
    # Wordmark
    draw_text(img, 72, 120, "KEDGER", color=WHITE, scale=14, tracking=2)
    draw_text(
        img,
        72,
        250,
        "HOOKS -> ANCHORS -> SEALED .KXP",
        color=MUTED,
        scale=3,
        tracking=1,
    )
    # Prompt line
    d = ImageDraw.Draw(img)
    d.rectangle([72, 320, 86, 352], fill=CYAN)
    draw_text(img, 98, 324, "KEDGER INIT --NAME ALICE", color=CYAN, scale=3)
    draw_text(img, 72, 380, "OSS ENG-MEMORY CLI  ·  KEDGER.MEMORY.V1", color=DIM, scale=2)
    img.save(OUT / "kedger-banner.png", optimize=True)
    # Keep SVG companion for crisp zoom; PNG is README-primary on GitHub dark/light
    print("wrote", OUT / "kedger-banner.png")


def render_mark() -> None:
    s = 256
    img = Image.new("RGB", (s, s), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([12, 12, s - 12, s - 12], radius=28, outline=LINE, width=4)
    draw_text(img, 78, 70, "K", color=CYAN, scale=18, tracking=1)
    d.rectangle([64, 200, 192, 210], fill=CYAN_DIM)
    img.save(OUT / "kedger-mark.png", optimize=True)
    print("wrote", OUT / "kedger-mark.png")


def render_cli_listing() -> None:
    """Terminal command listing strip for README."""
    rows = [
        ("kedger init --name alice", "keys + policy + ide hooks"),
        ("kedger remember reject ...", "durable anchor / policy"),
        ("kedger cognify --promote", "episode + promote"),
        ("kedger peer card", "public card for teammate"),
        ("kedger peer send --to bob.json", "grant + seal + export .kxp"),
        ("kedger peer open hf_....kxp", "import into local store"),
        ("kedger hydrate --live", "preview next-agent context"),
        ("kedger doctor", "health + identity locks"),
    ]
    w, row_h, top = 1100, 54, 70
    h = top + 24 + len(rows) * row_h + 28
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 20)
    chrome(img, "KEDGER CLI")
    y = top + 18
    d = ImageDraw.Draw(img)
    for cmd, desc in rows:
        draw_text(img, 36, y, ">", color=CYAN, scale=3)
        draw_text(img, 70, y, cmd.upper().replace("…", "..."), color=WHITE, scale=2, tracking=1)
        dw = text_width(desc.upper(), 2)
        draw_text(img, w - dw - 36, y + 4, desc.upper(), color=DIM, scale=2, tracking=1)
        y += row_h
        d.line([(36, y - 10), (w - 36, y - 10)], fill=GRID)
    img.save(OUT / "cli-listing.png", optimize=True)
    print("wrote", OUT / "cli-listing.png")


def render_social() -> None:
    w, h = 1280, 640
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 32)
    chrome(img)
    draw_text(img, 72, 140, "KEDGER", color=WHITE, scale=16, tracking=2)
    draw_text(img, 72, 320, "LOCAL-FIRST MEMORY FOR CODING AGENTS", color=MUTED, scale=3)
    d = ImageDraw.Draw(img)
    d.rectangle([72, 400, 88, 440], fill=CYAN)
    draw_text(img, 104, 408, "KEDGER INIT --NAME ALICE", color=CYAN, scale=3)
    draw_text(img, 72, 520, "~/.KEDGER/  ·  .KXP  ·  KEDGER.MEMORY.V1", color=DIM, scale=2)
    draw_text(img, 72, 580, "GITHUB.COM/GAGANTAKIITD/KEDGER", color=DIM, scale=2)
    img.save(OUT / "social.png", optimize=True)
    print("wrote", OUT / "social.png")


def render_idea_panel() -> None:
    """Compact idea diagram: session → memory → pack → next agent."""
    w, h = 1100, 280
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 20)
    chrome(img, "IDEA")
    boxes = [
        (40, "SESSION", "hooks ingest"),
        (300, "MEMORY", "anchors + ops"),
        (560, "PACK", "sealed .kxp"),
        (820, "NEXT", "peer agent"),
    ]
    d = ImageDraw.Draw(img)
    for i, (x, title, sub) in enumerate(boxes):
        d.rounded_rectangle([x, 100, x + 220, 220], radius=8, outline=CYAN, width=2, fill=PANEL)
        draw_text(img, x + 28, 128, title, color=WHITE, scale=3)
        draw_text(img, x + 28, 180, sub.upper(), color=CYAN_DIM, scale=2)
        if i < len(boxes) - 1:
            draw_text(img, x + 230, 150, ">", color=CYAN, scale=4)
    img.save(OUT / "idea-flow.png", optimize=True)
    print("wrote", OUT / "idea-flow.png")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    render_banner()
    render_mark()
    render_cli_listing()
    render_social()
    render_idea_panel()


if __name__ == "__main__":
    main()
