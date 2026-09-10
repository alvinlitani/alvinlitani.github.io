"""Build the resume PDF locally, without Ruby or Jekyll.

Mirrors the steps in .github/workflows/resume.yml: render index.md through
_layouts/resume.html, serve the result over HTTP, print it with headless Edge,
then run check_pdf.py over the output.

    python .github/scripts/preview.py            # build preview.pdf
    python .github/scripts/preview.py --verify   # and prove it matches CI

This renders the markdown itself rather than running Jekyll, so it is only
trustworthy while index.md stays inside the subset it handles: headings,
paragraphs, emphasis, bold, links and flat lists. --verify is what keeps that
claim honest -- it compares the local PDF against the CI-built one committed in
the repo and fails if they diverge. Run it after any unusual markdown.
"""

import http.server
import os
import re
import shutil
import socket
import subprocess
import sys
import threading
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / ".github" / "scripts"
VENV = SCRIPTS / ".venv"
PREVIEW_DIR = ROOT / "_preview"
OUT_PDF = ROOT / "preview.pdf"
CI_PDF = ROOT / "Alvin Litani Liauw Resume.pdf"

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]


# --------------------------------------------------------------------------
# Dependencies live in their own venv so the global interpreter stays clean.
# Re-executes itself inside that venv on first run.
# --------------------------------------------------------------------------

def ensure_venv():
    vpy = VENV / ("Scripts" if os.name == "nt" else "bin") / (
        "python.exe" if os.name == "nt" else "python")
    if pathlib.Path(sys.prefix).resolve() == VENV.resolve():
        return None
    if not vpy.exists():
        print("first run: creating %s" % VENV.relative_to(ROOT))
        subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
        subprocess.run([str(vpy), "-m", "pip", "install", "--quiet",
                        "markdown", "pyyaml", "pdfminer.six"], check=True)
    return vpy


vpy = ensure_venv()
if vpy:
    sys.exit(subprocess.run([str(vpy), __file__] + sys.argv[1:]).returncode)

import yaml                     # noqa: E402
import markdown as md           # noqa: E402


# --------------------------------------------------------------------------
# Render
# --------------------------------------------------------------------------

def split_front_matter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    if not m:
        sys.exit("index.md has no YAML front matter")
    return yaml.safe_load(m.group(1)), m.group(2)


def render_layout(layout, page, content, baseurl, updated):
    """Fill the fixed set of Liquid tags used by _layouts/resume.html.

    Deliberately not a Liquid implementation. If the layout gains a tag this
    does not know, the leftover {{ }} or {% %} is detected below and reported
    rather than silently rendered into the page.
    """
    def rel(path):
        return (baseurl.rstrip("/") + path) if baseurl else path

    contacts = []
    for item in page.get("contact") or []:
        text, url = item.get("text", ""), item.get("url")
        inner = '<a href="%s">%s</a>' % (url, text) if url else text
        contacts.append("<span>%s</span>" % inner)

    out = layout

    # {% if page.headline %}...{% endif %} and the location guard
    out = re.sub(r"\{%\s*if page\.headline\s*%\}(.*?)\{%\s*endif\s*%\}",
                 (lambda m: m.group(1)) if page.get("headline") else "",
                 out, flags=re.S)
    out = re.sub(r"\{%\s*if page\.location\s*%\}(.*?)\{%\s*endif\s*%\}",
                 (lambda m: m.group(1)) if page.get("location") else "",
                 out, flags=re.S)

    # the contact loop, replaced wholesale
    out = re.sub(r"\{%\s*for item in page\.contact\s*%\}.*?\{%\s*endfor\s*%\}",
                 lambda m: "\n          ".join(contacts), out, flags=re.S)

    # '/path' | relative_url
    out = re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}",
                 lambda m: rel(m.group(1)), out)

    # site.time | date: "..."
    out = re.sub(r"\{\{\s*site\.time\s*\|\s*date:[^}]*\}\}",
                 lambda m: updated, out)

    for key in ("fullname", "headline", "location"):
        out = re.sub(r"\{\{\s*page\.%s\s*\}\}" % key,
                     lambda m, k=key: str(page.get(k, "")), out)

    out = out.replace("{{ content }}", content)

    leftover = re.findall(r"\{\{.*?\}\}|\{%.*?%\}", out, re.S)
    if leftover:
        sys.exit("preview.py does not understand these layout tags, so the "
                 "output would not match Jekyll:\n  " +
                 "\n  ".join(t.strip() for t in leftover))
    return out


def build():
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    page, body = split_front_matter((ROOT / "index.md").read_text(encoding="utf-8"))
    layout = (ROOT / "_layouts" / "resume.html").read_text(encoding="utf-8")

    # Jekyll stamps site.time at build time; match its "%B %Y".
    import datetime
    updated = datetime.date.today().strftime("%B %Y")

    content = md.markdown(body, extensions=["extra", "sane_lists"])
    html = render_layout(layout, page, content, config.get("baseurl") or "", updated)

    if PREVIEW_DIR.exists():
        shutil.rmtree(PREVIEW_DIR)
    PREVIEW_DIR.mkdir()
    (PREVIEW_DIR / "index.html").write_text(html, encoding="utf-8")
    shutil.copytree(ROOT / "assets", PREVIEW_DIR / "assets")
    return html


# --------------------------------------------------------------------------
# Serve + print
# --------------------------------------------------------------------------

def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve(directory, port):
    handler = lambda *a, **kw: QuietHandler(*a, directory=str(directory), **kw)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def find_browser():
    for path in EDGE_CANDIDATES:
        if pathlib.Path(path).exists():
            return path
    sys.exit("no Edge or Chrome found; looked in:\n  " + "\n  ".join(EDGE_CANDIDATES))


def render_pdf():
    # Served over HTTP, never file:// -- the layout asks for /assets/style.css
    # absolutely, which under file:// resolves to the filesystem root and the
    # stylesheet silently fails to load.
    port = free_port()
    httpd = serve(PREVIEW_DIR, port)
    profile = PREVIEW_DIR / ".browser-profile"
    try:
        if OUT_PDF.exists():
            OUT_PDF.unlink()
        proc = subprocess.run(
            [find_browser(), "--headless=new", "--disable-gpu",
             "--no-first-run", "--no-default-browser-check",
             "--user-data-dir=%s" % profile,
             "--no-pdf-header-footer", "--print-to-pdf=%s" % OUT_PDF,
             "http://127.0.0.1:%d/" % port],
            capture_output=True, text=True, timeout=180)
        # On Windows the launcher returns 0 immediately and a child process
        # does the rendering, so the file appears after the call returns.
        # Wait for it to show up and stop growing before trusting it.
        wait_for_pdf(proc)
    finally:
        httpd.shutdown()


def wait_for_pdf(proc, timeout=90.0):
    import time
    deadline = time.time() + timeout
    last, stable = -1, 0
    while time.time() < deadline:
        size = OUT_PDF.stat().st_size if OUT_PDF.exists() else -1
        if size > 0 and size == last:
            stable += 1
            if stable >= 3:          # ~0.6s unchanged: writing has finished
                return
        else:
            stable = 0
        last = size
        time.sleep(0.2)
    sys.exit("the browser produced no usable PDF within %ds (exit %s)\n%s"
             % (timeout, proc.returncode,
                (proc.stderr or proc.stdout or "").strip()[-1500:]))


# --------------------------------------------------------------------------
# Verify against the PDF that CI built
# --------------------------------------------------------------------------

def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def verify():
    from pdfminer.high_level import extract_text
    from pdfminer.pdfpage import PDFPage

    if not CI_PDF.exists():
        sys.exit("no CI-built PDF in the repo to compare against")

    dirty = subprocess.run(["git", "status", "--porcelain", "--", "index.md",
                            "_layouts", "assets", "_config.yml"],
                           cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if dirty:
        print("\nSKIPPED verification: these are modified locally, so the "
              "committed PDF was built from different input:")
        print("  " + "\n  ".join(dirty.splitlines()))
        print("  Commit and push, let CI rebuild, then re-run --verify.")
        return 0

    def pages(p):
        with open(p, "rb") as fh:
            return len(list(PDFPage.get_pages(fh)))

    mine, theirs = pages(OUT_PDF), pages(CI_PDF)
    my_text, their_text = norm(extract_text(str(OUT_PDF))), norm(extract_text(str(CI_PDF)))

    problems = []
    if mine != theirs:
        problems.append("page count differs: preview %d, CI %d" % (mine, theirs))
    if my_text != their_text:
        import difflib
        problems.append("extracted text differs")
        diff = list(difflib.unified_diff(their_text.split(), my_text.split(),
                                         "CI", "preview", n=2, lineterm=""))
        problems.append("  " + " ".join(diff[:40]))

    if problems:
        print("\nVERIFY FAILED -- this renderer is not equivalent to Jekyll here:")
        for p in problems:
            print("  - " + p)
        print("\n  Use the portable-Ruby fallback for an exact build.")
        return 1

    print("\nVERIFIED identical to the CI-built PDF (%d pages, text matches)." % mine)
    return 0


def main():
    build()
    render_pdf()
    print("wrote %s" % OUT_PDF.relative_to(ROOT))

    rc = subprocess.run([sys.executable, str(SCRIPTS / "check_pdf.py"), str(OUT_PDF)],
                        cwd=ROOT).returncode

    if "--verify" in sys.argv:
        rc = verify() or rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
