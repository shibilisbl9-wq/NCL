"""Rebuild every deliverable. Needs: python3 (Pillow, python-docx, openpyxl), Chromium (Playwright's), poppler-utils, LibreOffice (only to verify docx/xlsx).
Logo PNGs / vectors are built once from the client's source files (see make_logos.py, make_vectors.py)."""
import subprocess, sys
for s in ['make_pattern', 'build_letterhead', 'make_signature', 'make_envelopes', 'make_quotation', 'make_quotation_xlsx',
          'make_stamps', 'make_bag', 'make_symbol_concepts', 'make_guidelines', 'make_concepts_doc']:
    print('>>', s); subprocess.run([sys.executable, f'build/{s}.py'], check=True)
