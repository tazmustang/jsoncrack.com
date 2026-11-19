# Solution complète de gestion des approbations
### SharePoint + Power Apps + Power Automate

Une application pour soumettre des demandes (achat, dépense, congé…), les faire approuver ou rejeter,
et suivre leur statut. Les courriels sont envoyés automatiquement.

```
 Demandeur ──(Power Apps : nouvelle demande)──► Liste SharePoint « ApprovalRequests »
                                                   │
                       Flux 1 : courriel à l'approbateur ◄─┘
 Approbateur ──(Power Apps : Approuver / Rejeter)──► Liste mise à jour
                                                   │
                       Flux 2 : courriel au demandeur ◄─┘
```

## Contenu du dossier
| Fichier | Rôle |
|---|---|
| `1-sharepoint/liste-ApprovalRequests.md` | Colonnes de la liste SharePoint |
| `2-powerapps/0-App-OnStart.txt` | Formules de l'application (OnStart, écran de démarrage) |
| `2-powerapps/1-scrHome.yaml` | Écran d'accueil : *Mes demandes* / *À approuver*, recherche, filtre |
| `2-powerapps/2-scrNew.yaml` | Formulaire de nouvelle demande |
| `2-powerapps/3-scrDetails.yaml` | Détail, Approuver / Rejeter / Annuler |
| `3-powerautomate/Flux1-Nouvelle-demande.md` | Courriel envoyé à l'approbateur |
| `3-powerautomate/Flux2-Decision.md` | Courriel envoyé au demandeur après la décision |

## Prérequis (gratuit si vous avez Microsoft 365)
- Un compte **Microsoft 365** professionnel ou scolaire (Business Basic/Standard/Premium, E1/E3/E5, A1/A3…).
  Ces plans incluent **Power Apps pour Microsoft 365** et **Power Automate pour Microsoft 365**.
- La solution n'utilise que des **connecteurs standards** (SharePoint, Office 365 Users, Office 365 Outlook) :
  **aucune licence Premium n'est nécessaire**.
- Un site SharePoint où vous pouvez créer une liste (droit *Modifier* ou *Propriétaire*).

---

## ÉTAPE 1 : créer la liste SharePoint (10 min)
1. Ouvrez votre site SharePoint > **+ Nouveau** > **Liste** > **Liste vide**.
2. Nom : **`ApprovalRequests`** > **Créer**.
3. Ajoutez les colonnes de `1-sharepoint/liste-ApprovalRequests.md` avec **+ Ajouter une colonne**.
   Respectez les noms **et** les valeurs de choix exactement (accents compris).
4. Partagez le site avec les utilisateurs (droit *Modifier*). Sinon, ils ne pourront pas créer de demandes.

## ÉTAPE 2 : créer l'application Power Apps (20 min)
1. https://make.powerapps.com > **+ Créer** > **Application vide** > **Application canevas vide**
   - Nom : `Gestion des approbations`, format : **Tablette** > **Créer**.
2. **Données** (icône cylindre) > **+ Ajouter des données** :
   - **SharePoint** > votre site > cochez `ApprovalRequests` > **Se connecter**
   - **Utilisateurs Office 365** (*Office 365 Users*)
3. Dans l'**arborescence**, renommez `Screen1` en **`scrHome`**, puis ajoutez 2 écrans **vides** :
   **`scrNew`** et **`scrDetails`**. Les noms doivent être exacts.
4. Pour chaque écran :
   1. Sélectionnez l'écran dans l'arborescence.
   2. Ouvrez le fichier `.yaml` correspondant, sélectionnez **tout** le texte et copiez-le (Ctrl+A, Ctrl+C).
   3. Dans Power Apps Studio, collez avec **Ctrl+V** ou **clic droit > Coller**. Les contrôles apparaissent avec leurs formules.
5. Sélectionnez **App** dans l'arborescence et collez le contenu de `0-App-OnStart.txt` dans les propriétés
   **OnStart** et **StartScreen**.
6. **Enregistrer** > **Publier** > **Partager** l'application avec les utilisateurs.

## ÉTAPE 3 : créer les 2 flux Power Automate (15 min)
Suivez `3-powerautomate/Flux1-Nouvelle-demande.md`, puis `Flux2-Decision.md`.
Remplacez `COLLEZ_ICI_LE_LIEN_DE_VOTRE_APPLICATION` par le lien web de l'application
(Power Apps > Applications > `...` > Détails).

---

## Utilisation
**Demandeur**
1. Ouvrez l'application > **+ Nouvelle demande**.
2. Remplissez le titre, la catégorie, le montant et la description, puis choisissez l'**approbateur** (tapez son nom).
3. **Envoyer la demande** : l'approbateur reçoit un courriel.
4. L'onglet **Mes demandes** affiche vos demandes et leur statut en couleur
   (orange = en attente, vert = approuvée, rouge = rejetée, gris = annulée).
   Tant qu'une demande est *En attente*, vous pouvez l'annuler depuis son détail.

**Approbateur**
1. Onglet **À approuver** (ou lien dans le courriel).
2. Ouvrez la demande, ajoutez un commentaire et cliquez **Approuver** ou **Rejeter**. Un commentaire est obligatoire pour rejeter.
3. Le demandeur reçoit automatiquement un courriel avec la décision.

---

## Dépannage
| Problème | Solution |
|---|---|
| Le collage du YAML ne fait rien ou affiche une erreur de version | Dans le fichier, retirez le suffixe de version (ex. `Label@2.5.1` → `Label`, `Classic/Button@2.2.0` → `Classic/Button`). Vous pouvez aussi créer le contrôle à la main et copier chaque propriété (`Propriété: =formule`). |
| La galerie ne se colle pas | Insérez une **galerie verticale vide** nommée `galRequests`, puis collez dedans les 4 contrôles du bloc `Children:`. |
| Erreurs de formule en tapant à la main | En Power Apps français, le séparateur d'arguments est `;` et l'enchaînement est `;;`. Les fichiers fournis utilisent la syntaxe anglaise (`,` et `;`). Le collage YAML la convertit automatiquement. |
| « ApprovalRequests introuvable » | La source de données n'est pas ajoutée, ou la liste porte un autre nom. |
| `Status`/`Category` en erreur | Les valeurs de choix doivent être identiques à celles de la liste (`En attente`, `Approuvé`, `Rejeté`, `Annulé`). |
| Le flux 2 s'exécute en boucle | La condition de déclenchement est absente ou mal collée. |
| Avertissement de délégation (triangle jaune) | Sans gravité sous 2000 demandes par personne. Vous pouvez monter la limite dans Paramètres > Général > *Limite de lignes de données* (max 2000). |

## Améliorations possibles
- Approbation à 2 niveaux : ajoutez une colonne `Approver2` et un statut `En attente niveau 2`.
- Approbation depuis Teams/Outlook : voir l'option à la fin de `Flux2-Decision.md`.
- Pièces jointes : activez les pièces jointes de la liste et ajoutez un contrôle *Pièces jointes* via un formulaire.
