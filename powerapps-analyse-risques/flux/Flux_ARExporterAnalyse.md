# Flux Power Automate « ARExporterAnalyse »

Ce flux remplace le flux HTTP de la version HTML (« RH-DSST - Envoyer analyse SharePoint »).
Il est **appelé directement par l'application Power Apps** (bouton « Envoyer à SharePoint (PDF/Excel) »).

> **Avantage :** le déclencheur « Power Apps (V2) » et les connecteurs SharePoint, OneDrive Entreprise
> et Office 365 Outlook sont tous **standards** : aucune licence Premium n'est requise
> (contrairement au déclencheur « Lors de la réception d'une demande HTTP », qui est Premium).
> Il n'y a plus d'URL à configurer sur chaque poste.

Ce que fait le flux :

1. dépose le fichier **JSON** (même format que l'application HTML) dans la bibliothèque SharePoint ;
2. dépose le fichier **CSV** (s'ouvre dans Excel) dans la bibliothèque ;
3. convertit le rapport HTML en **PDF** (via OneDrive) et le dépose dans la bibliothèque ;
4. envoie un **courriel** aux responsables SST avec le PDF en pièce jointe ;
5. répond à l'application.

---

## Création pas à pas

Dans <https://make.powerautomate.com> (même environnement que l'application) :
**Créer → Flux de cloud instantané → « Lorsque Power Apps appelle un flux (V2) »** (PowerApps V2).
Nom du flux : **`ARExporterAnalyse`** (sans espace : c'est le nom utilisé dans la formule de l'application).

### Étape 1 — Déclencheur « Lorsque Power Apps appelle un flux (V2) »

Ajoutez **4 entrées de type Texte, dans cet ordre exact** (l'ordre doit correspondre à l'appel `ARExporterAnalyse.Run(...)`) :

| # | Nom de l'entrée | Contenu reçu |
|---|-----------------|--------------|
| 1 | `NomFichier`  | ex. `AR_SST_Maintenance_2026-04-15` (sans extension) |
| 2 | `RapportHTML` | rapport complet (entête, synthèse, grille, plan d'action) |
| 3 | `DonneesCSV`  | grille au format CSV (séparateur « ; ») |
| 4 | `DonneesJSON` | analyse au format JSON de l'application HTML |

### Étape 2 — SharePoint « Créer un fichier » (JSON)

- Adresse du site : **RH SST Analyse de risque**
- Chemin d'accès du dossier : la bibliothèque **Analyse de risque** (bouton dossier → sélectionner)
- Nom du fichier : contenu dynamique `NomFichier` puis tapez `.json`
- Contenu du fichier : contenu dynamique `DonneesJSON`

Renommez l'action : **Créer fichier JSON**.

### Étape 3 — SharePoint « Créer un fichier » (Excel / CSV)

- Mêmes site et dossier
- Nom du fichier : `NomFichier` + `.csv`
- Contenu du fichier : `DonneesCSV`

Renommez l'action : **Créer fichier Excel**.

### Étape 4 — OneDrive Entreprise « Créer un fichier » (fichier temporaire)

- Chemin d'accès du dossier : `/AR_Temp` (créez ce dossier dans votre OneDrive au besoin)
- Nom du fichier : `NomFichier` + `.html`
- Contenu du fichier : `RapportHTML`

Renommez l'action : **Créer HTML temporaire**.

### Étape 5 — OneDrive Entreprise « Convertir un fichier »

- Fichier : contenu dynamique **ID** de l'étape « Créer HTML temporaire »
- Type cible : **PDF**

Renommez l'action : **Convertir en PDF**.

### Étape 6 — SharePoint « Créer un fichier » (PDF)

- Mêmes site et dossier qu'aux étapes 2 et 3
- Nom du fichier : `NomFichier` + `.pdf`
- Contenu du fichier : **Contenu du fichier** de l'étape « Convertir en PDF »

Renommez l'action : **Créer fichier PDF**.

### Étape 7 — OneDrive Entreprise « Supprimer un fichier »

- Fichier : **ID** de l'étape « Créer HTML temporaire » (nettoyage du fichier temporaire)

### Étape 8 — Office 365 Outlook « Envoyer un e-mail (V2) »

- À : adresse(s) des responsables SST (séparées par « ; »)
- Objet : `Nouvelle analyse de risques SST : ` + `NomFichier`
- Corps : par exemple
  « Une nouvelle analyse de risques a été déposée dans la bibliothèque *Analyse de risque*
  du site RH SST Analyse de risque. Le rapport PDF est joint. »
- Pièces jointes (Afficher les paramètres avancés) :
  - Nom : `NomFichier` + `.pdf`
  - Contenu : **Contenu du fichier** de l'étape « Convertir en PDF »

### Étape 9 — « Répondre à une application ou à un flux PowerApp »

- Ajoutez une sortie **Texte** nommée `Resultat` avec la valeur `OK`.

**Enregistrez** le flux, puis ajoutez-le à l'application (voir le guide, étape 5).

---

## Dépannage du flux

| Symptôme | Solution |
|----------|----------|
| « ARExporterAnalyse n'est pas reconnu » dans Power Apps | Le flux n'a pas été ajouté à l'application (volet Power Automate → Ajouter un flux) ou il porte un autre nom. |
| Erreur « Le fichier existe déjà » | Une analyse du même service a déjà été envoyée à la même date. Dans chaque action « Créer un fichier » SharePoint, vous pouvez ajouter `_` + `utcNow('HHmmss')` au nom, ou supprimer l'ancien fichier. |
| Accents illisibles dans le CSV | Le fichier commence par un BOM UTF-8 ; ouvrez-le par double-clic dans Excel. Sinon : Excel → Données → À partir d'un fichier texte/CSV → Origine 65001 UTF-8. |
| PDF vide ou mise en page tronquée | Normal pour les grilles très larges : le PDF est en portrait. Le fichier CSV contient toutes les données. |
| Le flux a modifié des entrées après un changement dans Power Apps | Dans Power Apps, volet Power Automate → « … » à côté du flux → **Actualiser**. |
