# Version 3.3 — correctif du blocage dans la page HTML SharePoint

Fichier : `appreciation-cadres-v3.3.html` (remplace la v3.2). Il contient les trois formulaires du 15 octobre 2026 (voir `VERSION-3.2.md`).

---

## 1. Le problème

Dans la page HTML SharePoint, l'application restait bloquée sur l'écran « Protection de vos données locales ». Avec le bon mot de passe, elle répondait **« ❌ Mot de passe incorrect »**. En arrière-plan, l'erreur était `"[object Object]" is not valid JSON`.

**Cause (reproduite en test) :** SharePoint ne bloque pas toujours le stockage du navigateur par une erreur. Il peut le **remplacer par une imitation** : l'écriture « réussit », mais la lecture renvoie un objet au lieu d'un texte. La v3.1 croyait donc le stockage disponible. Elle affichait l'écran de mot de passe, puis échouait en lisant le brouillon (`JSON.parse` d'un objet). L'échec était présenté comme un mauvais mot de passe.

## 2. Ce que corrige la v3.3

| Avant | Maintenant |
|---|---|
| Le stockage est jugé disponible s'il ne lève pas d'erreur | Le stockage est **vérifié par un aller-retour complet** (écrire, relire le même texte, vérifier qu'une clé absente est vide) |
| `JSON.parse` direct sur ce qui est lu | Toutes les lectures passent par `lireStockage()` et `lireJSON()` : elles ne plantent jamais |
| Brouillon illisible = « Mot de passe incorrect » | Un brouillon illisible est ignoré ; l'application démarre |
| ⚙️ Configuration « enregistrée » même quand rien n'est conservé | Elle est gardée pour la session, et un message le dit clairement |

**Résultat dans SharePoint :** pas d'écran de mot de passe. L'application s'ouvre directement, avec le bandeau « Formulaire affiché dans une page SharePoint ». Le reste fonctionne : 💾 Copie locale, 📁 Charger un dossier, ☁️ Déposer sur SharePoint.

**Sur le poste (fichier ouvert dans Edge) :** rien ne change. Le mot de passe et le brouillon chiffré fonctionnent comme avant.

Tests faits le 16 octobre 2026 en navigateur automatisé, sans erreur :
- stockage bloqué ;
- stockage imité qui renvoie des objets (le cas qui bloquait) ;
- stockage en mémoire ;
- vraie iframe isolée (`sandbox="allow-scripts allow-downloads allow-modals allow-popups"`) ;
- usage local normal ;
- les trois formulaires.

## 3. Étape obligatoire avant de téléverser dans SharePoint : inscrire les adresses dans le fichier

Dans une page HTML SharePoint, le navigateur **ne peut rien conserver**. Les adresses saisies dans ⚙️ Configuration sont donc perdues à chaque ouverture. Il faut les inscrire **une fois dans le fichier** :

1. Ouvrez `appreciation-cadres-v3.3.html` dans le Bloc-notes (ou Visual Studio Code, gratuit).
2. Cherchez (Ctrl+F) : `const CONFIG_DEFAUT`
3. Remplissez les trois adresses entre les apostrophes :

```js
const CONFIG_DEFAUT = {
  depotNewFormUrl: 'https://villedequebec.sharepoint.com/sites/VOTRE-SITE/Lists/Depot_Appreciations/NewForm.aspx',
  mesDossiersUrl: 'https://villedequebec.sharepoint.com/sites/VOTRE-SITE/Dossiers_Appreciations',
  lienApplication: 'https://villedequebec.sharepoint.com/sites/VOTRE-SITE/SitePages/...'
};
```

4. Enregistrez, puis téléversez le fichier dans Pages du site.

Ce ne sont pas des secrets : sans compte de la Ville, ces pages ne s'ouvrent pas.

## 4. Test dans SharePoint (10 minutes)

| # | Action | Résultat attendu | ✅ / ❌ |
|---|---|---|---|
| 1 | Ouvrir la page HTML | **Aucun écran de mot de passe** ; bandeau « Formulaire affiché dans une page SharePoint » | |
| 2 | Choisir un type de poste, remplir le nom | Les champs restent remplis | |
| 3 | « 💾 Copie locale » | Un fichier `appreciation-….json` arrive dans Téléchargements | |
| 4 | Actualiser (F5), puis « 📁 Charger un dossier » avec ce fichier | Les données reviennent | |
| 5 | « ☁️ Déposer sur SharePoint » | Fichier `depot-….json` téléchargé et fenêtre « dernière étape » | |
| 6 | « Ouvrir le formulaire de dépôt » et « 📂 Ouvrir Mes dossiers » | Les pages s'ouvrent dans un nouvel onglet | |
| 7 | « 🖨️ Aperçu PDF » | La fenêtre d'impression s'affiche | |
| 8 | Lien « ✉️ Envoyer » (Aide-mémoire) | Outlook s'ouvre | |

Si 6, 7 ou 8 ne fonctionnent pas, notez-le : je pourrai les remplacer par des liens simples (`<a target="_blank">`). Ce sont les seules fonctions qui dépendent des réglages de Microsoft.

## 5. Les conseils de Copilot, point par point

| Conseil de Copilot | Avis | Pourquoi |
|---|---|---|
| Le stockage, `fetch` et `XMLHttpRequest` sont interdits | ✅ Juste | C'est la règle du bac à sable (voir `README.md`) |
| L'erreur JSON vient d'un `JSON.parse` sur un objet | ✅ Juste | Confirmé et corrigé (section 2) |
| Ajouter une fonction `safeJsonParse` | ✅ Fait | C'est `lireJSON()` |
| Inscrire la configuration dans le fichier | ✅ Juste | C'est la section 3 : il suffit de remplir `CONFIG_DEFAUT`, qui existe déjà |
| Supprimer complètement le coffre-fort et le mot de passe | ❌ Pas nécessaire | Le coffre-fort protège le brouillon quand le fichier est utilisé sur le poste. Depuis la v3.1, il est sauté automatiquement quand le stockage manque ; la v3.3 détecte maintenant aussi l'imitation de SharePoint |
| Remplacer le stockage par `window.appData` | ❌ Inutile | La variable `state` joue déjà ce rôle. Sans stockage, rien ne survit à un rafraîchissement, quelle que soit la variable |
| « Abandonner les fichiers JSON » et écrire dans des listes | ⚠️ Contradictoire | Copilot dit lui-même que la page ne peut pas faire d'appel réseau. Elle ne peut donc **pas écrire dans une liste**. Le fichier de dépôt est le seul pont possible |
| Architecture HTML → fichier JSON → SharePoint → Power Automate | ✅ Déjà en place | C'est exactement le circuit de dépôt de la v3.0 (`Depot_Appreciations` → flux → `Dossiers_Appreciations`) |
| Listes Appréciations, Objectifs, Leadership, Valeurs, Approbations et 7 flux | ⚠️ Déjà fait ailleurs | C'est l'architecture de l'application **Power Apps EVAL** déjà construite (7 listes, 3 flux). Il ne faut pas la refaire pour la page HTML |
| Version 2 : SPFx + listes | ✅ Juste | C'est la recommandation déjà notée dans `ETAT-DU-PROJET.md`, à demander au TI |

**En résumé :** Copilot a bien trouvé la famille du problème. Le correctif nécessaire est petit : vérifier réellement le stockage et lire le JSON prudemment. Il n'est pas nécessaire de réécrire l'application ni de supprimer le mot de passe.
