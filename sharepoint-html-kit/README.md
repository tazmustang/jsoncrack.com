# Kit « Page HTML dans SharePoint » — Guide complet

Ce kit rassemble ce qu'il faut savoir pour créer une **page HTML dans SharePoint Online**, la nouvelle fonctionnalité dont parlent les publications LinkedIn (Ami Diamond, Gemma Saint, Stefan Bauer, Therman Trotman, etc.), avec les solutions aux **liens qui ne fonctionnent pas**.

Tout est **gratuit** et ne demande **aucune installation** : deux fichiers HTML s'ouvrent par double-clic dans Edge ou Chrome.

| Fichier | Rôle |
|---|---|
| `README.md` | Ce guide : recherche, règles, installation, utilisation, dépannage |
| `modele-page-sharepoint.html` | Modèle de page d'accueil prêt à personnaliser et à téléverser |
| `verificateur-html-sharepoint.html` | Outil local : vérifie un fichier HTML avant téléversement, corrige les liens, convertit les images en base64 |

> ⚠️ La fonctionnalité est en **préversion publique depuis début octobre 2026** et sa disponibilité générale est prévue **de mi-novembre à fin décembre 2026** (message MC1479517). Certains détails ci-dessous peuvent encore changer : testez toujours dans votre locataire.

---

## 1. Ce qu'est la fonctionnalité

- Une page HTML est un **fichier `.html` stocké dans la bibliothèque « Pages du site » (Site Pages)**, à côté des pages `.aspx` classiques. On peut la modifier, la publier et la partager comme une page normale.
- Trois façons d'en créer une :
  1. **+ Nouveau › Page HTML** sur le site ;
  2. le **bouton Copilot flottant** du site, ou **+ Créer** dans la page d'accueil « Publier » ;
  3. **téléverser** un fichier HTML existant (ou un **dossier HTML** contenant la page et ses fichiers).
- **Licences** : créer ou modifier avec Copilot exige une licence **Microsoft 365 Copilot**. **Téléverser, publier et consulter ne l'exigent pas.** C'est donc gratuit pour vous si vous écrivez le HTML vous-même (ou avec ce kit).
- **Permissions** : publier ne donne **aucun** droit supplémentaire. Seules les personnes qui voient déjà le site verront la page.

### Comment SharePoint affiche la page (le point clé)

SharePoint affiche votre HTML dans un **iframe « bac à sable » (sandbox)**, isolé de l'en-tête, du pied de page et de la navigation SharePoint. Comme le rappelle Stefan Bauer dans les commentaires : *« C'est le comportement standard d'un iframe sandbox… pas de HTML intégré au DOM de SharePoint. »* Presque toutes les « bizarreries » (liens, scripts, polices) découlent de cela.

---

## 2. Ce qui fonctionne / ce qui ne fonctionne pas

| Élément | Statut | Quoi faire |
|---|---|---|
| CSS dans `<style>` ou `style="…"` | ✅ Fonctionne | Mettez tout le CSS dans le fichier |
| `<link rel="stylesheet" href="…">` | ❌ Bloqué | Copiez le CSS dans `<style>` |
| JavaScript dans `<script>…</script>` du même fichier | ✅ Fonctionne | |
| Script depuis un CDN (jQuery, Bootstrap, etc.) | ❌ Bloqué | Copiez le code dans le fichier ou réécrivez en JS simple |
| Chart.js, Mermaid, React, Fluent UI, Babylon | ⚠️ Prévu, via un CDN géré par Microsoft | Référence exacte encore peu documentée : testez |
| `fetch()`, AJAX, API REST/Graph SharePoint | ❌ Bloqué | Écrivez les données directement dans le fichier |
| `localStorage`, `sessionStorage`, cookies | ❌ Bloqué | |
| Google Fonts / polices web externes | ❌ Bloqué | Utilisez les polices système (`"Segoe UI", system-ui, Arial`) |
| Images en **base64** (`data:image/…`) | ✅ Fonctionne | Outil n° 2 du vérificateur |
| Images du **même domaine** SharePoint | ⚠️ Selon Microsoft oui ; certains testeurs disent non | Testez, sinon base64 |
| Images d'un autre site | ⚠️ Résultats contradictoires | Base64 recommandé |
| Ancres internes (`href="#section"`) | ✅ Fonctionne | Idéal pour un menu |
| Formulaires qui envoient des données | ❌ | Lien vers Microsoft Forms |
| Taille maximale du fichier | 10 Mo | Attention aux images base64 |
| Accès à la page SharePoint parente (`window.top`) | ❌ | |

Il est également question, chez certains testeurs, d'une capacité à **pré-charger des données de listes SharePoint** (jusqu'à 100 000 éléments par source) au moment de l'affichage, en lecture seule. Ce mécanisme passe par Copilot et n'est pas encore documenté publiquement : ne comptez pas dessus pour l'instant.

---

## 3. Installation (activer la fonctionnalité sur votre site)

1. La fonctionnalité est **activée par défaut** pendant le déploiement ; aucune action de l'administrateur Microsoft 365 n'est requise.
2. Si l'option **+ Nouveau › Page HTML** ou le téléversement de fichiers `.html` n'apparaît pas, un propriétaire du site doit l'autoriser :
   - ouvrir le site › **Contenu du site** › **Pages du site** (Site Pages) ;
   - menu **Types de fichiers** (File types) › activer **Autoriser les fichiers HTML** (Allow HTML files).
3. Si rien n'apparaît toujours, votre locataire n'a pas encore reçu la préversion : attendez le déploiement (au plus tard fin décembre 2026).

## 4. Les liens : pourquoi certains fonctionnent et d'autres non

Synthèse de la vidéo d'Ami Diamond et du billet Microsoft Tech Community « SharePoint HTML Page Links Not Working? » :

| Type de lien | Fonctionne par défaut ? |
|---|---|
| Lien vers le **même site** | ✅ Oui |
| Lien vers un autre site du **même locataire** (`*.sharepoint.com` de votre organisation) | ✅ Oui |
| Navigation **entre pages** / ancres dans la page | ✅ Oui |
| Lien vers un **autre locataire Microsoft 365** | ❌ Non, à autoriser |
| Lien **hors de SharePoint** (site Web externe) | ❌ Non, à autoriser |

Message typique d'un lien bloqué : *« ne peut pas être ouvert, car votre organisation n'autorise pas l'accès à ce site »*. C'est exactement le problème décrit par Nathan Thorndyke (« les liens externes s'affichent correctement mais ne s'ouvrent pas »).

### Solution 1 : autoriser le domaine (administrateur ou propriétaire du site)

1. Sur le site : **roue dentée ⚙️ › Informations sur le site › Afficher tous les paramètres du site**.
2. Section **Administration de la collection de sites** › **Sécurité des champs HTML** (HTML Field Security).
3. Choisir **Autoriser les contributeurs à insérer des iframes uniquement à partir des domaines suivants**, puis ajouter chaque domaine **sans `https://`** (ex. `learn.microsoft.com`, `www.youtube.com`).
4. Enregistrer, puis **actualiser** la page HTML.

Astuce : le vérificateur du kit dresse automatiquement la liste des domaines externes de votre page, prête à copier.

### Solution 2 : bien écrire les liens dans le HTML

- Les liens qui quittent la page : **`target="_blank" rel="noopener"`** (nouvel onglet). Dans un iframe isolé, `target="_top"` / `_parent` sont souvent bloqués, et selon certains testeurs, tous les liens s'ouvrent de toute façon dans un nouvel onglet.
- Utilisez des **URL complètes** (`https://votre-locataire.sharepoint.com/sites/…`) plutôt que des chemins relatifs (`../page.html`), sauf si vous avez testé ces derniers après téléversement d'un dossier complet.
- Pas de liens `javascript:` ni de `window.open()`.
- Le bouton **« Corriger les liens et télécharger »** du vérificateur applique ces règles automatiquement.

### Diagnostiquer un lien qui ne marche pas

1. Appuyez sur **F12** › onglet **Console**, puis cliquez sur le lien.
2. Un message contenant *« sandboxed »* ou *« allow-top-navigation »* signifie que la cible du lien est à remplacer par `target="_blank"`.
3. Un message *« votre organisation n'autorise pas… »* signifie qu'il faut ajouter le domaine (Solution 1).
4. Procédez comme Mimoh Joshi le recommande : classez le lien (même site / même locataire / autre locataire / externe), puis appliquez la règle correspondante.

---

## 5. Utilisation du kit, pas à pas

### Étape 1 : personnaliser le modèle

1. Ouvrez `modele-page-sharepoint.html` dans un éditeur de texte (Bloc-notes fonctionne ; **Visual Studio Code**, gratuit, est plus confortable).
2. Cherchez **`À MODIFIER`** et remplacez :
   - les couleurs dans `:root` (votre charte graphique) ;
   - les titres et textes ;
   - **`VOTRE-LOCATAIRE`** et **`VOTRE-SITE`** dans les liens ;
   - les tableaux `indicateurs` et `projets` dans le `<script>` en bas du fichier (vos données).
3. Double-cliquez sur le fichier pour l'aperçu dans votre navigateur.

Le modèle contient : en-tête, menu d'ancres collant, cartes « outils », indicateurs et barres de progression (sans bibliothèque), onglets accessibles au clavier, liens de démonstration de chaque type, FAQ dépliable.

### Étape 2 : ajouter des images

1. Ouvrez `verificateur-html-sharepoint.html`, section **2. Convertir une image en base64**.
2. Choisissez l'image, saisissez un **texte alternatif**, cliquez **Copier la balise `<img>`** et collez-la dans votre page.
3. Gardez les images légères (moins de 300 Ko chacune). Pour les réduire gratuitement : <https://squoosh.app>.

### Étape 3 : vérifier

1. Dans le vérificateur, section **1**, glissez votre fichier HTML.
2. Corrigez les éléments **rouges (bloquants)**. Les éléments orange sont à tester.
3. Au besoin, cliquez sur **Corriger les liens et télécharger** pour obtenir `votre-page-corrige.html`.
4. Copiez la liste des **domaines externes** et transmettez-la au propriétaire du site (section 4, Solution 1).

> Le vérificateur fonctionne **hors ligne** : vos fichiers ne quittent jamais votre ordinateur.

### Étape 4 : téléverser et publier

1. Site SharePoint › **Pages** (ou Contenu du site › Pages du site).
2. **Charger › Fichiers**, puis choisissez votre `.html`. Pour une page avec fichiers annexes, utilisez **Charger › Dossier** en conservant la structure.
3. Ouvrez la page, vérifiez l'affichage et **testez chaque lien**.
4. Cliquez sur **Publier**. Pour la mettre en avant, ajoutez-la à la navigation du site ou définissez-la comme page d'accueil (… › Définir comme page d'accueil), après test.

### Étape 5 (facultative) : avec Copilot (licence requise)

Exemples de requêtes à adapter :

```
Crée une page HTML de lancement pour la campagne « Bien-être d'automne » :
bannière, 3 cartes d'activités, calendrier, FAQ. Couleurs #0f6cbd et #e3008c.
Tout le CSS et le JavaScript dans le fichier, aucune ressource externe,
polices système uniquement, titres sémantiques, texte alternatif sur chaque image,
contraste d'au moins 4,5:1, liens externes avec target="_blank".
```

```
Modifie cette page : ajoute une section « Contacts » en grille de 4 cartes,
et un menu d'ancres en haut vers chaque section.
```

Copilot n'applique pas automatiquement le thème du site : précisez toujours couleurs et polices, puis repassez le fichier au vérificateur.

---

## 6. Bonnes pratiques et gouvernance

- **Quand utiliser une page HTML ?** Pour des pages qui doivent se démarquer : campagnes, lancements de projets, événements saisonniers, tableaux de bord visuels (avis de Gemma Saint). Pour l'intranet courant, les **pages SharePoint modernes** restent plus simples à maintenir (Therman Trotman : « SharePoint Pages gère très bien les liaisons »).
- **À utiliser avec parcimonie**, et documentez pourquoi une page est en HTML.
- **Désignez un responsable** par page HTML : seul quelqu'un qui connaît un peu le HTML pourra la modifier en dehors de Copilot.
- **Données** : la page est statique ; mettez à jour les chiffres manuellement (tableaux en haut du `<script>`) et indiquez la date de mise à jour en pied de page.
- **Accessibilité** : `lang="fr"`, un seul `<h1>`, titres hiérarchisés, `alt` sur les images, contraste suffisant, navigation possible au clavier (le modèle respecte tout cela).
- **Mobile** : testez dans l'application SharePoint mobile ; le modèle est adaptatif.
- **Sécurité** : les propriétaires de site peuvent désactiver « Autoriser les fichiers HTML » sur les sites sensibles. N'autorisez dans « Sécurité des champs HTML » que les domaines de confiance.

---

## 7. Dépannage rapide

| Symptôme | Cause probable | Solution |
|---|---|---|
| Pas d'option « Page HTML » ni de téléversement `.html` | Fichiers HTML non autorisés ou préversion pas encore reçue | Section 3 |
| Le style ne s'applique pas | `<link rel="stylesheet">` externe | CSS dans `<style>` |
| Police différente de celle prévue | Police web externe bloquée | Polices système |
| Script/graphique absent | Bibliothèque CDN bloquée | JS dans le fichier (le modèle dessine les graphiques en CSS) |
| Lien externe visible mais ne s'ouvre pas | Domaine non autorisé | Section 4, Solution 1 |
| Lien qui ne fait rien, erreur « sandboxed » (F12) | `target="_top"`/`_self` | `target="_blank"` |
| Image cassée | Image externe ou chemin relatif | Base64 |
| Téléversement refusé | Fichier > 10 Mo | Réduire les images |
| Données jamais à jour | `fetch()` bloqué | Données dans le fichier |

---

## 8. Sources

- Microsoft Support : [Create, upload, edit, and publish HTML pages in SharePoint](https://support.microsoft.com/en-us/sharepoint/create-edit-publish-html-pages)
- Microsoft 365 Message Center : [MC1479517 – SharePoint: HTML pages](https://mc.merill.net/message/MC1479517)
- Microsoft Tech Community : [SharePoint HTML Page Links Not Working? Here's How to Fix Them!](https://techcommunity.microsoft.com/discussions/sharepoint_general/sharepoint-html-page-links-not-working-heres-how-to-fix-them/4563424)
- HubSite 365 : [SharePoint: Fix Broken HTML Page Links](https://www.hubsite365.com/en-ww/crm-pages/sharepoint-html-page-links-not-working-heres-how-to-fix-them.htm)
- spdenis : [SharePoint HTML pages, what they can and cannot do](https://spdenis.com/sharepoint-html-pages-what-they-can-and-cannot-do/)
- Fivenumber : [SharePoint HTML Pages: What Actually Works Today](https://www.fivenumber.com/sharepoint-html-pages-are-coming-here-is-what-actually-works-today/)
- erik365 : [SharePoint gets HTML pages support](https://erik365.blog/2026/09/28/sharepoint-gets-html-pages-support/)
- PnP : [SharePoint HTML Pages Are Here](https://pnp.github.io/blog/post/sharepoint-html-pages-are-here/)
- NextM365 : [SharePoint HTML Pages: Roadmap 569208 Explained](https://nextm365.com/blog/sharepoint-html-pages-roadmap-569208)
- Vantage365 : [SharePoint HTML Pages: What's Changing in 2026](https://vantage365.com/sharepoint-html-pages/)
- SharePoint Diary : [Configure HTML Field Security in SharePoint Online](https://www.sharepointdiary.com/2018/04/html-field-security-in-sharepoint-online.html)
- Stefan Bauer : [Mythbusting: Image Accessibility in SharePoint](https://n8d.at/mythbusting-image-accessibility-in-sharepoint/)
- Microsoft Support : [Add accessible content and links to a SharePoint Online site](https://support.microsoft.com/en-us/accessibility/sharepoint/add-accessible-content-and-links-to-a-sharepoint-online-site)
