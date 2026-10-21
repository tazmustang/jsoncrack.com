# À faire, dans l'ordre — pour tester l'appréciation

Mis à jour le 21 octobre 2026.

## Où on en est

| | État |
|---|---|
| Application v3.8 (3 formulaires, rôles, mode SharePoint) | ✅ Prête et testée de mon côté |
| Guides (installation, utilisation, flux) | ✅ Prêts |
| Liste Depot_Appreciations | ✅ Créée — il manque la colonne « Contenu » |
| Bibliothèque Dossiers_Appreciations | ⬜ À créer |
| Flux « AC - Traiter un dépôt » | ⬜ À construire : **sans lui, on peut tester le formulaire, mais pas le cheminement** (courriels, certification, approbations) |
| Déploiement réel | ⬜ Plus tard, après le pilote (phase 2 avec le TI) |

## Étape A — Tester le formulaire (30 minutes, aujourd'hui)

| # | Tâche | Aide | État |
|---|---|---|---|
| A1 | Ajouter la colonne **Contenu** (Plusieurs lignes de texte, **sans** texte enrichi) à Depot_Appreciations | Guide d'installation, section 2 | ⬜ |
| A2 | Créer la bibliothèque **Dossiers_Appreciations** et ses 6 colonnes | Guide d'installation, section 3 | ⬜ |
| A3 | Déposer `appreciation-cadres-v3.8.html` ; supprimer les v3.3 à v3.7 | Guide d'installation, section 4 | ⬜ |
| A4 | Faire les tests **sur le poste** (1 à 13) et **dans SharePoint** (S1 à S7) | Guide d'installation, section 5 | ⬜ |
| A5 | M'envoyer les ✅ / ❌, avec des captures de ce qui ne fonctionne pas | — | ⬜ |

## Étape B — Tester le cheminement complet (une demi-journée, puis 1 heure)

| # | Tâche | Aide | État |
|---|---|---|---|
| B1 | Construire le flux **AC - Traiter un dépôt**, avec `modeTest` = true | **5-GUIDE-FLUX-DEPOT**, sections 1 à 8 | ⬜ |
| B2 | Jouer les 4 rôles seule, avec des données fictives (tests 1 à 9) | 5-GUIDE-FLUX-DEPOT, section 9 | ⬜ |
| B3 | M'envoyer l'historique d'exécution du flux si une étape devient rouge | — | ⬜ |
| B4 | Pilote avec 2 ou 3 vraies personnes (`modeTest` = false, données fictives) | 5-GUIDE-FLUX-DEPOT, section 9 | ⬜ |
| B5 | Remettre le Guide d'utilisation aux personnes du pilote | 2-GUIDE-UTILISATION | ⬜ |

## Étape C — Avant le déploiement réel (avec le TI)

Site dédié, compte de service, permissions par dossier, approbation finale avec PDF et archives, journal, tests exigés par l'EFVP (5-GUIDE-FLUX-DEPOT, section 10).

**Décisions déjà prises :**
- ordre des postures selon le PBRI (Responsable, puis Innovant) ;
- question de la section C du cadre sans équipe : celle du Word du 15 octobre ;
- virgule gardée dans « suivantes, donnez » ;
- seule la personne en appréciation choisit le type de poste.
