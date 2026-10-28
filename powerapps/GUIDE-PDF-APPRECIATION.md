---
title: "Guide — PDF de l'appréciation"
subtitle: "VERSION FINALE — 28 octobre 2026 · Application Power Apps « Appréciation de la contribution »"
lang: fr-CA
---

# Ce que vous obtenez

- **🖨️ Aperçu PDF** (barre de gauche) produit le **PDF complet** de l'appréciation, sur plusieurs pages :
  - identification et participants ;
  - sections A à F ;
  - évaluation globale ;
  - avis, certification et approbations.
- Le PDF est **joint au dossier**, comme pièce jointe de l'élément de la liste Appreciations : `Appreciation_dossierN.pdf`.
- **Une seule version** : chaque nouvelle demande **remplace** l'ancienne.
- Le PDF a **les mêmes accès que le dossier** : la personne, ses supérieurs, le directeur si requis et les RH. Personne d'autre.
- On l'ouvre avec **📄 Ouvrir le PDF**, dans le formulaire, ou avec **📄 PDF** sur la ligne du dossier, dans **Mes dossiers**.

**Comment ça marche :**

1. L'application assemble la page en HTML.
2. Le flux **GenererPDFAppreciation** la convertit en PDF avec **OneDrive Entreprise › Convertir un fichier**.
3. Le flux supprime l'ancienne pièce jointe du même nom et joint le nouveau PDF au dossier.
4. Le flux supprime le fichier temporaire.

Tout se fait avec des connecteurs **standard**, sans licence Premium.

**Fichiers fournis :**

| Fichier | Contenu |
|---|---|
| `btnApercuPDF-OnSelect.txt` | Formule du bouton Aperçu PDF |
| `FLUX-FINAUX.txt` (flux 3) | Le flux, action par action |
| `generer-formule-pdf.py` | Le programme qui produit la formule (pour la modifier) |

# Étape 1 — Préalable

La liste **Appreciations** doit accepter les pièces jointes. Pour le vérifier : **⚙️ › Paramètres de la liste › Paramètres avancés › Pièces jointes = Activé**. C'est le réglage par défaut.

# Étape 2 — Le flux GenererPDFAppreciation (dans la solution)

1. Ouvrez la solution, puis **+ Nouveau › Automatisation › Flux de cloud › Instantané**.
2. Nom : `GenererPDFAppreciation`. Déclencheur : **Power Apps (V2)**.
3. Quand une connexion est demandée, choisissez la **référence de connexion** de la solution : **SharePoint Appreciation** ou **OneDrive Appreciations**.

**Entrées du déclencheur, dans cet ordre :**

| N° | Type | Nom |
|---|---|---|
| 1 | Texte | `nomFichier` |
| 2 | Texte | `html` |
| 3 | Nombre | `idDossier` |

**Actions, dans cet ordre :**

1. **OneDrive Entreprise › Créer un fichier**
   - Dossier : `/`
   - Nom : **nomFichier**, puis tapez `.html`
   - Contenu : **html**
2. **OneDrive Entreprise › Convertir un fichier**
   - Fichier : **Id** (de l'action 1)
   - Type cible : **PDF**
3. **SharePoint › Obtenir les pièces jointes**, renommée `Pieces jointes`
   - Site : variable **Site Appréciations**
   - Liste : variable **Liste Appreciations**
   - Id : **idDossier**
4. **Contrôle › Appliquer à chacun**, renommée `Anciennes versions`, sur le **Corps** de « Pieces jointes ». Dedans, une **Condition** : **Nom d'affichage** *est égal à* l'expression (fx) `concat(triggerBody()?['text'], '.pdf')`.
   - **Si oui** : **SharePoint › Supprimer la pièce jointe**
     - Site et liste : idem
     - Id : **idDossier**
     - Id de la pièce jointe : **Id**
5. **SharePoint › Ajouter une pièce jointe**, renommée `Ajouter PDF`, **sous** la boucle
   - Site et liste : idem
   - Id : **idDossier**
   - Nom : **nomFichier**, puis tapez `.pdf`
   - Contenu : **Contenu du fichier** (de l'action 2)
6. **OneDrive Entreprise › Supprimer un fichier**
   - Fichier : **Id** (de l'action 1)
7. **Power Apps › Répondre à une application ou à un flux Power Apps**
   - Sortie **Texte** nommée `lien` = expression (fx) `body('Ajouter_PDF')?['AbsoluteUri']` — elle doit apparaître comme une **pastille**, pas comme du texte

Cliquez sur **Enregistrer**.

# Étape 3 — L'application

1. Dans le volet **Power Automate** : **+ Ajouter un flux**, puis **GenererPDFAppreciation**. Si le flux était déjà ajouté : **… › Actualiser**.
2. **btnApercuPDF.OnSelect** : collez `btnApercuPDF-OnSelect.txt`.
3. **btnOuvrirPDF** (copie de btnApercuPDF) :
   - **Text** : `"📄 Ouvrir le PDF"`
   - **Visible** : `!IsBlank(varLienPDF)`
   - **OnSelect** : `Launch(varLienPDF)`
4. *(Optionnel, plus tard)* **Mes dossiers** : bouton **📄 PDF** sur chaque ligne. Voir `FORMULES-POWERAPPS-FINALES.txt`, partie 11.

**Pourquoi un bouton « Ouvrir » ?** Le navigateur bloque l'ouverture automatique d'un onglet quand elle survient 10 à 30 secondes après le clic. C'est le temps que prend la création du PDF. Le bouton ouvre le PDF d'un seul clic, sans blocage.

# Étape 4 — Tester

| N° | Test | Résultat attendu |
|---|---|---|
| 1 | Aperçu PDF sur un dossier enregistré | Message vert, puis le bouton « 📄 Ouvrir le PDF » apparaît et ouvre le PDF |
| 2 | Élément du dossier dans SharePoint | Pièce jointe `Appreciation_dossierN.pdf` |
| 3 | Refaire Aperçu PDF | Toujours une seule pièce jointe de ce nom |
| 5 | Mes dossiers › 📄 PDF | Le PDF s'ouvre |
| 6 | Un collègue sans lien | Aucun accès au dossier ni au PDF |
| 7 | Formulaire jamais enregistré | Message « Enregistrez d'abord le dossier… » |

**Si un message rouge apparaît :** ouvrez le flux, puis **Historique des exécutions**, et la dernière exécution. L'action en rouge donne la cause.

- **`.lien` souligné en rouge dans l'application** : faites … › **Actualiser** sur le flux.
- **« Code de langue fr-CA non pris en charge »** : n'utilisez jamais « fr-CA » dans les formules. La formule fournie n'en contient pas.

# Pour les TI

- **Flux** GenererPDFAppreciation dans la solution.
- **Référence de connexion OneDrive Appreciations** (compte de service). Le fichier .html temporaire y passe et y est supprimé aussitôt.
- **Aucune bibliothèque à créer** : le PDF est joint au dossier, avec ses accès.
