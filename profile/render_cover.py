"""QEGの公開判定例から、GitHub用の譜面をPC幅とスマートフォン幅で作る。"""

import json
from pathlib import Path
from urllib.request import urlopen

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
FIXTURES = "https://raw.githubusercontent.com/RNA4219/quality-evidence-graph/v0.4.2/fixtures"
PAPER, INK, RULE, ACCENT = "#101124", "#fafaff", "#9199bd", "#c0acff"
SERIF = HERE / "fonts/InstrumentSerif-Regular.ttf"
SANS = HERE / "fonts/BarlowCondensed-SemiBold.ttf"


def fixture(case, filename):
    with urlopen(f"{FIXTURES}/{case}/{filename}.json", timeout=20) as response:
        return json.load(response)


def verdicts():
    case = "positive-placement-change-retirement"
    inputs = fixture(case, "gate-input")
    replacement = next(node for node in inputs["graph"]["nodes"] if node["id"] == "hate:AETE-login-001")
    minimum = inputs["policy"]["placementRetirementPolicy"]["minConsecutiveGreen"]
    approved = fixture(case, "expected-gate-verdict")
    rejected = fixture("negative-retirement-manual-replacement", "expected-gate-verdict")
    return (replacement["recentGreenRuns"], minimum, approved["expectedVerdict"],
            rejected["expectedVerdict"], rejected["expectedDisqualifications"][0]["code"])


def cover(mobile, values):
    runs, minimum, passed, rejected, reason = values
    width, height = (720, 470) if mobile else (1560, 540)
    image = Image.new("RGB", (width, height), PAPER)
    draw = ImageDraw.Draw(image)

    def label(x, y, text, size, face=SANS, fill=INK, anchor="lm"):
        font = ImageFont.truetype(str(face), size)
        draw.text((x, y), text, font=font, fill=fill, anchor=anchor)

    margin = 36 if mobile else 64
    top = 38 if mobile else 53
    label(margin, top, "R_N_A", 41 if mobile else 53)
    label(width - margin, top, "AI CONDUCTOR", 29 if mobile else 41, anchor="rm")
    draw.line((margin, top + 33, width - margin, top + 33), fill=RULE, width=2)

    if mobile:
        label(margin - 3, 134, "Quality Evidence Graph", 81, SERIF)
        x, right, first, second = margin, width - margin, 253, 393
    else:
        label(margin - 4, 210, "Quality Evidence", 131, SERIF)
        label(margin - 4, 369, "Graph", 179, SERIF)
        x, right, first, second = 866, width - margin, 223, 392

    # 一点が一回の連続成功。最初の minimum 点だけを下の括弧で結ぶ。
    end = right - (165 if mobile else 160)
    start = x + 18
    step = (end - start - 25) / (runs - 1)
    label(x, first - 47, "E2E", 33)
    label(right, first - 47, passed, 42, SERIF, anchor="rm")
    draw.line((x, first, right, first), fill=RULE, width=2)
    for index in range(runs):
        note = round(start + index * step)
        draw.line((note + 8, first, note + 8, first - 21), fill=INK, width=2)
        draw.ellipse((note - 9, first - 6, note + 9, first + 6), fill=INK)
    threshold = int(start + (minimum - 1) * step)
    draw.line([(start, first + 12), (start, first + 22),
               (threshold, first + 22), (threshold, first + 12)], fill=RULE, width=2)
    label(right, first + 25, f"{runs} RUNS / {minimum} REQUIRED", 25 if mobile else 30, anchor="rm")

    label(x, second - 42, "MANUAL", 33)
    label(right, second - 42, reason, 37, fill=ACCENT, anchor="rm")
    gap = start + step * 2
    draw.line((x, second, gap - 16, second), fill=RULE, width=2)
    draw.line((gap + 16, second, right, second), fill=RULE, width=2)
    for dx in (-5, 5):
        draw.line((gap + dx - 4, second + 10, gap + dx + 4, second - 10), fill=ACCENT, width=3)
    label(right, second + 27, rejected, 31, SERIF, fill=ACCENT, anchor="rm")
    return image


if __name__ == "__main__":
    examples = verdicts()
    for name, narrow in [("qeg-score", False), ("qeg-score-mobile", True)]:
        cover(narrow, examples).save(ASSETS / f"{name}.png", optimize=True)
