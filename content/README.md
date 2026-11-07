# content/

Single source of truth for everything the portfolio and CV say.

- `portfolio.yaml` holds the English content, section by section, in the order the site shows it.
- `index.html`, `cv*.html` and `translations.js` render this content. When the content changes here, those files follow.
- Git history is the version history: every content change is its own commit, so `git log -p content/portfolio.yaml` shows what changed and when.

## Fields

- `source` says where a fact comes from: `fields.md` is the spring 2026 portfolio fill-out sheet; `fNNNN` / `dNNN` are reviewed fact ids from the personal knowledge base (Expo identity corpus, reviewed 2026-10-16/17).
- `as_of` is the date the fact was last confirmed.
- `show: false` keeps an entry in the record without rendering it.

## Workflow

1. Edit `portfolio.yaml` (or let Claude apply new material to it).
2. Review the diff.
3. Sync `index.html`, `cv*.html` and `translations.js` (FR/UK) to match.
