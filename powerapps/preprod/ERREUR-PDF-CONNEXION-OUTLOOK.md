---
title: "Erreur du PDF après la migration PréProd : MissingConnectionReference « Office 365 Outlook »"
subtitle: "Flux 3 GenererPDFAppreciation · 9 novembre 2026"
lang: fr-CA
---

# Le message

> Échec de GenererPDFAppreciation.Run : MissingConnectionReference — There was problem connecting to connector 'Office 365 Outlook'.

# La cause (vérifiée dans la solution 1.0.0.8)

Le flux 3 utilise 3 connexions : OneDrive, SharePoint et **Office 365 Outlook**. Outlook sert seulement à la **gestion des erreurs** (courriel au soutien depuis la boîte partagée).

Dans la solution, les 3 connexions du flux 3 sont réglées sur **« Fournie par l'utilisateur exécutant uniquement »** (`runtimeSource: invoker`). Le flux utilise donc les connexions **de la personne qui clique sur Aperçu PDF**, pas celles du compte de service.

L'application a été liée au flux 3 **avant** l'ajout du courriel d'erreur. Elle ne demande donc pas de connexion Outlook à l'utilisateur. Dans l'ancien PréProd, la connexion existait déjà ; dans le nouveau, elle manque : d'où l'erreur.

C'est aussi contraire à ce qui est documenté : le fichier temporaire doit aller dans le OneDrive **du compte de service**, pas dans celui de chaque utilisateur.

# La correction (TI, dans le nouveau PréProd — aucune nouvelle version requise)

1. **make.powerapps.com** › environnement PréProd › **Solutions** › Solution-ApplicationAppréciation.
2. **Références de connexion** : vérifiez que les 3 références ont une connexion **du compte de service**, à l'état **Connecté** :
   - OneDrive Entreprise RHDSSTDAAT-1b68d ;
   - SharePoint RHDSSTDAAT-11da3 ;
   - Office 365 Outlook Gestion_formulaire_approb… (b0245).
3. Ouvrez le flux **GenererPDFAppreciation** › page **Détails**.
4. Encadré **Utilisateurs exécutant uniquement** › **Modifier**.
5. Section **Connexions utilisées** : pour **chacune des 3** connexions, remplacez « Fournie par l'utilisateur exécutant uniquement » par **la connexion du compte de service**.
6. **Enregistrer**.
7. Désactivez, puis réactivez le flux 3.
8. Dans l'application : fermez-la complètement, rouvrez-la, puis testez **Aperçu PDF**.

Si l'étape 5 est grisée (solution gérée), faites la correction ci-dessous.

# Correction permanente (dans la prochaine version 1.0.0.9, bac à sable)

1. Bac à sable › flux **GenererPDFAppreciation** › Détails › **Utilisateurs exécutant uniquement** › Modifier › les 3 connexions = **Utiliser cette connexion** (compte de service) › Enregistrer.
2. Dans Power Apps Studio : **Power Automate** (volet de gauche) › sur GenererPDFAppreciation : **⋯ › Supprimer de l'application**, puis **Ajouter un flux** › GenererPDFAppreciation. Les formules ne changent pas (même nom).
3. Enregistrer, publier, exporter la **1.0.0.9**.

# Vérifications

| Test | Résultat attendu |
|---|---|
| Aperçu PDF, avec votre compte | « PDF créé », bouton « Ouvrir le PDF » |
| Aperçu PDF, avec un testeur qui n'a jamais ouvert l'application | Même chose, **sans** demande de connexion |
| Historique d'exécution du flux 3 | Exécution réussie |
| Flux 2 (courriels d'étape) | Fonctionne toujours : il utilise déjà le compte de service |
