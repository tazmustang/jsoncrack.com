# Flux Power Automate de l'application Inspections

Deux flux **instantanés**, appelés par l'application. Tous les connecteurs utilisés sont
**standards** (Power Apps V2, SharePoint, OneDrive Entreprise, Office 365 Outlook) :
aucune licence Premium.

| Flux | Rôle | Obligatoire ? |
|---|---|---|
| `INSExporterInspection` | Crée le PDF et le fichier Excel (CSV) dans « Inspections complétées » et envoie le PDF par courriel | Facultatif (bouton « Envoyer ») |
| `INSAjouterPhoto` | Dépose une photo dans la bibliothèque « Photos inspections » | Facultatif (photos) |

> Les anciens flux de l'outil HTML (Flux 1 – Fichier vers listes, Flux 2 – Courriel avec le PDF)
> **ne sont plus nécessaires** : l'application écrit directement dans les listes SharePoint.

Pour chaque flux : <https://make.powerautomate.com> → **Créer → Flux de cloud instantané** →
déclencheur **« Lorsque Power Apps appelle un flux (V2) »**. Donnez **exactement** le nom
indiqué (sans espace) : c'est le nom utilisé dans les formules de l'application.

---

## Flux 1 — `INSExporterInspection`

### Étape 1 — Déclencheur « Lorsque Power Apps appelle un flux (V2) »

Ajoutez **3 entrées de type Texte, dans cet ordre** :

| # | Nom | Contenu |
|---|-----|---------|
| 1 | `NomFichier` | ex. `Inspection_Garage_municipal_2026-09-24` (sans extension) |
| 2 | `RapportHTML` | rapport complet (renseignements, non-conformités en premier, liste de vérification, signature) |
| 3 | `DonneesCSV` | toutes les réponses au format CSV (séparateur « ; ») |

### Étape 2 — SharePoint « Créer un fichier » (Excel / CSV)

- Adresse du site : **RH – Inspections milieu de travail**
- Chemin d'accès du dossier : **Documents partagés / Inspections complétées**
- Nom du fichier : `NomFichier` puis tapez `.csv`
- Contenu du fichier : `DonneesCSV`

### Étape 3 — OneDrive Entreprise « Créer un fichier » (temporaire)

- Chemin d'accès du dossier : `/INS_Temp` (créez ce dossier dans votre OneDrive au besoin)
- Nom du fichier : `NomFichier` + `.html`
- Contenu du fichier : `RapportHTML`

Renommez l'action : **Créer HTML temporaire**.

### Étape 4 — OneDrive Entreprise « Convertir un fichier »

- Fichier : **ID** de « Créer HTML temporaire »
- Type cible : **PDF**

Renommez l'action : **Convertir en PDF**.

### Étape 5 — SharePoint « Créer un fichier » (PDF)

- Même site et même dossier qu'à l'étape 2
- Nom du fichier : `NomFichier` + `.pdf`
- Contenu du fichier : **Contenu du fichier** de « Convertir en PDF »

### Étape 6 — OneDrive Entreprise « Supprimer un fichier »

- Fichier : **ID** de « Créer HTML temporaire »

### Étape 7 — Office 365 Outlook « Envoyer un e-mail (V2) »

- À : adresse(s) des destinataires (gestionnaire, comité SST…)
- Objet : `Inspection du milieu de travail – ` + `NomFichier`
- Corps : « Une inspection du milieu de travail a été réalisée. Le rapport PDF est joint ;
  il est aussi déposé dans le dossier *Inspections complétées*. »
- Pièces jointes : Nom = `NomFichier` + `.pdf` ; Contenu = **Contenu du fichier** de « Convertir en PDF »

### Étape 8 — « Répondre à une application ou à un flux PowerApp »

- Sortie Texte `Resultat` = `OK`.

**Enregistrer.**

---

## Flux 2 — `INSAjouterPhoto`

### Préalable : la bibliothèque « Photos inspections »

Sur le site : **Nouveau → Bibliothèque de documents** → nom **`Photos inspections`**.
Ajoutez deux colonnes **Une ligne de texte** : `CleReponse` et `IdInspection`.

### Étape 1 — Déclencheur « Lorsque Power Apps appelle un flux (V2) »

**4 entrées de type Texte, dans cet ordre** :

| # | Nom | Contenu |
|---|-----|---------|
| 1 | `NomFichier` | nom de la photo (`Photo_….jpg`) |
| 2 | `ContenuBase64` | image encodée (`data:image/jpeg;base64,…`) |
| 3 | `CleReponse` | lien avec l'élément de la liste de vérification |
| 4 | `IdInspection` | lien avec l'inspection |

### Étape 2 — SharePoint « Créer un fichier »

- Adresse du site : votre site
- Chemin d'accès du dossier : **/Photos inspections**
- Nom du fichier : `NomFichier`
- Contenu du fichier : **expression** (icône *fx*) :

```
base64ToBinary(last(split(triggerBody()?['text_1'], ',')))
```

> `text_1` désigne la 2ᵉ entrée (`ContenuBase64`). Si vos entrées portent d'autres noms
> internes, tapez `base64ToBinary(last(split(` , insérez le contenu dynamique
> **ContenuBase64**, puis terminez par `, ',')))`.

Renommez l'action : **Créer la photo**.

### Étape 3 — SharePoint « Mettre à jour les propriétés du fichier »

- Adresse du site : votre site — Nom de la bibliothèque : **Photos inspections**
- Id : **ItemId** de « Créer la photo »
- CleReponse : contenu dynamique `CleReponse`
- IdInspection : contenu dynamique `IdInspection`

### Étape 4 — « Répondre à une application ou à un flux PowerApp »

- Sortie Texte `Resultat` = `OK`.

**Enregistrer.**

---

## Ajouter les flux à l'application

Power Apps Studio → volet **Power Automate** → **+ Ajouter un flux** → choisir
`INSExporterInspection`, puis `INSAjouterPhoto`.

## Dépannage

| Symptôme | Solution |
|---|---|
| « INSExporterInspection n'est pas reconnu » | Flux non ajouté à l'application, ou nom différent. |
| « Le fichier existe déjà » | Une inspection du même endroit à la même date existe déjà : ajoutez `_` + l'expression `utcNow('HHmmss')` au nom des fichiers dans les actions « Créer un fichier ». |
| Photo vide ou illisible | Vérifiez l'expression `base64ToBinary(...)` de l'étape 2 du flux 2. |
| La photo n'apparaît pas dans la fenêtre de détail | Vérifiez que la colonne `CleReponse` est bien remplie (étape 3 du flux 2). |
| Après une modification du flux, erreur dans Power Apps | Volet Power Automate → « … » du flux → **Actualiser**. |
