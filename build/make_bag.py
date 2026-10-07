import sys; sys.path.insert(0,'build')
import render
D='deliverables/07-Plastic-Bag'
render.pdf('src/plastic-bag.html', f'{D}/NCL-PlasticBag-350x450-front-back-artwork.pdf')
render.pdf('src/plastic-bag.html', f'{D}/NCL-PlasticBag-350x450-with-production-guides.pdf','?guides=1')
render.png(f'{D}/NCL-PlasticBag-350x450-with-production-guides.pdf', f'{D}/preview-guides', 40)
render.png(f'{D}/NCL-PlasticBag-350x450-front-back-artwork.pdf', f'{D}/preview', 40)
