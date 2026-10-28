"""Symbol concepts + app-icon colourways, all derived from the master symbol geometry (ncl-symbol-orange.svg).
The concepts are proposals to move the mark away from other radiating 'spark' logos; none replaces the master artwork.
Outputs: brand/concepts/*.svg, brand/logos/vector/ncl-app-icon-*.svg, brand/logos/png/ncl-app-icon-*.png"""
import re, sys, pathlib, subprocess, tempfile
sys.path.insert(0, 'build')
import chrome

ROOT = pathlib.Path(__file__).resolve().parent.parent
SYM = (ROOT / 'brand/logos/vector/ncl-symbol-orange.svg').read_text()
vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', SYM).group(1).split()]
CX, CY = vb[0] + vb[2] / 2, vb[1] + vb[3] / 2
PATHS = re.findall(r' d="([^"]+)"', SYM)
# the four paths are corner pieces, each holding one vertical and one horizontal petal
TL, BR, TR, BL = PATHS
ORANGE, NAVY, WHITE, OFF, SLATE = '#F36B24', '#0F1E2A', '#FFFFFF', '#F5F5F4', '#303E4A'
R = 60  # reach well past the symbol for clip triangles

def petals(paths=PATHS, fill=ORANGE, clip=None, mask=None):
    c = f' clip-path="url(#{clip})"' if clip else (f' mask="url(#{mask})"' if mask else '')
    return f'<g fill="{fill}"{c} transform="translate({-CX:.3f} {-CY:.3f})">' + ''.join(f'<path d="{d}"/>' for d in paths) + '</g>'

def tri(a, b):  # triangle from the centre to two far points (symbol-centred coords, shifted back)
    pts = [(0, 0), a, b]
    return '<polygon points="' + ' '.join(f'{x + CX:.2f},{y + CY:.2f}' for x, y in pts) + '"/>'

# octants: V* = vertical petal regions, H* = horizontal petal regions
OCT = {'V_tl': tri((0, -R), (-R, -R)), 'V_tr': tri((0, -R), (R, -R)), 'V_bl': tri((0, R), (-R, R)), 'V_br': tri((0, R), (R, R)),
       'H_tl': tri((-R, 0), (-R, -R)), 'H_bl': tri((-R, 0), (-R, R)), 'H_tr': tri((R, 0), (R, -R)), 'H_br': tri((R, 0), (R, R))}
def clipdef(cid, keys):
    return f'<clipPath id="{cid}">' + ''.join(OCT[k] for k in keys) + '</clipPath>'

def maskdef(mid, keys, hole=12.5):
    """Octants minus a central disc: single petals with a clean arc at the base instead of half a curl."""
    polys = ''.join(OCT[k].replace('<polygon', '<polygon fill="#fff"') for k in keys)
    return f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="{CX-R:.2f}" y="{CY-R:.2f}" width="{2*R}" height="{2*R}">{polys}<circle cx="{CX:.3f}" cy="{CY:.3f}" r="{hole}" fill="#000"/></mask>'

def svg(inner, defs='', box=(-42, -42, 84, 84)):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{box[0]} {box[1]} {box[2]} {box[3]}">'
            f'{"<defs>" + defs + "</defs>" if defs else ""}{inner}</svg>')

VERT = ['V_tl', 'V_tr', 'V_bl', 'V_br']; HORZ = ['H_tl', 'H_bl', 'H_tr', 'H_br']
PIN = ['V_tl', 'H_tr', 'V_br', 'H_bl']

# each concept: fn(fg, accent) -> svg markup. fg = main colour, accent = second colour on that background
CONCEPTS = {
    'a-master': ('Master (current)', 'Eight petals in four mirrored pairs. Reference only.',
                 lambda fg, ac: svg(petals(fill=fg))),
    'b-lamp': ('Lamp core', 'A solid dot fills the empty centre: a light source the petals radiate from. Smallest possible change.',
               lambda fg, ac: svg(petals(fill=fg) + f'<circle r="6.2" fill="{ac}"/>')),
    'c-two-tone': ('Two-tone', 'Vertical petals in orange, horizontal petals in navy. Ties the symbol to the wordmark colour; no single-colour spark reads like this.',
                   lambda fg, ac: svg(petals(fill=fg, clip='v') + petals(fill=ac, clip='h'), clipdef('v', VERT) + clipdef('h', HORZ))),
    'd-pinwheel': ('Pinwheel', 'One petal from each pair, in rotation. Four blades read as motion and a turbine, not a spark.',
                   lambda fg, ac: svg(petals(fill=fg, mask='p'), maskdef('p', PIN))),
    'e-beams': ('Beams', 'Only the vertical petals: light thrown up and down like a wall washer. Strong silhouette at favicon size.',
                lambda fg, ac: svg(petals(fill=fg, mask='v'), maskdef('v', VERT))),
    'f-rising': ('Rising light', 'Top half of the symbol over a horizon bar: light rising over the city. Closest to “Lighting the Way”.',
                 lambda fg, ac: svg(petals([TL, TR], fill=fg) + f'<rect x="-38" y="6" width="76" height="6.4" rx="3.2" fill="{ac}"/>',
                                    box=(-42, -46, 84, 62))),
    'g-lens': ('Lens', 'The master symbol held inside a thin ring, like a luminaire seen from below. Encloses the mark so it stops reading as a loose spark.',
               lambda fg, ac: svg(petals(fill=fg) + f'<circle r="47" fill="none" stroke="{ac}" stroke-width="3.4"/>', box=(-50, -50, 100, 100))),
}

# colour-only routes: master geometry, no shape change. (vertical petals, horizontal petals, background)
COLOURWAYS = {  # name, vertical, horizontal, artwork background, icon tile
    'orange-navy':    ('Orange + navy', ORANGE, NAVY, WHITE, OFF),
    'navy-orange':    ('Navy + orange', NAVY, ORANGE, WHITE, OFF),
    'orange-slate':   ('Orange + slate', ORANGE, SLATE, WHITE, OFF),
    'orange-white':   ('Orange + white on navy', ORANGE, WHITE, NAVY, NAVY),
    'all-navy':       ('Navy only', NAVY, NAVY, WHITE, ORANGE),
    'orange-on-navy': ('Orange on navy', ORANGE, ORANGE, NAVY, NAVY),
}
def colourway(v, h):
    return svg(petals(fill=v, clip='v') + petals(fill=h, clip='h'), clipdef('v', VERT) + clipdef('h', HORZ))


# ---- geometric direction (from reference boards): petals cut from a closed shape by straight gaps.
# Gaps on the axes run to the centre (between pairs); gaps on the diagonals stop in a round U (inside a pair),
# which keeps NCL's structure of eight petals joined in four pairs.
def geo(n=8, outer=('circle', 40), r_in=13, gap=(1.6, 0.06), u=22, split=None, rot=0, fill=ORANGE, mid=None):
    """gap = (half-width at the centre, growth per unit radius) of the cut inside a pair; cuts widen outward so petals read as rays.
    split = the same for the cuts between pairs (defaults to gap); wider splits make the four pairs read clearly."""
    mid = mid or 'g' + re.sub(r'\W', '', f'{n}{outer}{r_in}{gap}{u}{split}')
    kind, size = outer
    split = split or gap
    shape = lambda f: (f'<circle r="{size}" fill="{f}"/>' if kind == 'circle' else
                       f'<rect x="{-size}" y="{-size}" width="{2*size}" height="{2*size}" rx="{size*0.24:.2f}" fill="{f}"/>')
    def wedge(r0, g):
        w = lambda r: g[0] + g[1] * r
        return f'<polygon points="{r0},{-w(r0):.3f} 80,{-w(80):.3f} 80,{w(80):.3f} {r0},{w(r0):.3f}" fill="#000"/>'
    cuts = f'<circle r="{r_in}" fill="#000"/>'
    for k in range(n):
        a = rot + k * 360 / n
        # between pairs the cut runs to the centre; inside a pair it stops in a round U at radius u
        cuts += f'<g transform="rotate({a:.3f})">' + (wedge(0, split) if k % 2 == 0 else wedge(u, gap) + f'<circle cx="{u}" r="{gap[0] + gap[1] * u:.3f}" fill="#000"/>') + '</g>'
    m = f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-60" y="-60" width="120" height="120">{shape("#fff")}{cuts}</mask>'
    return svg(f'<g mask="url(#{mid})">{shape(fill)}</g>', m)

GEO = {
    'h-aperture': ('Aperture', 'Eight petals cut from a disc, joined in four U-shaped pairs around a round opening. Reads as a lens or a downlight seen from below.',
                   lambda fg, ac: geo(8, ('circle', 40), r_in=11, gap=(0.9, 0.08), u=19, split=(1.8, 0.15), fill=fg)),
    'i-window':   ('Window', 'The same cut from a rounded square: a lit window, a city block. Squares sit well next to the wordmark and on an app tile.',
                   lambda fg, ac: geo(8, ('square', 36), r_in=10.5, gap=(0.9, 0.075), u=18, split=(1.8, 0.14), fill=fg)),
    'j-disc':     ('Solid disc', 'Heavier: narrow cuts and a small opening, so the mark reads as one solid badge. Strongest at 16 px; prints well as a stamp.',
                   lambda fg, ac: geo(8, ('circle', 40), r_in=7, gap=(0.9, 0.05), u=14, fill=fg)),
    'k-sunburst': ('Sunburst', 'Twelve petals in six pairs. More radiance, closer to a light source; still a closed circle, not a loose spark.',
                   lambda fg, ac: geo(12, ('circle', 40), r_in=15, gap=(0.7, 0.06), u=22, split=(1.3, 0.12), fill=fg)),
}
CONCEPTS.update(GEO)

def icon(sym_markup, bg, rounded=True, size=1024):
    """Rounded-square icon with the symbol at ~56% of the tile, as an SVG."""
    inner = re.search(r'<svg[^>]*viewBox="([^"]+)"[^>]*>(.*)</svg>', sym_markup, re.S)
    x, y, w, h = [float(v) for v in inner.group(1).split()]
    s = size * 0.56 / max(w, h)
    rx = size * 0.225 if rounded else size / 2
    edge = f' stroke="#D9DDE0" stroke-width="{size * 0.012:.1f}"' if bg in (WHITE, OFF) else ''  # light tiles need an edge
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">'
            f'<rect width="{size}" height="{size}" rx="{rx:.1f}" fill="{bg}"{edge}/>'
            f'<g transform="translate({size/2:.1f} {size/2:.1f}) scale({s:.4f}) translate({-(x + w/2):.3f} {-(y + h/2):.3f})">'
            f'{inner.group(2)}</g></svg>')

def to_png(svg_text, out, px=1024):
    with tempfile.TemporaryDirectory() as td:
        html = pathlib.Path(td) / 'i.html'
        html.write_text(f'<!doctype html><html><body style="margin:0;background:transparent">'
                        f'<div style="width:{px}px;height:{px}px">{svg_text.replace("<svg ", f"<svg width={px} height={px} ", 1)}</div></body></html>')
        subprocess.run([str(chrome.CHROME), *chrome.BASE, f'--window-size={px},{px}', '--default-background-color=00000000',
                        f'--screenshot={out}', html.resolve().as_uri()], check=True, capture_output=True)

if __name__ == '__main__':
    C = ROOT / 'brand/concepts'; C.mkdir(exist_ok=True)
    for key, (name, _, fn) in CONCEPTS.items():
        (C / f'ncl-symbol-{key}-on-light.svg').write_text(fn(ORANGE, NAVY))
        (C / f'ncl-symbol-{key}-on-dark.svg').write_text(fn(ORANGE, WHITE if key != 'c-two-tone' else OFF))
        (C / f'ncl-icon-{key}-navy.svg').write_text(icon(fn(ORANGE, WHITE if key != 'c-two-tone' else OFF), NAVY))
    for k, (_, v, h, _, tile) in COLOURWAYS.items():
        (C / f'ncl-colour-{k}.svg').write_text(colourway(v, h))
        (C / f'ncl-colour-{k}-icon.svg').write_text(icon(colourway(v, h), tile))
    # app-icon colourways of the master symbol (navy is the new primary)
    master = CONCEPTS['a-master'][2]
    ways = {'navy': (ORANGE, NAVY), 'slate': (ORANGE, SLATE), 'white': (ORANGE, WHITE), 'orange-navy-symbol': (NAVY, ORANGE)}
    for k, (fg, bg) in ways.items():
        s = icon(master(fg, fg), bg)
        (ROOT / f'brand/logos/vector/ncl-app-icon-{k}.svg').write_text(s)
        to_png(s, ROOT / f'brand/logos/png/ncl-app-icon-{k}.png')
    print('concepts:', len(CONCEPTS), 'icons:', len(ways))
