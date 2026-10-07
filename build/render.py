"""Render helpers: html + query -> PDF; PDF -> PNG preview via poppler."""
import subprocess, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import chrome

ROOT = pathlib.Path(__file__).resolve().parent.parent

def pdf(src, out, query=''):
    out = ROOT / out; out.parent.mkdir(parents=True, exist_ok=True)
    url = (ROOT / src).resolve().as_uri() + query
    subprocess.run([str(chrome.CHROME), *chrome.BASE, '--no-pdf-header-footer', f'--print-to-pdf={out}', url],
                   check=True, capture_output=True)
    return out

def png(pdf_path, out_prefix, dpi=110, first=None, last=None):
    out_prefix = ROOT / out_prefix
    cmd = ['pdftoppm', '-r', str(dpi), '-png']
    if first: cmd += ['-f', str(first)]
    if last: cmd += ['-l', str(last)]
    subprocess.run([*cmd, str(ROOT / pdf_path), str(out_prefix)], check=True)
