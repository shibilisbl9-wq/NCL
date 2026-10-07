"""Extract the vector symbol + stacked lockup from the client's Broucher.ai (Illustrator PDF).
Usage: python3 -I make_vectors.py <brochure.svg from `pdftocairo -svg`> <out_dir>"""
import re, sys, os
svg_path, out = sys.argv[1], sys.argv[2]
s = open(svg_path).read()
body_start = s.index('</defs>')
defs = s[:body_start]
body = s[body_start:].split('\n')

# group top-level blocks
blocks, buf, depth = [], [], 0
for ln in body[1:]:
    if ln.startswith('<g'):
        buf = [ln]; depth = 1
        if ln.endswith('/>'): blocks.append(buf); buf = []; depth = 0
        continue
    if depth:
        buf.append(ln)
        if ln.startswith('</g>'): blocks.append(buf); buf = []; depth = 0
        continue
    blocks.append([ln])

sym_blocks = blocks[945:949]      # 4 orange paths = symbol
txt_blocks = blocks[949:954]      # NEW CITY LIGHT / tagline / (R) glyph
ring_block = blocks[954][0]       # circle of the registered mark (stroked path)
sym_paths = [re.search(r' d="([^"]*)"', b[0]).group(1) for b in sym_blocks]

# symbol bbox
nums = lambda d: [float(x) for x in re.findall(r'-?\d+\.?\d*', d)]
xs, ys = [], []
for d in sym_paths:
    n = nums(d); xs += n[0::2]; ys += n[1::2]
x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
w, h = x1 - x0, y1 - y0
print('symbol bbox', x0, y0, w, h)

def symbol_svg(color='#F36B24', pad=0):
    ds = ''.join(f'<path d="{d}"/>' for d in sym_paths)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0-pad:.3f} {y0-pad:.3f} {w+2*pad:.3f} {h+2*pad:.3f}">'
            f'<g fill="{color}" fill-rule="nonzero">{ds}</g></svg>')

# glyph defs needed
txt = '\n'.join('\n'.join(b) for b in txt_blocks)
used = set(re.findall(r'xlink:href="#(glyph-[\d-]+)"', txt))
glyph_defs = ''
for g in used:
    m = re.search(rf'<g id="{g}">.*?</g>', defs, re.S)
    glyph_defs += m.group(0) + '\n'

# text bbox: wordmark spans x 603.4..~811, y ~ 155..188 ; combine with symbol (y 54..~116)
vx0, vy0, vx1, vy1 = 598.0, 48.0, 818.0, 190.0
def stacked_svg(sym='#F36B24', text='#F5F5F4'):
    t = re.sub(r'fill="rgb\([^"]*\)"', f'fill="{text}"', txt)
    t += re.sub(r'stroke="rgb\([^"]*\)"', f'stroke="{text}"', ring_block)
    ds = ''.join(f'<path d="{d}"/>' for d in sym_paths)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="{vx0} {vy0} {vx1-vx0} {vy1-vy0}">'
            f'<defs>{glyph_defs}</defs><g fill="{sym}">{ds}</g>{t}</svg>')

os.makedirs(out, exist_ok=True)
for name, col in [('orange', '#F36B24'), ('navy', '#0F1E2A'), ('white', '#F5F5F4')]:
    open(f'{out}/ncl-symbol-{name}.svg', 'w').write(symbol_svg(col))
open(f'{out}/ncl-stacked-on-dark.svg', 'w').write(stacked_svg('#F36B24', '#F5F5F4'))
open(f'{out}/ncl-stacked-on-light.svg', 'w').write(stacked_svg('#F36B24', '#0F1E2A'))
open(f'{out}/ncl-stacked-mono-white.svg', 'w').write(stacked_svg('#F5F5F4', '#F5F5F4'))
open(f'{out}/ncl-stacked-mono-navy.svg', 'w').write(stacked_svg('#0F1E2A', '#0F1E2A'))
print('ok')
