"""R_N_A の署名と代表作へのリンクを、GitHubの広幅・狭幅用に組む。"""

from pathlib import Path
from xml.etree import ElementTree as ET

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
INK = "#17352f"
PAPER = "#f6f1e7"
MINT = "#9dd9bc"


def add(parent, tag, **attrs):
    return ET.SubElement(parent, tag, {k.replace("_", "-"): str(v) for k, v in attrs.items()})


def lettering(parent, font, label, x, y, size, color, tracking=0):
    """同梱書体の字形で組み、閲覧端末のインストール状況に依存させない。"""
    em = font["head"].unitsPerEm
    group = add(parent, "g", transform=f"translate({x} {y}) scale({size / em} {-size / em})", fill=color)
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    advance = 0
    for char in label:
        glyph = glyphs[cmap[ord(char)]]
        if char != " ":
            pen = SVGPathPen(glyphs)
            glyph.draw(pen)
            add(group, "path", d=pen.getCommands(), transform=f"translate({advance:g})")
        advance += glyph.width + tracking * em / size
    return advance * size / em


def signature(root, defs, serif, x, baseline, size, animated):
    for index, char in enumerate("RNA"):
        x += lettering(root, serif, char, x, baseline, size, PAPER)
        if index == 2:
            break
        gap = size * 0.37
        # 波はアンダースコアの字幅だけを通る。名前の三文字は動かさない。
        group = add(root, "g", transform=f"translate({x:g} {baseline + size * .065:g}) scale({gap / 40:g})")
        clip_id = f"underscore-{index}"
        clip = add(defs, "clipPath", id=clip_id)
        add(clip, "rect", x=1, y=-6, width=38, height=12)
        slot = add(group, "g", clip_path=f"url(#{clip_id})")
        crest = "h12 c3 0 4 -4 7 -4 s4 4 7 4 h14"
        path = add(slot, "path", d=f"M-40 0 {crest} {crest}",
                   stroke=MINT, stroke_width=3.3, fill="none")
        if animated:
            add(path, "animateTransform", attributeName="transform", type="translate",
                values="0 0;40 0", dur="4s", begin=f"-{index}s", repeatCount="indefinite")
        x += gap


def card(serif, sans, compact, animated):
    width, height, split, left = (440, 92, 201, 15) if compact else (960, 124, 527, 24)
    root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width=str(width), height=str(height),
                      viewBox=f"0 0 {width} {height}", role="img", attrib={"aria-labelledby": "title"})
    add(root, "title", id="title").text = "R_N_A · AI Conductor ｜ 技術の代表作 Quality Evidence Graph を開く"
    defs = add(root, "defs")
    add(root, "rect", width=width, height=height, fill=PAPER)
    add(root, "rect", width=split, height=height, fill=INK)
    signature(root, defs, serif, left, 57 if compact else 94, 69 if compact else 109, animated)
    if compact:
        lettering(root, sans, "AI CONDUCTOR", left + 1, 82, 16, PAPER, 1.35)
    else:
        lettering(root, sans, "AI", 330, 53, 26, PAPER, 1.8)
        lettering(root, sans, "CONDUCTOR", 330, 82, 26, PAPER, 1.8)

    inset = 15 if compact else 26
    project_x = split + inset
    caption = add(root, "text", x=project_x, y=22 if compact else 33, fill=INK,
                  font_family="system-ui, sans-serif", font_size=14 if compact else 16,
                  font_weight=600, letter_spacing=1)
    caption.text = "技術の代表作"
    if compact:
        lettering(root, sans, "Quality Evidence", project_x, 53, 29, INK)
        lettering(root, sans, "Graph", project_x, 82, 29, INK)
    else:
        lettering(root, sans, "Quality Evidence Graph", project_x, 91, 43, INK)
    arrow = add(root, "g", transform=f"translate({width - inset - 15} {inset})")
    add(arrow, "path", d="M1 16 15 2 M4 2 H15 V13", fill="none", stroke=INK,
        stroke_width=2, stroke_linecap="square")
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="unicode") + "\n"


def project_row(sans, name, description, compact):
    width, height = (440, 65) if compact else (960, 54)
    root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width=str(width), height=str(height),
                      viewBox=f"0 0 {width} {height}", role="img", attrib={"aria-labelledby": "title"})
    add(root, "title", id="title").text = f"{name} ｜ {description}"
    add(root, "rect", width=width, height=height, fill=PAPER)
    inset = 14 if compact else 22
    lettering(root, sans, name, inset, 28 if compact else 35, 26 if compact else 28, INK)
    label = add(root, "text", x=inset if compact else 420, y=52 if compact else 33,
                fill=INK, font_family="system-ui, sans-serif", font_size=16)
    label.text = description
    add(root, "path", d=f"M{inset} {height-1} H{width-inset}", stroke="#c7c8bb")
    add(root, "path", d="M0 8 H15 M9 2 15 8 9 14", fill="none", stroke=INK,
        stroke_width=1.8, transform=f"translate({width-inset-16} {height//2-8})")
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="unicode") + "\n"


if __name__ == "__main__":
    with TTFont(HERE / "fonts/InstrumentSerif-Regular.ttf") as serif, \
         TTFont(HERE / "fonts/BarlowCondensed-SemiBold.ttf") as sans:
        for compact, suffix in ((False, ""), (True, "-mobile")):
            for animated, ending in ((True, ""), (False, "-still")):
                output = ASSETS / f"profile-card{suffix}{ending}.svg"
                output.write_text(card(serif, sans, compact, animated), encoding="utf-8", newline="\n")
            for slug, name, description in (
                ("rand", "RanD", "論文やAIニュースを集め、評価をMarkdownで読む"),
                ("atelier", "LLM Atelier", "Android実機のNPUで会話モデルの全43層を動かす"),
                ("direction", "Anything Frontend Art Direction", "制作者が書体や余白を選んだ理由をAIに教える"),
            ):
                output = ASSETS / f"work-{slug}{suffix}.svg"
                output.write_text(project_row(sans, name, description, compact), encoding="utf-8", newline="\n")
