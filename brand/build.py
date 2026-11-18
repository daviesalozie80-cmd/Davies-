"""Builds the GEOECONOMICS EXPLAINED banner (2560x1440) and profile picture (1024x1024).

Marlow is drawn by the same parametric code as the character bible
(../character-system/gen.py), so he is identical to the approved design.
Usage: python3 build.py   (reads ./assets: map.json + font files; render PNGs with assets/render.js)
"""
import base64, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "assets")
spec = importlib.util.spec_from_file_location("gen", os.path.join(HERE, "..", "character-system", "gen.py"))
gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)

# One brand expression added on top of the library: confident = gently raised brows + calm smile.
gen.EXPR["confident"] = dict(brows=((-4, -2), (-4, -2)), eyes="oval", mouth="smile")
gen.POSES["presenting"] = dict(view="3q", expr="confident",
                               arms=[[(-30, -172), (-44, -110)], [(30, -172), (66, -196), (104, -236)]],
                               legs=[[(-12, -75), (-16, 0)], [(12, -75), (18, 0)]])
M = gen.CAST["marlow"]
MAP = json.load(open(os.path.join(ASSETS, "map.json")))

# ---------------------------------------------------------------- brand palette
NAVY_D, NAVY, TEAL_D, TEAL, CREAM, WHITE = "#0B1726", "#10213A", "#15444C", "#2B6E73", "#F2EDE4", "#FFFFFF"
RED, YELLOW = "#B5473A", "#E0A43A"

def font_face(fam, weight, file):
    b = base64.b64encode(open(os.path.join(ASSETS, file), "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{weight};src:url(data:font/woff2;base64,{b}) format('woff2');}}"

FONTS = "<style>" + font_face("Montserrat", 900, "montserrat-latin-900-normal.woff2") + \
        font_face("Montserrat", 800, "montserrat-latin-800-normal.woff2") + \
        font_face("Inter", 500, "inter-latin-500-normal.woff2") + font_face("Inter", 600, "inter-latin-600-normal.woff2") + "</style>"

def globe(cx, cy, r, land_op=0.95):
    """Orthographic globe (generated at centre 512, radius 400) re-scaled to (cx, cy, r)."""
    s = r / 400
    t = f"translate({cx - 512*s:.1f},{cy - 512*s:.1f}) scale({s:.4f})"
    return (f'<g transform="{t}">'
            f'<path d="{MAP["globeSphere"]}" fill="{TEAL_D}"/>'
            f'<path d="{MAP["globeGrat"]}" fill="none" stroke="{CREAM}" stroke-opacity="0.10" stroke-width="{1.6/s:.2f}"/>'
            f'<path d="{MAP["globeLand"]}" fill="{TEAL}" fill-opacity="{land_op}" stroke="{TEAL_D}" stroke-width="{1.2/s:.2f}"/>'
            f'<path d="{MAP["globeSphere"]}" fill="none" stroke="{YELLOW}" stroke-opacity="0.55" stroke-width="{4/s:.2f}"/>'
            f'</g>')

def arc(a, b, lift=0.22, **kw):
    """Curved trade route that bows upward (northward) between two hubs."""
    (x1, y1), (x2, y2) = a, b
    cx = (x1 + x2) / 2
    cy = min(y1, y2) - abs(x2 - x1) * lift - 20
    attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<path d="M{x1},{y1} Q{cx:.1f},{cy:.1f} {x2},{y2}" fill="none" {attrs}/>'

# ---------------------------------------------------------------- shared props (flat vector, ink outlines)
INK = gen.INK
def cargo_ship(x, y, s=1.0):
    cols = [RED, TEAL, YELLOW, CREAM, "#5B6573", TEAL, RED, CREAM, YELLOW, "#5B6573"]
    boxes = []
    for row in range(3):
        for i in range(8 - row):
            c = cols[(i * 3 + row * 2) % len(cols)]
            boxes.append(f'<rect x="{40 + i*34 + row*10}" y="{-60 - row*24}" width="32" height="22" fill="{c}" stroke="{INK}" stroke-width="2.2"/>')
    hull = (f'<path d="M0,-40 L330,-40 L300,10 L24,10 Z" fill="#22344D" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M14,-8 L318,-8 L308,10 L24,10 Z" fill="{RED}" stroke="{INK}" stroke-width="2.4"/>')
    bridge = (f'<rect x="286" y="-100" width="34" height="60" fill="{CREAM}" stroke="{INK}" stroke-width="2.4"/>'
              f'<rect x="291" y="-92" width="24" height="8" fill="#22344D"/><rect x="300" y="-122" width="8" height="22" fill="#5B6573" stroke="{INK}" stroke-width="2"/>')
    wake = "".join(f'<path d="M{-20 - i*40},{18 + i*4} q20,-8 40,0" fill="none" stroke="{CREAM}" stroke-opacity="{0.35 - i*0.08}" stroke-width="3" stroke-linecap="round"/>' for i in range(4))
    return f'<g transform="translate({x},{y}) scale({s})">{wake}{"".join(boxes)}{bridge}{hull}</g>'

def pumpjack(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M-70,0 L70,0" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M-30,0 L0,-110 L30,0 Z" fill="none" stroke="#5B6573" stroke-width="10" stroke-linejoin="round"/>'
            f'<g transform="rotate(-12 0 -112)"><rect x="-110" y="-124" width="200" height="22" rx="6" fill="#5B6573" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M-110,-124 q-34,10 -30,44 l24,0 q0,-26 20,-30 Z" fill="{YELLOW}" stroke="{INK}" stroke-width="3"/></g>'
            f'<path d="M-128,-82 L-128,0" stroke="{CREAM}" stroke-opacity="0.6" stroke-width="3"/>'
            f'<circle cx="0" cy="-112" r="9" fill="{CREAM}" stroke="{INK}" stroke-width="3"/>'
            f'<rect x="60" y="-52" width="40" height="52" rx="6" fill="{RED}" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M60,-36 L100,-36 M60,-18 L100,-18" stroke="{INK}" stroke-width="2.4"/></g>')

def mini_chart(x, y, w, h):
    up = [(0, .80), (.12, .74), (.24, .77), (.36, .60), (.48, .64), (.60, .45), (.72, .50), (.84, .30), (1, .18)]
    dn = [(0, .35), (.14, .40), (.28, .36), (.42, .52), (.56, .48), (.70, .63), (.84, .60), (1, .76)]
    def pl(pts): return " ".join(f"{x + px*w:.1f},{y + py*h:.1f}" for px, py in pts)
    grid = "".join(f'<path d="M{x},{y + h*k/4:.1f} L{x+w},{y + h*k/4:.1f}" stroke="{CREAM}" stroke-opacity="0.08" stroke-width="2"/>' for k in range(5))
    return (grid + f'<polyline points="{pl(dn)}" fill="none" stroke="{RED}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity="0.8"/>'
            f'<polyline points="{pl(up)}" fill="none" stroke="{YELLOW}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity="0.9"/>'
            f'<circle cx="{x + w}" cy="{y + up[-1][1]*h}" r="9" fill="{YELLOW}" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="{x + w}" cy="{y + dn[-1][1]*h}" r="9" fill="{RED}" stroke="{INK}" stroke-width="2.5"/>')

def map_pin(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0,0 C-14,-18 -20,-28 -20,-38 A20,20 0 1 1 20,-38 C20,-28 14,-18 0,0 Z" fill="{RED}" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="0" cy="-38" r="7" fill="{CREAM}"/></g>')

# ---------------------------------------------------------------- BANNER 2560x1440
W, H = 2560, 1440
SAFE = (507, 508, 1546, 423)  # YouTube "safe area for all devices"
H_ = MAP["hubs"]
routes = [("Shanghai", "Singapore"), ("Singapore", "Dubai"), ("Dubai", "Rotterdam"), ("Rotterdam", "NewYork"), ("Houston", "Rotterdam"),
          ("Santos", "Rotterdam"), ("Lagos", "Rotterdam"), ("Mumbai", "Dubai"), ("Singapore", "Sydney"), ("Tokyo", "Shanghai"), ("NewYork", "Santos"), ("LosAngeles", "Houston")]
b = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{FONTS}',
     '<defs>'
     f'<radialGradient id="bg" cx="50%" cy="48%" r="75%"><stop offset="0" stop-color="#132845"/><stop offset="1" stop-color="{NAVY_D}"/></radialGradient>'
     '<filter id="blur" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="60"/></filter>'
     '<filter id="soft"><feGaussianBlur stdDeviation="18"/></filter>'
     f'<radialGradient id="textglow"><stop offset="0" stop-color="{NAVY_D}" stop-opacity="0.88"/><stop offset="0.55" stop-color="{NAVY_D}" stop-opacity="0.7"/><stop offset="1" stop-color="{NAVY_D}" stop-opacity="0"/></radialGradient>'
     '<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.05 0"/></filter>'
     '</defs>',
     f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
     # world map + borders
     f'<path d="{MAP["land"]}" fill="#173A55" fill-opacity="0.75"/>',
     f'<path d="{MAP["borders"]}" fill="none" stroke="{NAVY_D}" stroke-opacity="0.8" stroke-width="1.4"/>']
# trade routes + hubs
for i, (a, c) in enumerate(routes):
    hi = i in (2, 3, 5)
    b.append(arc(H_[a], H_[c], lift=0.18, stroke=CREAM if hi else YELLOW, stroke_opacity="0.55" if hi else "0.42",
                 stroke_width="4" if hi else "3", stroke_dasharray="2 12" if not hi else "18 10", stroke_linecap="round"))
for k, (x, y) in H_.items():
    b.append(f'<circle cx="{x}" cy="{y}" r="16" fill="{YELLOW}" fill-opacity="0.16"/><circle cx="{x}" cy="{y}" r="6.5" fill="{CREAM}" fill-opacity="0.85"/>')
# currency glyphs (very faint)
for (sym, x, y, sz) in (("$", 300, 330, 150), ("€", 2300, 300, 130), ("¥", 2410, 760, 110), ("£", 170, 820, 120)):
    b.append(f'<text x="{x}" y="{y}" font-family="Montserrat" font-weight="900" font-size="{sz}" fill="{CREAM}" fill-opacity="0.07" text-anchor="middle">{sym}</text>')
# darken behind text for readability
b.append(f'<ellipse cx="1580" cy="705" rx="760" ry="330" fill="url(#textglow)"/>')
b.append(f'<rect width="{W}" height="{H}" filter="url(#grain)"/>')
# decorative edges (outside safe area: TV/desktop only)
b.append(mini_chart(2110, 250, 330, 170))
b.append(cargo_ship(2085, 1180, 1.25))
b.append(f'<path d="M1980,1205 L2560,1205" stroke="{CREAM}" stroke-opacity="0.12" stroke-width="3"/>')
b.append(pumpjack(250, 1205, 1.15))
b.append(f'<path d="M40,1205 L560,1205" stroke="{CREAM}" stroke-opacity="0.12" stroke-width="3"/>')
# Marlow + globe lockup (face inside safe area)
b.append(globe(740, 800, 340))
b.append(f'<ellipse cx="745" cy="1172" rx="150" ry="22" fill="#000" opacity="0.35" filter="url(#soft)"/>')
b.append(gen.place(gen.figure(M, pose="presenting"), 745, 1170, 2.05))
# Wordmark (inside safe area)
tx = 1100
b.append(f'<text x="{tx}" y="668" font-family="Montserrat" font-weight="900" font-size="104" letter-spacing="1" fill="{CREAM}">GEOECONOMICS</text>')
b.append(f'<rect x="{tx+4}" y="560" width="84" height="7" rx="3.5" fill="{RED}"/>')
b.append(f'<text x="{tx+4}" y="757" font-family="Montserrat" font-weight="800" font-size="76" letter-spacing="58.6" fill="{YELLOW}">EXPLAINED</text>')
b.append(f'<text x="{tx+6}" y="826" font-family="Inter" font-weight="500" font-size="29" fill="{CREAM}" fill-opacity="0.86">Understanding the Money, Resources &amp; Power Shaping Our World</text>')
b.append("</svg>")
banner = "".join(b)

# Safe-area guide version (for checking only)
guide = banner.replace("</svg>", f'<rect x="{SAFE[0]}" y="{SAFE[1]}" width="{SAFE[2]}" height="{SAFE[3]}" fill="none" stroke="#FF00AA" stroke-width="4" stroke-dasharray="20 10"/>'
                                    f'<rect x="0" y="{(H-423)//2}" width="{W}" height="423" fill="none" stroke="#00E5FF" stroke-width="3" stroke-dasharray="10 10"/>'
                                    f'<rect x="{(W-2276)//2}" y="{(H-423)//2}" width="2276" height="423" fill="none" stroke="#FFE600" stroke-width="3" stroke-dasharray="6 8"/></svg>')

# ---------------------------------------------------------------- PROFILE 1024x1024
p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">{FONTS}',
     f'<defs><radialGradient id="pbg" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#16304F"/><stop offset="1" stop-color="{NAVY_D}"/></radialGradient></defs>',
     f'<rect width="1024" height="1024" fill="url(#pbg)"/>',
     globe(512, 470, 380, land_op=0.9),
     # one subtle trade arc across the globe
     f'<path d="M232,560 Q512,330 800,520" fill="none" stroke="{CREAM}" stroke-opacity="0.35" stroke-width="7" stroke-dasharray="4 20" stroke-linecap="round"/>',
     f'<circle cx="232" cy="560" r="11" fill="{CREAM}" fill-opacity="0.7"/><circle cx="800" cy="520" r="11" fill="{CREAM}" fill-opacity="0.7"/>',
     gen.place(gen.figure(M, "front", "confident"), 512, 460 + 238 * 4.15, 4.15),
     "</svg>"]
profile_navy = "".join(p)

# Main profile picture: clean white background, close head-and-shoulders crop (hair swoop kept inside the circle).
PS = 5.0
profile = "".join([
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">',
    f'<rect width="1024" height="1024" fill="{WHITE}"/>',
    gen.place(gen.figure(M, "front", "confident"), 512, 565 + 238 * PS, PS),
    "</svg>"])

out = os.path.join(HERE, "src"); os.makedirs(out, exist_ok=True)
for name, svg in (("banner-2560x1440", banner), ("banner-safe-area-guide", guide), ("profile-1024x1024", profile), ("profile-1024x1024-navy", profile_navy)):
    open(os.path.join(out, name + ".svg"), "w").write(svg)
print("built")
