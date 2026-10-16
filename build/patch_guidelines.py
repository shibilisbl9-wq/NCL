"""Put the new photographic mockups and the new email signature into the brand book.

The delivered book (build/base/NCL-Brand-Guidelines-v1.0-delivered.pdf, 33 pages) was built from sources that are
newer than src/brand-guidelines.html, so it is NOT rebuilt here. This script renders only the pages that change and
splices them in:

  p02  Contents           page numbers updated (Company data 32 -> 36)
  p23  Stationery system  new "one system" mockup + current previews
  p29  Email signature    the approved banner and its editable files
  p30-33 NEW              Mockups, two per page with their specs: letterhead & quotation form · envelopes ·
                          quotation cover & stamps · carrier bag & brand book
  p34-36                  Already delivered / Brand in the world / Company data, renumbered (were 30-32)
  p37                     back cover, unchanged

Mockup photos come from deliverables/08-Mockups/NCL-Mockups-v1.0.pdf (scene area cropped, slide text removed).
Run: python3 build/patch_guidelines.py
"""
import pathlib, subprocess, sys
from PIL import Image
from pypdf import PdfReader, PdfWriter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import render

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / 'build/base/NCL-Brand-Guidelines-v1.0-delivered.pdf'
OUT = ROOT / 'deliverables/00-Brand-Guidelines/NCL-Brand-Guidelines-v1.0.pdf'
TMP = ROOT / 'build/_tmp/guidelines-patch'
MOCK = ROOT / 'brand/mockups'
L = '../brand/logos/png/'; R = '../brand/reference-images/'; D = '../deliverables/'; M = '../brand/mockups/'

# slide number in NCL-Mockups-v1.0.pdf -> file name
SLIDES = {2: 'system', 3: 'brand-book', 4: 'letterhead', 5: 'envelope-c4', 6: 'envelope-dl',
          7: 'quotation-form', 8: 'quotation-cover', 9: 'stamps', 10: 'carrier-bag'}


def mockup_images():
    """Crop the photographed scene out of each 3200 x 1800 slide (the left 860 px is slide text, the bottom is its footer)."""
    MOCK.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    subprocess.run(['pdfimages', '-j', str(ROOT / 'deliverables/08-Mockups/NCL-Mockups-v1.0.pdf'), str(TMP / 's')], check=True)
    for n, name in SLIDES.items():
        im = Image.open(TMP / f's-{n - 1:03d}.jpg').convert('RGB')
        assert im.size == (3200, 1800), im.size
        im.crop((860, 0, 3200, 1640)).resize((1872, 1312), Image.LANCZOS).save(MOCK / f'ncl-mockup-{name}.jpg', quality=88)


# ---------- page helpers (same markup as build/make_guidelines.py) ----------
def head(eyebrow, title, lead=None):
    ld = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<div class="pad"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1>{ld}</div>'


def body(inner):
    return f'<div class="body">{inner}</div>'


def thumb(src, label, mh='128mm'):
    return (f'<div style="display:flex;flex-direction:column;justify-content:flex-start;min-height:0"><div class="bd shadowbox" '
            f'style="background:#fff;min-height:0;display:flex;align-items:center;justify-content:center;padding:2mm">'
            f'<img src="{src}" style="max-width:100%;max-height:{mh};object-fit:contain" alt=""></div>'
            f'<div class="cap" style="margin-top:1.6mm;font-weight:600;letter-spacing:.08em;text-transform:uppercase">{label}</div></div>')


def spec(rows):
    return '<table class="t"><tbody>' + ''.join(
        f'<tr><td style="width:30mm;font-weight:700;color:var(--muted);font-size:6.4pt;letter-spacing:.12em;text-transform:uppercase">{k}</td><td>{v}</td></tr>'
        for k, v in rows) + '</tbody></table>'


def photo(name, caption=None):
    """Mockup at its natural 1.43 : 1 ratio: the scenes run edge to edge, so cropping would cut the artwork."""
    cap = (f'<figcaption class="cap" style="margin-top:1.6mm;font-weight:600;letter-spacing:.08em;text-transform:uppercase">{caption}</figcaption>'
           if caption else '')
    return (f'<figure style="margin:0"><img class="shadowbox" src="{M}ncl-mockup-{name}.jpg" '
            f'style="display:block;width:100%;aspect-ratio:1872/1312" alt="">{cap}</figure>')


def mock(name, eyebrow, title, text, rows):
    return (f'<div style="min-width:0">{photo(name)}'
            f'<div class="eyebrow" style="margin-top:4.5mm">{eyebrow}</div><h2 style="margin-top:1mm">{title}</h2>'
            f'<p style="margin-bottom:2.2mm">{text}</p>{spec(rows)}</div>')


def pair(a, b):
    return f'<div class="grid g2" style="column-gap:8mm;align-items:start">{a}{b}</div>'


MOCK_NOTE = 'Mockups are illustrative: paper, light and ink are simulated. Send the print PDFs, never a mockup, to the printer.'

pages = {}  # final page number -> (section, html)

pages[2] = ('', 'TOC')

pages[23] = ('05 Stationery', head('05 · Stationery', 'The stationery system',
    'One system, built from the logo: one navy, #0F1E2A, for the footer band, the quotation cover and the envelopes, '
    'carrying the arrow pattern, and a restrained use of orange. White, light pages for correspondence; navy and orange for closed surfaces.') + body(f'''
<div class="grid" style="grid-template-columns:1.5fr 1fr;column-gap:8mm;height:100%;align-items:start">
 {photo('system', 'Mockup · letterhead, quotation form and cover, envelopes')}
 <div class="grid" style="grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;column-gap:3.5mm;row-gap:3mm;height:100%">
  {thumb(D + '01-Letterhead/preview-sample-1.png', 'Letterhead')}
  {thumb(D + '05-Quotation/preview-cover-sample-1.png', 'Quotation · cover')}
  {thumb(D + '03-Envelope-Large-C4/preview-2.png', 'Envelope C4 · back')}
  {thumb(D + '04-Envelope-Small-DL/preview-1.png', 'Envelope DL · front')}
  {thumb(D + '06-Stamp/NCL-Stamp-round-navy-preview.png', 'Stamp · round')}
  {thumb(D + '06-Stamp/NCL-Stamp-rect-navy-preview.png', 'Stamp · rect.')}
  {thumb(D + '07-Plastic-Bag/preview-orange-1.png', 'Plastic bag')}
  {thumb(D + '02-Email-Signature/NCL-Email-Signature-sample.png', 'Email signature')}
 </div>
</div>'''))

pages[29] = ('05 Stationery', head('05 · Stationery', 'Email signature',
    'One wide banner, placed at 600 px: a dark hero with the glowing symbol, the logo and the tagline, then name, title, '
    'contacts and address on white, closed by the orange rule and the navy pattern strip.') + body(f'''
<div class="grid" style="grid-template-columns:1.25fr 1fr;column-gap:10mm;height:100%">
 <div style="display:flex;flex-direction:column;gap:5mm;min-height:0">
  <div class="bd" style="background:var(--tint);padding:7mm;display:flex;align-items:center;justify-content:center">
   <img src="{D}02-Email-Signature/NCL-Email-Signature-sample.png" class="shadowbox" style="width:100%" alt=""></div>
  <div class="cap" style="font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin-top:-3mm">Master · 1800 × 621 px · default text</div>
  <div class="card"><h3>Layers in the editable files</h3>
   <p style="margin:0">Background hero (photo) · white panel · footer strip (image) · logo (vector) · tagline · name &amp; title ·
   contacts (icons + text) · company name &amp; address. Only the two images are raster; the rest is vector or live text.</p></div>
 </div>
 <div>
 {spec([('Size', '1800 × 621 px master, inserted at 600 px wide: 3× for sharp screens'),
        ('Type', 'Montserrat; the Arabic tagline in Noto Kufi Arabic. The approved JPG set name and address in another sans; the editable files use Montserrat'),
        ('Editable', 'SVG with layers and live text (Illustrator, Figma, Inkscape) · .ai, PDF-compatible, live text · PSD, one layer per element, text rasterised'),
        ('Editor', 'NCL-Email-Signature-Editor.html: type name, title and contacts, download PNG, JPG or SVG. Works offline, fonts embedded'),
        ('Clickable text', 'An image alone is not clickable, stays hidden until the reader allows images and is silent to screen readers: always type name, phone and email as text under it'),
        ('Fonts to install', 'brand/fonts/desktop/ · Montserrat and Noto Kufi Arabic TTF, free (SIL OFL), needed to edit the .ai and SVG'),
        ('Files', '02-Email-Signature/ · approved JPG, SVG, .ai, PSD, editor, sample PNG, links/')])}
 </div>
</div>'''))

pages[30] = ('05 Stationery', head('05 · Mockups', 'Letterhead &amp; quotation form',
    'The delivered artwork, photographed in place, for presentations and proposals. ' + MOCK_NOTE) + body(pair(
    mock('letterhead', '01 · Letterhead', 'Letterhead', 'English logo left, Arabic logo right, a navy footer band with address, phones and web. Sample letter text is illustrative.',
         [('Size', 'A4 · 210 × 297 mm'), ('Print file', '3 mm bleed + crop marks'), ('Files', 'PDF (blank, sample letter), Word .docx')]),
    mock('quotation-form', '05 · Quotation', 'Quotation form', 'Bilingual A4 form: details, parties, item table, totals, terms and signature boxes. Shown with sample data and the round stamp.',
         [('Size', 'A4 · 210 × 297 mm'), ('Print file', '3 mm bleed, blank'), ('Files', 'PDF (blank, sample), Excel .xlsx')]))))

pages[31] = ('05 Stationery', head('05 · Mockups', 'Envelopes',
    'One two-sided design in two sizes: white front with both logos and a navy contact strip; navy back with the patterned flap. ' + MOCK_NOTE) + body(pair(
    mock('envelope-c4', '03 · Envelope', 'Large envelope C4', 'Holds A4 flat. The back is the same navy as the quotation cover, with a centred logo.',
         [('Size', 'C4 · 324 × 229 mm'), ('Print file', '5 mm bleed, front + back'), ('Also', 'Trim-size PDF')]),
    mock('envelope-dl', '04 · Envelope', 'Small envelope DL', 'The same design at letter size, for folded A4 letters and quotations.',
         [('Size', 'DL · 220 × 110 mm'), ('Print file', '5 mm bleed, front + back'), ('Also', 'Trim-size PDF')]))))

pages[32] = ('05 Stationery', head('05 · Mockups', 'Quotation cover &amp; stamps',
    'The navy cover that wraps every quotation, and the two company stamps. ' + MOCK_NOTE) + body(pair(
    mock('quotation-cover', '05 · Quotation', 'Quotation cover', 'Navy with the arrow pattern, an outlined symbol and an orange spine band. White write-in boxes on the front; partners, QR code and contacts on the back.',
         [('Size', 'A4 · front + back'), ('Print file', '3 mm bleed + crop marks'), ('Files', 'PDF (print, blank) · sample previews')]),
    mock('stamps', '06 · Stamp', 'Company stamps', 'One colour, every letter outlined. Round: both names on the arcs. Rectangular: both logos, the symbol between them, address and contacts. Simulated ink.',
         [('Round', 'Ø 43 mm'), ('Rectangular', '80 × 26 mm'), ('Files', 'SVG + PDF, navy and black')]))))

pages[33] = ('05 Stationery', head('05 · Mockups', 'Carrier bag &amp; brand book',
    'The bag in both films, and this book as a printed object. ' + MOCK_NOTE) + body(pair(
    mock('carrier-bag', '07 · Plastic bag', 'Carrier bag', 'Orange film with the arrow pattern, or clear film with orange and navy print on a white underlay. Die-line and film belong to the manufacturer.',
         [('Size', '350 × 450 mm'), ('Handle', 'Die-cut, 150 × 32 mm'), ('Top hem', '30 mm seal zone')]),
    mock('brand-book', '00 · Brand guidelines', 'Brand guidelines book', 'The rulebook for the identity: logo, colour, typography, graphic language and how each stationery piece is built.',
         [('Format', 'A4 landscape · 297 × 210 mm'), ('Version', '1.0 · October 2026'), ('File', '00-Brand-Guidelines/ · PDF')]))))

pages[34] = ('05 Stationery', head('05 · Applications', 'Already delivered: cards, badges, sets',
    'Existing identity work supplied with this project. These pieces set the colours and mood the new stationery follows.') + body(f'''
<div class="grid" style="grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;column-gap:5mm;row-gap:5mm;height:100%">
 <div class="frame" style="grid-row:span 2;position:relative"><img src="{R}mock-business-cards.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#fff">Business cards · orange front, slate back</div></div>
 <div class="frame" style="position:relative"><img src="{R}mock-id-badge.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#fff">ID badge</div></div>
 <div class="frame" style="position:relative"><img src="{R}mock-sling-bag.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#fff">Merchandise</div></div>
</div>'''))

pages[35] = ('05 Stationery', head('05 · Applications', 'The brand in the world',
    'Vehicles, containers, signage, window graphics and workwear: the same orange, navy and white, with the logo kept large and uncluttered.') + body(f'''
<div class="grid g3" style="grid-template-rows:1fr 1fr;column-gap:4mm;row-gap:4mm;height:100%">
 <div class="frame" style="position:relative"><img src="{R}mock-truck.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-container.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-storefront-sign.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-window-graphics.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-apparel.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}post-lighting-way.jpg" style="object-position:center 30%" alt=""></div>
</div>'''))

pages[36] = ('Reference', head('Reference', 'Company data &amp; open items',
    'Everything printed in this pack comes from one list. Change it here first, then rebuild.') + body('''
<div class="grid" style="grid-template-columns:1fr 1.15fr;column-gap:10mm;height:100%">
 <div>
  <h3>Company data used on the stationery</h3>
  <table class="t"><tbody>
   <tr><td style="width:24mm;font-weight:700;color:var(--muted)">Name</td><td>New City Light · إنارة المدينة الجديدة</td></tr>
   <tr><td style="font-weight:700;color:var(--muted)">Tagline</td><td>Lighting the Way · ننير الدرب</td></tr>
   <tr><td style="font-weight:700;color:var(--muted)">Address</td><td>Baghdad – Al-Mansour – Al-Dawoodi, Iraq<br><span class="ar" style="direction:rtl">بغداد – المنصور – الداوودي</span></td></tr>
   <tr><td style="font-weight:700;color:var(--muted)">Phone</td><td>+964 783 577 6393<br>+964 786 555 3648<br>+964 780 517 7717</td></tr>
   <tr><td style="font-weight:700;color:var(--muted)">Email</td><td>admin@dulights.com</td></tr>
   <tr><td style="font-weight:700;color:var(--muted)">Web</td><td>www.dulights.com</td></tr>
  </tbody></table>
  <p class="cap" style="margin-top:2.5mm">Taken from the company brochure (Broucher.ai).</p>
 </div>
 <div>
  <h3>To confirm before printing</h3>
  <ul>
   <li><b>Logo master.</b> The English lockup is now the vector artwork from NCL’s SAMP file (Oct 2026), with the tagline respaced to the wordmark width and the text centred on the symbol. Use these files from now on; the older PNGs are retired.</li>
   <li><b>Website.</b> The brochure says <i>dulights.com</i> (also its email); the business card mockup says <i>www.NewCityLight.com</i>. One has to win.</li>
   <li><b>Arabic spelling.</b> The Arabic logo reads «انارة» (no hamza); the brochure body text writes «إنارة». Decide once and use it everywhere.</li>
   <li><b>Experience claim.</b> The brochure says “more than 30 years” but its timeline starts in 1998 (28 years). Don’t print either on stationery until settled.</li>
   <li><b>Fonts.</b> GE SS Two and Nasalization are commercial or personal-use only; check licences. Montserrat and Noto Kufi are free.</li>
   <li><b>Colours.</b> CMYK values are starting points. Approve a printed swatch (and Pantone match if you use spot colour).</li>
   <li><b>Quotation terms &amp; stamp wording.</b> Placeholders. Legal and registration wording needs NCL’s sign-off.</li>
  </ul>
 </div>
</div>'''))

TOC_SECTIONS = [('01', 'The brand', 3), ('02', 'The logo', 6), ('03', 'Colour & typography', 12), ('04', 'Graphic language', 18),
                ('05', 'Stationery & applications', 22), ('', 'Company data & open items', 36)]


def toc():
    rows = ''.join(f'<tr><td style="width:18mm;font-weight:800;font-size:18pt;color:var(--orange-text);padding:5.5mm 2mm">{n}</td>'
                   f'<td style="font-weight:700;font-size:13pt">{t}</td><td style="text-align:right;font-weight:600;font-size:11pt;color:var(--muted)">{p:02d}</td></tr>'
                   for n, t, p in TOC_SECTIONS)
    return head('Contents', 'Contents') + body(f'''
<div class="grid" style="grid-template-columns:1.2fr 1fr;column-gap:14mm">
 <table class="t" style="font-size:11pt"><tbody>{rows}</tbody></table>
 <div class="card"><h3>About this book</h3><p>These guidelines describe the New City Light identity as delivered in the rebranding files, and set out the stationery system built from it: letterhead, envelopes, quotation, stamp, plastic bag and email signature.</p><p style="margin:0">Where a value was measured from existing artwork rather than specified by the client (slate colour, pattern, text-safe orange), the page says so.</p></div>
</div>''')


def build():
    mockup_images()
    order = sorted(pages)
    sheets = []
    for n in order:
        sec, html = pages[n]
        if html == 'TOC':
            html = toc()
        ft = f'<div class="foot"><span>New City Light &nbsp;·&nbsp; Brand Guidelines</span><span>{sec} &nbsp;·&nbsp; <b>{n:02d}</b></span></div>'
        sheets.append(f'<div class="sheet gp" data-w="297" data-h="210">{html}{ft}</div>')
    src = ROOT / 'src/brand-guidelines-patch.html'
    src.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>NCL Brand Guidelines</title>'
                   '<link rel="stylesheet" href="shared/common.css"><link rel="stylesheet" href="guidelines.css"></head><body>\n'
                   + '\n'.join(sheets) + '\n<script src="shared/common.js"></script></body></html>', encoding='utf-8')
    patch_pdf = render.pdf('src/brand-guidelines-patch.html', 'build/_tmp/guidelines-patch/patch.pdf')

    base, patch = PdfReader(BASE), PdfReader(patch_pdf)
    assert len(base.pages) == 33, 'base must be the 33-page delivered book'
    assert len(patch.pages) == len(order), (len(patch.pages), len(order))
    new = dict(zip(order, patch.pages))
    # final page -> source page in the delivered book (1-based); everything not rendered above comes from there
    from_base = {n: n for n in range(1, 29)}
    from_base[37] = 33
    w = PdfWriter()
    for n in range(1, 38):
        w.add_page(new[n] if n in new else base.pages[from_base[n] - 1])
    w.add_metadata({'/Title': 'New City Light – Brand Guidelines v1.0', '/Author': 'New City Light'})
    with open(OUT, 'wb') as f:
        w.write(f)
    print('guidelines:', OUT.relative_to(ROOT), '37 pages')


if __name__ == '__main__':
    build()
