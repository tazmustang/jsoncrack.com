# Guide d'installation — Appréciation de la contribution (version 3.8)

Pour la personne qui installe et entretient l'outil. Mis à jour le 20 octobre 2026.

Tout est gratuit, sans aucune installation sur les postes. Le site de test est **SandBox Annie Audet**.

---

## 1. Comment l'outil fonctionne

| Élément | Rôle |
|---|---|
| `appreciation-cadres-v3.8.html` | L'application : un seul fichier qui contient les 3 formulaires du 15 octobre 2026 |
| Bibliothèque « Appréciation de la contribution des cadres » | L'endroit où les gens **ouvrent** l'application (un clic sur le fichier) |
| Liste **Depot_Appreciations** | La porte d'entrée : chacun y **colle** son dépôt dans le champ « Contenu » (ou joint un fichier). SharePoint note qui l'a déposé |
| Bibliothèque **Dossiers_Appreciations** | Les dossiers officiels (« Mes dossiers ») |
| Flux Power Automate « AC - Traiter un dépôt » | Lit chaque dépôt, vérifie l'identité et l'étape, met à jour le dossier, envoie les courriels. **À construire** (section 6) |

**Deux façons de travailler :**

| | Dans SharePoint (clic sur le fichier) | Sur le poste (⤓ Télécharger, puis ouvrir) |
|---|---|---|
| Remplir, choisir son rôle et son poste | ✅ | ✅ |
| Garder la saisie si on ferme la page | ❌ : il faut **déposer** avant de partir | ✅ brouillon protégé par mot de passe |
| Déposer | **Copier-coller** dans le champ « Contenu » | Fichier joint au formulaire de dépôt |
| Reprendre un dossier | 📂 Mes dossiers, puis 📁 Charger un dossier | Idem, ou le brouillon du poste |

SharePoint bloque l'enregistrement et les téléchargements dans l'aperçu ; c'est une règle de Microsoft. L'application le détecte et passe d'elle-même en **mode SharePoint**, avec un bandeau qui l'explique.

## 2. La liste « Depot_Appreciations » ✅ (créée le 19 octobre) — **ajouter la colonne « Contenu »**

**À faire maintenant (2 minutes)**, pour le dépôt dans SharePoint :

1. Ouvrez la liste **Depot_Appreciations**.
2. Cliquez sur **+ Ajouter une colonne › Plusieurs lignes de texte**.
3. Nom : `Contenu` (à la lettre). Ouvrez **Plus d'options** et **désactivez « Utiliser le texte enrichi »** : le champ doit rester en texte brut.
4. Cliquez sur **Enregistrer**.
5. Vérifiez : le formulaire « Nouvel élément » affiche maintenant un grand champ **Contenu** au-dessus de « Pièces jointes ».

Un dossier complet fait environ 20 000 caractères. Le champ en accepte environ 64 000. Si un dépôt était trop long, l'application le signale et propose de joindre un fichier à la place.

Pour mémoire, si la liste est à refaire :

1. Dans le site, cliquez sur **+ Nouveau › Liste › Liste vide**. Nom : `Depot_Appreciations` (à la lettre). Cliquez sur **Créer**.
2. Allez dans ⚙️ › **Paramètres de la liste** › colonne **Titre** : « Exiger que cette colonne contienne des informations » = **Non**.
3. Dans **Paramètres avancés** :
   - Pièces jointes : **Activées** ;
   - Accès en lecture : **Lire les éléments créés par l'utilisateur** ;
   - Accès en création et modification : **Créer des éléments et modifier les éléments créés par l'utilisateur**.
4. Ajoutez la colonne **Contenu** (voir plus haut).
5. Vérifiez : l'adresse `https://villedequebec.sharepoint.com/sites/SandBoxAnnieAudet/Lists/Depot_Appreciations/NewForm.aspx` doit afficher « Nouvel élément », avec **Contenu** et **Ajouter des pièces jointes**.

## 3. Créer la bibliothèque « Dossiers_Appreciations »

1. Cliquez sur **+ Nouveau › Bibliothèque de documents › Bibliothèque vide**. Nom : `Dossiers_Appreciations` (à la lettre). Cliquez sur **Créer**.
2. Ajoutez ces colonnes avec **+ Ajouter une colonne** :

| Colonne | Type |
|---|---|
| DossierId | Une seule ligne de texte |
| NomPersonne | Une seule ligne de texte |
| TypePoste | Une seule ligne de texte |
| Statut | Choix : Brouillon · En approbation · En approbation finale · Complété |
| EtapeEnCours | Une seule ligne de texte |
| DerniereMaj | Date et heure |

3. Allez dans ⚙️ › **Paramètres de la bibliothèque** › **Paramètres de contrôle de version** : **Créer des versions principales**, conserver **50** versions.
4. Vérifiez : l'adresse `https://villedequebec.sharepoint.com/sites/SandBoxAnnieAudet/Dossiers_Appreciations` doit s'ouvrir.

## 4. Déposer l'application

1. Dans la bibliothèque « Appréciation de la contribution des cadres », créez si vous le voulez un dossier **Application**.
2. **Permissions** : vous en modification, les utilisateurs en **lecture seule**.
3. Cliquez sur **Charger › Fichiers** › `appreciation-cadres-v3.8.html`.
4. Supprimez les anciennes versions (v3.3 à v3.6).

**Les adresses SharePoint sont déjà inscrites dans le fichier** : formulaire de dépôt, « Mes dossiers » et lien de la bibliothèque. Il n'y a rien à modifier dans le Bloc-notes.

> Si un jour une adresse change, ouvrez le fichier dans le Bloc-notes et cherchez `const CONFIG_DEFAUT`. Collez la nouvelle adresse **entre les deux apostrophes** de la bonne ligne, puis enregistrez.

**Mises à jour :** déposez la nouvelle version. Si elle porte le **même nom** que l'ancienne, choisissez **Remplacer** : le lien reste le même et l'historique garde l'ancienne. Si le nom change (par exemple v3.8 → v3.8), supprimez l'ancienne.

## 5. Tester (15 minutes)

Faites le test **sur le poste** :
1. Téléchargez le fichier avec ⤓ Télécharger dans la bibliothèque.
2. Ouvrez-le (double-clic : il s'ouvre dans Edge).

| # | Action | Résultat attendu | ✅ / ❌ |
|---|---|---|---|
| 1 | Créer le mot de passe | L'application s'ouvre sur « Qui êtes-vous ? » | |
| 2 | Cocher « Personne en appréciation » | Le choix du type de poste apparaît | |
| 3 | Choisir « Cadre avec équipe » | Le formulaire s'ouvre ; pas de numéro de dossier | |
| 4 | Remplir le nom, puis « 💾 Copie locale » | Un fichier `appreciation-….json` arrive dans Téléchargements | |
| 5 | Actualiser (F5) et redonner le mot de passe | Le brouillon revient ; le rôle est gardé | |
| 6 | « 📁 Charger un dossier » avec le fichier de l'étape 4 | Les données reviennent | |
| 7 | « ☁️ Déposer sur SharePoint » | Un fichier `depot-….json` arrive et une fenêtre d'instructions s'ouvre | |
| 8 | « Ouvrir le formulaire de dépôt », joindre le fichier, Enregistrer | L'élément apparaît dans Depot_Appreciations | |
| 9 | « 📂 Ouvrir Mes dossiers » | La bibliothèque Dossiers_Appreciations s'ouvre | |
| 10 | « 🖨️ Aperçu PDF » | La fenêtre d'impression s'affiche ; la version est au bas | |
| 11 | « 🗑️ Nouveau formulaire » | Tout est vidé ; « Qui êtes-vous ? » est redemandé | |
| 12 | Cocher « Supérieur(e) immédiat(e) » | Pas de choix du type de poste : « Ouvrez le dossier de la personne en appréciation » | |
| 13 | « 📁 Charger un dossier » avec le fichier de l'étape 4 | Le formulaire s'ouvre avec le type de poste choisi par la personne | |

**Ensuite, le test dans SharePoint** (simple clic sur le fichier dans la bibliothèque) :

| # | Action | Résultat attendu | ✅ / ❌ |
|---|---|---|---|
| S1 | Ouvrir le fichier | Pas de mot de passe ; bandeau « Vous travaillez dans SharePoint… » | |
| S2 | Cocher « Personne en appréciation », choisir le poste, remplir le nom | Le formulaire s'affiche | |
| S3 | « ☁️ Déposer sur SharePoint » | La fenêtre propose « 📋 Copier le contenu du dépôt » | |
| S4 | « 📋 Copier », puis « 🔗 Ouvrir le formulaire de dépôt » | Le formulaire s'ouvre dans un nouvel onglet | |
| S5 | Coller (Ctrl+V) dans **Contenu**, puis Enregistrer | L'élément apparaît dans Depot_Appreciations ; le champ Contenu commence par `{"format":"appreciation-depot-v1"` | |
| S6 | Dans l'onglet de l'application, cliquer sur « 📁 Charger un dossier » avec un fichier `.json` | Les données reviennent | |
| S7 | « 🖨️ Aperçu PDF » | Notez si la fenêtre d'impression s'affiche (cela dépend des réglages de Microsoft) | |

## 6. Prochaine étape : le flux « AC - Traiter un dépôt »

Sans ce flux, un dépôt reste dans la liste : aucun courriel n'est envoyé et aucun dossier officiel n'est créé. Le flux :
- lit le champ **Contenu** (ou, s'il est vide, le fichier joint) ;
- reconnaît le déposant (son compte de la Ville) ;
- vérifie que c'est bien son étape ;
- ne recopie que les sections que son rôle peut modifier ;
- met à jour le dossier dans Dossiers_Appreciations ;
- avise la personne suivante ;
- supprime l'élément de dépôt.

Il n'utilise que des connecteurs standard (SharePoint, Office 365 Outlook, Office 365 Users), donc **aucune licence Premium**. Prévoyez 2 à 3 jours avec les tests. Dans le site de test, il peut être construit avec votre propre compte. Pour le site officiel, il faudra un compte de service fourni par le TI. Le guide pas à pas sera fourni à cette étape.

## 7. Ce qu'il ne faut pas faire

- Mettre le fichier dans **Pages du site** : l'option « Page HTML » n'y est pas encore activée (déploiement Microsoft jusqu'à fin décembre 2026).
- Coller l'application dans une page wiki ou un composant « Incorporer » : SharePoint retire le JavaScript.
- Retirer le mot de passe de l'application : il protège le brouillon sur le poste, et il est déjà sauté automatiquement dans SharePoint.
- Activer le texte enrichi dans la colonne « Contenu » : il abîmerait le contenu collé.
- Renommer les identifiants dans le code (performant, autonomie, sst…). Ils relient la page, le flux et le PDF ; seuls les libellés peuvent changer.
