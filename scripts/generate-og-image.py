#!/usr/bin/env python3
"""Generate the Open Graph / Twitter social-share card (1200x630 PNG).

Social platforms reject SVG for og:image, so we render a raster card here.
Re-run after changing copy:  python3 scripts/generate-og-image.py
Output: assets/og-image.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG_TOP = (13, 17, 28)      # deep navy
BG_BOT = (23, 31, 51)      # slightly lighter navy
INK = (237, 241, 248)
MUTED = (151, 163, 186)
ACCENT = (99, 132, 255)    # indigo
ACCENT2 = (45, 212, 191)   # teal

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "og-image.png")


def load_font(size, bold=False):
    candidates = (
        ["/System/Library/Fonts/Supplemental/Arial Bold.ttf",
         "/Library/Fonts/Arial Bold.ttf",
         "/System/Library/Fonts/Helvetica.ttc"]
        if bold else
        ["/System/Library/Fonts/Supplemental/Arial.ttf",
         "/Library/Fonts/Arial.ttf",
         "/System/Library/Fonts/Helvetica.ttc"]
    )
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def vertical_gradient(w, h, top, bottom):
    base = Image.new("RGB", (w, h), top)
    draw = ImageDraw.Draw(base)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return base


def rounded_chip(draw, xy, text, font, fg, border):
    x, y = xy
    pad_x, pad_y = 18, 10
    tb = draw.textbbox((0, 0), text, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    box = [x, y, x + tw + pad_x * 2, y + th + pad_y * 2]
    draw.rounded_rectangle(box, radius=(th + pad_y * 2) // 2, outline=border, width=2)
    draw.text((x + pad_x, y + pad_y - tb[1]), text, font=font, fill=fg)
    return box[2] - box[0]


def main():
    img = vertical_gradient(W, H, BG_TOP, BG_BOT)
    draw = ImageDraw.Draw(img)

    # accent rule top-left
    draw.rounded_rectangle([80, 96, 152, 104], radius=4, fill=ACCENT)

    f_kicker = load_font(26, bold=True)
    f_name = load_font(92, bold=True)
    f_title = load_font(40, bold=True)
    f_body = load_font(27)
    f_chip = load_font(24, bold=True)

    draw.text((80, 130), "TUSHAR TILWANI", font=f_kicker, fill=MUTED)
    draw.text((78, 168), "Frontend / Full Stack", font=f_name, fill=INK)
    draw.text((78, 268), "Software Engineer", font=f_name, fill=ACCENT)

    draw.text((80, 392), "13+ years at eBay, Oracle Cloud & Amazon", font=f_title, fill=INK)
    draw.text((80, 446),
              "React · TypeScript · Observability · Web Performance",
              font=f_body, fill=MUTED)

    # metric chips
    chips = ["2M+ concurrent users", "10M+ daily views", "100+ teams · OpenTelemetry"]
    x = 80
    for c in chips:
        w = rounded_chip(draw, (x, 520), c, f_chip, INK, ACCENT2)
        x += w + 18

    img.save(OUT, "PNG")
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
