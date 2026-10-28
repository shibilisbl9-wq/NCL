import sys, pathlib, re; sys.path.insert(0, 'build')
import render

L = '../brand/logos/png/'; V = '../brand/logos/vector/'; R = '../brand/reference-images/'; D = '../deliverables/'
pages = []
def add(sec, html, kind='', pid=None, foot=True): pages.append(dict(sec=sec, html=html, kind=kind, id=pid, foot=foot))
def head(eyebrow, title, lead=None):
    ld = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<div class="pad"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1>{ld}</div>'
def body(inner, top=None, style=''):
    t = f'top:{top}mm;' if top else ''
    return f'<div class="body" style="{t}{style}">{inner}</div>'
def divider(num, title, sub):
    return (f'<div class="abs pat-slate" style="inset:0"></div>'
            f'<img class="abs" src="{V}ncl-symbol-orange.svg" style="right:-46mm;bottom:-52mm;width:210mm;opacity:.09" alt="">'
            f'<img class="abs" src="{L}ncl-horizontal-on-dark.png" style="left:18mm;top:15mm;width:46mm" alt="">'
            f'<div class="big-num">{num}</div><div class="div-title">{title}</div><div class="div-sub">{sub}</div>')

# ------------------------------------------------------------------ COVER
add('', f'''
<div class="abs pat-slate" style="inset:0"></div>
<img class="abs" src="{V}ncl-symbol-orange.svg" style="right:-58mm;top:-44mm;width:290mm;opacity:.10" alt="">
<img class="abs" src="{V}ncl-stacked-on-dark.svg" style="left:26mm;top:30mm;height:66mm" alt="New City Light">
<div class="abs" style="left:26mm;top:118mm;font-weight:800;font-size:40pt;line-height:1.02;color:#fff;letter-spacing:-.015em">Brand<br>Guidelines</div>
<div class="abs" style="left:26mm;top:160mm;width:70mm;height:1.1mm;background:var(--orange)"></div>
<div class="abs" style="left:26mm;top:166mm;font-size:8.6pt;letter-spacing:.2em;text-transform:uppercase;color:#aebbc6;font-weight:600">Visual identity &amp; stationery system</div>
<div class="abs" style="left:26mm;top:174mm;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:#7f91a0;font-weight:600">Version 1.0 &nbsp;·&nbsp; October 2026</div>
<div class="abs ar" style="right:26mm;bottom:22mm;font-size:17pt;font-weight:800;color:#fff;text-align:left">دليل الهوية البصرية</div>
''', kind='dark', foot=False)

# ------------------------------------------------------------------ CONTENTS (filled later)
add('', '@@TOC@@', pid='toc')

# ------------------------------------------------------------------ 01 BRAND
add('01 Brand', divider('01', 'The brand', 'Who New City Light is, what it stands for and how it speaks.'), kind='dark', foot=False, pid='s1')

add('01 Brand', head('01 · Brand', 'Who we are', 'New City Light (NCL) is a Baghdad lighting company that designs, supplies, installs and commissions lighting for homes, commercial buildings and large public projects.') + body(f'''
<div class="grid" style="grid-template-columns:1.1fr 1fr 1fr;column-gap:9mm;height:96mm">
 <div>
  <h3>What we do</h3>
  <ul>
   <li><b>1 · Study &amp; design.</b> Lighting design and illumination calculations for every kind of project, to international standards.</li>
   <li><b>2 · Supply.</b> Quality lighting products and electrical installations, with genuine warranties.</li>
   <li><b>3 · Installation.</b> Specialised technical crews, from residential work to complex media façades and architectural lighting.</li>
   <li><b>4 · Programming &amp; commissioning.</b> Smart control systems set up for the best aesthetic and functional result.</li>
  </ul>
  <div class="card" style="margin-top:5mm"><h3>Partners named in the company brochure</h3><p style="margin:0">Exclusive agent in Iraq for <b>DuLight</b> (UAE) and for international brands including OSRAM, Tridonic, LEDVANCE, PCE and Frequentis.</p></div>
 </div>
 <div>
  <h3>Milestones</h3>
  <table class="t"><tbody>
   <tr><td style="width:14mm;font-weight:800;color:var(--orange-text)">1998</td><td>Starts in the Baghdad electrical market, distributing quality lighting products.</td></tr>
   <tr><td style="font-weight:800;color:var(--orange-text)">2004</td><td>Becomes distributor for OSRAM (Germany) and Tridonic (Austria).</td></tr>
   <tr><td style="font-weight:800;color:var(--orange-text)">2005</td><td>Opens a branch in Dubai to serve the Iraqi market with high-quality materials and technology transfer.</td></tr>
   <tr><td style="font-weight:800;color:var(--orange-text)">2012</td><td>Establishes a factory in the Jebel Ali Free Zone (JAFZA), Dubai, to manufacture and assemble lighting fixtures.</td></tr>
  </tbody></table>
  <p class="cap" style="margin-top:3mm">Source: company brochure (Arabic). Wording condensed.</p>
 </div>
 <div style="position:relative;background:var(--navy);margin:-2mm 0 0;overflow:hidden">
   <div class="abs pat-slate" style="inset:0"></div>
   <img class="abs" src="{V}ncl-stacked-on-dark.svg" style="left:50%;top:50%;transform:translate(-50%,-56%);width:78%" alt="">
   <div class="abs ar" style="left:0;right:0;bottom:7mm;text-align:center;color:#fff;font-weight:700;font-size:9pt;line-height:1.9">مدينة جديدة. إنارة جديدة.<br>منظور جديد.</div>
 </div>
</div>
<div class="frame abs" style="left:0;right:0;bottom:0;height:34mm"><img src="{R}post-city.jpg" style="object-position:center 92%" alt=""></div>'''), pid='about')

add('01 Brand', head('01 · Brand', 'Essence &amp; voice', 'The line “Lighting the Way” (ننير الدرب) is the promise. Everything we make should feel like it guides the viewer from darkness to clarity: confident, warm and precise.') + body(f'''
<div class="grid" style="grid-template-columns:1fr 1fr;column-gap:12mm;height:96mm">
 <div>
  <h3>Brand line</h3>
  <div style="font-weight:800;font-size:25pt;line-height:1.05;letter-spacing:-.01em">LIGHTING<br>THE WAY.</div>
  <div class="ar" style="font-weight:800;font-size:19pt;color:var(--orange-text);margin-top:2mm;text-align:left;direction:rtl">ننير الدرب.</div>
  <h3 style="margin-top:7mm">Brand statement</h3>
  <div class="ar" style="font-weight:700;font-size:13pt;line-height:1.7;direction:rtl;text-align:left">مدينة جديدة. إنارة جديدة. منظور جديد.</div>
  <p class="cap" style="margin-top:1.5mm">Working English: “A new city. New lighting. A new perspective.” Confirm wording before public use.</p>
 </div>
 <div>
  <h3>Personality <span style="font-weight:500;letter-spacing:.04em;text-transform:none;color:var(--muted)">(proposed – to be confirmed by NCL)</span></h3>
  <div class="grid g2" style="row-gap:3mm;column-gap:4mm;margin-bottom:5mm">
   <div class="card"><h2 style="margin:0">Precise</h2><p style="margin:0">Technical credibility; every claim is specific.</p></div>
   <div class="card"><h2 style="margin:0">Warm</h2><p style="margin:0">Light is human; imagery and tone are inviting.</p></div>
   <div class="card"><h2 style="margin:0">Confident</h2><p style="margin:0">Short, declarative lines. No hedging.</p></div>
   <div class="card"><h2 style="margin:0">Forward</h2><p style="margin:0">New city, new perspective: modern, never trendy.</p></div>
  </div>
  <h3>Headline style (taken from the existing campaign posts)</h3>
  <div style="display:flex;flex-wrap:wrap;gap:2mm">
   <span class="pill" style="background:var(--navy);color:#fff;font-size:6.2pt">HOME. ELEVATED.</span>
   <span class="pill" style="background:var(--navy);color:#fff;font-size:6.2pt">YOUR CITY. REIMAGINED.</span>
   <span class="pill" style="background:var(--navy);color:#fff;font-size:6.2pt">BRILLIANCE FROM ABOVE.</span>
   <span class="pill" style="background:var(--navy);color:#fff;font-size:6.2pt">LIGHTING CITIES. LIGHTING LIVES.</span>
  </div>
  <p style="margin-top:3mm">Two short sentences, capitals, full stops. Body copy is sentence case, plain and specific.</p>
 </div>
</div>
<div class="frame abs" style="left:0;right:0;bottom:0;height:34mm"><img src="{R}post-linear.jpg" style="object-position:center 74%" alt=""></div>'''), pid='essence')

# ------------------------------------------------------------------ 02 LOGO
add('02 Logo', divider('02', 'The logo', 'Symbol, wordmark and tagline: how they fit together and how to protect them.'), kind='dark', foot=False, pid='s2')

add('02 Logo', head('02 · Logo', 'Primary logo', 'The horizontal lockup is the default. It combines the radiating symbol, the NEW CITY LIGHT wordmark and the tagline LIGHTING THE WAY with the ® mark. It is supplied as artwork. Never retype or rebuild it.') + body(f'''
<div class="grid" style="grid-template-columns:1.7fr 1fr;column-gap:10mm;height:100%">
 <div class="bd" style="position:relative;background:#fff;display:flex;align-items:center;justify-content:center">
   <div style="position:relative;width:86%">
     <img src="{L}ncl-horizontal-full-colour.png" style="width:100%" alt="">
     <div class="abs" style="left:6%;top:-17%;width:5mm;height:5mm;border-radius:50%;background:var(--navy);color:#fff;font:700 7pt/5mm Montserrat;text-align:center">1</div>
     <div class="abs" style="left:48%;top:-17%;width:5mm;height:5mm;border-radius:50%;background:var(--navy);color:#fff;font:700 7pt/5mm Montserrat;text-align:center">2</div>
     <div class="abs" style="left:48%;top:104%;width:5mm;height:5mm;border-radius:50%;background:var(--navy);color:#fff;font:700 7pt/5mm Montserrat;text-align:center">3</div>
     <div class="abs" style="left:96%;top:104%;width:5mm;height:5mm;border-radius:50%;background:var(--navy);color:#fff;font:700 7pt/5mm Montserrat;text-align:center">4</div>
   </div>
 </div>
 <div>
  <h3>Anatomy</h3>
  <ul>
   <li><b>1 · Symbol.</b> Eight swept petals in four mirrored pairs, radiating from a central gap. Stands alone as the app icon and favicon.</li>
   <li><b>2 · Wordmark.</b> NEW CITY LIGHT in a wide, softly rounded display face, drawn as artwork.</li>
   <li><b>3 · Tagline.</b> LIGHTING THE WAY in widely tracked, light capitals.</li>
   <li><b>4 · ® mark.</b> Always reproduced with the logo; never removed or resized separately.</li>
  </ul>
  <div class="card" style="margin-top:4mm"><h3>Files</h3><p style="margin:0;font-size:7pt">brand/logos/png/ncl-horizontal-*.png (5413 px wide)<br>brand/logos/vector/ncl-stacked-*.svg, ncl-symbol-*.svg</p></div>
 </div>
</div>'''), pid='logo1')

def lk(tile, title, text):
    return f'<div style="display:grid;grid-template-columns:1.25fr 1fr;column-gap:5mm;min-height:0">{tile}<div style="padding-top:2mm"><h3>{title}</h3><p>{text}</p></div></div>'
add('02 Logo', head('02 · Logo', 'Lockups', 'Four approved forms. Choose by space and language, never by taste.') + body(f'''
<div class="grid g2" style="height:100%;grid-template-rows:1fr 1fr;column-gap:9mm;row-gap:6mm">
 {lk(f'<div class="tile bd"><img src="{L}ncl-horizontal-full-colour.png" style="max-width:88%" alt=""></div>','Horizontal · EN','Default for stationery, documents, web headers and signage.')}
 {lk(f'<div class="tile bd"><img src="{L}ncl-arabic-navy.png" style="max-width:80%" alt=""></div>','Arabic lockup','Pairs with the English logo on bilingual stationery, or leads Arabic-only material. Sits on the right.')}
 {lk(f'<div class="tile bd"><img src="{V}ncl-stacked-on-light.svg" style="max-width:62%;max-height:84%" alt=""></div>','Stacked','For square and portrait spaces: bags, packaging, covers, stamps. Vector artwork.')}
 {lk(f'<div class="tile bd" style="background:var(--tint)"><img src="{L}ncl-app-icon-navy.png" style="max-width:none;max-height:none;height:78%" alt=""></div>','Symbol / app icon','When the name is already present or space is tight: avatars, favicons, patterns, embossing.')}
</div>'''), pid='logo2')

add('02 Logo', head('02 · Logo', 'Clear space &amp; minimum size', 'Keep a margin equal to <b>x</b>, the height of the capital letters in the wordmark, clear on all sides. Below the minimum widths, switch to the symbol alone.') + body(f'''
<div class="grid" style="grid-template-columns:1.5fr 1fr;column-gap:10mm;height:100%">
 <div class="bd" style="position:relative;background:#fff;display:flex;align-items:center;justify-content:center">
  <div style="position:relative;padding:7mm;border:.35mm dashed var(--orange-text)">
   <img src="{L}ncl-horizontal-full-colour.png" style="width:110mm;max-width:none;max-height:none" alt="">
   <div class="abs" style="left:0;top:0;width:7mm;height:7mm;background:rgba(243,107,36,.18);display:flex;align-items:center;justify-content:center;font:800 8pt Montserrat;color:var(--orange-text)">x</div><div class="abs" style="right:0;top:0;width:7mm;height:7mm;background:rgba(243,107,36,.18);display:flex;align-items:center;justify-content:center;font:800 8pt Montserrat;color:var(--orange-text)">x</div><div class="abs" style="left:0;bottom:0;width:7mm;height:7mm;background:rgba(243,107,36,.18);display:flex;align-items:center;justify-content:center;font:800 8pt Montserrat;color:var(--orange-text)">x</div><div class="abs" style="right:0;bottom:0;width:7mm;height:7mm;background:rgba(243,107,36,.18);display:flex;align-items:center;justify-content:center;font:800 8pt Montserrat;color:var(--orange-text)">x</div>
  </div>
 </div>
 <div>
  <h3>Minimum size · shown at actual size</h3>
  <div style="display:flex;align-items:flex-end;gap:10mm;margin:3mm 0 2mm">
   <div><img src="{L}ncl-horizontal-full-colour.png" style="width:40mm" alt=""><div class="cap" style="margin-top:1.5mm">Print: 40 mm wide<br>Screen: 160 px wide</div></div>
   <div><img src="{V}ncl-symbol-orange.svg" style="width:8mm" alt=""><div class="cap" style="margin-top:1.5mm">Symbol only:<br>8 mm / 20 px</div></div>
  </div>
  <div class="card" style="margin-top:6mm"><h3>Why 40 mm?</h3><p style="margin:0">The tagline is the first element to break up. Below about 40 mm its capitals fall under 2 pt and fill in when printed. These minimums are our recommendation; confirm on a printed proof.</p></div>
  <ul style="margin-top:4mm"><li>Never place text or graphics inside the clear space.</li><li>Align the logo to the page margin, not to an arbitrary position.</li></ul>
 </div>
</div>'''), pid='logo3')

def vtile(bg, img, label, fg='#fff', extra=''):
    return f'<div class="tile" style="background:{bg};height:100%;{extra}"><img src="{img}" style="max-width:76%;max-height:58%" alt=""><div class="lbl" style="color:{fg}">{label}</div></div>'
add('02 Logo', head('02 · Logo', 'Colour versions', 'Choose the version that gives the strongest contrast with the background. Full colour is for white and very light surfaces only.') + body(f'''
<div class="grid g3" style="height:100%;grid-template-rows:1fr 1fr">
 {vtile('#FFFFFF', L+'ncl-horizontal-full-colour.png', 'Full colour · on white', '#5E6B76', 'border:.25mm solid var(--line)')}
 {vtile('#0F1E2A', L+'ncl-horizontal-on-dark.png', 'On dark · on navy', '#9fb0bd')}
 {vtile('#F36B24', L+'ncl-horizontal-mono-white.png', 'Mono white · on orange', '#0F1E2A')}
 {vtile('#E6E8EA', L+'ncl-horizontal-mono-navy.png', 'Mono navy · on light grey', '#5E6B76')}
 {vtile('#303E4A', L+'ncl-horizontal-on-dark.png', 'On dark · on slate', '#c5d0d8')}
 {vtile('#FFFFFF', L+'ncl-horizontal-mono-black.png', 'One colour black · stamps, fax, newsprint', '#5E6B76', 'border:.25mm solid var(--line)')}
</div>'''), pid='logo4')

def mtile(inner, label, bg='#fff', extra=''):
    return f'<div class="tile bd" style="background:{bg};height:100%;{extra}">{inner}<div class="x">×</div><div class="lbl" style="color:#5E6B76;left:3mm;right:3mm;bottom:2.4mm;font-size:5.6pt">{label}</div></div>'
LOGO = L + 'ncl-horizontal-full-colour.png'
add('02 Logo', head('02 · Logo', 'What not to do', 'These distortions weaken recognition. If a layout seems to need one of them, change the layout.') + body(f'''
<div class="grid g4" style="height:100%;grid-template-rows:1fr 1fr;row-gap:4mm">
 {mtile(f'<img src="{LOGO}" style="max-width:70%;transform:scaleX(1.45)" alt="">','Don’t stretch or squash')}
 {mtile(f'<img src="{LOGO}" style="max-width:70%;transform:rotate(-14deg)" alt="">','Don’t rotate')}
 {mtile(f'<img src="{LOGO}" style="max-width:76%;filter:hue-rotate(185deg) saturate(1.4)" alt="">','Don’t recolour outside the palette')}
 {mtile(f'<img src="{LOGO}" style="max-width:76%;filter:drop-shadow(0 .9mm .9mm rgba(0,0,0,.55))" alt="">','Don’t add shadows, glows or bevels')}
 {mtile(f'<img src="{L}ncl-horizontal-mono-navy.png" style="max-width:76%" alt="">','Don’t use low-contrast backgrounds', '#303E4A')}
 {mtile(f'<img src="{LOGO}" style="max-width:76%;transform:scaleX(-1)" alt="">','Don’t mirror or flip')}
 {mtile(f'<div style="position:absolute;inset:0;background:url({R}post-city.jpg) center/cover"></div><img src="{LOGO}" style="max-width:76%;position:relative" alt="">','Don’t place on busy photography')}
 {mtile(f'<div style="display:flex;align-items:center;gap:2mm"><img src="{V}ncl-symbol-orange.svg" style="width:9mm" alt=""><span style="font:800 12pt Arial,Helvetica,sans-serif;color:var(--navy)">NEW CITY LIGHT</span></div>','Don’t retype the wordmark in another font')}
</div>'''), pid='logo5')

# ------------------------------------------------------------------ 03 COLOUR & TYPE
add('03 Colour & type', divider('03', 'Colour &amp; typography', 'A small palette used with discipline, and the type families that carry the voice.'), kind='dark', foot=False, pid='s3')

def sw(bg, fg, name, hexv, rgb, cmyk, role, h='100%', extra=''):
    return f'<div class="sw" style="background:{bg};color:{fg};padding:4.5mm;height:{h};{extra}"><div class="nm">{name}</div><div class="hx">{hexv}</div><div class="vl">RGB {rgb}<br>CMYK ≈ {cmyk}<br>{role}</div></div>'
add('03 Colour & type', head('03 · Colour', 'Palette', 'Orange is the light; navy is the night it shines in. Navy and off-white carry most surfaces, orange is the accent that draws the eye.') + body(f'''
<div style="display:grid;grid-template-columns:1.25fr 1.25fr 1fr 1fr;column-gap:4mm;height:76mm">
 {sw('#F36B24','#0F1E2A','NCL Orange','#F36B24','243 · 107 · 36','0 · 56 · 85 · 5','Primary accent. Symbol, key shapes, large type.')}
 {sw('#0F1E2A','#FFFFFF','NCL Navy','#0F1E2A','15 · 30 · 42','64 · 29 · 0 · 84','Primary dark. Wordmark, text, backgrounds.')}
 {sw('#F5F5F4','#0F1E2A','Off-white','#F5F5F4','245 · 245 · 244','0 · 0 · 0 · 4','Primary light. Paper and reversed type.', extra='border:.25mm solid var(--line)')}
 {sw('#303E4A','#FFFFFF','Slate','#303E4A','48 · 62 · 74','35 · 16 · 0 · 71','Secondary. Envelopes, cards, pattern base.')}
</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;column-gap:4mm;margin-top:4mm;height:19mm">
 <div style="background:#BD470B;color:#fff;padding:3mm 4mm"><div style="font-weight:800;font-size:8pt">Orange Text</div><div class="hx" style="font-size:7pt;font-weight:600">#BD470B</div><div class="vl" style="font-size:6pt">Small orange text on light backgrounds</div></div>
 <div style="background:#5E6B76;color:#fff;padding:3mm 4mm"><div style="font-weight:800;font-size:8pt">Muted</div><div class="hx" style="font-size:7pt;font-weight:600">#5E6B76</div><div class="vl" style="font-size:6pt">Secondary text, captions</div></div>
 <div style="background:#D9DDE0;color:#0F1E2A;padding:3mm 4mm"><div style="font-weight:800;font-size:8pt">Line</div><div class="hx" style="font-size:7pt;font-weight:600">#D9DDE0</div><div class="vl" style="font-size:6pt">Rules and borders</div></div>
 <div style="background:#F1F2F3;color:#0F1E2A;padding:3mm 4mm"><div style="font-weight:800;font-size:8pt">Tint</div><div class="hx" style="font-size:7pt;font-weight:600">#F1F2F3</div><div class="vl" style="font-size:6pt">Panels and table stripes</div></div>
</div>
<div style="display:flex;height:6mm;margin-top:6mm"><div style="flex:45;background:#0F1E2A"></div><div style="flex:30;background:#F5F5F4;border:.25mm solid var(--line)"></div><div style="flex:15;background:#F36B24"></div><div style="flex:10;background:#303E4A"></div></div>
<div style="display:flex;justify-content:space-between" class="cap"><span>Navy 45%</span><span>Off-white / white 30%</span><span>Orange 15%</span><span>Slate 10%</span></div>
<p class="cap" style="margin-top:2.4mm">Indicative proportions. CMYK values are straight conversions from RGB and are starting points only; match to a printed swatch before approving. Slate and the utility colours were sampled from the approved mockups.</p>
'''), pid='col1')

def cp(fg, bg, label, ratio, verdict, vcls, sample='Aa'):
    return f'<tr><td style="width:24mm"><div style="background:{bg};color:{fg};font-weight:800;font-size:13pt;text-align:center;padding:1.2mm 0;border:.25mm solid var(--line)">{sample}</div></td><td style="font-weight:600">{label}</td><td style="font-weight:800;font-variant-numeric:tabular-nums">{ratio}</td><td><span class="pill {vcls}">{verdict}</span></td></tr>'
add('03 Colour & type', head('03 · Colour', 'Contrast &amp; legibility', 'Measured contrast ratios (WCAG). Orange is bright but not dark: it does not carry small text on white, and white does not carry small text on orange.') + body(f'''
<div class="grid" style="grid-template-columns:1.3fr 1fr;column-gap:10mm">
 <table class="t"><thead><tr><th></th><th>Pairing</th><th>Ratio</th><th>Use</th></tr></thead><tbody>
  {cp('#0F1E2A','#FFFFFF','Navy on white','16.9 : 1','Any size','ok')}
  {cp('#FFFFFF','#0F1E2A','White on navy','16.9 : 1','Any size','ok')}
  {cp('#0F1E2A','#F36B24','Navy on orange','5.6 : 1','Any size','ok')}
  {cp('#F36B24','#0F1E2A','Orange on navy','5.6 : 1','Any size','ok')}
  {cp('#FFFFFF','#303E4A','White on slate','11.0 : 1','Any size','ok')}
  {cp('#BD470B','#FFFFFF','Orange Text on white','5.2 : 1','Any size','ok')}
  {cp('#F36B24','#FFFFFF','Orange on white','3.0 : 1','Large type ≥ 18 pt bold / graphics only','warn')}
  {cp('#FFFFFF','#F36B24','White on orange','3.0 : 1','Large type ≥ 18 pt bold / graphics only','warn')}
  {cp('#F5F5F4','#F36B24','Off-white on orange','2.8 : 1','Logo and graphics only','bad')}
 </tbody></table>
 <div>
  <div class="card"><h3>Rules of thumb</h3>
   <ul>
    <li>Text on an orange surface: <b>navy</b>. The white logo on orange is the one exception, because it is artwork.</li>
    <li>Orange type on white: only for headlines at 18 pt bold or larger. Otherwise use Orange Text <b>#BD470B</b>.</li>
    <li>Footer and caption text on navy: off-white at 75% or stronger.</li>
    <li>Never put orange text on slate below 14 pt (3.6 : 1).</li>
   </ul></div>
  <p class="cap" style="margin-top:3mm">Ratios calculated from the hex values on the palette page. WCAG AA requires 4.5 : 1 for normal text and 3 : 1 for large text.</p>
 </div>
</div>'''), pid='col2')

add('03 Colour & type', head('03 · Typography', 'Primary typeface: Montserrat', 'A geometric sans with a wide range of weights. It is already used across the presentation, business cards and brochure, and it is free (SIL Open Font Licence) so every supplier can install it.') + body(f'''
<div class="grid" style="grid-template-columns:.85fr 1.5fr;column-gap:10mm;height:100%">
 <div style="background:var(--navy);color:#fff;position:relative;overflow:hidden">
  <div class="abs pat-slate" style="inset:0"></div>
  <div class="abs" style="left:7mm;top:5mm;font-weight:800;font-size:96pt;line-height:1;color:#fff">Aa</div>
  <div class="abs" style="left:7mm;bottom:20mm;font-weight:800;font-size:13pt">Montserrat</div>
  <div class="abs" style="left:7mm;bottom:7mm;right:7mm;font-weight:400;font-size:7.4pt;line-height:1.6;color:#c9d1d8;letter-spacing:.06em">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 &amp; @ + % ( ) – . ,</div>
 </div>
 <table class="t"><thead><tr><th style="width:24mm">Weight</th><th>Sample</th><th style="width:44mm">Use</th></tr></thead><tbody>
  <tr><td>Light 300</td><td style="font-weight:300;font-size:11pt">Lighting the way</td><td>Contact details, captions on dark</td></tr>
  <tr><td>Regular 400</td><td style="font-weight:400;font-size:11pt">Lighting the way</td><td>Body text</td></tr>
  <tr><td>Medium 500</td><td style="font-weight:500;font-size:11pt">Lighting the way</td><td>Table values, form entries</td></tr>
  <tr><td>SemiBold 600</td><td style="font-weight:600;font-size:11pt">Lighting the way</td><td>Labels, names, small caps</td></tr>
  <tr><td>Bold 700</td><td style="font-weight:700;font-size:11pt">Lighting the way</td><td>Headings, emphasis</td></tr>
  <tr><td>ExtraBold 800</td><td style="font-weight:800;font-size:11pt">LIGHTING THE WAY</td><td>Titles and display capitals</td></tr>
 </tbody></table>
</div>'''), pid='ty1')

add('03 Colour & type', head('03 · Typography', 'Arabic &amp; display faces', 'English and Arabic are set side by side on almost everything we produce. Arabic is never an afterthought: same hierarchy, same colour, same alignment rules, mirrored.') + body(f'''
<div class="grid g3" style="height:92mm">
 <div class="card" style="border-left-color:var(--navy)"><h3>Arabic · brand face</h3>
  <div style="font-weight:800;font-size:15pt;margin-bottom:2mm">GE SS Two</div>
  <p>Used in the current company brochure (Light, Medium and Bold). It is a commercial typeface: make sure the licence covers every supplier and screen use.</p>
  <h3 style="margin-top:4mm">Arabic · used in these templates</h3>
  <div style="font-weight:800;font-size:13pt;margin-bottom:1.5mm">Noto Kufi Arabic</div>
  <p>Open-source (SIL OFL), geometric and wide, the closest free match to the Arabic logo. Used for every Arabic line in the stationery files here.</p>
 </div>
 <div class="card" style="border-left-color:var(--navy)"><h3>Arabic sample</h3>
  <div class="ar" style="font-weight:800;font-size:20pt;line-height:1.5;text-align:left">إنارة المدينة الجديدة</div>
  <div class="ar" style="font-weight:700;font-size:12pt;line-height:1.8;text-align:left;margin-top:2mm">مدينة جديدة. إنارة جديدة. منظور جديد.</div>
  <div class="ar" style="font-weight:400;font-size:9pt;line-height:1.9;text-align:left;margin-top:3mm;color:#3b4a56">نقدم لعملائنا حلولاً هندسية شاملة تبدأ من الفكرة وحتى التسليم النهائي للمشروع.</div>
  <p class="cap" style="margin-top:3mm">Set Arabic about 1 pt larger than the English beside it, with generous leading (1.7–1.9).</p>
 </div>
 <div class="card" style="border-left-color:var(--orange)"><h3>Display · logo and campaigns</h3>
  <div style="font-weight:800;font-size:15pt;margin-bottom:2mm">Nasalization</div>
  <p>The wordmark and the campaign headlines on the existing posts use a wide, rounded techno face that matches Nasalization (Heavy and Extended Light, as embedded in the brochure). It is not bundled here.</p>
  <p><b>Check before reuse:</b> Nasalization is free for personal use only. Commercial campaigns need a licence, or the headlines should be supplied as outlined artwork.</p>
  <p style="margin:0">The stationery in this pack does not need it: the logo is artwork.</p>
 </div>
</div>
<div class="abs" style="left:0;right:0;bottom:0;height:34mm;background:var(--navy);color:#fff;display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:10mm;padding:5mm 8mm;align-items:center">
 <div><div style="font-weight:700;font-size:5.8pt;letter-spacing:.16em;color:var(--orange);text-transform:uppercase;display:flex;justify-content:space-between"><span>Address</span><span class="ar" style="letter-spacing:0;font-size:7pt">العنوان</span></div><div style="font-size:8pt;margin-top:1mm">Baghdad – Al-Mansour – Al-Dawoodi, Iraq</div><div class="ar" style="font-size:8.4pt;text-align:left;margin-top:.6mm">بغداد – المنصور – الداوودي</div></div>
 <div><div style="font-weight:700;font-size:5.8pt;letter-spacing:.16em;color:var(--orange);text-transform:uppercase;display:flex;justify-content:space-between"><span>Phone</span><span class="ar" style="letter-spacing:0;font-size:7pt">الهاتف</span></div><div style="font-size:8pt;margin-top:1mm">+964 783 577 6393</div></div>
 <div class="cap" style="color:#9fb0bd;font-size:7pt;line-height:1.6">Pairing pattern: English label left, Arabic label right on the same line; English value left-aligned, Arabic value right-aligned directly beneath.</div>
</div>'''), pid='ty2')

def hrow(role, face, size, case, colour):
    return f'<tr><td style="font-weight:700">{role}</td><td>{face}</td><td>{size}</td><td>{case}</td><td>{colour}</td></tr>'
add('03 Colour & type', head('03 · Typography', 'Hierarchy for documents', 'One consistent scale for letters, quotations and printed forms. Sizes are for A4 at 100%.') + body(f'''
<div class="grid" style="grid-template-columns:1.35fr 1fr;column-gap:10mm">
 <table class="t"><thead><tr><th>Role</th><th>Face · weight</th><th>Size / leading</th><th>Case</th><th>Colour</th></tr></thead><tbody>
  {hrow('Document title','Montserrat 800','19–24 pt / 1.1','CAPS · tracked 0.2 em','Navy')}
  {hrow('Arabic title','Noto Kufi 800','17–22 pt / 1.3','—','Orange')}
  {hrow('Heading','Montserrat 700','11–13 pt / 1.25','Sentence','Navy')}
  {hrow('Body','Montserrat 400','9–9.5 pt / 1.6','Sentence','Navy')}
  {hrow('Table text','Montserrat 400 / 500','7.8–8.4 pt / 1.3','Sentence','Navy')}
  {hrow('Label','Montserrat 700','5.6–6.4 pt / tracked 0.14 em','CAPS','Orange Text / Muted')}
  {hrow('Caption','Montserrat 400','6.3–7 pt / 1.5','Sentence','Muted')}
  {hrow('Contact details','Montserrat 400','6.8 pt / 1.55','Sentence','Off-white on navy')}
  {hrow('Arabic body','Noto Kufi 400','body + 1 pt / 1.8','—','Navy')}
 </tbody></table>
 <div class="bd" style="padding:7mm;background:#fff">
  <div style="font-weight:800;font-size:15pt;letter-spacing:.18em;color:var(--navy)">QUOTATION</div>
  <div class="ar" style="font-weight:800;font-size:13pt;color:var(--orange);text-align:left;direction:rtl">عرض سعر</div>
  <div style="height:.9mm;width:16mm;background:var(--orange);margin:3mm 0 4mm"></div>
  <div style="font-weight:700;font-size:10.5pt;margin-bottom:1.5mm">Lighting design and supply proposal</div>
  <p style="font-size:8.6pt">Thank you for the opportunity to support your project. We are pleased to submit our proposal covering design, supply and commissioning.</p>
  <div style="font-weight:700;font-size:5.8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-text);margin-top:3mm">Prepared by</div>
  <div style="font-weight:500;font-size:8pt;border-bottom:.25mm solid var(--line);padding:1mm 0">Full Name</div>
  <p class="cap" style="margin-top:3mm">Live example of the scale on the left.</p>
 </div>
</div>'''), pid='ty3')

# ------------------------------------------------------------------ 04 GRAPHIC LANGUAGE
add('04 Graphic language', divider('04', 'Graphic language', 'The symbol as a device, the petal pattern, imagery and icons.'), kind='dark', foot=False, pid='s4')

add('04 Graphic language', head('04 · Graphic language', 'Symbol &amp; pattern', 'The symbol can be enlarged and cropped as a graphic device. The pattern is a quiet, tone-on-tone texture made of the same swept petal, used to give flat colour some depth.') + body(f'''
<div class="grid g4" style="height:62mm">
 <div class="tile" style="background:#0F1E2A"><img src="{V}ncl-symbol-orange.svg" style="position:absolute;left:-18%;top:-22%;width:120%;max-width:none;max-height:none;opacity:1" alt=""><div class="lbl" style="color:#9fb0bd">Symbol cropped · navy</div></div>
 <div class="tile pat-orange-dark" style="background-color:#F36B24;background-size:12mm 9.8mm"><div class="lbl" style="color:#0F1E2A">Pattern · on orange</div></div>
 <div class="tile pat-slate" style="background-color:#303E4A;background-size:12mm 9.8mm"><div class="lbl" style="color:#c5d0d8">Pattern · on slate</div></div>
 <div class="tile pat-navy" style="background-color:#0F1E2A;background-size:12mm 9.8mm"><div class="lbl" style="color:#9fb0bd">Pattern · on navy</div></div>
</div>
<div class="grid g3" style="margin-top:7mm">
 <div><h3>Symbol device</h3><ul><li>Crop at the page edge, never inside a box.</li><li>One large symbol per layout.</li><li>Orange on navy, white on orange, navy on white.</li></ul></div>
 <div><h3>Pattern</h3><ul><li>Contrast between pattern and ground stays below about 11%.</li><li>Never behind running text; use on bands, flaps and closed surfaces.</li><li>Files: brand/patterns/*.svg (seamless tile).</li></ul></div>
 <div class="card"><h3>Note</h3><p style="margin:0">The pattern tile here is rebuilt from the approved card and envelope mockups. If the original pattern artwork exists, drop it into <b>brand/patterns</b> and rebuild: nothing else changes.</p></div>
</div>'''), pid='gl1')

add('04 Graphic language', head('04 · Graphic language', 'Imagery', 'Night, architecture, warm light. Photography should feel like the moment a space comes alive: deep navy shadows, glowing amber light, clean geometry.') + body(f'''
<div class="grid" style="grid-template-columns:repeat(4,1fr);height:68mm;column-gap:4mm">
 <div class="frame"><img src="{R}post-pathway.jpg" alt=""></div><div class="frame"><img src="{R}post-wall.jpg" alt=""></div><div class="frame"><img src="{R}post-linear.jpg" alt=""></div><div class="frame"><img src="{R}post-downlight.jpg" alt=""></div>
</div>
<p class="cap" style="margin:1.6mm 0 5mm">Existing campaign visuals supplied with the project.</p>
<div class="grid g2">
 <div class="card" style="border-left-color:#1f8a4c"><h3>Do</h3><ul><li>Dusk and night scenes, light as the hero.</li><li>Warm light (about 2700–3000 K) against deep blue-black shadow.</li><li>Clean architecture; one clear subject per frame.</li><li>Leave calm space for headline and logo.</li></ul></div>
 <div class="card" style="border-left-color:#C0392B"><h3>Don’t</h3><ul><li>Flat daylight stock photography or cold, clinical white light.</li><li>Cluttered frames where the logo has to fight the picture.</li><li>Heavy filters, clip-art, or lens-flare effects.</li><li>Placing the logo directly on bright, busy areas; use a navy overlay first.</li></ul></div>
</div>'''), pid='gl2')

add('04 Graphic language', head('04 · Graphic language', 'App icon &amp; avatars', 'Orange symbol on a navy rounded square is the primary icon. Navy is the colour that separates NCL from other orange “spark” marks, so the white-on-orange tile is retired for icons and avatars.') + body(f'''
<div class="grid" style="grid-template-columns:1fr 1.2fr;column-gap:10mm;height:100%">
 <div class="grid g2" style="row-gap:5mm;grid-template-rows:1fr 1fr">
  <div class="tile bd" style="background:var(--tint)"><img src="{L}ncl-app-icon-navy.png" style="width:44mm;max-width:none;max-height:none" alt=""><div class="lbl" style="color:#5E6B76">App icon · primary · navy</div></div>
  <div class="tile bd" style="background:var(--tint)"><div style="width:36mm;height:36mm;border-radius:50%;background:var(--navy);display:flex;align-items:center;justify-content:center"><img src="{V}ncl-symbol-orange.svg" style="width:20mm;max-width:none;max-height:none" alt=""></div><div class="lbl" style="color:#5E6B76">Avatar · circle</div></div>
  <div class="tile bd" style="background:var(--tint)"><div style="display:flex;align-items:flex-end;gap:5mm"><img src="{L}ncl-app-icon-navy.png" style="width:16mm;max-width:none;max-height:none;border-radius:0" alt=""><img src="{L}ncl-app-icon-navy.png" style="width:9mm;max-width:none;max-height:none" alt=""><img src="{L}ncl-app-icon-navy.png" style="width:5mm;max-width:none;max-height:none" alt=""></div><div class="lbl" style="color:#5E6B76">Favicon · 64 / 32 / 16</div></div>
  <div class="tile bd" style="background:#fff"><div style="width:36mm;height:36mm;background:#fff;border:.5mm solid var(--line,#d9dee2);border-radius:50%;display:flex;align-items:center;justify-content:center"><img src="{V}ncl-symbol-orange.svg" style="width:20mm;max-width:none;max-height:none" alt=""></div><div class="lbl" style="color:#5E6B76">Avatar · light (secondary)</div></div>
 </div>
 <div class="frame" style="position:relative"><img src="{R}mock-phone-icon.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#fff">Existing mockup (orange tile, now retired): update it with the navy icon</div></div>
</div>'''), pid='gl3')

# ------------------------------------------------------------------ 05 STATIONERY
add('05 Stationery', divider('05', 'Stationery &amp; applications', 'Letterhead, envelopes, quotation, stamp, bag and email signature, with the specs a printer needs.'), kind='dark', foot=False, pid='s5')

def thumb(src, label, ar='auto', bd=True, bg='#fff', fit='contain', mh='128mm'):
    return f'<div style="display:flex;flex-direction:column;justify-content:flex-start;min-height:0"><div class="{"bd " if bd else ""}shadowbox" style="background:{bg};min-height:0;display:flex;align-items:center;justify-content:center;padding:2mm"><img src="{src}" style="max-width:100%;max-height:{mh};object-fit:{fit}" alt=""></div><div class="cap" style="margin-top:1.6mm;font-weight:600;letter-spacing:.08em;text-transform:uppercase">{label}</div></div>'
add('05 Stationery', head('05 · Stationery', 'The stationery system', 'One system, built from the logo, the navy footer band, the petal pattern and a restrained use of orange. White, light pages for correspondence; slate and orange for closed surfaces.') + body(f'''
<div class="grid" style="grid-template-columns:1.1fr 1fr;column-gap:8mm;height:100%">
 <div class="frame" style="position:relative"><img src="{R}mock-stationery-set.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#334">Existing mockup: letterhead, envelope, card, badges</div></div>
 <div class="grid" style="grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;column-gap:3.5mm;row-gap:3mm">
  {thumb(D+'01-Letterhead/preview-sample-1.png','Letterhead')}
  {thumb(D+'03-Envelope-Large-C4/preview-2.png','Envelope C4 · back')}
  {thumb(D+'04-Envelope-Small-DL/preview-1.png','Envelope DL · front')}
  {thumb(D+'05-Quotation/preview-sample-1.png','Quotation')}
  {thumb(D+'06-Stamp/NCL-Stamp-round-navy-preview.png','Stamp · round')}
  {thumb(D+'06-Stamp/NCL-Stamp-rect-navy-preview.png','Stamp · rect.')}
  {thumb(D+'07-Plastic-Bag/preview-1.png','Plastic bag')}
  {thumb(D+'02-Email-Signature/preview.png','Email signature')}
 </div>
</div>'''), pid='st0')

def spec(rows):
    return '<table class="t"><tbody>' + ''.join(f'<tr><td style="width:30mm;font-weight:700;color:var(--muted);font-size:6.4pt;letter-spacing:.12em;text-transform:uppercase">{k}</td><td>{v}</td></tr>' for k, v in rows) + '</tbody></table>'

add('05 Stationery', head('05 · Stationery', 'Letterhead', 'A4, bilingual. English logo left, Arabic logo right, a hairline with an orange accent, and the contact data in a navy band at the foot.') + body(f'''
<div class="grid" style="grid-template-columns:84mm 1fr;column-gap:10mm;height:100%">
 {thumb(D+'01-Letterhead/preview-sample-1.png','Sample letter')}
 <div>
 {spec([('Size','A4 · 210 × 297 mm · portrait'),('Margins','20 mm left and right · body starts 45 mm from top · body ends about 265 mm'),('Header','EN logo 64 mm wide at 20 / 14 mm · Arabic logo 10.7 mm tall, right aligned · hairline at 32 mm with a 16 mm orange accent'),('Footer','Navy band 26 mm tall, full bleed, petal pattern at 5% · 1.3 mm orange line on top · three columns: address, phones, email and web · Montserrat 6.8 pt'),('Paper','100–120 gsm uncoated white'),('Print','Offset or digital, 4 colour. Footer band is a full-bleed flood: send the 3 mm bleed file with crop marks'),('Office printing','Desktop printers cannot print to the page edge; use pre-printed stock for letters and the Word template only for files sent as PDF'),('Files','01-Letterhead/ · print PDF with bleed, blank PDF, sample letter, Word template')])}
 </div>
</div>'''), pid='st1')

add('05 Stationery', head('05 · Stationery', 'Envelopes', 'Two sizes, one look. The front is white and writable, with the logos at the top and the contact line above a navy strip. The back follows the approved mockup: slate body, patterned flap, white logo.') + body(f'''
<div class="grid" style="grid-template-columns:1fr 1fr;column-gap:8mm;height:100%">
 <div style="display:grid;grid-template-rows:1fr 1fr;row-gap:4mm">
  <div style="display:grid;grid-template-columns:1fr 1fr;column-gap:4mm;min-height:0">{thumb(D+'03-Envelope-Large-C4/preview-1.png','C4 · front')}{thumb(D+'03-Envelope-Large-C4/preview-2.png','C4 · back')}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;column-gap:4mm;min-height:0">{thumb(D+'04-Envelope-Small-DL/preview-1.png','DL · front')}{thumb(D+'04-Envelope-Small-DL/preview-2.png','DL · back')}</div>
 </div>
 <div>
 {spec([('Large · C4','324 × 229 mm (holds A4 unfolded) · flap along the long edge'),('Small · DL','220 × 110 mm (holds A4 folded in three)'),('Front','White · logo EN top left, Arabic top right · contact line · navy strip with pattern'),('Back','Slate #303E4A · flap in slightly lighter slate with pattern · white logo, centred below the flap'),('Bleed','5 mm in the print file (envelope converters usually ask for 5 mm)'),('Stock','100–120 gsm uncoated; the dark back needs offset or digital flood coverage'),('Cost note','The dark back is the expensive part. If budget is tight: print the white front only and leave the back plain'),('Die-line','Artwork is at finished size. Your envelope manufacturer will place it on their own die-line and may adjust the flap shape'),('Files','03-Envelope-Large-C4/ · 04-Envelope-Small-DL/')])}
 </div>
</div>'''), pid='st2')

add('05 Stationery', head('05 · Stationery', 'Quotation', 'A bilingual A4 form: quotation number, client and project blocks, an itemised table, totals, terms and three signature boxes, including one for the company stamp.') + body(f'''
<div class="grid" style="grid-template-columns:84mm 1fr;column-gap:10mm;height:100%">
 {thumb(D+'05-Quotation/preview-sample-1.png','Sample, illustrative data')}
 <div>
 {spec([('Size','A4 · 210 × 297 mm · same header and footer as the letterhead'),('Fields','Quotation no., date, valid until, prepared by, currency, payment terms · client company, attention, phone · project name, location, reference'),('Table','7 item lines · No., description, unit, qty, unit price, total · navy header, light row stripes'),('Totals','Subtotal, discount, tax / VAT, grand total in a navy block'),('Signatures','Prepared by · Approved by · Company stamp'),('Terms','Four default lines. They are placeholders: replace with NCL’s legal wording'),('Excel version','18 lines, discount % and tax % cells, all totals as formulas; prints on one A4 page'),('Files','05-Quotation/ · blank PDF (print with bleed), sample PDF, Excel template')])}
 <p class="cap" style="margin-top:3mm">The sample figures are invented for illustration. The Excel file has been checked: 2 × 10 + 1 × 5 = 25.00, less 10% discount, plus 5% tax = 23.625.</p>
 </div>
</div>'''), pid='st3')

add('05 Stationery', head('05 · Stationery', 'Company stamp', 'One-colour vector stamps with the text converted to outlines: a round seal and a rectangular address stamp. Both carry English and Arabic.') + body(f'''
<div class="grid" style="grid-template-columns:1fr 1.3fr 1fr;column-gap:8mm;height:84mm">
 <div class="tile bd" style="background:#fff"><img src="{D}06-Stamp/NCL-Stamp-round-navy-preview.png" style="max-width:82%;max-height:90%" alt=""><div class="lbl" style="color:#5E6B76">Round · Ø 42 mm</div></div>
 <div class="tile bd" style="background:#fff"><img src="{D}06-Stamp/NCL-Stamp-rect-navy-preview.png" style="max-width:86%;max-height:90%" alt=""><div class="lbl" style="color:#5E6B76">Rectangular · 69 × 33 mm</div></div>
 <div>
  {spec([('Colour','One colour. Navy or the traditional blue for ink; black for the artwork you send to the stamp maker'),('Line weight','Thin lines 0.22–0.28 mm; heavy outer ring 0.8 mm'),('Text','Montserrat and Noto Kufi Arabic, outlined: no fonts to install'),('Formats','SVG and PDF, black and navy'),('Legal','Check whether Iraqi or customs authorities require registered wording such as a licence number. None has been added')])}
 </div>
</div>'''), pid='st4')

add('05 Stationery', head('05 · Stationery', 'Plastic bag', 'A solid orange carrier bag: white stacked logo and the Arabic statement on the front, symbol and contact details on the back, with the petal pattern as a dark-orange tone-on-tone texture.') + body(f'''
<div class="grid" style="grid-template-columns:44mm 44mm 1fr;column-gap:8mm;height:100%">
 {thumb(D+'07-Plastic-Bag/preview-1.png','Front')}
 {thumb(D+'07-Plastic-Bag/preview-2.png','Back')}
 <div>
  {spec([('Flat size','350 × 450 mm. Assumed: confirm gusset, film width and print repeat with the bag maker'),('Handle','Die-cut handle 150 × 32 mm, 48 mm from the top edge; top 30 mm is the heat-seal hem: no artwork'),('Film','Orange film or white film flooded with orange. White print for the logo'),('Colours','Orange (match to #F36B24), white, and optionally a dark orange for the pattern: 3 spots'),('Safe area','Keep text and logos 15 mm inside the edges and below the handle'),('Files','07-Plastic-Bag/ · artwork PDF and a version with the die-cut and safe-area guides shown')])}
 </div>
</div>'''), pid='st5')

add('05 Stationery', head('05 · Stationery', 'Email signature', 'A clean table-based HTML signature: logo, name and role, then phone, email, web and address, with the Arabic brand statement below.') + body(f'''
<div class="grid" style="grid-template-columns:1fr 1fr;column-gap:10mm;height:100%">
 <div class="bd" style="background:#fff;padding:6mm;display:flex;align-items:center;justify-content:center"><img src="{D}02-Email-Signature/preview.png" style="max-width:100%;max-height:100%" alt=""></div>
 <div>
  {spec([('Width','About 520 px; the logo is 210 px wide, supplied at 640 px for sharp screens'),('Fonts','Montserrat falls back to Segoe UI / Arial, as most email programs cannot load web fonts'),('Colours','Labels use Orange Text #BD470B; name and details navy'),('Images','Gmail and Outlook.com need the logo hosted at a public https address; edit the image path in the HTML first. An embedded-image version is included for Apple Mail and Outlook desktop'),('Rules','No photos, quotes, disclaimers in colour or animated banners; one logo only'),('Files','02-Email-Signature/ · HTML, embedded-image HTML, logo PNG')])}
 </div>
</div>'''), pid='st6')

add('05 Stationery', head('05 · Applications', 'Already delivered: cards, badges, sets', 'Existing identity work supplied with this project. These pieces set the colours and mood the new stationery follows.') + body(f'''
<div class="grid" style="grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;column-gap:5mm;row-gap:5mm;height:100%">
 <div class="frame" style="grid-row:span 2;position:relative"><img src="{R}mock-business-cards.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#fff">Business cards · orange front, slate back</div></div>
 <div class="frame" style="position:relative"><img src="{R}mock-id-badge.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#fff">ID badge</div></div>
 <div class="frame" style="position:relative"><img src="{R}mock-sling-bag.jpg" alt=""><div class="cap" style="position:absolute;left:3mm;bottom:2mm;color:#fff">Merchandise</div></div>
</div>'''), pid='st7')

add('05 Stationery', head('05 · Applications', 'The brand in the world', 'Vehicles, containers, signage, window graphics and workwear: the same orange, navy and white, with the logo kept large and uncluttered.') + body(f'''
<div class="grid g3" style="grid-template-rows:1fr 1fr;column-gap:4mm;row-gap:4mm;height:100%">
 <div class="frame" style="position:relative"><img src="{R}mock-truck.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-container.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-storefront-sign.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-window-graphics.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}mock-apparel.jpg" alt=""></div>
 <div class="frame" style="position:relative"><img src="{R}post-lighting-way.jpg" style="object-position:center 30%" alt=""></div>
</div>'''), pid='st8')

# ------------------------------------------------------------------ REFERENCE
add('Reference', head('Reference', 'Company data &amp; open items', 'Everything printed in this pack comes from one list. Change it here first, then rebuild.') + body(f'''
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
   <li><b>Logo files.</b> In the supplied full-colour and single-colour PNGs the ® ring is a hairline displaced to the right of the “R”. This pack rebuilds it from the correct on-dark file. Please fix the master artwork.</li>
   <li><b>Website.</b> The brochure says <i>dulights.com</i> (also its email); the business card mockup says <i>www.NewCityLight.com</i>. One has to win.</li>
   <li><b>Arabic spelling.</b> The Arabic logo reads «انارة» (no hamza); the brochure body text writes «إنارة». Decide once and use it everywhere.</li>
   <li><b>Experience claim.</b> The brochure says “more than 30 years” but its timeline starts in 1998 (28 years). Don’t print either on stationery until settled.</li>
   <li><b>Fonts.</b> GE SS Two and Nasalization are commercial or personal-use only; check licences. Montserrat and Noto Kufi are free.</li>
   <li><b>Colours.</b> CMYK values are starting points. Approve a printed swatch (and Pantone match if you use spot colour).</li>
   <li><b>Pattern.</b> Rebuilt from the mockups. Replace with the original if one exists.</li>
   <li><b>Symbol likeness.</b> Alone, the symbol can read like other orange “spark” marks used by tech brands. Navy icon adopted; colour options and symbol concepts (including a geometric direction) are in 08-Symbol-Concepts for NCL to review.</li>
   <li><b>Quotation terms &amp; stamp wording.</b> Placeholders. Legal and registration wording needs NCL’s sign-off.</li>
  </ul>
 </div>
</div>'''), pid='ref')

# back cover
add('', f'''
<div class="abs pat-slate" style="inset:0"></div>
<img class="abs" src="{V}ncl-symbol-orange.svg" style="left:50%;top:50%;transform:translate(-50%,-62%);width:44mm" alt="">
<div class="abs" style="left:0;right:0;top:122mm;text-align:center;font-weight:800;font-size:11pt;letter-spacing:.34em;color:#fff">LIGHTING THE WAY</div>
<div class="abs ar" style="left:0;right:0;top:134mm;text-align:center;font-weight:700;font-size:11pt;color:#aebbc6">ننير الدرب</div>
<div class="abs" style="left:0;right:0;bottom:16mm;text-align:center;font-size:6.6pt;letter-spacing:.18em;color:#7f91a0;font-weight:600;text-transform:uppercase">New City Light · Baghdad · Iraq &nbsp;·&nbsp; Brand Guidelines v1.0 · 2026</div>
''', kind='dark', foot=False, pid='back')

# ------------------------------------------------------------------ assemble
toc_sections = [('01', 'The brand', 's1'), ('02', 'The logo', 's2'), ('03', 'Colour & typography', 's3'), ('04', 'Graphic language', 's4'), ('05', 'Stationery & applications', 's5'), ('', 'Company data & open items', 'ref')]
idx = {p['id']: i + 1 for i, p in enumerate(pages) if p['id']}
toc_rows = ''.join(f'<tr><td style="width:18mm;font-weight:800;font-size:18pt;color:var(--orange-text);padding:5.5mm 2mm">{n}</td><td style="font-weight:700;font-size:13pt">{t}</td><td style="text-align:right;font-weight:600;font-size:11pt;color:var(--muted)">{idx[i]:02d}</td></tr>' for n, t, i in toc_sections)
toc = head('Contents', 'Contents') + body(f'''
<div class="grid" style="grid-template-columns:1.2fr 1fr;column-gap:14mm">
 <table class="t" style="font-size:11pt"><tbody>{toc_rows}</tbody></table>
 <div class="card"><h3>About this book</h3><p>These guidelines describe the New City Light identity as delivered in the rebranding files, and set out the stationery system built from it: letterhead, envelopes, quotation, stamp, plastic bag and email signature.</p><p style="margin:0">Where a value was measured from existing artwork rather than specified by the client (slate colour, pattern, text-safe orange), the page says so.</p></div>
</div>''')
for p in pages:
    if p['html'] == '@@TOC@@': p['html'] = toc

out = []
for n, p in enumerate(pages, 1):
    ft = f'<div class="foot"><span>New City Light &nbsp;·&nbsp; Brand Guidelines</span><span>{p["sec"]} &nbsp;·&nbsp; <b>{n:02d}</b></span></div>' if p['foot'] else ''
    out.append(f'<div class="sheet gp {p["kind"]}" data-w="297" data-h="210">{p["html"]}{ft}</div>')
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>NCL Brand Guidelines</title>
<link rel="stylesheet" href="shared/common.css"><link rel="stylesheet" href="guidelines.css"></head><body>
{chr(10).join(out)}
<script src="shared/common.js"></script></body></html>'''
pathlib.Path('src/brand-guidelines.html').write_text(html)
D0 = 'deliverables/00-Brand-Guidelines'
render.pdf('src/brand-guidelines.html', f'{D0}/NCL-Brand-Guidelines-v1.0.pdf')
print(len(pages), 'pages')
