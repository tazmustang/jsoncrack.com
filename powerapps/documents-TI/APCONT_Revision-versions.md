---
title: "APCONT — Détail de révision des versions"
subtitle: "Application « Appréciation de la contribution » · Solution-ApplicationAppreciation"
lang: fr-CA
---

# Comment tenir ce document

À **chaque** nouvelle version exportée :

1. Ajoutez une ligne au tableau 1 et une section au tableau 2.
2. Mettez aussi à jour le numéro affiché dans l'écran **À propos** (lblVersion).

Les numéros de version sont ceux de la solution Power Platform : **majeure.mineure.build.révision**.

# 1. Historique des versions

| Version | Date | Environnement(s) | Type | Résumé | Par |
|---|---|---|---|---|---|
| 1.0.0.0 | 26 octobre 2026 | Bac à sable | Création | Première version complète : application, 2 flux, listes, variables | Annie Audet |
| 1.0.0.1 | 28 octobre 2026 | Bac à sable | Version finale initiale | Flux PDF (flux 3), PDF joint au dossier, écran allégé, corrections des tests | Annie Audet |
| 1.0.0.2 | 29 octobre 2026 | Bac à sable | Correction | Type de rencontre conservé et affiché dans le PDF | Annie Audet |
| 1.0.0.3 | 30 octobre 2026 | Bac à sable | Modification | Échelle des postures de leadership à 4 niveaux, avec la note 1 | Annie Audet |
| **1.0.0.4** | *[date d'export]* | **PréProd** (puis Prod) | Conformité aux exigences des TI | Noms APCONT, groupes d'application, validation, confirmation, gestion des erreurs, À propos, Aide | Annie Audet |

# 2. Détail des changements

## 1.0.0.4 — Conformité aux exigences des TI

- Variables d'environnement renommées selon la convention (APCONT_…) ; nouvelle variable **APCONT_CourrielSoutien** ; bascule « Exporter la valeur » à **Non** pour les 6 variables.
- Listes PréProd et Prod nommées **APCONT_Appreciations** et **APCONT_Parametres**.
- Flux 1 : retire le groupe local **APCONT_Utilisateurs** (au lieu des Membres du site) de chaque nouveau dossier.
- Flux 1, 2 et 3 : gestion des erreurs (étendue Essayer + courriel au soutien).
- Application :
  - commentaires et mise en forme des formules ;
  - validation des champs obligatoires ;
  - confirmation avant la création d'un dossier ;
  - App.OnError ;
  - écran **À propos** (soutien, téléphone, formulaire de courriel) ;
  - écran d'**aide** (didacticiel).
- Liste Parametres : nouvelles clés SupportNom et SupportTelephone.

## 1.0.0.3 — Échelle des postures

- colEchelle à 4 niveaux : Insatisfaisant, Partiellement satisfaisant, Complètement satisfaisant, Supérieur ; descriptions mises à jour.
- Le tableau de l'échelle (echelleLegend) est généré à partir de colEchelle et affiche la note 1.
- Textes de la section B mis à jour.

## 1.0.0.2 — Type de rencontre

- Comparaison des choix par mot-clé (cases à cocher et enregistrement).
- Relecture complète du dossier à l'ouverture du formulaire.

## 1.0.0.1 — Version finale initiale

- Flux 3 GenererPDFAppreciation : PDF joint au dossier, une seule version.
- Bouton « Ouvrir le PDF » ; onglets Synthèse et Plan retirés ; « Transmis aux RH » ; dates sans fr-CA.
- 26 corrections au guide d'origine (voir le guide de mise en production, partie 3).

# 3. Approbations de mise en production

| Version | PréProd — date et approbateur | Prod — date et approbateur |
|---|---|---|
| 1.0.0.4 | | |
| | | |
