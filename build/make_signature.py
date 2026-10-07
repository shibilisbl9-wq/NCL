import base64, pathlib, sys
sys.path.insert(0,'build'); import chrome
ROOT=pathlib.Path('deliverables/02-Email-Signature')
IMG='images/ncl-signature-logo.png'
def block(img_src):
    return f'''<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;font-family:Montserrat,'Segoe UI',Arial,Helvetica,sans-serif;color:#0F1E2A;">
  <tr><td style="padding:0 0 12px 0;"><img src="{img_src}" width="210" alt="New City Light – Lighting the Way" style="display:block;border:0;width:210px;height:auto;"></td></tr>
  <tr><td style="padding:0 0 10px 0;"><table cellpadding="0" cellspacing="0" border="0" role="presentation"><tr><td width="38" height="3" bgcolor="#F36B24" style="font-size:0;line-height:0;height:3px;width:38px;">&nbsp;</td></tr></table></td></tr>
  <tr><td style="padding:0;font-size:16px;line-height:20px;font-weight:700;color:#0F1E2A;">Full Name</td></tr>
  <tr><td style="padding:2px 0 10px 0;font-size:10px;line-height:14px;font-weight:600;letter-spacing:1.6px;text-transform:uppercase;color:#BD470B;">Job Title &nbsp;·&nbsp; Department</td></tr>
  <tr><td style="padding:0;font-size:12px;line-height:19px;color:#0F1E2A;">
    <span style="color:#BD470B;font-weight:700;">T</span>&nbsp;&nbsp;<a href="tel:+9647835776393" style="color:#0F1E2A;text-decoration:none;">+964 783 577 6393</a><br>
    <span style="color:#BD470B;font-weight:700;">E</span>&nbsp;&nbsp;<a href="mailto:admin@dulights.com" style="color:#0F1E2A;text-decoration:none;">admin@dulights.com</a><br>
    <span style="color:#BD470B;font-weight:700;">W</span>&nbsp;&nbsp;<a href="https://www.dulights.com" style="color:#0F1E2A;text-decoration:none;">www.dulights.com</a><br>
    <span style="color:#BD470B;font-weight:700;">A</span>&nbsp;&nbsp;Baghdad – Al-Mansour – Al-Dawoodi, Iraq
  </td></tr>
  <tr><td style="padding:10px 0 0 0;font-size:11px;line-height:16px;color:#5E6B76;text-align:left;" dir="rtl">مدينة جديدة. إنارة جديدة. منظور جديد.</td></tr>
</table>'''
def page(inner):
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>NCL Email Signature</title></head>
<body style="margin:0;padding:24px;background:#ffffff;">
<!-- Copy everything between the START and END comments into your email client's signature editor. -->
<!-- START SIGNATURE -->
{inner}
<!-- END SIGNATURE -->
</body></html>'''
(ROOT/'NCL-Email-Signature.html').write_text(page(block(IMG)))
b64=base64.b64encode((ROOT/IMG).read_bytes()).decode()
(ROOT/'NCL-Email-Signature-embedded-image.html').write_text(page(block('data:image/png;base64,'+b64)))
chrome.shot(ROOT/'NCL-Email-Signature.html', ROOT/'preview.png', 520, 400, 2)

from PIL import Image, ImageChops
pp = ROOT/'preview.png'
im = Image.open(pp).convert('RGB'); bb = ImageChops.difference(im, Image.new('RGB', im.size, (255,255,255))).getbbox(); pad = 40
im.crop((max(bb[0]-pad,0), max(bb[1]-pad,0), bb[2]+pad, bb[3]+pad)).save(pp)
