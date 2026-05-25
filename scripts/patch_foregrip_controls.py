"""Patch v8 concept art: foregrip pistol trigger on front, +/- on aft face."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "visuals/launcher/output/radr-bazooka-side-v8-viewfinder-flush.png"
OUT = ROOT / "visuals/launcher/output/radr-bazooka-side-v11-foregrip-fix.png"


def sample_median(im: Image.Image, box: tuple[int, int, int, int]) -> tuple[int, int, int]:
    crop = im.crop(box)
    px = list(crop.getdata())
    rs = sorted(p[0] for p in px)
    gs = sorted(p[1] for p in px)
    bs = sorted(p[2] for p in px)
    mid = len(px) // 2
    return rs[mid], gs[mid], bs[mid]


def fill_rect(im: Image.Image, box: tuple[int, int, int, int]) -> None:
    draw = ImageDraw.Draw(im)
    color = sample_median(im, (box[0] + 4, box[1] + 4, box[0] + 20, box[1] + 20))
    draw.rectangle(box, fill=color)


def main() -> None:
    im = Image.open(SRC).convert("RGB")
    w, h = im.size

    # Foregrip region (left/middle grip — seeker hand). Side-view coords for 1536x1024.
    fg_center = (598, 505)
    fg_w, fg_h = 58, 118

    # 1) Remove old side +/- buttons (visible on outer face in side profile)
    fill_rect(im, (618, 468, 652, 548))

    # 2) Remove old front lever / button on muzzle-facing edge
    fill_rect(im, (628, 548, 668, 582))

    # 3) Clone rear pistol trigger, scale down, place on front of foregrip
    # Rear trigger source on pistol grip (right side of tube)
    trigger_src = (1018, 568, 1098, 652)
    trigger = im.crop(trigger_src).resize((52, 58), Image.Resampling.LANCZOS)
    # Paste on front (muzzle-facing) of foregrip
    paste_x = fg_center[0] + 18
    paste_y = fg_center[1] + 28
    im.paste(trigger, (paste_x, paste_y))

    # 4) +/- on aft face (breech-facing / left edge of foregrip)
    aft_x = fg_center[0] - fg_w // 2 - 2
    btn_w, btn_h = 14, 14
    gap = 4
    plus_box = (aft_x - btn_w, fg_center[1] - btn_h - gap // 2, aft_x, fg_center[1] - gap // 2)
    minus_box = (aft_x - btn_w, fg_center[1] + gap // 2, aft_x, fg_center[1] + btn_h + gap // 2)

    draw = ImageDraw.Draw(im)
    btn_fill = (42, 48, 38)
    btn_edge = (18, 22, 16)
    for box in (plus_box, minus_box):
        draw.rectangle(box, fill=btn_fill, outline=btn_edge, width=1)

    try:
        font = ImageFont.truetype("arial.ttf", 11)
    except OSError:
        font = ImageFont.load_default()

    draw.text((plus_box[0] + 3, plus_box[1] + 1), "+", fill=(210, 210, 200), font=font)
    draw.text((minus_box[0] + 4, minus_box[1] + 1), "-", fill=(210, 210, 200), font=font)

    # Soft blend pasted trigger edges
    region = im.crop((paste_x - 2, paste_y - 2, paste_x + 56, paste_y + 62))
    region = region.filter(ImageFilter.GaussianBlur(radius=0.4))
    im.paste(region, (paste_x - 2, paste_y - 2))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT, quality=95)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
