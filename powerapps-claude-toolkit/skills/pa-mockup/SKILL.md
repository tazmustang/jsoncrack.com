---
name: pa-mockup
description: Étape 2 de la construction d'une Power App Canvas. À partir d'un design brief validé, crée une maquette HTML jouable (un seul fichier, cliquable, avec fausses données respectant le vrai modèle de données) qui imite Power Apps, puis une spécification de construction écran par écran. Utiliser quand l'utilisateur demande une maquette, un prototype, un mock-up ou veut « voir » son application avant de la construire.
---

# Maquette jouable Power Apps (étape 2)

Objectif : que l'utilisateur **clique dans son application** avant qu'on la construise. Corriger une
maquette coûte quelques secondes ; corriger une app construite coûte des heures.

## Entrées

- Le design brief validé (`brief-*.md`). S'il n'existe pas, propose d'abord le skill `pa-design-brief`
  (ou un mini-brief de 10 lignes si l'utilisateur est pressé).
- `modele-donnees.md` et `standards-construction.md` des connaissances du projet.

## Livrable 1 : la maquette HTML

Un **seul fichier HTML autonome** (HTML + CSS + JavaScript, aucune bibliothèque externe, aucun appel
réseau) affiché en artifact sur claude.ai ou écrit en fichier `maquette-<nom-app>.html` dans Claude Code.
Le fichier `exemple-maquette.html` (à côté de ce fichier) montre le niveau attendu : inspire-toi de sa structure.

Exigences :

1. **Cadre Power Apps** : zone d'application aux dimensions du format choisi (1366 × 768 tablette ou
   640 × 1136 téléphone), centrée, avec la police Segoe UI et la palette des standards.
2. **Tous les écrans du brief**, avec la navigation réelle (boutons, retour, sélection dans une
   galerie → écran de détail).
3. **Fausses données réalistes** stockées dans des tableaux JavaScript dont les **noms et propriétés
   sont exactement ceux des sources et colonnes** du modèle (ex. `Demandes = [{Title, Statut,
   DateDebut…}]`). 6 à 10 lignes par source, en français, avec des cas limites (texte long, valeur
   vide, statuts variés).
4. **Comportement simulé** : recherche et filtres qui filtrent vraiment, formulaires qui ajoutent ou
   modifient une ligne en mémoire, validations des règles du brief (messages d'erreur), notification
   de succès, état vide des galeries.
5. **Noms des contrôles** : chaque élément porte un attribut `data-pa="galDemandes"` avec le nom prévu
   selon les conventions. Un interrupteur « Afficher les noms des contrôles » en haut de page affiche
   ces noms en surimpression (étiquettes jaunes). C'est ce qui relie la maquette à la construction.
6. **Sélecteur d'écran / de rôle** en haut (hors du cadre) pour tester chaque écran et chaque rôle.
7. Ressembler à Power Apps (contrôles modernes Fluent : boutons arrondis, champs avec bordure,
   en-tête coloré) sans chercher la perfection graphique.

Après la maquette, demande : « Clique partout et dis-moi ce qui ne va pas ». Itère jusqu'à validation.
Chaque retour de l'utilisateur doit aussi être reporté dans le brief (mentionne-le).

## Livrable 2 : la spécification de construction

Une fois la maquette validée, produis `spec-<nom-app>.md`, le plan que suivront `pa-build-mcp` ou
`pa-yaml-edit` :

```markdown
# Spécification de construction — <Nom de l'application>

## App
- StartScreen : scrAccueil
- Formulas (formules nommées) : fxCouleurPrimaire = …; fxUtilisateur = User(); …
- OnStart : (vide si possible)
- Sources de données à connecter dans Studio : Demandes (SharePoint, site …), Office365Users

## scrAccueil
| Contrôle | Type | Parent | Propriétés clés (Power Fx) |
|---|---|---|---|
| conAccueilRoot | GroupContainer / AutoLayout vertical | écran | Width: =Parent.Width … |
| galDemandes | Gallery / Vertical | conAccueilBody | Items: =Sort(Filter(Demandes, …), Created, SortOrder.Descending) |
| btnNouvelle | Bouton | conAccueilHeader | OnSelect: =NewForm(frmDemande); Navigate(scrDetail) |

Règles du brief couvertes : R1, R3.
(une section par écran)

## Points d'attention
Délégation, permissions, éléments que la maquette simplifie (ex. pièces jointes).
```

## Règles

- La maquette ne doit jamais introduire de fonctionnalité absente du brief sans la signaler.
- Les formules de la spec utilisent la syntaxe Power Fx **anglaise / invariante** (virgule `,` entre
  arguments, `;` entre instructions), qui est celle du code source `.pa.yaml`.
- Termine en proposant la méthode de construction : MCP (Claude Code, construction automatique) ou
  YAML (copier-coller dans Studio, fonctionne partout).
