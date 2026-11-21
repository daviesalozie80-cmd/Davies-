"""Banner v2: illustrated "skyline of the world economy" (2560x1440).

Flat, ink-outlined landmarks of world financial and trade hubs frame the title, over a light sky,
with a container harbour in the middle. Marlow (same code as the character bible) stands on the quay.
Usage: python3 build_skyline.py   -> src/banner-skyline-2560x1440.svg (+ safe-area guide)
"""
import importlib.util, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv = sys.argv[:1]
spec = importlib.util.spec_from_file_location("brand", os.path.join(HERE, "build.py"))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
gen, M, INK = B.gen, B.M, B.INK

W, H = 2560, 1440
SKY_T, SKY_B, WATER, WATER_D = "#CFE0E8", "#EEF1EC", "#9DBBC8", "#86A9B8"
SAND, BROWN, BROWN_D, SLATE, SLATE_L, GLASS, GLASS_D, STONE = "#D8C7A8", "#B08A6A", "#977257", "#7F8C9B", "#B9C4CE", "#A7BDCB", "#8FA7B7", "#C9B99C"
NAVY, TEAL_D, RED, YELLOW, CREAM, WHITE = "#10213A", "#15444C", B.RED, B.YELLOW, B.CREAM, B.WHITE
SW = 3.2  # building outline width (matches character outline weight at banner scale)

def P(d, fill="none", sw=SW, stroke=INK, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'

def R(x, y, w, h, fill, sw=SW, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"/>'

def hlines(x, y1, y2, w, step, sw=2, op=0.45):
    return "".join(P(f"M{x+6},{y} L{x+w-6},{y}", sw=sw, extra=f'opacity="{op}"') for y in range(int(y1), int(y2), step))

def vlines(x1, x2, y, h, step, sw=2, op=0.45):
    return "".join(P(f"M{x},{y+6} L{x},{y+h-6}", sw=sw, extra=f'opacity="{op}"') for x in range(int(x1), int(x2), step))

def windows(x, y, w, h, cols, rows, fill=SLATE_L, pad=12):
    cw, ch = (w - pad * (cols + 1)) / cols, (h - pad * (rows + 1)) / rows
    return "".join(f'<rect x="{x+pad+i*(cw+pad):.1f}" y="{y+pad+j*(ch+pad):.1f}" width="{cw:.1f}" height="{ch:.1f}" fill="{fill}" stroke="{INK}" stroke-width="1.8"/>'
                   for i in range(cols) for j in range(rows))

# ---------------------------------------------------------------- landmarks (original stylised drawings)
def art_deco(x, base, w, top):
    """New-York-style stepped Art Deco tower with spire."""
    h = base - top
    s = [R(x, top + h * 0.30, w, h * 0.70, BROWN),
         R(x + w * 0.12, top + h * 0.16, w * 0.76, h * 0.16, BROWN),
         R(x + w * 0.26, top + h * 0.05, w * 0.48, h * 0.12, BROWN_D),
         P(f"M{x+w*0.42},{top+h*0.05} L{x+w*0.5},{top-60} L{x+w*0.58},{top+h*0.05} Z", fill=BROWN_D),
         vlines(x + 16, x + w - 8, top + h * 0.30, h * 0.70, 22, op=0.5), vlines(x + w * 0.12 + 14, x + w * 0.88 - 6, top + h * 0.16, h * 0.16, 20, op=0.5)]
    return "".join(s)

def glass_tower(x, base, w, top):
    h = base - top
    return (P(f"M{x},{base} L{x},{top+90} L{x+w},{top} L{x+w},{base} Z", fill=GLASS)
            + P(f"M{x+w*0.55},{top+40} L{x+w*0.55},{base}", sw=2.4, extra='opacity="0.6"')
            + "".join(P(f"M{x+6},{y} L{x+w-6},{y}", sw=1.8, extra='opacity="0.35"') for y in range(int(top + 110), int(base), 26))
            + P(f"M{x+w*0.18},{top+160} L{x+w*0.45},{top+60}", stroke=WHITE, sw=5, extra='opacity="0.7"'))

def clock_tower(cx, base, top):
    """London-style Gothic clock tower."""
    w = 86
    x = cx - w / 2
    shaft_top = top + 230
    s = [R(x, shaft_top, w, base - shaft_top, SAND),
         vlines(x + 14, x + w - 6, shaft_top + 120, base - shaft_top - 120, 18, op=0.5),
         R(x - 8, top + 150, w + 16, 92, STONE),
         f'<circle cx="{cx}" cy="{top+196}" r="31" fill="{WHITE}" stroke="{INK}" stroke-width="{SW}"/>',
         P(f"M{cx},{top+196} L{cx},{top+176} M{cx},{top+196} L{cx+13},{top+203}", sw=3),
         R(x - 2, top + 118, w + 4, 34, SAND),
         P(f"M{x-2},{top+118} L{cx},{top} L{x+w+2},{top+118} Z", fill=SLATE),
         P(f"M{cx},{top} L{cx},{top-46}", sw=4)]
    return "".join(s)

def pearl_tower(cx, base, top):
    """Shanghai-style tower: tripod, two spheres, antenna."""
    s = [P(f"M{cx-70},{base} L{cx-12},{top+520} M{cx+70},{base} L{cx+12},{top+520} M{cx},{base} L{cx},{top+520}", sw=9),
         P(f"M{cx-70},{base} L{cx-12},{top+520} M{cx+70},{base} L{cx+12},{top+520}", stroke=SLATE_L, sw=4),
         R(cx - 14, top + 150, 28, 380, SLATE_L),
         f'<circle cx="{cx}" cy="{top+500}" r="64" fill="{RED}" stroke="{INK}" stroke-width="{SW}"/>',
         P(f"M{cx-46},{top+478} Q{cx-30},{top+452} {cx-6},{top+448}", stroke=WHITE, sw=6, extra='opacity="0.55"'),
         f'<rect x="{cx-70}" y="{top+494}" width="140" height="12" fill="{SLATE}" stroke="{INK}" stroke-width="2.2"/>',
         f'<circle cx="{cx}" cy="{top+230}" r="40" fill="{RED}" stroke="{INK}" stroke-width="{SW}"/>',
         f'<circle cx="{cx}" cy="{top+120}" r="15" fill="{RED}" stroke="{INK}" stroke-width="2.6"/>',
         P(f"M{cx},{top+105} L{cx},{top}", sw=4)]
    return "".join(s)

def spire(cx, base, top):
    """Dubai-style stepped, tapering supertall."""
    h = base - top
    steps = 7
    out = []
    for i in range(steps):
        w = 150 * (1 - i / (steps + 1.5))
        y0 = base - h * (i + 1) / (steps + 1)
        y1 = base - h * i / (steps + 1)
        out.append(R(cx - w / 2, y0, w, y1 - y0, SLATE_L if i % 2 == 0 else GLASS))
        out.append(P(f"M{cx},{y0+8} L{cx},{y1-8}", sw=1.8, extra='opacity="0.5"'))
    out.append(P(f"M{cx-10},{base-h*steps/(steps+1)} L{cx},{top} L{cx+10},{base-h*steps/(steps+1)} Z", fill=SLATE_L))
    return "".join(out)

def sky_hotel(x, base, top):
    """Singapore-style three towers with a ship-shaped sky deck."""
    out = []
    for i in range(3):
        tx = x + i * 78
        out.append(P(f"M{tx},{base} L{tx+8},{top+40} L{tx+52},{top+40} L{tx+60},{base} Z", fill=SAND))
        out.append(P(f"M{tx+30},{top+50} L{tx+30},{base}", sw=2, extra='opacity="0.5"'))
        out.append("".join(P(f"M{tx+10},{y} L{tx+52},{y}", sw=1.6, extra='opacity="0.35"') for y in range(int(top + 70), int(base), 24)))
    out.append(P(f"M{x-24},{top+40} L{x+250},{top+28} L{x+262},{top+16} L{x-30},{top+26} Z", fill=STONE))
    return "".join(out)

def office(x, base, w, h, fill, cols, rows):
    return R(x, base - h, w, h, fill) + windows(x, base - h, w, h, cols, rows)

def crane(x, quay, s=1.0, col=TEAL_D):
    g = [P("M0,0 L0,-300 M70,0 L70,-300", stroke=col, sw=14), P("M0,0 L0,-300 M70,0 L70,-300", sw=2.4),
         P("M0,-150 L70,-150 M0,-300 L70,-300 M0,-150 L70,-300", stroke=col, sw=8),
         R(-40, -330, 280, 30, col), P("M-40,-330 L35,-410 L110,-330", stroke=INK, sw=3),
         R(150, -326, 34, 46, YELLOW), P("M167,-280 L167,-200", sw=2.6),
         R(147, -200, 40, 26, RED, sw=2.4)]
    return f'<g transform="translate({x},{quay}) scale({s})">{"".join(g)}</g>'

def container_stack(x, base, cols_n, rows_n, w=66, h=38):
    pal = [RED, TEAL_D, YELLOW, CREAM, SLATE, "#2B6E73", RED, SAND]
    out = []
    for r in range(rows_n):
        for c in range(cols_n - r % 2):
            col = pal[(c * 3 + r * 5) % len(pal)]
            cx = x + c * w + (r % 2) * w / 2
            out.append(R(cx, base - (r + 1) * h, w, h, col, sw=2.6))
            out.append(vlines(cx + 8, cx + w - 4, base - (r + 1) * h, h, 9, sw=1.4, op=0.35))
    return "".join(out)

def cloud(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            + P("M0,40 Q-6,8 30,10 Q44,-22 84,-6 Q112,-24 136,6 Q170,6 168,40 Z", fill=WHITE, sw=2.6, extra='stroke-opacity="0.35"')
            + "</g>")

def pier(x, top, w):
    """Quay deck with a dark edge and pilings standing in the water (keeps the lower banner open)."""
    posts = "".join(f'<rect x="{px}" y="{top+64}" width="16" height="70" fill="#4A5361" stroke="{INK}" stroke-width="2.4"/>' for px in range(int(x + 30), int(x + w - 20), 90))
    refl = "".join(P(f"M{px-6},{top+150} l28,0", stroke=WHITE, sw=3, extra='opacity="0.45"') for px in range(int(x + 30), int(x + w - 20), 90))
    return posts + refl + R(x, top, w, 64, "#5B6573") + R(x, top + 46, w, 18, "#4A5361", sw=2.4)

# ---------------------------------------------------------------- composition
QL, QR, SHORE = 1000, 965, 862   # left quay, right quay, far-shore/water line
o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{B.FONTS}',
     f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SKY_T}"/><stop offset="0.6" stop-color="{SKY_B}"/></linearGradient>'
     f'<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER}"/><stop offset="1" stop-color="{WATER_D}"/></linearGradient></defs>',
     f'<rect width="{W}" height="{H}" fill="url(#sky)"/>']
# clouds + trade routes across the sky (above the safe area)
o += [cloud(700, 170, 1.3), cloud(1480, 110, 1.0), cloud(1900, 260, 0.8), cloud(1080, 300, 0.7)]
for (a, b, lift, col) in (((600, 300), (2085, 330), 0.16, NAVY), ((260, 120), (2220, 160), 0.07, RED), ((2085, 330), (2400, 470), 0.3, NAVY)):
    o.append(B.arc(a, b, lift=lift, stroke=col, stroke_opacity="0.35", stroke_width="4", stroke_dasharray="3 14", stroke_linecap="round"))
# far shore skyline (distant, behind water)
far = []
xx = 940
for i, (w, h) in enumerate([(60, 44), (40, 70), (90, 36), (34, 96), (70, 54), (50, 30), (44, 82), (110, 40), (60, 64), (40, 28), (80, 50), (52, 74)]):
    far.append(f'<rect x="{xx}" y="{SHORE-h}" width="{w}" height="{h}" fill="#B7C7D1"/>'); xx += w + 6
o.append("".join(far))
o.append(f'<rect x="0" y="{SHORE}" width="{W}" height="{H-SHORE}" fill="url(#sea)"/>')
o.append(P(f"M0,{SHORE} L{W},{SHORE}", sw=2.4, extra='opacity="0.5"'))
for (wx, wy, ww) in ((1040, 930, 60), (1180, 980, 80), (1560, 950, 70), (1660, 1010, 50), (1300, 1080, 90), (1480, 1150, 60), (1120, 1200, 70)):
    o.append(P(f"M{wx},{wy} q{ww/4},-10 {ww/2},0 t{ww/2},0", stroke=WHITE, sw=3, extra='opacity="0.6"'))

# LEFT city
left = [art_deco(30, QL, 220, 70),
        office(0, QL, 200, 300, SLATE, 3, 5),
        glass_tower(270, QL, 170, 190),
        office(430, QL, 190, 400, STONE, 3, 6),
        clock_tower(600, QL, 300),
        office(650, QL, 150, 250, SLATE, 2, 4),
        office(780, QL, 120, 170, SAND, 2, 3)]
o += left
o.append(pier(-10, QL, 940))                                             # left quay
o.append(P(f"M-10,{QL+16} L930,{QL+16}", stroke=YELLOW, sw=6))           # quay edge marking
o.append(container_stack(740, QL, 3, 2))

# RIGHT city + port
right = [office(2005, QR, 150, 300, STONE, 2, 5),
         pearl_tower(2085, QR, 250),
         spire(2250, QR, 20),
         office(2160, QR, 160, 230, SLATE, 2, 4),
         sky_hotel(2310, QR, 470),
         office(2440, QR, 140, 360, BROWN, 2, 6)]
o += right
o.append(pier(1690, QR, 900))                                           # right quay
o.append(P(f"M1690,{QR+16} L2580,{QR+16}", stroke=YELLOW, sw=6))
o.append(container_stack(1720, QR, 3, 2))

# ship in the harbour (centre, below the title)
o.append(B.cargo_ship(1265, 925, 0.9))
o.append(f'<g transform="translate(2560,0) scale(-1,1)">{B.cargo_ship(780, 1290, 0.62)}</g>')  # smaller ship heading west (TV area)

bg_layers = list(o)  # background only (used by the 'Subscribe' banner)
# Marlow on the left quay, presenting the title (face inside the safe area)
o.append(f'<ellipse cx="650" cy="{QL+4}" rx="80" ry="12" fill="#000" opacity="0.18"/>')
o.append(gen.place(gen.figure(M, pose="presenting"), 650, QL, 1.45))

# Title block (centre of the safe area) with a white halo, like hand-lettered signage
tx = 1420
def T(y, size, weight, text, fill, ls=0, family="Montserrat", halo=16):
    return (f'<text x="{tx}" y="{y}" text-anchor="middle" font-family="{family}" font-weight="{weight}" font-size="{size}" letter-spacing="{ls}" '
            f'fill="{fill}" stroke="{WHITE}" stroke-width="{halo}" stroke-linejoin="round" paint-order="stroke">{text}</text>')
o.append(T(648, 112, 900, "GEOECONOMICS", NAVY, 1, halo=18))
o.append(T(738, 70, 800, "EXPLAINED", RED, 40, halo=16).replace(f'x="{tx}"', f'x="{tx+20}"'))
o.append(T(800, 30, 600, "Understanding the Money, Resources &amp; Power Shaping Our World", NAVY, 0, "Inter", halo=10))
o.append("</svg>")
svg = "".join(o)

guide = svg.replace("</svg>", '<rect x="507" y="508" width="1546" height="423" fill="none" stroke="#FF00AA" stroke-width="4" stroke-dasharray="20 10"/>'
                              '<rect x="0" y="508" width="2560" height="423" fill="none" stroke="#00B7FF" stroke-width="3" stroke-dasharray="10 10"/></svg>')
os.makedirs(os.path.join(HERE, "src"), exist_ok=True)
open(os.path.join(HERE, "src", "banner-skyline-2560x1440.svg"), "w").write(svg)
open(os.path.join(HERE, "src", "banner-skyline-safe-area-guide.svg"), "w").write(guide)
print("built skyline")

# ---------------------------------------------------------------- Banner v3: background + "Subscribe"
sub = bg_layers + [
    f'<text x="1280" y="768" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="212" letter-spacing="2" '
    f'fill="{NAVY}" stroke="{WHITE}" stroke-width="24" stroke-linejoin="round" paint-order="stroke">Subscribe</text>',
    "</svg>"]
sub_svg = "".join(sub)
open(os.path.join(HERE, "src", "banner-subscribe-2560x1440.svg"), "w").write(sub_svg)
open(os.path.join(HERE, "src", "banner-subscribe-safe-area-guide.svg"), "w").write(sub_svg.replace("</svg>",
    '<rect x="507" y="508" width="1546" height="423" fill="none" stroke="#FF00AA" stroke-width="4" stroke-dasharray="20 10"/></svg>'))
print("built subscribe")
