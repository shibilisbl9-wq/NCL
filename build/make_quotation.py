import sys, pathlib; sys.path.insert(0,'build')
import render

ITEMS = [  # sample data only
 ('LED linear profile system, 20 W/m, 3000 K, anodised black, 2 m', 'm', 120, 18.50),
 ('Recessed COB downlight, 12 W, 3000 K, IP44', 'pcs', 80, 14.00),
 ('Outdoor pathway bollard, 10 W, IP65, graphite', 'pcs', 24, 96.00),
 ('Constant-voltage LED driver, 100 W, 24 V', 'pcs', 18, 38.50),
 ('Installation supervision and commissioning', 'lot', 1, 850.00),
]
def money(v): return f'{v:,.2f}'

def build(sample):
    rows = ''
    total = 0
    for i in range(1, 8):
        if sample and i <= len(ITEMS):
            d, u, q, p = ITEMS[i-1]; t = q*p; total += t
            rows += f'<tr><td class="c">{i}</td><td>{d}</td><td class="c">{u}</td><td class="r">{q}</td><td class="r">{money(p)}</td><td class="r">{money(t)}</td></tr>'
        else:
            rows += f'<tr><td class="c"></td><td></td><td class="c"></td><td class="r"></td><td class="r"></td><td class="r"></td></tr>'
    disc = total*0.05 if sample else 0; net = total-disc; vat = net*0.0 if sample else 0; grand = net+vat
    f = (lambda v: money(v)) if sample else (lambda v: '')
    def fld(label_en, label_ar, val=''):
        return f'<div class="fld"><div class="lab"><span>{label_en}</span><span class="ar">{label_ar}</span></div><div class="val">{val}</div></div>'
    S = (lambda v: v) if sample else (lambda v: '')
    tag = '<div class="sample-tag">SAMPLE – ILLUSTRATIVE DATA</div>' if sample else ''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>NCL Quotation A4</title>
<link rel="stylesheet" href="shared/common.css"><style>
.logo-en{{left:20mm;top:14mm;width:64mm}} .logo-ar{{right:20mm;top:14mm;height:10.7mm}} .hdr-rule{{top:32mm}}
.title{{position:absolute;left:20mm;right:20mm;top:37mm;display:flex;justify-content:space-between;align-items:baseline}}
.title .en{{font-weight:800;font-size:19pt;letter-spacing:.2em;color:var(--navy)}}
.title .ar{{font-weight:800;font-size:17pt;color:var(--orange)}}
.grid{{position:absolute;left:20mm;right:20mm;display:grid;column-gap:5mm}}
.meta{{top:48.5mm;grid-template-columns:repeat(3,1fr);row-gap:2mm}}
.fld .lab{{display:flex;justify-content:space-between;font-size:5.6pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-text)}}
.fld .lab .ar{{letter-spacing:0;font-size:6.2pt}}
.fld .val{{height:6.2mm;border-bottom:.25mm solid var(--line);font-size:8.4pt;font-weight:500;padding-top:1.3mm;white-space:nowrap}}
.parties{{top:76mm;grid-template-columns:1fr 1fr;column-gap:6mm}}
.box{{background:var(--tint);border-left:1mm solid var(--orange);padding:2.4mm 3.5mm 1.5mm;height:24.5mm}}
.box h4{{display:flex;justify-content:space-between;font-size:5.8pt;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);font-weight:800;margin-bottom:.8mm}}
.box h4 .ar{{letter-spacing:0;font-size:6.6pt}}
.box .fld .val{{height:5.2mm;padding-top:.8mm;border-bottom-color:#cfd4d8;font-size:8pt}}
table.items{{position:absolute;left:20mm;right:20mm;top:104mm;width:170mm;border-collapse:collapse;font-size:8pt}}
.items thead th{{background:var(--navy);color:#fff;font-weight:600;font-size:6.4pt;letter-spacing:.08em;text-transform:uppercase;padding:2mm 2mm;text-align:left;line-height:1.25}}
.items thead th .ar{{display:block;letter-spacing:0;font-size:6.4pt;text-transform:none;font-weight:600;opacity:.9}}
.items thead th.c{{text-align:center}} .items thead th.r{{text-align:right}}
.items thead th:first-child{{border-top:.9mm solid var(--orange)}} .items thead th{{border-top:.9mm solid var(--orange)}}
.items td{{height:8.4mm;border-bottom:.25mm solid var(--line);padding:0 2mm;vertical-align:middle;line-height:1.3;font-size:7.8pt}}
.items td.c{{text-align:center;color:var(--muted)}} .items td.r{{text-align:right;font-variant-numeric:tabular-nums}}
.items tbody tr:nth-child(even) td{{background:#fafafa}}
.bottom{{position:absolute;left:20mm;right:20mm;top:176mm;display:grid;grid-template-columns:1fr 70mm;column-gap:8mm}}
.terms h4,.sig h4{{font-size:5.8pt;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:var(--navy);margin-bottom:1.4mm;display:flex;justify-content:space-between}}
.terms h4 .ar,.sig h4 .ar{{letter-spacing:0;font-size:6.6pt}}
.terms ol{{padding-left:3.6mm;font-size:6.6pt;line-height:1.55;color:#33434f}}
.terms li{{margin-bottom:.7mm}}
.tot{{width:70mm;font-size:8pt}}
.tot .row{{display:flex;justify-content:space-between;padding:1.5mm 2mm;border-bottom:.25mm solid var(--line);font-weight:500}}
.tot .row span:first-child{{font-size:6.4pt;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:var(--muted)}}
.tot .row .ar{{font-size:6.4pt;color:var(--muted);margin-left:2mm}}
.tot .row b{{font-variant-numeric:tabular-nums;font-weight:600}}
.tot .grand{{background:var(--navy);color:#fff;border:0;border-left:1mm solid var(--orange);padding:2.4mm 2.4mm}}
.tot .grand span:first-child{{color:#fff;font-weight:700}} .tot .grand b{{color:var(--orange);font-size:10pt;font-weight:800}}
.sigrow{{position:absolute;left:20mm;right:20mm;top:219mm;display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:8mm}}
.sig .line{{height:25mm;border:.25mm solid var(--line);border-radius:.8mm;background:#fff}}
.sig .cap{{font-size:6pt;color:var(--muted);margin-top:1mm}}
.sample-tag{{position:absolute;right:20mm;top:6mm;font-size:5.6pt;font-weight:700;letter-spacing:.16em;color:var(--orange)}}
.smp{{font-size:8.2pt}}
</style></head><body>
<div class="sheet" data-w="210" data-h="297">
  {tag}
  <img class="abs logo-en" src="../brand/logos/png/ncl-horizontal-full-colour.png" alt="">
  <img class="abs logo-ar" src="../brand/logos/png/ncl-arabic-navy.png" alt="">
  <div class="hdr-rule"></div>
  <div class="title"><div class="en">QUOTATION</div><div class="ar">عرض سعر</div></div>

  <div class="grid meta">
    {fld('Quotation No.','رقم العرض',S('NCL-Q-2026-0147'))}
    {fld('Date','التاريخ',S('7 Oct 2026'))}
    {fld('Valid until','صالح لغاية',S('6 Nov 2026'))}
    {fld('Prepared by','أعدّه',S('Full Name'))}
    {fld('Currency','العملة',S('USD'))}
    {fld('Payment terms','شروط الدفع',S('50% advance / 50% on delivery'))}
  </div>

  <div class="grid parties">
    <div class="box"><h4><span>Quoted to</span><span class="ar">السادة</span></h4>
      {fld('Company','الشركة',S('Client Company Name'))}
      <div style="display:grid;grid-template-columns:1fr 1fr;column-gap:4mm">{fld('Attention','عناية',S('Project Manager'))}{fld('Phone','الهاتف',S('+964 7XX XXX XXXX'))}</div>
    </div>
    <div class="box"><h4><span>Project</span><span class="ar">المشروع</span></h4>
      {fld('Project name','اسم المشروع',S('Project name'))}
      <div style="display:grid;grid-template-columns:1fr 1fr;column-gap:4mm">{fld('Location','الموقع',S('Baghdad'))}{fld('Reference','المرجع',S('RFQ-0000'))}</div>
    </div>
  </div>

  <table class="items"><thead><tr>
    <th class="c" style="width:9mm">No.<span class="ar">ت</span></th>
    <th>Description<span class="ar">الوصف</span></th>
    <th class="c" style="width:13mm">Unit<span class="ar">الوحدة</span></th>
    <th class="r" style="width:14mm">Qty<span class="ar">الكمية</span></th>
    <th class="r" style="width:24mm">Unit price<span class="ar">سعر الوحدة</span></th>
    <th class="r" style="width:27mm">Total<span class="ar">المجموع</span></th></tr></thead>
    <tbody>{rows}</tbody></table>

  <div class="bottom">
    <div class="terms"><h4><span>Terms &amp; conditions</span><span class="ar">الشروط والأحكام</span></h4>
      <ol><li>Prices are valid for the period stated above and exclude any taxes or duties not shown.</li>
      <li>Delivery: ____ weeks from order confirmation and receipt of advance payment.</li>
      <li>Warranty: as per the manufacturer's terms for each product supplied.</li>
      <li>Any change to the scope or quantities will be quoted separately.</li></ol></div>
    <div class="tot">
      <div class="row"><span>Subtotal<span class="ar">المجموع الفرعي</span></span><b>{f(total)}</b></div>
      <div class="row"><span>Discount<span class="ar">الخصم</span></span><b>{f(disc) if sample else ''}</b></div>
      <div class="row"><span>Tax / VAT<span class="ar">الضريبة</span></span><b>{f(vat)}</b></div>
      <div class="row grand"><span>Grand total<span class="ar" style="color:#fff">الإجمالي</span></span><b>{f(grand)}</b></div>
    </div>
  </div>

  <div class="sigrow">
    <div class="sig"><h4><span>Prepared by</span><span class="ar">أعدّه</span></h4><div class="line"></div><div class="cap">Name · signature · date</div></div>
    <div class="sig"><h4><span>Approved by</span><span class="ar">اعتمده</span></h4><div class="line"></div><div class="cap">Name · signature · date</div></div>
    <div class="sig"><h4><span>Company stamp</span><span class="ar">ختم الشركة</span></h4><div class="line"></div><div class="cap">&nbsp;</div></div>
  </div>

  <div class="footer-band pat-navy">
    <div class="footer-grid">
      <div><div class="lab"><span>Address</span><span class="ar">العنوان</span></div><div><b>New City Light</b><br>Baghdad – Al-Mansour – Al-Dawoodi, Iraq</div><div class="arl ar">بغداد – المنصور – الداوودي</div></div>
      <div><div class="lab"><span>Phone</span><span class="ar">الهاتف</span></div><div class="num ltr">+964 783 577 6393<br>+964 786 555 3648<br>+964 780 517 7717</div></div>
      <div><div class="lab"><span>Email · Web</span><span class="ar">البريد · الموقع</span></div><div class="ltr">admin@dulights.com<br>www.dulights.com</div>
      <div class="ltr" style="margin-top:1.4mm;font-size:5.6pt;letter-spacing:.2em;text-transform:uppercase;color:var(--orange);font-weight:600">Lighting the Way</div></div>
    </div>
  </div>
</div><script src="shared/common.js"></script></body></html>'''

pathlib.Path('src/quotation.html').write_text(build(False))
pathlib.Path('src/quotation-sample.html').write_text(build(True))
D = 'deliverables/05-Quotation'
render.pdf('src/quotation.html', f'{D}/NCL-Quotation-A4-blank-print-3mm-bleed.pdf', '?mode=print')
render.pdf('src/quotation.html', f'{D}/NCL-Quotation-A4-blank.pdf')
render.pdf('src/quotation-sample.html', f'{D}/NCL-Quotation-A4-sample-filled.pdf')
render.png(f'{D}/NCL-Quotation-A4-sample-filled.pdf', f'{D}/preview-sample', 110)
render.png(f'{D}/NCL-Quotation-A4-blank.pdf', f'{D}/preview-blank', 80)
