#!/usr/bin/env python3
"""Render a short terminal-style demo GIF for README (no asciinema required)."""

from __future__ import annotations

import struct
import zlib
from pathlib import Path

# 16-color-ish dark terminal palette (RGB)
BG = (18, 18, 22)
FG = (220, 220, 215)
DIM = (120, 120, 130)
GREEN = (120, 200, 140)
CYAN = (120, 190, 210)
YELLOW = (220, 190, 110)

W, H = 720, 420
MARGIN_X, MARGIN_Y = 24, 28
LINE_H = 22
CHAR_W = 9


def _font_bitmap() -> dict[str, list[str]]:
    """Minimal 5x7-ish glyphs as rows of 0/1 (only chars we need)."""
    # Using a simple block font via string rows
    g = {
        " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
        "-": ["00000", "00000", "11111", "00000", "00000", "00000", "00000"],
        ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
        "/": ["00001", "00010", "00100", "01000", "10000", "00000", "00000"],
        ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
        "=": ["00000", "11111", "00000", "11111", "00000", "00000", "00000"],
        ">": ["10000", "01000", "00100", "01000", "10000", "00000", "00000"],
        "_": ["00000", "00000", "00000", "00000", "00000", "00000", "11111"],
        "~": ["00000", "01010", "10100", "00000", "00000", "00000", "00000"],
        "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
        "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
        "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
        "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
        "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
        "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
        "6": ["01110", "10000", "11110", "10001", "10001", "10001", "01110"],
        "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
        "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
        "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
        "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
        "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
        "C": ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
        "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
        "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
        "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
        "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01110"],
        "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
        "I": ["01110", "00100", "00100", "00100", "00100", "00100", "01110"],
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
        "[": ["01110", "01000", "01000", "01000", "01000", "01000", "01110"],
        "]": ["01110", "00010", "00010", "00010", "00010", "00010", "01110"],
        '"': ["01010", "01010", "00000", "00000", "00000", "00000", "00000"],
        "'": ["00100", "00100", "00000", "00000", "00000", "00000", "00000"],
        ",": ["00000", "00000", "00000", "00000", "01100", "00100", "01000"],
        "(": ["00100", "01000", "10000", "10000", "10000", "01000", "00100"],
        ")": ["00100", "00010", "00001", "00001", "00001", "00010", "00100"],
        "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
        "!": ["00100", "00100", "00100", "00100", "00100", "00000", "00100"],
    }
    # lowercase aliases
    for ch in list(g):
        if "A" <= ch <= "Z":
            g[ch.lower()] = g[ch]
    return g


FONT = _font_bitmap()


def new_frame() -> list[list[tuple[int, int, int]]]:
    return [[BG for _ in range(W)] for _ in range(H)]


def plot(frame, x, y, color) -> None:
    if 0 <= x < W and 0 <= y < H:
        frame[y][x] = color


def draw_char(frame, x, y, ch: str, color) -> None:
    glyph = FONT.get(ch) or FONT.get(ch.upper()) or FONT[" "]
    scale = 2
    for row, bits in enumerate(glyph):
        for col, bit in enumerate(bits):
            if bit == "1":
                for dy in range(scale):
                    for dx in range(scale):
                        plot(frame, x + col * scale + dx, y + row * scale + dy, color)


def draw_text(frame, x, y, text: str, color=FG) -> None:
    cx = x
    for ch in text:
        draw_char(frame, cx, y, ch, color)
        cx += CHAR_W


def draw_chrome(frame, title: str = "kedger — local memory CLI") -> None:
    for y in range(H):
        for x in range(W):
            # subtle vertical gradient
            t = y / H
            frame[y][x] = (
                int(BG[0] + 8 * t),
                int(BG[1] + 10 * t),
                int(BG[2] + 18 * t),
            )
    # top bar
    for y in range(36):
        for x in range(W):
            frame[y][x] = (28, 30, 38)
    draw_text(frame, MARGIN_X, 10, title, CYAN)
    # accent line
    for x in range(W):
        frame[36][x] = (60, 140, 150)


def frame_to_png(frame) -> bytes:
    """Minimal PNG encoder (RGBA)."""
    raw = bytearray()
    for row in frame:
        raw.append(0)  # filter none
        for r, g, b in row:
            raw.extend((r, g, b, 255))

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", W, H, 8, 6, 0, 0, 0)
    return b"".join(
        [
            b"\x89PNG\r\n\x1a\n",
            chunk(b"IHDR", ihdr),
            chunk(b"IDAT", zlib.compress(bytes(raw), 9)),
            chunk(b"IEND", b""),
        ]
    )


SCENES: list[tuple[list[tuple[str, tuple[int, int, int]]], float]] = [
    (
        [
            ("$ kedger keys init --name me", FG),
            ("principal_id: princ_01…", DIM),
            ("keys_dir:     ~/.kedger/keys/", DIM),
        ],
        1.2,
    ),
    (
        [
            ('$ kedger remember reject "No cookie sessions"', FG),
            ("anchor: anc_…  kind=reject  shareable=false", GREEN),
        ],
        1.2,
    ),
    (
        [
            ("$ kedger cognify --force", FG),
            ("episode: ep_…  candidates: 1  resealed: yes", GREEN),
        ],
        1.1,
    ),
    (
        [
            ("$ kedger handoff", FG),
            ("wrote: ./handoff.kxp  (age-shaped .kxp)", CYAN),
        ],
        1.1,
    ),
    (
        [
            ("$ kedger hydrate --live", FG),
            ("# Kedger hydrate", YELLOW),
            ("- [reject] No cookie sessions", FG),
        ],
        1.3,
    ),
    (
        [
            ("$ kedger why anc_…", FG),
            ("statement: No cookie sessions", FG),
            ("evidence: remember → cognify → promote", DIM),
            ("", FG),
            ("durable across sessions. sealed for handoff.", GREEN),
        ],
        1.6,
    ),
]


def render(out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.parent / "_demo_frames"
    tmp.mkdir(parents=True, exist_ok=True)
    for p in tmp.glob("*.png"):
        p.unlink()

    paths: list[Path] = []
    delays: list[int] = []
    idx = 0
    for lines, delay_s in SCENES:
        # progressive reveal
        for n in range(1, len(lines) + 1):
            frame = new_frame()
            draw_chrome(frame)
            y = MARGIN_Y + 28
            for text, color in lines[:n]:
                draw_text(frame, MARGIN_X, y, text[:78], color)
                y += LINE_H
            path = tmp / f"frame_{idx:03d}.png"
            path.write_bytes(frame_to_png(frame))
            paths.append(path)
            # hold longer on final line of scene
            delays.append(int(delay_s * 100) if n == len(lines) else 35)
            idx += 1

    # Assemble GIF with ffmpeg palette
    import subprocess

    concat = tmp / "list.txt"
    # Use palettegen from sequence
    pattern = str(tmp / "frame_%03d.png")
    palette = tmp / "palette.png"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-framerate",
            "8",
            "-i",
            pattern,
            "-vf",
            "palettegen=max_colors=64",
            str(palette),
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-framerate",
            "8",
            "-i",
            pattern,
            "-i",
            str(palette),
            "-lavfi",
            "paletteuse=dither=bayer",
            "-loop",
            "0",
            str(out),
        ],
        check=True,
        capture_output=True,
    )
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    render(root / "docs" / "assets" / "demo.gif")
    # also copy to artifacts when present
    art = Path("/opt/cursor/artifacts/kedger-demo.gif")
    if art.parent.is_dir():
        art.write_bytes((root / "docs" / "assets" / "demo.gif").read_bytes())
        print(f"copied {art}")
