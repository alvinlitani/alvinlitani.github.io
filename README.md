# Markdown resume on GitHub Pages

Edit `index.md`, push, and GitHub rebuilds the page. No local Ruby install, no
build step you run yourself, no JavaScript needed to render the resume.

```
.
├── _config.yml            site config — check baseurl before your first push
├── index.md               ← the only file you edit regularly
├── _layouts/
│   └── resume.html        page shell, masthead, print button
└── assets/
    └── style.css          screen + print styles
```

## Setting it up

1. Create a repo and copy these four files in, keeping the folder structure.
2. Push to the `main` branch.
3. Repo → **Settings** → **Pages** → set **Source** to *Deploy from a branch*,
   branch `main`, folder `/ (root)`. Save.
4. Wait about a minute. The URL appears at the top of that same settings page.

**Set `baseurl` before you do.** In `_config.yml`:

- Repo named `resume` → site lives at `username.github.io/resume/` → `baseurl: "/resume"`
- Repo named `username.github.io` → site lives at the root → `baseurl: ""`

Getting this wrong loads the page with no styling at all, which is the single
most common way this setup breaks.

## Previewing locally

Optional. Pushing and waiting ~30 seconds works fine. If you want a faster loop,
from the repo root:

```bash
docker run --rm -p 4000:4000 -v "$PWD:/srv/jekyll" jekyll/jekyll \
  jekyll serve --host 0.0.0.0
```

Then open `http://localhost:4000`. Set `baseurl: ""` while previewing locally and
remember to set it back before pushing.

## Markdown conventions

The stylesheet reads structure from plain markdown. Two conventions matter:

**A role heading is `###`, and the line under it is the meta line.**

```markdown
### Application and server administrator
*PT Midtrans — 2013 to 2015, Jakarta, Indonesia*

- Bullet.
- Bullet.
```

The paragraph directly after any `###` is styled small, italic, and grey. Use it
for dates, employer, location, or a project's stack. Anything else there will
look wrong.

**Section headings are `##`** and get the hairline rule above them.

Name, headline, location, and contact links live in the YAML front matter at the
top of `index.md`, not in the body. Add or remove contact entries freely — they
lay out in a wrapping row.

The name key is `fullname`, not `name`. Jekyll reserves `page.name` for the
source filename, so a front matter `name:` is silently ignored and the masthead
renders "index.md" instead of yours.

## The PDF

The button calls `window.print()`. In the dialog, choose **Save as PDF** as the
destination. The output is real selectable text, so applicant tracking systems
can parse it — this is why the button isn't a one-click JS download. Libraries
like html2pdf.js screenshot the page into an image, and an ATS reading that sees
a blank document.

Two dialog settings to check the first time:

- **Margins: Default.** The stylesheet sets `@page` margins to 0.55in × 0.65in.
  Overriding to "None" double-counts and crops.
- **Headers and footers: off.** Otherwise the browser stamps the URL and date
  across your resume.

Page size is set to US Letter, which is standard in Canada. Change `size: letter`
to `size: a4` in the `@page` rule if you're applying somewhere that expects A4.

### Fitting to one page

Adjust in `assets/style.css` inside `@media print`, in this order:

1. `body { font-size: 10.5pt }` — 10pt still reads fine, 9.5pt is the floor.
2. `body { line-height: 1.4 }` — 1.32 buys noticeable space.
3. `h2 { margin: 15pt 0 7pt }` — the space between sections.
4. `@page { margin: 0.55in 0.65in }` — 0.4in is about as tight as looks
   deliberate rather than cramped.

If a job's bullets split awkwardly across pages, `ul { break-inside: avoid }` is
already keeping each list together. Remove that rule if you'd rather allow a
split than accept a large gap.

## Before you send this anywhere

`index.md` has placeholders in square brackets — the consultancy name, two city
names, the certificate institution, and your email and LinkedIn handle in the
front matter. Search for `[` and `example.com` to find them.

The bullets describe what you built but carry no numbers. One number per role,
where you have an honest one, does more than any styling here.
