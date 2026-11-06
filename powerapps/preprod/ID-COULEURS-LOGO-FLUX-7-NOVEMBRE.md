---
title: "ID, nouvelles couleurs, logo et erreur du flux « Suivi des étapes »"
subtitle: "Application Appréciation de la contribution (SRHVQ) · Complément au plan 1.0.0.7 · 7 novembre 2026"
lang: fr-CA
---

# 1. L'erreur sur txtId › Default

**Ce que montre le soulignement rouge :** `employeeId` n'existe pas dans le connecteur « Utilisateurs d'Office 365 » de Power Apps. Ce connecteur ne donne pas accès au numéro d'employé, même s'il est dans l'annuaire.

**Correction (30 secondes)** : txtId › **Default**, remplacez tout par :

```
// ID de l'employé : saisi par la personne (non disponible dans le connecteur de l'annuaire)
varDossier.IdEmploye
```

Puis :
- **txtId › HintText** : `"Votre numéro d'employé (obligatoire)"`
- la **validation** de btnDeposer (champ obligatoire) empêche d'enregistrer sans ID.

> Il existe une solution avancée (requête Microsoft Graph avec le connecteur Groupes Office 365), mais elle ajoute un connecteur et une étape de validation par les TI. Je ne la recommande pas avant le lancement.

# 2. Les nouvelles couleurs

| Élément | Avant | Après (format Power Apps) |
|---|---|---|
| **Bandeau** (et les éléments or-brun) | #857650, RGBA(133; 118; 80; 1) | **#00285E** : `RGBA(0; 40; 94; 1)` |
| **Gris** (textes secondaires, libellés, étapes à venir) | #6B7280 et #9CA3AF | **#8A8C8E** : `RGBA(138; 140; 142; 1)` |

**Ce qui ne change pas :** les gris **très pâles** des bordures et des fonds (#E5E7EB, #F3F4F6). En #8A8C8E, ils deviendraient trop foncés et alourdiraient l'écran.

> ⚠️ **Accessibilité, à signaler aux Communications :** le gris #8A8C8E sur fond blanc a un contraste de **3,4 : 1**. La norme demande au moins 4,5 : 1 pour le petit texte. Il convient aux titres et aux libellés en gras ; pour les petits textes (notes, dates), un gris plus foncé serait plus lisible.

## 2.1 Le bandeau (2 contrôles)

Aujourd'hui, le bandeau est **déjà bleu #00285E en Prod**. Il est or-brun seulement **hors Prod** (bac à sable, PréProd), pour qu'on voie qu'on est dans un environnement de test. Sa formule actuelle est `If(varEnv = "PROD"; RGBA(0;40;94;1); RGBA(133;118;80;1))`.

Pour le mettre bleu **partout** :

| Contrôle | Propriété | Formule |
|---|---|---|
| **headerBar** (scrFormulaire) | Fill | `RGBA(0; 40; 94; 1)` |
| **headerBar_1** (scrMesDossiers) | Fill | `RGBA(0; 40; 94; 1)` |

> Facultatif : pour savoir qu'on est en test, ajoutez « (PRÉPROD) » au sous-titre. headerSub › Text : `"Formulaire : " & … & If(varEnv <> "PROD"; "  ·  " & varEnv; "")`

## 2.2 Les autres éléments or-brun (12 contrôles)

Même couleur bleue, `RGBA(0; 40; 94; 1)` :

| Contrôle | Propriétés à changer |
|---|---|
| btnHelp (« Comment remplir ce formulaire ») | Fill **et** BorderColor |
| btnCalloutHelp | Fill **et** BorderColor |
| gLockedNote | Fill |
| gLockedLabel | Color |
| sigSIChip, sigSHChip, sigDirChip | Fill |
| sigSIChipLabel, sigSHChipLabel, sigDirChipLabel | Color |
| statutPill | Fill |
| statutPillLabel | Color |

> Les formules de ces propriétés contiennent souvent un `If(…)`. Ne remplacez **que** `RGBA(133; 118; 80; …)` par `RGBA(0; 40; 94; …)`, en gardant le dernier chiffre (la transparence) tel quel. Astuce : dans la barre fx, utilisez **Rechercher et remplacer** : `133; 118; 80` par `0; 40; 94`.

## 2.3 Les gris (environ 80 contrôles) : la méthode rapide

Power Apps permet de **changer la couleur de plusieurs contrôles d'un coup** :

1. Dans l'**arborescence**, maintenez **Ctrl** et cliquez sur plusieurs étiquettes de la liste ci-dessous.
2. Dans le **panneau de droite**, changez **Couleur** (Color), ou dans la barre fx, propriété **Color** : `RGBA(138; 140; 142; 1)`.
3. Tous les contrôles sélectionnés changent ensemble.

**Écran scrFormulaire**, propriété **Color** :

- **Libellés :** autosaveNote, stepLabel, stepDate, stepDotLabel, tabLabel, lblNom, lblId, lblPoste, lblRoleTitle, lblPosteTitle, lblActionsTitle.
- **Notes :** aNote1, aNote2, bNote, vNote, evNote, compDesc, evDesc, avisText, aideSub.
- **En-têtes des postures :** p1HdrItem, p1HdrCadre, p1HdrSup, p1ComLabel. Même chose pour p2, p3 et p4.
- **Messages de verrou :** bAttenteText, bLockLabel, vLockLabel, dLockLabel, eLockLabel, fLockLabel, evLockLabel.
- **Valeurs :** valLbl1, valLbl2.
- **Section G :** certChipLabel, certDetail, sigSIRoleLabel, sigSIDetail, sigSHRoleLabel, sigSHDetail, sigDirRoleLabel, sigDirDetail.

**Écran scrMesDossiers**, propriété **Color** : pageSubtitle, filtrePillLabel, lblCompte, cellRole, cellModifie, emptyHint, footNote.

**Boutons désactivés**, propriété **DisabledColor** : btnHelp, btnDeposer, btnMesDossiers, btnApercuPDF, btnOuvrirPDF, btnNouveau, btnCalloutHelp, btnActSupprimer, btnAddActuel, btnAveSupprimer, btnAddAvenir, btnDevPrecSupprimer, btnAddDevPrec, btnDevNouvSupprimer, btnAddDevNouv, btnContact, btnOuvrir, btnPDFDossier, btnNouveauDossier.

> **Note :** stepLabel, stepDotLabel et stepDate ont une formule `If(…)` (gris pour les étapes à venir). Dans ces 3 contrôles, remplacez seulement `156; 163; 175` et `107; 114; 128` par `138; 140; 142`, avec Rechercher et remplacer.

**Si vous préférez que je le fasse pour vous :** exportez la solution du bac à sable en **non gérée** et envoyez-moi le .zip. Je change toutes les couleurs d'un coup et je vous renvoie une solution à réimporter dans le **bac à sable**. Faites-le à un moment où vous ne modifiez rien d'autre dans l'application, pour ne pas perdre de travail.

## 2.4 Le PDF

Recollez **btnApercuPDF-OnSelect.txt** (mis à jour) : le filet sous les titres passe au bleu #00285E, et les textes gris passent au #8A8C8E.

# 3. Le logo dans le bandeau bleu

Fichiers fournis (dossier **logo**) :
- **logo-ville-quebec-blanc.png** : blanc sur fond transparent, **pour le bandeau bleu** ;
- **logo-ville-quebec-couleur.png** : fond transparent, pour les fonds blancs (À propos, documents).

> Faites confirmer par les Communications que cette version blanche (« renversée ») est conforme. Elles ont peut-être un fichier officiel à utiliser à la place.

**Étapes (à faire sur les 2 écrans) :**

1. Barre de gauche › **Médias** (icône d'image) › **Charger** › choisissez **logo-ville-quebec-blanc.png**.
2. Arborescence › cliquez sur **headerBar** (scrFormulaire).
3. **Insérer › Médias › Image**. Renommez-la **imgLogo**.
4. Propriétés :

| Propriété | Valeur |
|---|---|
| Image | `'logo-ville-quebec-blanc'` (choisissez-le dans la liste) |
| Height | `48` |
| Width | `146` |
| ImagePosition | `ImagePosition.Fit` |
| X | `20` |
| Y | `(Parent.Height - Self.Height) / 2` |

5. Si headerBar est un **conteneur à disposition automatique** (X et Y grisés) : glissez imgLogo en **premier** dans headerBar, puis **AlignInContainer** : `AlignInContainer.Center`.
6. Refaites les étapes 2 à 5 dans **headerBar_1** (scrMesDossiers), avec le nom **imgLogo_1**.
7. Vérifiez que le titre « Appréciation de la contribution » ne chevauche pas le logo. Au besoin, augmentez **PaddingLeft** du titre (ex. `180`).

# 4. L'erreur du flux « Appréciation – Suivi des étapes »

**Le message :** « The parameter with value `@outputs('Changements')?['body/ColumnHasChanged/CourrielPersonne']` in path 'emailMessage/To' with type/format 'Boolean' is not convertible to type/format 'String/email' ».

**En clair :** dans le champ **À** du nouveau courriel, vous avez choisi « **CourrielPersonne** » dans la section **Changements** du contenu dynamique. Ce n'est pas l'adresse : c'est la réponse **Oui/Non** à la question « la colonne CourrielPersonne a-t-elle changé ? ». Le courriel ne peut pas partir à « Oui ».

**Correction :**

1. Ouvrez le flux en **Modifier** › ouvrez l'action **Envoyer un e-mail (V2) 5**, celle du nouveau courriel « la version de votre supérieur est prête ».
2. Champ **À** : supprimez la pastille (le **x**).
3. Cliquez dans le champ › **fx** (expression) › collez :

```
triggerOutputs()?['body/CourrielPersonne']
```

   › **Ajouter**. Vous pouvez aussi choisir **CourrielPersonne** dans la section du **déclencheur** (« Lorsqu'un élément est créé ou modifié »), **pas** dans « Changements ».
4. **Enregistrer.**

✅ Le flux s'enregistre sans erreur.

> **Règle à retenir :** dans le contenu dynamique, la section **« Changements »** contient des **Oui/Non** (« la colonne a-t-elle changé ? »). Les **valeurs** (adresses, nom, statut) sont dans la section du **déclencheur**.
