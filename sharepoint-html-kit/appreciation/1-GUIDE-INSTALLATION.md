# Guide d'installation — Appréciation de la contribution (version 3.7)

Pour la personne qui installe et entretient l'outil. Mis à jour le 19 octobre 2026.

Tout est gratuit, sans aucune installation sur les postes. Le site de test est **SandBox Annie Audet**.

---

## 1. Comment l'outil fonctionne

| Élément | Rôle |
|---|---|
| `appreciation-cadres-v3.7.html` | L'application : un seul fichier qui contient les 3 formulaires du 15 octobre 2026 |
| Bibliothèque « Appréciation de la contribution des cadres » | L'endroit où les gens **trouvent et téléchargent** l'application |
| Liste **Depot_Appreciations** | La porte d'entrée : chacun y joint son fichier de dépôt. SharePoint note qui l'a déposé |
| Bibliothèque **Dossiers_Appreciations** | Les dossiers officiels (« Mes dossiers ») |
| Flux Power Automate « AC - Traiter un dépôt » | Lit chaque dépôt, vérifie l'identité et l'étape, met à jour le dossier, envoie les courriels. **À construire** (section 6) |

**Règle importante :** l'aperçu SharePoint (clic sur le fichier dans la bibliothèque) affiche l'application, mais il **bloque l'enregistrement et les téléchargements**. On travaille donc dans le fichier **téléchargé et ouvert sur le poste**. C'est une règle de Microsoft ; l'application l'indique elle-même dans un bandeau.

## 2. Créer la liste « Depot_Appreciations » ✅ (faite le 19 octobre)

Pour mémoire, si elle est à refaire :

1. Dans le site, cliquez sur **+ Nouveau › Liste › Liste vide**. Nom : `Depot_Appreciations` (à la lettre). Cliquez sur **Créer**.
2. Allez dans ⚙️ › **Paramètres de la liste** › colonne **Titre** : « Exiger que cette colonne contienne des informations » = **Non**.
3. Dans **Paramètres avancés** :
   - Pièces jointes : **Activées** ;
   - Accès en lecture : **Lire les éléments créés par l'utilisateur** ;
   - Accès en création et modification : **Créer des éléments et modifier les éléments créés par l'utilisateur**.
4. Vérifiez : l'adresse `https://villedequebec.sharepoint.com/sites/SandBoxAnnieAudet/Lists/Depot_Appreciations/NewForm.aspx` doit afficher « Nouvel élément », avec **Ajouter des pièces jointes**.

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
3. Cliquez sur **Charger › Fichiers** › `appreciation-cadres-v3.7.html`.
4. Supprimez les anciennes versions (v3.3, v3.4, v3.5).

**Les adresses SharePoint sont déjà inscrites dans le fichier** : formulaire de dépôt, « Mes dossiers » et lien de la bibliothèque. Il n'y a rien à modifier dans le Bloc-notes.

> Si un jour une adresse change, ouvrez le fichier dans le Bloc-notes et cherchez `const CONFIG_DEFAUT`. Collez la nouvelle adresse **entre les deux apostrophes** de la bonne ligne, puis enregistrez.

**Mises à jour :** déposez la nouvelle version. Si elle porte le **même nom** que l'ancienne, choisissez **Remplacer** : le lien reste le même et l'historique garde l'ancienne. Si le nom change (par exemple v3.7 → v3.7), supprimez l'ancienne.

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

Ensuite, ouvrez le fichier **dans l'aperçu SharePoint** (simple clic dans la bibliothèque). Résultat attendu : pas de mot de passe, et un bandeau qui demande de cliquer sur ⤓ Télécharger.

## 6. Prochaine étape : le flux « AC - Traiter un dépôt »

Sans ce flux, un dépôt reste dans la liste : aucun courriel n'est envoyé et aucun dossier officiel n'est créé. Le flux :
- lit le fichier joint ;
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
- Retirer le mot de passe de l'application : il protège le brouillon sur le poste, et il est déjà sauté automatiquement dans l'aperçu SharePoint.
- Renommer les identifiants dans le code (performant, autonomie, sst…). Ils relient la page, le flux et le PDF ; seuls les libellés peuvent changer.
