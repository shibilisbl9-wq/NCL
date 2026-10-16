"""Editable email-signature banner (1800 x 621 px) rebuilt from the approved flat JPG.

Input : deliverables/02-Email-Signature/ncl-signature-banner-letterhead-pattern.jpg (approved design, flat)
Output: deliverables/02-Email-Signature/
          NCL-Email-Signature-editable.svg   layered vector, live text (Illustrator / Figma / Inkscape)
          NCL-Email-Signature-editable.ai    PDF-compatible .ai, live text (opens in Illustrator)
          NCL-Email-Signature-layered.psd    Photoshop, one raster layer per element (text NOT live)
          NCL-Email-Signature-Editor.html    fill in name/title/contacts in a browser, download PNG/JPG/SVG
          NCL-Email-Signature-sample.png     what the default text looks like
          links/                             the two raster layers (hero glow, footer strip)

The hero photo and the footer pattern stay raster (they are raster in the approved JPG).
Logo and wordmark are vector, from brand/logos/vector/ncl-stacked-on-dark.svg. Everything else is live text.
"""
import base64, json, pathlib, re, subprocess, sys, xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import chrome

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'deliverables/02-Email-Signature'
SRC = OUT / 'ncl-signature-banner-letterhead-pattern.jpg'
TMP = ROOT / 'build/_tmp/signature'
W, H = 1800, 621
NAVY, ORANGE, OFFWHITE = '#0F1E2A', '#F36B24', '#F5F5F4'

DEFAULTS = {
    'name': 'Full Name',
    'title': 'Job Title',
    'phone': '+964 783 577 6393',
    'email': 'admin@dulights.com',
    'web': 'www.dulights.com',
    'address1': 'Al-Mansour – Al-Dawoodi',
    'address2': 'Baghdad, Iraq',
    'tagline_en': 'lighting the way',
    'tagline_ar': 'ننير الدرب',
}


# ---------- raster layers, cut from the approved JPG ----------
def raster_layers():
    im = Image.open(SRC).convert('RGB')
    assert im.size == (W, H), im.size
    hero = im.crop((0, 0, W, 360))
    a = np.asarray(hero).astype(float)
    hp = a - np.asarray(hero.filter(ImageFilter.GaussianBlur(3))).astype(float)

    def erase(x0, x1, y0, y1, pad=6):
        # vertical blend of the rows just outside the box, plus film grain from a clean dark area
        top, bot, w = a[y0 - pad:y0].mean(0), a[y1:y1 + pad].mean(0), x1 - x0
        for y in range(y0, y1):
            t = (y - y0) / (y1 - y0)
            a[y, x0:x1] = (top * (1 - t) + bot * t)[x0:x1] + hp[255 + (y - y0) % 100, 250:250 + w]

    erase(95, 630, 115, 252)    # baked-in logo
    erase(800, 1215, 145, 222)  # baked-in tagline
    links = OUT / 'links'
    links.mkdir(exist_ok=True)
    Image.fromarray(np.clip(a, 0, 255).astype('uint8')).save(links / 'ncl-signature-hero.jpg', quality=92)
    im.crop((0, 588, W, H)).save(links / 'ncl-signature-footer-strip.png')


def b64(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(pathlib.Path(path).read_bytes()).decode()


# ---------- vector logo parts from the stacked master ----------
def logo_parts():
    ns = {'s': 'http://www.w3.org/2000/svg'}
    XL = '{http://www.w3.org/1999/xlink}href'
    root = ET.parse(ROOT / 'brand/logos/vector/ncl-stacked-on-dark.svg').getroot()
    glyphs = {g.get('id'): [p.get('d') for p in g.findall('s:path', ns)] for g in root.find('s:defs', ns)}
    symbol = [p.get('d') for p in root.find('s:g', ns).findall('s:path', ns)]
    line1, line2 = [], []
    for g in root.findall('s:g', ns)[1:]:
        for u in g.findall('s:use', ns):
            x, y = float(u.get('x')), float(u.get('y'))
            for d in glyphs[u.get(XL)[1:]]:
                (line1 if y < 175 else line2).append(f'<path transform="translate({x:.3f} {y:.3f})" d="{d}"/>')
    ring = root.findall('s:path', ns)[-1]
    line2.append(f'<path fill="none" stroke="currentColor" stroke-width="1" stroke-miterlimit="10" '
                 f'transform="{ring.get("transform")}" d="{ring.get("d")}"/>')
    return symbol, line1, line2


def logo_svg(fill_symbol, fill_text, x, y, h):
    """Horizontal lockup: symbol + two-line wordmark, symbol height h, top-left at (x, y)."""
    symbol, line1, line2 = logo_parts()
    s = h / 80.094                                      # symbol box is 80.09 units
    sym = ''.join(f'<path d="{d}"/>' for d in symbol)
    k = s * 1.745                                       # wordmark : symbol ratio of the approved banner
    wx, wy = x + h * 1.32, y + h * 0.58                 # wordmark origin = line-1 baseline
    return (f'<g id="Logo">'
            f'<g id="Symbol" fill="{fill_symbol}" transform="translate({x:.2f} {y:.2f}) scale({s:.5f}) translate(-667.75 -51.492)">{sym}</g>'
            f'<g id="Wordmark" fill="{fill_text}" color="{fill_text}" transform="translate({wx:.2f} {wy:.2f}) scale({k:.5f}) translate(-603.368 -172.186)">'
            f'<g id="NEW_CITY_LIGHT">{"".join(line1)}</g><g id="LIGHTING_THE_WAY">{"".join(line2)}</g></g></g>')


def wordmark_line1(fill, x, baseline, width):
    _, line1, _ = logo_parts()
    k = width / 211.6
    return (f'<g id="Company_name" fill="{fill}" transform="translate({x:.2f} {baseline:.2f}) scale({k:.5f}) translate(-603.368 -172.186)">'
            f'{"".join(line1)}</g>')


# Material Icons (Apache 2.0): call, mail, language
ICON = {
    'phone': 'M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z',
    'email': 'M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z',
    'web': 'M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95c-.32-1.25-.78-2.45-1.38-3.56 1.84.63 3.37 1.91 4.33 3.56zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56-1.84-.63-3.37-1.9-4.33-3.56zm2.95-8H5.08c.96-1.66 2.49-2.93 4.33-3.56C8.81 5.55 8.35 6.75 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2 0-.68.07-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95c-.96 1.65-2.49 2.93-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z',
}


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def font_css(embed, desktop=False):
    """desktop=True uses the static TTF files, so the .ai carries the real PostScript names
    (Montserrat-Regular ...) and Illustrator maps them to an installed Montserrat."""
    if not embed:
        return ''
    if desktop:
        faces = [('Montserrat', 400, 'desktop/Montserrat-Regular.ttf'), ('Montserrat', 500, 'desktop/Montserrat-Medium.ttf'),
                 ('Montserrat', 600, 'desktop/Montserrat-SemiBold.ttf'), ('Noto Kufi Arabic', 400, 'desktop/NotoKufiArabic-Regular.ttf')]
    else:
        faces = [('Montserrat', 400, 'Montserrat-latin-400.woff2'), ('Montserrat', 500, 'Montserrat-latin-500.woff2'),
                 ('Montserrat', 600, 'Montserrat-latin-600.woff2'), ('Noto Kufi Arabic', 400, 'NotoKufiArabic-arabic-400.woff2')]
    return ''.join(f"@font-face{{font-family:'{f}';font-weight:{w};src:url({b64(ROOT / 'brand/fonts' / n, 'font/' + n.rsplit('.', 1)[1])})}}"
                   for f, w, n in faces)


def signature_svg(d=DEFAULTS, hero=None, strip=None, embed_fonts=True, only=None, desktop_fonts=False):
    """only: render a single layer id (for the PSD), everything else omitted."""
    hero = hero or b64(OUT / 'links/ncl-signature-hero.jpg', 'image/jpeg')
    strip = strip or b64(OUT / 'links/ncl-signature-footer-strip.png', 'image/png')
    M = "font-family:Montserrat,'Segoe UI',Arial,sans-serif"
    L = {
        'Background_hero': f'<image x="0" y="0" width="{W}" height="360" href="{hero}" xlink:href="{hero}" preserveAspectRatio="none"/>',
        'Background_white': f'<rect x="0" y="360" width="{W}" height="228" fill="#FFFFFF"/>',
        'Footer_strip': f'<image x="0" y="588" width="{W}" height="33" href="{strip}" xlink:href="{strip}" preserveAspectRatio="none"/>',
        'Logo': logo_svg(ORANGE, OFFWHITE, 110, 137, 85),
        'Tagline': (f'<text id="Tagline_EN" x="815" y="194" style="{M};font-size:30px;font-weight:400" fill="#FFFFFF">{esc(d["tagline_en"])}</text>'
                    f'<text id="Dot" x="1074" y="192" text-anchor="middle" style="{M};font-size:30px;font-weight:400" fill="#B9B4B0">·</text>'
                    f'<text id="Tagline_AR" x="1210" y="194" text-anchor="end" style="font-family:\'Noto Kufi Arabic\',Tahoma,sans-serif;font-size:30px;font-weight:400" fill="#FFFFFF">{esc(d["tagline_ar"])}</text>'),
        'Name_and_title': (f'<text id="Name" x="155" y="452" style="{M};font-size:31px;font-weight:600" fill="{NAVY}">{esc(d["name"])}</text>'
                           f'<text id="Job_title" x="155" y="487" style="{M};font-size:23px;font-weight:500" fill="#E2561A">{esc(d["title"])}</text>'),
        'Contacts': ''.join(
            f'<g id="{k.title()}"><path transform="translate(639 {y - 25}) scale(1.4)" fill="{ORANGE}" d="{ICON[k]}"/>'
            f'<text x="687" y="{y}" style="{M};font-size:23px;font-weight:400" fill="{NAVY}">{esc(d[k])}</text></g>'
            for k, y in (('phone', 449), ('email', 495), ('web', 541))),
        'Company_and_address': (wordmark_line1(ORANGE, 1222, 458, 323) +
                                f'<text id="Address_line_1" x="1222" y="496" style="{M};font-size:23px;font-weight:400" fill="{NAVY}">{esc(d["address1"])}</text>'
                                f'<text id="Address_line_2" x="1222" y="531" style="{M};font-size:23px;font-weight:400" fill="{NAVY}">{esc(d["address2"])}</text>'),
    }
    order = ['Background_hero', 'Background_white', 'Footer_strip', 'Logo', 'Tagline', 'Name_and_title', 'Contacts', 'Company_and_address']
    body = ''.join(f'<g id="{k}" inkscape:groupmode="layer" inkscape:label="{k.replace("_", " ")}">{L[k]}</g>'
                   for k in order if only in (None, k))
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<title>New City Light – email signature</title><style>{font_css(embed_fonts, desktop_fonts)}</style>{body}</svg>\n')


def shot(html, png, transparent=False):
    extra = ['--default-background-color=00000000'] if transparent else []
    subprocess.run([str(chrome.CHROME), *chrome.BASE, f'--window-size={W},{H + 300}', *extra,
                    f'--screenshot={png}', pathlib.Path(html).resolve().as_uri()], check=True, capture_output=True)
    Image.open(png).crop((0, 0, W, H)).save(png)


def html_page(svg, w=W, h=H, transparent=False):
    bg = 'transparent' if transparent else '#fff'
    return (f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{bg}}}svg{{display:block}}</style>'
            f'{svg[svg.index("<svg"):]}')


def build():
    TMP.mkdir(parents=True, exist_ok=True)
    raster_layers()
    svg = signature_svg()
    (OUT / 'NCL-Email-Signature-editable.svg').write_text(svg, encoding='utf-8')

    # sample PNG + .ai (PDF-compatible: Illustrator opens it with live text)
    page = TMP / 'sig.html'
    page.write_text(html_page(svg), encoding='utf-8')
    shot(page, OUT / 'NCL-Email-Signature-sample.png')
    pdf_page = TMP / 'sig-pdf.html'
    pdf_page.write_text(html_page(signature_svg(desktop_fonts=True)).replace('<style>', f'<style>@page{{size:{W * 0.75}pt {H * 0.75}pt;margin:0}}'
                                                       f'svg{{width:{W * 0.75}pt;height:{H * 0.75}pt}}'), encoding='utf-8')
    chrome.pdf(pdf_page, OUT / 'NCL-Email-Signature-editable.ai')

    # layered PSD: one transparent PNG per layer, then ImageMagick packs them (first image = flattened composite)
    names = ['Background_hero', 'Background_white', 'Footer_strip', 'Logo', 'Tagline', 'Name_and_title', 'Contacts', 'Company_and_address']
    pngs = []
    for n in names:
        p = TMP / f'layer-{n}.html'
        p.write_text(html_page(signature_svg(only=n), transparent=True), encoding='utf-8')
        out = TMP / f'layer-{n}.png'
        shot(p, out, transparent=True)
        pngs.append((n, out))
    cmd = ['convert', str(OUT / 'NCL-Email-Signature-sample.png')]
    for n, p in pngs:
        cmd += ['(', str(p), '-set', 'label', n.replace('_', ' '), ')']
    subprocess.run(cmd + [str(OUT / 'NCL-Email-Signature-layered.psd')], check=True)

    # in-browser editor
    tpl = (ROOT / 'src/email-signature-editor.html').read_text(encoding='utf-8')
    editor_svg = signature_svg(d={k: f'{{{{{k}}}}}' for k in DEFAULTS})
    tpl = tpl.replace('/*SVG_TEMPLATE*/', json.dumps(editor_svg)).replace('/*DEFAULTS*/', json.dumps(DEFAULTS, ensure_ascii=False))
    (OUT / 'NCL-Email-Signature-Editor.html').write_text(tpl, encoding='utf-8')
    print('signature: editable SVG / AI / PSD / editor written')


if __name__ == '__main__':
    build()
