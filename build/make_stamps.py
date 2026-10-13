"""Round + rectangular company stamps. Pipeline: HTML/SVG -> Chromium PDF -> pdftocairo SVG -> flatten glyph <use> into paths."""
import sys, re, subprocess, pathlib; sys.path.insert(0, 'build')
import render, chrome
ROOT = pathlib.Path('.'); OUT = ROOT / 'deliverables/06-Stamp'; OUT.mkdir(parents=True, exist_ok=True)
TMP = ROOT / 'build/_tmp'; TMP.mkdir(exist_ok=True)
SYM = re.search(r'<svg[^>]*viewBox="([^"]+)"[^>]*>(.*)</svg>', (ROOT / 'brand/logos/vector/ncl-symbol-navy.svg').read_text(), re.S)
VB = [float(v) for v in SYM.group(1).split()]; SYM_INNER = SYM.group(2).replace('fill="#0F1E2A"', 'fill="#000"')
def symbol(cx, cy, size):
    s = size / max(VB[2], VB[3])
    return f'<g transform="translate({cx - VB[2]*s/2:.3f} {cy - VB[3]*s/2:.3f}) scale({s:.5f}) translate({-VB[0]:.3f} {-VB[1]:.3f})">{SYM_INNER}</g>'

FONTS = '''@font-face{font-family:'Montserrat';font-weight:600;src:url(../../brand/fonts/Montserrat-latin-600.woff2)}
@font-face{font-family:'Montserrat';font-weight:700;src:url(../../brand/fonts/Montserrat-latin-700.woff2)}
@font-face{font-family:'Montserrat';font-weight:500;src:url(../../brand/fonts/Montserrat-latin-500.woff2)}
@font-face{font-family:'NCL Arabic';font-weight:700;src:url(../../brand/fonts/NotoKufiArabic-arabic-700.woff2)}
@font-face{font-family:'NCL Arabic';font-weight:600;src:url(../../brand/fonts/NotoKufiArabic-arabic-600.woff2)}'''

import parts
WM = (ROOT / 'brand/logos/vector/ncl-wordmark-black.svg').read_text()
WM_DEFS = re.search(r'<defs>(.*)</defs>', WM, re.S).group(1)
WM_USE = re.search(r'</defs><g fill="#000000">(.*)</g></svg>', WM, re.S).group(1)
WM_VB = (602.8, 155.2, 210.4, 17.4)
def wordmark(x, y, width):
    """Real logo letterforms (outlined glyphs from the stacked logo), top-left at x,y, scaled to width."""
    k = width / WM_VB[2]
    return f'<g fill="#000" transform="translate({x - WM_VB[0]*k:.4f} {y - WM_VB[1]*k:.4f}) scale({k:.5f})">{WM_USE}</g>'
def ico(name, x, y, size, w=1.9):
    k = size / 24
    return f'<g transform="translate({x:.3f} {y:.3f}) scale({k:.4f})" fill="none" stroke="#000" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{parts.ICON_PATHS[name]}</g>'

def round_svg():
    W = H = 44; c = 22; r_out = 21.2
    return W, H, f"""
<defs>{WM_DEFS}
 <path id="top" d="M {c-16.4} {c} A 16.4 16.4 0 0 1 {c+16.4} {c}"/>
 <path id="bot" d="M {c-18.0} {c} A 18.0 18.0 0 0 0 {c+18.0} {c}"/>
</defs>
<circle cx="{c}" cy="{c}" r="{r_out}" fill="none" stroke="#000" stroke-width="0.8"/>
<circle cx="{c}" cy="{c}" r="{r_out-1.35}" fill="none" stroke="#000" stroke-width="0.28"/>
<circle cx="{c}" cy="{c}" r="13.3" fill="none" stroke="#000" stroke-width="0.5"/>
<text font-family="Montserrat" font-weight="700" font-size="3.9" letter-spacing="0.62" fill="#000"><textPath href="#top" startOffset="50%" text-anchor="middle">NEW CITY LIGHT</textPath></text>
<text font-family="NCL Arabic" font-weight="800" font-size="3.9" fill="#000"><textPath href="#bot" startOffset="50%" text-anchor="middle">{parts.NAME_AR}</textPath></text>
<circle cx="{c-16.9}" cy="{c}" r="0.5" fill="#000"/><circle cx="{c+16.9}" cy="{c}" r="0.5" fill="#000"/>
{symbol(c, c, 12.2)}
"""

def rect_svg():
    W, H = 70, 34
    bx, bw = 20.5, 44.0                      # text block: left edge, width (EN + AR share this width)
    return W, H, f"""
<defs>{WM_DEFS}</defs>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="3" fill="none" stroke="#000" stroke-width="0.8"/>
<rect x="1.9" y="1.9" width="{W-3.8}" height="{H-3.8}" rx="1.9" fill="none" stroke="#000" stroke-width="0.28"/>
{symbol(10.2, H/2+0.5, 11.5)}
<line x1="16.9" y1="7" x2="16.9" y2="{H-6}" stroke="#000" stroke-width="0.28"/>
{wordmark(bx, 6.7, bw)}
<text x="{bx+bw/2}" y="18.7" text-anchor="middle" font-family="NCL Arabic" font-weight="800" font-size="{bw/7.14:.3f}" fill="#000" direction="rtl">{parts.NAME_AR}</text>
<text x="{bx+bw/2}" y="24.0" text-anchor="middle" font-family="Montserrat" font-weight="600" font-size="2.15" letter-spacing="0.12" fill="#000">{parts.ADDR_EN}  <tspan font-family="NCL Arabic" direction="rtl">·</tspan>  <tspan font-family="NCL Arabic" font-weight="700" direction="rtl">{parts.ADDR_AR}</tspan></text>
<line x1="{bx}" y1="25.9" x2="{bx+bw}" y2="25.9" stroke="#000" stroke-width="0.2"/>
{ico('mail', bx, 27.25, 2.1)}
<text x="{bx+2.9}" y="28.95" font-family="Montserrat" font-weight="500" font-size="1.6" fill="#000">{parts.EMAIL}</text>
{ico('phone', bx+bw-17.3, 27.25, 2.1)}
<text x="{bx+bw}" y="28.95" text-anchor="end" font-family="Montserrat" font-weight="500" font-size="1.6" fill="#000">{parts.PHONE}</text>
"""

def flatten(svg_text):
    defs = dict(re.findall(r'<g id="(glyph-[\d-]+)">\s*(.*?)\s*</g>', svg_text, re.S))
    def sub(m):
        gid, x, y = m.group(1), m.group(2), m.group(3)
        return f'<g transform="translate({x} {y})">{defs[gid]}</g>'
    out = re.sub(r'<use xlink:href="#(glyph-[\d-]+)" x="([-\d.]+)" y="([-\d.]+)"/>', sub, svg_text)
    out = re.sub(r'<g id="glyph-[\d-]+">.*?</g>', '', out, flags=re.S)   # drop glyph defs
    return out

for name, fn in (('round', round_svg), ('rect', rect_svg)):
    W, H, inner = fn()
    inner = f'<g transform="translate(0.6 0.6)">{inner}</g>'; W, H = W + 1.2, H + 1.2
    html = TMP / f'stamp-{name}.html'
    html.write_text(f'''<!doctype html><meta charset="utf-8"><style>{FONTS}@page{{size:{W}mm {H}mm;margin:0}}html,body{{margin:0;background:#fff}}svg{{display:block;width:{W}mm;height:{H}mm}}</style>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{inner}</svg>''')
    # fonts url relative to build/_tmp -> ../../brand/fonts OK
    pdf = TMP / f'stamp-{name}-fonts.pdf'
    subprocess.run([str(chrome.CHROME), *chrome.BASE, '--no-pdf-header-footer', f'--print-to-pdf={pdf}', html.resolve().as_uri()], check=True, capture_output=True)
    svg = TMP / f'stamp-{name}-raw.svg'
    subprocess.run(['pdftocairo', '-svg', str(pdf), str(svg)], check=True)
    flat = flatten(svg.read_text())
    flat = re.sub(r'<(?:rect|path)[^>]*fill="rgb\(100%, 100%, 100%\)"[^>]*/>', '', flat)
    flat = re.sub(r'fill="rgb\([^"]*\)"', 'fill="#000000"', flat); flat = re.sub(r'stroke="rgb\([^"]*\)"', 'stroke="#000000"', flat)
    for tag, col in (('black', '#000000'), ('navy', '#0F1E2A')):
        (OUT / f'NCL-Stamp-{name}-{tag}-outlined.svg').write_text(flat.replace('#000000', col))
    # outlined PDF from the flattened svg (paths only, no fonts)
    wrap = TMP / f'stamp-{name}-outlined.html'
    wrap.write_text(f'<!doctype html><meta charset="utf-8"><style>@page{{size:{W}mm {H}mm;margin:0}}html,body{{margin:0;background:#fff}}img{{display:block;width:{W}mm;height:{H}mm}}</style><img src="../../deliverables/06-Stamp/NCL-Stamp-{name}-black-outlined.svg">')
    subprocess.run([str(chrome.CHROME), *chrome.BASE, '--no-pdf-header-footer', f'--print-to-pdf={OUT / f"NCL-Stamp-{name}-black-outlined.pdf"}', wrap.resolve().as_uri()], check=True, capture_output=True)
    print(name, 'ok', len(flat))
