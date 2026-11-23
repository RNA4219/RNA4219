"""プロフィールの表紙をPC用とスマートフォン用に組む。"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


HERE = Path(__file__).resolve().parent
SERIF = HERE / "fonts/InstrumentSerif-Regular.ttf"
SANS = HERE / "fonts/BarlowCondensed-SemiBold.ttf"
PAPER, INK, RED = "#ffe3b9", "#211d1b", "#ff6246"
NAME = "R_N_A"


def draw_signature(draw, x, y, available_width):
    reference = ImageFont.truetype(SERIF, 100)
    size = int(100 * available_width / reference.getlength(NAME))
    font = ImageFont.truetype(SERIF, size)
    draw.text((x, y), NAME, font=font, fill=PAPER, anchor="lm")
    # 名前に元からある二本の下線に、赤鉛筆の色を少しずらして重ねる。
    offset = max(2, round(size / 77))
    for prefix in ("R", "R_N"):
        start = x + font.getlength(prefix)
        draw.text((start + offset, y - offset), "_", font=font, fill=RED, anchor="lm")


def cover(illustration, mobile):
    width, height = (720, 414) if mobile else (1560, 570)
    edge, margin = (348, 26) if mobile else (800, 58)
    image = Image.new("RGB", (width, height), INK)
    image.paste(ImageOps.fit(illustration, (width - edge, height), centering=(0.52, 0.50)), (edge, 0))
    draw = ImageDraw.Draw(image)
    role = ImageFont.truetype(SANS, 32 if mobile else 49)
    title = ImageFont.truetype(SERIF, 35 if mobile else 48)
    draw.text((margin, 38 if mobile else 62), "AI CONDUCTOR", font=role, fill=PAPER, anchor="lm")
    draw_signature(draw, margin - 2, 163 if mobile else 255, edge - 2 * margin)
    rule_y = height - (120 if mobile else 115)
    draw.line((margin, rule_y, edge - margin, rule_y), fill=PAPER, width=2)
    draw.text((margin, height - (82 if mobile else 71)), "Quality Evidence Graph",
              font=title, fill=PAPER, anchor="lm")
    second = (margin, height - 41) if mobile else (edge - margin, height - 71)
    draw.text(second, "DEAD AIR FM", font=title, fill=PAPER, anchor="lm" if mobile else "rm")
    return image


if __name__ == "__main__":
    with Image.open(HERE / "press-hand.webp") as illustration:
        for filename, mobile in (("rna-sleeve", False), ("rna-sleeve-mobile", True)):
            cover(illustration, mobile).save(HERE.parent / "assets" / f"{filename}.webp",
                                             quality=89, method=6)
