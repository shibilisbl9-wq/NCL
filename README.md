# New City Light – stationery & brand guidelines

Everything here was built from the rebranding pack (logos, mockups, presentation, `Broucher.ai`).
All text and layout are live source (HTML/CSS) so any change is a rebuild, not a redraw.

## What's in `deliverables/`

| Folder | Contents |
|---|---|
| `00-Brand-Guidelines` | `NCL-Brand-Guidelines-v1.0.pdf` – 33 pages, A4 landscape |
| `01-Letterhead` | A4 print PDF (3 mm bleed + crop marks), blank PDF, sample-letter PDF, **Word template (.docx)** |
| `02-Email-Signature` | HTML signature, embedded-image version, logo PNG, preview |
| `03-Envelope-Large-C4` | C4 324×229 mm, front + back, print PDF (5 mm bleed) + trim-size PDF |
| `04-Envelope-Small-DL` | DL 220×110 mm, front + back, same files |
| `05-Quotation` | A4 bilingual form (blank print PDF, blank PDF, sample-filled PDF) + **Excel template with formulas** |
| `06-Stamp` | Round Ø42 mm + rectangular 69×33 mm, one-colour, **text outlined**: SVG + PDF, black and navy |
| `07-Plastic-Bag` | 350×450 mm front/back artwork + version with die-cut/safe-area guides |
| `08-Symbol-Concepts` | 16-page review deck: navy app icon, 6 colour-only routes, 6 shape changes to the master, 4 geometric concepts (Aperture, Window, Solid disc, Sunburst), recommendation. **Proposals, not approved artwork.** |

Supporting: `brand/` (logo PNG/SVG kit, petal pattern tiles, fonts, reference images), `src/` (HTML sources), `build/` (scripts; `python3 build/build_all.py`).

## Read this before sending anything to print

These are real limits, not footnotes:

1. **Nothing has been test-printed.** Colours are RGB (`#F36B24` orange, `#0F1E2A` navy, `#F5F5F4` off-white, `#303E4A` slate). The CMYK values in the book are straight conversions – approve a printed swatch first. No Pantone matches were assigned.
2. **Website conflict.** The brochure says `www.dulights.com` / `admin@dulights.com` (used on everything here). The business-card mockup says `www.NewCityLight.com`. Tell me which one is right and I'll rebuild.
3. **Defect in the supplied logo files.** In the full-colour and single-colour PNGs the ® ring is a hairline sitting to the *right* of the "R" instead of around it. The on-dark file is correct. My logo kit rebuilds the ® from the correct file – please fix the master artwork too.
4. **Arabic spelling.** The Arabic logo reads «انارة» (no hamza); the brochure body text writes «إنارة». I used the hamza form in running text and the logo artwork as supplied.
5. **"30+ years" vs 1998.** The brochure claims 30+ years of experience but its timeline starts in 1998 (28 years). I did not print either claim.
6. **Pattern is a reconstruction** of the one visible on the card/envelope mockups (the original file wasn't in the pack). Drop the original into `brand/patterns/` if you have it.
7. **Fonts.** Montserrat (Latin) and Noto Kufi Arabic (Arabic) are free and are used everywhere. The brochure uses *GE SS Two* (Arabic, commercial) and *Nasalization* (logo/headlines, free for personal use only) – not bundled; check licences. The stationery doesn't need them (the logo is artwork).
8. **Contrast.** White-on-orange and orange-on-white are only 3.0:1 – fine for the logo and large type, not for small text. Small orange labels use a darker `#BD470B` (5.2:1). Details on page 14 of the book.
9. **Office printers can't print to the page edge**, so the letterhead's full-bleed footer band only works on pre-printed stock. The Word template is for files you send as PDF.
10. **Email signature images must be hosted** at a public https URL for Gmail/Outlook.com; edit the `src` in the HTML. Montserrat falls back to Segoe UI/Arial in mail clients.
11. **Placeholders I wrote, not NCL:** quotation terms, the four personality words, the working English translation of the Arabic statement, bag size (350×450 mm), min logo sizes (40 mm / 160 px). Stamp wording has no registration/licence number – check what the authorities require.
12. **Envelope and bag die-lines** belong to your manufacturer; artwork is at finished size.

13. **Symbol likeness.** Alone, the orange radiating symbol (especially white-on-orange) reads like other tech/AI "spark" marks. The navy app icon (`brand/logos/png/ncl-app-icon-navy.png`) is now primary; the old orange tile `ncl-app-icon.png` is kept but retired. Colour-only routes and shape concepts are in `brand/concepts/` and `08-Symbol-Concepts`. Concepts B–G reuse the master petal geometry; H–K (geometric direction, from reference boards the client shared) are new parametric geometry. All are starting points for a designer, not artwork. Colour does not change one-colour uses (stamp, embossing). Avoid light/off-white icon tiles: cream behind orange brings the likeness back.

Source data used: company brochure (contacts, services, milestones, partners), approved mockups (slate colour, pattern, direction).
