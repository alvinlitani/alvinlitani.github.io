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

# 2. Each bullet must extract as marker AND text on one line. Counting lines
#    that merely start with the marker is not enough: when the ::before is
#    taken out of the normal flow, the markers extract as their own lines and
#    such a check passes while the list is in fact shredded.
expected = len(re.findall(r"^- ", pathlib.Path("index.md").read_text(encoding="utf-8"), re.M))
lines = text.splitlines()
attached = len([ln for ln in lines if re.match(r"^\s*-\s+\S", ln)])
orphan = len([ln for ln in lines if re.match(r"^\s*-\s*$", ln)])

if orphan:
    failures.append(
        f"{orphan} bullet markers extract detached from their text; "
        "the ::before marker has left the normal inline flow"
    )

if expected and attached < expected * 0.9:
    failures.append(
        f"only {attached} of {expected} bullets extract as marker + text on one line"
    )

# 3. Real text, not a scan.
if len(text.strip()) < 1000:
    failures.append(f"extracted only {len(text.strip())} characters; PDF may not be real text")

summary = [
    "### Resume PDF",
    "",
    f"- Pages: **{pages}**",
    f"- Extracted characters: {len(text.strip())}",
    f"- Bullets extracting as marker + text: {attached} of {expected}",
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
