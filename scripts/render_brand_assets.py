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
PANEL_HOT = (18, 36, 48)
GRID = (19, 42, 56)
CYAN = (94, 234, 212)
CYAN_DIM = (125, 211, 199)
MUTED = (159, 184, 196)
WHITE = (232, 255, 251)
DIM = (90, 122, 136)
LINE = (45, 90, 110)
WARN = (248, 113, 113)  # lost-context red
OK = (52, 211, 153)  # remembered green

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
    "!": ["00100", "00100", "00100", "00100", "00100", "00000", "00100"],
    "?": ["01110", "10001", "00001", "00010", "00100", "00000", "00100"],
    "~": ["00000", "00000", "01001", "10110", "00000", "00000", "00000"],
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


def chrome(img: Image.Image, title: str = "KEDGER", right: str = "LOCAL MEMORY CLI") -> None:
    d = ImageDraw.Draw(img)
    w, _ = img.size
    d.rectangle([0, 0, w, 52], fill=PANEL)
    d.line([(0, 52), (w, 52)], fill=CYAN, width=2)
    draw_text(img, 20, 16, title, color=CYAN, scale=3, tracking=1)
    draw_text(img, w - text_width(right, 2) - 24, 20, right, color=CYAN_DIM, scale=2)


def panel(
    img: Image.Image,
    box: tuple[int, int, int, int],
    *,
    fill: tuple[int, int, int] = PANEL,
    outline: tuple[int, int, int] = LINE,
    width: int = 2,
) -> None:
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(list(box), radius=10, outline=outline, width=width, fill=fill)


def render_banner() -> None:
    """Hero: brand-first + one job line + install cue."""
    w, h = 1440, 480
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 24)
    chrome(img)
    draw_text(img, 72, 100, "KEDGER", color=WHITE, scale=14, tracking=2)
    draw_text(img, 72, 230, "YOUR NEXT AGENT REMEMBERS", color=CYAN, scale=4, tracking=1)
    draw_text(
        img,
        72,
        290,
        "HOOKS CAPTURE  ·  ANCHORS KEEP  ·  .KXP HANDS OFF",
        color=MUTED,
        scale=3,
        tracking=1,
    )
    d = ImageDraw.Draw(img)
    d.rectangle([72, 360, 86, 392], fill=CYAN)
    draw_text(img, 98, 364, "PIP INSTALL KEDGER  &&  KEDGER INIT --NAME ALICE", color=CYAN, scale=3)
    draw_text(img, 72, 430, "LOCAL-FIRST  ·  CURSOR + CLAUDE  ·  NO CLOUD REQUIRED", color=DIM, scale=2)
    img.save(OUT / "kedger-banner.png", optimize=True)
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
    """1280×640 share card — problem + brand + CTA."""
    w, h = 1280, 640
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 32)
    chrome(img, "KEDGER", "OPEN SOURCE")
    draw_text(img, 72, 110, "KEDGER", color=WHITE, scale=14, tracking=2)
    draw_text(img, 72, 250, "CODING AGENTS FORGET.", color=WARN, scale=4, tracking=1)
    draw_text(img, 72, 320, "KEDGER MAKES THEM REMEMBER.", color=CYAN, scale=4, tracking=1)
    d = ImageDraw.Draw(img)
    d.rectangle([72, 410, 88, 450], fill=CYAN)
    draw_text(img, 104, 418, "PIP INSTALL KEDGER", color=CYAN, scale=3)
    draw_text(img, 72, 510, "HOOKS -> ANCHORS -> SEALED .KXP  ·  LOCAL-FIRST", color=MUTED, scale=2)
    draw_text(img, 72, 560, "GITHUB.COM/GAGANTAKIITD/KEDGER", color=DIM, scale=2)
    img.save(OUT / "social.png", optimize=True)
    print("wrote", OUT / "social.png")


def render_idea_panel() -> None:
    """Pipeline: session → memory → pack → next agent."""
    w, h = 1100, 300
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 20)
    chrome(img, "HOW IT WORKS", "4 STEPS")
    boxes = [
        (36, "1 SESSION", "hooks ingest"),
        (300, "2 MEMORY", "anchors + ops"),
        (564, "3 PACK", "sealed .kxp"),
        (828, "4 NEXT", "hydrate live"),
    ]
    d = ImageDraw.Draw(img)
    for i, (x, title, sub) in enumerate(boxes):
        panel(img, (x, 90, x + 220, 250), outline=CYAN, fill=PANEL)
        draw_text(img, x + 20, 120, title, color=WHITE, scale=3)
        draw_text(img, x + 20, 180, sub.upper(), color=CYAN_DIM, scale=2)
        if i < len(boxes) - 1:
            draw_text(img, x + 232, 150, ">", color=CYAN, scale=4)
    img.save(OUT / "idea-flow.png", optimize=True)
    print("wrote", OUT / "idea-flow.png")


def render_before_after() -> None:
    """Show the product job: without vs with Kedger."""
    w, h = 1100, 420
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 20)
    chrome(img, "THE JOB", "SHOW DONT TELL")
    # Left: without
    panel(img, (36, 80, 520, 380), outline=WARN, fill=PANEL)
    draw_text(img, 60, 100, "WITHOUT KEDGER", color=WARN, scale=3)
    left_lines = [
        (150, "> NEW CHAT", WHITE),
        (200, "  WHAT DID WE DECIDE?", MUTED),
        (250, "  WHY NOT REDIS?", MUTED),
        (300, "  WHICH FILES CHANGED?", MUTED),
        (340, "  ...COLD START", DIM),
    ]
    for y, text, color in left_lines:
        draw_text(img, 60, y, text, color=color, scale=2)
    # Right: with
    panel(img, (580, 80, 1064, 380), outline=OK, fill=PANEL)
    draw_text(img, 604, 100, "WITH KEDGER", color=OK, scale=3)
    right_lines = [
        (150, "> KEDGER HYDRATE --LIVE", CYAN),
        (200, "  REJECT: NO REDIS", WHITE),
        (250, "  DECISION: POSTGRES", WHITE),
        (300, "  OPS: AUTH.PY +42/-8", WHITE),
        (340, "  READY FOR NEXT AGENT", OK),
    ]
    for y, text, color in right_lines:
        draw_text(img, 604, y, text, color=color, scale=2)
    img.save(OUT / "before-after.png", optimize=True)
    print("wrote", OUT / "before-after.png")


def render_peer_story() -> None:
    """Alice → Bob handoff strip — the two-person story."""
    w, h = 1100, 360
    img = Image.new("RGB", (w, h), BG)
    paint_grid(img, 20)
    chrome(img, "PEER HANDOFF", "ALICE -> BOB")
    # Alice column
    panel(img, (36, 80, 360, 320), outline=CYAN, fill=PANEL)
    draw_text(img, 60, 100, "ALICE", color=CYAN, scale=3)
    for y, line in [
        (150, "INIT --NAME ALICE"),
        (190, "AGENT WORKS"),
        (230, "PEER SEND"),
        (270, "-> HF_....KXP"),
    ]:
        draw_text(img, 60, y, line, color=WHITE if "->" not in line else CYAN, scale=2)
    # Arrow mid
    draw_text(img, 400, 180, "SEND", color=CYAN, scale=3)
    draw_text(img, 400, 220, ".KXP", color=MUTED, scale=2)
    # Bob column
    panel(img, (560, 80, 1064, 320), outline=OK, fill=PANEL)
    draw_text(img, 584, 100, "BOB", color=OK, scale=3)
    for y, line, color in [
        (150, "PEER OPEN HF_....KXP", WHITE),
        (190, "HYDRATE --LIVE", CYAN),
        (230, "NEW IDE CHAT", WHITE),
        (270, "CONTINUES WITH CONTEXT", OK),
    ]:
        draw_text(img, 584, y, line, color=color, scale=2)
    img.save(OUT / "peer-story.png", optimize=True)
    print("wrote", OUT / "peer-story.png")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    render_banner()
    render_mark()
    render_cli_listing()
    render_social()
    render_idea_panel()
    render_before_after()
    render_peer_story()


if __name__ == "__main__":
    main()
