"""Symbol concepts review document (A4 landscape). Run make_symbol_concepts.py first."""
import sys, pathlib; sys.path.insert(0, 'build')
import render
from make_symbol_concepts import CONCEPTS, COLOURWAYS

C = '../brand/concepts/'; L = '../brand/logos/png/'; V = '../brand/logos/vector/'
# honest read of each concept: distance from generic orange 'spark' marks, and trade-offs
NOTES = {
    'a-master':   ('—', 'Current artwork.', 'Alone, at icon size and in orange-on-light, it reads as a generic radiating spark.'),
    'b-lamp':     ('Low', 'Tiny change; keeps all existing artwork recognisable. Gives the symbol a clear meaning: a light source.', 'Still an eight-ray starburst. Helps, does not solve.'),
    'c-two-tone': ('Medium–high', 'Navy ties the symbol to the wordmark. Same geometry, so every existing application still works.', 'Only works in colour. One-colour uses (stamp, embossing, bag) fall back to the master.'),
    'd-pinwheel': ('High', 'Clear break. Reads as motion, energy, a turbine.', 'Can read as a fan, which is the wrong product for a lighting company. Thin bases at small sizes.'),
    'e-beams':    ('High', 'Bold, simple silhouette; survives a 16 px favicon.', 'Loses the radiance of the original. Can read as an hourglass or an “X”.'),
    'f-rising':   ('High', 'Most on-message: light rising over the city, “Lighting the Way”. Distinctive in the lockup.', 'Wide, not square, so weaker as an app icon. Sunrise marks are common in other sectors.'),
    'g-lens':     ('Medium', 'Encloses the mark so it becomes a badge, like a luminaire seen from below. Good for seals and signage.', 'The ring disappears at favicon size, where the likeness is worst.'),
}
pages = []
def page(html, dark=False, num=True):
    pages.append((html, dark, num))
def head(eyebrow, title, lead=''):
    return f'<div class="pad"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1>{f"<p class=lead>{lead}</p>" if lead else ""}</div>'

# cover
page(f'''<div class="abs pat-slate" style="inset:0"></div>
<img class="abs" src="{C}ncl-symbol-c-two-tone-on-dark.svg" style="right:-40mm;top:-30mm;width:230mm;opacity:.12" alt="">
<img class="abs" src="{L}ncl-horizontal-on-dark.png" style="left:26mm;top:28mm;width:70mm" alt="New City Light">
<div class="abs" style="left:26mm;top:92mm;font-weight:800;font-size:38pt;line-height:1.02;color:#fff;letter-spacing:-.015em">Symbol<br>concepts</div>
<div class="abs" style="left:26mm;top:132mm;width:70mm;height:1.1mm;background:var(--orange)"></div>
<div class="abs" style="left:26mm;top:139mm;width:150mm;font-size:9pt;line-height:1.6;color:#c9d1d8">Proposals only. None of these replaces the master artwork until NCL approves it.</div>
<div class="abs" style="left:26mm;top:160mm;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:#7f91a0;font-weight:600">For review &nbsp;·&nbsp; October 2026</div>''', dark=True, num=False)

# the problem + what changed already
page(head('Why', 'The symbol on its own', 'Next to the wordmark the logo is clearly New City Light. On its own (app icon, avatar, favicon) an orange radiating star with an empty centre looks like the “spark” marks used by several tech and AI brands. Most people see the symbol alone at small sizes, so that is where the likeness matters most.') + f'''
<div class="body"><div class="grid" style="grid-template-columns:1fr 1fr 1.25fr;column-gap:9mm;height:100%">
 <div class="tile bd" style="background:var(--tint)"><img src="{L}ncl-app-icon.png" style="width:46mm;max-width:none;max-height:none" alt=""><div class="lbl" style="color:#5E6B76">Before · white on orange · retired</div></div>
 <div class="tile bd" style="background:var(--tint)"><img src="{L}ncl-app-icon-navy.png" style="width:46mm;max-width:none;max-height:none" alt=""><div class="lbl" style="color:#5E6B76">Now · orange on navy · primary</div></div>
 <div><h3>Done already, no logo change</h3><ul>
  <li><b>Navy app icon</b> is now the primary icon and favicon. The guidelines are updated.</li>
  <li><b>White-on-orange tile retired</b> for icons and avatars. It is the closest match to other spark marks.</li>
  <li>Use the <b>full lockup</b> wherever there is room. The likeness only appears when the symbol stands alone.</li></ul>
  <h3 style="margin-top:6mm">Still open</h3><ul>
  <li>Should the symbol itself change? The next pages show six options, all built from the master geometry.</li>
  <li>Before the ® is relied on, have a trademark attorney run a clearance search on whichever symbol is chosen.</li></ul></div>
</div></div>''')

# overview
cells = ''
for k, (name, _, _) in CONCEPTS.items():
    cells += (f'<div style="display:flex;flex-direction:column;min-height:0"><div class="tile bd" style="background:#fff;height:44mm">'
              f'<img src="{C}ncl-symbol-{k}-on-light.svg" style="width:34mm;height:34mm;max-width:none;max-height:none" alt=""></div>'
              f'<div style="display:flex;align-items:flex-end;gap:2.5mm;margin-top:2.5mm"><img src="{C}ncl-icon-{k}-navy.svg" style="width:11mm" alt="">'
              f'<img src="{C}ncl-icon-{k}-navy.svg" style="width:5.6mm" alt=""><img src="{C}ncl-icon-{k}-navy.svg" style="width:2.8mm" alt="">'
              f'<div class="cap" style="margin-left:auto;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--navy)">{name}</div></div></div>')
page(head('Overview', 'Seven symbols side by side', 'The master plus six alternatives. Each one is shown with its navy icon at 64, 32 and 16 px. Judge them at the smallest size first: that is where the problem is.') +
     f'<div class="body"><div class="grid" style="grid-template-columns:repeat(4,1fr);row-gap:7mm;column-gap:6mm">{cells}</div></div>')

# colour-only routes
cw = ''
for k, (name, v, h, bg, _) in COLOURWAYS.items():
    cw += (f'<div style="display:flex;flex-direction:column;min-height:0"><div class="tile{" bd" if bg == "#FFFFFF" else ""}" style="background:{bg};height:46mm">'
           f'<img src="{C}ncl-colour-{k}.svg" style="width:34mm;height:34mm;max-width:none;max-height:none" alt=""></div>'
           f'<div style="display:flex;align-items:flex-end;gap:2.5mm;margin-top:2.5mm"><img src="{C}ncl-colour-{k}-icon.svg" style="width:11mm" alt="">'
           f'<img src="{C}ncl-colour-{k}-icon.svg" style="width:5.6mm" alt=""><img src="{C}ncl-colour-{k}-icon.svg" style="width:2.8mm" alt="">'
           f'<div class="cap" style="margin-left:auto;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--navy)">{name}</div></div></div>')
page(head('Colour only', 'Same symbol, new colours', 'No change to the shape, so every existing file, the stamp and the pattern stay valid. Colour does most of the work on screens and in full-colour print. In one-colour uses (stamp, embossing) the shape is unchanged, so the likeness stays there.') +
     f'<div class="body"><div class="grid" style="grid-template-columns:repeat(3,1fr);row-gap:6mm;column-gap:8mm">{cw}</div></div>')

# one page per concept
for k, (name, desc, _) in CONCEPTS.items():
    if k == 'a-master': continue
    dist, pro, con = NOTES[k]
    page(head(f'Concept {k[0].upper()}', name, desc) + f'''
<div class="body"><div class="grid" style="grid-template-columns:1fr 1fr 1.05fr;column-gap:7mm;height:100%">
 <div class="grid" style="grid-template-rows:1fr 1fr;row-gap:5mm">
  <div class="tile bd" style="background:#fff"><img src="{C}ncl-symbol-{k}-on-light.svg" style="width:42mm;height:42mm;max-width:none;max-height:none" alt=""><div class="lbl" style="color:#5E6B76">On light</div></div>
  <div class="tile" style="background:var(--navy)"><img src="{C}ncl-symbol-{k}-on-dark.svg" style="width:42mm;height:42mm;max-width:none;max-height:none" alt=""><div class="lbl" style="color:#9fb0bd">On navy</div></div>
 </div>
 <div class="grid" style="grid-template-rows:1fr 1fr;row-gap:5mm">
  <div class="tile bd" style="background:var(--tint)"><div style="display:flex;align-items:flex-end;gap:4mm"><img src="{C}ncl-icon-{k}-navy.svg" style="width:30mm" alt=""><img src="{C}ncl-icon-{k}-navy.svg" style="width:8.5mm" alt=""><img src="{C}ncl-icon-{k}-navy.svg" style="width:4.2mm" alt=""></div><div class="lbl" style="color:#5E6B76">App icon · 128 / 32 / 16 px</div></div>
  <div class="tile bd" style="background:#fff;justify-content:flex-start;padding:0 4mm"><div style="display:flex;align-items:center;gap:2.6mm;width:100%">
    <img src="{C}ncl-symbol-{k}-on-light.svg" style="width:13mm;height:13mm;flex:none" alt="">
    <div style="flex:1;overflow:hidden"><img src="{L}ncl-horizontal-full-colour.png" style="width:121%;max-width:none;max-height:none;margin-left:-21%" alt=""></div></div>
    <div class="lbl" style="color:#5E6B76">In the lockup (mock-up, not final spacing)</div></div>
 </div>
 <div>
  <h3>Distance from generic spark marks</h3><div style="font-weight:800;font-size:20pt;color:var(--orange-text);margin-bottom:5mm">{dist}</div>
  <div class="card" style="border-left-color:#1f8a4c;margin-bottom:4mm"><h3>For</h3><p style="margin:0">{pro}</p></div>
  <div class="card" style="border-left-color:#C0392B"><h3>Against</h3><p style="margin:0">{con}</p></div>
  <p class="cap" style="margin-top:4mm">Built from the master petal geometry with no redrawing. A designer should refine curves, weights and spacing before anything is final.</p>
 </div>
</div></div>''')

# recommendation
page(head('Recommendation', 'What we would do', 'Keep the navy icon (done). Then pick one of two routes, depending on how far NCL wants to move.') + f'''
<div class="body"><div class="grid" style="grid-template-columns:1fr 1fr 1fr;column-gap:8mm;height:100%">
 <div><div class="tile bd" style="background:#fff;height:52mm"><img src="{C}ncl-symbol-c-two-tone-on-light.svg" style="width:38mm;height:38mm;max-width:none;max-height:none" alt=""></div>
  <h2 style="margin-top:4mm">Route 1 · Two-tone</h2><p>Lowest risk. Same symbol, recoloured. No reprint of one-colour items (stamp, bag). Business cards, signage and digital pick it up at the next print run.</p></div>
 <div><div class="tile bd" style="background:#fff;height:52mm"><img src="{C}ncl-symbol-f-rising-on-light.svg" style="width:44mm;max-width:none;max-height:none" alt=""></div>
  <h2 style="margin-top:4mm">Route 2 · Rising light</h2><p>A real break, and the closest to “Lighting the Way”. Needs a square icon variant, new lockups and a full artwork update. Only worth it if NCL is still early in the rollout.</p></div>
 <div class="card"><h3>Before deciding</h3><ul>
  <li>Show the shortlist to a few customers at icon size and ask what they see.</li>
  <li>Have a designer refine the chosen option. These are built from the master geometry, not finished artwork.</li>
  <li>Trademark clearance search on the chosen symbol (lighting is a different class from software, but check).</li>
  <li>Update the master files, then rebuild this pack: <i>python3 build/build_all.py</i>.</li></ul></div>
</div></div>''')

out = []
for n, (h, dark, num) in enumerate(pages, 1):
    ft = f'<div class="foot"><span>New City Light &nbsp;·&nbsp; Symbol concepts</span><span><b>{n:02d}</b></span></div>' if num else ''
    out.append(f'<div class="sheet gp {"dark" if dark else ""}" data-w="297" data-h="210">{h}{ft}</div>')
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>NCL Symbol Concepts</title>
<link rel="stylesheet" href="shared/common.css"><link rel="stylesheet" href="guidelines.css">
<style>.tile .lbl{{position:absolute;left:3mm;bottom:2.4mm;font-size:5.6pt;letter-spacing:.14em;text-transform:uppercase;font-weight:600}}</style></head><body>
{chr(10).join(out)}
<script src="shared/common.js"></script></body></html>'''
pathlib.Path('src/symbol-concepts.html').write_text(html)
D = 'deliverables/08-Symbol-Concepts'
render.pdf('src/symbol-concepts.html', f'{D}/NCL-Symbol-Concepts.pdf')
print(len(pages), 'pages')
