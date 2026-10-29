---
name: pa-build-mcp
description: Méthode 1 de construction d'une Power App Canvas. Construit l'application directement dans Power Apps Studio via le serveur Canvas Authoring MCP de Microsoft (coédition), écran par écran, en suivant la spécification issue de la maquette et les standards de l'utilisateur, puis corrige les bugs et enregistre les leçons apprises. Utiliser dans Claude Code quand l'utilisateur veut « construire avec MCP », « générer l'app dans Studio » ou « construire la spec ».
---

# Construire une Power App avec le MCP Canvas Authoring (méthode 1)

Fonctionne dans **Claude Code** (le MCP tourne en local sur le poste de l'utilisateur).
Outils du serveur `canvas-authoring` : `connect`, `sync_canvas`, `compile_canvas`, `list_controls`,
`describe_control`, `list_data_sources`, `get_data_source_schema`, `list_apis`, `describe_api`,
`search_stock_images`, `check_app`, `check_accessibility`.

**Avant toute chose, lis `lecons-apprises.md` (à côté de ce fichier) et applique chaque leçon.**

## 0. Vérifier les prérequis

1. Les outils `mcp__canvas-authoring__*` sont-ils disponibles ? Sinon :
   - lance `dotnet --list-sdks` : il faut un SDK **10.x** (gratuit : https://dotnet.microsoft.com/download/dotnet/10.0) ;
   - le serveur s'installe soit avec le plugin officiel Microsoft
     (`/plugin marketplace add microsoft/power-platform-skills` puis
     `/plugin install canvas-apps@power-platform-skills`), soit manuellement :
     `claude mcp add canvas-authoring -- dnx Microsoft.PowerApps.CanvasAuthoring.McpServer --yes`
   - redémarre Claude Code ensuite. Renvoie l'utilisateur au guide `README.md` du kit, section Méthode 1.
2. Trouve la spec (`spec-*.md`), le brief, `modele-donnees.md` et `standards-construction.md`. Sans spec,
   propose d'abord `pa-mockup` (ou accepte une spec courte rédigée maintenant avec l'utilisateur).

## 1. Se connecter à la session de coédition

1. Demande l'URL de Studio (barre d'adresse, app ouverte en modification). Rappelle :
   coédition activée (Paramètres → Mises à jour → **Coédition**), et **garder l'onglet ouvert** toute la session.
2. Extrais de l'URL `https://make.powerapps.com/e/<ENV_ID>/canvas/?action=edit&app-id=...` :
   - `environment_id` = segment après `/e/` ;
   - `app_id` = dernier segment de `app-id` décodé (après le dernier `/`) ;
   - `environment_category` = `prod` pour make.powerapps.com.
3. Appelle `connect`. En cas d'erreur 404 : même compte que Studio → réessayer avec
   `force_account_select: true`, puis avec `auth_flow: "browser"`.

## 2. Préparer l'espace de travail

1. Crée un dossier vide dédié (ex. `./app-<nom>`), chemin absolu. Aucun autre fichier dedans.
2. `sync_canvas` vers ce dossier : tu obtiens `App.pa.yaml`, `Screen1.pa.yaml`, `_EditorState.pa.yaml`.
3. Garde brief, spec et notes **en dehors** de ce dossier.

## 3. Vérifier les données AVANT d'écrire

1. `list_data_sources` : chaque source de la spec doit être présente. Sinon, demande à l'utilisateur de
   l'ajouter dans Studio (Données → Ajouter des données), puis recommence.
2. `get_data_source_schema` pour chaque source : compare avec `modele-donnees.md`. Signale tout écart
   (nom interne différent, type Choix vs Texte, Lookup…) et corrige la spec, pas les données.

## 4. Construire écran par écran

Pour chaque écran de la spec, dans l'ordre :

1. `list_controls` (une fois) puis `describe_control` pour **chaque type** de contrôle utilisé :
   ne devine jamais une propriété, un `Variant` ou une valeur d'énumération.
2. Écris le fichier `<NomEcran>.pa.yaml` (le **premier écran remplace `Screen1`** : garde la clé
   `Screen1` ou renomme-la et mets à jour `_EditorState.pa.yaml` et `App.StartScreen`).
3. Commence par `App.pa.yaml` : `Formulas` (couleurs, utilisateur), `StartScreen`.
4. `compile_canvas` après chaque écran. Corrige dans cet ordre : erreurs `YamlInvalidSyntax`
   (utilise ligne/colonne), versions de contrôles, noms inconnus, puis erreurs de formules.
   Regroupe les messages identiques : 50 erreurs ont souvent une seule cause.
5. Une fois compilé, dis à l'utilisateur : « L'écran X est dans Studio, vérifie-le » et passe au suivant.

Règles YAML essentielles (détails dans `reference-yaml.md`) :
chaque valeur commence par `=` ; texte entre guillemets `="Texte"` ; toute valeur contenant `: `
est entourée d'apostrophes ou écrite en bloc `|-` ; les enregistrements `{...}` sont entre apostrophes ;
pas de tabulations ; syntaxe Power Fx invariante (`,` entre arguments, `;` entre instructions).

## 5. Vérifier

1. `check_app` et `check_accessibility` sur l'app appliquée ; corrige ce qui est pertinent.
2. Parcours chaque règle R1, R2… du brief et indique comment elle est couverte.
3. Demande à l'utilisateur de tester dans Studio (Aperçu, F5) en suivant le parcours principal.

## 6. Corriger les bugs ET enseigner au skill

Quand l'utilisateur signale un bug :

1. Reproduis la cause dans le YAML (relis le fichier concerné, pas de réécriture complète d'écran).
2. Corrige, `compile_canvas`, demande de retester.
3. **Apprends** : si l'erreur risque de se reproduire sur une autre app, ajoute une entrée à
   `lecons-apprises.md` (format ci-dessous) **après accord de l'utilisateur**. Si c'est une préférence
   personnelle (style, nommage), propose plutôt de l'ajouter à `standards-construction.md`.

```markdown
### <Titre court de la leçon>
- Symptôme : …
- Cause : …
- Règle : toujours / jamais …
- Exemple correct : `…`
```

## Fin de session

Résume : écrans créés, règles couvertes, points à faire manuellement dans Studio (connexions,
partage, publication — **l'utilisateur doit enregistrer et publier lui-même** : Fichier → Enregistrer
puis Publier), leçons ajoutées.
