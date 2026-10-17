"""Add an email-signature slide to the stationery mockups PDF.

Base : build/base/NCL-Mockups-v1.0-delivered.pdf (10 flat 3200 x 1800 JPEG slides, no source available)
Out  : deliverables/08-Mockups/NCL-Mockups-v1.0.pdf (11 slides) + brand/mockups/ncl-mockup-email-signature.jpg

What changes in the delivered slides (pixels only, retouched in place):
  - new slide 05 "02 · Email signature" after the letterhead, drawn in HTML with the slide typography
    (calibrated against slide 04 to within a few pixels) on a rebuilt grey backdrop
  - every page number "NN / 10" becomes "NN / 11"
  - cover list gets "· EMAIL SIGNATURE"
  - brand-book slide: PAGES 33 -> 37 (the book now has 37 pages)
Run: python3 build/make_mockup_signature.py
"""
import pathlib, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter
from reportlab.pdfgen import canvas

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import chrome

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / 'build/base/NCL-Mockups-v1.0-delivered.pdf'
OUT = ROOT / 'deliverables/08-Mockups/NCL-Mockups-v1.0.pdf'
TMP = ROOT / 'build/_tmp/mockups'
FONTS = ROOT / 'brand/fonts'
W, H = 3200, 1800
TOTAL = 11
SIG_INDEX = 4          # 0-based position of the new slide (after the letterhead slide)

FONT_CSS = ''.join(f"@font-face{{font-family:M;font-weight:{w};src:url({(FONTS / f'Montserrat-latin-{w}.woff2').as_uri()})}}"
                   for w in (400, 500, 600, 700, 800))
BASE_CSS = FONT_CSS + 'html,body{margin:0;background:transparent}.s{position:relative;width:3200px;height:1800px;font-family:M;overflow:hidden}'


def shoot(html, png):
    """Render a 3200 x 1800 transparent layer (headless viewport is shorter than the window, so shoot tall and crop)."""
    page = TMP / (png.stem + '.html')
    page.write_text(f'<!doctype html><meta charset="utf-8"><style>{BASE_CSS}</style>{html}', encoding='utf-8')
    subprocess.run([str(chrome.CHROME), *chrome.BASE, '--window-size=3200,2100', '--default-background-color=00000000',
                    f'--screenshot={png}', page.resolve().as_uri()], check=True, capture_output=True)
    return Image.open(png).convert('RGBA').crop((0, 0, W, H))


def erase(im, x0, y0, x1, y1, pad=5, seed=0):
    """Paint a small box out of a noisy grey background: vertical blend of the rows around it plus matching grain."""
    a = np.asarray(im).astype(float)
    top, bot = a[y0 - pad:y0, x0:x1].mean(0), a[y1:y1 + pad, x0:x1].mean(0)
    grain = (a - np.asarray(im.filter(ImageFilter.GaussianBlur(3))).astype(float))[y0 - pad:y0, x0:x1].std()
    rng = np.random.default_rng(seed)
    for y in range(y0, y1):
        t = (y - y0) / (y1 - y0)
        a[y, x0:x1] = top * (1 - t) + bot * t + rng.normal(0, grain, (x1 - x0, 1))
    return Image.fromarray(a.clip(0, 255).astype('uint8'))


def backdrop():
    """Soft grey radial backdrop with film grain, sampled to match the delivered slides."""
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    L = 212 - 25 * ((xx - 1100) ** 2 + ((yy - 450) * 1.15) ** 2) / 2147 ** 2
    n = np.random.default_rng(7).normal(0, 2.6, (H, W))
    return Image.fromarray(np.stack([L - 1 + n, L + n, L + 4 + n], -1).clip(0, 255).astype('uint8'))


FOOTER_CSS = ('.fl,.fr{position:absolute;top:1717px;font-weight:600;font-size:20px;letter-spacing:.16em;color:#5E6873}'
              '.fl{left:144px}.fr{right:146px}.fr b{color:#D2521A;font-weight:800}')


def number_layer(n):
    return shoot(f'<style>{FOOTER_CSS}</style><div class="s"><div class="fr"><b>{n:02d}</b> / {TOTAL}</div></div>', TMP / f'num-{n}.png')


SIG = (ROOT / 'deliverables/02-Email-Signature/NCL-Email-Signature-sample.png').as_uri()
ICON = (ROOT / 'brand/logos/png/ncl-app-icon.png').as_uri()
BODY = ('Thank you for the opportunity to support your project. Following our review of the drawings you shared, '
        'please find attached our proposal covering lighting design, supply of fixtures, installation support and commissioning.')


def signature_slide():
    html = f'''<style>{FOOTER_CSS}
.rule{{position:absolute;left:145px;top:150px;width:86px;height:5px;background:#F36B24}}
.eb{{position:absolute;left:145px;top:196px;font-weight:700;font-size:22px;letter-spacing:.2em;color:#C4501A}}
.h{{position:absolute;left:142px;top:241px;width:700px;font-weight:800;font-size:84px;line-height:1.08;color:#0F1E2A;letter-spacing:-.01em}}
.p{{position:absolute;left:145px;top:370px;width:690px;font-size:28px;line-height:45px;color:#3B4753}}
.col2{{position:absolute;left:145px;width:680px}}
.hr{{height:2px;background:#9EA4AB;margin-bottom:28px}}
.sp{{border-collapse:collapse;width:680px}}.sp td{{padding:8px 0;height:38px;vertical-align:top;line-height:37px}}
.sp .k{{width:218px;font-weight:700;font-size:18px;letter-spacing:.16em;color:#5E6873}}.sp .v{{font-size:25px;color:#0F1E2A;font-weight:500}}
.note{{margin-top:40px;font-size:21px;line-height:31px;color:#5E6873}}
/* mail window */
.win{{position:absolute;left:1010px;top:230px;width:1560px;height:1090px;background:#fff;border-radius:22px;overflow:hidden;
  box-shadow:0 70px 140px rgba(15,30,42,.32),0 12px 30px rgba(15,30,42,.18);transform:perspective(3600px) rotateY(-7deg) rotateX(2deg);transform-origin:left center}}
.bar{{height:66px;background:#EEF0F2;display:flex;align-items:center;gap:14px;padding-left:28px;border-bottom:1px solid #DDE1E4}}
.bar i{{width:18px;height:18px;border-radius:50%;background:#CDD2D7;display:block}}
.side{{position:absolute;left:0;top:66px;bottom:0;width:290px;background:#F6F7F8;border-right:1px solid #E3E6E9;padding:40px 30px;box-sizing:border-box}}
.side div{{height:16px;border-radius:8px;background:#DDE1E5;margin-bottom:30px}}.side .on{{background:#F7C9AE}}
.main{{position:absolute;left:290px;right:0;top:66px;bottom:0;padding:52px 70px;box-sizing:border-box}}
.subj{{font-weight:700;font-size:34px;color:#0F1E2A;margin-bottom:34px}}
.from{{display:flex;align-items:center;gap:22px;margin-bottom:40px}}
.from img{{width:66px;height:66px;border-radius:50%}}
.from b{{display:block;font-size:24px;color:#0F1E2A;font-weight:600}}.from span{{font-size:20px;color:#7A858F}}
.from em{{margin-left:auto;font-style:normal;font-size:20px;color:#7A858F;align-self:flex-start}}
.txt{{font-size:23px;line-height:38px;color:#2C3B47;max-width:1060px}}.txt p{{margin:0 0 22px}}
.sig{{display:block;width:1040px;margin-top:6px}}
.plain{{font-size:19px;color:#5E6873;margin-top:16px;letter-spacing:.01em}}
/* phone */
.ph{{position:absolute;left:2560px;top:520px;width:480px;height:990px;border-radius:70px;background:#10161D;padding:16px;box-sizing:border-box;
  box-shadow:0 60px 110px rgba(15,30,42,.38),0 10px 24px rgba(15,30,42,.25);transform:rotate(-3deg)}}
.scr{{width:100%;height:100%;border-radius:56px;background:#fff;overflow:hidden;padding:70px 26px 0;box-sizing:border-box;position:relative}}
.notch{{position:absolute;left:50%;top:18px;width:120px;height:32px;border-radius:16px;background:#10161D;transform:translateX(-50%)}}
.ps{{font-weight:700;font-size:21px;color:#0F1E2A;margin:6px 0 16px;line-height:28px}}
.pf{{display:flex;align-items:center;gap:12px;margin-bottom:18px}}.pf img{{width:40px;height:40px;border-radius:50%}}
.pf b{{font-size:16px;color:#0F1E2A;font-weight:600;display:block}}.pf span{{font-size:13px;color:#7A858F}}
.pt{{font-size:14.5px;line-height:23px;color:#2C3B47}}.pt p{{margin:0 0 12px}}
.psig{{display:block;width:100%;margin-top:4px}}
</style>
<div class="s">
 <div class="rule"></div><div class="eb">02 · EMAIL SIGNATURE</div><div class="h">Email signature</div>
 <div class="p">One wide banner for every email: the glowing symbol, logo and tagline over a dark hero, then name, title, contacts and address on white. Staff add their own details in the browser editor.</div>
 <div class="col2" id="c2"><div class="hr"></div><table class="sp">
  <tr><td class="k">SIZE</td><td class="v">1800 × 621 px, shown at 600 px</td></tr>
  <tr><td class="k">EDITABLE</td><td class="v">SVG, .ai, layered PSD</td></tr>
  <tr><td class="k">EDITOR</td><td class="v">Browser · PNG, JPG, SVG out</td></tr></table>
  <div class="note">Shown in a generic mail app with the default text. Type name, phone and email as text under the image too.</div></div>
 <div class="win"><div class="bar"><i></i><i></i><i></i></div>
  <div class="side"><div class="on" style="width:70%"></div><div style="width:55%"></div><div style="width:62%"></div><div style="width:48%"></div><div style="width:58%"></div></div>
  <div class="main"><div class="subj">Lighting design proposal – Project name</div>
   <div class="from"><img src="{ICON}" alt=""><div><b>Full Name</b><span>to Client Company</span></div><em>16 Oct 2026</em></div>
   <div class="txt"><p>Dear Sir / Madam,</p><p>{BODY}</p><p>Kind regards,</p></div>
   <img class="sig" src="{SIG}" alt="">
   <div class="plain">Full Name · Job Title · +964 783 577 6393 · admin@dulights.com</div></div></div>
 <div class="ph"><div class="scr"><div class="notch"></div>
  <div class="ps">Lighting design proposal – Project name</div>
  <div class="pf"><img src="{ICON}" alt=""><div><b>Full Name</b><span>to Client Company</span></div></div>
  <div class="pt"><p>Dear Sir / Madam,</p><p>{BODY}</p><p>Kind regards,</p></div>
  <img class="psig" src="{SIG}" alt=""></div></div>
 <div class="fl">NEW CITY LIGHT · STATIONERY MOCKUPS</div><div class="fr"><b>{SIG_INDEX + 1:02d}</b> / {TOTAL}</div>
</div>
<script>/* the divider sits 44 px under the paragraph, as on the delivered slides */
var p=document.querySelector('.p');document.getElementById('c2').style.top=(p.offsetTop+p.offsetHeight+44)+'px';</script>'''
    layer = shoot(html, TMP / 'signature-layer.png')
    return Image.alpha_composite(backdrop().convert('RGBA'), layer).convert('RGB')


def build():
    TMP.mkdir(parents=True, exist_ok=True)
    subprocess.run(['pdfimages', '-j', str(BASE), str(TMP / 's')], check=True)
    slides = [Image.open(TMP / f's-{i:03d}.jpg').convert('RGB') for i in range(10)]
    assert all(s.size == (W, H) for s in slides)

    # cover: append "· EMAIL SIGNATURE" to the contents line (old text typeset invisibly so the new words line up)
    cover_line = shoot('<div class="s"><div style="position:absolute;left:244px;top:1263px;font-weight:600;font-size:27px;'
                       'letter-spacing:.2em;color:#E4E8EC;white-space:nowrap"><span style="color:transparent">LETTERHEAD · ENVELOPES · '
                       'QUOTATION · STAMP · BAG</span> · EMAIL SIGNATURE</div></div>', TMP / 'cover-line.png')
    slides[0] = Image.alpha_composite(slides[0].convert('RGBA'), cover_line).convert('RGB')

    # brand-book slide: PAGES 33 -> 37
    s = erase(slides[2], 358, 814, 414, 852, seed=1)
    fix = shoot('<div class="s"><div style="position:absolute;left:364px;top:810px;font-size:25px;line-height:37px;font-weight:500;'
                'color:#0F1E2A">37</div></div>', TMP / 'pages-37.png')
    slides[2] = Image.alpha_composite(s.convert('RGBA'), fix).convert('RGB')

    out = slides[:SIG_INDEX] + [signature_slide()] + slides[SIG_INDEX:]
    for n, im in enumerate(out, 1):
        if n == 1 or n == SIG_INDEX + 1:
            continue
        im = erase(im, 2955, 1710, 3066, 1745, seed=n)
        out[n - 1] = Image.alpha_composite(im.convert('RGBA'), number_layer(n)).convert('RGB')

    sig_jpg = ROOT / 'brand/mockups/ncl-mockup-email-signature.jpg'
    out[SIG_INDEX].crop((860, 0, 3200, 1640)).resize((1872, 1312), Image.LANCZOS).save(sig_jpg, quality=88)

    c = canvas.Canvas(str(OUT), pagesize=(1600, 900))
    c.setTitle('New City Light – stationery mockups'); c.setAuthor('New City Light')
    for n, im in enumerate(out, 1):
        p = TMP / f'out-{n:02d}.jpg'
        im.save(p, quality=92, subsampling=0)
        c.drawImage(str(p), 0, 0, 1600, 900)
        c.showPage()
    c.save()
    print('mockups:', OUT.relative_to(ROOT), len(out), 'slides')


if __name__ == '__main__':
    build()
