"""Arabic wordmark = the *sound* of the name (New City Light -> نيو سيتي لايت), not a translation.
Set in Noto Kufi Arabic ExtraBold, rendered to tight-cropped transparent PNGs in the four brand colours."""
import subprocess, pathlib, sys
sys.path.insert(0, 'build'); import chrome
from PIL import Image
ROOT = pathlib.Path('.'); T = ROOT / 'build/_tmp'; T.mkdir(exist_ok=True)
NAME = 'نيو سيتي لايت'
COLS = {'navy': '#0F1E2A', 'white': '#FFFFFF', 'orange': '#F36B24', 'black': '#000000'}
for k, c in COLS.items():
    h = T / f'arwm-{k}.html'
    h.write_text(f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:K;font-weight:800;src:url(../../brand/fonts/NotoKufiArabic-arabic-800.woff2)}}
html,body{{margin:0;background:transparent}}
div{{font:800 300px/1.6 K;color:{c};direction:rtl;white-space:nowrap;padding:40px 60px;display:inline-block}}</style><div>{NAME}</div>''')
    png = T / f'arwm-{k}-raw.png'
    subprocess.run([str(chrome.CHROME), *chrome.BASE, '--default-background-color=00000000', '--window-size=2400,700',
                    f'--screenshot={png}', h.resolve().as_uri()], check=True, capture_output=True)
    im = Image.open(png).convert('RGBA'); bb = im.getchannel('A').getbbox()
    im = im.crop(bb); im.save(ROOT / f'brand/logos/png/ncl-arabic-{k}.png'); print(k, im.size)
