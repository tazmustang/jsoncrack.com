---
name: pa-design-brief
description: Étape 1 de la construction d'une Power App Canvas. Interroge l'utilisateur par petits groupes de questions puis produit un design brief complet (objectif, rôles, données exactes, écrans, parcours, règles, design). Utiliser quand l'utilisateur veut créer ou refaire une Power App, une application Canvas, ou dit « design brief », « nouvelle app », « j'ai une idée d'application ».
---

# Design brief Power Apps (étape 1)

Objectif : transformer une idée floue en un **brief précis** que les étapes suivantes (maquette,
construction) pourront suivre sans deviner. Aucune formule Power Fx à cette étape.

## Avant de commencer

1. Cherche dans les connaissances du projet : `modele-donnees.md` et `standards-construction.md`.
   - S'ils existent, utilise-les : ne repose pas de questions dont la réponse y figure.
   - S'il n'y a pas de modèle de données, demande à l'utilisateur de décrire ses sources (nom exact,
     colonnes, types) ou de remplir le modèle `modele-donnees.md`.
2. Si l'utilisateur fournit déjà une description détaillée, extrais-en le maximum avant de poser des
   questions.

## Entrevue (3 à 5 questions par tour, jamais plus)

Avance dans cet ordre et arrête-toi dès que l'information suffit :

1. **Le problème** : quel processus l'application remplace-t-elle (courriel, Excel, papier) ? Qu'est-ce
   qui fait mal aujourd'hui ? À quoi ressemble le succès ?
2. **Les utilisateurs** : qui l'utilise, combien, sur quel appareil (PC, tablette, téléphone, terrain) ?
   Quels rôles avec quels droits ?
3. **Les données** : quelles sources (doivent exister dans `modele-donnees.md`) ? Faut-il en créer ?
   Volumes ? Qui peut voir quoi ?
4. **Les parcours** : décris l'action principale du début à la fin (« je crée une demande, puis… »).
   Quelles actions secondaires ?
5. **Les règles** : validations, champs obligatoires, calculs, changements de statut, notifications.
6. **Le périmètre** : ce qui est explicitement hors périmètre pour la version 1.

Propose des réponses par défaut raisonnables entre parenthèses pour accélérer
(ex. « Format tablette ? (par défaut : oui, 1366 × 768) »).

## Livrable : le design brief

Quand tu as assez d'informations, produis le brief en Markdown avec exactement ces sections, puis
demande : « Valides-tu ce brief ou veux-tu modifier quelque chose ? ». Enregistre-le sous
`brief-<nom-app>.md` (en artifact/document sur claude.ai, en fichier dans Claude Code).

```markdown
# Design brief — <Nom de l'application>

## 1. Objectif
Une phrase sur le problème résolu + 2-3 critères de succès mesurables.

## 2. Utilisateurs et rôles
| Rôle | Appareil | Droits |

## 3. Sources de données
| Source (nom exact) | Type | Utilisation (lecture / création / modification / suppression) |
Colonnes utilisées par source (noms internes exacts). Problèmes de délégation anticipés.

## 4. Écrans
Pour chaque écran (nommé selon les standards, ex. scrAccueil) :
- **But** : …
- **Contenu** : en-tête, galerie de…, formulaire avec les champs…, boutons…
- **Navigation** : vient de … / mène à …

## 5. Parcours utilisateur
Étapes numérotées du parcours principal, puis des parcours secondaires.

## 6. Règles métier et validations
Liste numérotée (R1, R2…) : règle, où elle s'applique, message affiché.

## 7. Design
Format, palette (référence aux standards), particularités.

## 8. Hors périmètre (v1)

## 9. Questions ouvertes / hypothèses
Ce que tu as supposé faute de réponse — à confirmer.
```

## Règles

- Utilise **uniquement** des noms de sources et de colonnes connus. Une colonne nouvelle est marquée
  « À CRÉER » dans la section 3.
- Garde le périmètre petit : propose de reporter en v2 tout ce qui n'est pas indispensable.
- Respecte les conventions de nommage de `standards-construction.md` pour les écrans.
- Une fois le brief validé, suggère l'étape suivante : « On passe à la maquette jouable
  (skill pa-mockup) ? ».
