---
title: "Votre solution et le risque OneDrive — Analyse et actions"
subtitle: "Application Appréciation de la contribution (SRHVQ) · 30 octobre 2026"
lang: fr-CA
---

# 1. Ce que montre votre solution

La solution contient **15 objets** : 1 application, 3 flux, 5 variables d'environnement et **6 références de connexion**. Il n'en faudrait que 4.

| Référence de connexion | Âge | Probablement | Action |
|---|---|---|---|
| SharePoint Appreciations | 3 jours | Celle du projet ✔ | Garder |
| Outlook Appreciations | 3 jours | Celle du projet ✔ | Garder |
| Utilisateurs Office 365 Appreciations | 3 jours | Celle du projet ✔ | Garder |
| **OneDrive Entreprise RHDSSTDAAT-1b68d** | 1 an | Utilisée par le **flux 3** (conversion PDF) | Garder : c'est la seule référence OneDrive |
| **SharePoint RHDSSTDAAT-11da3** | 1 an | Ancien projet ; peut-être utilisée par une action du flux 3 | Vérifier (ci-dessous) |
| **Office 365 Outlook Gestion_formulaire_approb…** | 4 mois | Ancien projet (formulaire d'approbation) | Vérifier (ci-dessous) |

**Pourquoi c'est important :** à l'import, les TI doivent choisir une connexion du compte de service **pour chacune** des références. Des références inutiles compliquent l'import et peuvent créer de la confusion.

## Vérifier qui utilise chaque référence (10 minutes)

1. Dans la solution, cliquez sur le flux **GenererPDFAppreciation** (le nom, pas les ⋯) : la page **Détails** du flux s'ouvre.
2. Repérez la section **Références de connexion** : elle liste celles que le flux utilise.
3. Faites de même pour les 2 autres flux.

**Si une ancienne référence n'est utilisée par AUCUN flux :**

1. ⋯ à côté de la référence.
2. **Supprimer de cette solution**.

> ⚠️ **Jamais « Supprimer de cet environnement »** : la référence sert peut-être encore à votre ancien projet.

**Si « SharePoint RHDSSTDAAT-11da3 » est utilisée par le flux 3 :** ce n'est pas bloquant, les TI y brancheront le compte de service. Pour simplifier :

1. Ouvrez le flux 3 en **Modifier**.
2. Sur chaque action SharePoint (Pièces jointes, Supprimer la pièce jointe, Ajouter PDF) : **⋯ › Connexions**, choisissez **SharePoint Appreciations**.
3. **Enregistrez**, puis retirez l'ancienne référence de la solution.

**Pour la demande déjà envoyée**, indiquez aux TI les références à brancher sur le compte de service.

# 2. Les flux et OneDrive : y a-t-il un risque d'erreur ?

**Oui, mais il est faible et surtout lié à un point à vérifier par les TI.** Le flux 3 utilise OneDrive comme espace de travail temporaire. Il y crée un fichier .html, le convertit en PDF, joint le PDF au dossier, puis supprime le .html. La conversion en PDF n'existe que dans le connecteur OneDrive Entreprise, d'où son utilisation.

Les flux 1 et 2 **n'utilisent pas OneDrive** : aucun risque de ce côté.

| Risque | Probabilité | Ce qui arriverait | Prévention |
|---|---|---|---|
| **1. Le compte de service n'a pas de OneDrive** (pas de licence, ou jamais ouvert) | **Le plus probable**, si le compte de service est récent | Le flux 3 échoue à « Créer un fichier » ; l'application affiche « Le PDF n'a pas pu être créé » | **Demander aux TI** : le compte de service a une licence avec OneDrive, et son OneDrive a été **ouvert au moins une fois** (initialisé) |
| 2. Deux personnes produisent le PDF **du même dossier** à la même seconde | Très faible | Conflit de nom du fichier temporaire | Nom temporaire unique (voir 2.1) |
| 3. Le .html temporaire n'est pas supprimé si la conversion échoue | Faible | Un petit fichier reste dans le OneDrive du compte de service | Le courriel d'erreur avertit le soutien ; nettoyage au besoin |
| 4. La conversion prend plus de 2 minutes | Très faible (10 à 30 s d'habitude) | L'application affiche « Le PDF n'a pas pu être créé » | Réessayer |
| 5. Limites de débit du connecteur, en période de pointe | Faible | Ralentissement ou échec ponctuel | Aucune action ; à surveiller avec les courriels d'erreur |

Aucun de ces risques ne touche les **données** : le dossier n'est jamais modifié par le flux 3. Seul le PDF ne serait pas produit, et on peut réessayer.

## 2.1 Petite amélioration recommandée : un nom temporaire unique

Dans le flux 3, action **Créer un fichier** (OneDrive), champ **Nom de fichier** : remplacez le contenu par cette **expression** (onglet fx) :

```
concat(triggerBody()?['text'], '-', guid(), '.html')
```

Le nom du **PDF joint au dossier** ne change pas : il est fixé par l'action « Ajouter PDF ». La suppression du fichier temporaire utilise son **Id** : rien d'autre à changer.

## 2.2 À ajouter dans votre courriel aux TI

> Le flux GenererPDFAppreciation utilise OneDrive Entreprise (création d'un fichier temporaire, puis conversion en PDF). Merci de confirmer que le **compte de service** utilisé pour les connexions a une **licence incluant OneDrive** et que son **OneDrive est initialisé**. Les références de connexion à brancher sur le compte de service sont : SharePoint Appreciations, Outlook Appreciations, Utilisateurs Office 365 Appreciations, OneDrive Entreprise RHDSSTDAAT-1b68d *[+ SharePoint RHDSSTDAAT-11da3 et Office 365 Outlook Gestion_formulaire… si elles restent dans la solution]*.

# 3. Votre formulaire de demande

| Champ | Votre réponse | Commentaire |
|---|---|---|
| Type | Mise en PréProd (nouvelle appli) | ✔ |
| Acronyme | SRHVQ | ✔ Tous les documents utilisent maintenant SRHVQ |
| Date souhaitée | 6 novembre 2026 | Serré pour un lancement le 9 : prévoir le scénario pilote |
| Pièces jointes | Solution 1.0.0.1, Excel, schémas, demande | ✔ Si vous ré-exportez avant l'import, remplacez le .zip (voir le pas à pas du site, dernière partie) |
| Commentaires | « J'ai indiqué Bruno… » | Ajoutez le texte de la section 2.2 |
