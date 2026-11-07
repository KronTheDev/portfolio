# Portfolio Fill-Out Sheet — v2 (backchecked 2026-11-07)

v1 was the spring 2026 sheet. Every value below was checked against your public repos, the Steam and Wikidot pages, and your reviewed identity facts. Tags: **✓** verified, **✎** corrected, **＋** new, **?** your call.
Street addresses from v1 are removed (the repo is public).

## Backcheck log

| # | Item | v1 said | Found | Source |
|---|---|---|---|---|
| 1 | PsyPunker progress | "M3 complete; Builder UI in progress" | ✎ Phase 1 (M1–M6) complete, **v0.1.0 tagged** 27 Apr 2026; 263 tests, 4 CI workflows (CI, release, Runner Lite release, security). Last commit 30 Apr 2026. | psypunker repo: docs/phase2-brief.md |
| 2 | PsyPunker vs MitoData | — | ✓ MitoData is PsyPunker's Phase 4 enterprise tier, not a rename. Keep PsyPunker as the name. | psypunker README |
| 3 | Monochromality status | "available on Steam", "commercially released" | ✎ **Not released.** Steam: "Coming soon to Early Access, TBA", wishlist only, publisher Null Concept Games. | Steam app 3744840 |
| 4 | Monochromality levels/entities | 15 levels; Howler, Hounds, Duller | ✓ Matches the official site, which **you built** (KronTheDev/monochromality). Steam page says "10+ levels". | monochromality repo, Steam |
| 5 | EveryMotion | "Active — WIP (resumed)", SDK back in development | ✎ Shut down. Site repo last updated Nov 2025; `everymotion` SDK repo is empty. | d008, GitHub |
| 6 | Above The Line | "Active — WIP", C++ / Blueprint | ✎ Paused since summer 2026. UE **5.6**, Blueprint-only since June 2026. Repo last push Jul 2026. | f0022, f0066, f0271, .uproject |
| 7 | ATL webdisplay | "Private — do not show" | ✓ Public repo is only a Quartz wrapper for the Obsidian vault; no action. | GitHub |
| 8 | KronStudios role | "Co-founded and co-lead" | ✎ Co-founder and **President**; ~9 members, VP + HQ Council. | f0287 |
| 9 | Level 360 | "most prominent published work" | ✓ "Halls of Past Screams", by DR Andrew Pie, rating **+17**, last edited 26 Jun 2026. | backrooms-wiki.wikidot.com/level-360 |
| 10 | REIU-V | 150 → 900+, Aug 2023–Feb 2024 | ✓ No contradiction; 2025 return confirmed. | f0075, f0076, n2 |
| 11 | T‖RUTHLESS | ~2022–2023, ~15 people, GDD rev 0.15 | ✓ Matches GDD + private repo `T-RUTHLESS-Proj-Rep` (last push Mar 2024). | d009, GitHub |
| 12 | Education | Terminale only | ✎ Now at Université de Montpellier (L1 Informatique, Sept 2026). Lycée split corrected. | f0192, d006 |
| 13 | Languages | Russian "not preferred" | ? Your reviewed fact says native in Russian too (f0197). Live site shows "passive". | f0197 |
| 14 | Skills | full list | ? You said the list is inflated (d004). Below, each skill shows the repo that proves it; unproven ones are marked. | repos |
| 15 | Lodge | not listed | ＋ Public Rust repo, ~19.6k lines, 172 tests, 5 crates. Licence settled on Apache-2.0 (README fixed). | KronTheDev/lodge |
| 16 | Expo | not listed | ＋ Private repo `doorman-protocol`, 94 commits, ~7.9k lines Python, 3 services. | doorman-protocol |
| 17 | Websites | not listed | ＋ You built the EveryMotion, Monochromality and KronStudios sites (HTML/CSS/JS). | repos |

---

## Identity

| Field | Value |
|---|---|
| Legal name | Andriyan Pyrig ✓ *(CV header only)* |
| Pseudonym / brand | Andrew Pie ✓ |
| GitHub handle | KronTheDev ✓ |
| Other handles | Kron · kronbrosgames (Discord) · DR Andrew Pie (Backrooms Wiki) ＋ |

Introductory Punchline: "I bid you, Welcome" ✓

---

## Hero

**Tagline**: "The future won't come for us. Never. Yet we must strive towards it. Always." ✓ (below the Hero)

**Role cycle**:

- Developer
- Systems Engineer
- Game Designer
- Lore Architect
- Scriptwriter
- ? Founder *(you use it for yourself, f0179)*

---

## About

**Location:**

> France / Ukraine ✓ *(no city on purpose)*

**Open to:**

> Freelance, Internship, Collaboration ✓

**Domain focus:**

> Web Development, Game Dev (Shared Projects), AI, Backend Development ✓
> ? add "Systems / Self-hosting" (Expo, Lodge)

**Bio — paragraph 1**: unchanged ✓ ("fluent across four languages, passable in a fifth" holds: UK, FR, EN, RU + Spanish.)

**Bio — paragraph 2**: unchanged ✓

**＋ Status line (optional, under the bio):**

> Computer Science student at Université de Montpellier (2026–). Building local-first AI and developer tools on the side.

---

## Skills

Evidence after each item. **unproven** = nothing public shows it yet; keep, move to "familiar", or drop.

### Spoken Languages
- Ukrainian — native ✓
- French — fluent ✓
- English — fluent ✓ *(Ev@Lang above B1 in 2023; near-native now)*
- Russian — ? native / passive / drop
- Spanish — moderate ✓

### Programming Languages
- TypeScript — PsyPunker ✓
- JavaScript — EveryMotion, Monochromality, KronStudios sites ✓
- Python — Expo (doorman, fetcher, memory services) ✓
- **Rust** — Lodge, PsyPunker framing layer ＋
- HTML / CSS — 4 sites ✓
- UE Blueprint — Above The Line ✓
- C++ — unproven *(ATL moved off C++)*
- C# — unproven
- SQL — Expo (SQLite) ✓ light

### Frameworks / Runtimes
- Unreal Engine 5.6 — Above The Line ✓
- Tauri + React — PsyPunker ✓
- Node.js — PsyPunker tooling ✓
- llama.cpp — Lodge (llama-cpp-2), Expo ✓
- **ratatui** — Lodge terminal UI ＋
- HuggingFace Transformers — unproven publicly

### Tools / Infrastructure
- Git + Git LFS — ATL ✓
- GitHub Actions — PsyPunker (4 workflows) ✓
- pnpm + Turborepo — PsyPunker ✓
- Vitest — PsyPunker (263 tests) ✓
- ESLint + commitlint — PsyPunker ✓
- **Docker Compose** — Expo ＋
- **Linux (Ubuntu, Mint) · Tailscale · self-hosting (Coolify, Supabase, n8n)** — Expo, KronStudios ＋
- CUDA — unproven publicly *(rig not yet running GPU inference)*

### Other
- Obsidian (in depth) + Quartz — ATL GDD wiki ✓
- Lore Forge ✓
- Blender (basic) ✓
- Google Docs (scriptwriting) ✓
- **Hardware: Arduino / ESP32, soldering, 3D printing** ＋ *(Expo CEC bridge, f0176)*

---

## Projects

### Project 1 — PsyPunker ✎ *(moved to first: strongest shipped code)*
| Field | Value |
|---|---|
| Name | PsyPunker |
| Status | v0.1.0 — Phase 2 planned |
| GitHub URL | *(private — presented without a link)* |
| Live URL | *(none — desktop application)* |

**Description**:

> A physical-key execution platform: insert a drive, a world opens. A Tauri desktop app split into a Builder (React + Monaco visual editor, compiler and signing pipeline) and a Runner that validates the drive's key and renders the Kernel as a fullscreen overlay isolated from the host, leaving nothing behind on removal. Phase 1 shipped as v0.1.0: Ed25519 signing, Argon2id drive binding, BadUSB pre-check, sensor broker, runtime capability monitor, drive-only audit log, and an adversarial test suite. Its enterprise tier, MitoData, is planned for Phase 4.

**Tech stack**: TypeScript · Rust · Tauri · React · Monaco · pnpm + Turborepo · Ed25519 + Argon2id · Vitest · GitHub Actions

---

### Project 2 — Lodge ＋
| Field | Value |
|---|---|
| Name | Lodge |
| Status | Active — WIP *(last commit May 2026)* |
| GitHub URL | https://github.com/KronTheDev/lodge |
| Live URL | *(none — terminal app)* |

**Description**:

> A language-agnostic installer runtime with a conversational terminal interface. Lodge reads a developer-shipped manifest that describes what a package is, works out where each file belongs on Windows, macOS or Linux, and runs the install live in a cabin-themed terminal UI. A bundled offline model (llama.cpp + SmolLM2) understands plain-English commands like "do I have git?" or "is port 8080 free?", with optional online providers. Ships with Clean Cabin, a non-destructive file-cleanup extension, and a validated extension registry.

**Tech stack**: Rust (5-crate workspace) · ratatui · llama.cpp · genai · 172 tests

---

### Project 3 — Expo ＋ ?
| Field | Value |
|---|---|
| Name | Expo |
| Status | Active — WIP |
| GitHub URL | *(private)* |
| Live URL | *(none)* |

**Description** *(architecture only, nothing personal)*:

> A local-first, voice-first personal AI that runs entirely on my own hardware. An always-on low-power server (the "doorman") handles fast triage with a small local LLM, semantic intent routing, live news and API lookups, and long-term RAG memory with nightly consolidation; a GPU rig takes the heavy inference. Everything is self-hosted with Docker Compose over Tailscale, with a regression suite run after every rebuild.

**Tech stack**: Python · llama.cpp · Qdrant · SQLite · Docker Compose · Tailscale · Whisper

---

### Project 4 — Above The Line ✎
| Field | Value |
|---|---|
| Name | Above The Line |
| Status | WIP — Paused |
| GitHub URL | https://github.com/KronStudios-Games/abovetheline ✓ |
| Live URL | (Private webdisplay — do not show) |

**Description**:

> A first-person vertical narrative survival game set after the Yellowstone supereruption of Labor Day 2039 reshapes Vancouver's atmosphere. Society splits by elevation, above or below a toxic gas cloud; the player leaves the fragile safety of a high-rise and travels upward. Built in Unreal Engine 5.6 with a (semi-)diegetic UI. Developed under KronStudios-Games; Andrew Pie is Project Director and Worldbuilding/Narrative Lead. The Quartz GDD wiki documents factions, locations, the prologue timeline, gameplay systems and infrastructure conventions.

**Tech stack**: Unreal Engine 5.6 · UE Blueprint · Git LFS · Supabase · Quartz + Obsidian

---

### Project 5 — Monochromality ✎
| Field | Value |
|---|---|
| Name | Monochromality |
| Status | Upcoming — Early Access, TBA *(contributor Apr–Nov 2025)* |
| GitHub URL | *(private — Null Concept team repo)* · site: https://github.com/KronTheDev/monochromality |
| Live URL | https://kronthedev.github.io/monochromality/ · https://store.steampowered.com/app/3744840/Monochromality/ |

**Description**:

> A Backrooms-inspired first-person horror game by Null Concept, coming to Steam Early Access. 15 mapped levels planned at release, each with its own hazards and ambiance, and three predators: the Howler, the Hounds and the Duller. I shaped its lore from the Backrooms Wikidot canon, handled logistics, gameplay oversight and translation, and built its official website.

**Tech stack**: Unreal Engine · UE Blueprint · website: HTML / CSS / JS

---

### Project 6 — EveryMotion ✎ *(move below the fold or to Experience only)*
| Field | Value |
|---|---|
| Name | EveryMotion |
| Status | Closed |
| GitHub URL | https://github.com/KronTheDev/everymotion.github.io *(site only)* |
| Live URL | https://kronthedev.github.io/everymotion.github.io/ |

**Description**:

> An AI-powered, controller-free motion tracking concept for AR/VR: computer vision plus RAG-enhanced prediction, no sensors, no controllers. I founded it, set the technical vision and built its public site and manifesto before the venture shut down.

**Tech stack**: HTML / CSS / JS *(site)* · Computer Vision, RAG *(planned core)*

---

### Project 7 — Primecit Mod — NO ✓ *(kept out)*

---

## Experience

Most recent first. Independent initiatives — no formal employment.

### Entry 1 — Expo ＋ ?
| Field | Value |
|---|---|
| Role / Title | Creator & Systems Engineer |
| Organisation or Project | Expo (personal AI infrastructure) |
| From | Oct 2026 *(build start; concept earlier)* |
| To | Present |

> Designing and building a self-hosted personal AI across two machines: an always-on server running local LLM triage, intent routing, RAG memory and a chat interface, and a GPU rig for heavy inference. Docker Compose, Tailscale, llama.cpp, Qdrant; ZFS storage; a regression suite and nightly self-evaluation.

### Entry 2 — Lodge ＋
| Field | Value |
|---|---|
| Role / Title | Creator & Lead Developer |
| Organisation or Project | Lodge |
| From | Apr 2026 |
| To | Present |

> Built a Rust installer runtime with a natural-language terminal interface, an offline bundled model, OS placement rulesets for Windows, macOS and Linux, and an extension registry with automated validation. 5 crates, 172 tests.

### Entry 3 — PsyPunker ✎
| Field | Value |
|---|---|
| Role / Title | Founder & Lead Developer ✓ |
| Organisation or Project | PsyPunker |
| From | 2026 ✓ |
| To | Present |

> Sole architect and developer of a USB-bound cryptographic Kernel execution platform. Designed the full system architecture — signing pipeline, sandbox model, drive-identity binding, 20-vector threat model — and built a TypeScript + Rust monorepo using Tauri, React, pnpm and Turborepo. Shipped Phase 1 as v0.1.0 (April 2026) with 263 tests and CI, release and security workflows.

### Entry 4 — KronStudios-Games / Above The Line ✎
| Field | Value |
|---|---|
| Role / Title | Co-Founder & President · Project Director & Narrative Lead |
| Organisation or Project | KronStudios-Games |
| From | 2025 ✓ |
| To | Present |

> Co-founded and lead, as President, a volunteer revenue-share indie studio of about nine people, producing Above The Line in Unreal Engine 5.6. Responsible for project direction, narrative design, lore architecture and team coordination. Set up phased milestones, a protected-branch PR workflow, STAR-based recruiting, a merit-weighted revenue-share agreement and a Quartz GDD wiki; built the studio website. Revived the team after a stall in spring 2026.

### Entry 5 — Monochromality / Null Concept ✎
| Field | Value |
|---|---|
| Role / Title | Logistics & Suggestions Manager · Lore Writer · Gameplay Overseer · Translator ✓ |
| Organisation or Project | Null Concept |
| From | April 2025 ✓ |
| To | November 2025 *(stepped back, not fully departed)* ✓ |

> Joined early and shaped the game's direction with Backrooms lore frameworks drawn from the Wikidot canon. Cross-functional role across logistics, coordination, lore writing, gameplay oversight, partial voice acting and translation; built the official website. Stepped back over sustained deadline slips and diverging creative vision. *(✎ "commercially released" removed: the game is not out yet.)*

### Entry 6 — SCP Roleplay Server (REIU-V) ✓
| Field | Value |
|---|---|
| Role / Title | Co-Founder & Lead Manager |
| Organisation or Project | REIU-V — SCP RP Discord |
| From | August 2023 |
| To | February 2024 |

> Unchanged from v1.

### Entry 7 — Writing *(parallel thread)* ✎
| Field | Value |
|---|---|
| Role / Title | Writer |
| Organisation or Project | Independent / Backrooms Wikidot / REIU-V / Personal |
| From | ~2023 |
| To | Present |

> v1 text kept, with three checks applied:
> - Level 360 "Halls of Past Screams": add "(+17 rating)" ✓.
> - A Sound Sinner: ✎ "stands as the most complete example" → "Draft #1 (Nov 2025) with a full pitch". It is unfinished (d014). Also, the mercy killing is The Gal mid-story, not the ending; the ending is the gunslinger dropping his gun into the Pacific (n5).
> - Information Paradox: ✓ "a scientist at the California Aerospace Complex falling through an impossible locker into an endless tunnel" matches the manuscript; add "in progress".

### Entry 8 — Subject To F.U.N ✓ — unchanged.

### Entry 9 — T‖RUTHLESS ✓ — unchanged.

---

## Vision Quote ✓

> "Everything I make is an argument that these things belong together."

---

## Contact ✓

| Field | Value |
|---|---|
| Email | kronthedev@gmail.com |
| LinkedIn URL | *(none)* |
| Other link | Discord: @kronbrosgames |
| ＋ Backrooms Wiki | DR Andrew Pie |

---

## CV-Only Fields

*CV header: **Andriyan Pyrig** (Andrew Pie / KronTheDev)*

**Education:** ✎
> Université de Montpellier · Licence Informatique (Computer Science), L1 · Sept 2026 – present
> Lycée Rosa Luxemburg, Canet-en-Roussillon · Terminale, Baccalauréat · Jan – June 2026
> Lycée Jules Siegfried, Le Havre · Seconde, Première, Terminale (1st semester) · 2023 – Dec 2025
> Collège Belle Etoile, Montivilliers · Diplôme national du Brevet, Mention Très Bien · 2023

**Languages spoken:** UK native · FR fluent · EN fluent · RU ? · ES moderate

**Certifications:** ＋ Ev@Lang English, above B1 · March 2023

**Internships:** ✓
> HAROPA Port, Le Havre · IT department (SI) observation internship · June 2024
> La Tôlerie Plastique · 3ème work placement · May 2023 *(optional)*

**Additional CV note** ＋ *(optional)*:
> Self-hosts my own infrastructure (Linux, Docker, Tailscale) and builds hardware prototypes (Arduino, ESP32, 3D printing).
