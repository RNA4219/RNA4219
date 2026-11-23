"""DEAD AIR FMの87.9 MHzの録音から、プロフィール用の動く波形を作る。"""

import argparse
import base64
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
RATE = 8000
BPM = 128
BEATS = 8
SECONDS = BEATS * 60 / BPM
FRAMES = 75
SCALE = 2
BG, GRID = "#101820", "#293942"
PAPER, MUTED, WAVE, LIT, CUE = "#f5f0df", "#b9cac7", "#75aaa9", "#c1f5e8", "#ff8866"


def read_audio(html_path):
    html = html_path.read_text(encoding="utf-8")
    track = re.search(r'<script type="audio/mp4" id="recording-0" data-start="([\d.]+)"[^>]*>([^<]+)</script>', html)
    if not track or "Midnight Circuit" not in html:
        raise ValueError("87.9 MHzの録音が見つかりません")
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", "pipe:0", "-ac", "1", "-ar", str(RATE),
         "-f", "s16le", "pipe:1"],
        input=base64.b64decode(track[2]), stdout=subprocess.PIPE, check=True,
    ).stdout
    # ラジオの再生開始位置を基準に、3小節目と4小節目を切り出す。
    start = round((float(track[1]) + SECONDS) * RATE)
    samples = np.frombuffer(pcm, dtype="<i2")[start:start + round(SECONDS * RATE)]
    if len(samples) != round(SECONDS * RATE):
        raise ValueError("録音が指定区間より短いです")
    return samples.astype(float)


def font(filename, size):
    return ImageFont.truetype(HERE / "fonts" / filename, round(size * SCALE))


def tracked(draw, x, y, label, face, spacing, color):
    for letter in label:
        draw.text((round(x * SCALE), y * SCALE), letter, font=face, fill=color, anchor="ls")
        x += face.getlength(letter) / SCALE + spacing


def make_banner(samples, mobile):
    width, height = (400, 78) if mobile else (920, 108)
    margin, scope_x = (13, 146) if mobile else (24, 262)
    right = width - margin
    top, bottom = (27, 66) if mobile else (35, 92)
    mid = (top + bottom) / 2
    scope_width = right - scope_x
    base = Image.new("RGB", (width * SCALE, height * SCALE), BG)
    draw = ImageDraw.Draw(base)

    def line(coords, color, weight=1):
        draw.line(tuple(round(n * SCALE) for n in coords), fill=color, width=round(weight * SCALE))

    wordmark = font("InstrumentSerif-Regular.ttf", 43 if mobile else 66)
    sans = "BarlowCondensed-SemiBold.ttf"
    draw.text((margin * SCALE, (46 if mobile else 69) * SCALE), "R_N_A",
              font=wordmark, fill=PAPER, anchor="ls")
    tracked(draw, margin + 1, 65 if mobile else 91, "AI CONDUCTOR",
            font(sans, 13 if mobile else 16), 1.35 if mobile else 2.7, MUTED)

    label_y = 17 if mobile else 24
    # 再生ボタンと同じ向きの小さな印を局名に添える。画像全体が選局画面へのリンク。
    draw.polygon([(scope_x * SCALE, (label_y - 8) * SCALE), (scope_x * SCALE, label_y * SCALE),
                  ((scope_x + 6) * SCALE, (label_y - 4) * SCALE)], fill=CUE)
    label = font(sans, 13 if mobile else 16)
    tracked(draw, scope_x + 12, label_y, "DEAD AIR FM", label, 1.0, PAPER)
    draw.text((right * SCALE, label_y * SCALE), "87.9 MHz", font=label, fill=MUTED, anchor="rs")

    for beat in range(BEATS + 1):
        x = scope_x + scope_width * beat / BEATS
        line((x, top, x, bottom), GRID, 0.5)
        line((x, bottom + 2, x, bottom + 4), MUTED, 0.5)
    line((scope_x, mid, right, mid), GRID)

    # 縦線1本につき同じ長さの音を取り、実際の正負のピークを上下に描く。
    columns = scope_width // 2
    bins = np.array_split(samples, columns)
    gain = (bottom - top - 4) / (2 * max(abs(samples.min()), samples.max()))
    strokes = []
    for index, chunk in enumerate(bins):
        x = scope_x + index * scope_width / (columns - 1)
        coords = (x, mid - max(0, chunk.max()) * gain, x, mid - min(0, chunk.min()) * gain)
        line(coords, WAVE)
        strokes.append(tuple(round(n * SCALE) for n in coords))

    def frame(index):
        image = base.copy()
        ink = ImageDraw.Draw(image)
        head = (scope_x + scope_width * index / FRAMES) * SCALE
        for coords in strokes:
            if head - 0.09 * scope_width * SCALE <= coords[0] <= head:
                ink.line(coords, fill=LIT, width=SCALE)
        x = round(head)
        ink.line((x, top * SCALE, x, bottom * SCALE), fill=CUE, width=2 * SCALE)
        ink.polygon([(x - 3 * SCALE, (top - 2) * SCALE), (x + 3 * SCALE, (top - 2) * SCALE),
                     (x, (top + 2) * SCALE)], fill=CUE)
        return image

    stem = "radio-wave-mobile" if mobile else "radio-wave"
    still = frame(FRAMES // 3)
    still.save(ASSETS / f"{stem}.png", optimize=True)
    palette = still.quantize(colors=128)
    frames = [frame(i).quantize(palette=palette, dither=Image.Dither.NONE) for i in range(FRAMES)]
    frames[0].save(ASSETS / f"{stem}.gif", save_all=True, append_images=frames[1:],
                   duration=round(SECONDS * 1000 / FRAMES), disposal=1, loop=0, optimize=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("radio_html", type=Path, help="DEAD AIR FMのindex.html")
    audio = read_audio(parser.parse_args().radio_html)
    for narrow in (False, True):
        make_banner(audio, narrow)
