---
title: "Mise à jour du 28 octobre 2026"
subtitle: "PDF joint au dossier, allègement de l'écran (sans onglets Synthèse ni Plan), dates"
lang: fr-CA
---

# Résumé des changements

| N° | Demande | Solution |
|---|---|---|
| 1 | Joindre le PDF au dossier de l'employé | Le flux 3 **joint le PDF à l'élément** de la liste Appreciations (pièce jointe), au lieu de la bibliothèque Appreciations_PDF |
| 2 | Plusieurs versions du PDF portent à confusion | Le flux **remplace** l'ancien PDF du même nom : il y a toujours **une seule** version, la plus récente |
| 3 | Plan de développement jugé trop lourd | **Onglet Plan de développement supprimé**, avec son bouton d'impression. Les objectifs à venir et le développement restent dans le formulaire (sections A et D) et dans le PDF complet |
| 4 | Trop de « Comment remplir » | On garde **seulement** le bouton du haut à gauche |
| 5 | Retirer « Synthèse » | **Onglet supprimé** (il causait aussi l'erreur « Impossible d'utiliser la fonction Average avec une table vide ») |
| 6 | « Transmis à la paie » | Devient **« Transmis aux RH »** dans la barre d'étapes et le PDF |
| 7 | Erreur fr-CA dans stepDate | Nouvelle formule ci-dessous |
| 8 | Bouton « Ouvrir le PDF » | Il est nécessaire (le navigateur bloque l'ouverture automatique). Il existe en **deux endroits** : dans le formulaire, et sur chaque ligne de **Mes dossiers** (bouton 📄 PDF) |

**Bonus du point 1 :** une pièce jointe a **exactement les mêmes accès que le dossier**. Seuls la personne, ses supérieurs, le directeur si requis et les RH peuvent ouvrir le PDF. L'action « Accorder l'accès » et la bibliothèque Appreciations_PDF ne sont donc **plus nécessaires**.

Ordre conseillé : **A** (flux) → **B** (application) → **C** (Mes dossiers) → **D** (ménage) → **E** (test).

# A. Modifier le flux GenererPDFAppreciation (15 minutes)

Ouvrez le flux en modification, dans la solution.

## A.1 Le déclencheur Power Apps (V2)

1. **Supprimez** l'entrée **courriel** (… à droite de l'entrée › Supprimer).
2. Ajoutez une entrée **Nombre** nommée `idDossier`.
3. Ordre final : **nomFichier** (Texte), **html** (Texte), **idDossier** (Nombre).

## A.2 Les actions 1 et 2 ne changent pas

- **Créer un fichier** (OneDrive) ;
- **Convertir un fichier** (OneDrive).

## A.3 Supprimer les 3 anciennes actions SharePoint

Supprimez ces cartes (… › Supprimer) :

- **Créer un fichier** (SharePoint, vers Appreciations_PDF) ;
- **Accorder l'accès à un élément ou à un dossier** ;
- **Obtenir les propriétés du fichier**.

## A.4 Ajouter les nouvelles actions, sous « Convertir un fichier »

**a) SharePoint › Obtenir les pièces jointes** — renommez-la `Pieces jointes`

- Adresse du site : variable **Site Appréciations**
- Nom de la liste : variable **Liste Appreciations**
- Id : **idDossier** (contenu dynamique du déclencheur)

**b) Contrôle › Appliquer à chacun** — renommez-la `Anciennes versions`

- Sortie : **Corps** de « Pieces jointes » (contenu dynamique)
- À l'intérieur, ajoutez une **Condition** :
  - à gauche : **Nom d'affichage** (DisplayName, venant de « Pieces jointes ») ;
  - au milieu : **est égal à** ;
  - à droite : l'**expression** (fx) suivante — c'est la méthode qui fonctionne à coup sûr :

    ```
    concat(triggerBody()?['text'], '.pdf')
    ```
- Dans **Si oui** : **SharePoint › Supprimer la pièce jointe**
  - Site et liste : les mêmes variables
  - Id : **idDossier**
  - Id de la pièce jointe : **Id** (venant de « Pieces jointes »)

**c) SharePoint › Ajouter une pièce jointe** — **SOUS la boucle, à l'extérieur** (utilisez le « + » de la flèche *sous* la carte « Anciennes versions », pas le « Ajouter une action » à l'intérieur) ; renommez-la `Ajouter PDF`

- Site et liste : les mêmes variables
- Id : **idDossier**
- Nom de fichier : **nomFichier** du déclencheur Power Apps (icône mauve), puis tapez `.pdf` (avec le point)
- Contenu du fichier : **Contenu du fichier**, venant de « Convertir un fichier »

## A.5 Les deux dernières actions

- **Supprimer un fichier** (OneDrive) : ne change pas. Elle supprime le fichier .html temporaire.
- **Répondre à une application ou à un flux Power Apps** : sortie **lien** = **URI absolu** (AbsoluteUri), venant de « Ajouter PDF ».

**Ordre final :**

1. Créer un fichier (OneDrive)
2. Convertir un fichier
3. Pieces jointes
4. Anciennes versions (Condition › Supprimer la pièce jointe)
5. Ajouter PDF
6. Supprimer un fichier (OneDrive)
7. Répondre à Power Apps

Cliquez sur **Enregistrer**.

> La liste Appreciations doit accepter les pièces jointes. C'est le réglage par défaut. Pour le vérifier : ⚙️ › Paramètres de la liste › Paramètres avancés › Pièces jointes = **Activé**.

# B. Modifier l'application (scrFormulaire)

**B.1 Actualiser le flux.** Dans le volet **Power Automate**, faites … › **Actualiser** sur GenererPDFAppreciation. C'est obligatoire, parce que ses entrées ont changé.

**B.2 Bouton Aperçu PDF.** Dans **btnApercuPDF.OnSelect**, collez tout le fichier `btnApercuPDF-OnSelect.txt` (nouvelle version).

**B.3 Supprimer les onglets Synthèse et Plan de développement.** Dans l'Arborescence (sous panelOnglets) :

- clic droit sur **panelSynthese** › **Supprimer** ;
- clic droit sur **panelPlan** › **Supprimer** (son bouton « Imprimer ce plan » part avec lui).

Puis **Revérifier tout** : l'erreur « Impossible d'utiliser la fonction Average avec une table vide » disparaît.

**B.4 Bouton « 📄 Ouvrir le PDF »** (s'il n'est pas déjà créé). Copiez **btnApercuPDF** (Ctrl+C, Ctrl+V), renommez la copie `btnOuvrirPDF`, puis :

- **Text** : `"📄 Ouvrir le PDF"`
- **Visible** : `!IsBlank(varLienPDF)`
- **OnSelect** : `Launch(varLienPDF)`

**B.5 Onglets.** Dans **scrFormulaire.OnVisible**, collez le fichier `scrFormulaire-OnVisible-corrige.txt` (nouvelle version). Seule la liste des onglets a changé :

```
ClearCollect(colTabs;
    {TabLabel: "← Retour au formulaire"; TabID: 1});;
```

Puis **tabBar.Visible** : `CurrentTabID <> 1`. La barre d'onglets disparaît du formulaire ; elle n'apparaît que dans l'aide (ouverte par **« ❓ Comment remplir ce formulaire »**, en haut à gauche), avec un seul bouton **« ← Retour au formulaire »**.

**B.6 Retirer le bandeau « Première fois ? »** Sélectionnez **aideCallout** (le bandeau avec le second bouton « Comment remplir ») :

- **Visible** : `false`
- **Height** : `0`

**B.7 Barre d'étapes.** Dans **galEtapes.Items**, sur la ligne de l'étape 6, remplacez `"Transmis à la paie"` par `"Transmis aux RH"`.

**B.8 stepDate.Text** :

```
If(ThisItem.Fait And Not(IsBlank(ThisItem.DateEtape)); Text(ThisItem.DateEtape; "d mmm yyyy"); "")
```

Faites aussi une recherche avec la **loupe 🔍** sur `[$-fr-CA]` : effacez-le partout où il reste.

# C. Bouton « 📄 PDF » dans Mes dossiers (scrMesDossiers)

1. Dans l'Arborescence, ouvrez **galDossiers › rowDossierWrap › rowDossier** et cliquez sur **btnOuvrir**.
2. Faites **Ctrl+C**, puis **Ctrl+V**. La copie apparaît dans la même ligne. Renommez-la `btnPDFDossier`.
3. Propriétés de **btnPDFDossier** :

**Text**

```
"📄 PDF"
```

**Width**

```
80
```

**Visible**

```
!IsEmpty(Filter(ThisItem.Attachments; EndsWith(DisplayName; ".pdf")))
```

> Si `Attachments` est souligné en rouge : effacez `Attachments`, tapez `ThisItem.` et choisissez la colonne des pièces jointes proposée par Power Apps (en français, elle peut s'appeler **'Pièces jointes'**). Faites la même chose dans OnSelect.

**OnSelect**

```
Launch(Coalesce(LookUp(ThisItem.Attachments; StartsWith(DisplayName; "Appreciation_")).AbsoluteUri; First(Filter(ThisItem.Attachments; EndsWith(DisplayName; ".pdf"))).AbsoluteUri))
```

Le bouton ouvre le PDF de **l'appréciation complète** joint au dossier.

**En-tête du tableau :** dans **tblHeader**, élargissez **hdrAction** à `190` pour qu'il couvre les deux boutons.

# D. Ménage

1. Dans la bibliothèque **Appreciations_PDF**, supprimez les PDF de test. Quand le nouveau flux fonctionne, **supprimez la bibliothèque** elle-même (⚙️ › Paramètres de la bibliothèque › Supprimer cette bibliothèque). Elle ne sert plus.
2. Les anciens PDF déjà créés ne sont pas joints aux dossiers : il suffit de refaire **Aperçu PDF** sur chaque dossier concerné.

# E. Tester

| N° | Test | Résultat attendu | ✓ |
|---|---|---|---|
| 1 | Ouvrir un dossier, puis Aperçu PDF | Message vert ; le bouton « 📄 Ouvrir le PDF » apparaît et ouvre le PDF | |
| 2 | Dans SharePoint, ouvrir l'élément du dossier | Une pièce jointe `Appreciation_dossierN.pdf` | |
| 3 | Refaire Aperçu PDF | Toujours **une seule** pièce jointe `Appreciation_dossierN.pdf`, mise à jour | |
| 4 | Mes dossiers | Le bouton 📄 PDF apparaît sur la ligne et ouvre le PDF | |
| 6 | Un dossier « Complété » | Le PDF se crée et s'ouvre aussi | |
| 7 | Un collègue sans lien | Ne voit ni le dossier ni le PDF | |
| 8 | Écran | Un seul bouton « Comment remplir » ; plus d'onglets Synthèse ni Plan ; aucune erreur Average ; étape 6 « Transmis aux RH » | |
