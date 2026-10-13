import sys; sys.path.insert(0,'build')
import render, pathlib, parts
SPECS = {
 'c4': dict(name='Envelope C4', label='Large envelope – C4', W=324, H=229, logo=72, mx=16, my=14, flapD=0.50, flapS=0.30, logo_b=96, logo_by=0.74),
 'dl': dict(name='Envelope DL', label='Small envelope – DL', W=220, H=110, logo=50, mx=11, my=9.5, flapD=0.50, flapS=0.30, logo_b=62, logo_by=0.72),
}
TPL = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>NCL {name}</title>
<link rel="stylesheet" href="shared/common.css"><style>
.front{{background:#fff}}
.front .logo{{left:{mx}mm;top:{my}mm;width:{logo}mm}}
.front .logo-ar{{right:{mx}mm;top:{ary:.2f}mm;height:{arh:.2f}mm}}
.front .strip{{position:absolute;left:calc(-1*var(--b));right:calc(-1*var(--b));bottom:calc(-1*var(--b));height:calc({strip}mm + var(--b));background-color:var(--navy)}}
.front .strip::before{{content:"";position:absolute;left:0;right:0;top:0;height:{strip_o}mm;background:var(--orange)}}
.front .contact{{position:absolute;left:{mx}mm;bottom:{cbot}mm;font-size:{fs}pt;font-weight:500;letter-spacing:.04em;color:var(--muted)}}
.front .contact span{{color:var(--orange);font-weight:700;margin:0 1.6mm}}
.back{{background:var(--slate)}}
.back .flap{{position:absolute;left:calc(-1*var(--b));top:calc(-1*var(--b));right:calc(-1*var(--b));height:calc({fd}mm + var(--b));
  background-color:#374858;clip-path:polygon(0 0,100% 0,100% {fs_pct:.2f}%,50% 100%,0 {fs_pct:.2f}%)}}
.back .flap-edge{{position:absolute;left:calc(-1*var(--b));top:calc(-1*var(--b));right:calc(-1*var(--b));height:calc({fd}mm + var(--b))}}
.back .logo{{left:50%;transform:translateX(-50%);top:{lby}mm;width:{logo_b}mm}}
</style></head><body>
<div class="sheet front" data-w="{W}" data-h="{H}">
  <img class="abs logo" src="../brand/logos/png/ncl-horizontal-full-colour.png" alt="">
  <img class="abs logo-ar" src="../brand/logos/png/ncl-arabic-navy.png" alt="">
  <div class="contact ltr">{web}<span>·</span>{phone}<span>·</span>{addr}</div>
  <div class="strip pat-navy"></div>
</div>
<div class="sheet back" data-w="{W}" data-h="{H}">
  <div class="flap pat-slate"></div>
  <svg class="flap-edge" viewBox="0 0 100 100" preserveAspectRatio="none" style="pointer-events:none" width="100%" height="100%"></svg>
  <img class="abs logo" src="../brand/logos/png/ncl-horizontal-on-dark.png" alt="">
</div>
<script src="shared/common.js"></script></body></html>'''
for key, s in SPECS.items():
    fd = s['H'] * s['flapD']
    html = TPL.format(name=s['name'], W=s['W'], H=s['H'], logo=s['logo'], mx=s['mx'], my=s['my'],
        arh=s['logo'] * 0.5 / 5.495, ary=s['my'] + (s['logo'] * 907 / 5413 - s['logo'] * 0.5 / 5.495) / 2, web=parts.WEB, phone=parts.PHONE, addr=parts.ADDR_EN, strip=s['H'] * 0.045 + 1.5, strip_o=s['H'] * 0.008 + .6,
        cbot=s['H'] * 0.045 + 4, fs=6 + s['W'] / 220 * 1.0, fd=fd, fs_pct=s['flapS'] / s['flapD'] * 100,
        logo_b=s['logo_b'], lby=s['H'] * s['logo_by'] - 5)
    pathlib.Path(f'src/envelope-{key}.html').write_text(html)
    D = {'c4': 'deliverables/03-Envelope-Large-C4', 'dl': 'deliverables/04-Envelope-Small-DL'}[key]
    base = f"NCL-Envelope-{key.upper()}"
    render.pdf(f'src/envelope-{key}.html', f'{D}/{base}-front-back-print-5mm-bleed.pdf', '?mode=print&bleed=5')
    render.pdf(f'src/envelope-{key}.html', f'{D}/{base}-front-back-trim-size.pdf')
    render.png(f'{D}/{base}-front-back-trim-size.pdf', f'{D}/preview', 80)
    print(key, 'ok')
