"""Rebuild every deliverable. Needs: python3 (Pillow, python-docx, openpyxl), Chromium (Playwright's), poppler-utils, LibreOffice (only to verify docx/xlsx).
Logo PNGs / vectors are built once from the client's source files (see make_logos.py, make_vectors.py).

WARNING: the deliverables delivered on 16 Oct 2026 (quotation cover, orange/clear bags, arrow pattern, navy envelopes,
re-set stamps) were built from newer sources that are not in this repo. Running the stationery scripts below
overwrites them with OLDER designs. Until those sources are added, run only:
  python3 build/make_signature_editable.py && python3 build/patch_guidelines.py"""
import subprocess, sys
if '--force' not in sys.argv:
    sys.exit(__doc__ + '\n\nRefusing to run without --force.')
for s in ['make_pattern', 'build_letterhead', 'make_signature_editable', 'make_envelopes', 'make_quotation', 'make_quotation_xlsx',
          'make_stamps', 'make_bag', 'make_guidelines', 'patch_guidelines']:
    print('>>', s); subprocess.run([sys.executable, f'build/{s}.py'], check=True)
