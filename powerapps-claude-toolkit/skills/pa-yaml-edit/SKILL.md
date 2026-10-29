---
name: pa-yaml-edit
description: Méthode 2 de construction d'une Power App Canvas, sans MCP. Génère ou modifie du code source Power Apps (.pa.yaml) que l'utilisateur copie depuis Power Apps Studio (« Afficher le code ») et recolle (« Coller le code »), écran par écran ou contrôle par contrôle, en respectant ses standards. Utiliser quand l'utilisateur colle du YAML Power Apps, demande du « code à coller dans Studio », un écran en YAML, ou travaille sur claude.ai sans Claude Code.
---

# Construire / modifier une Power App en YAML (méthode 2)

Fonctionne **partout** (claude.ai gratuit, Claude Desktop, Claude Code) : aucune installation, Claude
produit du texte que l'utilisateur colle dans Power Apps Studio.

**Avant toute chose, lis `lecons-apprises.md` et `reference-yaml.md` (à côté de ce fichier).**

## Le cycle copier → modifier → coller

1. **Copier depuis Studio** : dans l'arborescence, clic droit (ou `…`) sur un écran ou un contrôle →
   **Afficher le code** (*View code*) → **Copier le code**. L'utilisateur colle ce YAML dans la conversation.
2. **Modifier** : tu renvoies le **bloc complet** modifié, prêt à coller, dans un seul bloc de code
   ```` ```yaml ````. Jamais de « … reste inchangé … » dans le code.
3. **Coller dans Studio** : clic droit sur l'écran/le conteneur cible dans l'arborescence →
   **Coller** → **Coller le code** (*Paste code*), ou `Ctrl+V` dans l'arborescence.
   Pour remplacer un écran : supprimer/renommer l'ancien d'abord pour éviter les doublons de noms.

Si l'utilisateur n'a rien à copier (nouvelle app), demande-lui d'abord de copier le code d'un écran
contenant quelques contrôles (bouton, étiquette, galerie, conteneur) : ça te donne les **noms de types
et versions exacts** de son environnement. Réutilise exactement ces noms (`Control: …`).

## Ce que tu produis

- **Nouvel écran** : un bloc commençant par `Screens:` suivi de l'écran, conforme à la spec
  (`spec-*.md`) et à `standards-construction.md` (nommage, conteneurs AutoLayout, couleurs via
  `fxCouleur…`).
- **Nouveau(x) contrôle(s)** : un bloc commençant par `- nomControle:` (séquence YAML), à coller dans
  le conteneur voulu.
- **Modification** : le bloc entier de l'écran ou du contrôle d'origine, modifié.
- **Ce qui ne se colle pas** : propriétés de l'objet `App` (`Formulas`, `StartScreen`, `OnStart`) et
  connexions de données. Donne-les à part avec l'instruction « Sélectionne **App** dans
  l'arborescence → propriété `Formulas` → colle ceci ».

Après chaque bloc, ajoute une courte liste « À vérifier après collage » (sources de données à
ajouter, noms qui doivent exister, propriétés à contrôler).

## Règles de code (résumé — détails dans reference-yaml.md)

- Chaque valeur de propriété commence par `=` : `Text: ="Bonjour"`, `Width: =320`, `Visible: =true`.
- Valeur contenant `: ` (fréquent en français : « Statut : ») → entourer d'apostrophes ou bloc `|-`.
- Enregistrement Power Fx `{...}` → entre apostrophes : `Default: '={Value: "Brouillon"}'`.
- Formules sur plusieurs lignes → bloc `|-` avec le `=` sur la première ligne de contenu.
- Indentation de 2 espaces, **jamais de tabulation**. `Children:` est une liste (`- nom:`).
- Syntaxe Power Fx **invariante** (anglaise) : `,` entre arguments, `.` décimal, `;` entre
  instructions. Studio en français l'affichera ensuite avec `;` et `;;` : c'est normal.
- Utilise uniquement les colonnes de `modele-donnees.md` ; colonnes Choix → `.Value`.
- Noms de contrôles uniques dans toute l'application (Studio renomme sinon en `btnX_1`).

## Corriger les bugs ET enseigner au skill

Quand l'utilisateur signale une erreur (message de Studio ou comportement) :

1. Demande le message d'erreur exact et le code actuel du contrôle (Afficher le code).
2. Corrige et renvoie le bloc complet.
3. Si l'erreur est généralisable, propose une nouvelle entrée pour `lecons-apprises.md` au format :

```markdown
### <Titre court>
- Symptôme : …
- Cause : …
- Règle : toujours / jamais …
- Exemple correct : `…`
```

Sur claude.ai, l'utilisateur ajoute cette entrée au fichier et réimporte le skill (voir le guide) ;
dans Claude Code, modifie directement le fichier après accord.
