"""Generates the channel's character design sheets as SVG + HTML.

Every character is built from the same parametric skeleton so proportions,
outline weight and shading stay identical across views, expressions and poses.
Run:  python3 gen.py   (writes ./sheets/*.svg and ./character-bible.html)
"""
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(OUT, "sheets"), exist_ok=True)

# ---------------------------------------------------------------- palette
INK = "#1E1F22"          # outline + limbs (never pure black)
STROKE = 2.8             # outline width at 300-unit figure height
LIMB = 4.2               # stick-limb width
PAL = {
    "charcoal": "#2B2E33", "slate": "#5B6573", "offwhite": "#F2EDE4", "sand": "#D8C7A8",
    "brick": "#B5473A", "teal": "#3E8E85", "amber": "#E0A43A",
}

# ---------------------------------------------------------------- skeleton (figure units, ground y=0, up = negative)
HEAD_C = (0, -238); HEAD_R = 48
TORSO = (-42, -205, 84, 130, 38)  # x, y, w, h, rx  -> spans y -205..-75
HIP_Y = -75
SHOULDER = {"L": (-36, -172), "R": (36, -172)}

_uid = [0]
def uid(p="c"):
    _uid[0] += 1
    return f"{p}{_uid[0]}"

# ---------------------------------------------------------------- characters
CAST = {
    "marlow": dict(name="Marlow", skin="#EBC9A4", skin_sh="#D3AC84", hair="#4A3426", hair_style="marlow",
                   outfit="coat", main="#2F3B52", main_sh="#243046", inner="#ECE7DD", pants="#2B2B2E",
                   accent="#E0A43A", accent_sh="#C08926", detail="#B5473A"),
    "rosa": dict(name="Rosa", skin="#B98058", skin_sh="#9E6844", hair="#2A1E1A", hair_style="bun",
                 outfit="hoodie", main="#3E8E85", main_sh="#33756D", inner="#2E6A63", pants="#3A3F4A",
                 accent="#F2EDE4", accent_sh="#D9D2C6", detail="#F2EDE4"),
    "vera": dict(name="Dr. Vera Lind", skin="#F1D4BD", skin_sh="#DDB89C", hair="#B9B6B1", hair_style="bob",
                 outfit="cardigan", main="#8A8F98", main_sh="#757A83", inner="#F4F1EA", pants="#3D3F45",
                 accent="#3E8E85", accent_sh="#33756D", detail="#F2EDE4", glasses=True),
    "minister": dict(name="The Minister", skin="#E3BE9A", skin_sh="#C9A07A", hair="#55575C", hair_style="sidepart",
                     outfit="suit", main="#3A3D44", main_sh="#2E3036", inner="#F4F1EA", pants="#2E3036",
                     accent="#B5473A", accent_sh="#963A2F", detail="#3E8E85"),
    "ledger": dict(name="Mr. Ledger", skin="#F0CDAE", skin_sh="#D9AF8C", hair=None, hair_style="bald",
                   outfit="suit", main="#25262B", main_sh="#1B1C20", inner="#F4F1EA", pants="#1B1C20",
                   accent="#C9A24A", accent_sh="#A9853A", detail="#C9A24A", mustache=True),
    "worker": dict(name="Dev (The Worker)", skin="#C99470", skin_sh="#AE7A57", hair="#2E241F", hair_style="hardhat",
                   outfit="vest", main="#E07B39", main_sh="#C4672C", inner="#5F7183", pants="#3B4048",
                   accent="#E0A43A", accent_sh="#C08926", detail="#D9DCE0"),
    "commons": dict(name="The Commons", skin="#AEB6C0", skin_sh="#98A1AC", hair=None, hair_style="none",
                    outfit="plain", main="#7D8794", main_sh="#6B7581", inner="#7D8794", pants="#5B6573",
                    accent="#7D8794", accent_sh="#6B7581", detail="#7D8794", faceless=True),
}

# ---------------------------------------------------------------- expressions
# brows: ((angle, dy) left, (angle, dy) right); +angle = inner end lower (cross); -angle = inner end raised (worry)
EXPR = {
    "neutral":      dict(brows=((0, 0), (0, 0)), eyes="oval", mouth="line"),
    "happy":        dict(brows=((-6, -3), (-6, -3)), eyes="happy", mouth="smile"),
    "sad":          dict(brows=((-22, 0), (-22, 0)), eyes="down", mouth="frown"),
    "angry":        dict(brows=((26, 4), (26, 4)), eyes="oval", mouth="grit"),
    "surprised":    dict(brows=((-6, -9), (-6, -9)), eyes="big", mouth="o"),
    "shocked":      dict(brows=((-10, -12), (-10, -12)), eyes="wide", mouth="gasp", extra="shock"),
    "confused":     dict(brows=((-16, -7), (14, 2)), eyes="oval", mouth="wavy", extra="question"),
    "worried":      dict(brows=((-22, -3), (-22, -3)), eyes="oval", mouth="wavy", extra="sweat"),
    "fearful":      dict(brows=((-28, -8), (-28, -8)), eyes="wide", mouth="grimace", extra="sweat"),
    "excited":      dict(brows=((-8, -9), (-8, -9)), eyes="big", mouth="grin", extra="sparkle"),
    "serious":      dict(brows=((12, 2), (12, 2)), eyes="oval", mouth="line"),
    "thinking":     dict(brows=((6, 1), (-12, -6)), eyes="up", mouth="side", extra="dots"),
    "determined":   dict(brows=((20, 3), (20, 3)), eyes="squint", mouth="firm"),
    "suspicious":   dict(brows=((16, 3), (-4, -3)), eyes="sidelook", mouth="smirk"),
    "disappointed": dict(brows=((-12, 3), (-12, 3)), eyes="half", mouth="frown"),
}

# ---------------------------------------------------------------- primitives
def path(d, fill="none", stroke=INK, sw=STROKE, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'

def circle(cx, cy, r, fill, stroke=INK, sw=STROKE, extra=""):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def ellipse(cx, cy, rx, ry, fill, stroke="none", sw=0, extra=""):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def shaded(shape_fn, base, shade, dx, dy):
    """Flat two-tone cel shading: shade colour, lighter copy offset, clipped to the shape, outline on top."""
    cid = uid("clip")
    return (f'<clipPath id="{cid}">{shape_fn("none", "none", 0)}</clipPath>'
            f'{shape_fn(shade, "none", 0)}'
            f'<g clip-path="url(#{cid})"><g transform="translate({dx},{dy})">{shape_fn(base, "none", 0)}</g></g>'
            f'{shape_fn("none", INK, STROKE)}')

def limb(points, sw=LIMB):
    """Stick limb. 2 points = slight curve; 3+ points = jointed polyline."""
    if len(points) == 2:
        (x1, y1), (x2, y2) = points
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        nx, ny = -(y2 - y1), (x2 - x1)
        L = math.hypot(nx, ny) or 1
        bend = 0.12 * math.hypot(x2 - x1, y2 - y1)
        cx, cy = mx + nx / L * bend * (1 if x2 < x1 else -1), my + ny / L * bend * (1 if x2 < x1 else -1)
        d = f"M{x1},{y1} Q{cx:.1f},{cy:.1f} {x2},{y2}"
    else:
        d = "M" + " L".join(f"{x},{y}" for x, y in points)
    return path(d, sw=sw)

# ---------------------------------------------------------------- head
def face_layout(view):
    # returns (eye xs, eye y, brow y, mouth x, mouth y, scale)
    if view == "front":
        return [-15, 15], -237, -254, 0, -215, 1.0
    if view == "3q":
        return [2, 26], -237, -254, 15, -215, 0.92
    if view == "side":
        return [30], -239, -257, 37, -217, 0.85
    return [], 0, 0, 0, 0, 1

def eyes_svg(kind, xs, y, s):
    out = []
    for i, x in enumerate(xs):
        if kind == "oval":
            out.append(ellipse(x, y, 4.3 * s, 6.6, INK))
        elif kind == "big":
            out.append(ellipse(x, y - 1, 5.2 * s, 8.2, INK))
        elif kind == "wide":
            out.append(ellipse(x, y - 1, 8.5 * s, 9.5, "#FFFFFF", INK, 2.2))
            out.append(circle(x, y - 1, 2.8, INK, "none", 0))
        elif kind == "happy":
            out.append(path(f"M{x-5*s},{y+2} Q{x},{y-7} {x+5*s},{y+2}", sw=3.2))
        elif kind == "down":
            out.append(ellipse(x, y + 2, 4.0 * s, 5.4, INK))
        elif kind == "squint":
            out.append(ellipse(x, y + 1, 4.6 * s, 3.4, INK))
        elif kind == "up":
            out.append(ellipse(x + 1.5, y - 2, 4.3 * s, 6.6, INK))
        elif kind == "sidelook":
            out.append(ellipse(x + 3, y + 1, 4.3 * s, 4.6, INK))
        elif kind == "half":
            cid = uid("eye")
            out.append(f'<clipPath id="{cid}"><rect x="{x-10}" y="{y-1.5}" width="20" height="14"/></clipPath>')
            out.append(f'<g clip-path="url(#{cid})">{ellipse(x, y, 4.3*s, 6.6, INK)}</g>')
            out.append(path(f"M{x-6*s},{y-1.5} L{x+6*s},{y-1.5}", sw=2.4))
        elif kind == "closed":
            out.append(path(f"M{x-5*s},{y} Q{x},{y+5} {x+5*s},{y}", sw=3.0))
    return "".join(out)

def brows_svg(spec, xs, y, s, thick=4.6):
    out = []
    for i, x in enumerate(xs):
        ang, dy = spec[i] if len(xs) == 2 else spec[1]
        side = -1 if (i == 0 and len(xs) == 2) else 1  # left brow: inner end is +x
        half = 7.5 * s
        a = math.radians(ang)
        # inner end moves down for +ang
        x1, y1 = x - half, y + dy
        x2, y2 = x + half, y + dy
        if side == -1:
            y2 += math.sin(a) * half; y1 -= math.sin(a) * half
        else:
            y1 += math.sin(a) * half; y2 -= math.sin(a) * half
        out.append(path(f"M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}", sw=thick))
    return "".join(out)

def mouth_svg(kind, x, y, s):
    w = 8 * s
    if kind == "line":   return path(f"M{x-w},{y} L{x+w},{y}", sw=2.8)
    if kind == "smile":  return path(f"M{x-w-1},{y-3} Q{x},{y+7} {x+w+1},{y-3}", sw=2.8)
    if kind == "frown":  return path(f"M{x-w},{y+3} Q{x},{y-5} {x+w},{y+3}", sw=2.8)
    if kind == "o":      return ellipse(x, y + 1, 4.2, 5.4, "#4A2A27", INK, 2.2)
    if kind == "gasp":   return ellipse(x, y + 2, 6.4, 9.0, "#4A2A27", INK, 2.4)
    if kind == "grin":
        return (path(f"M{x-w-3},{y-3} Q{x},{y-1} {x+w+3},{y-3} Q{x},{y+14} {x-w-3},{y-3} Z", fill="#4A2A27", sw=2.4)
                + path(f"M{x-5},{y+6} Q{x},{y+3} {x+5},{y+6}", fill="#C9645A", stroke="none", sw=0))
    if kind == "grit":
        return (f'<rect x="{x-w-2}" y="{y-4}" width="{2*w+4}" height="9" rx="3" fill="#FFFFFF" stroke="{INK}" stroke-width="2.4"/>'
                + path(f"M{x-w-1},{y+0.5} L{x+w+1},{y+0.5}", sw=1.6))
    if kind == "grimace":
        return (f'<rect x="{x-w-1}" y="{y-3}" width="{2*w+2}" height="8" rx="3" fill="#FFFFFF" stroke="{INK}" stroke-width="2.2"/>'
                + path(f"M{x-w},{y+1} L{x+w},{y+1}", sw=1.4) + path(f"M{x-3},{y-3} L{x-3},{y+5} M{x+3},{y-3} L{x+3},{y+5}", sw=1.2))
    if kind == "wavy":   return path(f"M{x-w},{y+1} q{w/4},-4 {w/2},0 t{w/2},0 t{w/2},0 t{w/2},0", sw=2.6)
    if kind == "side":   return path(f"M{x+1},{y} L{x+w+2},{y-2}", sw=2.8)
    if kind == "smirk":  return path(f"M{x-w},{y+1} Q{x+2},{y+3} {x+w+1},{y-4}", sw=2.8)
    if kind == "firm":   return path(f"M{x-w},{y+1} Q{x},{y-2} {x+w},{y+1}", sw=3.4)
    return ""

def extra_svg(kind, view):
    hx, hy = HEAD_C
    if kind == "sweat":
        return path(f"M{hx+44},{hy-26} q-6,10 0,14 q6,-4 0,-14 Z", fill="#9FC9E6", sw=1.8)
    if kind == "shock":
        return "".join(path(f"M{hx+a},{hy-62} L{hx+b},{hy-76}", sw=3) for a, b in ((-24, -32), (0, 0), (24, 32)))
    if kind == "question":
        return f'<text x="{hx+46}" y="{hy-40}" font-family="Arial Black,Arial" font-weight="900" font-size="30" fill="{PAL["amber"]}" stroke="{INK}" stroke-width="1.6">?</text>'
    if kind == "sparkle":
        def star(x, y, r):
            return path(f"M{x},{y-r} L{x+r*0.3},{y-r*0.3} L{x+r},{y} L{x+r*0.3},{y+r*0.3} L{x},{y+r} L{x-r*0.3},{y+r*0.3} L{x-r},{y} L{x-r*0.3},{y-r*0.3} Z", fill=PAL["amber"], sw=1.6)
        return star(hx + 56, hy - 42, 10) + star(hx - 58, hy - 30, 7)
    if kind == "dots":
        return "".join(circle(hx + 50 + i * 10, hy - 52 - i * 9, 3 + i * 1.3, "#FFFFFF", INK, 1.8) for i in range(3))
    return ""

def hair_svg(c, view):
    st, col = c["hair_style"], c["hair"]
    hx, hy = HEAD_C
    if st == "marlow":
        sh = {"front": 0, "3q": 9, "side": 0, "back": 0}[view]
        if view in ("front", "3q"):
            cap = (f"M{-47+sh*0.2},{hy-14} C{-50+sh*0.2},{hy-68} {50+sh*0.2},{hy-68} {47+sh*0.2},{hy-14} "
                   f"L{40+sh*0.2},{hy-24} Q{30+sh},{hy-36} {18+sh},{hy-29} Q{6+sh},{hy-39} {-6+sh},{hy-31} "
                   f"Q{-20+sh},{hy-39} {-31+sh},{hy-28} Q{-41+sh*0.5},{hy-26} {-47+sh*0.2},{hy-14} Z")
            tuft = f"M{-8+sh},{hy-46} C{-6+sh},{hy-76} {20+sh},{hy-86} {33+sh},{hy-68} C{24+sh},{hy-74} {10+sh},{hy-68} {13+sh},{hy-49} Z"
            return path(tuft, fill=col) + path(cap, fill=col)
        if view == "side":
            cap = (f"M{30},{hy-30} Q{22},{hy-22} {12},{hy-26} Q{2},{hy-18} {-8},{hy-20} Q{-24},{hy-6} {-30},{hy+18} "
                   f"Q{-44},{hy+12} {-48},{hy-6} C{-50},{hy-62} {28},{hy-74} {44},{hy-24} Z")
            tuft = f"M{2},{hy-48} C{8},{hy-78} {34},{hy-84} {44},{hy-62} C{34},{hy-68} {22},{hy-62} {22},{hy-46} Z"
            return path(tuft, fill=col) + path(cap, fill=col)
        cap = (f"M{-47},{hy+4} C{-52},{hy-68} {52},{hy-68} {47},{hy+4} Q{36},{hy+20} {22},{hy+10} "
               f"Q{8},{hy+22} {-6},{hy+12} Q{-22},{hy+22} {-34},{hy+12} Q{-44},{hy+14} {-47},{hy+4} Z")
        tuft = f"M{-8},{hy-46} C{-6},{hy-76} {20},{hy-86} {33},{hy-68} C{24},{hy-74} {10},{hy-68} {13},{hy-49} Z"
        return path(tuft, fill=col) + path(cap, fill=col)
    if st == "bun":
        bun = circle(hx + 2, hy - 58, 17, col)
        if view == "back":
            cap = f"M{-47},{hy+2} C{-52},{hy-66} {52},{hy-66} {47},{hy+2} Q{0},{hy+12} {-47},{hy+2} Z"
        else:
            cap = (f"M{-47},{hy-4} C{-50},{hy-66} {50},{hy-66} {47},{hy-4} L{44},{hy-10} "
                   f"Q{20},{hy-36} {-4},{hy-26} Q{-28},{hy-34} {-44},{hy-10} Z")
        return bun + path(cap, fill=col)
    if st == "bob":
        if view == "back":
            cap = f"M{-52},{hy+30} C{-58},{hy-70} {58},{hy-70} {52},{hy+30} Q{0},{hy+40} {-52},{hy+30} Z"
            return path(cap, fill=col)
        cap = (f"M{-52},{hy+30} C{-60},{hy-70} {60},{hy-70} {52},{hy+30} L{40},{hy+30} L{40},{hy-14} "
               f"L{-40},{hy-14} L{-40},{hy+30} Z")
        return path(cap, fill=col)
    if st == "sidepart":
        if view == "back":
            return path(f"M{-47},{hy+2} C{-52},{hy-68} {52},{hy-68} {47},{hy+2} Q{0},{hy+10} {-47},{hy+2} Z", fill=col)
        cap = (f"M{-47},{hy-6} C{-50},{hy-68} {50},{hy-68} {47},{hy-6} L{44},{hy-12} "
               f"Q{30},{hy-40} {-12},{hy-34} Q{-34},{hy-30} {-45},{hy-12} Z")
        return path(cap, fill=col) + path(f"M{-14},{hy-34} Q{-10},{hy-46} {-2},{hy-54}", sw=1.8)
    if st == "bald":
        return path(f"M{-22},{hy-34} Q{-12},{hy-44} {2},{hy-44}", stroke="#FFFFFF", sw=4, extra='opacity="0.8"')
    if st == "hardhat":
        hat = (f"M{-44},{hy-14} C{-46},{hy-74} {46},{hy-74} {44},{hy-14} Z")
        brim = f'<rect x="{-56}" y="{hy-18}" width="112" height="10" rx="5" fill="{PAL["amber"]}" stroke="{INK}" stroke-width="{STROKE}"/>'
        ridge = path(f"M0,{hy-60} L0,{hy-18}", sw=2)
        return path(hat, fill=PAL["amber"]) + ridge + brim
    return ""

def head_svg(c, view, expr_name):
    hx, hy = HEAD_C
    e = EXPR[expr_name]
    out = [shaded(lambda f, s, w: circle(hx, hy, HEAD_R, f, s, w), c["skin"], c["skin_sh"], -5, -9)]
    if view == "side":  # simple ear on the side view
        out.append(ellipse(-4, hy + 2, 7, 9, c["skin_sh"], INK, 2.2))
    if c.get("hair_style") not in ("hardhat",):
        out.append(hair_svg(c, view))
    if view != "back" and not c.get("faceless"):
        xs, ey, by, mx, my, s = face_layout(view)
        out.append(eyes_svg(e["eyes"], xs, ey, s))
        if c.get("glasses") and view != "side":
            out.append("".join(circle(x, ey, 11.5 * s, "none", INK, 2.2) for x in xs))
            out.append(path(f"M{xs[0]+11.5*s},{ey} L{xs[1]-11.5*s},{ey}", sw=2.2))
        elif c.get("glasses"):
            out.append(circle(xs[0], ey, 10, "none", INK, 2.2) + path(f"M{xs[0]-10},{ey} L-20,{ey-4}", sw=2))
        out.append(brows_svg(e["brows"], xs, by, s, thick=4.6 if c["name"] == "Marlow" else 3.4))
        if c.get("mustache"):
            out.append(path(f"M{mx-14},{my-1} Q{mx-7},{my-9} {mx},{my-4} Q{mx+7},{my-9} {mx+14},{my-1} Q{mx+6},{my-4} {mx},{my-1} Q{mx-6},{my-4} {mx-14},{my-1} Z", fill="#6B6460", sw=2))
        out.append(mouth_svg(e["mouth"], mx, my + (3 if c.get("mustache") else 0), s))
        if e.get("extra"):
            out.append(extra_svg(e["extra"], view))
    if c.get("hair_style") == "hardhat":
        out.append(hair_svg(c, view))
    return "".join(out)

# ---------------------------------------------------------------- torso + outfit
def torso_shape(view):
    x, y, w, h, rx = TORSO
    if view == "side":
        x, w = -29, 58
    elif view == "3q":
        x, w = -39, 78
    def f(fill, stroke, sw):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    return f, (x, y, w, h)

def torso_svg(c, view):
    shape, (x, y, w, h) = torso_shape(view)
    cid = uid("tc")
    o = c["outfit"]
    off = {"front": 0, "3q": 8, "side": 12, "back": 0}[view]
    det = []
    pants = f'<rect x="{x-2}" y="{-97}" width="{w+4}" height="30" fill="{c["pants"]}"/>' + path(f"M{x},{-97} L{x+w},{-97}", sw=2)
    if view != "back":
        if o == "coat":
            det.append(path(f"M{-15+off},{-200} L{off},{-150} L{15+off},{-200} Z", fill=c["inner"], sw=2.2))
            det.append(path(f"M{off},{-150} L{off},{-99}", sw=2))
            det += [circle(off + 7, yy, 2.6, INK, "none", 0) for yy in (-138, -118)]
            if view != "side":
                det.append(path(f"M{20+off},{-176} q-4,-7 0,-11 q4,4 0,11 Z", fill=c["detail"], sw=1.6))  # map-pin badge
        elif o == "hoodie":
            det.append(path(f"M{-18+off},{-120} Q{off},{-128} {18+off},{-120} L{22+off},{-100} L{-22+off},{-100} Z", fill=c["main_sh"], sw=2))
            det.append(path(f"M{-6+off},{-196} L{-8+off},{-166} M{6+off},{-196} L{8+off},{-166}", stroke=c["accent"], sw=2.4))
        elif o == "cardigan":
            det.append(path(f"M{-14+off},{-201} L{off},{-130} L{14+off},{-201} Z", fill=c["inner"], sw=2.2))
            det.append(path(f"M{off},{-130} L{off},{-99}", sw=2))
            det += [circle(off - 6, yy, 2.4, INK, "none", 0) for yy in (-122, -108)]
            det.append(path(f"M{-12+off},{-196} L{-3+off},{-150} M{12+off},{-196} L{3+off},{-150}", stroke=c["accent"], sw=2))
            det.append(f'<rect x="{-7+off}" y="-152" width="14" height="18" rx="2" fill="#FFFFFF" stroke="{INK}" stroke-width="1.8"/>')
            det.append(f'<rect x="{-4+off}" y="-148" width="8" height="3" fill="{c["accent"]}"/>')
        elif o == "suit":
            det.append(path(f"M{-16+off},{-201} L{off},{-140} L{16+off},{-201} Z", fill=c["inner"], sw=2.2))
            det.append(path(f"M{-4+off},{-196} L{4+off},{-196} L{6+off},{-150} L{off},{-142} L{-6+off},{-150} Z", fill=c["accent"], sw=1.8))
            det.append(path(f"M{off},{-140} L{off},{-99}", sw=2))
            if c["name"] == "Mr. Ledger":
                det.append(path(f"M{-26+off},{-160} L{-14+off},{-160} L{-20+off},{-168} Z", fill=c["accent"], sw=1.4))
            elif view != "side":
                det.append(f'<rect x="{17+off}" y="-178" width="9" height="6" fill="{c["detail"]}" stroke="{INK}" stroke-width="1.2"/>')
        elif o == "vest":
            det.append(f'<rect x="{x-2}" y="-200" width="{w+4}" height="105" fill="{c["main"]}"/>')
            det.append(f'<rect x="{-10+off}" y="-205" width="20" height="108" fill="{c["inner"]}"/>')
            det += [f'<rect x="{x-2}" y="{yy}" width="{w+4}" height="6" fill="{c["detail"]}"/>' for yy in (-150, -126)]
            det.append(path(f"M{-10+off},{-200} L{-10+off},{-98} M{10+off},{-200} L{10+off},{-98}", sw=2))
    else:
        det.append(path(f"M0,{-188} L0,{-99}", sw=1.8))
        if o == "vest":
            det += [f'<rect x="{x-2}" y="{yy}" width="{w+4}" height="6" fill="{c["detail"]}"/>' for yy in (-150, -126)]
    over = []
    if o == "coat":  # scarf band + tail (signature) sit on top of the outline
        over.append(f'<rect x="{x+4}" y="-208" width="{w-8}" height="16" rx="8" fill="{c["accent"]}" stroke="{INK}" stroke-width="{STROKE}"/>')
        if view != "back":
            tx = -16 + off if view != "side" else 14
            over.append(path(f"M{tx},{-198} L{tx-3},{-150} L{tx+9},{-150} L{tx+10},{-198} Z", fill=c["accent"], sw=2.4))
            over.append(path(f"M{tx-1},{-150} l0,6 M{tx+3},{-150} l0,6 M{tx+7},{-150} l0,6", sw=1.8))
            over.append(path(f"M{tx-2},{-162} L{tx+9},{-162}", stroke=c["accent_sh"], sw=2.2))
    if o == "hoodie":
        over.append(f'<rect x="{x+6}" y="-210" width="{w-12}" height="14" rx="7" fill="{c["inner"]}" stroke="{INK}" stroke-width="{STROKE}"/>')
    under = (f'<clipPath id="{cid}">{shape("none","none",0)}</clipPath>'
             f'<g clip-path="url(#{cid})">{shape(c["main_sh"],"none",0)}<g transform="translate(-8,0)">{shape(c["main"],"none",0)}</g>{pants}{"".join(det)}</g>')
    return under + shape("none", INK, STROKE) + "".join(over)

# ---------------------------------------------------------------- poses
STAND = dict(arms=[[(-33, -172), (-46, -110)], [(33, -172), (46, -110)]], legs=[[(-13, -75), (-14, 0)], [(13, -75), (14, 0)]])
POSES = {
    "standing":    dict(view="front", expr="neutral", **STAND),
    "walking":     dict(view="3q", expr="neutral", lean=4, arms=[[(-30, -172), (-12, -112)], [(30, -172), (50, -116)]],
                        legs=[[(-10, -75), (-30, 0)], [(10, -75), (24, 0)]]),
    "running":     dict(view="3q", expr="determined", lean=14, arms=[[(-30, -172), (-52, -150), (-34, -126)], [(30, -172), (52, -160), (66, -190)]],
                        legs=[[(-10, -75), (-30, -40), (-52, -22)], [(10, -75), (36, -44), (34, 0)]]),
    "sitting":     dict(view="3q", expr="neutral", seat=True, arms=[[(-30, -172), (-12, -122), (30, -84)], [(30, -172), (50, -120), (56, -80)]],
                        legs=[[(-6, -80), (74, -74), (72, 0)], [(8, -80), (86, -74), (86, 0)]]),
    "pointing":    dict(view="3q", expr="serious", arms=[[(-30, -172), (-44, -110)], [(30, -172), (118, -190)]], **{k: STAND[k] for k in ("legs",)}),
    "explaining":  dict(view="front", expr="happy", arms=[[(-33, -172), (-58, -140), (-74, -160)], [(33, -172), (58, -140), (74, -160)]], legs=STAND["legs"]),
    "thinking":    dict(view="front", expr="thinking", arms=[[(-36, -172), (-34, -128), (52, -146)], [(36, -172), (64, -146), (26, -198)]], legs=STAND["legs"]),
    "looking_back": dict(view="3q", head_flip=True, expr="suspicious", arms=[[(-30, -172), (-12, -112)], [(30, -172), (50, -116)]],
                         legs=[[(-10, -75), (-28, 0)], [(10, -75), (22, 0)]]),
    "holding":     dict(view="front", expr="neutral", prop="box", arms=[[(-33, -172), (-46, -140), (-30, -124)], [(33, -172), (46, -140), (30, -124)]], legs=STAND["legs"]),
    "reading":     dict(view="front", expr="serious", eyes_down=True, prop="paper", arms=[[(-33, -172), (-40, -130), (-24, -140)], [(33, -172), (40, -130), (24, -140)]], legs=STAND["legs"]),
    "working":     dict(view="3q", expr="determined", seat=True, prop="laptop", arms=[[(-30, -172), (-6, -130), (48, -112)], [(30, -172), (52, -134), (72, -114)]],
                        legs=[[(-6, -80), (74, -74), (72, 0)], [(8, -80), (86, -74), (86, 0)]]),
    "arguing":     dict(view="3q", expr="angry", lean=8, prop="burst", arms=[[(-30, -172), (-52, -170), (-46, -200)], [(30, -172), (100, -168)]],
                        legs=[[(-10, -75), (-26, 0)], [(10, -75), (26, 0)]]),
    "celebrating": dict(view="front", expr="excited", prop="confetti", arms=[[(-33, -172), (-58, -210), (-62, -258)], [(33, -172), (58, -210), (62, -258)]],
                        legs=[[(-13, -75), (-28, 0)], [(13, -75), (28, 0)]]),
    "falling":     dict(view="front", expr="shocked", rot=-62, prop="dust", arms=[[(-33, -172), (-70, -200), (-74, -240)], [(33, -172), (70, -210), (90, -232)]],
                        legs=[[(-13, -75), (-40, -40)], [(13, -75), (40, -30)]]),
    "reacting":    dict(view="front", expr="shocked", lean=-10, arms=[[(-33, -172), (-62, -180), (-50, -214)], [(33, -172), (62, -180), (50, -214)]],
                        legs=[[(-13, -75), (-22, 0)], [(13, -75), (18, 0)]]),
}

def prop_svg(name):
    if name == "box":
        return (f'<rect x="-34" y="-150" width="68" height="50" rx="3" fill="#C9A27A" stroke="{INK}" stroke-width="{STROKE}"/>'
                + path("M-34,-136 L34,-136", sw=1.6) + f'<rect x="-8" y="-150" width="16" height="14" fill="#E8D7BA" stroke="{INK}" stroke-width="1.6"/>')
    if name == "paper":
        return (f'<g transform="rotate(-6 0 -150)"><rect x="-26" y="-178" width="52" height="62" rx="2" fill="#FFFFFF" stroke="{INK}" stroke-width="{STROKE}"/>'
                + "".join(path(f"M-18,{-166+i*9} L{18 - (i%2)*8},{-166+i*9}", stroke="#9AA3AE", sw=2) for i in range(5)) + "</g>")
    if name == "laptop":
        return (f'<rect x="20" y="-100" width="110" height="10" fill="#7A5B43" stroke="{INK}" stroke-width="{STROKE}"/>'
                + path("M28,-90 L28,0 M122,-90 L122,0", sw=4)
                + path("M58,-102 L104,-102 L112,-146 L66,-146 Z", fill="#4A5260", sw=2.4) + path("M64,-102 L108,-102", sw=3))
    if name == "burst":
        pts = []
        for i in range(16):
            r = 26 if i % 2 == 0 else 14
            a = math.pi * 2 * i / 16
            pts.append(f"{130 + r*math.cos(a):.1f},{-250 + r*math.sin(a):.1f}")
        return path("M" + " L".join(pts) + " Z", fill=PAL["amber"], sw=2) + f'<text x="124" y="-240" font-family="Arial Black,Arial" font-size="26" font-weight="900" fill="{INK}">!</text>'
    if name == "confetti":
        cols = [PAL["amber"], PAL["teal"], PAL["brick"], "#FFFFFF"]
        return "".join(f'<rect x="{x}" y="{y}" width="8" height="12" rx="1" fill="{cols[i%4]}" stroke="{INK}" stroke-width="1.2" transform="rotate({i*37} {x} {y})"/>'
                       for i, (x, y) in enumerate([(-90, -280), (80, -290), (-70, -320), (100, -250), (-110, -230), (60, -330), (0, -340), (120, -310)]))
    if name == "dust":
        return "".join(ellipse(x, -4, r, r * 0.6, "#D8D2C6", INK, 1.6) for x, r in ((-60, 12), (60, 14), (90, 9)))
    return ""

def seat_svg():
    return (f'<rect x="-34" y="-82" width="96" height="10" rx="3" fill="#8A4B3F" stroke="{INK}" stroke-width="{STROKE}"/>'
            + path("M-28,-72 L-28,0 M58,-72 L58,0", sw=4) + path("M-34,-82 L-40,-160", stroke="#8A4B3F", sw=9) + path("M-34,-82 L-40,-160", sw=2))

def figure(c, view="front", expr="neutral", pose=None, flip=False):
    """Return SVG group (no translate) of a full character."""
    p = dict(POSES["standing"]) if pose is None else dict(POSES[pose])
    if pose is None:
        p["view"], p["expr"] = view, expr
    v = p["view"]
    arms, legs = p["arms"], p["legs"]
    if v == "side":
        arms = [[(0, -172), (6, -110)]]
        legs = [[(-4, -75), (-6, 0)], [(4, -75), (8, 0)]]
    parts = []
    parts.append(ellipse(0, 2, 44, 7, "#000000", extra='opacity="0.14"'))
    if p.get("seat"):
        parts.append(seat_svg())
    parts += [limb(l) for l in legs]
    upper = []
    if v in ("3q", "side") and len(arms) == 2:
        upper.append(limb(arms[0]))  # far arm behind body
    if v == "back":
        upper += [limb(a) for a in arms]
    upper.append(torso_svg(c, v))
    head = head_svg(c, "3q" if p.get("head_flip") else v, p.get("expr", expr))
    if p.get("eyes_down"):
        head = head.replace(f'cy="-238"', 'cy="-232"')
    if p.get("head_flip"):
        head = f'<g transform="scale(-1,1)">{head}</g>'
    upper.append(head)
    if v in ("front",):
        upper += [limb(a) for a in arms]
    elif v in ("3q",):
        upper.append(limb(arms[1]))
    elif v == "side":
        upper.append(limb(arms[0]))
    if p.get("prop") in ("box", "paper"):
        upper.insert(len(upper) - 2, prop_svg(p["prop"]))
    lean = p.get("lean", 0)
    parts.append(f'<g transform="rotate({lean} 0 -75)">{"".join(upper)}</g>')
    if p.get("prop") in ("laptop",):
        parts.insert(1, prop_svg("laptop"))
    if p.get("prop") in ("burst", "confetti", "dust"):
        parts.append(prop_svg(p["prop"]))
    g = "".join(parts)
    if p.get("rot"):
        g = f'<g transform="translate(0,-40) rotate({p["rot"]} 0 -110)">{g.replace(prop_svg("dust"), "")}</g>' + prop_svg("dust")
    if flip:
        g = f'<g transform="scale(-1,1)">{g}</g>'
    return g

# ---------------------------------------------------------------- sheet helpers
def place(svg, x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})">{svg}</g>'

def label(x, y, text, size=15, weight=700, color=INK, anchor="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,Helvetica,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{text}</text>'

def sheet(w, h, body, title, subtitle=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<rect width="{w}" height="{h}" fill="{PAL["offwhite"]}"/>'
            f'<rect x="0" y="0" width="{w}" height="64" fill="{PAL["charcoal"]}"/>'
            f'{label(28, 41, title, 24, 800, "#F2EDE4", "start")}'
            f'{label(w-28, 41, subtitle, 14, 500, "#C9C2B5", "end")}'
            f'{body}</svg>')

def save(name, svg):
    with open(os.path.join(OUT, "sheets", name + ".svg"), "w") as f:
        f.write(svg)
    return svg

M = CAST["marlow"]
sheets = {}

# 1. Turnaround + proportions
body = []
for i, (v, lab, fl) in enumerate([("front", "FRONT", False), ("3q", "THREE-QUARTER", False), ("side", "SIDE (PROFILE)", False), ("back", "BACK", False)]):
    x = 150 + i * 250
    body.append(place(figure(M, v, "neutral"), x, 440, 1.0))
    body.append(label(x, 480, lab, 14, 800))
# proportion guides
for yy, t in ((440, "0 — ground"), (365, "legs 75u (¼)"), (235, "torso 130u"), (154, "head ⌀96u (⅓)")):
    body.append(f'<line x1="40" y1="{yy}" x2="1060" y2="{yy}" stroke="{PAL["brick"]}" stroke-width="1" stroke-dasharray="5 5" opacity="0.55"/>')
    body.append(label(1068, yy + 4, t, 11, 600, PAL["brick"], "start"))
body.append(f'<line x1="40" y1="202" x2="1060" y2="202" stroke="{PAL["brick"]}" stroke-width="1" stroke-dasharray="5 5" opacity="0.55"/>')
body.append(label(1068, 206, "neck / scarf line", 11, 600, PAL["brick"], "start"))
body.append(label(600, 530, "Total height ≈ 3 heads (head 96u · torso 130u, overlaps head by 15u · legs 75u). Head width = 1.14× torso width.", 14, 500, PAL["slate"]))
sheets["01-marlow-turnaround"] = save("01-marlow-turnaround", sheet(1200, 560, "".join(body), "MARLOW — Turnaround & Proportions", "Main character · permanent reference"))

# 2. Expressions (head close-ups)
body = []
names = list(EXPR)
labels = []
for i, n in enumerate(names):
    col, row = i % 5, i // 5
    x, y = 120 + col * 240, 330 + row * 300
    body.append(place(f'<g transform="translate(0,238)">{head_svg(M, "front", n)}</g>', x, y - 100, 1.35))
    labels.append(label(x, y + 14, f"{i+1}. {n.upper()}", 15, 800))
body += labels
sheets["02-marlow-expressions"] = save("02-marlow-expressions", sheet(1200, 1000, "".join(body), "MARLOW — Expression Library (15)", "Change only brows · eyes · mouth"))

# 3. Poses
body = []
for i, n in enumerate(POSES):
    col, row = i % 5, i // 5
    x, y = 120 + col * 240, 400 + row * 380
    body.append(place(figure(M, pose=n), x, y, 0.92))
    body.append(label(x, y + 34, n.replace("_", " ").upper(), 15, 800))
sheets["03-marlow-poses"] = save("03-marlow-poses", sheet(1200, 1240, "".join(body), "MARLOW — Pose Library (15)", "Same skeleton · same proportions"))

# 4. Cast lineup
body = []
order = ["marlow", "rosa", "vera", "minister", "ledger", "worker", "commons"]
roles = ["GUIDE / NARRATOR", "EVERYDAY CITIZEN", "THE EXPERT", "THE LEADER", "THE CREDITOR", "THE WORKER", "THE COMMONS"]
for i, k in enumerate(order):
    x = 95 + i * 168
    body.append(place(figure(CAST[k], "front", "neutral"), x, 430, 0.95))
    body.append(label(x, 470, CAST[k]["name"], 15, 800))
    body.append(label(x, 490, roles[i], 11, 700, PAL["slate"]))
sheets["04-cast-lineup"] = save("04-cast-lineup", sheet(1200, 530, "".join(body), "THE CAST — One Universe", "Same skeleton, outline & shading for every character"))

# 5. Supporting cast: 3 expressions each + 3q
body = []
sup = ["rosa", "vera", "minister", "ledger", "worker", "commons"]
exs = {"rosa": ["worried", "sad", "happy"], "vera": ["serious", "thinking", "surprised"], "minister": ["happy", "suspicious", "shocked"],
       "ledger": ["suspicious", "happy", "angry"], "worker": ["determined", "disappointed", "excited"], "commons": ["neutral", "neutral", "neutral"]}
for r, k in enumerate(sup):
    y = 150 + r * 190
    body.append(label(30, y - 40, CAST[k]["name"].upper(), 17, 800, INK, "start"))
    body.append(place(figure(CAST[k], "3q", "neutral"), 110, y + 132, 0.5))
    if k == "commons":
        tints = [("#AEB6C0", "#7D8794"), ("#9AA3AE", "#6B7581"), ("#C3C9D0", "#8E98A4"), ("#AEB6C0", "#5B6573"), ("#9AA3AE", "#7D8794")]
        for j, (hd, bd) in enumerate(tints):
            cc = dict(CAST[k], skin=hd, skin_sh=hd, main=bd, main_sh=bd)
            body.append(place(figure(cc, "front", "neutral"), 290 + j * 62, y + 130, 0.42))
        hi = dict(CAST[k], skin=PAL["brick"], skin_sh="#963A2F", main=PAL["brick"], main_sh="#963A2F")
        body.append(place(figure(hi, "front", "neutral"), 290 + 5 * 62, y + 130, 0.42))
        body.append(label(470, y + 160, "crowd tints · highlight one in brick red = 'this is you / the 1 in 6'", 12, 700, PAL["slate"]))
        exs[k] = []
    for j, e in enumerate(exs[k]):
        x = 300 + j * 170
        body.append(place(f'<g transform="translate(0,238)">{head_svg(CAST[k], "front", e)}</g>', x, y + 30, 1.0))
        body.append(label(x, y + 102, e, 12, 700, PAL["slate"]))
    # swatches
    sw = [CAST[k][kk] for kk in ("skin", "hair", "main", "inner", "pants", "accent") if CAST[k].get(kk)]
    for j, colr in enumerate(sw):
        body.append(f'<rect x="{850 + j*52}" y="{y-6}" width="44" height="44" rx="6" fill="{colr}" stroke="{INK}" stroke-width="1.5"/>')
        body.append(label(872 + j * 52, y + 54, colr, 9, 600, PAL["slate"]))
sheets["05-supporting-cast"] = save("05-supporting-cast", sheet(1200, 1300, "".join(body), "SUPPORTING CAST — Views, Expressions, Colours", "Every role has a clear storytelling job"))

# 6. Palette
body = []
groups = [
    ("BRAND / SCENE PALETTE", [("Charcoal", PAL["charcoal"]), ("Slate", PAL["slate"]), ("Off-white", PAL["offwhite"]), ("Sand", PAL["sand"]),
                               ("Brick red · decline/debt", PAL["brick"]), ("Teal · growth", PAL["teal"]), ("Amber · highlight", PAL["amber"])]),
    ("MARLOW", [("Skin", M["skin"]), ("Skin shade", M["skin_sh"]), ("Hair", M["hair"]), ("Coat", M["main"]), ("Coat shade", M["main_sh"]),
                ("Shirt", M["inner"]), ("Scarf", M["accent"]), ("Scarf shade", M["accent_sh"]), ("Trousers", M["pants"]), ("Pin", M["detail"])]),
    ("LINE & UTILITY", [("Ink outline", INK), ("Mouth interior", "#4A2A27"), ("Ground shadow 14%", "#BDBAB4"), ("Sweat drop", "#9FC9E6")]),
]
y = 110
for title, cols in groups:
    body.append(label(30, y, title, 16, 800, INK, "start"))
    for j, (n, colr) in enumerate(cols):
        x = 30 + j * 114
        body.append(f'<rect x="{x}" y="{y+14}" width="100" height="70" rx="8" fill="{colr}" stroke="{INK}" stroke-width="1.5"/>')
        body.append(label(x + 50, y + 102, colr, 11, 700, INK))
        body.append(label(x + 50, y + 118, n, 10, 500, PAL["slate"]))
    y += 165
sheets["06-palette"] = save("06-palette", sheet(1200, y + 10, "".join(body), "COLOUR SYSTEM", "Muted base · one accent per meaning"))

# ---------------------------------------------------------------- HTML bible
html = ["""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Character Bible</title><style>
:root{--bg:#E9E4DA;--ink:#1E1F22;--muted:#5B6573}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#1D1F23;--ink:#ECE7DD;--muted:#A8B0BA}}
:root[data-theme="dark"]{--bg:#1D1F23;--ink:#ECE7DD;--muted:#A8B0BA}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,Helvetica,Arial,sans-serif}
main{max-width:1240px;margin:0 auto;padding:24px 16px}
h1{font-size:28px;margin:8px 0 4px} p{color:var(--muted);margin:0 0 20px}
section{margin:0 0 28px} svg{width:100%;height:auto;border-radius:12px;display:block;box-shadow:0 2px 10px rgba(0,0,0,.12)}
</style></head><body><main><h1>Character Bible</h1><p>Original cast in a minimal 2D explainer style. Every sheet is generated from one parametric skeleton, so proportions never drift.</p>"""]
for k, s in sheets.items():
    html.append(f'<section id="{k}">{s}</section>')
html.append("</main></body></html>")
with open(os.path.join(OUT, "character-bible.html"), "w") as f:
    f.write("".join(html))
print("ok", list(sheets))
