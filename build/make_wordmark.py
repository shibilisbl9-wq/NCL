"""Cut the NEW CITY LIGHT wordmark (and the tagline line) out of the stacked logo as stand-alone outlined SVGs,
so other artwork can use the real logo letterforms (not a look-alike font)."""
import re, pathlib
src = pathlib.Path('brand/logos/vector/ncl-stacked-on-light.svg').read_text()
defs = src[src.index('<defs>') + 6: src.index('</defs>')]
body = src[src.index('</defs>') + 7:]
groups = re.findall(r'<g fill="#0F1E2A" fill-opacity="1">\n(.*?)</g>', body, re.S)
def build(group_idx, glyph_prefix, vb, col, name):
    use = groups[group_idx]
    ids = set(re.findall(r'#(glyph-[\d-]+)', use))
    d = ''.join(m.group(0) + '\n' for g in sorted(ids) for m in [re.search(rf'<g id="{g}">.*?</g>', defs, re.S)])
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="{vb}">'
           f'<defs>{d}</defs><g fill="{col}">{use}</g></svg>')
    pathlib.Path(f'brand/logos/vector/{name}.svg').write_text(svg)
VB_WORD = '602.8 155.2 210.4 17.4'      # NEW CITY LIGHT
VB_TAG = '604 168.5 201 15.6'           # LIGHTING THE WAY (tracked)
for col, tag in (('#0F1E2A', 'navy'), ('#FFFFFF', 'white'), ('#000000', 'black')):
    build(0, 'glyph-19', VB_WORD, col, f'ncl-wordmark-{tag}')
