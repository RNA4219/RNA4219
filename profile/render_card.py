"""R_N_A の署名と代表作へのリンクを、GitHubの広幅・狭幅用に組む。"""

from pathlib import Path
from xml.etree import ElementTree as ET

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
INK = "#101124"
WHITE = "#fafaff"
INDEX = "#f0f1fc"
VIOLET = "#6651d7"


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


def travelling_light(group, defs, halves, compact, animated):
    """帯の中心を往復する一本の経路を、光点とその尾で共有する。"""
    tip = halves * 44
    turns = halves // 2
    outward = "c21 0 22 48 44 48 c21 0 22 -48 44 -48"
    returning = "c-22 0 -23 -48 -44 -48 c-22 0 -23 48 -44 48"
    path = " ".join(["M0 -24"] + [outward] * turns + ["c36 0 36 48 0 48"] + [returning] * turns)
    # 一本の帯の半分を進んだ位置は、折り返しのいちばん外側。静止版にもここで光を当てる。
    timing = {"dur": "4s", "begin": "-2s", "repeatCount": "indefinite"}
    for length, width, color in ((8, 6, "#9e7bff"), (4, 5, "#d3c2ff"), (1.2, 4, "#fffaff")):
        trail = add(group, "path", d=path, pathLength=100, fill="none", stroke=color,
                    stroke_width=width * (1.45 if compact else 1), stroke_linecap="round",
                    stroke_dasharray=f"{length} {110 - length:g}", stroke_dashoffset=length - 50)
        if animated:
            add(trail, "animate", attributeName="stroke-dashoffset",
                values=f"{length};{length - 100:g}", **timing)

    halo = add(defs, "radialGradient", id="light-halo")
    for offset, color, opacity in ((0, "#ffffff", 1), (.22, "#f7edff", .98),
                                   (.43, "#c5a1ff", .87), (.68, "#9973ff", .42), (1, "#835bff", 0)):
        add(halo, "stop", offset=offset, stop_color=color, stop_opacity=opacity)
    head = add(group, "g")
    if animated:
        add(head, "animateMotion", path=path, calcMode="paced", **timing)
    else:
        head.set("transform", f"translate({tip + 27} 0)")
    add(head, "circle", r=25 if compact else 19, fill="url(#light-halo)")
    core = add(head, "g", transform="scale(1.4)" if compact else "scale(1)")
    add(core, "path", d="M0 -10 Q1 -2 9 0 Q1 2 0 10 Q-1 2 -9 0 Q-1 -2 0 -10 Z", fill="#fff")
    add(core, "circle", r=3.1, fill="#fff")


def helix(root, defs, compact, animated):
    """一本の帯が先端で折り返す。奥の帯、横桟、手前の帯の順に重ねる。"""
    halves = 2 if compact else 4
    tip = halves * 44
    position = ("translate(150 68) rotate(-43) scale(.65)" if compact
                else "translate(280 89) rotate(-15) scale(1.13)")
    group = add(root, "g", transform=position, aria_hidden="true")
    ribbons = " ".join(f"M{44 * i} -27 c26 0 24 48 44 48 v6 c-25 0 -28 -48 -44 -48 z"
                       for i in range(halves))
    gradient = add(defs, "linearGradient", id="ribbon-light", x1=0, x2=tip, y1=0, y2=0,
                   gradientUnits="userSpaceOnUse", spreadMethod="reflect")
    for offset, color in ((0, "#7662cf"), (".42", "#a28ce3"), (".68", "#b7a6f3"), (1, "#8a76d2")):
        add(gradient, "stop", offset=offset, stop_color=color)

    add(group, "path", d=ribbons, transform="scale(1 -1)", fill="#6966bd")
    for half in range(halves):
        x = 44 * half
        # 横桟の端は、帯と同じ三次ベジェ曲線に沿って配置する。
        for t in (.15, .33, .69, .88):
            u = 1 - t
            cx = x + 3 * u**2 * t * 21 + 3 * u * t**2 * 20 + t**3 * 44
            cy = 24 * (2 * t**2 * (3 - 2 * t) - 1)
            add(group, "path", d=f"M{cx-2:.1f} {cy:.1f} L{cx+2:.1f} {-cy:.1f}",
                stroke="#9697df", stroke_width=2.2, stroke_linecap="round")
    # 右端を閉じて、二本に見える部分が一本の鎖であることを示す。
    add(group, "path", d=f"M{tip} -24 c36 0 36 48 0 48", fill="none",
        stroke="url(#ribbon-light)", stroke_width=5.8)
    add(group, "path", d=ribbons, fill="url(#ribbon-light)")
    for half in range(halves):
        add(group, "path", d="M1 -26 C25 -26 25 21 43 22", transform=f"translate({44 * half})",
            fill="none", stroke="#cfc2fa", stroke_width=.8)
    travelling_light(group, defs, halves, compact, animated)


def card(serif, sans, compact, animated):
    width, height, split, left = (440, 92, 219, 14) if compact else (960, 124, 527, 24)
    root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width=str(width), height=str(height),
                      viewBox=f"0 0 {width} {height}", role="img", attrib={"aria-labelledby": "title"})
    add(root, "title", id="title").text = "R_N_A · AI Conductor ｜ 技術の代表作 Quality Evidence Graph を開く"
    defs = add(root, "defs")
    add(root, "rect", width=width, height=height, fill=WHITE)
    add(root, "rect", width=split, height=height, fill=INK)
    helix(root, defs, compact, animated)
    lettering(root, serif, "R_N_A", left, 53 if compact else 80, 53 if compact else 98, WHITE)
    lettering(root, sans, "AI CONDUCTOR", left + 1, 79 if compact else 112,
              16 if compact else 21, "#d4ceff", 1.35 if compact else 2.7)

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
    add(arrow, "path", d="M1 16 15 2 M4 2 H15 V13", fill="none", stroke=VIOLET,
        stroke_width=2, stroke_linecap="square")
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="unicode") + "\n"


def project_row(sans, name, description, compact):
    width, height = (440, 65) if compact else (960, 54)
    root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width=str(width), height=str(height),
                      viewBox=f"0 0 {width} {height}", role="img", attrib={"aria-labelledby": "title"})
    add(root, "title", id="title").text = f"{name} ｜ {description}"
    add(root, "rect", width=width, height=height, fill=INDEX)
    inset = 14 if compact else 22
    lettering(root, sans, name, inset, 28 if compact else 35, 26 if compact else 28, INK)
    label = add(root, "text", x=inset if compact else 420, y=52 if compact else 33,
                fill=INK, font_family="system-ui, sans-serif", font_size=16)
    label.text = description
    add(root, "path", d=f"M{inset} {height-1} H{width-inset}", stroke="#cbd0e9")
    add(root, "path", d="M0 8 H15 M9 2 15 8 9 14", fill="none", stroke=VIOLET,
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
