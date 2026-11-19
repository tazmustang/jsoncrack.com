# Liste SharePoint : `ApprovalRequests`

Créez la liste **avec ce nom exact (en anglais, sans espace ni accent)**.
Les formules Power Apps et Power Automate utilisent ces noms.
**Ne renommez pas les colonnes après leur création.**

| # | Nom de la colonne (exact) | Type SharePoint | Paramètres |
|---|---|---|---|
| 1 | `Title` | (existe déjà, « Titre ») | Obligatoire |
| 2 | `Description` | Plusieurs lignes de texte | Texte brut |
| 3 | `Category` | Choix | Valeurs : `Achat`, `Dépense`, `Congé`, `Formation`, `Autre`. Valeur par défaut : `Autre` |
| 4 | `Amount` | Nombre | 2 décimales, non obligatoire |
| 5 | `Approver` | Personne ou groupe | Personnes uniquement, sélection unique |
| 6 | `Status` | Choix | Valeurs : `En attente`, `Approuvé`, `Rejeté`, `Annulé`. Valeur par défaut : `En attente` |
| 7 | `ApproverComments` | Plusieurs lignes de texte | Texte brut |
| 8 | `DecisionDate` | Date et heure | Inclure l'heure : Oui |
| 9 | `NotificationSent` | Oui/Non | Valeur par défaut : **Non** |

Colonnes automatiques déjà présentes et utilisées :
- `Created By` (Créé par) : le demandeur
- `Created` (Créé) : la date de la demande

## Pourquoi écrire les noms en anglais ?
SharePoint garde pour toujours le **premier nom** donné à une colonne comme nom interne.
Un nom sans accent ni espace évite les noms internes du type `Cat_x00e9_gorie`.
Après coup, vous pouvez traduire l'affichage **de la liste** dans SharePoint. Par contre,
Power Apps utilise le nom d'affichage. Si vous le modifiez, il faudra remplacer ce nom dans toutes les formules.
Le plus simple est de garder les noms anglais.
