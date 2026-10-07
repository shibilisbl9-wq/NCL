"""Build the PNG logo set from the client's supplied artwork (alpha-mask recolouring, trimmed)."""
import sys, os
from PIL import Image
SRC = sys.argv[1]            # extracted Logo/ folder
OUT = sys.argv[2]
NAVY, ORANGE, WHITE = (15, 30, 42), (243, 107, 36), (245, 245, 244)
os.makedirs(OUT, exist_ok=True)

def trim(im):
    bb = im.split()[-1].point(lambda v: 255 if v > 8 else 0).getbbox()
    return im.crop(bb)

def tint(im, rgb):
    a = im.split()[-1]
    out = Image.new('RGBA', im.size, rgb + (0,)); out.putalpha(a); return out

def save(im, name): trim(im).save(f'{OUT}/{name}', optimize=True)

full  = Image.open(f'{SRC}/Asset 3 copy (2).png').convert('RGBA')   # orange symbol + navy wordmark
black = Image.open(f'{SRC}/Asset black (1).png').convert('RGBA')    # single colour
dark  = Image.open(f'{SRC}/Asset 3 (4).png').convert('RGBA')        # orange symbol + white wordmark
ar    = Image.open(f'{SRC}/arabic logo (2).png').convert('RGBA')    # arabic, black

# --- Fix: in the supplied full-colour / single-colour PNGs the (R) ring is a white hairline displaced to the
# right of the "R". The on-dark file has it correct (ring around R), so reuse that (R) for every light variant.
def fix_reg(im, rgb):
    w, h = im.size; box = (int(w * .935), int(h * .62), w, h)
    im = im.copy(); a = im.split()[-1]
    a.paste(0, box); im.putalpha(a)
    reg_a = dark.split()[-1].crop(box)
    patch = Image.new('RGBA', reg_a.size, rgb + (0,)); patch.putalpha(reg_a)
    im.alpha_composite(patch, dest=box[:2]); return im
full  = fix_reg(full,  NAVY)
black = fix_reg(black, NAVY)

# make sure full-colour uses the exact brand navy for text, orange for symbol (source already does)
save(full,  'ncl-horizontal-full-colour.png')
save(dark,  'ncl-horizontal-on-dark.png')
save(tint(black, NAVY),   'ncl-horizontal-mono-navy.png')
save(tint(black, WHITE),  'ncl-horizontal-mono-white.png')
save(tint(black, ORANGE), 'ncl-horizontal-mono-orange.png')
save(tint(black, (0, 0, 0)), 'ncl-horizontal-mono-black.png')
save(tint(ar, NAVY),   'ncl-arabic-navy.png')
save(tint(ar, WHITE),  'ncl-arabic-white.png')
save(tint(ar, ORANGE), 'ncl-arabic-orange.png')
save(tint(ar, (0, 0, 0)), 'ncl-arabic-black.png')
icon = Image.open(f'{SRC}/../PNG/Asset 2@2x.png').convert('RGBA'); icon.save(f'{OUT}/ncl-app-icon.png', optimize=True)
for f in sorted(os.listdir(OUT)): print(f, Image.open(f'{OUT}/{f}').size)
