---
title: "Guide — PDF de l'appréciation complète"
subtitle: "Application Power Apps « Appréciation de la contribution » — 27 octobre 2026"
lang: fr-CA
---

# Ce que vous allez obtenir

Le bouton **🖨️ Aperçu PDF** produira un **vrai PDF de plusieurs pages** avec toute l'appréciation :

- identification et participants ;
- sections A à F ;
- évaluation globale ;
- tableau des avis, de la certification et des approbations.

Le PDF peut être produit **à toute étape** : il affiche le statut du moment (Brouillon, Certifié, etc.).

**Comment ça marche :**

1. L'application assemble l'appréciation sous forme de page web (HTML).
2. Un petit flux Power Automate, **GenererPDFAppreciation**, crée un fichier temporaire dans OneDrive.
3. Le flux le convertit en PDF avec l'action **« Convertir un fichier »**.
4. Il dépose le PDF dans la bibliothèque SharePoint **Appreciations_PDF**, donne à la personne qui l'a demandé le droit de le lire, puis supprime le fichier temporaire.
5. L'application ouvre le PDF dans un nouvel onglet.

**Coût :** connecteurs **standard** uniquement (SharePoint, OneDrive Entreprise, Power Apps). Aucune licence Premium.

**Fichiers fournis :**

| Fichier | Contenu |
|---|---|
| `btnApercuPDF-OnSelect.txt` | La formule complète du bouton, prête à coller |
| `generer-formule-pdf.py` | Le programme qui a produit la formule (pour la modifier plus tard) |
| `GUIDE-PDF-APPRECIATION.docx` | Ce guide |

Ordre des étapes : **1 → 2 → 3 → 4**. L'application ne peut appeler le flux que s'il existe déjà.

# Étape 1 — Créer la bibliothèque Appreciations_PDF (5 minutes)

1. Dans le site SharePoint, cliquez sur **+ Nouveau › Bibliothèque de documents**. Nom : `Appreciations_PDF` (sans accent ni espace). Cliquez sur **Créer**.
2. Cliquez sur **⚙️ › Paramètres de la bibliothèque › Autorisations pour cette bibliothèque**.
3. Cliquez sur **Arrêter l'héritage des autorisations** et confirmez.
4. Ne gardez que :
   - **Propriétaires du site** : Contrôle total ;
   - **RH – Appréciations** : Lecture (si ce groupe existe déjà).
5. **Retirez** les **Membres du site** et les **Visiteurs du site** : cochez-les, puis cliquez sur **Supprimer les autorisations utilisateur**.

> **Pourquoi ?** Un PDF d'appréciation est confidentiel. Personne ne voit les PDF des autres. Le flux donne à chaque personne l'accès **à son PDF seulement**, au moment où elle le demande.

**À noter pour les TI :** cette bibliothèque doit aussi exister sur les sites de pré-prod et de prod, avec les mêmes autorisations.

# Étape 2 — Créer le flux GenererPDFAppreciation (20 minutes)

Créez-le **dans la solution**, sinon il ne partira pas avec l'export :

1. Ouvrez la solution **Solution-ApplicationAppreciation**.
2. Cliquez sur **+ Nouveau › Automatisation › Flux de cloud › Instantané**.
3. Nom du flux : `GenererPDFAppreciation` (en un seul mot, sans accent).
4. Déclencheur : **Power Apps (V2)**, aussi appelé « Lorsque Power Apps appelle un flux (V2) ». Cliquez sur **Créer**.

Quand une action demande une connexion, choisissez la **référence de connexion** de la solution :

- SharePoint : **SharePoint Appreciation** ;
- OneDrive Entreprise : créez une nouvelle référence, **OneDrive Appreciations**.

## 2.1 Le déclencheur : 3 entrées

Dans le déclencheur, cliquez 3 fois sur **+ Ajouter une entrée › Texte** :

| N° | Nom de l'entrée (exact) | Rôle |
|---|---|---|
| 1 | `nomFichier` | Nom du PDF, sans « .pdf » |
| 2 | `html` | Le contenu de l'appréciation |
| 3 | `courriel` | La personne qui recevra l'accès au PDF |

L'**ordre** est important : l'application envoie les valeurs dans cet ordre.

## 2.2 Action 1 — Créer le fichier temporaire

- Action : **OneDrive Entreprise › Créer un fichier**
- Chemin d'accès du dossier : `/`
- Nom de fichier : choisissez **nomFichier** dans le contenu dynamique, puis tapez `.html` juste après.
- Contenu du fichier : **html** (contenu dynamique).

## 2.3 Action 2 — Convertir en PDF

- Action : **OneDrive Entreprise › Convertir un fichier**
- Fichier : **Id**, venant de « Créer un fichier » (contenu dynamique).
- Type cible : **PDF**.

## 2.4 Action 3 — Déposer le PDF dans SharePoint

- Action : **SharePoint › Créer un fichier**
- Adresse du site : la variable d'environnement **Site Appréciations**. Dans le bac à sable, c'est votre site SandBoxAnnieAudet.
- Chemin d'accès du dossier : `/Appreciations_PDF`
- Nom de fichier : **nomFichier**, puis tapez `.pdf`.
- Contenu du fichier : **Contenu du fichier**, venant de « Convertir un fichier ».

## 2.5 Action 4 — Donner l'accès à la personne

- Action : **SharePoint › Accorder l'accès à un élément ou à un dossier**
- Adresse du site : la même que l'action 3.
- Nom de la liste ou de la bibliothèque : **Appreciations_PDF**.
- Id : **ItemId**, venant de l'action 3 « Créer un fichier ».
- Destinataires : **courriel** (contenu dynamique du déclencheur).
- Rôles : **Peut afficher**.
- Notifier les destinataires : **Non**.

## 2.6 Action 5 — Obtenir le lien du PDF

- Action : **SharePoint › Obtenir les propriétés du fichier**
- Adresse du site : la même.
- Nom de la bibliothèque : **Appreciations_PDF**.
- Id : **ItemId**, venant de l'action 3.

## 2.7 Action 6 — Supprimer le fichier temporaire

- Action : **OneDrive Entreprise › Supprimer un fichier**
- Fichier : **Id**, venant de l'action 1 « Créer un fichier » (celle de OneDrive, pas celle de SharePoint).

## 2.8 Action 7 — Répondre à l'application

- Action : **Power Apps › Répondre à une application ou à un flux Power Apps** (aussi appelée « Répondre à Power Apps »).
- Cliquez sur **+ Ajouter une sortie › Texte**.
- Nom : `lien` (en minuscules).
- Valeur : **Lien vers l'élément**, venant de « Obtenir les propriétés du fichier ».

Cliquez sur **Enregistrer**. Le **Vérificateur de flux** doit être vide.

# Étape 3 — Brancher le flux et coller la formule (5 minutes)

1. Dans Power Apps Studio, cliquez sur l'icône **Power Automate** du menu de gauche (ou sur **… › Power Automate**), puis sur **+ Ajouter un flux**, et choisissez **GenererPDFAppreciation**.
2. Vérifiez que le flux apparaît sous le nom **GenererPDFAppreciation** dans la liste des flux de l'application.
3. Cliquez sur le bouton **btnApercuPDF**, puis choisissez la propriété **OnSelect**.
4. Ouvrez `btnApercuPDF-OnSelect.txt` dans le Bloc-notes : **Ctrl+A**, **Ctrl+C**.
5. Dans la barre de formule : **Ctrl+A**, **Ctrl+V**. La nouvelle formule remplace `Set(CurrentTabID; 4)`.
6. Cliquez sur **Enregistrer**.

> L'onglet **🎯 Plan de développement** reste disponible avec son propre bouton « Imprimer ce plan ». Seul le bouton de gauche change.

**Si Power Apps souligne `GenererPDFAppreciation` en rouge :** le flux a été ajouté sous un autre nom. Effacez le mot, tapez `Gener` et choisissez le nom proposé dans la liste.

# Étape 4 — Tester

| N° | Action | Résultat attendu | ✅ / ❌ |
|---|---|---|---|
| 1 | Ouvrir un dossier enregistré, puis cliquer sur **Aperçu PDF** | Message « Création du PDF en cours… » | |
| 2 | Attendre de 10 à 30 secondes | Message vert, puis le PDF s'ouvre dans un nouvel onglet | |
| 3 | Lire le PDF | Plusieurs pages : identification, sections A à F, évaluation, approbations | |
| 4 | Ouvrir la bibliothèque Appreciations_PDF | Le fichier `Appreciation_dossier1_…pdf` y est | |
| 5 | Dans OneDrive, regarder le dossier racine | Aucun fichier `.html` qui traîne | |
| 6 | Cliquer sur **Aperçu PDF** sur un formulaire **jamais enregistré** | Message « Enregistrez d'abord le dossier… » | |

**Si ça ne fonctionne pas :**

- **Message rouge « Le PDF n'a pas pu être créé » :**
  1. Ouvrez le flux dans Power Automate, puis **Historique des exécutions 28 jours**.
  2. Cliquez sur l'exécution en échec. L'action en rouge indique où ça bloque.
  3. Envoyez-moi une capture de cette action.
- **Le PDF s'ouvre mais affiche « Accès refusé » :** vérifiez l'action 4 (Destinataires = **courriel**, Rôles = **Peut afficher**).
- **Le PDF est mal mis en page :** tout l'aspect (couleurs, titres, tableaux) est réglé au début de la formule. On peut l'ajuster sans toucher au flux.

# Pour les TI (mise en pré-prod et en prod)

- **Nouveau flux dans la solution :** GenererPDFAppreciation.
- **Nouvelle référence de connexion :** OneDrive Appreciations (OneDrive Entreprise). Elle doit utiliser le **compte de service**. Les fichiers temporaires passent par son OneDrive et sont supprimés aussitôt.
- **Nouvelle bibliothèque :** `Appreciations_PDF` sur chaque site, héritage arrêté, Propriétaires et RH seulement.
- **Ménage conseillé :** une fois par année, archiver ou supprimer les anciens PDF. Ils peuvent toujours être recréés depuis l'application.
