# SST 360 — plan directeur et outil 5 Pourquoi

| Fichier | Rôle |
|---|---|
| `plan-directeur-sst360.html` | Plan directeur de l'application SST 360 (Power Apps + SharePoint), version 1.1. |
| `outil-5-pourquoi/arbre-5-pourquoi_v3.0.html` | Outil HTML d'analyse des causes (5 Pourquoi, version 3.0). C'est l'outil de référence pour l'onglet Analyse de SST 360. |

## Installation de l'outil 5 Pourquoi

Rien à installer. L'outil tient en un seul fichier et fonctionne sans Internet.

1. Copiez `arbre-5-pourquoi_v3.0.html` sur votre poste, ou dans une bibliothèque SharePoint ou OneDrive.
2. Ouvrez-le avec Edge ou Chrome (double-clic).

## Utilisation

1. Remplissez les **Informations générales** et l'énoncé du **problème** : un fait observable, sans désigner de personne.
2. Dans la **grille de collecte**, cochez les facteurs constatés, puis cliquez sur **Créer les branches Pourquoi** : une branche « Pourquoi 1 » est créée pour chaque facteur coché.
3. Pour creuser une réponse, cliquez sur **+ Pourquoi** sous cette réponse. Un avertissement apparaît si une réponse s'arrête à une « erreur humaine ».
4. Sur la réponse où l'équipe peut réellement agir, cliquez sur **Marquer cause racine**, puis remplissez l'action corrective : description, responsable, échéance et statut.
5. Relisez la section **Causes racines et suivi des actions**. Le **test du « Donc »** permet de vérifier que la chaîne tient debout.
6. Pour garder votre travail :
   - **Enregistrer dans l'historique** conserve l'analyse sur ce poste et dans ce navigateur.
   - **Exporter (JSON)** crée un fichier que vous pouvez partager ou recharger plus tard.
   - **Exporter en PDF** ouvre l'impression ; choisissez alors « Enregistrer au format PDF ».

> L'enregistrement automatique et l'historique restent dans le navigateur du poste. Exportez en JSON avant de changer de poste ou d'effacer les données de navigation.

## Lien avec SST 360

La section 03 du plan directeur explique comment chaque partie de l'outil est reprise dans l'application : grille des facteurs, arbre stocké dans la liste `SST_Pourquoi`, actions des causes racines dans `SST_Actions` et rapport d'enquête PDF.
