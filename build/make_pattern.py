"""Seamless petal tessellation tile (reconstruction of the pattern on the approved card/envelope mockups).
Slanted petals on a half-drop grid. Replace with the original pattern file if you have it."""
import os
OUT = 'brand/patterns'; os.makedirs(OUT, exist_ok=True)
PETAL = ('M 8.2 1.4 C 9.6 -0.5 12.4 -0.5 13.8 1.4 L 20.4 24.8 C 22 30.4 18.8 33 14.4 33 '
         'L 7.6 33 C 3.2 33 0 30.4 1.6 24.8 Z')
W, H, ANG, S = 44, 36, -24, 0.93
def tile(fill, opacity):
    ps = ''
    for (x, y) in [(0, 0), (W / 2, H / 2)]:
        for dx in (-W, 0, W):
            for dy in (-H, 0, H):
                ps += (f'<path transform="translate({x+dx+W/4:.2f} {y+dy+H/4:.2f}) rotate({ANG}) '
                       f'scale({S}) translate(-11 -17)" d="{PETAL}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<g fill="{fill}" fill-opacity="{opacity}">{ps}</g></svg>')
variants = {'on-navy': ('#FFFFFF', 0.05), 'on-slate': ('#FFFFFF', 0.07), 'on-orange': ('#FFFFFF', 0.11),
            'on-white': ('#0F1E2A', 0.035), 'on-orange-dark': ('#0F1E2A', 0.08)}
for k, (c, o) in variants.items():
    open(f'{OUT}/ncl-pattern-{k}.svg', 'w').write(tile(c, o))
