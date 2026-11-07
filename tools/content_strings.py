# -*- coding: utf-8 -*-
"""Localised site strings generated from content/portfolio.yaml.

Edit content/portfolio.yaml first (EN source of truth), then mirror the change here
for FR and UK, then run:  python3 tools/build_site.py
"""

L360 = '<a href="https://backrooms-wiki.wikidot.com/level-360" target="_blank" rel="noopener" class="tl-link">Level 360 ↗</a>'

S = {}

# ───────────────────────────── ENGLISH ─────────────────────────────
S['en'] = dict(
    tag_open='Freelance · Internship · Collaboration · Sales',
    tag_domain='Web · Game Dev · AI · Backend · B2B Sales',

    skills_heading='Skills', skills_sub='What I work with — grouped by category.',
    sg_spoken='Spoken Languages', sg_prog='Programming Languages',
    sg_frameworks='Frameworks / Runtimes', sg_tools='Tools / Infrastructure',
    sg_systems='Systems / Hardware', sg_other='Other',
    lang_uk='Ukrainian — native', lang_fr='French — fluent', lang_en='English — fluent',
    lang_ru='Russian — passive', lang_es='Spanish — moderate',
    sk_cpp='C++ (familiar)', sk_cs='C# (familiar)',
    sk_selfhost='Self-hosting', sk_print='3D printing',
    sk_blender='Blender (basic)', sk_gdocs='Scriptwriting',
    sk_sales='Consultative sales',

    projects_heading='Projects',
    projects_sub='Selected work — shipped builds, active systems, and ongoing initiatives.',
    badge_v01='v0.1.0 — Shipped', badge_active='Active — WIP', badge_paused='WIP — Paused',
    badge_upcoming='Upcoming', badge_closed='Closed',
    proj_ps_desc='A physical-key execution platform: insert a drive, a world opens. A Tauri desktop app split into a Builder (React + Monaco visual editor, compile and signing pipeline) and a Runner that validates the drive\'s key and renders the Kernel as a fullscreen overlay isolated from the host — drive out, session gone, zero trace. Phase 1 shipped as v0.1.0 with 263 tests and CI, release and security workflows. Its enterprise tier, MitoData, comes later.',
    proj_lodge_desc='A language-agnostic installer runtime with a conversational terminal interface. Lodge reads a manifest that describes what a package is, works out where each file belongs on Windows, macOS or Linux, and runs the install live in a cabin-themed terminal UI. A bundled offline model understands plain-English commands like "do I have git?" — 5 crates, 172 tests.',
    proj_expo_desc='A local-first, voice-first personal AI running entirely on my own hardware. An always-on low-power server handles fast triage with a small local LLM, semantic intent routing, live lookups and long-term RAG memory with nightly consolidation; a GPU rig takes the heavy inference. Self-hosted end to end, with a regression suite run after every rebuild.',
    proj_atl_desc='A first-person vertical narrative survival game set after the Yellowstone supereruption of Labor Day 2039 reshapes Vancouver\'s atmosphere. Society splits by elevation, above or below a toxic gas cloud; the player leaves the fragile safety of a high-rise and travels upward. Unreal Engine 5.6, (semi-)diegetic UI. Project Director & Narrative Lead under KronStudios-Games.',
    proj_mono_desc='A Backrooms-inspired first-person horror game by Null Concept, coming to Steam Early Access. 15 mapped levels planned at release, each with its own hazards and ambiance, and three predators — the Howler, the Hounds and the Duller. I shaped its lore, handled logistics and translation, and built its official website.',
    proj_em_desc='An AI-powered, controller-free motion tracking concept for AR/VR — computer vision plus RAG-enhanced prediction, no sensors, no controllers. I founded it, set the technical vision and built its public site before the venture shut down.',

    experience_heading='Experience',
    experience_sub='Independent initiatives and freelance work — no salaried employment, no pretence otherwise.',

    exp_gr_role='Freelance Sales Representative', exp_gr_date='Nov 2026',
    exp_gr_org='Grondia — Swiss campsite-management SaaS',
    exp_gr_desc='Prepared and co-led a French-language remote sales call with the founder on 50 minutes\' notice, tailoring the pitch to a ~100-pitch Swiss campsite — seasonal contracts, point of sale, CHF and TWINT payments, Swiss data hosting — and handling questions on pricing, migration and data location. The founder\'s verdict: <em>"literally perfect."</em> Then a full day representing Grondia on its stand at SETT 2026 in Montpellier, qualifying campsite operators and booking demos.',

    exp_expo_role='Creator & Systems Engineer', exp_expo_date='2026 — Present',
    exp_expo_org='Expo — personal AI infrastructure',
    exp_expo_desc='Designing and building a self-hosted personal AI across two machines: an always-on server running local LLM triage, intent routing, RAG memory and a chat interface, and a GPU rig for heavy inference. Docker Compose, Tailscale, llama.cpp, Qdrant and SQLite, with a regression suite and nightly self-evaluation.',

    exp_lodge_role='Creator & Lead Developer', exp_lodge_date='Apr 2026 — Present', exp_lodge_org='Lodge',
    exp_lodge_desc='Built a Rust installer runtime with a natural-language terminal interface, a bundled offline model, OS placement rulesets for Windows, macOS and Linux, and an extension registry with automated validation. 5 crates, 172 tests, Apache-2.0.',

    exp_ps_role='Founder & Lead Developer', exp_ps_date='2026 — Present', exp_ps_org='PsyPunker',
    exp_ps_desc='Sole architect and developer of a USB-bound cryptographic Kernel execution platform. Designed the full system architecture — signing pipeline, sandbox model, drive-identity binding, a 20-vector threat model — and built a TypeScript + Rust monorepo with Tauri, React, pnpm and Turborepo. Shipped Phase 1 as v0.1.0 (April 2026) with 263 tests and CI, release and security workflows.',

    exp_ks_role='Co-Founder & President · Project Director & Narrative Lead', exp_ks_date='2025 — Present',
    exp_ks_org='KronStudios-Games — Above The Line',
    exp_ks_desc='Co-founded and lead, as President, a volunteer revenue-share indie studio of about nine people producing Above The Line in Unreal Engine 5.6. Responsible for project direction, narrative design, lore architecture and team coordination. Set up phased milestones, a protected-branch PR workflow, STAR-based recruiting, a merit-weighted revenue-share agreement and a Quartz GDD wiki; built the studio website.',

    exp_nc_role='Logistics & Suggestions Manager · Lore Writer · Gameplay Overseer · Translator',
    exp_nc_date='Apr 2025 — Nov 2025', exp_nc_org='Null Concept — Monochromality',
    exp_nc_desc='Joined early and shaped the game\'s direction with Backrooms lore frameworks drawn from the Wikidot canon. Cross-functional role across logistics, coordination, lore writing, gameplay oversight, partial voice acting and translation; built the official website. Stepped back over sustained deadline slips and diverging creative vision.',

    exp_em_role='CEO, Owner & Lead Developer', exp_em_date='2025 — 2026', exp_em_org='EveryMotion',
    exp_em_desc='Founded and led an AI-powered motion tracking startup concept targeting AR/VR. Defined the technical vision (computer vision, RAG-enhanced prediction), built the public-facing web presence, and managed the early team and product roadmap before the venture shut down.',

    exp_reiu_role='Co-Founder & Lead Manager', exp_reiu_date='Aug 2023 — Feb 2024', exp_reiu_org='REIU-V — SCP Roleplay Server',
    exp_reiu_desc='Founded and maintained an SCP-themed roleplay Discord community that grew to ~150 members during tenure and accelerated to 900+ after departure. Managed server infrastructure, community moderation, and narrative frameworks.',

    exp_wr_role='Writer', exp_wr_date='~2023 — Present', exp_wr_org='Independent · Backrooms Wikidot · REIU-V · Personal',
    exp_wr_desc='Writing has run as a parallel thread across almost every initiative. The first serious application was the REIU-V community: original in-universe documents in clinical SCP format — technical protocols, anomalous research logs, consciousness-overwriting procedures — with a new batch written for its commemoration event in August 2025.<br><br>Active on the Backrooms Wikidot Feb–Aug 2025: published articles, collaborative pieces, and contest submissions including the <em>Despair Writings</em> contest. Most prominent published work: ' + L360 + ' <em>"Halls of Past Screams"</em> (+17).<br><br>From late 2025: novel and screenplay writing, both in progress. <em>A Sound Sinner</em> — a Tarantino-structured post-apocalyptic screenplay. <em>Information Paradox</em> — literary science fiction, quieter register. Running concurrently: the Above The Line prologue and story summary, the narrative foundation before a single line of code.',

    exp_fun_role='Founder & Project Manager', exp_fun_date='~2023 — Never shipped',
    exp_fun_org='Subject To F.U.N (Fourth-Wall Understanding Network)',
    exp_fun_desc='A KronStudios concept — a fourth-wall-breaking action puzzle thriller in the vein of Portal and The Stanley Parable. The title itself was a sarcastic joke built into the premise. Never reached a single line of production code. Revision 0.01 is the entire paper trail it left behind.',

    exp_tr_role='Founder & Lead', exp_tr_date='~2022 — ~2023', exp_tr_org='T||RUTHLESS — First KronStudios Initiative',
    exp_tr_desc='Founded and directed the first KronStudios initiative: a narrative-driven UE5 shooter with a semi-free-choice storyline. The title — a deliberate dual-read: <em>Ruthless</em> on first glance, <em>Truthless</em> on closer inspection — embedded into the story of a soldier named Rad Bronx, uncovering a century-old government conspiracy through I.R.I.S. Project Manager and Head UE5 Developer across ~15 people. Never reached a playable build. The foundational leadership lesson that shaped everything after.',

    vision_quote='"Everything I make is an argument that these things belong together."',
    contact_heading='Get in Touch', contact_sub='Open to freelance, internships, collaborations and sales work.',
)

# ───────────────────────────── FRANÇAIS ─────────────────────────────
S['fr'] = dict(
    tag_open='Freelance · Stage · Collaboration · Vente',
    tag_domain='Web · Jeu Vidéo · IA · Backend · Vente B2B',

    skills_heading='Compétences', skills_sub='Mes outils et technologies — groupés par catégorie.',
    sg_spoken='Langues parlées', sg_prog='Langages de programmation',
    sg_frameworks='Frameworks / Runtimes', sg_tools='Outils / Infrastructure',
    sg_systems='Systèmes / Matériel', sg_other='Autre',
    lang_uk='Ukrainien — natif', lang_fr='Français — courant', lang_en='Anglais — courant',
    lang_ru='Russe — passif', lang_es='Espagnol — intermédiaire',
    sk_cpp='C++ (notions)', sk_cs='C# (notions)',
    sk_selfhost='Auto-hébergement', sk_print='Impression 3D',
    sk_blender='Blender (notions)', sk_gdocs='Scénarisation',
    sk_sales='Vente conseil',

    projects_heading='Projets',
    projects_sub='Travaux sélectionnés — versions livrées, systèmes actifs et initiatives en cours.',
    badge_v01='v0.1.0 — Livré', badge_active='Actif — WIP', badge_paused='WIP — En pause',
    badge_upcoming='À venir', badge_closed='Fermé',
    proj_ps_desc='Une plateforme d\'exécution à clé physique : on insère un support, un monde s\'ouvre. Une application desktop Tauri en deux faces — un Builder (éditeur visuel React + Monaco, pipeline de compilation et de signature) et un Runner qui valide la clé du support et affiche le Kernel en overlay plein écran, isolé de l\'hôte. Support retiré, session terminée — zéro trace. La phase 1 est sortie en v0.1.0 avec 263 tests et des workflows CI, release et sécurité. Son offre entreprise, MitoData, viendra ensuite.',
    proj_lodge_desc='Un runtime d\'installation agnostique au langage, avec une interface terminal conversationnelle. Lodge lit un manifeste qui décrit ce qu\'est un paquet, détermine où chaque fichier doit aller sous Windows, macOS ou Linux, et exécute l\'installation en direct dans une interface terminal au style chalet. Un modèle hors-ligne intégré comprend des commandes en langage naturel comme « est-ce que j\'ai git ? » — 5 crates, 172 tests.',
    proj_expo_desc='Une IA personnelle locale et pilotée à la voix, qui tourne entièrement sur mon propre matériel. Un serveur basse consommation toujours allumé gère le tri rapide avec un petit LLM local, le routage sémantique des intentions, les recherches en direct et une mémoire RAG à long terme consolidée chaque nuit ; une machine GPU prend en charge l\'inférence lourde. Entièrement auto-hébergé, avec une suite de tests de régression après chaque reconstruction.',
    proj_atl_desc='Un jeu de survie narratif vertical à la première personne : après la super-éruption du Yellowstone, le jour du Labor Day 2039, l\'atmosphère de Vancouver est transformée. La société se divise selon l\'altitude, au-dessus ou en dessous d\'un nuage de gaz toxique ; le joueur quitte la sécurité précaire d\'un gratte-ciel et remonte. Unreal Engine 5.6, interface (semi-)diégétique. Directeur de projet et responsable narratif sous KronStudios-Games.',
    proj_mono_desc='Un jeu d\'horreur à la première personne inspiré des Backrooms, par Null Concept, bientôt en accès anticipé sur Steam. 15 niveaux prévus à la sortie, chacun avec ses dangers et son ambiance, et trois prédateurs — le Hurleur, les Traqueurs et l\'Atone. J\'ai façonné son lore, géré la logistique et la traduction, et créé son site officiel.',
    proj_em_desc='Un concept de suivi de mouvement sans manettes, propulsé par l\'IA, pour la réalité augmentée et virtuelle — vision par ordinateur et prédiction RAG, sans capteurs ni contrôleurs. Je l\'ai fondé, j\'en ai défini la vision technique et créé le site public avant l\'arrêt du projet.',

    experience_heading='Expérience',
    experience_sub='Initiatives indépendantes et missions freelance — aucun emploi salarié, sans s\'en cacher.',

    exp_gr_role='Commercial indépendant', exp_gr_date='Nov 2026',
    exp_gr_org='Grondia — SaaS suisse de gestion de campings',
    exp_gr_desc='Préparé et co-animé avec le fondateur un appel de vente à distance en français, avec 50 minutes de préavis, en adaptant le pitch à un camping suisse d\'environ 100 emplacements — contrats saisonniers, caisse, paiements en CHF et TWINT, hébergement des données en Suisse — et répondu aux questions sur les tarifs, la migration et la localisation des données. Le verdict du fondateur : <em>« littéralement parfait ».</em> Puis une journée complète sur le stand Grondia au SETT 2026 à Montpellier, à qualifier des exploitants de campings et à planifier des démos.',

    exp_expo_role='Créateur & Ingénieur Systèmes', exp_expo_date='2026 — Présent',
    exp_expo_org='Expo — infrastructure d\'IA personnelle',
    exp_expo_desc='Conception et construction d\'une IA personnelle auto-hébergée sur deux machines : un serveur toujours allumé pour le tri par LLM local, le routage des intentions, la mémoire RAG et une interface de chat, et une machine GPU pour l\'inférence lourde. Docker Compose, Tailscale, llama.cpp, Qdrant et SQLite, avec une suite de régression et une auto-évaluation nocturne.',

    exp_lodge_role='Créateur & Développeur Principal', exp_lodge_date='Avr 2026 — Présent', exp_lodge_org='Lodge',
    exp_lodge_desc='Développement d\'un runtime d\'installation en Rust avec une interface terminal en langage naturel, un modèle hors-ligne intégré, des règles de placement pour Windows, macOS et Linux, et un registre d\'extensions à validation automatique. 5 crates, 172 tests, Apache-2.0.',

    exp_ps_role='Fondateur & Développeur Principal', exp_ps_date='2026 — Présent', exp_ps_org='PsyPunker',
    exp_ps_desc='Seul architecte et développeur d\'une plateforme d\'exécution de Kernels cryptographiques liés à une clé USB. Conception de l\'architecture complète — pipeline de signature, modèle sandbox, liaison à l\'identité du support, modèle de menaces à 20 vecteurs — et monorepo TypeScript + Rust avec Tauri, React, pnpm et Turborepo. Phase 1 livrée en v0.1.0 (avril 2026) avec 263 tests et des workflows CI, release et sécurité.',

    exp_ks_role='Co-fondateur & Président · Directeur de Projet & Responsable Narratif', exp_ks_date='2025 — Présent',
    exp_ks_org='KronStudios-Games — Above The Line',
    exp_ks_desc='Co-fondateur et président d\'un studio indépendant bénévole à partage de revenus, d\'environ neuf personnes, qui développe Above The Line sous Unreal Engine 5.6. Responsable de la direction du projet, du design narratif, de l\'architecture du lore et de la coordination. Mise en place de jalons par phases, d\'un workflow de PR sur branches protégées, d\'un recrutement par entretiens STAR, d\'un accord de partage des revenus au mérite et d\'un wiki GDD sous Quartz ; création du site du studio.',

    exp_nc_role='Responsable Logistique & Suggestions · Auteur de Lore · Superviseur Gameplay · Traducteur',
    exp_nc_date='Avr 2025 — Nov 2025', exp_nc_org='Null Concept — Monochromality',
    exp_nc_desc='Arrivé tôt, j\'ai orienté le jeu avec des cadres narratifs tirés du canon Backrooms Wikidot. Rôle transversal : logistique, coordination, écriture du lore, supervision du gameplay, doublage partiel et traduction ; création du site officiel. Je me suis mis en retrait face aux retards répétés et à une vision créative divergente.',

    exp_em_role='PDG, Fondateur & Développeur Principal', exp_em_date='2025 — 2026', exp_em_org='EveryMotion',
    exp_em_desc='Fondateur et directeur d\'un concept de startup de suivi de mouvement par IA pour la réalité augmentée et virtuelle. Définition de la vision technique (vision par ordinateur, prédiction RAG), création de la présence web et gestion de l\'équipe et de la feuille de route, avant l\'arrêt du projet.',

    exp_reiu_role='Co-Fondateur & Responsable Principal', exp_reiu_date='Août 2023 — Fév 2024', exp_reiu_org='REIU-V — Serveur SCP Roleplay',
    exp_reiu_desc='Fondateur et principal gestionnaire d\'une communauté Discord de jeu de rôle SCP, passée à ~150 membres pendant mon passage, puis à 900+ après mon départ. Gestion de l\'infrastructure serveur, de la modération et des cadres narratifs.',

    exp_wr_role='Écrivain', exp_wr_date='~2023 — Présent', exp_wr_org='Indépendant · Backrooms Wikidot · REIU-V · Personnel',
    exp_wr_desc='L\'écriture est le fil conducteur de presque chaque initiative. Première application sérieuse au sein de REIU-V : documents techniques in-universe au format SCP — protocoles, journaux de recherche anormale, procédures d\'effacement de conscience — avec une nouvelle série écrite pour son événement commémoratif d\'août 2025.<br><br>Actif sur le Backrooms Wikidot de février à août 2025 : articles publiés, collaborations et participations aux concours, dont le <em>Despair Writings</em>. Œuvre la plus notable : ' + L360 + ' <em>« Halls of Past Screams »</em> (+17).<br><br>Depuis fin 2025 : roman et scénario, tous deux en cours. <em>A Sound Sinner</em> — scénario post-apocalyptique à la Tarantino. <em>Information Paradox</em> — science-fiction littéraire, registre plus intimiste. En parallèle : le prologue et le résumé narratif d\'Above The Line, posés avant la première ligne de code.',

    exp_fun_role='Fondateur & Chef de Projet', exp_fun_date='~2023 — Jamais sorti',
    exp_fun_org='Subject To F.U.N (Fourth-Wall Understanding Network)',
    exp_fun_desc='Un concept KronStudios — un jeu d\'action-puzzle brisant le quatrième mur, dans l\'esprit de Portal et The Stanley Parable. Le titre lui-même était une blague sarcastique intégrée au concept. Pas une seule ligne de code de production. La Révision 0.01 est toute la trace qu\'il a laissée.',

    exp_tr_role='Fondateur & Directeur', exp_tr_date='~2022 — ~2023', exp_tr_org='T||RUTHLESS — Première Initiative KronStudios',
    exp_tr_desc='Fondateur et directeur de la première initiative KronStudios : un shooter narratif UE5 avec un système de choix semi-libre. Le titre — double lecture délibérée : <em>Ruthless</em> au premier coup d\'œil, <em>Truthless</em> en y regardant de plus près — portée par l\'histoire d\'un soldat nommé Rad Bronx, découvrant un complot gouvernemental centenaire via l\'unité de renseignement I.R.I.S. Directeur de projet et développeur UE5 principal sur ~15 personnes. Jamais de version jouable — mais la leçon de direction qui a structuré tout ce qui a suivi.',

    vision_quote='« Tout ce que je fais plaide pour une seule chose : ces disciplines sont faites pour aller ensemble. »',
    contact_heading='Me contacter', contact_sub='Ouvert au freelance, aux stages, aux collaborations et aux missions commerciales.',
)

# ───────────────────────────── УКРАЇНСЬКА ─────────────────────────────
S['uk'] = dict(
    tag_open='Фриланс · Стажування · Співпраця · Продажі',
    tag_domain='Веб · Геймдев · ШІ · Бекенд · B2B-продажі',

    skills_heading='Навички', skills_sub='Що використовую — згруповано за категоріями.',
    sg_spoken='Розмовні мови', sg_prog='Мови програмування',
    sg_frameworks='Фреймворки / Рантайми', sg_tools='Інструменти / Інфраструктура',
    sg_systems='Системи / Залізо', sg_other='Інше',
    lang_uk='Українська — рідна', lang_fr='Французька — вільно', lang_en='Англійська — вільно',
    lang_ru='Російська — пасивна', lang_es='Іспанська — середній рівень',
    sk_cpp='C++ (базово)', sk_cs='C# (базово)',
    sk_selfhost='Self-hosting', sk_print='3D-друк',
    sk_blender='Blender (базово)', sk_gdocs='Сценарування',
    sk_sales='Консультативні продажі',

    projects_heading='Проекти',
    projects_sub='Вибрані роботи — випущені версії, активні системи та поточні ініціативи.',
    badge_v01='v0.1.0 — Випущено', badge_active='Активний — WIP', badge_paused='WIP — Пауза',
    badge_upcoming='Скоро', badge_closed='Закрито',
    proj_ps_desc='Платформа виконання з фізичним ключем: вставте носій — і відкривається світ. Десктопний застосунок на Tauri з двома сторонами — Builder (візуальний редактор React + Monaco, пайплайн компіляції та підпису) і Runner, що перевіряє ключ носія та показує Kernel повноекранним оверлеєм, ізольованим від хоста. Носій вийнято — сесія завершена, жодного сліду. Фаза 1 вийшла як v0.1.0 з 263 тестами та CI, release і security воркфлоу. Корпоративний рівень, MitoData, — пізніше.',
    proj_lodge_desc='Мовно-незалежний рантайм встановлення з розмовним термінальним інтерфейсом. Lodge читає маніфест, що описує, чим є пакет, визначає, куди має лягти кожен файл у Windows, macOS чи Linux, і виконує встановлення наживо в термінальному інтерфейсі у стилі лісової хатини. Вбудована офлайн-модель розуміє команди звичайною мовою на кшталт «у мене є git?» — 5 crates, 172 тести.',
    proj_expo_desc='Локальний персональний ШІ з голосовим керуванням, що працює повністю на моєму власному залізі. Завжди ввімкнений енергоощадний сервер виконує швидкий тріаж малою локальною LLM, семантичну маршрутизацію намірів, живі запити та довготривалу RAG-пам\'ять із нічною консолідацією; GPU-машина бере на себе важкий інференс. Повністю self-hosted, з регресійними тестами після кожної перебудови.',
    proj_atl_desc='Вертикальна наративна гра на виживання від першої особи: після супервиверження Єллоустоуну на День праці 2039 року атмосфера Ванкувера змінюється. Суспільство розколюється за висотою — над чи під хмарою токсичного газу; гравець залишає крихку безпеку хмарочоса і рухається вгору. Unreal Engine 5.6, (напів)дієгетичний інтерфейс. Директор проекту та наративний керівник від KronStudios-Games.',
    proj_mono_desc='Гра жахів від першої особи у стилі Backrooms від Null Concept, що готується до раннього доступу в Steam. 15 рівнів на старті, кожен зі своїми небезпеками та атмосферою, і три хижаки — Виючий, Гончі та Сірий. Я формував її лор, відповідав за логістику й переклад і створив офіційний сайт.',
    proj_em_desc='Концепт відстеження руху без контролерів на базі ШІ для AR/VR — комп\'ютерний зір і RAG-передбачення, без сенсорів і геймпадів. Я заснував його, визначив технічне бачення та створив публічний сайт, перш ніж проект закрився.',

    experience_heading='Досвід',
    experience_sub='Незалежні ініціативи та фриланс — без штатного працевлаштування, без прикрас.',

    exp_gr_role='Фриланс-представник з продажів', exp_gr_date='Лис 2026',
    exp_gr_org='Grondia — швейцарський SaaS для керування кемпінгами',
    exp_gr_desc='За 50 хвилин підготував і разом із засновником провів дистанційний дзвінок із продажу французькою, адаптувавши пітч під швейцарський кемпінг приблизно на 100 місць — сезонні контракти, каса, платежі в CHF і TWINT, зберігання даних у Швейцарії — і відповів на питання про ціни, міграцію та розташування даних. Вердикт засновника: <em>«буквально ідеально».</em> Потім повний день на стенді Grondia на виставці SETT 2026 у Монпельє: кваліфікував власників кемпінгів і призначав демо.',

    exp_expo_role='Творець і системний інженер', exp_expo_date='2026 — Дотепер',
    exp_expo_org='Expo — інфраструктура персонального ШІ',
    exp_expo_desc='Проектую та будую self-hosted персональний ШІ на двох машинах: завжди ввімкнений сервер із локальним LLM-тріажем, маршрутизацією намірів, RAG-пам\'яттю та чат-інтерфейсом, і GPU-машина для важкого інференсу. Docker Compose, Tailscale, llama.cpp, Qdrant і SQLite, з регресійним набором тестів і нічною самоперевіркою.',

    exp_lodge_role='Творець і провідний розробник', exp_lodge_date='Кві 2026 — Дотепер', exp_lodge_org='Lodge',
    exp_lodge_desc='Створив на Rust рантайм встановлення з термінальним інтерфейсом природною мовою, вбудованою офлайн-моделлю, правилами розміщення для Windows, macOS і Linux та реєстром розширень з автоматичною валідацією. 5 crates, 172 тести, Apache-2.0.',

    exp_ps_role='Засновник і провідний розробник', exp_ps_date='2026 — Дотепер', exp_ps_org='PsyPunker',
    exp_ps_desc='Єдиний архітектор і розробник платформи виконання криптографічних Kernel-бандлів, прив\'язаних до USB. Розробив повну архітектуру — пайплайн підпису, модель пісочниці, прив\'язку до ідентифікатора носія, модель загроз на 20 векторів — і збудував монорепо TypeScript + Rust на Tauri, React, pnpm і Turborepo. Випустив фазу 1 як v0.1.0 (квітень 2026) з 263 тестами та CI, release і security воркфлоу.',

    exp_ks_role='Співзасновник і президент · Директор проекту та наративний керівник', exp_ks_date='2025 — Дотепер',
    exp_ks_org='KronStudios-Games — Above The Line',
    exp_ks_desc='Співзаснував і як президент очолюю волонтерську інді-студію з розподілом доходу (близько дев\'яти людей), що створює Above The Line на Unreal Engine 5.6. Відповідаю за напрям проекту, наративний дизайн, архітектуру лору та координацію команди. Запровадив поетапні віхи, PR-воркфлоу із захищеними гілками, рекрутинг за методом STAR, угоду про розподіл доходу за внеском і GDD-вікі на Quartz; створив сайт студії.',

    exp_nc_role='Менеджер логістики та пропозицій · Автор лору · Наглядач геймплею · Перекладач',
    exp_nc_date='Кві 2025 — Лис 2025', exp_nc_org='Null Concept — Monochromality',
    exp_nc_desc='Долучився на ранньому етапі та задав напрям гри наративними рамками з канону Backrooms Wikidot. Крос-функціональна роль: логістика, координація, лор, нагляд за геймплеєм, часткове озвучення та переклад; створив офіційний сайт. Відійшов через постійні зриви дедлайнів і розбіжність творчого бачення.',

    exp_em_role='CEO, власник і провідний розробник', exp_em_date='2025 — 2026', exp_em_org='EveryMotion',
    exp_em_desc='Заснував і очолив стартап-концепт відстеження руху на базі ШІ для AR/VR. Визначив технічне бачення (комп\'ютерний зір, RAG-передбачення), створив публічний сайт, керував командою та дорожньою картою, доки проект не закрився.',

    exp_reiu_role='Співзасновник і провідний менеджер', exp_reiu_date='Сер 2023 — Лют 2024', exp_reiu_org='REIU-V — SCP Roleplay сервер',
    exp_reiu_desc='Заснував і підтримував Discord-спільноту рольових ігор у стилі SCP, яка виросла до ~150 учасників за час мого перебування і досягла 900+ після відходу. Керував інфраструктурою сервера, модерацією та наративними рамками.',

    exp_wr_role='Письменник', exp_wr_date='~2023 — Дотепер', exp_wr_org='Незалежно · Backrooms Wikidot · REIU-V · Особисте',
    exp_wr_desc='Письменництво проходить паралельною ниткою крізь майже кожну ініціативу. Перше серйозне застосування — спільнота REIU-V: технічні документи у форматі SCP — протоколи, журнали аномальних досліджень, процедури перезапису свідомості — і нова серія для пам\'ятної події у серпні 2025.<br><br>Активний на Backrooms Wikidot з лютого по серпень 2025: статті, колаборації та конкурсні роботи, зокрема <em>Despair Writings</em>. Найпомітніша публікація: ' + L360 + ' <em>«Halls of Past Screams»</em> (+17).<br><br>З кінця 2025: роман і сценарій, обидва в роботі. <em>A Sound Sinner</em> — постапокаліптичний сценарій у стилі Тарантіно. <em>Information Paradox</em> — літературна наукова фантастика, тихіший регістр. Паралельно: пролог і сюжетний конспект Above The Line — наративна основа до першого рядка коду.',

    exp_fun_role='Засновник і менеджер проекту', exp_fun_date='~2023 — Так і не вийшло',
    exp_fun_org='Subject To F.U.N (Fourth-Wall Understanding Network)',
    exp_fun_desc='Концепт KronStudios — екшн-головоломка з руйнуванням четвертої стіни, натхненна Portal і The Stanley Parable. Назва сама по собі була саркастичним жартом, вбудованим у концепцію. Жодного рядка виробничого коду. Ревізія 0.01 — єдиний документ, що від нього залишився.',

    exp_tr_role='Засновник і керівник', exp_tr_date='~2022 — ~2023', exp_tr_org='T||RUTHLESS — Перша ініціатива KronStudios',
    exp_tr_desc='Заснував і керував першою ініціативою KronStudios: наративним шутером на UE5 із системою напіввільного вибору. Назва — навмисне подвійне прочитання: <em>Ruthless</em> на перший погляд, <em>Truthless</em> при уважнішому розгляді — розкрита через історію солдата Рада Бронкса, що викриває вікову урядову змову через підрозділ I.R.I.S. Директор проекту та провідний розробник UE5 у команді ~15 осіб. До робочого прототипу справа не дійшла. Фундаментальний урок, що визначив усе подальше.',

    vision_quote='«Все, що я роблю — це доказ того, що цим речам місце поруч.»',
    contact_heading='Зв\'язатися', contact_sub='Відкритий до фрилансу, стажувань, співпраці та роботи в продажах.',
)

# ───────────────────────────── CV ─────────────────────────────
CV = {
 'en': dict(
   edu_title='Education', free_title='Freelance', intern_title='Internship', exp_title='Experience',
   skills_title='Technical Skills', langs_title='Languages',
   edu=[('Université de Montpellier', 'Sept 2026 – Present', 'Licence Informatique (Computer Science), first year'),
        ('Lycée Rosa Luxemburg — Canet-en-Roussillon', 'Jan – June 2026', 'Terminale · Baccalauréat'),
        ('Lycée Jules Siegfried — Le Havre', '2023 – Dec 2025', 'Seconde · Première · Terminale (first semester)'),
        ('Collège Belle Etoile — Montivilliers', '2023', 'Diplôme national du Brevet, Mention Très Bien')],
   free=[('Grondia — B2B SaaS, Switzerland', 'Nov 2026', 'Freelance Sales Rep: French-language remote sales call co-led with the founder (feedback: "literally perfect"), plus a full day on the trade-show stand at SETT 2026, Montpellier.')],
   intern=[('HAROPA Port — Le Havre, SI Department', 'June 2024', "Observation internship within the information systems department of one of Europe's largest port authorities.")],
   exp=[('Creator &amp; Systems Engineer', '2026 — Present', 'Expo — personal AI infrastructure', 'Self-hosted personal AI across two machines: always-on server with local LLM triage, intent routing, RAG memory and chat UI; GPU rig for heavy inference. Docker Compose, Tailscale, llama.cpp, Qdrant, SQLite.'),
        ('Creator &amp; Lead Developer', 'Apr 2026 — Present', 'Lodge', 'Rust installer runtime with a natural-language terminal UI, bundled offline model and per-OS placement rulesets. 5 crates, 172 tests, Apache-2.0.'),
        ('Founder &amp; Lead Developer', '2026 — Present', 'PsyPunker', 'Sole architect of a USB-bound cryptographic Kernel execution platform (Tauri, React, Rust, TypeScript monorepo). Shipped Phase 1 as v0.1.0 in April 2026 with 263 tests and CI, release and security workflows.'),
        ('Co-Founder &amp; President · Project Director', '2025 — Present', 'KronStudios-Games — Above The Line', 'Lead a ~9-person volunteer revenue-share studio building a narrative survival game in Unreal Engine 5.6. Project direction, narrative design, PR workflow, STAR recruiting, merit-weighted revenue share, Quartz GDD wiki.'),
        ('Logistics Manager · Lore Writer · Gameplay Overseer · Translator', 'Apr 2025 — Nov 2025', 'Null Concept — Monochromality (Steam, upcoming)', 'Cross-functional contributor on an upcoming Backrooms horror game: lore frameworks, logistics, gameplay oversight, partial voice acting, translation; built the official website.'),
        ('CEO, Owner &amp; Lead Developer', '2025 — 2026', 'EveryMotion', 'Founded an AI motion-tracking startup concept for AR/VR; set the technical vision and built the public site before the venture shut down.'),
        ('Co-Founder &amp; Lead Manager', 'Aug 2023 — Feb 2024', 'REIU-V — SCP Roleplay Discord Server', 'Grew an SCP roleplay community to ~150 members (900+ after departure); infrastructure, moderation and narrative frameworks.'),
        ('Writer', '~2023 — Present', 'Independent · Backrooms Wikidot · REIU-V · Personal', 'Published Backrooms Wikidot articles (Level 360, +17) and contest entries; in-universe SCP technical documents; screenplay and novel in progress: <em>A Sound Sinner</em>, <em>Information Paradox</em>.', True),
        ('Founder &amp; Lead', '~2022 — ~2023', 'T||RUTHLESS &amp; Subject To F.U.N — First KronStudios initiatives', 'Directed two UE5 game projects as Project Manager and Head Developer across ~15 people; full GDDs and storyline addenda. Neither reached a playable build — the leadership lesson behind everything after.')],
   skills=[('Languages', 'TypeScript, JavaScript, Python, Rust, HTML/CSS, UE Blueprint, SQL · familiar: C++, C#'),
           ('Engines / Runtimes', 'Unreal Engine 5, Tauri, React, Node.js, llama.cpp, ratatui'),
           ('Tooling', 'Git + Git LFS, GitHub Actions, pnpm + Turborepo, Vitest, ESLint, Docker Compose'),
           ('Systems / Hardware', 'Linux, Tailscale, self-hosting (Coolify, Supabase, n8n), Qdrant, SQLite, Arduino / ESP32, 3D printing'),
           ('Other', 'Consultative sales (FR/EN), Obsidian + Quartz, Lore Forge, Blender (basic), Google Docs (scriptwriting)')],
   langs=[('Ukrainian', 'native'), ('French', 'fluent'), ('English', 'fluent'), ('Russian', 'passive'), ('Spanish', 'moderate')],
 ),
 'fr': dict(
   edu_title='Formation', free_title='Freelance', intern_title='Stage', exp_title='Expérience',
   skills_title='Compétences Techniques', langs_title='Langues',
   edu=[('Université de Montpellier', 'Sept 2026 – Présent', 'Licence Informatique, première année'),
        ('Lycée Rosa Luxemburg — Canet-en-Roussillon', 'Janv – Juin 2026', 'Terminale · Baccalauréat'),
        ('Lycée Jules Siegfried — Le Havre', '2023 – Déc 2025', 'Seconde · Première · Terminale (premier semestre)'),
        ('Collège Belle Etoile — Montivilliers', '2023', 'Diplôme national du Brevet, Mention Très Bien')],
   free=[('Grondia — SaaS B2B, Suisse', 'Nov 2026', 'Commercial indépendant : appel de vente à distance en français aux côtés du fondateur (retour : « littéralement parfait »), et animation commerciale du stand au SETT 2026 (Montpellier).')],
   intern=[('HAROPA Port — Le Havre, Département SI', 'Juin 2024', "Stage d'observation au sein du département des systèmes d'information de l'un des plus grands ports d'Europe.")],
   exp=[('Créateur &amp; Ingénieur Systèmes', '2026 — Présent', 'Expo — infrastructure d\'IA personnelle', 'IA personnelle auto-hébergée sur deux machines : serveur toujours allumé (tri par LLM local, routage des intentions, mémoire RAG, interface de chat) et machine GPU pour l\'inférence lourde. Docker Compose, Tailscale, llama.cpp, Qdrant, SQLite.'),
        ('Créateur &amp; Développeur Principal', 'Avr 2026 — Présent', 'Lodge', 'Runtime d\'installation en Rust avec interface terminal en langage naturel, modèle hors-ligne intégré et règles de placement par OS. 5 crates, 172 tests, Apache-2.0.'),
        ('Fondateur &amp; Développeur Principal', '2026 — Présent', 'PsyPunker', 'Seul architecte d\'une plateforme d\'exécution de Kernels cryptographiques liés à une clé USB (monorepo Tauri, React, Rust, TypeScript). Phase 1 livrée en v0.1.0 en avril 2026, avec 263 tests et des workflows CI, release et sécurité.'),
        ('Co-fondateur &amp; Président · Directeur de Projet', '2025 — Présent', 'KronStudios-Games — Above The Line', 'Direction d\'un studio bénévole à partage de revenus (~9 personnes) qui développe un jeu de survie narratif sous Unreal Engine 5.6. Direction de projet, design narratif, workflow de PR, recrutement STAR, partage des revenus au mérite, wiki GDD Quartz.'),
        ('Responsable Logistique · Auteur de Lore · Superviseur Gameplay · Traducteur', 'Avr 2025 — Nov 2025', 'Null Concept — Monochromality (Steam, à venir)', 'Contributeur transversal sur un jeu d\'horreur Backrooms à venir : cadres narratifs, logistique, supervision du gameplay, doublage partiel, traduction ; création du site officiel.'),
        ('PDG, Fondateur &amp; Développeur Principal', '2025 — 2026', 'EveryMotion', 'Fondateur d\'un concept de startup de suivi de mouvement par IA pour l\'AR/VR ; vision technique et site public, avant l\'arrêt du projet.'),
        ('Co-Fondateur &amp; Responsable Principal', 'Août 2023 — Fév 2024', 'REIU-V — Serveur Discord SCP Roleplay', 'Communauté de jeu de rôle SCP portée à ~150 membres (900+ après mon départ) ; infrastructure, modération et cadres narratifs.'),
        ('Écrivain', '~2023 — Présent', 'Indépendant · Backrooms Wikidot · REIU-V · Personnel', 'Articles publiés sur le Backrooms Wikidot (Level 360, +17) et participations aux concours ; documents techniques SCP in-universe ; scénario et roman en cours : <em>A Sound Sinner</em>, <em>Information Paradox</em>.', True),
        ('Fondateur &amp; Directeur', '~2022 — ~2023', 'T||RUTHLESS &amp; Subject To F.U.N — Premières initiatives KronStudios', 'Direction de deux projets de jeux UE5 comme chef de projet et développeur principal sur ~15 personnes ; GDD complets et addenda narratifs. Aucune version jouable — la leçon de direction derrière tout ce qui a suivi.')],
   skills=[('Langages', 'TypeScript, JavaScript, Python, Rust, HTML/CSS, UE Blueprint, SQL · notions : C++, C#'),
           ('Moteurs / Runtimes', 'Unreal Engine 5, Tauri, React, Node.js, llama.cpp, ratatui'),
           ('Outils', 'Git + Git LFS, GitHub Actions, pnpm + Turborepo, Vitest, ESLint, Docker Compose'),
           ('Systèmes / Matériel', 'Linux, Tailscale, auto-hébergement (Coolify, Supabase, n8n), Qdrant, SQLite, Arduino / ESP32, impression 3D'),
           ('Autre', 'Vente conseil (FR/EN), Obsidian + Quartz, Lore Forge, Blender (notions), Google Docs (scénarisation)')],
   langs=[('Ukrainien', 'langue maternelle'), ('Français', 'courant'), ('Anglais', 'courant'), ('Russe', 'passif'), ('Espagnol', 'intermédiaire')],
 ),
 'uk': dict(
   edu_title='Освіта', free_title='Фриланс', intern_title='Стажування', exp_title='Досвід',
   skills_title='Технічні навички', langs_title='Мови',
   edu=[('Université de Montpellier', 'Вер 2026 – дотепер', 'Licence Informatique (комп\'ютерні науки), перший курс'),
        ('Lycée Rosa Luxemburg — Canet-en-Roussillon', 'Січ – чер 2026', 'Terminale · Baccalauréat'),
        ('Lycée Jules Siegfried — Le Havre', '2023 – гру 2025', 'Seconde · Première · Terminale (перший семестр)'),
        ('Collège Belle Etoile — Montivilliers', '2023', 'Diplôme national du Brevet, Mention Très Bien (з відзнакою)')],
   free=[('Grondia — B2B SaaS, Швейцарія', 'Лис 2026', 'Фриланс-представник з продажів: дистанційний дзвінок французькою разом із засновником (відгук: «буквально ідеально») і повний день на стенді виставки SETT 2026, Монпельє.')],
   intern=[('HAROPA Port — Гавр, ІТ-департамент (SI)', 'Чер 2024', 'Ознайомче стажування в департаменті інформаційних систем одного з найбільших портів Європи.')],
   exp=[('Творець і системний інженер', '2026 — Дотепер', 'Expo — інфраструктура персонального ШІ', 'Self-hosted персональний ШІ на двох машинах: завжди ввімкнений сервер (локальний LLM-тріаж, маршрутизація намірів, RAG-пам\'ять, чат) і GPU-машина для важкого інференсу. Docker Compose, Tailscale, llama.cpp, Qdrant, SQLite.'),
        ('Творець і провідний розробник', 'Кві 2026 — Дотепер', 'Lodge', 'Рантайм встановлення на Rust з термінальним інтерфейсом природною мовою, вбудованою офлайн-моделлю та правилами розміщення для кожної ОС. 5 crates, 172 тести, Apache-2.0.'),
        ('Засновник і провідний розробник', '2026 — Дотепер', 'PsyPunker', 'Єдиний архітектор платформи виконання криптографічних Kernel-бандлів, прив\'язаних до USB (монорепо Tauri, React, Rust, TypeScript). Фаза 1 випущена як v0.1.0 у квітні 2026, 263 тести, CI, release і security воркфлоу.'),
        ('Співзасновник і президент · Директор проекту', '2025 — Дотепер', 'KronStudios-Games — Above The Line', 'Очолюю волонтерську студію з розподілом доходу (~9 людей), що створює наративну гру на виживання на Unreal Engine 5.6. Напрям проекту, наративний дизайн, PR-воркфлоу, STAR-рекрутинг, розподіл доходу за внеском, GDD-вікі на Quartz.'),
        ('Менеджер логістики · Автор лору · Наглядач геймплею · Перекладач', 'Кві 2025 — Лис 2025', 'Null Concept — Monochromality (Steam, скоро)', 'Крос-функціональний учасник гри жахів Backrooms, що готується до виходу: лор, логістика, нагляд за геймплеєм, часткове озвучення, переклад; створив офіційний сайт.'),
        ('CEO, власник і провідний розробник', '2025 — 2026', 'EveryMotion', 'Заснував стартап-концепт відстеження руху на базі ШІ для AR/VR; технічне бачення та публічний сайт, доки проект не закрився.'),
        ('Співзасновник і провідний менеджер', 'Сер 2023 — Лют 2024', 'REIU-V — SCP Roleplay Discord-сервер', 'Виростив спільноту SCP-рольових ігор до ~150 учасників (900+ після відходу); інфраструктура, модерація, наративні рамки.'),
        ('Письменник', '~2023 — Дотепер', 'Незалежно · Backrooms Wikidot · REIU-V · Особисте', 'Опубліковані статті на Backrooms Wikidot (Level 360, +17) і конкурсні роботи; внутрішньосвітові технічні документи SCP; сценарій і роман у роботі: <em>A Sound Sinner</em>, <em>Information Paradox</em>.', True),
        ('Засновник і керівник', '~2022 — ~2023', 'T||RUTHLESS і Subject To F.U.N — перші ініціативи KronStudios', 'Керував двома проектами ігор на UE5 як менеджер проекту та провідний розробник у команді ~15 осіб; повні GDD і сюжетні додатки. До робочої версії не дійшло — урок лідерства, що визначив усе подальше.')],
   skills=[('Мови', 'TypeScript, JavaScript, Python, Rust, HTML/CSS, UE Blueprint, SQL · базово: C++, C#'),
           ('Рушії / Рантайми', 'Unreal Engine 5, Tauri, React, Node.js, llama.cpp, ratatui'),
           ('Інструменти', 'Git + Git LFS, GitHub Actions, pnpm + Turborepo, Vitest, ESLint, Docker Compose'),
           ('Системи / Залізо', 'Linux, Tailscale, self-hosting (Coolify, Supabase, n8n), Qdrant, SQLite, Arduino / ESP32, 3D-друк'),
           ('Інше', 'Консультативні продажі (FR/EN), Obsidian + Quartz, Lore Forge, Blender (базово), Google Docs (сценарування)')],
   langs=[('Українська', 'рідна'), ('Французька', 'вільно'), ('Англійська', 'вільно'), ('Російська', 'пасивна'), ('Іспанська', 'середній рівень')],
 ),
}
