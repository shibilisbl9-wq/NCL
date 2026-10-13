"""Seamless tile of upright rounded triangles on a half-drop (brick) grid - matches the pattern visible on the approved
card/envelope mockups (apex up, staggered rows, tone-on-tone). 12 x 12 unit tile; CSS sets the physical size."""
import os
OUT = 'brand/patterns'; os.makedirs(OUT, exist_ok=True)
T = 12.0                 # tile size (units)
BASE, HGT, R = 4.8, 5.3, 0.75   # triangle base, height, corner radius

def rounded_poly(pts, r):
    n = len(pts); d = ''
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        def toward(a, b, rr):
            dx, dy = b[0] - a[0], b[1] - a[1]; L = (dx * dx + dy * dy) ** .5
            return (a[0] + dx / L * min(rr, L / 2), a[1] + dy / L * min(rr, L / 2))
        a_ = toward(p1, p0, r); b_ = toward(p1, p2, r)
        d += ('M' if i == 0 else 'L') + f'{a_[0]:.3f} {a_[1]:.3f} Q {p1[0]:.3f} {p1[1]:.3f} {b_[0]:.3f} {b_[1]:.3f} '
    return d + 'Z'

def rounded_tri(cx, top):
    """Upright arrow motif: triangular head on a short stem, apex up (as on the approved envelope/card mockups)."""
    hw, sw, hh, th = 2.8, 1.45, 3.3, 5.5          # head half-width, stem half-width, head height, total height
    pts = [(cx, top), (cx + hw, top + hh), (cx + sw, top + hh), (cx + sw, top + th),
           (cx - sw, top + th), (cx - sw, top + hh), (cx - hw, top + hh)]
    return rounded_poly(pts, 0.35)

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
