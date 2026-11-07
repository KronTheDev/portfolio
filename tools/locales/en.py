# -*- coding: utf-8 -*-
"""English: the reference locale. fr.py and uk.py must define the same keys."""

STRINGS = {'nav_home': 'Home',
 'nav_about': 'About',
 'nav_skills': 'Skills',
 'nav_projects': 'Projects',
 'nav_experience': 'Experience',
 'nav_contact': 'Contact',
 'hero_eyebrow': 'I bid you, Welcome',
 'roles': ['Developer', 'Systems Engineer', 'Game Designer', 'Lore Architect', 'Scriptwriter'],
 'hero_cta_view': 'View Work',
 'hero_cta_touch': 'Get in Touch',
 'hero_tagline': "The future won't come for us. Never. Yet we must strive towards it. Always.",
 'about_heading': 'About Me',
 'bio_hey': '"Hey,"',
 'bio_p1_l1': "You've seen that opener before. So let's get to it: I'm <span "
              'id="glitchName">Andrew</span> — and I build things that probably shouldn\'t belong in the '
              'same portfolio.',
 'bio_p1_l2': 'Code, systems, worlds, and the words that hold them together.',
 'bio_p1_l3': "I'm Ukrainian and French, fluent across four languages — and passable in a fifth, <em>though "
              "I wouldn't recommend it.</em> Somewhere between the text editor and the worlds that don't "
              'exist yet, that tends to show up in the work.',
 'bio_p1_l4': 'This portfolio is the longer version.',
 'bio_p1_l5': 'Scroll down to see where that lands.',
 'bio_p2': "Right now I'm focused on the space where those disciplines actually overlap — where a system "
           'needs a story to make sense, or a story needs a system to hold its weight. Most people pick a '
           "lane. I've never been particularly good at that.<br>What I'm building toward is work that "
           "doesn't need a genre label. Games that read like literature. Narratives that function like "
           'architecture. Code that serves something larger than itself, while still having a self. In '
           "short, a vague reflection of what I embody.<br>The distinction, if there is one: I don't treat "
           'any of these as separate crafts. They inform and <em>interlap</em> each other '
           'constantly.<br>Their <em>cross-contamination</em> is usually where the most interesting work '
           'comes from, speaking from experience.',
 'tag_location': 'France / Ukraine',
 'tag_open': 'Freelance · Internship · Collaboration · Sales',
 'tag_domain': 'Web · Game Dev · AI · Backend · B2B Sales',
 'skills_heading': 'Skills',
 'skills_sub': 'What I work with — grouped by category.',
 'sg_spoken': 'Spoken Languages',
 'sg_prog': 'Programming Languages',
 'sg_frameworks': 'Frameworks / Runtimes',
 'sg_tools': 'Tools / Infrastructure',
 'sg_systems': 'Systems / Hardware',
 'sg_other': 'Other',
 'lang_uk': 'Ukrainian — native',
 'lang_fr': 'French — fluent',
 'lang_en': 'English — fluent',
 'lang_ru': 'Russian — passive',
 'lang_es': 'Spanish — moderate',
 'sk_cpp': 'C++ (familiar)',
 'sk_cs': 'C# (familiar)',
 'sk_selfhost': 'Self-hosting',
 'sk_print': '3D printing',
 'sk_blender': 'Blender (basic)',
 'sk_gdocs': 'Scriptwriting',
 'sk_sales': 'Consultative sales',
 'projects_heading': 'Projects',
 'projects_sub': 'Selected work — shipped builds, active systems, and ongoing initiatives.',
 'badge_v01': 'v0.1.0 — Shipped',
 'badge_active': 'In development',
 'badge_paused': 'Paused',
 'badge_upcoming': 'Upcoming',
 'badge_closed': 'Closed',
 'proj_ps_desc': 'A physical-key execution platform: insert a drive, a world opens. A Tauri desktop app '
                 'split into a Builder (React + Monaco visual editor, compile and signing pipeline) and a '
                 "Runner that validates the drive's key and renders the Kernel as a fullscreen overlay "
                 'isolated from the host — drive out, session gone, zero trace. Phase 1 shipped as v0.1.0 '
                 'with 263 tests and CI, release and security workflows. Its enterprise tier, MitoData, '
                 'comes later.',
 'proj_lodge_desc': 'A language-agnostic installer runtime with a conversational terminal interface. Lodge '
                    'reads a manifest that describes what a package is, works out where each file belongs on '
                    'Windows, macOS or Linux, and runs the install live in a cabin-themed terminal UI. A '
                    'bundled offline model understands plain-English commands like "do I have git?" — 5 '
                    'crates, 172 tests.',
 'proj_expo_desc': 'A local-first, voice-first personal AI running entirely on my own hardware. An always-on '
                   'low-power server handles fast triage with a small local LLM, semantic intent routing, '
                   'live lookups and long-term RAG memory with nightly consolidation; a GPU rig takes the '
                   'heavy inference. Self-hosted end to end, with a regression suite run after every '
                   'rebuild.',
 'proj_atl_desc': 'A first-person vertical narrative survival game set after the Yellowstone supereruption '
                  "of Labor Day 2039 reshapes Vancouver's atmosphere. Society splits by elevation, above or "
                  'below a toxic gas cloud; the player leaves the fragile safety of a high-rise and travels '
                  'upward. Unreal Engine 5.6, (semi-)diegetic UI. Project Director & Narrative Lead under '
                  'KronStudios-Games.',
 'proj_mono_desc': 'A Backrooms-inspired first-person horror game by Null Concept, coming to Steam Early '
                   'Access. 15 mapped levels planned at release, each with its own hazards and ambiance, and '
                   'three predators — the Howler, the Hounds and the Duller. I shaped its lore, handled '
                   'logistics and translation, and built its official website.',
 'proj_em_desc': 'An AI-powered, controller-free motion tracking concept for AR/VR — computer vision plus '
                 'RAG-enhanced prediction, no sensors, no controllers. I founded it, set the technical '
                 'vision and built its public site before the venture shut down.',
 'experience_heading': 'Experience',
 'experience_sub': 'Independent initiatives and freelance work — no salaried employment, no pretence '
                   'otherwise.',
 'exp_gr_role': 'Freelance Sales Representative',
 'exp_gr_date': 'Nov 2026',
 'exp_gr_org': 'Grondia — Swiss campsite-management SaaS',
 'exp_gr_desc': "Prepared and co-led a French-language remote sales call with the founder on 50 minutes' "
                'notice, tailoring the pitch to a ~100-pitch Swiss campsite — seasonal contracts, point of '
                'sale, CHF and TWINT payments, Swiss data hosting — and handling questions on pricing, '
                'migration and data location. The founder\'s verdict: <em>"literally perfect."</em> Then a '
                'full day representing Grondia on its stand at SETT 2026 in Montpellier, qualifying campsite '
                'operators and booking demos.',
 'exp_expo_role': 'Creator & Systems Engineer',
 'exp_expo_date': '2026 — Present',
 'exp_expo_org': 'Expo — personal AI infrastructure',
 'exp_expo_desc': 'Designing and building a self-hosted personal AI across two machines: an always-on server '
                  'running local LLM triage, intent routing, RAG memory and a chat interface, and a GPU rig '
                  'for heavy inference. Docker Compose, Tailscale, llama.cpp, Qdrant and SQLite, with a '
                  'regression suite and nightly self-evaluation.',
 'exp_lodge_role': 'Creator & Lead Developer',
 'exp_lodge_date': 'Apr 2026 — Present',
 'exp_lodge_org': 'Lodge',
 'exp_lodge_desc': 'Built a Rust installer runtime with a natural-language terminal interface, a bundled '
                   'offline model, OS placement rulesets for Windows, macOS and Linux, and an extension '
                   'registry with automated validation. 5 crates, 172 tests, Apache-2.0.',
 'exp_ps_role': 'Founder & Lead Developer',
 'exp_ps_date': '2026 — Present',
 'exp_ps_org': 'PsyPunker',
 'exp_ps_desc': 'Sole architect and developer of a USB-bound cryptographic Kernel execution platform. '
                'Designed the full system architecture — signing pipeline, sandbox model, drive-identity '
                'binding, a 20-vector threat model — and built a TypeScript + Rust monorepo with Tauri, '
                'React, pnpm and Turborepo. Shipped Phase 1 as v0.1.0 (April 2026) with 263 tests and CI, '
                'release and security workflows.',
 'exp_ks_role': 'Co-Founder & President · Project Director & Narrative Lead',
 'exp_ks_date': '2025 — Present',
 'exp_ks_org': 'KronStudios-Games — Above The Line',
 'exp_ks_desc': 'Co-founded and lead, as President, a volunteer revenue-share indie studio of about nine '
                'people producing Above The Line in Unreal Engine 5.6. Responsible for project direction, '
                'narrative design, lore architecture and team coordination. Set up phased milestones, a '
                'protected-branch PR workflow, STAR-based recruiting, a merit-weighted revenue-share '
                'agreement and a Quartz GDD wiki; built the studio website.',
 'exp_nc_role': 'Logistics & Suggestions Manager · Lore Writer · Gameplay Overseer · Translator',
 'exp_nc_date': 'Apr 2025 — Nov 2025',
 'exp_nc_org': 'Null Concept — Monochromality',
 'exp_nc_desc': "Joined early and shaped the game's direction with Backrooms lore frameworks drawn from the "
                'Wikidot canon. Cross-functional role across logistics, coordination, lore writing, gameplay '
                'oversight, partial voice acting and translation; built the official website. Stepped back '
                'over sustained deadline slips and diverging creative vision.',
 'exp_em_role': 'CEO, Owner & Lead Developer',
 'exp_em_date': '2025 — 2026',
 'exp_em_org': 'EveryMotion',
 'exp_em_desc': 'Founded and led an AI-powered motion tracking startup concept targeting AR/VR. Defined the '
                'technical vision (computer vision, RAG-enhanced prediction), built the public-facing web '
                'presence, and managed the early team and product roadmap before the venture shut down.',
 'exp_reiu_role': 'Co-Founder & Lead Manager',
 'exp_reiu_date': 'Aug 2023 — Feb 2024',
 'exp_reiu_org': 'REIU-V — SCP Roleplay Server',
 'exp_reiu_desc': 'Founded and maintained an SCP-themed roleplay Discord community that grew to ~150 members '
                  'during tenure and accelerated to 900+ after departure. Managed server infrastructure, '
                  'community moderation, and narrative frameworks.',
 'exp_wr_role': 'Writer',
 'exp_wr_date': '~2023 — Present',
 'exp_wr_org': 'Independent · Backrooms Wikidot · REIU-V · Personal',
 'exp_wr_desc': 'Writing has run as a parallel thread across almost every initiative. The first serious '
                'application was the REIU-V community: original in-universe documents in clinical SCP format '
                '— technical protocols, anomalous research logs, consciousness-overwriting procedures — with '
                'a new batch written for its commemoration event in August 2025.<br><br>Active on the '
                'Backrooms Wikidot Feb–Aug 2025: published articles, collaborative pieces, and contest '
                'submissions including the <em>Despair Writings</em> contest. Most prominent published work: '
                '<a href="https://backrooms-wiki.wikidot.com/level-360" target="_blank" rel="noopener" '
                'class="tl-link">Level 360 ↗</a> <em>"Halls of Past Screams"</em> (+17).<br><br>From late '
                '2025: novel and screenplay writing, both in progress. <em>A Sound Sinner</em> — a '
                'Tarantino-structured post-apocalyptic screenplay. <em>Information Paradox</em> — literary '
                'science fiction, quieter register. Running concurrently: the Above The Line prologue and '
                'story summary, the narrative foundation before a single line of code.',
 'exp_fun_role': 'Founder & Project Manager',
 'exp_fun_date': '~2023 — Never shipped',
 'exp_fun_org': 'Subject To F.U.N (Fourth-Wall Understanding Network)',
 'exp_fun_desc': 'A KronStudios concept — a fourth-wall-breaking action puzzle thriller in the vein of '
                 'Portal and The Stanley Parable. The title itself was a sarcastic joke built into the '
                 'premise. Never reached a single line of production code. Revision 0.01 is the entire paper '
                 'trail it left behind.',
 'exp_tr_role': 'Founder & Lead',
 'exp_tr_date': '~2022 — ~2023',
 'exp_tr_org': 'T||RUTHLESS — First KronStudios Initiative',
 'exp_tr_desc': 'Founded and directed the first KronStudios initiative: a narrative-driven UE5 shooter with '
                'a semi-free-choice storyline. The title — a deliberate dual-read: <em>Ruthless</em> on '
                'first glance, <em>Truthless</em> on closer inspection — embedded into the story of a '
                'soldier named Rad Bronx, uncovering a century-old government conspiracy through I.R.I.S. '
                'Project Manager and Head UE5 Developer across ~15 people. Never reached a playable build. '
                'The foundational leadership lesson that shaped everything after.',
 'vision_quote': '"Everything I make is an argument that these things belong together."',
 'contact_heading': 'Get in Touch',
 'contact_sub': 'Open to freelance, internships, collaborations and sales work.'}

CV = {'edu_title': 'Education',
 'free_title': 'Freelance',
 'intern_title': 'Internship',
 'exp_title': 'Experience',
 'skills_title': 'Technical Skills',
 'langs_title': 'Languages',
 'edu': [('Université de Montpellier',
          'Sept 2026 – Present',
          'Licence Informatique (Computer Science), first year'),
         ('Lycée Rosa Luxemburg — Canet-en-Roussillon', 'Jan – June 2026', 'Terminale · Baccalauréat'),
         ('Lycée Jules Siegfried — Le Havre',
          '2023 – Dec 2025',
          'Seconde · Première · Terminale (first semester)'),
         ('Collège Belle Etoile — Montivilliers', '2023', 'Diplôme national du Brevet, Mention Très Bien')],
 'free': [('Grondia — B2B SaaS, Switzerland',
           'Nov 2026',
           'Freelance Sales Rep: French-language remote sales call co-led with the founder (feedback: '
           '"literally perfect"), plus a full day on the trade-show stand at SETT 2026, Montpellier.')],
 'intern': [('HAROPA Port — Le Havre, SI Department',
             'June 2024',
             "Observation internship within the information systems department of one of Europe's largest "
             'port authorities.')],
 'exp': [('Creator &amp; Systems Engineer',
          '2026 — Present',
          'Expo — personal AI infrastructure',
          'Self-hosted personal AI across two machines: always-on server with local LLM triage, intent '
          'routing, RAG memory and chat UI; GPU rig for heavy inference. Docker Compose, Tailscale, '
          'llama.cpp, Qdrant, SQLite.'),
         ('Creator &amp; Lead Developer',
          'Apr 2026 — Present',
          'Lodge',
          'Rust installer runtime with a natural-language terminal UI, bundled offline model and per-OS '
          'placement rulesets. 5 crates, 172 tests, Apache-2.0.'),
         ('Founder &amp; Lead Developer',
          '2026 — Present',
          'PsyPunker',
          'Sole architect of a USB-bound cryptographic Kernel execution platform (Tauri, React, Rust, '
          'TypeScript monorepo). Shipped Phase 1 as v0.1.0 in April 2026 with 263 tests and CI, release and '
          'security workflows.'),
         ('Co-Founder &amp; President · Project Director',
          '2025 — Present',
          'KronStudios-Games — Above The Line',
          'Lead a ~9-person volunteer revenue-share studio building a narrative survival game in Unreal '
          'Engine 5.6. Project direction, narrative design, PR workflow, STAR recruiting, merit-weighted '
          'revenue share, Quartz GDD wiki.'),
         ('Logistics Manager · Lore Writer · Gameplay Overseer · Translator',
          'Apr 2025 — Nov 2025',
          'Null Concept — Monochromality (Steam, upcoming)',
          'Cross-functional contributor on an upcoming Backrooms horror game: lore frameworks, logistics, '
          'gameplay oversight, partial voice acting, translation; built the official website.'),
         ('CEO, Owner &amp; Lead Developer',
          '2025 — 2026',
          'EveryMotion',
          'Founded an AI motion-tracking startup concept for AR/VR; set the technical vision and built the '
          'public site before the venture shut down.'),
         ('Co-Founder &amp; Lead Manager',
          'Aug 2023 — Feb 2024',
          'REIU-V — SCP Roleplay Discord Server',
          'Grew an SCP roleplay community to ~150 members (900+ after departure); infrastructure, moderation '
          'and narrative frameworks.'),
         ('Writer',
          '~2023 — Present',
          'Independent · Backrooms Wikidot · REIU-V · Personal',
          'Published Backrooms Wikidot articles (Level 360, +17) and contest entries; in-universe SCP '
          'technical documents; screenplay and novel in progress: <em>A Sound Sinner</em>, <em>Information '
          'Paradox</em>.',
          True),
         ('Founder &amp; Lead',
          '~2022 — ~2023',
          'T||RUTHLESS &amp; Subject To F.U.N — First KronStudios initiatives',
          'Directed two UE5 game projects as Project Manager and Head Developer across ~15 people; full GDDs '
          'and storyline addenda. Neither reached a playable build — the leadership lesson behind everything '
          'after.')],
 'skills': [('Languages',
             'TypeScript, JavaScript, Python, Rust, HTML/CSS, UE Blueprint, SQL · familiar: C++, C#'),
            ('Engines / Runtimes', 'Unreal Engine 5, Tauri, React, Node.js, llama.cpp, ratatui'),
            ('Tooling', 'Git + Git LFS, GitHub Actions, pnpm + Turborepo, Vitest, ESLint, Docker Compose'),
            ('Systems / Hardware',
             'Linux, Tailscale, self-hosting (Coolify, Supabase, n8n), Qdrant, SQLite, Arduino / ESP32, 3D '
             'printing'),
            ('Other',
             'Consultative sales (FR/EN), Obsidian + Quartz, Lore Forge, Blender (basic), Google Docs '
             '(scriptwriting)')],
 'langs': [('Ukrainian', 'native'),
           ('French', 'fluent'),
           ('English', 'fluent'),
           ('Russian', 'passive'),
           ('Spanish', 'moderate')],
 'preview': 'CV Preview',
 'back': '← Portfolio',
 'save': '↓ Save as PDF'}
