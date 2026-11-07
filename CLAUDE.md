# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal portfolio site for **Andrew Pie (KronTheDev)**, deployed via GitHub Pages. Pure static HTML/CSS/JS — no build tools, no package manager, no framework.

**Long-term goals:**
- Dynamically-expanding project section that reflects GitHub repository progress and personal input.
- One-click export of an application-grade PDF CV (client-side `@media print` or server-side via Hetzner, TBD).

## Development

Open `index.html` directly in a browser or use any static file server:

```bash
python -m http.server 8080
# or
npx serve .
```

No lint or test commands. Skills, Projects, Experience, their FR/UK translations and the bodies of `cv.html`, `cv.fr.html`, `cv.uk.html` are generated: edit `tools/content_strings.py` (and the order/links lists in `tools/build_site.py`), then run `python3 tools/build_site.py`. Never hand-edit those generated sections. Nav, hero, about and contact are hand-written in `index.html` + `translations.js`.

## Architecture

Single-page layout (`index.html`) with one stylesheet (`style.css`) and one script (`script.js`). All sections live in `index.html`; no routing.

### Sections (in order)
| Section | ID | Notes |
|---|---|---|
| Nav | `.topbar` | Fixed, blur, dark. CV button (`.cv-btn`) links to `cv.html` / `cv.<lang>.html` for the active language. |
| Hero | `#hero` | Full viewport. Role typewriter cycles via `loopRoles()` in `script.js`. |
| About | `#about` | Two-col layout with `assets/about_profile.png`. |
| Skills | `#skills` | Generated. `skill-group` cards auto-fit into a responsive grid. |
| Projects | `#projects` | Generated. Each card: title, status badge, description, tech pills, optional links. |
| Experience | `#experience` | Generated. CSS timeline of `.tl-item` blocks; `tl-writing` marks the parallel writing entry. |
| Vision break | *(no ID)* | VT323 quote between experience and contact. |
| Contact | `#contact` | Three `.contact-chip` links. |

### script.js systems

1. **Canvas trail** — purple `rgba(102,117,255,...)` trail on `mousemove`. Disabled entirely on mobile (`isMobile()`). Toggle controlled by `#trailWidget` (bottom-left). `TRAIL_ENABLED` flag gates both the RAF loop and new point accumulation.

2. **Role typewriter** — `loopRoles()` async-loops through `TRANSLATIONS[lang].roles`, typing and erasing each entry into `#roleType`. Edit the `roles` arrays in `translations.js`.

4. **Language switch** — `applyTranslation()` fills every `data-i18n` / `data-i18n-html` element from `translations.js` (en / fr / uk) and remembers the choice in `localStorage`.

3. **Smooth scroll** — all `<a href="#...">` links use `scrollIntoView({ behavior: 'smooth' })`. No library needed.

### Style conventions
- Accent color: `#6675ff` (blue-purple). Used for active states, dots, links, badges.
- Dark surfaces: `#0e0e0e` base, `#111` alternate sections.
- Section headings: `font-family: 'Orbitron'`.
- Retro accent labels: `font-family: 'VT323'` (eyebrow text, quote, photo placeholder).
- Skill group labels: `font-family: 'Jersey 10'`.
