# Design brief — Demandes de congés

*Exemple de livrable produit par le skill `pa-design-brief`.*

## 1. Objectif
Remplacer les demandes de congés par courriel par une application unique.
Succès : 100 % des demandes passent par l'app ; décision du gestionnaire en moins de 48 h ;
plus aucun fichier Excel de suivi.

## 2. Utilisateurs et rôles
| Rôle | Appareil | Droits |
|---|---|---|
| Employé | PC / tablette | Créer, consulter ses demandes, annuler une demande « Soumis » |
| Gestionnaire | PC | Voir toutes les demandes, approuver / refuser avec commentaire |

## 3. Sources de données
| Source | Type | Utilisation |
|---|---|---|
| `DemandesConges` | SharePoint | lecture, création, modification (statut), suppression (annulation) |
| `Office365Users` | Connecteur | lecture (nom, photo) |
| `Office365Outlook` | Connecteur | envoi d'un courriel après décision |

Colonnes : `Title`, `TypeConge`, `DateDebut`, `DateFin`, `NbJours`, `Statut`,
`CommentaireGestionnaire`, `Author`, `Created`.
Délégation : filtre par `Author.Email` et `Statut.Value` → délégable.

## 4. Écrans
**scrAccueil**
- But : voir mes demandes (employé) ou toutes les demandes (gestionnaire).
- Contenu : en-tête (titre, bouton « Nouvelle demande »), filtre par statut, galerie triée par date
  de création décroissante (type, dates, nb jours, badge statut coloré), état vide.
- Navigation : → scrDemande (nouvelle) ; → scrDetail (clic sur une ligne).

**scrDemande**
- But : créer une demande.
- Contenu : titre, type (liste), dates début/fin, nombre de jours calculé (lecture seule),
  boutons Annuler / Envoyer.
- Navigation : ← scrAccueil.

**scrDetail**
- But : consulter une demande ; décider (gestionnaire) ; annuler (employé).
- Contenu : toutes les informations, zone commentaire + boutons Approuver / Refuser (gestionnaire,
  statut Soumis), bouton Annuler la demande (employé, statut Soumis).
- Navigation : ← scrAccueil.

## 5. Parcours utilisateur
1. L'employé ouvre l'app → voit ses demandes.
2. « Nouvelle demande » → remplit le formulaire → Envoyer → notification de succès → retour à l'accueil.
3. Le gestionnaire ouvre l'app → filtre « Soumis » → ouvre une demande → Approuver ou Refuser
   (commentaire) → courriel envoyé au demandeur.

## 6. Règles métier et validations
- R1 : Date de fin ≥ date de début (message « La date de fin doit suivre la date de début »).
- R2 : Nombre de jours = jours ouvrables (lundi-vendredi) entre les deux dates incluses.
- R3 : Bouton Envoyer désactivé tant que titre, type et dates ne sont pas remplis.
- R4 : Refus impossible sans commentaire.
- R5 : Seules les demandes « Soumis » peuvent être annulées ou décidées.

## 7. Design
Tablette 1366 × 768, palette et nommage des standards. Badges : Soumis = orange,
Approuvé = vert, Refusé = rouge.

## 8. Hors périmètre (v1)
Solde de congés, calendrier d'équipe, jours fériés, pièces jointes.

## 9. Questions ouvertes / hypothèses
- Hypothèse : le rôle gestionnaire est déterminé par l'appartenance au groupe « Gestionnaires RH ».
