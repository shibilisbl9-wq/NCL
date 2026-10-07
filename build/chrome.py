import subprocess, os, pathlib
CHROME = [p for p in pathlib.Path('/opt/pw-browsers').glob('chromium-*/chrome-linux/chrome')][0]
BASE = ['--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
        '--allow-file-access-from-files', '--font-render-hinting=none', '--virtual-time-budget=4000']

def shot(html, png, w, h, scale=1):
    subprocess.run([str(CHROME), *BASE, f'--window-size={w},{h}', f'--force-device-scale-factor={scale}',
                    f'--screenshot={png}', pathlib.Path(html).resolve().as_uri()],
                   check=True, capture_output=True)

def pdf(html, out):
    subprocess.run([str(CHROME), *BASE, '--no-pdf-header-footer', f'--print-to-pdf={out}',
                    pathlib.Path(html).resolve().as_uri()], check=True, capture_output=True)
