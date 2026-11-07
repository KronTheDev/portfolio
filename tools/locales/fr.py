# -*- coding: utf-8 -*-
"""Français. Écrit pour être lu en français, pas traduit mot à mot depuis en.py.
Mêmes clés que en.py ; le build refuse toute clé manquante ou en trop."""

L360 = '<a href="https://backrooms-wiki.wikidot.com/level-360" target="_blank" rel="noopener" class="tl-link">Level 360 ↗</a>'

STRINGS = {
    'nav_home': 'Accueil', 'nav_about': 'Profil', 'nav_skills': 'Compétences',
    'nav_projects': 'Projets', 'nav_experience': 'Parcours', 'nav_contact': 'Contact',

    'hero_eyebrow': 'Je vous souhaite la bienvenue',
    'roles': ['Développeur', 'Ingénieur systèmes', 'Game designer', 'Architecte d\'univers', 'Scénariste'],
    'hero_cta_view': 'Voir mes projets', 'hero_cta_touch': 'Me contacter',
    'hero_tagline': "L'avenir ne viendra jamais à nous. Jamais. C'est à nous d'aller vers lui. Toujours.",

    'about_heading': 'Qui je suis',
    'bio_hey': '« Salut. »',
    'bio_p1_l1': 'Vous connaissez déjà ce genre d\'introduction, alors allons droit au but : je suis <span id="glitchName">Andrew</span>, et je fabrique des choses qui, en principe, n\'ont rien à faire dans le même portfolio.',
    'bio_p1_l2': 'Du code, des systèmes, des mondes — et les mots qui font tenir le tout.',
    'bio_p1_l3': 'Ukrainien et français, je parle couramment quatre langues, et une cinquième à peu près — <em>je vous épargne la démonstration.</em> Ce va-et-vient entre l\'éditeur de code et des mondes qui n\'existent pas encore se sent dans tout ce que je fais.',
    'bio_p1_l4': 'Ce portfolio en est la version longue.',
    'bio_p1_l5': 'Descendez, la suite est en bas.',
    'bio_p2': 'Ce qui m\'intéresse aujourd\'hui, c\'est le point exact où ces disciplines se rencontrent : quand un système a besoin d\'une histoire pour avoir un sens, ou qu\'une histoire a besoin d\'un système pour tenir debout. On attend souvent de choisir une voie. Je n\'ai jamais su faire.<br>Ce que je cherche à construire se passe d\'étiquette. Des jeux qui se lisent comme des romans. Des récits bâtis comme de l\'architecture. Du code au service de quelque chose de plus grand, sans perdre sa propre personnalité. Bref, un reflet assez fidèle de ce que je suis.<br>S\'il y a une différence, c\'est celle-ci : pour moi, ce ne sont pas des métiers séparés. Ils se répondent et <em>se contaminent</em> sans arrêt.<br>Et c\'est presque toujours dans cette contamination que naît le travail le plus intéressant. Je parle d\'expérience.',
    'tag_location': 'France / Ukraine',
    'tag_open': 'Freelance · Stage · Collaboration · Vente',
    'tag_domain': 'Web · Jeu vidéo · IA · Back-end · Vente B2B',

    'skills_heading': 'Compétences', 'skills_sub': 'Ce avec quoi je travaille, par catégorie.',
    'sg_spoken': 'Langues', 'sg_prog': 'Langages de programmation',
    'sg_frameworks': 'Frameworks et moteurs', 'sg_tools': 'Outils et infrastructure',
    'sg_systems': 'Systèmes et matériel', 'sg_other': 'Autres',
    'lang_uk': 'Ukrainien — langue maternelle', 'lang_fr': 'Français — courant', 'lang_en': 'Anglais — courant',
    'lang_ru': 'Russe — compréhension', 'lang_es': 'Espagnol — intermédiaire',
    'sk_cpp': 'C++ (bases)', 'sk_cs': 'C# (bases)',
    'sk_selfhost': 'Auto-hébergement', 'sk_print': 'Impression 3D',
    'sk_blender': 'Blender (bases)', 'sk_gdocs': 'Écriture de scénario',
    'sk_sales': 'Vente conseil',

    'projects_heading': 'Projets',
    'projects_sub': 'Une sélection : versions livrées, systèmes en service et chantiers en cours.',
    'badge_v01': 'v0.1.0 — Livré', 'badge_active': 'En cours', 'badge_paused': 'En pause',
    'badge_upcoming': 'À venir', 'badge_closed': 'Arrêté',
    'proj_ps_desc': 'Une plateforme d\'exécution à clé physique : on branche une clé USB, un monde s\'ouvre. L\'application Tauri a deux faces — un Builder (éditeur visuel React + Monaco, compilation et signature) et un Runner qui vérifie la clé et affiche le Kernel en plein écran, isolé de la machine hôte. On retire la clé : la session s\'arrête, sans laisser de trace. La phase 1 est sortie en v0.1.0, avec 263 tests et des pipelines CI, de publication et de sécurité. Sa déclinaison entreprise, MitoData, viendra plus tard.',
    'proj_lodge_desc': 'Un installateur indépendant du langage, piloté depuis le terminal en langage naturel. Lodge lit un manifeste qui décrit le paquet, détermine où chaque fichier doit aller sous Windows, macOS ou Linux, et déroule l\'installation en direct dans une interface terminal à l\'ambiance chalet. Un petit modèle embarqué, sans connexion, comprend des demandes comme « est-ce que j\'ai git ? ». 5 crates, 172 tests.',
    'proj_expo_desc': 'Une IA personnelle, locale et pilotée à la voix, qui tourne entièrement sur mon matériel. Un serveur sobre, allumé en permanence, fait le premier tri avec un petit LLM local, oriente chaque demande, va chercher l\'information en direct et entretient une mémoire RAG consolidée chaque nuit ; une machine GPU se charge des calculs lourds. Tout est auto-hébergé, et une batterie de tests de non-régression tourne après chaque mise à jour.',
    'proj_atl_desc': 'Un jeu de survie narratif et vertical, à la première personne. Labor Day 2039 : le Yellowstone entre en éruption et l\'air de Vancouver devient irrespirable. La société se divise désormais par l\'altitude — au-dessus ou en dessous d\'un nuage toxique — et le joueur quitte l\'abri fragile d\'une tour pour monter toujours plus haut. Unreal Engine 5.6, interface (semi-)diégétique. Direction du projet et de la narration chez KronStudios-Games.',
    'proj_mono_desc': 'Un jeu d\'horreur à la première personne inspiré des Backrooms, développé par Null Concept et bientôt en accès anticipé sur Steam. 15 niveaux prévus à la sortie, chacun avec ses dangers et son ambiance sonore, et trois prédateurs : le Hurleur, les Chiens et l\'Éteint. J\'ai façonné son lore, géré la logistique et la traduction, et créé le site officiel.',
    'proj_em_desc': 'Un concept de capture de mouvement par IA pour la réalité virtuelle et augmentée, sans capteurs ni manettes : vision par ordinateur et prédiction assistée par RAG. Je l\'ai fondé, j\'en ai fixé la vision technique et j\'ai créé le site, avant que le projet ne s\'arrête.',

    'experience_heading': 'Parcours',
    'experience_sub': 'Projets personnels et missions freelance — pas d\'emploi salarié, et je ne prétends pas le contraire.',

    'exp_gr_role': 'Commercial indépendant', 'exp_gr_date': 'Nov. 2026',
    'exp_gr_org': 'Grondia — logiciel suisse de gestion de campings',
    'exp_gr_desc': 'Appelé 50 minutes avant le rendez-vous, j\'ai préparé puis co-animé avec le fondateur un appel de vente en français, avec un pitch taillé pour un camping suisse d\'une centaine d\'emplacements : contrats saisonniers, caisse, paiements en CHF et TWINT, données hébergées en Suisse. J\'ai répondu aux questions sur les tarifs, la migration et la localisation des données. Le verdict du fondateur : <em>« littéralement parfait ».</em> J\'ai ensuite tenu le stand Grondia une journée entière au SETT 2026 à Montpellier, à qualifier des gérants de campings et à caler des démos.',

    'exp_expo_role': 'Créateur et ingénieur systèmes', 'exp_expo_date': '2026 — aujourd\'hui',
    'exp_expo_org': 'Expo — infrastructure d\'IA personnelle',
    'exp_expo_desc': 'Je conçois et construis une IA personnelle auto-hébergée, répartie sur deux machines : un serveur allumé en permanence (tri par LLM local, routage des demandes, mémoire RAG, interface de discussion) et une machine GPU pour l\'inférence lourde. Docker Compose, Tailscale, llama.cpp, Qdrant et SQLite, avec tests de non-régression et auto-évaluation chaque nuit.',

    'exp_lodge_role': 'Créateur et développeur principal', 'exp_lodge_date': 'Avr. 2026 — aujourd\'hui', 'exp_lodge_org': 'Lodge',
    'exp_lodge_desc': 'Développement en Rust d\'un installateur qu\'on pilote en langage naturel depuis le terminal : modèle embarqué hors ligne, règles de placement pour Windows, macOS et Linux, et registre d\'extensions validé automatiquement. 5 crates, 172 tests, licence Apache-2.0.',

    'exp_ps_role': 'Fondateur et développeur principal', 'exp_ps_date': '2026 — aujourd\'hui', 'exp_ps_org': 'PsyPunker',
    'exp_ps_desc': 'Seul architecte et développeur d\'une plateforme qui exécute des Kernels chiffrés et signés, liés à une clé USB. J\'ai conçu toute l\'architecture — chaîne de signature, bac à sable, liaison à l\'identité du support, modèle de menaces sur 20 vecteurs — et monté un monorepo TypeScript + Rust (Tauri, React, pnpm, Turborepo). Phase 1 livrée en v0.1.0 en avril 2026, avec 263 tests et des pipelines CI, de publication et de sécurité.',

    'exp_ks_role': 'Cofondateur et président · Direction du projet et de la narration', 'exp_ks_date': '2025 — aujourd\'hui',
    'exp_ks_org': 'KronStudios-Games — Above The Line',
    'exp_ks_desc': 'Je préside un studio indépendant d\'une dizaine de bénévoles, rémunérés en parts de revenus, qui développe Above The Line sous Unreal Engine 5.6. Je pilote la direction du projet, le design narratif, la construction de l\'univers et la coordination. J\'ai mis en place des jalons par phases, un workflow de revue sur branches protégées, des entretiens de recrutement structurés (méthode STAR), un partage des revenus au mérite et un wiki de game design sous Quartz, et j\'ai créé le site du studio.',

    'exp_nc_role': 'Logistique et suggestions · Écriture du lore · Supervision du gameplay · Traduction',
    'exp_nc_date': 'Avr. 2025 — nov. 2025', 'exp_nc_org': 'Null Concept — Monochromality',
    'exp_nc_desc': 'Arrivé tôt sur le projet, j\'ai orienté le jeu en y apportant des bases narratives tirées du canon du Backrooms Wikidot. Un rôle transversal : logistique, coordination, écriture du lore, supervision du gameplay, un peu de doublage et la traduction ; j\'ai aussi créé le site officiel. Je me suis mis en retrait face aux retards à répétition et à une vision créative qui divergeait.',

    'exp_em_role': 'PDG, fondateur et développeur principal', 'exp_em_date': '2025 — 2026', 'exp_em_org': 'EveryMotion',
    'exp_em_desc': 'J\'ai fondé et dirigé un projet de startup de capture de mouvement par IA pour la réalité virtuelle et augmentée : vision technique (vision par ordinateur, prédiction par RAG), site public, petite équipe et feuille de route, jusqu\'à l\'arrêt du projet.',

    'exp_reiu_role': 'Cofondateur et responsable principal', 'exp_reiu_date': 'Août 2023 — févr. 2024', 'exp_reiu_org': 'REIU-V — serveur de jeu de rôle SCP',
    'exp_reiu_desc': 'J\'ai fondé et fait vivre une communauté Discord de jeu de rôle SCP, passée à environ 150 membres sous ma direction, puis à plus de 900 après mon départ. Infrastructure du serveur, modération et cadre narratif.',

    'exp_wr_role': 'Auteur', 'exp_wr_date': '~2023 — aujourd\'hui', 'exp_wr_org': 'Indépendant · Backrooms Wikidot · REIU-V · Projets personnels',
    'exp_wr_desc': 'L\'écriture traverse presque tous mes projets. Sa première vraie application, c\'est REIU-V : des documents internes au format SCP, au ton clinique — protocoles techniques, rapports de recherche sur des anomalies, procédures de réécriture de la conscience — et une nouvelle série écrite pour l\'événement commémoratif d\'août 2025.<br><br>Sur le Backrooms Wikidot, de février à août 2025 : articles publiés, textes à plusieurs mains et participations à des concours, dont <em>Despair Writings</em>. Mon texte le plus connu : ' + L360 + ' <em>« Halls of Past Screams »</em> (+17).<br><br>Depuis fin 2025 : un scénario et un roman, tous deux en cours. <em>A Sound Sinner</em>, western post-apocalyptique à la construction tarantinesque. <em>Information Paradox</em>, science-fiction littéraire, plus intime. En parallèle, le prologue et la trame d\'Above The Line, écrits avant la toute première ligne de code.',

    'exp_fun_role': 'Fondateur et chef de projet', 'exp_fun_date': '~2023 — jamais sorti',
    'exp_fun_org': 'Subject To F.U.N (Fourth-Wall Understanding Network)',
    'exp_fun_desc': 'Un concept KronStudios : un jeu d\'action et d\'énigmes qui brise le quatrième mur, dans la lignée de Portal et The Stanley Parable. Le titre lui-même était une blague sarcastique, au cœur du concept. Aucune ligne de code de production n\'a vu le jour ; la révision 0.01 du document de design est tout ce qu\'il en reste.',

    'exp_tr_role': 'Fondateur et directeur', 'exp_tr_date': '~2022 — ~2023', 'exp_tr_org': 'T||RUTHLESS — premier projet KronStudios',
    'exp_tr_desc': 'Le premier projet KronStudios, que j\'ai fondé et dirigé : un jeu de tir narratif sous UE5, avec une histoire à choix semi-libres. Un titre à double lecture — <em>Ruthless</em> au premier regard, <em>Truthless</em> au second — qui résume l\'histoire de Rad Bronx, un soldat qui découvre, grâce à l\'unité de renseignement I.R.I.S., un complot gouvernemental vieux d\'un siècle. Chef de projet et développeur UE5 principal d\'une équipe d\'environ 15 personnes. Le jeu n\'a jamais atteint de version jouable, mais c\'est la leçon de direction qui a structuré tout le reste.',

    'vision_quote': '« Tout ce que je crée défend une même idée : ces disciplines vont ensemble. »',
    'contact_heading': 'Me contacter', 'contact_sub': 'Disponible pour du freelance, un stage, une collaboration ou des missions commerciales.',
}

CV = {
    'preview': 'Aperçu du CV', 'back': '← Portfolio', 'save': '↓ Enregistrer en PDF',
    'edu_title': 'Formation', 'free_title': 'Missions freelance', 'intern_title': 'Stages', 'exp_title': 'Expérience',
    'skills_title': 'Compétences techniques', 'langs_title': 'Langues',
    'edu': [('Université de Montpellier', 'Sept. 2026 – aujourd\'hui', 'Licence Informatique, 1re année'),
            ('Lycée Rosa Luxemburg — Canet-en-Roussillon', 'Janv. – juin 2026', 'Terminale · Baccalauréat'),
            ('Lycée Jules Siegfried — Le Havre', '2023 – déc. 2025', 'Seconde · Première · Terminale (1er semestre)'),
            ('Collège Belle Etoile — Montivilliers', '2023', 'Diplôme national du brevet, mention très bien')],
    'free': [('Grondia — logiciel SaaS B2B, Suisse', 'Nov. 2026', 'Commercial indépendant : appel de vente en français co-animé avec le fondateur (retour : « littéralement parfait »), puis une journée sur le stand au SETT 2026, à Montpellier.')],
    'intern': [('HAROPA Port — Le Havre, direction des systèmes d\'information', 'Juin 2024', 'Stage d\'observation au service informatique de l\'un des plus grands ports d\'Europe.')],
    'exp': [('Créateur et ingénieur systèmes', '2026 — aujourd\'hui', 'Expo — infrastructure d\'IA personnelle', 'IA personnelle auto-hébergée sur deux machines : un serveur toujours allumé (tri par LLM local, routage des demandes, mémoire RAG, interface de discussion) et une machine GPU pour l\'inférence lourde. Docker Compose, Tailscale, llama.cpp, Qdrant, SQLite.'),
            ('Créateur et développeur principal', 'Avr. 2026 — aujourd\'hui', 'Lodge', 'Installateur en Rust piloté en langage naturel depuis le terminal, avec modèle embarqué hors ligne et règles de placement par système. 5 crates, 172 tests, licence Apache-2.0.'),
            ('Fondateur et développeur principal', '2026 — aujourd\'hui', 'PsyPunker', 'Seul architecte d\'une plateforme qui exécute des Kernels signés et chiffrés liés à une clé USB (monorepo Tauri, React, Rust, TypeScript). Phase 1 livrée en v0.1.0 en avril 2026 : 263 tests, pipelines CI, de publication et de sécurité.'),
            ('Cofondateur et président · Direction du projet', '2025 — aujourd\'hui', 'KronStudios-Games — Above The Line', 'Je préside un studio d\'une dizaine de bénévoles rémunérés en parts de revenus, qui développe un jeu de survie narratif sous Unreal Engine 5.6. Direction du projet, design narratif, workflow de revue, recrutement par entretiens STAR, partage des revenus au mérite, wiki de game design Quartz.'),
            ('Logistique · Écriture du lore · Supervision du gameplay · Traduction', 'Avr. 2025 — nov. 2025', 'Null Concept — Monochromality (Steam, à venir)', 'Rôle transversal sur un jeu d\'horreur Backrooms à venir : bases narratives, logistique, supervision du gameplay, un peu de doublage, traduction ; création du site officiel.'),
            ('PDG, fondateur et développeur principal', '2025 — 2026', 'EveryMotion', 'Projet de startup de capture de mouvement par IA pour la VR et l\'AR : vision technique et site public, jusqu\'à l\'arrêt du projet.'),
            ('Cofondateur et responsable principal', 'Août 2023 — févr. 2024', 'REIU-V — serveur Discord de jeu de rôle SCP', 'Communauté portée à environ 150 membres (plus de 900 après mon départ) : infrastructure, modération, cadre narratif.'),
            ('Auteur', '~2023 — aujourd\'hui', 'Indépendant · Backrooms Wikidot · REIU-V · Projets personnels', 'Articles publiés sur le Backrooms Wikidot (Level 360, +17) et participations à des concours ; documents SCP internes à l\'univers ; un scénario et un roman en cours : <em>A Sound Sinner</em>, <em>Information Paradox</em>.', True),
            ('Fondateur et directeur', '~2022 — ~2023', 'T||RUTHLESS et Subject To F.U.N — premiers projets KronStudios', 'Deux projets de jeux sous UE5, comme chef de projet et développeur principal d\'une équipe d\'environ 15 personnes ; documents de design complets et trames scénaristiques. Aucun n\'a atteint de version jouable — mais c\'est la leçon de direction qui a structuré tout le reste.')],
    'skills': [('Langages', 'TypeScript, JavaScript, Python, Rust, HTML/CSS, UE Blueprint, SQL · bases : C++, C#'),
               ('Moteurs et frameworks', 'Unreal Engine 5, Tauri, React, Node.js, llama.cpp, ratatui'),
               ('Outils', 'Git + Git LFS, GitHub Actions, pnpm + Turborepo, Vitest, ESLint, Docker Compose'),
               ('Systèmes et matériel', 'Linux, Tailscale, auto-hébergement (Coolify, Supabase, n8n), Qdrant, SQLite, Arduino / ESP32, impression 3D'),
               ('Autres', 'Vente conseil (FR/EN), Obsidian + Quartz, Lore Forge, Blender (bases), écriture de scénario')],
    'langs': [('Ukrainien', 'langue maternelle'), ('Français', 'courant'), ('Anglais', 'courant'), ('Russe', 'compréhension'), ('Espagnol', 'intermédiaire')],
}
