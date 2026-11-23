"""MOSS Imageの光の原画から、GitHubの広幅・狭幅用の表紙を組む。"""

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


HERE = Path(__file__).resolve().parent
SERIF = HERE / "fonts/InstrumentSerif-Regular.ttf"
SANS = HERE / "fonts/BarlowCondensed-SemiBold.ttf"
INK = "#f4f0e7"
CYAN = "#8fe2f2"


def edge_mask(size):
    """光跡がある右端を残し、左と上下の暗部を地色につなぐ。"""
    width, height = size
    left = Image.new("L", (width, 1))
    left.putdata([min(255, round(255 * x / (width * 0.15))) for x in range(width)])
    ends = Image.new("L", (1, height))
    ends.putdata([min(255, round(255 * min(y + 1, height - y) / (height * 0.085)))
                  for y in range(height)])
    return ImageChops.darker(left.resize(size), ends.resize(size))


def cover(source, mobile):
    width, height = (768, 148) if mobile else (1408, 184)
    canvas = Image.new("RGB", (width, height), source.getpixel((0, 0)))
    art_width = round(width * (0.67 if mobile else 0.60))
    trails = source.crop((source.width // 5, 0, source.width, source.height))
    art = ImageOps.fit(trails, (art_width, height), method=Image.Resampling.LANCZOS,
                       centering=(1.0, 0.63))
    canvas.paste(art, (width - art_width, 0), edge_mask(art.size))

    draw = ImageDraw.Draw(canvas)
    margin = 26 if mobile else 44
    baseline = 83 if mobile else 126
    wordmark = ImageFont.truetype(SERIF, 91 if mobile else 112)
    draw.text((margin - 4, baseline), "R_N_A", font=wordmark, fill=INK, anchor="ls")
    for prefix in ("R", "R_N"):
        x = margin - 4 + wordmark.getlength(prefix)
        draw.text((x, baseline), "_", font=wordmark, fill=CYAN, anchor="ls")

    role = ImageFont.truetype(SANS, 32 if mobile else 34)
    label_baseline = 129 if mobile else 103
    tracking = 2.5
    pen = float(margin) if mobile else margin + wordmark.getlength("R_N_A") + 32
    for letter in "AI CONDUCTOR":
        draw.text((round(pen), label_baseline), letter, font=role, fill=INK, anchor="ls")
        pen += role.getlength(letter) + tracking
    return canvas


if __name__ == "__main__":
    with Image.open(HERE / "moss-signal.webp") as source:
        for filename, mobile in (("rna-sleeve", False), ("rna-sleeve-mobile", True)):
            banner = cover(source, mobile)
            banner.save(HERE.parent / "assets" / f"{filename}.webp", quality=93, method=6)
