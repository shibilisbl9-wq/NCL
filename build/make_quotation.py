import sys, pathlib; sys.path.insert(0,"build")
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
.logo-en{{left:20mm;top:14mm;width:64mm}} .logo-ar{{right:20mm;top:16.25mm;height:6.2mm}} .hdr-rule{{top:32mm}}
.title{{position:absolute;left:20mm;right:20mm;top:36.5mm;display:flex;justify-content:space-between;align-items:baseline;line-height:1.2}}
.title .en{{font-weight:800;font-size:19pt;letter-spacing:.2em;color:var(--navy)}}
.title .ar{{font-weight:800;font-size:17pt;color:var(--orange)}}
.title-rule{{position:absolute;left:20mm;right:20mm;top:48mm;height:.7mm;background:var(--navy)}}
.title-rule::before{{content:"";position:absolute;left:0;top:0;width:34mm;height:.7mm;background:var(--orange)}}
.grid{{position:absolute;left:20mm;right:20mm;display:grid;column-gap:5mm}}
.meta{{top:54mm;grid-template-columns:repeat(3,1fr);row-gap:2mm}}
.lab,.fld .lab{{display:flex;justify-content:space-between;align-items:baseline;font-size:5.6pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-text);line-height:1.5}}
.fld .lab .ar,.lab .ar{{letter-spacing:0;font-size:6.2pt;line-height:1.5}}
.fld .val{{height:6.2mm;border-bottom:.25mm solid var(--line);font-size:8.4pt;font-weight:500;padding-top:1.3mm;white-space:nowrap}}
.parties{{top:80mm;grid-template-columns:1fr 1fr;column-gap:6mm}}
.box{{background:var(--tint);border-left:1mm solid var(--orange);padding:2.4mm 3.5mm 1.5mm;height:24.5mm}}
.box h4{{display:flex;justify-content:space-between;align-items:baseline;font-size:5.8pt;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);font-weight:800;margin-bottom:.8mm;line-height:1.5}}
.box h4 .ar{{letter-spacing:0;font-size:6.6pt}}
.box .fld .val{{height:5.2mm;padding-top:.8mm;border-bottom-color:#cfd4d8;font-size:8pt}}
table.items{{position:absolute;left:20mm;right:20mm;top:108mm;width:170mm;border-collapse:collapse;font-size:8pt}}
.items thead th{{background:var(--navy);color:#fff;font-weight:600;font-size:6.4pt;letter-spacing:.08em;text-transform:uppercase;padding:2mm 2mm;text-align:left;line-height:1.25;border-top:.9mm solid var(--orange)}}
.items thead th .ar{{display:block;letter-spacing:0;font-size:6.4pt;text-transform:none;font-weight:600;opacity:.9;margin-top:.3mm}}
.items thead th.c{{text-align:center}} .items thead th.r{{text-align:right}}
.items td{{height:8mm;border-bottom:.25mm solid var(--line);padding:0 2mm;vertical-align:middle;line-height:1.3;font-size:7.8pt}}
.items td.c{{text-align:center;color:var(--muted)}} .items td.r{{text-align:right;font-variant-numeric:tabular-nums}}
.items tbody tr:nth-child(even) td{{background:#fafafa}}
/* approvals (left) | totals (right) */
.mid{{position:absolute;left:20mm;right:20mm;top:178mm;display:grid;grid-template-columns:1fr 68mm;column-gap:9mm}}
.appr h4,.tc h4{{display:flex;justify-content:space-between;align-items:baseline;font-size:5.8pt;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:var(--navy);margin-bottom:1.4mm;line-height:1.5}}
.appr h4 .ar,.tc h4 .ar{{letter-spacing:0;font-size:6.6pt}}
.appr .three{{display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:4mm}}
.appr .line{{height:19mm;border:.25mm solid var(--line);border-radius:.8mm;background:#fff}}
.appr .cap{{font-size:5.6pt;color:var(--muted);margin-top:1mm}}
.tot{{font-size:8pt}}
.tot .row{{display:flex;align-items:baseline;padding:1.7mm 2mm;border-bottom:.25mm solid var(--line);font-weight:500}}
.tot .row .en{{flex:1;font-size:6.2pt;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:var(--muted)}}
.tot .row .ar{{font-size:6.4pt;color:var(--muted);margin:0 3mm;font-weight:600}}
.tot .row b{{min-width:20mm;text-align:right;font-variant-numeric:tabular-nums;font-weight:600}}
.tot .grand{{background:var(--navy);color:#fff;border:0;border-left:1mm solid var(--orange);padding:2.6mm 2.4mm}}
.tot .grand .en,.tot .grand .ar{{color:#fff;font-weight:700}} .tot .grand b{{color:var(--orange);font-size:10pt;font-weight:800}}
/* terms: EN left, AR right */
.tc{{position:absolute;left:20mm;right:20mm;top:214mm;display:grid;grid-template-columns:1fr 1fr;column-gap:10mm;border-top:.25mm solid var(--line);padding-top:3mm}}
.tc h4{{justify-content:flex-start}}
.tc .ar-col{{direction:rtl;text-align:right}}
.tc ol{{padding-left:3.6mm;font-size:7pt;line-height:1.6;color:#33434f}}
.tc .ar-col ol{{list-style-type:arabic-indic;padding-left:0;padding-right:4mm;font-family:'NCL Arabic','Montserrat',sans-serif;font-size:7.2pt;line-height:1.85}}
.tc li{{margin-bottom:.9mm}}
.sample-tag{{position:absolute;right:20mm;top:6mm;font-size:5.6pt;font-weight:700;letter-spacing:.16em;color:var(--orange)}}
.smp{{font-size:8.2pt}}
</style></head><body>
<div class="sheet" data-w="210" data-h="297">
  {tag}
  <img class="abs logo-en" src="../brand/logos/png/ncl-horizontal-full-colour.png" alt="">
  <img class="abs logo-ar" src="../brand/logos/png/ncl-arabic-navy.png" alt="">
  <div class="hdr-rule"></div>
  <div class="title"><div class="en">QUOTATION</div><div class="ar">عرض سعر</div></div>
  <div class="title-rule"></div>

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

  <div class="mid">
    <div class="appr"><h4><span>Approvals</span><span class="ar">الاعتمادات</span></h4>
      <div class="three">
        <div><div class="lab"><span>Prepared by</span><span class="ar">أعدّه</span></div><div class="line"></div><div class="cap">Name · signature · date</div></div>
        <div><div class="lab"><span>Approved by</span><span class="ar">اعتمده</span></div><div class="line"></div><div class="cap">Name · signature · date</div></div>
        <div><div class="lab"><span>Stamp</span><span class="ar">الختم</span></div><div class="line"></div><div class="cap">&nbsp;</div></div>
      </div></div>
    <div class="tot">
      <div class="row"><span class="en">Subtotal</span><span class="ar">المجموع الفرعي</span><b>{f(total)}</b></div>
      <div class="row"><span class="en">Discount</span><span class="ar">الخصم</span><b>{f(disc) if sample else ''}</b></div>
      <div class="row"><span class="en">Tax / VAT</span><span class="ar">الضريبة</span><b>{f(vat)}</b></div>
      <div class="row grand"><span class="en">Grand total</span><span class="ar">الإجمالي</span><b>{f(grand)}</b></div>
    </div>
  </div>

  <div class="tc">
    <div><h4><span>Terms &amp; conditions</span></h4>
      <ol><li>Prices are valid for the period stated above and exclude any taxes or duties not shown.</li>
      <li>Delivery: ____ weeks from order confirmation and receipt of advance payment.</li>
      <li>Warranty: as per the manufacturer's terms for each product supplied.</li>
      <li>Any change to the scope or quantities will be quoted separately.</li></ol></div>
    <div class="ar-col"><h4 class="ar"><span>الشروط والأحكام</span></h4>
      <ol><li>الأسعار سارية للمدة المذكورة أعلاه ولا تشمل أي ضرائب أو رسوم غير مبيّنة.</li>
      <li>التسليم: ____ أسبوعاً من تأكيد الطلب واستلام الدفعة المقدّمة.</li>
      <li>الضمان: وفق شروط الشركة المصنّعة لكل منتج يتم توريده.</li>
      <li>أي تغيير في نطاق العمل أو الكميات يُسعَّر بشكل منفصل.</li></ol></div>
  </div>

  <!--FOOTER-->
</div><script src="shared/common.js"></script></body></html>'''

import parts
pathlib.Path('src/quotation.html').write_text(build(False).replace('<!--FOOTER-->', parts.footer()))
pathlib.Path('src/quotation-sample.html').write_text(build(True).replace('<!--FOOTER-->', parts.footer()))
D = 'deliverables/05-Quotation'
render.pdf('src/quotation.html', f'{D}/NCL-Quotation-A4-blank-print-3mm-bleed.pdf', '?mode=print')
render.pdf('src/quotation.html', f'{D}/NCL-Quotation-A4-blank.pdf')
render.pdf('src/quotation-sample.html', f'{D}/NCL-Quotation-A4-sample-filled.pdf')
render.png(f'{D}/NCL-Quotation-A4-sample-filled.pdf', f'{D}/preview-sample', 110)
render.png(f'{D}/NCL-Quotation-A4-blank.pdf', f'{D}/preview-blank', 80)
