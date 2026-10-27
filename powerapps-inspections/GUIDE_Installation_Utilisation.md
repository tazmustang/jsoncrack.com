# Inspection du milieu de travail — Bâtiments, cours et accès — version Power Apps

**Guide d'installation et d'utilisation**
Service des ressources humaines – Division Santé et sécurité au travail — Ville de Québec

---

## 1. Pourquoi une version Power Apps ?

L'outil HTML (Inspection_Batiments.html, v1.5) fonctionne, mais SharePoint refuse de l'exécuter.
Il faut donc :

- synchroniser le site avec OneDrive sur chaque poste ;
- créer un raccourci sur le bureau ;
- choisir le dossier dans Edge sur chaque poste ;
- utiliser un flux qui lit les fichiers .json pour remplir les listes.

L'application Power Apps **supprime toutes ces étapes** :

| Outil HTML | Application Power Apps |
|---|---|
| Synchroniser / raccourci OneDrive, « Toujours conserver sur cet appareil », raccourci bureau | **Aucune installation sur le poste** : on ouvre l'application (navigateur, Teams, application mobile Power Apps sur tablette ou téléphone) |
| Choisir le dossier « Inspections complétées » dans Edge, autorisations d'accès aux fichiers | **Aucun réglage** : les données vont directement dans SharePoint |
| Fichier .json par inspection + Flux 1 qui remplit les listes | L'application **écrit directement dans les listes** : plus de Flux 1 |
| Liste de vérification (20 sujets, 78 éléments + « Autres ») | **Identique** (même contenu, version nov. 2016, mise à jour 1er mars 2017) |
| Oui / Non / N/A, recliquer annule, sujet « Non applicable » | Identique |
| Potentiel de gravité E/F, correctif, emplacement, responsable, échéancier, statut, photos, commentaire 💬 | Identique (fenêtre de détail) |
| Progression, « seulement les éléments sans réponse » | Identique |
| Onglet Résumé : compteurs, validation, tableau des non-conformités, signature | Identique |
| PDF / Excel / courriel | Bouton **Envoyer** → flux standard (PDF + Excel dans « Inspections complétées » + courriel) ; bouton **Imprimer** |
| Onglet Suivi : compteurs, correctifs de toutes les inspections, retards en rouge | Identique, **mises à jour immédiates dans SharePoint** |
| Exporter le suivi en Excel | Dans la liste SharePoint `INS_Reponses` : **Exporter → Exporter vers Excel** (vue « Correctifs à réaliser ») |

**Limites à connaître :**

- L'application a besoin du **réseau** (Wi-Fi ou cellulaire). L'outil HTML, lui, fonctionnait hors ligne.
- Les anciennes inspections (.json) ne sont pas importées : elles restent consultables
  (fichiers et PDF) dans « Inspections complétées ».
- Il n'y a pas de sauvegarde automatique à chaque clic : on clique sur **Enregistrer**.
  Un avertissement s'affiche si on quitte sans enregistrer.

**Coût :** aucune licence supplémentaire (connecteurs standards inclus dans Microsoft 365, pas de Dataverse).

### Contenu du dossier

```
powerapps-inspections/
├── GUIDE_Installation_Utilisation.md / .docx   ← ce guide
├── ecrans/                    ← code YAML des écrans (à coller dans Power Apps Studio)
│   ├── 1_scrAccueil.yaml
│   ├── 2_scrInspection.yaml
│   ├── 3_scrResume.yaml
│   └── 4_scrSuivi.yaml
├── formules/
│   ├── App_Formulas_FR.txt / _EN.txt   ← liste de vérification + modèle (App.Formulas)
│   ├── App_OnStart_FR.txt / _EN.txt    ← initialisation (App.OnStart)
│   ├── Controles_a_inserer_manuellement.md  ← signature et bouton photo
│   └── Reference_formules_FR.md        ← toutes les formules, contrôle par contrôle (secours)
└── flux/
    └── Flux_Inspections.md / .docx     ← les 2 flux Power Automate, étape par étape
```

---

## 2. Prérequis

- Compte Microsoft 365 de la Ville avec accès à <https://make.powerapps.com> et <https://make.powerautomate.com>.
- Droits de propriétaire (ou de gestion des listes) sur le site **RH – Inspections milieu de travail**.
- Durée de l'installation : environ 1 h 30.

---

## 3. Étape 1 — Créer les listes et la bibliothèque SharePoint

> **Important :** créez chaque colonne avec le **nom exact indiqué (sans accent ni espace)**.
> Une fois la colonne créée, vous pouvez changer son nom **affiché**, mais il est plus simple de ne pas y toucher.

Site → **Nouveau → Liste → Liste vide**.

### 3.1 Liste `INS_Inspections` (une ligne par inspection)

| Colonne | Type | Remarque |
|---|---|---|
| `Title` (colonne « Titre » existante) | Une ligne de texte | Contient l'**Endroit** |
| `Service` | Une ligne de texte | |
| `Inspecteur` | Une ligne de texte | Inspection réalisée par |
| `DateInspection` | Date et heure | Date uniquement |
| `Participants` | Plusieurs lignes de texte | Texte brut |
| `SectionsNA` | Une ligne de texte | Sujets non applicables (ex. `\|9\|17\|`) |
| `Signature` | Plusieurs lignes de texte | Texte brut — image de la signature |
| `IdInspection` | Une ligne de texte | Identifiant unique |
| `NbApplicables` | Nombre | |
| `NbRepondus` | Nombre | |
| `NbNonConformes` | Nombre | |
| `NbGraviteElevee` | Nombre | |
| `CorrectifsOuverts` | Nombre | |
| `ProchaineEcheance` | Date et heure | Date uniquement |
| `StatutSuivi` | Une ligne de texte | Ouvert, En cours, Fermé, Aucun correctif |

### 3.2 Liste `INS_Reponses` (une ligne par élément répondu — sert aussi de liste des correctifs)

| Colonne | Type | Remarque |
|---|---|---|
| `Title` (« Titre ») | Une ligne de texte | Contient l'**Élément**. Paramètres de la colonne : *Exiger des informations* = **Non** |
| `InspectionID` | Nombre | **À indexer** |
| `IdInspection` | Une ligne de texte | |
| `ItemID` | Une ligne de texte | Code de l'élément (ex. `s3-2`) |
| `SectionNo` | Nombre | No du sujet (1 à 21) |
| `Sujet` | Une ligne de texte | |
| `Reponse` | Une ligne de texte | O, N ou NA — **À indexer** |
| `Applicable` | Une ligne de texte | Oui / Non (sujet non applicable) |
| `Gravite` | Une ligne de texte | E ou F |
| `Commentaire` | Plusieurs lignes de texte | Texte brut — correctif et/ou commentaire |
| `Emplacement` | Une ligne de texte | |
| `Responsable` | Une ligne de texte | |
| `Echeance` | Date et heure | Date uniquement |
| `StatutCorrectif` | Une ligne de texte | À faire, En cours, Réalisé — **À indexer** |
| `DateRealise` | Date et heure | Date uniquement |
| `Endroit` | Une ligne de texte | Copie pour le suivi |
| `Service` | Une ligne de texte | Copie pour le suivi |
| `DateInspection` | Date et heure | Copie pour le suivi |

**Index :** liste `INS_Reponses` → Paramètres de la liste → **Colonnes indexées** → créez un index
sur `InspectionID`, `Reponse` et `StatutCorrectif` (indispensable au-delà de 5000 lignes, soit environ 60 inspections).

**Vue utile :** « Correctifs à réaliser » : filtre `Reponse` = `N` **et** `StatutCorrectif` différent de `Réalisé`,
tri par `Echeance`, regroupement par `Responsable`. Le menu **Exporter → Exporter vers Excel** de cette vue
remplace « Exporter le suivi en Excel ». Le menu **M'avertir** envoie un courriel quand une ligne change.

### 3.3 Bibliothèque `Photos inspections` (si vous utilisez les photos)

**Nouveau → Bibliothèque de documents** → `Photos inspections`, avec deux colonnes
**Une ligne de texte** : `CleReponse` et `IdInspection`.

### 3.4 Dossier « Inspections complétées »

Le dossier existant de la bibliothèque **Documents** reçoit les PDF et les fichiers Excel (CSV) envoyés par l'application.

### 3.5 Droits

Les inspecteurs doivent pouvoir **modifier** les deux listes, la bibliothèque Photos inspections
et le dossier Inspections complétées : en pratique, être **Membres** du site. Les gestionnaires
en consultation peuvent être Visiteurs (dans ce cas, ils voient l'application mais ne peuvent rien modifier).

---

## 4. Étape 2 — Créer l'application et coller les formules globales

1. <https://make.powerapps.com> → **+ Créer → Application vide → Application canevas vide** —
   Nom : `Inspection milieu de travail` — Format : **Tablette**.
2. **Paramètres** :
   - **Général → Limite de lignes de données** : `2000` ;
   - **Affichage** : 16:9 (1366 × 768), *Mettre à l'échelle* activé.
3. **Données → Ajouter des données → SharePoint** → site **RH – Inspections milieu de travail** →
   cochez **INS_Inspections**, **INS_Reponses** et **Photos inspections**.
4. Sélectionnez **App** dans l'arborescence :
   - **Formulas** : collez `formules/App_Formulas_FR.txt` ;
   - **OnStart** : collez `formules/App_OnStart_FR.txt`.
5. Clic droit sur **App** → **Exécuter OnStart**.

> **FR ou EN ?** Si les formules de votre Power Apps utilisent des **points-virgules** (`If(a; b; c)`),
> prenez les fichiers **_FR** ; si elles utilisent des **virgules** (`If(a, b, c)`), prenez **_EN**.
> Les fichiers YAML (étape 3) conviennent aux deux langues.

---

## 5. Étape 3 — Créer les écrans

### 5.1 Créer 4 écrans vides, nommés exactement :

| Ordre | Nom | Fichier |
|---|---|---|
| 1 | `scrAccueil` | `ecrans/1_scrAccueil.yaml` |
| 2 | `scrInspection` | `ecrans/2_scrInspection.yaml` |
| 3 | `scrResume` | `ecrans/3_scrResume.yaml` |
| 4 | `scrSuivi` | `ecrans/4_scrSuivi.yaml` |

`scrAccueil` doit être le **premier** écran de l'arborescence (écran de démarrage).
Créez les 4 écrans **avant** de coller le code (ils se référencent entre eux).

### 5.2 Coller le code

Pour chaque écran : ouvrez le fichier `.yaml` dans le Bloc-notes → **Ctrl+A**, **Ctrl+C** →
dans Power Apps Studio, sélectionnez l'écran dans l'arborescence → **Ctrl+V**.

### 5.3 Insérer deux contrôles à la main

Suivez `formules/Controles_a_inserer_manuellement.md` :

- **`penSignature`** (Entrée de stylet) sur `scrResume` ;
- **`addPhoto`** (Ajouter une image) dans la fenêtre de détail de `scrInspection`.

> Tant que les flux (étape 4) ne sont pas ajoutés, les boutons **Envoyer** et **addPhoto**
> affichent une erreur : c'est normal.

> **Si le collage YAML échoue**, `formules/Reference_formules_FR.md` donne chaque contrôle avec son type,
> sa position et ses formules. Les galeries `galSections`, `galElements`, `galNC`, `galSuivi` et
> `galInspections` sont des **galeries verticales vides** ; `galDPhotos` est une **galerie horizontale vide**.

---

## 6. Étape 4 — Créer les flux (facultatif mais recommandé)

Suivez `flux/Flux_Inspections.md` pour créer `INSExporterInspection` (PDF + Excel + courriel)
et `INSAjouterPhoto` (photos), puis ajoutez-les à l'application (volet **Power Automate → Ajouter un flux**).

Sans flux, l'application fonctionne : inspection, enregistrement, suivi, signature et impression.
Si vous n'utilisez pas les photos, supprimez `addPhoto`, `lblDPhotos`, `galDPhotos` et `lblDPhotoAide`.

---

## 7. Étape 5 — Tester, publier, partager

1. **F5** (aperçu) : créez une inspection test, répondez à quelques éléments (dont un **Non**
   avec gravité, responsable, échéance et photo), marquez un sujet « Non applicable »,
   signez, **Enregistrer**, puis **Envoyer**. Vérifiez les listes, le dossier et le courriel.
2. **Fichier → Enregistrer → Publier**.
3. **Partager** l'application avec l'équipe (ou un groupe Microsoft 365) en tant qu'**Utilisateur**.
4. Pour l'avoir sous la main :
   - **Teams** : ajoutez un onglet **Power Apps** dans le canal de l'équipe ;
   - **tablette ou téléphone** : installez l'application **Power Apps** (App Store / Google Play), connectez-vous et épinglez l'application ;
   - **poste** : ajoutez <https://apps.powerapps.com> (lien de l'application) aux favoris d'Edge.

L'ancienne procédure « Avoir les sites SharePoint en raccourci sur son poste » n'est plus nécessaire
pour l'outil d'inspection.

---

## 8. Guide d'utilisation

### 8.1 Accueil

- Liste des inspections (les plus récentes en premier) : endroit, service, inspecteur, date,
  non-conformités, gravité E, correctifs à réaliser, prochaine échéance et statut de suivi
  (**Ouvert** rouge, **En cours** orange, **Fermé** vert, **Aucun correctif** gris).
- **Rechercher** : début de l'endroit, du service ou du nom de l'inspecteur.
- **Cliquer** sur une inspection l'ouvre ; **corbeille** = supprimer (avec confirmation).
- **+ Nouvelle inspection** (l'inspecteur est prérempli avec votre nom) ; **Suivi des correctifs**.

### 8.2 Onglet Inspection

1. Remplissez **Endroit** (obligatoire), Service, Inspection réalisée par, Date, Participants.
2. À gauche, la liste des **sujets** (1 à 21) avec le nombre d'éléments répondus et les non-conformités.
   Cliquez sur un sujet pour afficher ses éléments à droite.
3. **Marquer non applicable** : le sujet n'est plus compté (cliquez de nouveau pour le rétablir).
4. Pour chaque élément : **Oui**, **Non** ou **N/A** (recliquer sur la même réponse l'annule).
5. Sur **Non**, la **fenêtre de détail** s'ouvre : potentiel de gravité **E** ou **F**, correctifs et/ou
   commentaires, emplacement, responsable, échéancier, statut, **photos**. Le crayon ✎ ouvre cette
   fenêtre pour n'importe quel élément (commentaire). Cliquez sur **Fermer** pour valider.
6. Sujet **21. Autres** : **+ Ajouter un élément** pour vos propres points (corbeille pour retirer).
7. La barre bleue montre la **progression** ; **Seulement sans réponse** aide à terminer.
8. **Enregistrer** (en haut à droite) : l'inspection est enregistrée dans SharePoint.

### 8.3 Onglet Résumé et envoi

- Compteurs : éléments répondus, non-conformités, gravité élevée, correctifs à réaliser.
- Message de **validation** : renseignements incomplets, éléments sans réponse, non-conformités sans gravité, signature.
- **Tableau des non-conformités** (gravité E en premier) : on peut y compléter le responsable, l'échéance
  (encadrée en rouge si en retard) et le statut.
- **Signature** : signez dans le cadre → **Valider la signature** → **Enregistrer**.
- **Envoyer (PDF + Excel + courriel)** : après avoir enregistré.
- **Imprimer cet écran** : impression du navigateur (Enregistrer au format PDF).

### 8.4 Onglet Suivi des correctifs

- Compteurs : inspections, non-conformités, correctifs à réaliser, **en retard**.
- Tableau de **tous les correctifs** de toutes les inspections, triés par échéance (retards en rouge),
  recherche par endroit ou responsable, option « Afficher aussi les correctifs réalisés ».
- Modifiez le **responsable**, l'**échéance** ou le **statut** : c'est **enregistré immédiatement** dans
  SharePoint, et le statut de suivi de l'inspection est recalculé.
- Cliquez sur l'endroit pour ouvrir l'inspection complète.

---

## 9. Rappel hebdomadaire des retards (ancien Flux 3)

Si vous utilisiez le flux de rappel, modifiez son action « Obtenir les éléments » :
liste **INS_Reponses**, requête de filtre :

```
Reponse eq 'N' and Applicable eq 'Oui' and StatutCorrectif ne 'Réalisé' and Echeance lt '@{formatDateTime(utcNow(),'yyyy-MM-dd')}'
```

---

## 10. Dépannage

| Problème | Solution |
|---|---|
| `INS_Inspections` ou `INS_Reponses` inconnus | Ajoutez les listes comme sources de données (étape 2.3) ; vérifiez leur nom. |
| Erreur sur une colonne (ex. `StatutCorrectif`) | Le nom de colonne SharePoint diffère : vérifiez l'orthographe exacte (sans accent). |
| « Titre est obligatoire » à l'enregistrement | `INS_Reponses` → colonne **Titre** → *Exiger des informations* : **Non**. |
| Erreurs de virgules / points-virgules | Utilisez l'autre version des fichiers (`_FR` / `_EN`). |
| `nfItems`, `colReponses`… inconnus | Collez App.Formulas et App.OnStart, puis **Exécuter OnStart**. |
| La fenêtre de détail ou la confirmation de suppression est cachée | Sélectionnez ses contrôles (`recVoile_…`, `recDialogue_…`, etc.) → **Réorganiser → Mettre au premier plan**. |
| La signature ne s'enregistre pas | Réduisez la taille du cadre `penSignature` (ex. 360 × 120) ; la colonne `Signature` doit être en *texte brut*. |
| Enregistrement lent la première fois | Normal : environ 80 réponses sont créées. Les enregistrements suivants ne mettent à jour que les réponses existantes. |
| Une saisie disparaît en tapant | Le texte est enregistré quand on quitte le champ (Tab ou clic ailleurs). |

---

## 11. Modifier la liste de vérification

La liste est dans **App.Formulas** :

- `nfSections` : les sujets (numéro et titre) ;
- `nfItems` : les éléments (`Cle` unique comme `s3-5`, `SectionNo`, `Element`).

Pour ajouter un élément, ajoutez une ligne à `nfItems` avec une **nouvelle** `Cle`.
Ne modifiez pas la `Cle` des éléments existants : elle relie les réponses déjà enregistrées.
