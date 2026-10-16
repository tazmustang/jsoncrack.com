# Version 3.2 — formulaire « cadre avec équipe » du 15 octobre 2026

Fichier : `appreciation-cadres-v3.2.html` (remplace `appreciation-cadres_-v3.1.html`).
Gratuit, rien à installer : il s'ouvre par double-clic dans Edge, comme avant.

---

## 1. Ce qui change à l'écran

| Où | Avant (28 septembre 2026) | Maintenant (15 octobre 2026) |
|---|---|---|
| Haut du formulaire | Pas d'introduction | Nouvelle carte **Introduction** : les 3 buts de l'appréciation et les 3 étapes |
| Type de rencontre | « Rencontre statutaire ou bilan de mi-année » en premier | Nouvel ordre : Période d'essai ou progression salariale · Première rencontre annuelle · **Bilan de mi-année** · Bilan annuel · **Autre (ex. : statutaire)** |
| Section A, Q1 | « Indicateur de mesure » · « Actions réalisées / Commentaires » | « **Indicateurs** de mesure » · « Actions réalisées / commentaires » |
| Section C (avec équipe) | « …thèmes pour lesquels des efforts ont été investis… » | « …thèmes **ayant fait l'objet d'actions ou d'efforts particuliers**…, soit à titre individuel ou auprès de son équipe » |
| Section C, colonnes | « Exemple d'application… » | « **Exemples** d'application à titre individuel » et « **Exemples** d'application auprès de l'équipe » |
| Section D | « Quelle est la résultante des actions… » | « **Quels ont été les résultats ou les impacts** des actions… » |
| Section E | « …et l'atteinte des attentes de l'organisation » | « …et **les attentes de l'organisation** » |
| Section F | « …Exemple : les défis à venir, les besoins de soutien… » | L'exemple est **retiré** |
| Échelle des postures | « de façon constance » (coquille) | « de façon **constante** » |
| Carte de choix, en-tête, pied de page, PDF | Version du 28 septembre 2026 | **Version du 15 octobre 2026** |

Rien d'autre ne change : mot de passe, brouillon chiffré, dépôt SharePoint, approbations, aperçu PDF et correctifs v3.1 sont identiques.

> **À savoir :** les sections A (Q2), D, E et F et le type de rencontre sont communs aux trois formulaires. Ces nouveaux libellés s'affichent donc aussi pour le cadre sans équipe et le professionnel. Leurs changements propres (postures, compétences, section C) et leur nouvelle date de version viendront à la prochaine étape.

## 2. Les dossiers déjà commencés

- Un **brouillon** (fichier `.json` ou copie locale) s'ouvre sans perte et passe automatiquement à la version du 15 octobre 2026.
- Un dossier **déjà certifié ou en approbation** garde sa version d'origine (28 septembre 2026), puisque son contenu a été figé à cette date.
- Une case cochée « Rencontre statutaire ou bilan de mi-année » devient « **Bilan de mi-année** ». Si c'était une rencontre statutaire, décochez-la et cochez « Autre (ex. : statutaire) ».
- Le circuit SharePoint (fichier de dépôt, Power Automate) **n'a pas à être modifié** : les noms des champs du fichier `.json` sont les mêmes.

## 3. Installation (5 minutes)

1. Téléchargez `appreciation-cadres-v3.2.html`.
2. Ouvrez-le dans Edge (double-clic) et vérifiez :
   - la carte « Cadre avec équipe » affiche **Version du 15 octobre 2026** ;
   - la carte **Introduction** apparaît en haut du formulaire ;
   - le type de rencontre suit le nouvel ordre.
3. Si les adresses SharePoint étaient inscrites dans votre ancien fichier (⚙️ Configuration), elles sont gardées par le navigateur. Sinon, inscrivez-les de nouveau dans ⚙️ Configuration.
4. Remplacez l'ancien fichier (v3.1) là où les gens le récupèrent (OneDrive ou bibliothèque SharePoint). Gardez une copie de la v3.1 au cas où.
5. Prévenez les utilisateurs : ils peuvent continuer leurs brouillons avec « 📁 Charger un dossier ».

## 4. Test rapide (10 minutes)

| # | Action | Résultat attendu | ✅ / ❌ |
|---|---|---|---|
| 1 | Ouvrir le fichier, créer ou entrer le mot de passe | L'application s'ouvre | |
| 2 | Choisir « Cadre avec équipe » | En-tête : « Personnel cadre avec équipe · Version du 15 octobre 2026 » | |
| 3 | Cocher « Bilan de mi-année » et « Autre », écrire « statutaire » | Les cases restent cochées | |
| 4 | Section A : remplir « Indicateurs de mesure » | Le texte reste en place | |
| 5 | Section C : cocher un thème | Colonnes « Exemples d'application à titre individuel » et « … auprès de l'équipe » | |
| 6 | « 🖨️ Aperçu PDF » | Type de rencontre : « Bilan de mi-année, Autre : statutaire » ; nouveaux libellés | |
| 7 | « 📁 Charger un dossier » avec un ancien brouillon `.json` | Les données reviennent ; version du 15 octobre 2026 | |

Ce test a été fait en navigateur automatisé le 16 octobre 2026 (étapes 1 à 7) : aucune erreur.

## 5. Points à valider avec les RH

1. **Ordre des postures.** Le formulaire Word présente Performant, Bienveillant, **Innovant, Responsable**. L'application affiche Performant, Bienveillant, **Responsable, Innovant** (ordre retenu dans une version antérieure). Faut-il suivre le Word ?
2. **Coquilles dans les documents Word** : « constance » (corrigé dans l'application) ; la numérotation des questions repart à 1 à la section C du formulaire avec équipe ; « Autre (ex. : statutaire) » est écrit de trois façons dans les trois formulaires.
