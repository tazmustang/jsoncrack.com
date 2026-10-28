---
title: "Appréciation de la contribution — Guide de tests pour l'équipe"
subtitle: "VERSION FINALE — 28 octobre 2026 · Durée : 30 à 45 minutes"
lang: fr-CA
---

# 1. Avant de commencer

| ✔ | À vérifier |
|---|---|
| ☐ | Vous avez reçu le courriel « **Annie Audet a partagé « Appréciation de la contribution » avec vous** » (vérifiez aussi le Courrier indésirable). |
| ☐ | Vous utilisez **Edge ou Chrome** sur votre poste de la Ville, connecté(e) avec votre compte de la Ville. |
| ☐ | Vous avez le **GUIDE-UTILISATION.docx** sous la main : il explique chaque écran. |
| ☐ | Vous utilisez **seulement du contenu fictif** (ex. : « Objectif test 1 »). |

**Les règles des tests**

- **Aucune vraie évaluation.** Tout ce que vous inscrivez est fictif.
- **Arrêtez-vous avant « Aviser »**, sauf si Annie vous a jumelé(e) avec une collègue ou un collègue (test 6). Sinon, votre vrai supérieur recevrait un courriel.
- **Notez tout** dans le tableau de la section 4 : erreurs, lenteurs, textes peu clairs, boutons difficiles à trouver.
- Les dossiers de test seront **supprimés** avant la mise en production.

# 2. Ouvrir l'application

1. Ouvrez le courriel de Microsoft Power Apps.
2. Cliquez sur **Ouvrir l'application**.
3. La première fois, une fenêtre peut demander d'**autoriser** les connexions (SharePoint, Office 365). Cliquez sur **Autoriser**.
4. L'écran **Mes dossiers** s'affiche.

> 💡 Ajoutez la page à vos **favoris** pour la retrouver facilement.

**Si un message dit « vous n'avez pas accès » ou « vous n'êtes pas membre » :** faites une capture d'écran et envoyez-la à Annie. Votre accès sera ajouté.

# 3. Les tests, un à un

Cochez chaque test réussi. S'il y a un problème, notez son **numéro** dans le tableau de la section 4.

## Test 1 — L'écran « Mes dossiers »

| ✔ | Étape | Résultat attendu |
|---|---|---|
| ☐ | Regardez l'écran d'accueil. | La liste de vos dossiers s'affiche (elle peut être vide). |
| ☐ | Cliquez sur les filtres **Tous**, **En cours**, **À approuver par moi**, **Complétés**. | La liste change sans erreur. |
| ☐ | Tapez un nom dans **Rechercher un nom**. | La liste se filtre. |

## Test 2 — Créer un nouveau formulaire

| ✔ | Étape | Résultat attendu |
|---|---|---|
| ☐ | Cliquez sur **📝 Nouveau formulaire**. | Le formulaire s'ouvre. « Vous êtes » indique **Personne en appréciation**. |
| ☐ | Choisissez un **type de poste** (cadre avec équipe, cadre sans équipe ou professionnel). | Le bon formulaire s'affiche. |
| ☐ | Vérifiez l'**identification**. | Votre nom et votre poste sont proposés automatiquement. |
| ☐ | Inscrivez un **ID** fictif et cochez un ou plusieurs **types de rencontre**. | Les cases restent cochées. |

## Test 3 — Remplir les sections

| ✔ | Étape | Résultat attendu |
|---|---|---|
| ☐ | **Section A** : écrivez 2 objectifs fictifs. Cliquez sur **+ Ajouter une ligne**. | Une nouvelle ligne apparaît. |
| ☐ | **Section B** : donnez quelques cotes et un exemple. | Les cotes s'enregistrent à l'écran. |
| ☐ | **Section C** : cochez 2 thèmes et écrivez un exemple. | — |
| ☐ | **Section D** et **section F** : écrivez quelques mots. | — |
| ☐ | Cliquez sur **❓ Comment remplir ce formulaire**. | L'aide s'affiche ; le bouton de retour ramène au formulaire. |

## Test 4 — Enregistrer, fermer, revenir

| ✔ | Étape | Résultat attendu |
|---|---|---|
| ☐ | Cliquez sur **☁️ Enregistrer et déposer**. | Un **message vert** confirme l'enregistrement. |
| ☐ | Cliquez sur **📂 Mes dossiers**. | Votre dossier apparaît dans la liste. |
| ☐ | **Fermez** le navigateur, rouvrez l'application, puis **ouvrez** votre dossier. | **Tout** ce que vous aviez inscrit est là : identification, poste, types de rencontre, sections. |
| ☐ | Regardez la **barre d'étapes** en haut. | L'étape « Déposé » a un ✓ et la date. |

## Test 5 — Le PDF

| ✔ | Étape | Résultat attendu |
|---|---|---|
| ☐ | Cliquez sur **🖨️ Aperçu PDF** et attendez (10 à 30 secondes). | Un **message vert** s'affiche. |
| ☐ | Cliquez sur **📄 Ouvrir le PDF**. | Le PDF s'ouvre dans un nouvel onglet et contient vos réponses. |
| ☐ | Refaites **Aperçu PDF** une 2e fois. | Le nouveau PDF **remplace** l'ancien : il n'y a toujours qu'une seule version. |

## Test 6 — Le circuit complet (seulement si Annie vous a jumelé(e))

Annie forme des **paires** : une personne joue la **personne en appréciation**, l'autre le **supérieur(e)**. Faites ce test seulement avec votre paire.

| ✔ | Qui | Étape | Résultat attendu |
|---|---|---|---|
| ☐ | Personne en appréciation | Section G : cliquez sur **Aviser**. | Le supérieur reçoit un courriel « prête pour votre consultation » avec un lien. |
| ☐ | Supérieur(e) | Ouvrez le lien du courriel. | « Vous êtes : Supérieur(e) immédiat(e) ». Le dossier est visible dans **À approuver par moi**. |
| ☐ | Personne en appréciation | Section G : cochez la confirmation, puis **Certifier**. | Votre contenu est **verrouillé**. Le supérieur reçoit « À approuver ». |
| ☐ | Supérieur(e) | Remplissez vos cotes (section B), la section E et l'évaluation globale. Section G : cochez, puis **Approuver**. | La barre d'étapes avance, avec la date. |
| ☐ | Les deux | Suivez la **barre d'étapes** jusqu'à la fin, avec Annie pour les dernières approbations. | À **Complété** : courriel à tous, dossier en **lecture seule**, étape « **Transmis aux RH** » cochée. |

## Test 7 — La confidentialité

| ✔ | Étape | Résultat attendu |
|---|---|---|
| ☐ | Demandez à une collègue ou un collègue **qui n'est pas dans votre dossier** d'ouvrir **Mes dossiers**. | Votre dossier **n'apparaît pas** chez cette personne. |

# 4. Mes observations

Remplissez ce tableau, puis retournez ce document à Annie **d'ici le *[date limite]***.

**Votre nom :** ______________________   **Date des tests :** ______________

| N° du test | Ce que j'ai fait | Ce qui s'est passé (ou ma suggestion) | Capture jointe ? |
|---|---|---|---|
| | | | ☐ Oui |
| | | | ☐ Oui |
| | | | ☐ Oui |
| | | | ☐ Oui |
| | | | ☐ Oui |

**En général :**

- L'application est-elle facile à utiliser ? ☐ Oui  ☐ Assez  ☐ Non
- Qu'est-ce qui vous a le plus plu ? ____________________________________
- Qu'est-ce qui devrait être amélioré ? __________________________________

> 💡 **Faire une capture d'écran :** appuyez sur **Windows + Maj + S**, sélectionnez la zone, puis collez-la (**Ctrl + V**) dans votre courriel.

Merci de votre aide !
