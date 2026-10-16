# État du projet « Pages HTML SharePoint » — au 14 octobre 2026

Résumé de tout ce qui a été trouvé, testé et décidé. **Commencez par ce document.**

---

## 1. Où on en est (en une minute)

| Sujet | État | Prochaine action |
|---|---|---|
| Fonctionnalité « Page HTML » dans SharePoint | ⏳ **Pas encore activée** dans le site SandBox Annie Audet | Refaire le test rapide (section 4) de temps en temps |
| Structure technique (type de contenu « Page Html ») | ✅ Déjà présente dans Pages du site | Ne rien modifier |
| Votre navigateur (HTML, CSS, JavaScript) | ✅ Fonctionne (test du 14 octobre) | — |
| Application « Appréciation de la contribution » | ✅ **v3.2** (16 oct.) : formulaire cadre avec équipe du 15 octobre 2026, utilisable **en local** | Installer la v3.2 (`appreciation/VERSION-3.2.md`) ; ensuite, cadre sans équipe et professionnel |
| Application dans une page wiki SharePoint | ❌ Impossible : SharePoint retire le JavaScript | Ne plus utiliser cette méthode |

---

## 2. Ce que nous avons appris

### La fonctionnalité
- Microsoft déploie les pages HTML depuis **début octobre 2026** (préversion) jusqu'à **fin décembre 2026** (disponibilité générale), message MC1479517.
- La page HTML tourne dans un **bac à sable** (iframe isolé) : JavaScript intégré permis, mais **pas de stockage navigateur, pas d'appel réseau, pas de script ou de feuille de style externe**, et un fichier de 10 Mo maximum.
- Liens : même site et même locataire ✅ ; autre locataire et sites externes ❌ tant que le domaine n'est pas ajouté dans **Sécurité des champs HTML**.
- Copilot est facultatif (licence requise). Téléverser un fichier `.html` est gratuit.

### Dans votre site (constats du 14 octobre)
| Constat | Signification |
|---|---|
| **+ Nouveau** de Pages du site propose seulement : Page Wiki (classique), Page Web Part (classique), Lien | L'option « Page HTML » n'est pas encore arrivée |
| **Paramètres de la bibliothèque › Types de contenu** affiche « Page Html », cochée « Visible sur le bouton Nouveau » | La structure est installée : bon signe, l'activation approche |
| Le fichier `test.html` **ne peut pas être ajouté** à Pages du site | Les fichiers HTML ne sont pas encore acceptés |
| `test.html` **ouvert dans un onglet** : fond bleu + « ✅ Le JavaScript fonctionne ! » | Tout est prêt de votre côté |

### Votre application « Appréciation de la contribution »
- Collée dans une **page wiki classique**, elle restait bloquée sur l'écran « Protection de vos données locales ». Cause : SharePoint **retire le JavaScript** des pages wiki. Seul le CSS s'affichait (preuve : logo cassé).
- Dans une future page HTML, la v3.0 serait aussi restée bloquée (stockage interdit, bandeau « Ouvrir l'application », fenêtres de confirmation).
- **La v3.1 corrige ces points.** Testée en simulation du bac à sable : démarrage OK, copie locale OK, dépôt OK.

---

## 3. Ce qu'il ne faut PAS faire

- ❌ **Appliquer un modèle de site** (Paramètres › Appliquer un modèle de site) : cela restructure tout le site et n'a rien à voir avec les pages HTML.
- ❌ Créer une **Page Wiki** ou une **Page Web Part (classique)** pour y mettre du HTML avec JavaScript : le script est retiré.
- ❌ Modifier ou supprimer le **type de contenu « Page Html »** ou ses colonnes.
- ❌ Choisir une **Page d'application** : c'est un composant de résultats de recherche, pas une page HTML.

---

## 4. Le test rapide à refaire de temps en temps (2 minutes)

1. Ouvrez **Pages du site** (⚙️ › Contenu du site › Pages du site).
2. Cliquez sur **+ Nouveau** : y a-t-il **« Page HTML »** ?
3. Sinon, glissez **`test.html`** (bureau) dans la liste.
4. Cliquez sur le fichier :
   - page bleue + bouton qui répond → 🎉 **c'est activé** : suivez `appreciation/GUIDE-APPRECIATION.md`, section 5 ;
   - téléversement refusé ou téléchargement → pas encore prêt ; supprimez le fichier s'il a été ajouté.

---

## 5. Les fichiers du kit

| Fichier | À quoi il sert | Quand |
|---|---|---|
| `ETAT-DU-PROJET.md` | Ce résumé | Maintenant |
| `README.md` | Guide complet sur les pages HTML SharePoint (règles, liens, installation, dépannage, sources) | Pour comprendre |
| `test.html` | Petit fichier de test (fond bleu + bouton) | Test rapide (section 4) |
| `appreciation/appreciation-cadres-v3.2.html` | L'application à jour (formulaire cadre avec équipe du 15 octobre 2026) | **Maintenant** |
| `appreciation/VERSION-3.2.md` | Changements, installation et test de la v3.2 | Maintenant |
| `appreciation/appliquer-correctifs.html` | Transforme votre `appreciation.html` v3.0 en **v3.1** | **Aujourd'hui** |
| `appreciation/GUIDE-APPRECIATION.md` | Guide de l'application : correctifs, utilisation, test du jour J, dépannage | Aujourd'hui et jour J |
| `test-bac-a-sable.html` | Diagnostic complet de ce que SharePoint autorise | Jour J |
| `modele-page-sharepoint.html` | Modèle de page d'accueil prêt à personnaliser | Jour J ou pour un projet de page |
| `verificateur-html-sharepoint.html` | Vérifie un fichier HTML avant téléversement, corrige les liens, convertit les images en base64 | Avant chaque téléversement |

Tous les fichiers `.html` s'ouvrent par **double-clic dans Edge**, sans installation, et fonctionnent hors ligne.

---

## 6. Prochaines étapes

1. **Aujourd'hui** : appliquer les correctifs → `appreciation-v3.1.html` sur le Bureau OneDrive → l'utiliser en l'ouvrant dans Edge.
2. **Chaque semaine** : test rapide (section 4).
3. **Jour J** (« Page HTML » disponible) : `GUIDE-APPRECIATION.md`, section 5 (tests 1 à 4), garder le résumé du `test-bac-a-sable.html`.
4. **Ensuite, selon les résultats** : soit l'application vit dans une page HTML SharePoint, soit elle reste en local. À plus long terme, envisager **Power Apps + liste SharePoint** pour une vraie sauvegarde et des approbations intégrées.
