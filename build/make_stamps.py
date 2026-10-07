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

def round_svg():
    W = H = 44; c = 22; r_out = 21.2
    return W, H, f'''
<circle cx="{c}" cy="{c}" r="{r_out}" fill="none" stroke="#000" stroke-width="0.8"/>
<circle cx="{c}" cy="{c}" r="{r_out-1.35}" fill="none" stroke="#000" stroke-width="0.28"/>
<defs>
 <path id="top" d="M {c-16.3} {c} A 16.3 16.3 0 0 1 {c+16.3} {c}"/>
 <path id="bot" d="M {c-16.9} {c} A 16.9 16.9 0 0 0 {c+16.9} {c}"/>
</defs>
<text font-family="Montserrat" font-weight="700" font-size="3.9" letter-spacing="0.62" fill="#000"><textPath href="#top" startOffset="50%" text-anchor="middle">NEW CITY LIGHT</textPath></text>
<text font-family="Montserrat" font-weight="600" font-size="2.7" letter-spacing="0.55" fill="#000"><textPath href="#bot" startOffset="50%" text-anchor="middle">BAGHDAD · IRAQ</textPath></text>
<circle cx="{c-16.6}" cy="{c}" r="0.55" fill="#000"/><circle cx="{c+16.6}" cy="{c}" r="0.55" fill="#000"/>
{symbol(c, c-2.6, 10.6)}
<text x="{c}" y="{c+8.0}" text-anchor="middle" font-family="NCL Arabic" font-weight="700" font-size="3.1" fill="#000" direction="rtl">إنارة المدينة الجديدة</text>
'''

def rect_svg():
    W, H = 70, 34
    return W, H, f'''
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="3" fill="none" stroke="#000" stroke-width="0.8"/>
<rect x="1.9" y="1.9" width="{W-3.8}" height="{H-3.8}" rx="1.9" fill="none" stroke="#000" stroke-width="0.28"/>
{symbol(12.2, H/2, 14)}
<line x1="21.4" y1="6" x2="21.4" y2="{H-6}" stroke="#000" stroke-width="0.28"/>
<text x="24.6" y="10.6" font-family="Montserrat" font-weight="700" font-size="3.3" letter-spacing="0.26" fill="#000">NEW CITY LIGHT</text>
<text x="{W-4.2}" y="16.2" text-anchor="start" font-family="NCL Arabic" font-weight="700" font-size="3.2" fill="#000" direction="rtl">إنارة المدينة الجديدة</text>
<line x1="24.6" y1="18.6" x2="{W-4.2}" y2="18.6" stroke="#000" stroke-width="0.22"/>
<text x="24.6" y="22.4" font-family="Montserrat" font-weight="500" font-size="2.0" fill="#000">Baghdad – Al-Mansour – Al-Dawoodi</text>
<text x="{W-4.2}" y="25.4" text-anchor="start" font-family="NCL Arabic" font-weight="600" font-size="2.1" fill="#000" direction="rtl">بغداد – المنصور – الداوودي</text>
<text x="24.6" y="28.6" font-family="Montserrat" font-weight="500" font-size="2.0" fill="#000">+964 783 577 6393</text>
<text x="{W-4.2}" y="28.6" text-anchor="end" font-family="Montserrat" font-weight="500" font-size="2.0" fill="#000">admin@dulights.com</text>
'''

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
