---
title: "Appréciation de la contribution — Prochaines étapes"
subtitle: "VERSION FINALE — 28 octobre 2026 · De la version finale au lancement"
lang: fr-CA
---

# Vue d'ensemble

| Étape | Quoi | Qui | Durée estimée |
|---|---|---|---|
| 1 | Démonstration à l'équipe en partage d'écran Teams | Annie + équipe | 1 rencontre |
| 2 | Présentation aux gestionnaires | Annie | 1 rencontre |
| 3 | Demande PréProd aux TI, **avec la liste des testeurs** | Annie | Selon les TI |
| 4 | Exigences avant la production | Annie + partenaires | En parallèle de l'étape 3 |
| 5 | Tests de l'équipe **en PréProd**, puis corrections | Annie + équipe | 1 à 2 semaines |
| 6 | Mise en production | TI (avec Annie) | Selon les TI |
| 7 | Lancement auprès des employés | Annie | 1 journée + suivi |
| 8 | Suivi après le lancement | Annie | Premier cycle d'appréciations |

> **Pourquoi cet ordre ?** Vos collègues ne peuvent pas ouvrir l'application dans votre environnement actuel : ils ne sont pas membres de son groupe de sécurité, et seuls les TI peuvent les y ajouter. Plutôt que de faire deux demandes, la demande PréProd inclut la liste des testeurs. Les tests de l'équipe se font donc en PréProd, ce qui est aussi plus fiable. D'ici là, faites une démonstration en partage d'écran Teams.

Cochez ☐ chaque action terminée.

# Tests par l'équipe (étapes 1 et 5)

Étape 1 : démonstration Teams (vous manipulez, l'équipe commente). Étape 5 : les actions ci-dessous, une fois l'accès PréProd obtenu, avec le lien PréProd.


| ✔ | Action | Fichier utile |
|---|---|---|
| ☐ | Remplacer *[lien de l'application]* et *[date limite]* dans le courriel et le guide de tests | tests-equipe/ |
| ☐ | Former les **paires** pour le test 6 (circuit complet), ou dire à l'équipe de le sauter | GUIDE-TESTS-EQUIPE.docx |
| ☐ | Vérifier que chaque testeur peut ouvrir l'application PréProd (sinon : message « not a member of the environment's security group » → écrire aux TI) | — |
| ☐ | Envoyer le courriel, avec le guide de tests et le guide d'utilisation en pièces jointes | COURRIEL-EQUIPE-TESTS.docx |
| ☐ | Recueillir les tableaux d'observations | — |

# Corrections après les tests (étape 5)

| ✔ | Action |
|---|---|
| ☐ | Classer les observations : **à corriger avant le lancement** / **amélioration plus tard** |
| ☐ | Faire les corrections, puis refaire les tests touchés |
| ☐ | **Supprimer les dossiers de test** dans la liste SharePoint *Appreciations* (et leurs PDF joints) |
| ☐ | Exporter de nouveau la solution *Solution-ApplicationAppreciation* si l'application a changé |

# Étape 2 — Présentation aux gestionnaires

| ✔ | Action | Fichier utile |
|---|---|---|
| ☐ | Ajouter à la présentation les résultats des tests de l'équipe (1 phrase suffit) | Presentation-Appreciation-contribution.pptx |
| ☐ | Présenter et faire une courte démonstration de l'application | Schemas-operationnels-et-avantages.pdf |
| ☐ | Obtenir l'**accord** pour demander le déploiement, et le noter (courriel de confirmation) | — |

# Étape 3 — Demande PréProd aux TI

| ✔ | Action | Fichier utile |
|---|---|---|
| ☐ | Remplir le formulaire des TI avec les réponses déjà préparées | DOSSIER-AUTORISATION-TI.docx |
| ☐ | Dans « Commentaires », inscrire les **noms des testeurs** à ajouter au groupe de sécurité PréProd | DOSSIER-AUTORISATION-TI.docx |
| ☐ | Joindre le guide de mise en production et le fichier Excel | GUIDE-MISE-EN-PRODUCTION.docx, Variables-environnement-et-deploiement.xlsx |
| ☐ | Joindre le **schéma de la solution** | Schema-solution.jpg |
| ☐ | Joindre l'export de la solution (.zip de Power Apps) | — |
| ☐ | Faire un suivi si aucune réponse après 2 semaines | — |

# Étape 4 — Exigences avant la production

Ces points sont souvent demandés par les TI. Commencez-les **en même temps** que l'étape 3.

| ✔ | Action | Avec qui |
|---|---|---|
| ☐ | **EFVP** (évaluation des facteurs relatifs à la vie privée) : l'application contient des renseignements personnels | Responsable de la protection des renseignements personnels |
| ☐ | **Durée de conservation** des dossiers et de leurs PDF (calendrier de conservation) | Gestion documentaire |
| ☐ | **Compte de service** pour les 3 flux, au lieu de votre compte personnel | TI |
| ☐ | **Personne suppléante** copropriétaire de l'application et des flux | Votre gestionnaire |
| ☐ | **Groupe de sécurité** pour tous les employés concernés | TI |

# Étape 6 — Mise en production par les TI

Ce que les TI feront, guidés par GUIDE-MISE-EN-PRODUCTION.docx. Votre rôle : répondre aux questions et **tester**.

| ✔ | Action | Qui |
|---|---|---|
| ☐ | Créer le site SharePoint et les listes *Appreciations* et *Parametres* (avec les permissions) | TI |
| ☐ | Importer la solution en **PréProd**, remplir les 5 variables d'environnement | TI |
| ☐ | Créer les connexions avec le compte de service et activer les 3 flux | TI |
| ☐ | Refaire les **15 tests** du guide en PréProd | Annie |
| ☐ | Importer en **Prod**, partager l'application avec le groupe de sécurité | TI |
| ☐ | Faire un dernier test rapide en Prod (créer, enregistrer, PDF), puis supprimer le dossier test | Annie |
| ☐ | Noter le **lien Prod** de l'application | Annie |

# Étape 7 — Lancement

| ✔ | Action | Fichier utile |
|---|---|---|
| ☐ | Remplacer *[lien de l'application]* et *[adresse de soutien]* dans le guide d'utilisation et le message | GUIDE-UTILISATION.docx, MESSAGE-ANNONCE.docx |
| ☐ | Enregistrer le guide d'utilisation en PDF (Word › Enregistrer sous › PDF) | — |
| ☐ | Envoyer l'annonce aux employés et gestionnaires | MESSAGE-ANNONCE.docx (version courriel) |
| ☐ | Publier sur Teams ou l'intranet | MESSAGE-ANNONCE.docx (version Teams) |
| ☐ | Envoyer le rappel aux gestionnaires | MESSAGE-ANNONCE.docx (version rappel) |

# Étape 8 — Suivi après le lancement

| ✔ | Action |
|---|---|
| ☐ | Les 2 premières semaines : vérifier chaque jour l'**historique des 3 flux** (Power Automate › Mes flux › Historique des exécutions) |
| ☐ | Tenir une liste des questions reçues, et compléter la FAQ du guide d'utilisation |
| ☐ | Faire un **bilan** à la fin du premier cycle d'appréciations (satisfaction, délais, problèmes) |
| ☐ | Améliorations possibles plus tard : bouton « 📄 PDF » dans Mes dossiers, tableau de suivi pour les RH |
| ☐ | Chaque année : mettre à jour la liste *Parametres* et appliquer la durée de conservation |
