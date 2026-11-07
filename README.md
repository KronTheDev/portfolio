# Andrew Pie — Portfolio

Personal portfolio and CV of **Andrew Pie (KronTheDev)**, live at [kronthedev.xyz](https://kronthedev.xyz).

The site presents my projects, experience and skills in English, French and Ukrainian, with a printable CV in each language.

## Features

- **Three languages, one source.** Every string on the site and in the CVs lives in a single file per language. A build step generates the page text and all three CVs from those files, and refuses to build if one language is missing a key. French and Ukrainian are written natively rather than translated word for word.
- **Printable CVs.** `cv.html`, `cv.fr.html` and `cv.uk.html` are styled for A4 print, so "Save as PDF" in the browser produces an application-ready CV.
- **No framework.** Plain HTML, CSS and JavaScript, served as static files by GitHub Pages. No package manager or runtime dependencies.
- **Interactive details.** A role typewriter, a cursor trail that can be toggled off (and is disabled on mobile), and a language switch that remembers your choice.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | Single-page layout: hero, about, skills, projects, experience, contact |
| `style.css`, `script.js` | Styling and interactive behaviour |
| `translations.js` | Generated page text for all three languages |
| `cv.html`, `cv.fr.html`, `cv.uk.html` | Printable CVs (generated content) |
| `tools/locales/` | Source text: `en.py`, `fr.py`, `uk.py` |
| `tools/build_site.py` | Renders the locales into the site and CVs |

## Updating content

Edit the relevant entries in `tools/locales/`, then rebuild:

```bash
python3 tools/build_site.py
```

Section order, tech pills and project links are defined in `tools/build_site.py`. Generated sections should not be edited by hand.

## Local preview

```bash
python3 -m http.server 8080
```

Then open <http://localhost:8080>.

## How this was built

I designed the site, its content model and the multilingual build pipeline, and I wrote and reviewed the content it presents. Implementation was done with [Claude Code](https://claude.com/claude-code), Anthropic's AI coding assistant, working under my direction: I defined the architecture and requirements, and reviewed and approved every change before merging. Commits made with its help are marked with a `Co-Authored-By: Claude` trailer.

## Licence

© Andrew Pie. All rights reserved. The code and content are shared for viewing; please ask before reusing them.
