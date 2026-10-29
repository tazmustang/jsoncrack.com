# Modèle de données — À REMPLIR

> Ce fichier décrit vos sources de données à Claude. C'est **le fichier le plus important** : sans lui,
> Claude invente des noms de colonnes et les formules ne fonctionnent pas.
> Dupliquez la section « Source » autant de fois que nécessaire, puis ajoutez ce fichier aux
> **Connaissances** de votre projet Claude. Un exemple complet est dans `exemples/modele-donnees-conges.md`.

## Astuce : récupérer les noms internes des colonnes

- **SharePoint** : Paramètres de la liste → cliquez sur une colonne → le nom interne est à la fin de
  l'URL (`...&Field=NomInterne`). Les espaces deviennent `_x0020_`.
- **Dataverse** : make.powerapps.com → Tables → votre table → Colonnes → colonne « Nom logique ».
- **Power Apps Studio** : dans une formule, tapez `NomSource.` et regardez l'autocomplétion.
- **Plus rapide** : dans Studio, ajoutez une galerie liée à la source, puis copiez la liste des champs
  proposés dans le panneau Données.

---

## Source : `NOM_EXACT_DE_LA_SOURCE`

- **Type** : Liste SharePoint / Table Dataverse / Excel (OneDrive) / Collection locale
- **Emplacement** : URL du site SharePoint ou environnement Dataverse
- **Rôle dans l'application** : (ex. « une ligne = une demande »)
- **Volume approximatif** : (ex. 500 lignes, +50/mois) → important pour la délégation

| Nom affiché | Nom interne (à utiliser dans les formules) | Type | Obligatoire | Valeurs possibles / remarques |
|---|---|---|---|---|
| Titre | `Title` | Texte (une ligne) | Oui | |
| Statut | `Statut` | Choix | Oui | Brouillon, Soumis, Approuvé, Refusé |
| Demandeur | `Demandeur` | Personne | Oui | |
| Date de début | `DateDebut` | Date | Oui | |
| Montant | `Montant` | Nombre | Non | 2 décimales |
| Projet | `Projet` | Recherche (Lookup) → `Projets` | Non | |

**Relations** : (ex. `Demandes.Projet` → `Projets.ID`)

**Règles de sécurité / permissions** : (ex. chacun ne voit que ses demandes ; les gestionnaires voient tout)

---

## Utilisateurs et rôles

| Rôle | Qui | Ce qu'il peut faire |
|---|---|---|
| Employé | Tous | Créer et voir ses demandes |
| Gestionnaire | Groupe « Gestionnaires » | Approuver / refuser |

## Connecteurs supplémentaires

- Office 365 Users (photo, nom, gestionnaire) — standard
- Office 365 Outlook (courriels) — standard
- Power Automate (flux : …)
