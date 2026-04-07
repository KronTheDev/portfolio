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

No lint, build, or test commands.

## Architecture

Single-page layout (`index.html`) with one stylesheet (`style.css`) and one script (`script.js`). All sections live in `index.html`; no routing.

### Sections (in order)
| Section | ID | Notes |
|---|---|---|
| Nav | `.topbar` | Fixed, blur, dark. CV download button (`.cv-btn`) currently `href="#"` — wire to a PDF when ready. |
| Hero | `#hero` | Full viewport. Role typewriter cycles via `loopRoles()` in `script.js`. |
| About | `#about` | Two-col layout. Photo placeholder is a CSS circle — replace `.photo-placeholder` with an `<img>`. |
| Skills | `#skills` | Four `skill-group` cards auto-fit into a responsive grid. Add/remove groups freely. |
| Projects | `#projects` | Three placeholder cards. Each card has: title, status badge, description, tech pills, links. |
| Experience | `#experience` | Vertical timeline driven purely by CSS. Add `.tl-item` blocks; the connecting line adjusts automatically. |
| Vision break | *(no ID)* | VT323 quote between experience and contact. |
| Contact | `#contact` | Three `.contact-chip` links. |

### script.js systems

1. **Canvas trail** — purple `rgba(102,117,255,...)` trail on `mousemove`. Disabled entirely on mobile (`isMobile()`). Toggle controlled by `#trailWidget` (bottom-left). `TRAIL_ENABLED` flag gates both the RAF loop and new point accumulation.

2. **Role typewriter** — `loopRoles()` async-loops through the `roles` array, typing and erasing each entry into `#roleType`. To change the cycling roles, edit the `roles` array in `script.js`.

3. **Smooth scroll** — all `<a href="#...">` links use `scrollIntoView({ behavior: 'smooth' })`. No library needed.

### Style conventions
- Accent color: `#6675ff` (blue-purple). Used for active states, dots, links, badges.
- Dark surfaces: `#0e0e0e` base, `#111` alternate sections.
- Section headings: `font-family: 'Orbitron'`.
- Retro accent labels: `font-family: 'VT323'` (eyebrow text, quote, photo placeholder).
- Skill group labels: `font-family: 'Jersey 10'`.
- All placeholder content uses `[bracket]` notation — easy to grep for unfilled fields.
