# Kit « Power Apps avec Claude » — Guide d'installation et d'utilisation

Ce kit reprend la méthode de la vidéo **« How I Build Power Apps 3x Faster With Claude »** (Ben Fetters) :
faire construire à Claude des applications **Power Apps Canvas** *comme vous les construisez*, grâce à un
projet Claude qui connaît vos données et à une « équipe » de skills spécialisés.

> ℹ️ Le kit a été construit à partir du plan de la vidéo (ses chapitres) et de la documentation officielle
> Microsoft du serveur *Canvas Authoring MCP*. La transcription de la vidéo n'était pas accessible, donc
> les détails peuvent différer de ce que montre l'auteur.

## Sommaire

1. [La méthode en un coup d'œil](#1-la-méthode-en-un-coup-dœil)
2. [Contenu du kit](#2-contenu-du-kit)
3. [Ce qu'il vous faut (et ce qui est gratuit)](#3-ce-quil-vous-faut-et-ce-qui-est-gratuit)
4. [Installation](#4-installation)
5. [Utilisation pas à pas](#5-utilisation-pas-à-pas)
6. [Corriger les bugs et enseigner aux skills](#6-corriger-les-bugs-et-enseigner-aux-skills)
7. [YAML ou MCP : laquelle choisir ?](#7-yaml-ou-mcp--laquelle-choisir-)
8. [Dépannage](#8-dépannage)

---

## 1. La méthode en un coup d'œil

| Chapitre de la vidéo | Ce que fait le kit |
|---|---|
| Set up a Claude project with your data | `projet-claude/` : instructions + modèle de données + vos standards |
| Build your team of skills | 4 skills dans `skills/` (et prêts à importer dans `dist/`) |
| Step 1 : Get a design brief | skill **pa-design-brief** |
| Step 2 : Build a playable mock-up | skill **pa-mockup** (maquette HTML cliquable + spécification) |
| Method 1 : Build with MCP | skill **pa-build-mcp** (Claude Code + serveur MCP Microsoft) |
| Fix bugs and teach your skill | fichier `lecons-apprises.md` dans chaque skill de construction |
| Method 2 : Edit with YAML | skill **pa-yaml-edit** (copier / coller le code dans Studio) |

```
Idée ──► 1. Design brief ──► 2. Maquette jouable ──► 3a. Construction MCP  ─┐
                                    + spécification   3b. Construction YAML ─┼─► Test ─► Bug ? ─► Leçon apprise
```

## 2. Contenu du kit

```
powerapps-claude-toolkit/
├── README.md                         ← ce guide
├── projet-claude/
│   ├── instructions-projet.md        ← à coller dans les instructions du projet Claude
│   ├── modele-donnees.md             ← À REMPLIR : vos listes / tables et colonnes
│   └── standards-construction.md     ← À PERSONNALISER : nommage, couleurs, mise en page
├── skills/                           ← les 4 skills (sources modifiables)
│   ├── pa-design-brief/SKILL.md
│   ├── pa-mockup/SKILL.md (+ exemple-maquette.html)
│   ├── pa-build-mcp/SKILL.md (+ lecons-apprises.md, reference-yaml.md)
│   └── pa-yaml-edit/SKILL.md (+ lecons-apprises.md, reference-yaml.md)
├── dist/                             ← les mêmes skills en .zip, prêts à importer dans claude.ai
├── exemples/                         ← exemple complet « Demandes de congés »
│   ├── modele-donnees-conges.md
│   ├── brief-conges.md
│   └── maquette-conges.html          ← ouvrez-le dans votre navigateur !
└── scripts/
    ├── empaqueter-skills.sh          ← refait les .zip (Mac/Linux)
    └── empaqueter-skills.ps1         ← refait les .zip (Windows)
```

**Pour voir le résultat attendu tout de suite** : double-cliquez sur `exemples/maquette-conges.html`.
Changez de rôle en haut, cochez « Afficher les noms des contrôles », créez une demande, approuvez-la.

## 3. Ce qu'il vous faut (et ce qui est gratuit)

| Élément | Nécessaire pour | Coût |
|---|---|---|
| Compte **claude.ai** | Projet, brief, maquette, méthode YAML | Gratuit ou payant ; les Projets et Skills dépendent de votre forfait (voir claude.ai → Paramètres) |
| **Power Apps** | Construire l'application | Inclus dans beaucoup de licences Microsoft 365 ; sinon **Power Apps Developer Plan** gratuit (environnement personnel de développement) |
| **Claude Code** | Méthode 1 (MCP) seulement | Nécessite un abonnement Claude payant ou une clé API |
| **.NET 10 SDK** | Méthode 1 (MCP) seulement | Gratuit — https://dotnet.microsoft.com/download/dotnet/10.0 |
| **Node.js** | Installateur Microsoft (optionnel) | Gratuit — https://nodejs.org |

👉 **Chemin le plus simple et gratuit** : projet Claude + skills brief / maquette / YAML.
La méthode MCP est plus automatique mais demande Claude Code.

## 4. Installation

### Étape A — Créer le projet Claude avec vos données (10 min)

1. Remplissez `projet-claude/modele-donnees.md` avec vos vraies sources (noms **internes** des colonnes ;
   l'astuce pour les trouver est dans le fichier). Inspirez-vous de `exemples/modele-donnees-conges.md`.
2. Personnalisez `projet-claude/standards-construction.md` (préfixes, couleurs, format…).
3. Sur **claude.ai** → **Projets** → **Créer un projet** (ex. « Mes Power Apps »).
4. **Instructions du projet** : collez le contenu de `projet-claude/instructions-projet.md`
   (le texte sous la ligne `---`).
5. **Connaissances du projet** : ajoutez `modele-donnees.md` et `standards-construction.md`.

### Étape B — Installer les skills dans claude.ai (5 min)

1. Sur claude.ai → **Paramètres** → **Capacités** (selon la version : **Personnaliser** → **Skills**).
   Activez l'**exécution de code** si demandé (requis pour les skills).
2. **Importer un skill** → choisissez `dist/pa-design-brief.zip`. Répétez pour `pa-mockup.zip`,
   `pa-yaml-edit.zip` (et `pa-build-mcp.zip` si vous voulez aussi l'avoir ici).
3. Vérifiez que les 4 skills sont **activés**.

> Après avoir modifié un skill (ex. une nouvelle leçon apprise), relancez le script
> `scripts/empaqueter-skills.ps1` (Windows) ou `.sh` (Mac/Linux), puis réimportez le .zip.
> Sans script : clic droit sur le dossier du skill → **Compresser** (le .zip doit contenir le dossier).

### Étape C — (Méthode 1 uniquement) Installer Claude Code + le serveur MCP

1. Installez **Claude Code** : https://code.claude.com (choisissez l'installateur pour votre système).
2. Installez le **.NET 10 SDK** puis vérifiez dans un terminal :

   ```bash
   dotnet --list-sdks
   ```

   Une ligne commençant par `10.` doit apparaître.
3. Installez le serveur MCP **Canvas Authoring**. Option recommandée, le plugin officiel Microsoft —
   dans Claude Code, tapez :

   ```bash
   /plugin marketplace add microsoft/power-platform-skills
   ```

   ```bash
   /plugin install canvas-apps@power-platform-skills
   ```

   Option manuelle (le serveur seul), dans un terminal :

   ```bash
   claude mcp add canvas-authoring -- dnx Microsoft.PowerApps.CanvasAuthoring.McpServer --yes
   ```

4. Copiez les skills du kit dans votre dossier personnel de skills Claude Code :
   - Windows (PowerShell) :

     ```powershell
     Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.claude\skills\"
     ```

   - Mac / Linux :

     ```bash
     mkdir -p ~/.claude/skills && cp -R skills/* ~/.claude/skills/
     ```

   Copiez aussi `projet-claude/modele-donnees.md` et `standards-construction.md` dans le dossier où
   vous lancerez Claude Code (Claude Code n'a pas accès aux connaissances de votre projet claude.ai).
5. Redémarrez Claude Code et tapez `/mcp` : `canvas-authoring` doit apparaître comme connecté.

### Étape D — Préparer Power Apps (pour la méthode MCP)

1. https://make.powerapps.com → **Créer** → **Application vide** → **Application canevas vide** (format tablette).
2. **Enregistrez** l'application une première fois.
3. **Paramètres** → **Mises à jour** → activez **Coédition** (*Coauthoring*).
4. Ajoutez vos sources de données (**Données** → **Ajouter des données** → votre liste SharePoint, etc.).
5. **Gardez cet onglet ouvert** pendant toute la construction et copiez son URL.

## 5. Utilisation pas à pas

### Étape 1 — Le design brief

Dans votre projet Claude, écrivez par exemple :

> Je veux une application pour gérer les demandes de congés de mon équipe. Fais le design brief.

Claude pose des questions par petits groupes, puis livre un brief en 9 sections (exemple :
`exemples/brief-conges.md`). Relisez-le, corrigez, validez. **Ajoutez le brief validé aux connaissances
du projet.**

### Étape 2 — La maquette jouable

> Fais la maquette jouable à partir du brief.

Claude produit une page HTML cliquable (affichée à côté de la conversation). Testez **tout** : chaque
bouton, chaque rôle, les erreurs de saisie. Dites ce qui ne va pas, Claude corrige. Quand c'est bon :

> La maquette est validée, produis la spécification de construction.

Ajoutez la spécification (`spec-<app>.md`) aux connaissances du projet.

### Étape 3a — Construire avec MCP (Claude Code)

Dans un terminal, placez-vous dans le dossier contenant le brief, la spec, le modèle de données et les
standards, lancez `claude`, puis :

> Construis l'application à partir de spec-conges.md avec le skill pa-build-mcp.

Claude vous demande l'URL de Studio, se connecte (une fenêtre de connexion Microsoft peut s'ouvrir :
utilisez **le même compte que Studio**), vérifie les sources de données, puis construit écran par
écran. Les changements apparaissent **en direct** dans votre onglet Studio. À la fin : testez (F5),
puis **Enregistrez et Publiez** vous-même.

### Étape 3b — Construire / modifier avec YAML (partout, gratuit)

1. Dans Studio, clic droit sur un écran existant → **Afficher le code** → **Copier le code**.
   (Pour une app neuve, ajoutez d'abord un conteneur, un bouton, une étiquette et une galerie : Claude
   apprendra les noms exacts des types de contrôles de votre environnement.)
2. Dans le projet Claude :

   > Voici le code d'un écran de mon app. Génère scrAccueil selon la spec. [collez le code]

3. Copiez le bloc ```yaml``` renvoyé. Dans Studio, clic droit dans l'arborescence → **Coller** →
   **Coller le code** (ou `Ctrl+V`).
4. Faites les réglages listés dans « À vérifier après collage » (ex. `App.Formulas`, sources de données).
5. Recommencez écran par écran.

## 6. Corriger les bugs et enseigner aux skills

C'est le cœur de la méthode : **chaque erreur corrigée une fois ne doit plus revenir.**

1. Décrivez le bug à Claude avec le **message d'erreur exact** et le code du contrôle (Afficher le code).
2. Claude corrige, vous retestez.
3. Claude propose une **leçon apprise** (Symptôme / Cause / Règle / Exemple).
   - Erreur technique → ajoutez-la à `skills/pa-build-mcp/lecons-apprises.md` **et**
     `skills/pa-yaml-edit/lecons-apprises.md`.
   - Préférence personnelle (style, nommage) → ajoutez-la à `standards-construction.md` (section 7),
     puis remplacez le fichier dans les connaissances du projet.
4. Mettez à jour le skill : dans Claude Code, Claude modifie directement le fichier
   (`~/.claude/skills/...`) ; sur claude.ai, refaites le .zip et réimportez le skill.

Les leçons de départ (Screen1 vide, `: ` dans les textes français, colonnes Choix `.Value`…) sont déjà
incluses.

## 7. YAML ou MCP : laquelle choisir ?

| | Méthode 1 — MCP | Méthode 2 — YAML |
|---|---|---|
| Outil | Claude Code + .NET 10 | claude.ai (n'importe quel forfait avec projets) |
| Installation | 15-20 min | aucune |
| Vitesse | Très rapide : l'app entière se construit seule | Écran par écran, copier-coller |
| Vérification | Claude compile et corrige lui-même | Vous voyez les erreurs au collage |
| Idéal pour | Nouvelles applications complètes | Retouches, ajouts d'écrans, apps existantes |
| Coût | Abonnement Claude payant | Gratuit possible |

**Conseil** : utilisez MCP pour la première version, puis YAML pour les petites retouches.

### Conseils pour de meilleurs résultats

- **Le modèle de données d'abord** : 90 % des formules ratées viennent d'un nom de colonne inventé.
- **Ne sautez pas la maquette** : c'est là que vous découvrez ce que vous voulez vraiment.
- **Petits pas** : un écran à la fois, testé avant de passer au suivant.
- **Faites grandir vos skills** : quelques minutes pour noter une leçon en font gagner des heures.

## 8. Dépannage

| Problème | Solution |
|---|---|
| Claude invente des colonnes | Vérifiez que `modele-donnees.md` est dans les connaissances du projet et contient les noms **internes** |
| Le skill ne se déclenche pas | Nommez-le : « utilise le skill pa-mockup » ; vérifiez qu'il est activé dans les paramètres |
| L'import du .zip échoue | Le .zip doit contenir le **dossier** du skill avec `SKILL.md` dedans ; utilisez le script d'empaquetage |
| `canvas-authoring` absent de `/mcp` | `dotnet --list-sdks` doit montrer 10.x ; redémarrez Claude Code |
| Erreur 404 à la connexion MCP | Connectez-vous avec le **même compte** que Studio ; l'onglet Studio doit rester ouvert ; coédition activée |
| Les changements n'apparaissent pas dans Studio | Onglet Studio fermé ou coédition désactivée : rouvrez l'app, demandez à Claude de se reconnecter |
| `YamlInvalidSyntax ... invalid mapping` au collage | Un texte contient « : » sans apostrophes (voir `reference-yaml.md`) |
| Formules avec `,` alors que Studio affiche `;` | Normal : le code source utilise la syntaxe invariante, Studio la convertit en français |

## Références

- Plugin officiel Microsoft (serveur MCP et skills canvas-apps) : https://github.com/microsoft/power-platform-skills
- Vidéo : https://youtu.be/vOWSya1Pb9k
