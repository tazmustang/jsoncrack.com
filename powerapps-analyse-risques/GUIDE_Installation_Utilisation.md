# Application Analyse de risques SST — version Power Apps

**Guide d'installation et d'utilisation**
Division de la santé et de la sécurité au travail — Ville de Québec

---

## 1. Présentation

Cette application Power Apps reprend **toutes les fonctions de l'application HTML
« Analyse de risques DSST V2.2 »**, mais les données sont enregistrées directement dans
**SharePoint** au lieu de fichiers locaux.

| Fonction de l'application HTML | Équivalent Power Apps |
|---|---|
| Entête (service, division, localisation, participants, date, commentaires) | Identique (écran **Grille d'analyse**) |
| Grille d'analyse (ajouter une ligne, + 5 lignes, monter/descendre, supprimer, filtre, recherche) | Identique — chaque ligne est une « carte » à 3 rangées |
| Calcul automatique IR = G × MP, IR résiduel, niveau et couleur | Identique (mêmes seuils : Faible ≤ 250, Modéré ≤ 750, Élevé ≤ 1250, Critique > 1250) |
| Onglets Matrice de risque, Aide-mémoire, Synthèse, Plan d'action | Identiques (un écran par onglet) |
| Sauvegarder / Charger (.json) | **Enregistrer** dans SharePoint ; l'écran **Accueil** liste et rouvre toutes les analyses |
| « Charger depuis SharePoint » (non déployé dans la version HTML) | **Fonctionne d'office** : cliquer sur une analyse dans l'Accueil |
| Envoyer à SharePoint (JSON + Excel + PDF + courriel) | Bouton **Envoyer à SharePoint (PDF/Excel)** → flux Power Automate *standard* |
| Exporter PDF (impression) | Bouton **Imprimer** du Plan d'action + PDF produit par le flux |
| Configuration des URL de flux (clic droit, localStorage) | **N'existe plus** : le flux est intégré à l'application |
| Anciennes analyses .json | Écran **Importer un JSON** (copier-coller du fichier) |

Non repris : Annuler/Refaire et sauvegarde automatique du navigateur (les données sont
enregistrées dans SharePoint avec le bouton **Enregistrer** ; un avertissement s'affiche si
l'on quitte sans enregistrer).

### Coût

**Aucune licence supplémentaire.** L'application n'utilise que des connecteurs *standards*
(SharePoint, OneDrive Entreprise, Office 365 Outlook, Power Apps V2), inclus dans les licences
Microsoft 365 de la Ville. Aucun connecteur Premium, aucun Dataverse.

### Contenu du dossier

```
powerapps-analyse-risques/
├── GUIDE_Installation_Utilisation.md   ← ce guide (aussi en .docx)
├── formules/
│   ├── App_Formulas_FR.txt      ← à coller dans App.Formulas (Power Apps en français)
│   ├── App_Formulas_EN.txt      ← idem, si Power Apps est en anglais
│   ├── App_OnStart_FR.txt       ← à coller dans App.OnStart (français)
│   ├── App_OnStart_EN.txt       ← idem (anglais)
│   └── Reference_formules_FR.md ← toutes les formules, contrôle par contrôle (secours)
├── ecrans/                      ← code YAML de chaque écran, à coller dans Power Apps Studio
│   ├── 1_scrAccueil.yaml
│   ├── 2_scrAnalyse.yaml
│   ├── 3_scrMatrice.yaml
│   ├── 4_scrAideMemoire.yaml
│   ├── 5_scrSynthese.yaml
│   ├── 6_scrPlanAction.yaml
│   └── 7_scrImport.yaml
├── flux/
│   └── Flux_ARExporterAnalyse.md ← création du flux Power Automate (étape par étape)
└── exemple/
    └── exemple_analyse.json     ← analyse d'exemple pour tester l'importation
```

---

## 2. Prérequis

- Un compte Microsoft 365 de la Ville avec accès à <https://make.powerapps.com> et <https://make.powerautomate.com>.
- Droits de **propriétaire** (ou membre avec droits de gestion des listes) sur le site SharePoint
  **RH SST Analyse de risque** (le même que celui utilisé par la version HTML).
- Navigateur Microsoft Edge ou Chrome.

Durée d'installation : environ 1 h à 1 h 30.

---

## 3. Étape 1 — Créer les deux listes SharePoint

> **Important :** créez chaque colonne **avec le nom exact indiqué (sans accent ni espace)**.
> Ne renommez pas les colonnes par la suite : Power Apps utilise ces noms dans les formules.

Sur le site **RH SST Analyse de risque** : **Nouveau → Liste → Liste vide**.

### 3.1 Liste `AR_Analyses` (une ligne par analyse — l'entête)

| Nom de colonne | Type SharePoint | Remarque |
|---|---|---|
| `Title` (colonne « Titre » existante) | Une ligne de texte | Contiendra le **Service** — ne pas renommer |
| `Division` | Une ligne de texte | |
| `Localisation` | Une ligne de texte | |
| `Participants` | Plusieurs lignes de texte | Texte brut (texte enrichi désactivé) |
| `DateAnalyse` | Date et heure | Format : **Date uniquement** |
| `Commentaires` | Plusieurs lignes de texte | Texte brut |
| `Statut` | Une ligne de texte | « Enregistrée » ou « Envoyée » (rempli par l'application) |
| `NbRisques` | Nombre | 0 décimale |
| `NbCritiques` | Nombre | |
| `NbEleves` | Nombre | |
| `NbModeres` | Nombre | |
| `NbFaibles` | Nombre | |
| `IRMax` | Nombre | |

### 3.2 Liste `AR_Lignes` (une ligne par risque de la grille)

| Nom de colonne | Type SharePoint | Remarque |
|---|---|---|
| `Title` (colonne « Titre » existante) | Une ligne de texte | Contiendra l'**Activité de travail**. Paramètres de la liste → colonne Titre → **Exiger des informations : Non** |
| `AnalyseID` | Nombre | Lien vers l'ID de `AR_Analyses`. Paramètres → **Colonnes indexées** → indexer `AnalyseID` |
| `Ordre` | Nombre | Position de la ligne dans la grille |
| `Cle` | Une ligne de texte | Identifiant interne de la ligne |
| `Environnement` | Une ligne de texte | |
| `Tache` | Plusieurs lignes de texte | Texte brut |
| `CategorieDanger` | Une ligne de texte | |
| `Risque` | Plusieurs lignes de texte | Texte brut |
| `Consequence` | Plusieurs lignes de texte | Texte brut |
| `Blessure` | Plusieurs lignes de texte | Texte brut |
| `MesuresExistantes` | Plusieurs lignes de texte | Texte brut |
| `G1` | Nombre | Gravité initiale |
| `MP1` | Nombre | Mesure préventive initiale |
| `MesuresSuggerees` | Plusieurs lignes de texte | Texte brut |
| `Cout` | Une ligne de texte | |
| `G2` | Nombre | Gravité résiduelle |
| `MP2` | Nombre | Mesure préventive résiduelle |

**Facultatif (pour les vues SharePoint) :** ajoutez une colonne calculée `IR` = `[G1]*[MP1]`
et `IRResiduel` = `[G2]*[MP2]` (type de données retourné : Nombre). L'application ne s'en sert pas.

### 3.3 Bibliothèque de documents

La bibliothèque **Analyse de risque** existante est réutilisée par le flux (fichiers JSON, CSV et PDF).

---

## 4. Étape 2 — Créer l'application et coller les formules globales

1. <https://make.powerapps.com> → **+ Créer → Application vide → Application canevas vide**.
   Nom : `Analyse de risques SST` — Format : **Tablette** → **Créer**.
2. **Paramètres** (roue dentée) :
   - **Général → Limite de lignes de données** : `2000`.
   - **Affichage** : taille **16:9 (1366 × 768)**, *Mettre à l'échelle* activé, *Verrouiller les proportions* activé.
3. **Ajouter les données** (icône cylindre → *Ajouter des données* → **SharePoint**) :
   choisissez le site **RH SST Analyse de risque**, cochez **AR_Analyses** et **AR_Lignes** → *Se connecter*.
4. Dans l'arborescence, sélectionnez **App** :
   - propriété **Formulas** : collez tout le contenu de `formules/App_Formulas_FR.txt` ;
   - propriété **OnStart** : collez le contenu de `formules/App_OnStart_FR.txt`.

> **Français ou anglais ?** Si les formules de Power Apps utilisent des **points-virgules**
> (ex. `If(a; b; c)`), utilisez les fichiers **_FR**. Si elles utilisent des **virgules**
> (ex. `If(a, b, c)`), utilisez les fichiers **_EN**.
> Les fichiers YAML des écrans (étape 3) fonctionnent dans les deux cas : Power Apps les convertit automatiquement.

5. Faites un clic droit sur **App** → **Exécuter OnStart**.

---

## 5. Étape 3 — Créer les 7 écrans (copier-coller du YAML)

### 5.1 Créer les écrans vides

**+ Nouvel écran → Vide**, 7 fois, puis renommez-les (double-clic dans l'arborescence) **exactement** :

| Ordre | Nom de l'écran | Fichier YAML |
|---|---|---|
| 1 | `scrAccueil` | `1_scrAccueil.yaml` |
| 2 | `scrAnalyse` | `2_scrAnalyse.yaml` |
| 3 | `scrMatrice` | `3_scrMatrice.yaml` |
| 4 | `scrAideMemoire` | `4_scrAideMemoire.yaml` |
| 5 | `scrSynthese` | `5_scrSynthese.yaml` |
| 6 | `scrPlanAction` | `6_scrPlanAction.yaml` |
| 7 | `scrImport` | `7_scrImport.yaml` |

Supprimez l'écran `Screen1` d'origine (ou renommez-le `scrAccueil`).
`scrAccueil` doit être **le premier** écran de l'arborescence (glisser-déposer au besoin) :
c'est l'écran de démarrage.

> **Créez les 7 écrans avant de coller le code**, car les écrans se référencent entre eux
> (boutons d'onglets, navigation).

### 5.2 Coller le code de chaque écran

Pour chaque écran :

1. Ouvrez le fichier `.yaml` correspondant avec le **Bloc-notes**, **Ctrl+A** puis **Ctrl+C**.
2. Dans Power Apps Studio, sélectionnez l'écran dans l'**arborescence**.
3. **Ctrl+V** (ou clic droit sur l'écran → **Coller**).
   Tous les contrôles de l'écran apparaissent avec leurs formules et leurs positions.

Ordre conseillé : `scrAccueil`, `scrAnalyse`, puis les autres.

À ce stade, seul le bouton **Envoyer à SharePoint (PDF/Excel)** de `scrAnalyse`
affiche une erreur (« ARExporterAnalyse n'est pas reconnu ») : elle disparaîtra à l'étape 4.

> **Si le collage YAML ne fonctionne pas** (version de Power Apps Studio plus ancienne) :
> le fichier `formules/Reference_formules_FR.md` liste chaque contrôle avec son type,
> sa position et toutes ses formules ; insérez le contrôle (menu *Insérer*) et copiez les
> propriétés une à une. Pour les deux galeries (`galAnalyses` et `galLignes`), insérez une
> **Galerie verticale vide**, puis ajoutez les contrôles à l'intérieur (crayon ✎ de la galerie).

---

## 6. Étape 4 — Créer le flux d'envoi vers SharePoint et l'ajouter à l'application

1. Créez le flux **`ARExporterAnalyse`** en suivant `flux/Flux_ARExporterAnalyse.md`.
2. Dans Power Apps Studio : volet **Power Automate** (icône à gauche) → **+ Ajouter un flux**
   → choisissez **ARExporterAnalyse**.
3. L'erreur du bouton **Envoyer à SharePoint** disparaît.

> Cette étape est **facultative** : sans flux, l'application fonctionne entièrement
> (enregistrement dans les listes SharePoint, synthèse, plan d'action, impression).
> Si vous ne créez pas le flux, supprimez simplement le bouton `btnEnvoyerSP`.

---

## 7. Étape 5 — Tester, publier et partager

1. Appuyez sur **F5** (aperçu) et testez :
   - **Accueil → Importer un JSON** → collez le contenu de `exemple/exemple_analyse.json` → **Importer** ;
   - vérifiez les IR (ligne 2 : 25 × 50 = **1250 Élevé**, résiduel 25 × 20 = **500 Modéré**) ;
   - **Enregistrer**, revenez à l'**Accueil** : l'analyse apparaît ; rouvrez-la ;
   - parcourez Matrice, Aide-mémoire, Synthèse, Plan d'action ;
   - **Envoyer à SharePoint** : vérifiez les 3 fichiers dans la bibliothèque et le courriel.
2. **Fichier → Enregistrer**, puis **Publier**.
3. **Partager** l'application (make.powerapps.com → « … » → *Partager*) avec les utilisateurs
   ou un groupe (ex. responsables SST), en **Utilisateur**.
4. Donnez à ces mêmes utilisateurs l'accès **Modification** (Collaborer) aux listes
   `AR_Analyses` et `AR_Lignes` et à la bibliothèque **Analyse de risque**
   (le plus simple : les ajouter comme **Membres** du site).

Les utilisateurs ouvrent l'application depuis <https://apps.powerapps.com>, l'application
mobile **Power Apps** (tablette sur le terrain) ou **Microsoft Teams**
(onglet → Power Apps → Analyse de risques SST).

---

## 8. Guide d'utilisation

### 8.1 Accueil

- Liste de toutes les analyses (les plus récentes en premier) : service, division, localisation,
  date, nombre de risques, nombre de critiques/élevés, IR maximal et statut
  (**Enregistrée** en bleu, **Envoyée** en vert).
- **Rechercher** : tapez le début du service, de la division ou de la localisation.
- **Cliquer sur une analyse** l'ouvre pour modification.
- **Corbeille** : supprime l'analyse et toutes ses lignes (confirmation demandée).
- **+ Nouvelle analyse** : grille vide, date du jour.
- **Importer un JSON** : reprendre une analyse faite avec l'ancienne application HTML.

### 8.2 Grille d'analyse

1. Remplissez l'**entête** : **Service** (obligatoire), Division, Localisation, Date,
   Participants, Commentaires.
2. **+ Ajouter une ligne** (ou **+ 5 lignes**). Chaque ligne est une carte de 3 rangées :
   - rangée 1 : Environnement, Activité de travail, Tâches, Catégorie de danger, ▲ ▼ (ordre), 🗑 (supprimer) ;
   - rangée 2 : Risques, Conséquences, Blessures / Maladie, Mesures en place, **G**, **MP** → **IR** coloré ;
   - rangée 3 : Mesures préventives suggérées, Coûts, **G rés.**, **MP rés.** → **IR résiduel**.
3. L'**IR = G × MP** et le niveau se calculent instantanément. La légende des valeurs G et MP
   est affichée au-dessus de la grille ; la **Matrice de risque** et l'**Aide-mémoire**
   sont accessibles par les onglets.
4. **Rechercher** et **Environnement** filtrent l'affichage des lignes.
5. Cliquez sur **Enregistrer** : l'entête va dans `AR_Analyses`, les lignes dans `AR_Lignes`.
   L'indicateur en haut passe de « ● Modifications non enregistrées » (jaune) à
   « ✔ Enregistrée dans SharePoint » (vert).

> Si vous cliquez sur **Accueil** sans enregistrer, un avertissement s'affiche ;
> un 2ᵉ clic quitte sans enregistrer.

Échelles (identiques à la version HTML) :

| G — Gravité | | MP — Mesure préventive | |
|---|---|---|---|
| 5 | Mineure (1ers soins) | 0 | Élimination à la source |
| 25 | Majeure (réversible, perte de temps) | 10 | Contrôle technique |
| 35 | Grave (irréversible) | 20 | PST + Audit documenté |
| 40 | Décès / tolérance zéro CNESST | 30 | PST ou Formation |
| | | 40 | Affichage + EPI |
| | | 50 | Aucune mesure |

Niveaux : **Faible** ≤ 250 · **Modéré** 251–750 · **Élevé** 751–1250 · **Critique** > 1250.

### 8.3 Onglets de consultation

- **Matrice de risque** : tableau G × MP coloré et légende des niveaux.
- **Aide-mémoire** : dangers, risques et conséquences par catégorie (Physique, Mécanique,
  Électrique, Chimique, Biologique, Humain, Ergonomique), avec filtre et recherche.
- **Synthèse** : total et nombre de risques par niveau, graphiques avant/après mesures
  correctives, répartition par environnement et par catégorie, top 10 des risques.
- **Plan d'action** : mesures correctives triées de l'IR le plus élevé au plus faible,
  filtres par niveau et environnement, % de réduction. Bouton **Imprimer** (navigateur → Enregistrer en PDF).

### 8.4 Envoyer à SharePoint (PDF / Excel / JSON + courriel)

Après **Enregistrer**, cliquez sur **Envoyer à SharePoint (PDF/Excel)**. Le flux dépose dans la
bibliothèque **Analyse de risque** :

- `AR_SST_<Service>_<date>.pdf` — rapport (entête, synthèse, grille, plan d'action) ;
- `AR_SST_<Service>_<date>.csv` — grille complète, s'ouvre dans Excel ;
- `AR_SST_<Service>_<date>.json` — même format que l'application HTML (réimportable) ;

puis envoie un courriel aux responsables SST. Le statut de l'analyse devient **Envoyée**.

### 8.5 Importer une ancienne analyse (.json)

1. Ouvrez le fichier `.json` avec le Bloc-notes → **Ctrl+A**, **Ctrl+C**.
2. Application → **Accueil → Importer un JSON** → collez → **Importer**.
3. Vérifiez la grille puis **Enregistrer** (l'analyse est créée dans SharePoint).

---

## 9. Dépannage

| Problème | Solution |
|---|---|
| « Le nom n'est pas valide » sur `AR_Analyses` ou `AR_Lignes` | Les listes ne sont pas ajoutées comme sources de données ou portent un autre nom (étape 2.3). |
| Erreur sur un champ (ex. `MesuresSuggerees`) | Le nom de colonne SharePoint diffère. Vérifiez l'orthographe exacte (sans accent) ; si une colonne a été renommée, recréez-la. |
| Erreur à l'enregistrement : « Titre est obligatoire » | Liste `AR_Lignes` → paramètres de la colonne **Titre** → *Exiger des informations* : **Non** (une ligne peut avoir une activité vide). |
| Les formules affichent des erreurs de virgule / point-virgule | Vous avez collé la version FR dans un Power Apps en anglais (ou l'inverse) : utilisez l'autre fichier (`_EN` / `_FR`). |
| `nfNiveaux`, `colLignes`… inconnus | Coller `App_Formulas` et `App_OnStart`, puis clic droit sur **App** → **Exécuter OnStart**. |
| La boîte de confirmation de suppression (Accueil) est cachée derrière la liste | Sélectionnez `recVoile_Acc`, `recDialogue_Acc`, `lblDialogue_Acc`, `btnConfirmerSuppr`, `btnAnnulerSuppr` → **Réorganiser → Mettre au premier plan**. |
| Plus de 2000 analyses | La recherche de l'accueil (« commence par ») et le filtre des lignes par `AnalyseID` sont délégables : aucune limite pratique. |
| Le texte disparaît d'un champ en tapant | Le champ est enregistré quand on le quitte (Tab ou clic ailleurs) : c'est normal. |

---

## 10. Modifier l'application plus tard

- **Ajouter un environnement** (ex. « Entrepôt ») : modifiez `nfEnvironnements` dans
  App.Formulas **et** les listes `["Tous", …]` des contrôles `ddFiltreEnv` (Grille) et `ddPAEnv` (Plan d'action).
- **Modifier l'aide-mémoire** : tables `nfCategories` et `nfAideMemoire` dans App.Formulas.
- **Modifier les seuils de risque** : table `nfNiveaux` (colonnes `Plancher` et `Seuil`)
  — les formules de l'enregistrement (`btnEnregistrer`) et des cartes de la Synthèse
  utilisent aussi les valeurs 250 / 750 / 1250.
