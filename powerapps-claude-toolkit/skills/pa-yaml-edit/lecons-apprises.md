# Leçons apprises — construction Power Apps

> Ce fichier grandit à chaque bug corrigé. Claude le lit avant chaque construction.
> Les premières leçons viennent de la documentation Microsoft du serveur Canvas Authoring MCP.

### Ne jamais laisser Screen1 vide
- Symptôme : l'application publiée affiche un écran vide en premier dans la liste.
- Cause : les écrans ont été créés dans de nouveaux fichiers sans réutiliser `Screen1`.
- Règle : toujours écrire le premier écran dans `Screen1.pa.yaml` (ou le renommer) et vérifier
  `_EditorState.pa.yaml` + `App.StartScreen`.

### Les valeurs contenant « : » cassent le YAML
- Symptôme : `YamlInvalidSyntax ... found invalid mapping`, sans nom de contrôle.
- Cause : `Text: ="Statut : " & ThisItem.Statut.Value` n'est pas entouré d'apostrophes.
  (Attention : en français on écrit souvent « Statut : » avec un espace avant les deux-points !)
- Règle : entourer d'apostrophes toute valeur contenant `: `, ou utiliser un bloc `|-`.
- Exemple correct : `Text: '="Statut : " & ThisItem.Statut.Value'`

### Les enregistrements Power Fx doivent être entre apostrophes
- Symptôme : erreur de syntaxe sur `Default: ={Value: "Brouillon"}`.
- Règle : `Default: '={Value: "Brouillon"}'`

### Un GroupContainer n'est pas cliquable
- Symptôme : rien ne se passe quand on clique sur une « carte ».
- Cause : `GroupContainer` n'a pas de propriété `OnSelect`.
- Règle : utiliser `ModernCard`, ou superposer un bouton/rectangle transparent qui porte `OnSelect`.

### Pas de Navigate dans OnStart
- Règle : définir `App.StartScreen` au lieu d'appeler `Navigate` dans `App.OnStart` ou dans
  `OnVisible` de l'écran de départ.

### Les colonnes Choix SharePoint renvoient un enregistrement
- Symptôme : `ThisItem.Statut` affiche une erreur ou rien dans une étiquette.
- Règle : afficher `ThisItem.Statut.Value` ; comparer avec `Statut.Value = "Approuvé"` ; enregistrer avec
  `Statut: {Value: "Approuvé"}` dans `Patch`.

<!-- Ajoutez vos nouvelles leçons sous cette ligne -->
