---
title: "Modifications des libellés — « Directeur de service » et « Confirmation »"
subtitle: "Application Appréciation de la contribution (SRHVQ) · 5 novembre 2026 · 30 minutes"
lang: fr-CA
---

# La règle d'or

On change **seulement les textes affichés**.

**Ne changez pas** la valeur **« Certifié »** du statut : ni dans la colonne Statut de SharePoint, ni dans les formules (`Statut.Value = "Certifié"`), ni dans le flux 2 (cas « Certifié »). C'est une valeur **technique** utilisée par la barre d'étapes, le filtre « À approuver par moi » et les courriels. La changer briserait le circuit. À l'écran et dans le PDF, elle s'affichera **« Confirmé »**.

# 1. Les textes de la section G (avec la loupe)

Pour chaque ligne : cliquez sur la **loupe 🔍** (barre de gauche du studio), tapez le **début du texte actuel**, cliquez sur le résultat, puis remplacez le texte dans la barre fx. **Gardez les guillemets.**

| Texte actuel | Nouveau texte |
|---|---|
| Section G — Certification et chaîne d'approbation | **Section G — Confirmation et chaîne d'approbation** |
| Avant la certification — aviser le supérieur immédiat | **Aviser le supérieur** |
| Personne en appréciation — certification d'accord | **Personne en appréciation — confirmation** |
| Je certifie avoir pris connaissance du contenu de ce formulaire et je confirme mon accord. | **Je confirme avoir pris connaissance du contenu de ce formulaire et je l'approuve.** |
| ✓ Certifier et soumettre | **✓ Approuver et soumettre** |
| Une approbation du directeur / de la directrice est requise (personne différente du supérieur hiérarchique) | **Une approbation du directeur / de la directrice de service est requise (personne différente du supérieur hiérarchique)** |
| Directeur / directrice (titre de la carte du directeur, dans la section G) | **Directeur / directrice de service** |

Puis cherchez aussi **« certif »** et **« directeur »** avec la loupe, pour trouver les autres textes : messages (Notify), aide « Comment remplir » (aideHtml), info-bulles, etc. Remplacez :
- certifier → **approuver et soumettre** ;
- certification → **confirmation** ;
- directeur / directrice → **directeur / directrice de service**.

> ⚠️ Avec la loupe, ne touchez **pas** aux résultats qui contiennent `"Certifié"` dans une **condition** (ex. `Statut.Value = "Certifié"`, `{Value: "Certifié"}`) : ce sont des valeurs techniques.

# 2. Les formules à recoller ou à modifier

| Où | Quoi faire |
|---|---|
| **scrFormulaire › OnVisible** | Recollez **scrFormulaire-OnVisible-corrige.txt**. Le rôle s'affiche maintenant « Directeur / directrice de service » dans le menu « Vous êtes » |
| **Barre d'étapes** (galEtapes › Items) | Recollez la formule de **barre-etapes-formules.txt** : « **Confirmé** (personne en appréciation) » et « Approuvé (**directeur de service**) » |
| **btnApercuPDF › OnSelect** | Recollez **btnApercuPDF-OnSelect.txt** : titre de la section G, « Directeur / directrice de service », « Confirmation et approbation (personne en appréciation) », statut affiché « Confirmé » |
| **cellRole › Text** (Mes dossiers, colonne « Mon rôle ») | Remplacez `"Directeur / directrice"` par `"Directeur / directrice de service"` |
| **statutPillLabel › Text** (Mes dossiers, pastille du statut) | `Substitute(Coalesce(ThisItem.Statut.Value; "Brouillon"); "Certifié"; "Confirmé")` |
| **Pastille du statut dans le formulaire** (en haut, à côté du type de poste) | Même idée : entourez la formule actuelle de `Substitute( … ; "Certifié"; "Confirmé")` |
| **btnDeposer** (validation) | Le message « Directeur ou directrice » devient « **Directeur ou directrice de service** » (FORMULES-CONFORMITE.txt, section C4) |

**Enregistrer**, puis **Publier**.

# 3. Les courriels (flux 2 « Appréciation – Suivi des étapes »)

| Cas du flux | Texte actuel | Nouveau texte |
|---|---|---|
| **Certifié** (corps) | … a certifié son formulaire. C'est maintenant votre étape… | … **a confirmé et approuvé** son formulaire. C'est maintenant votre étape… |
| **Approuvé SH** (corps) | … attend votre approbation (directeur ou directrice). | … attend votre approbation (**directeur ou directrice de service**). |

Le **nom du cas** « Certifié » ne change pas (valeur technique). Textes complets : FLUX-FINAUX.txt, flux 2.

# 4. Vérifier

| ✔ | À l'écran | Attendu |
|---|---|---|
| ☐ | Menu « Vous êtes » | Directeur / directrice de service |
| ☐ | Section G | Titre « Confirmation et chaîne d'approbation », « Aviser le supérieur », « Personne en appréciation — confirmation », « Je confirme… et je l'approuve », bouton « Approuver et soumettre » |
| ☐ | Barre d'étapes | Confirmé (personne en appréciation) · Approuvé (directeur de service) |
| ☐ | Mes dossiers, après « Approuver et soumettre » | Pastille « **Confirmé** » ; le SI voit le dossier dans « À approuver par moi » (preuve que la valeur technique est intacte) |
| ☐ | PDF | Section G « Confirmation et chaîne d'approbation » ; « Directeur / directrice de service » |
| ☐ | Courriel au SI après la confirmation | « … a confirmé et approuvé son formulaire » |

# 5. Les documents déjà mis à jour

Guide d'utilisation, message d'annonce, courriels automatiques, fiche résumé, scénario vidéo, schémas opérationnels, présentation, charte graphique.

**À noter :** dans la **liste SharePoint**, la colonne Statut continue d'afficher « Certifié » (valeur technique). Si vous voulez l'afficher autrement dans SharePoint, ajoutez une mise en forme de colonne plus tard. Ce n'est pas nécessaire.
