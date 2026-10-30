---
title: "Site « RH Power Apps Données PréProd » — Pas à pas, une étape à la fois"
subtitle: "Application Appréciation de la contribution (SRHVQ) · VERSION FINALE — 30 octobre 2026"
lang: fr-CA
---

# Avant de commencer

**Ce que vous allez faire sur le site :**

1. Préparer un dossier pour la documentation.
2. Créer 2 groupes : un pour les utilisateurs, un pour les RH.
3. Créer 2 listes : les dossiers et les paramètres.
4. Régler les listes : versions, pièces jointes, index.
5. Donner les accès à chaque liste.
6. Transmettre les valeurs aux TI.

**Durée :** environ 1 h 30. Vous pouvez arrêter entre deux étapes.

**Les noms à utiliser** (convention des TI, acronyme **SRHVQ**) :

| Élément | Nom exact |
|---|---|
| Groupe des utilisateurs | **SRHVQ_Utilisateurs** |
| Groupe des RH | **SRHVQ_RH** |
| Liste des dossiers | **SRHVQ_Appreciations** |
| Liste des paramètres | **SRHVQ_Parametres** |

> 💡 Faites un copier-coller des noms pour éviter les fautes. Le flux 1 cherchera le groupe **SRHVQ_Utilisateurs** par son nom exact.

# Étape 1 — Ouvrir le site et vérifier vos droits

1. Ouvrez le site **RH Power Apps Données PréProd** (lien reçu des TI).
2. **Copiez l'adresse** dans la barre du navigateur, **jusqu'au nom du site seulement** (ex. `https://villedequebec.sharepoint.com/sites/RHPowerAppsDonneesPreProd`). Ne gardez pas la fin, comme `/SitePages/Home.aspx`.
3. Collez-la dans l'Excel, onglet **Variables**, colonne **Pré-prod**, ligne du site.
4. Cliquez sur la **roue ⚙️** en haut à droite.

✅ Vous voyez **Autorisations du site** et **Informations sur le site** : vous avez les droits nécessaires.

❌ Vous ne voyez pas **Autorisations du site** : vous n'êtes pas propriétaire du site. Écrivez aux TI (Bruno Gagnon) pour demander les droits de **propriétaire** ou de **contrôle total** sur le site, ou au minimum sur vos listes. Sans ces droits, les étapes 3 à 9 sont impossibles.

# Étape 2 — Un dossier dans « Documents TI »

Le site est partagé entre plusieurs applications. On range donc vos documents dans un dossier à votre nom d'application.

1. Dans le menu de gauche du site, cliquez sur **Documents TI**. S'il n'y est pas : **⚙️ › Contenu du site** et cherchez-le.
2. Si la bibliothèque n'existe pas : **+ Nouveau › Bibliothèque de documents › Bibliothèque vide**, nom **Documents TI**, puis **Créer**.
3. Dans Documents TI : **+ Nouveau › Dossier**, nom **SRHVQ - Appréciation de la contribution**, puis **Créer**.

Vous y déposerez les documents à l'**étape 10**.

# Étape 3 — Créer le groupe SRHVQ_Utilisateurs

1. **⚙️ › Autorisations du site**.
2. En bas du panneau qui s'ouvre : **Paramètres d'autorisations avancés**. Une page classique s'ouvre.
3. Dans le ruban, onglet **Autorisations** : cliquez sur **Créer un groupe**.
4. Remplissez :
   - **Nom :** `SRHVQ_Utilisateurs`
   - **À propos de moi :** `Utilisateurs de l'application Appréciation de la contribution (contient le groupe Entra G-IS-APP de PréProd)`
   - **Propriétaire :** votre nom
   - **Qui peut afficher l'appartenance au groupe ?** Membres du groupe
   - **Qui peut modifier l'appartenance au groupe ?** Propriétaire du groupe
   - **Demandes d'adhésion :** Non
5. Tout en bas, section **Accorder des autorisations au groupe sur ce site** : **ne cochez AUCUNE case**. Le groupe ne doit avoir aucun droit sur le site.
6. Cliquez sur **Créer**. La page du groupe s'ouvre.
7. Cliquez sur **Nouveau › Ajouter des utilisateurs à ce groupe**.
8. Tapez le nom du groupe Entra de PréProd (**G-IS-APP-…**, fourni par les TI) et choisissez-le dans la liste.
9. Cliquez sur **Afficher les options** et **décochez** « Envoyer une invitation par courriel ».
10. **Partager**.

✅ La page du groupe SRHVQ_Utilisateurs contient **une seule ligne** : le groupe G-IS-APP de PréProd.

> En attendant le nom du groupe G-IS-APP : ajoutez vos **testeurs** un par un. Vous les remplacerez par le groupe Entra quand vous l'aurez.

# Étape 4 — Créer le groupe SRHVQ_RH

1. Revenez à **⚙️ › Autorisations du site › Paramètres d'autorisations avancés**.
2. **Créer un groupe** :
   - **Nom :** `SRHVQ_RH`
   - **À propos de moi :** `RH autorisées à consulter tous les dossiers d'appréciation`
   - Mêmes réglages qu'à l'étape 3
   - **Aucune case cochée** en bas
3. **Créer**.
4. **Nouveau › Ajouter des utilisateurs** : ajoutez les personnes des RH autorisées. Décochez l'invitation, puis **Partager**.

✅ Dans **Paramètres d'autorisations avancés**, les groupes SRHVQ_Utilisateurs et SRHVQ_RH **n'apparaissent pas** dans la liste des autorisations du site. C'est normal : ils n'ont aucun droit sur le site.

# Étape 5 — Vérifier le compte de service

1. **⚙️ › Autorisations du site** : ouvrez le groupe **Propriétaires**.
2. Cherchez le **compte de service** qui exécutera les flux. Les TI vous en donneront le nom.

❌ S'il n'y est pas, demandez aux TI de l'ajouter. Les flux 1 et 2 posent les autorisations de chaque dossier : ils ont besoin du **contrôle total**.

# Étape 6 — Créer la liste SRHVQ_Appreciations

1. Revenez à l'**accueil** du site (cliquez sur son nom en haut à gauche).
2. **+ Nouveau › Liste**.
3. Dans la fenêtre, section **Importer** : choisissez **À partir d'une liste existante**.
4. Choisissez le site **SandBoxAnnieAudet**. S'il n'est pas proposé, cherchez-le avec la zone de recherche.
5. Cliquez sur la liste **Appreciations**, puis **Suivant**.
6. Remplissez :
   - **Nom :** `SRHVQ_Appreciations`
   - **Description :** `Dossiers de l'application Appréciation de la contribution — ne pas modifier à la main`
   - **Afficher dans la navigation du site :** **décochez**. La liste n'a pas à être visible pour les utilisateurs.
7. **Créer**.

✅ La liste est créée, **vide**. Seule la structure (les colonnes) est recopiée, pas les données de test.

# Étape 7 — Régler la liste SRHVQ_Appreciations

Ouvrez la liste, puis **⚙️ › Paramètres de la liste**. Si vous voyez un panneau moderne, cliquez sur **Plus de paramètres de liste**.

**7a. Versions**

1. **Paramètres de contrôle de version**.
2. **Créer une version chaque fois que vous modifiez un élément** : **Oui**.
3. **OK**.

**7b. Pièces jointes**

1. **Paramètres avancés**.
2. **Pièces jointes à des éléments de liste** : **Activé**.
3. **OK**.

**7c. Les colonnes**

Dans la section **Colonnes**, vérifiez qu'il y a bien, entre autres : IdEmploye, Poste, Annee, TypePoste, TypeRencontre, Statut, CourrielPersonne, CourrielSI, CourrielSH, CourrielDirecteur, et les 6 colonnes de dates (AviseLe … TransmisPaieLe). La matrice de métadonnées liste les 34 colonnes.

1. Cliquez sur **TypeRencontre** : **Afficher les choix au moyen de** = **Cases à cocher (autoriser plusieurs sélections)**. **OK**.
2. Cliquez sur **Statut** : les 7 choix sont présents et la **valeur par défaut** est **Brouillon**. **OK**.

**7d. Les 6 index**

1. Section Colonnes, en bas : **Colonnes indexées**.
2. **Créer un index**, colonne principale **Annee**, puis **Créer**.
3. Recommencez pour **Statut**, **CourrielPersonne**, **CourrielSI**, **CourrielSH** et **CourrielDirecteur**. Un index à la fois.
4. **Ne créez pas** d'index sur TypeRencontre.

✅ La page Colonnes indexées affiche **6 index**.

# Étape 8 — Créer et remplir la liste SRHVQ_Parametres

1. Accueil du site : **+ Nouveau › Liste › À partir d'une liste existante**.
2. Choisissez **SandBoxAnnieAudet**, puis la liste **Parametres**, puis **Suivant**.
3. **Nom :** `SRHVQ_Parametres`. **Afficher dans la navigation :** décochez. **Créer**.
4. Dans la liste, **+ Nouveau** élément, 4 fois :

| Title | Valeur |
|---|---|
| Environnement | `PRE-PROD` |
| CourrielSoutien | *[adresse courriel du soutien]* |
| SupportNom | *[nom de la personne responsable du soutien]* |
| SupportTelephone | *[numéro de téléphone du soutien]* |

✅ La liste contient **exactement 4 éléments**, écrits exactement comme dans le tableau (majuscules comprises).

# Étape 9 — Donner les accès aux listes

## 9a. SRHVQ_Appreciations

1. Ouvrez la liste SRHVQ_Appreciations : **⚙️ › Paramètres de la liste › Autorisations pour cette liste**.
2. Dans le ruban : **Arrêter l'héritage des autorisations**, puis **OK**.
3. La liste des autorisations s'affiche. **Cochez tous les groupes et toutes les personnes, SAUF « Propriétaires ».** Ce sont par exemple Membres, Visiteurs, et les groupes d'autres applications du site.
4. Dans le ruban : **Supprimer les autorisations utilisateur**, puis **OK**.
5. Dans le ruban : **Accorder des autorisations**.
   1. Tapez `SRHVQ_Utilisateurs` et choisissez-le.
   2. **Afficher les options** : décochez l'invitation par courriel.
   3. Niveau d'autorisation : **Collaboration**.
   4. **Partager**.
6. Encore **Accorder des autorisations** : `SRHVQ_RH`, niveau **Lecture**, sans invitation, puis **Partager**.

✅ Il reste **exactement 3 lignes** :

| Nom | Niveau |
|---|---|
| Propriétaires du site | Contrôle total |
| SRHVQ_Utilisateurs | Collaboration |
| SRHVQ_RH | Lecture |

## 9b. SRHVQ_Parametres

Mêmes étapes 1 à 6, mais **SRHVQ_Utilisateurs** en **Lecture** (et SRHVQ_RH en **Lecture**). Les utilisateurs lisent les paramètres, ils ne les modifient jamais.

## 9c. Vérifier

1. Sur la page des autorisations de la liste, cliquez sur **Vérifier les autorisations** dans le ruban.
2. Tapez le nom d'un **testeur**, puis **Vérifier maintenant**.

✅ Le résultat affiche **Collaboration** sur SRHVQ_Appreciations, « par l'intermédiaire de SRHVQ_Utilisateurs ».

# Étape 10 — Déposer la documentation

Dans **Documents TI › SRHVQ - Appréciation de la contribution**, déposez :
- les 5 fichiers du dossier **documents-TI** : matrice de sécurité, matrice de métadonnées, architecture, liste des utilisateurs, révision des versions ;
- **GUIDE-MISE-EN-PRODUCTION.docx**.

Avant le dépôt, remplacez les **[crochets]** : adresse du site, groupe G-IS-APP, soutien.

# Étape 11 — Transmettre les valeurs aux TI

Écrivez à la personne des TI qui fera l'import (Bruno Gagnon ou la personne désignée) :

| Variable (nom d'affichage actuel) | Valeur PréProd |
|---|---|
| Site Appréciations | *[l'adresse copiée à l'étape 1]* |
| Liste Appreciations | **SRHVQ_Appreciations** |
| Liste Parametres | **SRHVQ_Parametres** |
| Courriel paie | votre adresse (pendant les tests) |
| Lienapplication | à remplir **après** l'import : le lien de l'application PréProd |

Indiquez aussi :
- le **compte de service** pour les connexions ;
- les **groupes** créés : SRHVQ_Utilisateurs (contient G-IS-APP) et SRHVQ_RH.

# Étape 12 — Après l'import par les TI

1. Demandez le **lien de l'application PréProd** : Power Apps › l'application › **Détails** › **Lien web**.
2. Faites inscrire ce lien dans la variable **Lienapplication** (par les TI, ou par vous si vous avez les droits).
3. Faites les **tests** du guide (GUIDE-PREPROD-ET-CONFORMITE, partie F) avec des données **fictives**.

# Important : la version déjà transmise (1.0.0.1)

Votre demande aux TI contient la solution exportée **1.0.0.1**, **avant** les ajustements de conformité.

| Avec la 1.0.0.1 en PréProd | Conséquence |
|---|---|
| Le flux 1 retire le groupe **Membres** du dossier, pas **SRHVQ_Utilisateurs** | Un nouveau dossier **reste visible par tous les membres de SRHVQ_Utilisateurs**. Faites seulement des tests **fictifs**, et ne faites pas le test de confidentialité avant la mise à niveau |
| Anciens noms des variables, pas de gestion des erreurs, pas d'écran À propos ni Aide | Non conforme aux exigences 2 à 10 |

**Deux options :**

1. **Recommandé, si Bruno n'a pas encore importé.** Faites au minimum le **flux 1** (partie B5 du guide de conformité), et créez le groupe SRHVQ_Utilisateurs dans le bac à sable (B1). Exportez de nouveau, en **gérée** et en version **1.0.0.2** ou plus, puis **remplacez le .zip** de la demande.
2. **Sinon :** laissez l'import de la 1.0.0.1 se faire, testez avec des données fictives, puis transmettez la **1.0.0.4** conforme comme **mise à niveau**. Les valeurs des variables et les données sont conservées.

Dans les deux cas : chaque nouvel export doit avoir un **numéro de version plus élevé** que le précédent, et être en **Gérée**.
