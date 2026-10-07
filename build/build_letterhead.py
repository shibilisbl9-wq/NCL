import sys, subprocess, os; sys.path.insert(0,'build'); os.makedirs('build/_tmp', exist_ok=True)
import render
from PIL import Image
D='deliverables/01-Letterhead'
render.pdf('src/letterhead.html', f'{D}/NCL-Letterhead-A4-print-3mm-bleed.pdf','?mode=print')
render.pdf('src/letterhead.html', f'{D}/NCL-Letterhead-A4-blank.pdf')
render.pdf('src/letterhead.html', f'{D}/NCL-Letterhead-A4-sample-letter.pdf','?sample=1')
render.png(f'{D}/NCL-Letterhead-A4-sample-letter.pdf', f'{D}/preview-sample', 110)
# header/footer artwork for Word
subprocess.run(['pdftoppm','-r','300','-png',f'{D}/NCL-Letterhead-A4-blank.pdf','build/_tmp/lh'],check=True)
im=Image.open('build/_tmp/lh-1.png'); mm=lambda v:int(round(v/25.4*300))
im.crop((0,0,im.width,mm(36))).save('build/_tmp/lh_header.png')
im.crop((0,mm(297-26),im.width,im.height)).save('build/_tmp/lh_footer.png')
subprocess.run(['python3','build/make_docx.py','build/_tmp/lh_header.png','build/_tmp/lh_footer.png',f'{D}/NCL-Letterhead-A4-Word-template.docx'],check=True)
