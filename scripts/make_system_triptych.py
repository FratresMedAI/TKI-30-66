#!/usr/bin/env python3
"""Composite Rocket (horizontal) | Launcher (horizontal) | Container (horizontal)."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ROUND = ROOT / "visuals/rocket/output/radr-round-authoritative.png"
LAUNCHER = ROOT / "visuals/launcher/output/radr-bazooka-authoritative-stowed.png"
CONTAINER = ROOT / "visuals/rocket/output/radr-container-authoritative.png"
DEFAULT_OUT = ROOT / "visuals/output/radr-system-triptych-landscape.png"

PANEL_HEIGHT = 720
GUTTER = 24
BG = (18, 22, 18)  # dark matte near launcher art
LABEL_COLOR = (220, 220, 210)


def fit_height(im: Image.Image, target_h: int) -> Image.Image:
    w, h = im.size
    scale = target_h / h
    new_w = max(1, int(w * scale))
    return im.resize((new_w, target_h), Image.Resampling.LANCZOS)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    p.add_argument("--height", type=int, default=PANEL_HEIGHT)
    args = p.parse_args()

    # Side view: nose left, tail right — same convention as launcher and tube
    rocket = Image.open(ROUND).convert("RGB")

    launcher = Image.open(LAUNCHER).convert("RGB")
    container = Image.open(CONTAINER).convert("RGB")

    panels = [
        ("Round (18 in)", fit_height(rocket, args.height)),  # horizontal L-R
        ("Launcher (40 in)", fit_height(launcher, args.height)),
        ("Protective tube", fit_height(container, args.height)),
    ]

    label_h = 36
    total_w = sum(im.size[0] for _, im in panels) + GUTTER * (len(panels) + 1)
    total_h = args.height + label_h + GUTTER * 2
    canvas = Image.new("RGB", (total_w, total_h), BG)

    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()

    x = GUTTER
    y_img = GUTTER + label_h
    for title, im in panels:
        draw.text((x, GUTTER), title, fill=LABEL_COLOR, font=font)
        canvas.paste(im, (x, y_img))
        x += im.size[0] + GUTTER

    args.out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.out, format="PNG", optimize=True)
    print(f"Wrote {args.out} ({canvas.size[0]} x {canvas.size[1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
