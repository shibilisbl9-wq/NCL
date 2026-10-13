"""Shared copy + markup pieces (single source for contact details and the stationery footer)."""
WEB = 'www.newcitylights.ir'
PHONE = '+964 987 654 3210'          # placeholder number (9876543210) with Iraq code
PHONE_TEL = '+9649876543210'
EMAIL = 'admin@newcitylights.ir'     # assumed: same mailbox name on the new domain - confirm
ADDR_EN = 'Baghdad, Iraq'
ADDR_AR = 'بغداد، العراق'
NAME_AR = 'نيو سيتي لايت'
TAG_EN = 'Lighting the Way'
TAG_AR = 'إنارة الطريق'

_S = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'
ICON_PATHS = {
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'mail': '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
 'web': '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 'pin': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
}
def icon(name, w=1.9, cls='ic'):
    return f'<svg class="{cls}" {_S.format(w=w)}>{ICON_PATHS[name]}</svg>'

def footer():
    return f'''<div class="footer-band pat-navy"><div class="ft">
  <div class="ft-id">
    <img class="ft-en" src="../brand/logos/vector/ncl-wordmark-white.svg" alt="New City Light">
    <img class="ft-ar" src="../brand/logos/png/ncl-arabic-white.png" alt="{NAME_AR}">
    <div class="ft-tag"><span>{TAG_EN}</span><i></i><i></i><i></i></div>
  </div>
  <div class="ft-contact">
    <div class="ft-main">
      <div class="ft-row ltr">{icon('phone')}<span>{PHONE}</span></div>
      <div class="ft-row ltr">{icon('mail')}<span>{EMAIL}</span></div>
      <div class="ft-row ltr">{icon('web')}<span>{WEB}</span></div>
    </div>
    <div class="ft-addr">
      {icon('pin')}
      <div><div class="ltr">{ADDR_EN}</div><div class="ar">{ADDR_AR}</div></div>
    </div>
  </div>
</div></div>'''

def inject_footer(path):
    import re, pathlib
    p = pathlib.Path(path); s = p.read_text()
    s2 = re.sub(r'<div class="footer-band.*?(?=</div>\s*<script src="shared/common.js">)', lambda m: footer() + '\n', s, flags=re.S)
    assert s2 != s or footer() in s, 'footer block not found in ' + path
    p.write_text(s2)
