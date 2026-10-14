# Appréciation de la contribution — version 3.1 et guide de test « Page HTML »

Ce dossier contient tout ce qu'il faut pour :

1. **corriger** votre application (v3.0 → v3.1) afin qu'elle fonctionne dans une page HTML SharePoint ;
2. **l'utiliser dès aujourd'hui** sur votre ordinateur ;
3. **tester**, le jour où l'option « Page HTML » apparaît, ce que SharePoint permet réellement chez vous.

Tout est gratuit, rien à installer : les outils s'ouvrent par double-clic dans Edge.

| Fichier | Rôle |
|---|---|
| `appreciation/GUIDE-APPRECIATION.md` | Ce guide |
| `appreciation/appliquer-correctifs.html` | Outil qui corrige **votre** fichier `appreciation.html` (sans toucher aux images) |
| `test-bac-a-sable.html` | Page de diagnostic à téléverser comme « Page HTML » le jour J |
| `verificateur-html-sharepoint.html` | Vérificateur général (liens, scripts externes, taille, images) |
| `modele-page-sharepoint.html` | Page simple pour confirmer que la fonctionnalité marche |
| `README.md` | Guide général sur les pages HTML SharePoint |

---

## 1. Pourquoi votre page restait bloquée

Vous aviez collé le code dans une **page wiki classique** (`…aspx?WikiPageMode=Edit`). SharePoint Online **retire tout le JavaScript** de ces pages. Seul le CSS s'affiche, d'où l'écran « Protection de vos données locales » qui ne répond pas. Le logo cassé en est la preuve : c'est le script qui le place.

Même dans une vraie « Page HTML », la v3.0 aurait été bloquée, car la page tourne dans un **bac à sable** où :

| Ce que la v3.0 utilisait | Dans le bac à sable | Correction v3.1 |
|---|---|---|
| `localStorage` (brouillon chiffré) | ❌ interdit | L'écran de mot de passe est sauté, l'application démarre directement |
| Détection « je suis dans un cadre » | Toujours vrai | Le bandeau « Ouvrir l'application » ne bloque plus la page |
| « 💾 Copie locale » | Le téléchargement était sauté si l'enregistrement échouait | Le fichier `.json` est toujours téléchargé |
| `confirm()` avant un dépôt | Peut répondre « Non » sans s'afficher | Si la fenêtre est bloquée, le dépôt continue (la case « Je certifie » / « J'approuve » reste obligatoire) |
| `alert()` pour les erreurs | Peut être invisible | L'erreur s'affiche aussi dans la page |
| Script bloqué (page wiki) | Écran figé | Message clair : « Cette page ne peut pas s'exécuter ici » |

Votre circuit (fichier de dépôt → formulaire SharePoint → Power Automate) **n'est pas modifié**.

---

## 2. Corriger votre fichier (aujourd'hui, 2 minutes)

1. Enregistrez votre code actuel (v3.0) dans un fichier `appreciation.html`, s'il n'en est pas déjà un.
2. Double-cliquez sur **`appliquer-correctifs.html`**.
3. Glissez `appreciation.html` dans la zone pointillée.
4. Vérifiez la liste : **12 lignes ✅** attendues.
   - « ↺ Déjà appliqué » : normal si le fichier était déjà corrigé.
   - « ❌ Introuvable » : ce passage a été modifié depuis la v3.0. Voir la section 7.
5. Cliquez sur **« Télécharger la version corrigée »**. Vous obtenez `appreciation-v3.1.html`.
6. Ouvrez-le dans Edge : l'écran de mot de passe et toutes les fonctions marchent comme avant.

> L'outil fonctionne hors ligne. Votre fichier ne quitte jamais votre ordinateur.

## 3. Utiliser l'application en attendant (recommandé)

- Placez `appreciation-v3.1.html` dans un dossier OneDrive ou dans une bibliothèque SharePoint.
- Chaque personne le **télécharge et l'ouvre dans Edge**. Tout fonctionne : mot de passe, brouillon chiffré, dépôts, aperçu PDF.
- **Ne le collez pas** dans une page wiki ni dans un composant « Incorporer » : le JavaScript y est bloqué. La v3.1 affiche alors le message bleu « Cette page ne peut pas s'exécuter ici ».

---

## 4. Le type de contenu « Page Html » que vous avez trouvé

Dans **Pages du site › Paramètres › Types de contenu**, vous avez trouvé **« Page Html »**, avec les colonnes *Contenu du canevas de création*, *URL de l'image de bannière*, *Contenu de la mise en page*, *Auteur*, *En-tête de rubrique* et *Appel à l'action*.

**Ce que cela signifie :** c'est un très bon signe. Microsoft a déjà installé la « structure » de la fonctionnalité dans votre site. Le bouton « + Nouveau › Page HTML » arrive en général peu après, quand le déploiement de l'interface atteint votre locataire.

**Ce que vous pouvez faire sans risque :**

1. **Regarder** les paramètres (Nom et description, Paramètres avancés) pour voir ce qu'ils contiennent.
2. **Essayer de créer une page** avec ce type de contenu :
   - ouvrez la bibliothèque **Pages du site** (⚙️ › Contenu du site › Pages du site) ;
   - cliquez sur **+ Nouveau** : si « Page Html » apparaît dans la liste, choisissez-le ;
   - sinon, **Charger › Fichiers**, téléversez `modele-page-sharepoint.html`, puis ouvrez ses **propriétés** (… › Détails, ou Modifier les propriétés) et vérifiez si le **Type de contenu** peut être réglé sur « Page Html ».
3. Ouvrez la page : si elle **s'affiche** (et ne se télécharge pas), la fonctionnalité est active. Passez à la section 5.

**À ne pas faire :**

- ❌ **Ne supprimez pas** et ne modifiez pas ce type de contenu (« Supprimer ce type de contenu », colonnes, Paramètres avancés) : c'est Microsoft qui le gère. Un changement pourrait casser la fonctionnalité quand elle sera activée.
- ❌ N'ajoutez pas ce type de contenu à d'autres bibliothèques.
- ❌ Ne réglez pas « Paramètres du flux de travail » sur ce type de contenu.

Si le fichier se télécharge au lieu de s'afficher, l'interface n'est pas encore activée chez vous. Ce n'est qu'une question de semaines (déploiement prévu jusqu'à fin décembre 2026).

---

## 5. Guide de test, le jour où « Page HTML » apparaît

Faites les tests **dans votre site sandbox**, dans cet ordre. Comptez environ 20 minutes.

### Test 1 : la fonctionnalité marche-t-elle ? (2 min)
1. Pages du site › **Charger › Fichiers** › `modele-page-sharepoint.html`.
2. Ouvrez la page.

| Résultat | Signification |
|---|---|
| La page s'affiche avec ses couleurs et les onglets « Nouvelles » réagissent au clic | ✅ Les pages HTML et le JavaScript fonctionnent |
| La page se télécharge | Fonctionnalité pas encore active, ou « Autoriser les fichiers HTML » désactivé (README, section 3) |
| Pas de couleurs, onglets inertes | JavaScript bloqué : notez-le et refaites le test plus tard |

### Test 2 : qu'est-ce que le bac à sable permet ? (5 min)
1. Ouvrez `test-bac-a-sable.html` dans le Bloc-notes et vérifiez les liens « À MODIFIER » de la section 3 (votre site est déjà prérempli).
2. Téléversez-le dans Pages du site, puis ouvrez-le.
3. Lisez le tableau **« Tests automatiques »**.
4. Cliquez sur chaque bouton de la section 2 : Boîte de dialogue, Téléchargement, Nouvel onglet, Impression, Presse-papiers, Lire un fichier.
5. Cliquez sur chaque lien de la section 3 et notez s'il s'ouvre.
6. **Copiez le « Résumé »** et gardez-le : c'est la carte des règles de votre organisation.

**Résultats attendus selon Microsoft :** JavaScript ✅, chiffrement ✅ probablement, localStorage ❌, fetch ❌, page parente ❌, liens même site et même locataire ✅, liens externes ❌ (tant qu'ils ne sont pas autorisés).

### Test 3 : votre application v3.1 (10 min)
1. Téléversez `appreciation-v3.1.html` dans Pages du site, puis ouvrez-le.
2. Cochez cette grille :

| # | Action | Résultat attendu (v3.1) | ✅ / ❌ |
|---|---|---|---|
| 1 | Ouvrir la page | L'application s'affiche **sans** écran de mot de passe, avec le bandeau « Formulaire affiché dans une page SharePoint » | |
| 2 | Choisir un type de poste et un rôle | Le formulaire s'adapte | |
| 3 | Remplir quelques champs, passer d'un onglet à l'autre | Les champs restent remplis | |
| 4 | « 💾 Copie locale » | Un fichier `appreciation-….json` arrive dans Téléchargements | |
| 5 | « 📁 Charger un dossier » avec ce fichier | Les données reviennent | |
| 6 | « ☁️ Déposer sur SharePoint » | Fichier `depot-….json` téléchargé et fenêtre « dernière étape » affichée | |
| 7 | Bouton « Ouvrir le formulaire de dépôt » | Le formulaire SharePoint s'ouvre dans un nouvel onglet | |
| 8 | « 📂 Ouvrir Mes dossiers » | La bibliothèque s'ouvre | |
| 9 | « 🖨️ Aperçu PDF » | La fenêtre d'impression s'affiche | |
| 10 | Lien « ✉️ Envoyer » (aide) | Outlook s'ouvre | |
| 11 | Actualiser la page (F5) | ⚠️ Le brouillon est **perdu** : c'est normal, pas de stockage. D'où les étapes 4 et 5 | |

3. Selon les résultats :

| Si… | Alors… |
|---|---|
| Tout est ✅ (sauf 11) | L'application peut vivre dans SharePoint. Formez les utilisateurs à « 💾 Copie locale » avant de fermer la page. |
| 4 ou 6 ❌ (téléchargements bloqués) | Le circuit de dépôt est impossible dans la page : gardez l'usage **local** (section 3) et mettez seulement un lien de téléchargement dans SharePoint. |
| 7, 8 ou 10 ❌ | Notez-le. Il faudra transformer ces boutons en liens `<a target="_blank">` (je peux faire cette version). |
| 9 ❌ | L'aperçu PDF ne fonctionnera que dans la version locale. |

### Test 4 : les liens externes (si besoin)
Si un lien externe ne s'ouvre pas, ajoutez son domaine dans **⚙️ › Informations sur le site › Afficher tous les paramètres du site › Sécurité des champs HTML**, sans `https://` (README, section 4).

---

## 6. Ce qui reste limité, même en v3.1

- **Pas de brouillon automatique** dans une page SharePoint, car le stockage est interdit. Un rafraîchissement ou une fermeture de la page fait perdre la saisie non copiée.
- **Fenêtres de confirmation** : si SharePoint les bloque, les actions « Nouveau formulaire », « Changer de type de poste » et « Recommencer à neuf » **ne feront rien**. C'est volontaire : on ne veut pas effacer sans confirmation. Le **dépôt**, lui, fonctionne.
- **Téléchargements, impression, nouvel onglet** : dépendent des réglages de Microsoft. Le test 2 vous le dira.

Pour une application avec saisie longue, rôles et approbations, la solution durable reste **Power Apps + liste SharePoint** : sauvegarde réelle, pas de fichiers à déposer, identité gérée automatiquement.

---

## 7. Corrections manuelles (si l'outil affiche « ❌ Introuvable »)

Ouvrez votre fichier dans le Bloc-notes (ou Visual Studio Code, gratuit) et cherchez (Ctrl+F) le texte indiqué.

| Correctif | Chercher | Remplacer par |
|---|---|---|
| Fonctions utilitaires | la ligne `<script>` (la seule du fichier) | `<script>` puis, à la ligne suivante : `function storageDispo(){ try{ localStorage.setItem('__t','1'); localStorage.removeItem('__t'); return true; }catch(e){ return false; } }` |
| Écran de mot de passe | `if(!cryptoAvailable){` suivi de `// Navigateur sans Web Crypto` | `if(!cryptoAvailable \|\| !storageDispo()){ localStorageOK = storageDispo();` |
| Bandeau de lancement | `return inIframe \|\| webParam;` | `return webParam;` |
| Copie locale | `if(!vaultKey) return;` | `if(!vaultKey){ if(manual){ exportJSON(); } return; }` |
| Copie locale (2 endroits) | `note.textContent = manual ? '⚠️ Sauvegarde locale indisponible ici` | ajouter juste avant : `if(manual){ exportJSON(); }` |
| Dépôt sans confirmation | `if(!confirm(confirmations[action])) return;` | `var t31 = Date.now(); var ok31 = confirm(confirmations[action]); if(!ok31 && Date.now() - t31 > 50) return;` |

Après une correction manuelle, repassez le fichier dans `appliquer-correctifs.html` : les correctifs restants s'appliqueront et les autres afficheront « ↺ Déjà appliqué ».

---

## 8. Dépannage

| Symptôme | Cause | Solution |
|---|---|---|
| Écran bleu « Cette page ne peut pas s'exécuter ici » | JavaScript bloqué (page wiki, composant Incorporer) | Utilisez le fichier en local (section 3) ou une vraie « Page HTML » |
| Écran de mot de passe qui ne répond pas | Ancienne version (v3.0) | Appliquez les correctifs (section 2) |
| Le fichier `.html` se télécharge au lieu de s'afficher dans SharePoint | Fonctionnalité pas encore active | Attendre ; vérifier « Autoriser les fichiers HTML » |
| Rien ne se passe en cliquant sur « Nouveau formulaire » | Fenêtres de confirmation bloquées | Rechargez la page (F5) pour repartir à vide |
| Le dépôt ne télécharge aucun fichier | Téléchargements bloqués par le bac à sable | Utiliser l'application en local |
| Lien externe qui ne s'ouvre pas | Domaine non autorisé | Sécurité des champs HTML (README, section 4) |
