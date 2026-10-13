"""Seamless tile of upright rounded triangles on a half-drop (brick) grid - matches the pattern visible on the approved
card/envelope mockups (apex up, staggered rows, tone-on-tone). 12 x 12 unit tile; CSS sets the physical size."""
import os
OUT = 'brand/patterns'; os.makedirs(OUT, exist_ok=True)
T = 12.0                 # tile size (units)
BASE, HGT, R = 4.8, 5.3, 0.75   # triangle base, height, corner radius

def rounded_tri(cx, top):
    """Apex-up isosceles triangle with rounded corners (quadratic corners)."""
    pts = [(cx, top), (cx + BASE / 2, top + HGT), (cx - BASE / 2, top + HGT)]
    d = ''
    n = len(pts)
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        def toward(a, b, r):
            dx, dy = b[0] - a[0], b[1] - a[1]; L = (dx * dx + dy * dy) ** .5
            return (a[0] + dx / L * r, a[1] + dy / L * r)
        r = R * (1.9 if i == 0 else 1.0)          # slightly softer apex
        a = toward(p1, p0, r); b = toward(p1, p2, r)
        d += ('M' if i == 0 else 'L') + f'{a[0]:.3f} {a[1]:.3f} Q {p1[0]:.3f} {p1[1]:.3f} {b[0]:.3f} {b[1]:.3f} '
    return d + 'Z'

def tile(fill, opacity):
    ps = ''
    # row A: cx = 3, 9 ; row B (half-drop): cx = 0, 6, 12 ; vertical pitch 6
    for row, (xs, y0) in enumerate((((3, 9), 0.5), ((0, 6, 12), 6.5))):
        for x in xs:
            for dy in (0, T) if False else (0,):
                ps += f'<path d="{rounded_tri(x, y0)}"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{T:g}" height="{T:g}" viewBox="0 0 {T:g} {T:g}">'
            f'<g fill="{fill}" fill-opacity="{opacity}">{ps}</g></svg>')

variants = {'on-navy': ('#FFFFFF', 0.06), 'on-slate': ('#FFFFFF', 0.075), 'on-orange': ('#FFFFFF', 0.12),
            'on-white': ('#0F1E2A', 0.04), 'on-orange-dark': ('#0F1E2A', 0.09)}
for k, (c, o) in variants.items():
    open(f'{OUT}/ncl-pattern-{k}.svg', 'w').write(tile(c, o))
print('pattern ok')
