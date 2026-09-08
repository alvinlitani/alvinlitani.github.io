"""Check the rendered resume PDF the way an applicant tracking system would.

Fails the build on the things that make a resume unreadable to a parser, and
only warns about page count.
"""

import os
import re
import sys
import pathlib

from pdfminer.high_level import extract_text
from pdfminer.pdfpage import PDFPage

pdf = pathlib.Path(sys.argv[1])
text = extract_text(str(pdf))

with open(pdf, "rb") as fh:
    pages = len(list(PDFPage.get_pages(fh)))

failures = []

# 1. The masthead has to survive. This is what the previous pandoc pipeline
#    silently dropped: front matter stripped, layout never applied, so the
#    PDF carried no name or contact details at all.
for needed in ("Alvin Litani Liauw", "alvin.litani@gmail.com"):
    if needed not in text:
        failures.append(f"missing from extracted text: {needed!r}")

# 2. Bullets must extract as markers at the start of their line. The marker is
#    a CSS ::before with position:absolute, so it is drawn in a separate text
#    run from the bullet body — if it lands after the text, a parser sees no
#    list at all.
expected = len(re.findall(r"^- ", pathlib.Path("index.md").read_text(encoding="utf-8"), re.M))
leading = len([ln for ln in text.splitlines() if ln.strip().startswith("•")])

if expected and leading < expected * 0.6:
    failures.append(
        f"only {leading} of {expected} bullets extract with a leading marker; "
        "the ::before marker is probably drawn out of order"
    )

# 3. Real text, not a scan.
if len(text.strip()) < 1000:
    failures.append(f"extracted only {len(text.strip())} characters; PDF may not be real text")

summary = [
    "### Resume PDF",
    "",
    f"- Pages: **{pages}**",
    f"- Extracted characters: {len(text.strip())}",
    f"- Bullets with leading marker: {leading} of {expected} in index.md",
]

if pages > 2:
    summary.append(f"- :warning: **{pages} pages** — this used to fit on 2.")

step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
if step_summary:
    with open(step_summary, "a", encoding="utf-8") as fh:
        fh.write("\n".join(summary) + "\n")
print("\n".join(summary))

if failures:
    print("\nFAILED:", file=sys.stderr)
    for f in failures:
        print(f"  - {f}", file=sys.stderr)
    sys.exit(1)

print("\nOK")
