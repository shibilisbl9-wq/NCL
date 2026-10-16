# New City Light – stationery & brand guidelines

Everything here was built from the rebranding pack (logos, mockups, presentation, `Broucher.ai`).
Text and layout are HTML/CSS source, but see "The sources are behind the deliverables" below: right now not every PDF can be rebuilt from this repo.

## What's in `deliverables/`

| Folder | Contents |
|---|---|
| `00-Brand-Guidelines` | `NCL-Brand-Guidelines-v1.0.pdf`: 37 pages, A4 landscape. Pages 30–33 are the photographic mockups; p23 and p29 updated |
| `01-Letterhead` | A4 print PDF (3 mm bleed + crop marks), blank PDF, sample-letter PDF, **Word template (.docx)**, `NEW.pdf` (Illustrator export, see below) |
| `02-Email-Signature` | Approved banner JPG (1800×621) + **editable versions**: layered SVG, `.ai`, layered PSD, browser editor, sample PNG, `links/` |
| `03-Envelope-Large-C4` | C4 324×229 mm, front + back, print PDF (5 mm bleed) + trim-size PDF |
| `04-Envelope-Small-DL` | DL 220×110 mm, front + back, same files |
| `05-Quotation` | Navy **cover** (front/back, print + blank PDF) and bilingual A4 form (blank print PDF, blank PDF, sample PDF) + **Excel template with formulas** |
| `06-Stamp` | Round Ø43 mm + rectangular 80×26 mm, one-colour, **text outlined**: SVG + PDF, black and navy; `new.pdf` (Illustrator export, see below) |
| `07-Plastic-Bag` | 350×450 mm, **orange** and **clear** film versions: artwork PDF + version with die-cut/safe-area guides |
| `08-Mockups` | `NCL-Mockups-v1.0.pdf`: 10 photographic mockup slides (16:9) |

## Email signature: which file to use

| File | Use it for | Limits |
|---|---|---|
| `NCL-Email-Signature-Editor.html` | **Each employee**: open in a browser, type name/title/contacts, download PNG/JPG/SVG | Text is not shrunk to fit; keep lines about as long as the defaults |
| `NCL-Email-Signature-editable.svg` | Designers: Illustrator, Figma, Inkscape. Named layers, live text, vector logo | Install the fonts in `brand/fonts/desktop/` first |
| `NCL-Email-Signature-editable.ai` | Illustrator | It's a PDF-compatible `.ai` made without Illustrator (I don't have it). Text is live and the fonts are embedded under their real names, but Illustrator may still break the text into separate lines. **Not tested in Illustrator.** If it gives you trouble, open the SVG |
| `NCL-Email-Signature-layered.psd` | Photoshop | One layer per element, but the **text is pixels, not live type**. To change a name, hide that layer and retype it |
| `links/` | Hero glow photo and footer strip, cut from your JPG | The baked-in logo and tagline were painted out of the hero |

Changes from your JPG, on purpose: name, title and address are in **Montserrat** (your JPG used a different sans, which is off-brand);
the placeholder address *"whole adress of new city light with sample pincode and evrething"* is replaced with **Al-Mansour – Al-Dawoodi / Baghdad, Iraq**
(add a postcode if you have one). Insert the PNG at **600 px wide** and type name, phone and email as plain text under it:
an image-only signature can't be clicked, is hidden until the reader allows images and is invisible to screen readers.

Supporting: `brand/` (logo PNG/SVG kit, pattern tiles, web fonts, `fonts/desktop/` TTFs for designers, `mockups/` crops, reference images), `src/` (HTML sources), `build/` (scripts).

## The sources are behind the deliverables

The deliverables from the 16 Oct 2026 zip were built from sources that are **not in this repo** (arrow-pattern tile, horizontal vector logos,
quotation cover, orange/clear bag, re-set stamps). Branch `ccr-92cfdab7-43a7pn` has some of that work, but not all of it.
So `src/` and `build/` cannot reproduce the current PDFs, and `build/build_all.py` now refuses to run without `--force`,
because running it would replace them with older designs. Only these two scripts are safe:

- `python3 build/make_signature_editable.py`: editable email-signature files, built from the approved JPG
- `python3 build/patch_guidelines.py`: takes the delivered 33-page book (`build/base/`) and re-renders the contents page, p23 and p29,
  adds four mockup pages (p30–33) and renumbers the pages after them

Send me the newer sources and I'll merge them in.

## Read this before sending anything to print

These are real limits, not footnotes:

1. **Nothing has been test-printed.** Colours are RGB (`#F36B24` orange, `#0F1E2A` navy, `#F5F5F4` off-white, `#303E4A` slate). The CMYK values in the book are straight conversions – approve a printed swatch first. No Pantone matches were assigned.
2. **Website conflict.** The brochure says `www.dulights.com` / `admin@dulights.com` (used on everything here). The business-card mockup says `www.NewCityLight.com`. Tell me which one is right and I'll rebuild.
3. **Defect in the supplied logo files.** In the full-colour and single-colour PNGs the ® ring is a hairline sitting to the *right* of the "R" instead of around it. The on-dark file is correct. My logo kit rebuilds the ® from the correct file – please fix the master artwork too.
4. **Arabic spelling.** The Arabic logo reads «انارة» (no hamza); the brochure body text writes «إنارة». I used the hamza form in running text and the logo artwork as supplied.
5. **"30+ years" vs 1998.** The brochure claims 30+ years of experience but its timeline starts in 1998 (28 years). I did not print either claim.
6. **Loose files.** `01-Letterhead/NEW.pdf` and `06-Stamp/new.pdf` are Illustrator exports from your zip. `NEW.pdf` looks the same as the blank letterhead. `new.pdf` is a re-set rectangular stamp with smaller address text. I committed both unchanged. Tell me if `new.pdf` should replace the stamp files.
7. **Fonts.** Montserrat (Latin) and Noto Kufi Arabic (Arabic) are free and are used everywhere. The brochure uses *GE SS Two* (Arabic, commercial) and *Nasalization* (logo/headlines, free for personal use only) – not bundled; check licences. The stationery doesn't need them (the logo is artwork).
8. **Contrast.** White-on-orange and orange-on-white are only 3.0:1 – fine for the logo and large type, not for small text. Small orange labels use a darker `#BD470B` (5.2:1). Details on page 13 of the book.
9. **Office printers can't print to the page edge**, so the letterhead's full-bleed footer band only works on pre-printed stock. The Word template is for files you send as PDF.
10. **Mockups are slides, not artwork.** The brand-book mockup slide still says "33 pages" (the book now has 37), and the quotation-cover slide lists a "sample" PDF that doesn't exist (only sample previews do). They're flat images, so I couldn't fix them.
11. **Placeholders I wrote, not NCL:** quotation terms, the four personality words, the working English translation of the Arabic statement, bag size (350×450 mm), min logo sizes (40 mm / 160 px). Stamp wording has no registration/licence number – check what the authorities require.
12. **Envelope and bag die-lines** belong to your manufacturer; artwork is at finished size.

Source data used: company brochure (contacts, services, milestones, partners), approved mockups (slate colour, pattern, direction).
