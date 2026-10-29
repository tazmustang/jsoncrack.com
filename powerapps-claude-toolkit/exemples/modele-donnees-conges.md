# Modèle de données — Exemple « Demandes de congés »

## Source : `DemandesConges`

- **Type** : Liste SharePoint
- **Emplacement** : https://votreentreprise.sharepoint.com/sites/RH
- **Rôle** : une ligne = une demande de congé
- **Volume** : ~300 lignes/an

| Nom affiché | Nom interne | Type | Obligatoire | Valeurs / remarques |
|---|---|---|---|---|
| Titre | `Title` | Texte | Oui | Motif court (« Vacances d'été ») |
| Type de congé | `TypeConge` | Choix | Oui | Vacances, Maladie, Personnel, Formation |
| Date de début | `DateDebut` | Date | Oui | |
| Date de fin | `DateFin` | Date | Oui | ≥ DateDebut |
| Nombre de jours | `NbJours` | Nombre | Oui | calculé dans l'app (jours ouvrables) |
| Statut | `Statut` | Choix | Oui | Soumis, Approuvé, Refusé |
| Commentaire du gestionnaire | `CommentaireGestionnaire` | Texte multiligne | Non | obligatoire si Refusé |
| Créé par | `Author` | Personne (système) | — | demandeur |
| Créé | `Created` | Date (système) | — | |

**Permissions** : tout le monde crée ; chaque employé voit ses demandes ; les gestionnaires voient tout.

## Utilisateurs et rôles

| Rôle | Qui | Droits |
|---|---|---|
| Employé | Tous | Créer, voir ses demandes, annuler une demande « Soumis » |
| Gestionnaire | Membres du groupe SharePoint « Gestionnaires RH » | Approuver / refuser avec commentaire |

## Connecteurs

- Office 365 Users (nom et photo) — standard
- Office 365 Outlook (courriel au demandeur après décision) — standard
