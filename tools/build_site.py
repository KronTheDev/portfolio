#!/usr/bin/env python3
"""Render content into the static site.

Source of truth: tools/content_strings.py (EN/FR/UK strings, CV rows).
This script rewrites:
  - translations.js  (skills → contact keys, about tags) for en / fr / uk
  - index.html       (Skills, Projects, Experience sections)
  - cv.html, cv.fr.html, cv.uk.html  (CV body)

Run from the repo root:  python3 tools/build_site.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
from content_strings import S, CV  # noqa: E402

LANGS = ['en', 'fr', 'uk']
T = S['en']

# ── Structure (order + non-translated data) ─────────────────────────────
SKILL_GROUPS = [
    ('sg_spoken',     ['@lang_uk', '@lang_fr', '@lang_en', '@lang_ru', '@lang_es']),
    ('sg_prog',       ['TypeScript', 'JavaScript', 'Python', 'Rust', 'HTML / CSS', 'UE Blueprint', 'SQL', '@sk_cpp', '@sk_cs']),
    ('sg_frameworks', ['Unreal Engine 5', 'Tauri', 'React', 'Node.js', 'llama.cpp', 'ratatui']),
    ('sg_tools',      ['Git + Git LFS', 'GitHub Actions', 'pnpm + Turborepo', 'Vitest', 'ESLint + commitlint', 'Docker Compose']),
    ('sg_systems',    ['Linux', 'Tailscale', '@sk_selfhost', 'Qdrant + SQLite', 'Arduino / ESP32', '@sk_print']),
    ('sg_other',      ['@sk_sales', 'Obsidian + Quartz', 'Lore Forge', '@sk_blender', '@sk_gdocs']),
]

PROJECTS = [  # id, title, badge key, stack, links
    ('ps',    'PsyPunker',      'badge_v01',      ['TypeScript', 'Rust', 'Tauri', 'React', 'Ed25519 + Argon2id', 'Turborepo'], []),
    ('lodge', 'Lodge',          'badge_active',   ['Rust', 'ratatui', 'llama.cpp', '172 tests'],
              [('GitHub ↗', 'https://github.com/KronTheDev/lodge')]),
    ('expo',  'Expo',           'badge_active',   ['Python', 'llama.cpp', 'Qdrant', 'Docker Compose', 'Tailscale'], []),
    ('atl',   'Above The Line', 'badge_paused',   ['Unreal Engine 5.6', 'UE Blueprint', 'Git LFS', 'Quartz'],
              [('GitHub ↗', 'https://github.com/KronStudios-Games/abovetheline')]),
    ('mono',  'Monochromality', 'badge_upcoming', ['Unreal Engine', 'UE Blueprint', 'HTML / CSS / JS'],
              [('Live ↗', 'https://kronthedev.github.io/monochromality/'),
               ('Steam ↗', 'https://store.steampowered.com/app/3744840/Monochromality/')]),
    ('em',    'EveryMotion',    'badge_closed',   ['HTML / CSS / JS', 'Computer Vision', 'RAG / AI'],
              [('GitHub ↗', 'https://github.com/KronTheDev/everymotion.github.io'),
               ('Live ↗', 'https://kronthedev.github.io/everymotion.github.io/')]),
]

EXPERIENCE = ['gr', 'expo', 'lodge', 'ps', 'ks', 'nc', 'em', 'reiu', 'wr', 'fun', 'tr']
WRITING = {'wr'}
HTML_KEYS = {k for k in T if k.endswith('_desc') and '<' in ''.join(S[l][k] for l in LANGS)}


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def text_el(tag, key, cls=None, i=''):
    c = f' class="{cls}"' if cls else ''
    if key in HTML_KEYS:
        return f'{i}<{tag}{c} data-i18n-html="{key}">{T[key]}</{tag}>'
    return f'{i}<{tag}{c} data-i18n="{key}">{esc(T[key])}</{tag}>'


# ── index.html sections ─────────────────────────────────────────────────
def render_index_sections():
    out = []
    out.append('  <!-- SKILLS -->')
    out.append('  <section id="skills" class="section-base">')
    out.append('    <div class="inner">')
    out.append(text_el('h2', 'skills_heading', i='      '))
    out.append(text_el('p', 'skills_sub', 'section-sub', '      '))
    out.append('      <div class="skills-grid">\n')
    for g, items in SKILL_GROUPS:
        out.append('        <div class="skill-group">')
        out.append(text_el('h3', g, i='          '))
        out.append('          <div class="pill-row">')
        for it in items:
            if it.startswith('@'):
                out.append(text_el('span', it[1:], 'pill', '            '))
            else:
                out.append(f'            <span class="pill">{esc(it)}</span>')
        out.append('          </div>')
        out.append('        </div>\n')
    out.append('      </div>')
    out.append('    </div>')
    out.append('  </section>\n')

    out.append('  <!-- PROJECTS -->')
    out.append('  <section id="projects" class="section-alt">')
    out.append('    <div class="inner">')
    out.append(text_el('h2', 'projects_heading', i='      '))
    out.append(text_el('p', 'projects_sub', 'section-sub', '      '))
    out.append('      <div class="projects-grid">\n')
    for pid, title, badge, stack, links in PROJECTS:
        out.append('        <div class="project-card">')
        out.append('          <div class="project-top">')
        out.append(f'            <h3>{esc(title)}</h3>')
        out.append(text_el('span', badge, 'status-badge', '            '))
        out.append('          </div>')
        out.append(text_el('p', f'proj_{pid}_desc', i='          '))
        out.append('          <div class="pill-row sm">')
        out += [f'            <span class="pill">{esc(s)}</span>' for s in stack]
        out.append('          </div>')
        if links:
            out.append('          <div class="project-links">')
            out += [f'            <a href="{u}" target="_blank" rel="noopener">{esc(l)}</a>' for l, u in links]
            out.append('          </div>')
        out.append('        </div>\n')
    out.append('      </div>')
    out.append('    </div>')
    out.append('  </section>\n')

    out.append('  <!-- EXPERIENCE -->')
    out.append('  <section id="experience" class="section-base">')
    out.append('    <div class="inner">')
    out.append(text_el('h2', 'experience_heading', i='      '))
    out.append(text_el('p', 'experience_sub', 'section-sub', '      '))
    out.append('      <div class="timeline">\n')
    for e in EXPERIENCE:
        w = e in WRITING
        out.append(f'        <div class="tl-item{" tl-writing" if w else ""}">')
        out.append(f'          <div class="tl-dot{" tl-dot-writing" if w else ""}"></div>')
        out.append('          <div class="tl-body">')
        out.append('            <div class="tl-header">')
        out.append(text_el('h3', f'exp_{e}_role', i='              '))
        out.append(text_el('span', f'exp_{e}_date', 'tl-date tl-date-writing' if w else 'tl-date', '              '))
        out.append('            </div>')
        out.append(text_el('p', f'exp_{e}_org', 'tl-org tl-org-writing' if w else 'tl-org', '            '))
        out.append(text_el('p', f'exp_{e}_desc', 'muted', '            '))
        out.append('          </div>')
        out.append('        </div>\n')
    out.append('      </div>')
    out.append('    </div>')
    out.append('  </section>\n')
    return '\n'.join(out) + '\n'


def build_index():
    p = ROOT / 'index.html'
    s = p.read_text(encoding='utf-8')
    a, b = s.index('  <!-- SKILLS -->'), s.index('  <!-- QUOTE / BREAK -->')
    s = s[:a] + render_index_sections() + s[b:]
    p.write_text(s, encoding='utf-8')


# ── translations.js ────────────────────────────────────────────────────
GEN_KEYS = [k for k in T if k not in ('tag_open', 'tag_domain')]


def js(v):
    return json.dumps(v, ensure_ascii=False)


def build_translations():
    p = ROOT / 'translations.js'
    s = p.read_text(encoding='utf-8')
    starts = {l: s.index(f'  {l}: {{') for l in LANGS}
    order = sorted(LANGS, key=lambda l: starts[l])
    for l in reversed(order):  # edit back-to-front so offsets stay valid
        st = starts[l]
        nxt = min([starts[o] for o in LANGS if starts[o] > st] + [len(s)])
        block = s[st:nxt]
        for k in ('tag_open', 'tag_domain'):
            block, n = re.subn(rf"{k}: (?:'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", f'{k}: {js(S[l][k])}', block, count=1)
            assert n == 1, (l, k)
        a = block.index('    skills_heading')   # generated keys run to the end of the block
        end = block.rindex('  },')
        lines = '\n'.join(f'    {k}: {js(S[l][k])},' for k in GEN_KEYS) + '\n'
        block = block[:a] + lines + block[end:]
        s = s[:st] + block + s[nxt:]
    p.write_text(s, encoding='utf-8')


# ── CV pages ───────────────────────────────────────────────────────────
def render_cv(l):
    c = CV[l]
    o = ['  <div class="cv-page">', '',
         '    <!-- HEADER -->',
         '    <header class="cv-header">',
         '      <div class="cv-name">Andriyan Pyrig</div>',
         '      <div class="cv-alias">Andrew Pie · KronTheDev</div>',
         '      <div class="cv-contact">',
         '        <a href="mailto:kronthedev@gmail.com">kronthedev@gmail.com</a>',
         '        <a href="https://github.com/KronTheDev" target="_blank">github.com/KronTheDev</a>',
         '        <span>Discord: @kronbrosgames</span>',
         f'        <span>{LOC[l]}</span>',
         '      </div>',
         '    </header>', '']

    def edu_block(title, rows):
        nonlocal o
        o.append('    <section class="cv-section">')
        o.append(f'      <div class="cv-section-title">{title}</div>')
        for name, date, sub in rows:
            o += ['      <div class="cv-edu-item">',
                  '        <div class="cv-edu-line">',
                  f'          <span class="cv-edu-name">{name}</span>',
                  f'          <span class="cv-edu-date">{date}</span>',
                  '        </div>',
                  f'        <div class="cv-edu-sub">{sub}</div>',
                  '      </div>']
        o += ['    </section>', '']

    edu_block(c['edu_title'], c['edu'])
    edu_block(c['free_title'], c['free'])
    edu_block(c['intern_title'], c['intern'])

    o.append('    <section class="cv-section">')
    o.append(f'      <div class="cv-section-title">{c["exp_title"]}</div>')
    for row in c['exp']:
        role, date, org, body = row[:4]
        w = len(row) > 4 and row[4]
        o += [f'      <div class="cv-exp-item{" cv-writing" if w else ""}">',
              '        <div class="cv-exp-header">',
              f'          <span class="cv-exp-role">{role}</span>',
              f'          <span class="cv-exp-date">{date}</span>',
              '        </div>',
              f'        <div class="cv-exp-org">{org}</div>',
              f'        <div class="cv-exp-body">{body}</div>',
              '      </div>']
    o += ['    </section>', '']

    o.append('    <section class="cv-section">')
    o.append(f'      <div class="cv-section-title">{c["skills_title"]}</div>')
    o.append('      <div class="cv-skills-grid">')
    o += [f'        <div class="cv-skill-row"><strong>{k}{" :" if l == "fr" else ":"}</strong> {v}</div>' for k, v in c['skills']]
    o += ['      </div>', '    </section>', '']

    o.append('    <section class="cv-section">')
    o.append(f'      <div class="cv-section-title">{c["langs_title"]}</div>')
    o.append('      <div class="cv-lang-row">')
    o += [f'        <span><strong>{k}</strong> — {v}</span>' for k, v in c['langs']]
    o += ['      </div>', '    </section>', '', '  </div>', '', '']
    return '\n'.join(o)


LOC = {'en': 'France / Ukraine', 'fr': 'France / Ukraine', 'uk': 'Франція / Україна'}


def build_cvs():
    for l, f in (('en', 'cv.html'), ('fr', 'cv.fr.html'), ('uk', 'cv.uk.html')):
        p = ROOT / f
        s = p.read_text(encoding='utf-8')
        a, b = s.index('  <div class="cv-page">'), s.index('</body>')
        s = s[:a] + render_cv(l) + s[b:]
        p.write_text(s, encoding='utf-8')


if __name__ == '__main__':
    build_index()
    build_translations()
    build_cvs()
    print('site rebuilt')
