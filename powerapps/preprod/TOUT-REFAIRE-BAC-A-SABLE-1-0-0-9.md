---
title: "Tout refaire dans le bac à sable : de la version 1.0.0.5 à la version 1.0.0.9"
subtitle: "Plan complet, étape par étape · 9 novembre 2026 · fichier de formules : FORMULES-1-0-0-5-VERS-1-0-0-9.txt"
lang: fr-CA
---

# 1. Ce qui se passe dans la nouvelle PréProd

## Ce que j'ai vérifié

J'ai comparé, contrôle par contrôle, la solution **1.0.0.5** que vous m'avez envoyée (exportée le **4 novembre**) et la **1.0.0.8** (6 novembre).

- La 1.0.0.5 ne contient **aucun** des changements faits depuis le 4 novembre : nouvelle étape, libellés, sécurité, couleurs, curseur, etc.
- Entre les deux, **52 contrôles** de l'application, **2 flux** et **1 colonne SharePoint** ont changé. Tout est dans ce guide et dans le fichier de formules.

## Pourquoi le dossier bloque après « Aviser le supérieur »

Regardez d'abord **quelle version est installée** dans la nouvelle PréProd : make.powerapps.com › environnement PréProd › **Solutions** › colonne **Version**.

| Version installée | Ce qui se passe après « Aviser » | Pourquoi ça bloque |
|---|---|---|
| **1.0.0.5** | La personne doit cocher « Je certifie… » puis cliquer sur **Certifier et soumettre** (section G). Le supérieur ne peut rien faire avant : c'est prévu ainsi dans cette version. | Si ce bloc n'apparaît pas, les choix de la colonne **Statut** de la nouvelle liste ne sont pas exactement les mêmes (voir 3.2). |
| **1.0.0.8** | La personne attend la version du supérieur (« Approuver et soumettre » grisé). Le supérieur doit cliquer sur **Transmettre ma version**. | **Deux erreurs** : (1) le courriel « Aviser » part vers **la personne elle-même** au lieu du supérieur (flux 2) ; (2) si la nouvelle liste n'a pas la colonne **VersionSILe**, « Transmettre ma version » échoue. Les deux restent bloqués : c'est exactement ce que vous voyez. |

## Débloquer un dossier de test tout de suite

1. Ouvrez la liste **SRHVQ_Appreciations** du site PréProd.
2. Sélectionnez le dossier › **Modifier**.
3. **Statut** = Brouillon ; videz **AviseLe**. Enregistrez.

Ou supprimez simplement les dossiers de test.

# 2. Avant de commencer : faites une copie de sécurité

1. Bac à sable › **Solutions** › Solution-ApplicationAppréciation › **Exporter** › **Non gérée**.
2. Gardez ce ZIP. Si quelque chose tourne mal, vous pourrez revenir en arrière.
3. Travaillez **toujours** dans la solution **non gérée** du bac à sable.

# 3. SharePoint

## 3.1 Nouvelle colonne VersionSILe (bac à sable ET PréProd)

À faire dans la liste **Appreciations du bac à sable**, et à demander aux TI pour la liste **SRHVQ_Appreciations de la PréProd**.

1. Ouvrez la liste › **+ Ajouter une colonne** › **Date et heure** › Suivant.
2. Nom : **VersionSILe** (exactement : V, S, I, L majuscules, sans espace ni accent).
3. **Inclure l'heure** : Oui. Ne pas rendre obligatoire. **Enregistrer**.
4. Vous pourrez ensuite renommer l'affichage en « Version du SI transmise le » : le nom interne restera VersionSILe.

## 3.2 Choix de la colonne Statut (à vérifier dans les deux listes)

Paramètres de la colonne **Statut** : les 7 choix doivent être écrits **exactement** ainsi, un par ligne :

```
Brouillon
Avisé au supérieur
Certifié
Approuvé SI
Approuvé SH
Approuvé directeur
Complété
```

Ne changez pas « Certifié » : l'application l'affiche « Confirmé ».

## 3.3 Sécurité de la liste (déjà fait en PréProd, à vérifier)

- **G-IS-APP-…** est **membre du groupe SharePoint SRHVQ_Utilisateurs**, jamais directement sur la liste.
- SRHVQ_Utilisateurs : **Collaboration** sur la liste ; aucun droit sur le site.

# 4. Les flux (bac à sable)

## 4.1 Flux 1 — Permissions à la création

1. Ouvrez le flux › **Modifier**.
2. Action **« Groupe Membres »** (Envoyer une requête HTTP à SharePoint) › champ **Uri** : effacez et collez :

```
_api/web/sitegroups/getbyname('SRHVQ_Utilisateurs')?$select=Id
```

3. **Enregistrer**.

La 1.0.0.5 retirait le groupe « Membres » du site au lieu de SRHVQ_Utilisateurs : tout le monde voyait tous les dossiers.

## 4.2 Flux 2 — Suivi des étapes

**a) Corriger le destinataire du courriel « Aviser » (erreur de la 1.0.0.8)**

1. Ouvrez **Statut changé** › **Selon le statut** › cas **Avisé au supérieur** › **Envoyer un e-mail (V2)**.
2. Champ **À** : supprimez ce qui s'y trouve › **Expression** (fx) › collez › **Ajouter** :

```
triggerOutputs()?['body/CourrielSI']
```

3. Corps du courriel : remplacez par :

> Bonjour,
>
> [Titre] a complété sa partie du formulaire d'appréciation de la contribution. Vous pouvez la consulter, compléter votre partie (cotes de la section B, bilan de la section E et évaluation globale), puis la lui transmettre avec le bouton « Transmettre ma version » avant la rencontre.
>
> Ouvrir le formulaire (lien)

**b) Courriel du cas « Certifié »** (au supérieur) : remplacez « a approuvé son appréciation » par **« a confirmé et approuvé son formulaire d'appréciation »**.

**c) Nouvelle condition « Version SI transmise »**

1. Sous la condition **Directeur ajouté** (au premier niveau du flux, pas à l'intérieur), cliquez sur **+** › **Condition**. Renommez-la **Version SI transmise**.
2. Ligne 1 : à gauche, Expression : `body('Changements')?['ColumnHasChanged']?['VersionSILe']` ; **est égal à** ; à droite, Expression : `true`.
3. **+ Ajouter** › **Ajouter une ligne** (opérateur **Et**). Ligne 2 : à gauche, Expression : `triggerOutputs()?['body/VersionSILe']` ; **n'est pas égal à** ; à droite : laissez vide.
4. Branche **Si oui** › **Ajouter une action** › Office 365 Outlook › **Envoyer un e-mail (V2)** :
   - **À** (Expression) : `triggerOutputs()?['body/CourrielPersonne']`
   - **Objet** : `Appréciation : la version de votre supérieur(e) est prête`
   - **Corps** : « Bonjour, Votre supérieur(e) immédiat(e) a complété sa partie de votre formulaire d'appréciation de la contribution (cotes, bilan et évaluation globale). Vous pouvez la consulter avant votre rencontre. Après la rencontre, vous pourrez approuver et soumettre le formulaire. » + le lien **LienApp** (même chose que dans les autres courriels).
5. **Enregistrer**. Vérifiez qu'il n'y a **aucune erreur** (Vérificateur de flux).

## 4.3 Flux 3 — GenererPDFAppreciation (erreur Outlook en PréProd)

1. Flux › page **Détails** › **Utilisateurs exécutant uniquement** › **Modifier**.
2. Pour les **3** connexions (OneDrive, SharePoint, Office 365 Outlook) : choisissez **la connexion du compte de service** au lieu de « Fournie par l'utilisateur exécutant uniquement ».
3. **Enregistrer**.

# 5. L'application (bac à sable)

Ouvrez l'application dans Power Apps Studio (**Modifier**). Gardez le fichier **FORMULES-1-0-0-5-VERS-1-0-0-9.txt** ouvert à côté.

**Méthode pour chaque numéro [1] à [55] du fichier :**

1. Loupe de l'arborescence › tapez le **nom du contrôle** › cliquez dessus.
2. Liste déroulante des propriétés (à gauche de la barre de formule) › choisissez la propriété.
3. Barre de formule : **Ctrl + A**, puis collez les lignes du fichier.
4. Pas de soulignement rouge ? Passez au suivant.

Faites-les **dans l'ordre**, par bloc :

| Étape | Numéros | Ce que ça change |
|---|---|---|
| 5.1 | [1] | Ouverture de l'écran : sécurité, rôles, libellé « Directeur / directrice de service » |
| 5.2 | [2] à [6] | Bandeau bleu, bouton d'aide qui ramène au formulaire, enregistrement et PDF (recopie des tableaux) |
| 5.3 | [7] [8] | Barre d'étapes à 8 étapes |
| 5.4 | [59] | Bannière « Choisissez votre type de poste » (nouveau contrôle, voir plus bas) |
| 5.5 | [9] | Numéro d'employé obligatoire |
| 5.6 | [10] à [18] | Curseur qui ne saute plus dans les tableaux de la section A |
| 5.7 | [19] à [31] | Section B : « Comportement démontré » ; cotes du supérieur cachées jusqu'à sa version |
| 5.8 | [32] [33] | Section E et évaluation globale cachées à la personne jusqu'à la version du supérieur |
| 5.9 | [34] à [49] | Section G : textes, « Approuver et soumettre », hauteur du bloc du supérieur |
| 5.10 | [56] à [58] | Bouton « Transmettre ma version » (nouveaux contrôles, voir plus bas) |
| 5.11 | [50] | Aide « Comment remplir » : 7 étapes à jour |
| 5.12 | [51] à [55] | Écran Mes dossiers : rôles, filtre « À approuver par moi », pastille « Confirmé » |

## 5.4 Créer la bannière lblChoisirPoste

1. Arborescence : cliquez sur le conteneur **mainScroll**.
2. **Insérer** › **Étiquette de texte**. Elle s'ajoute à la fin de mainScroll.
3. Renommez-la **lblChoisirPoste** (double-clic sur le nom).
4. Glissez-la juste **sous stepperWrap** dans l'arborescence.
5. Appliquez les propriétés du numéro **[59]**.

**Important :** ne la mettez **pas** dans la barre d'étapes (galEtapes) : c'était l'erreur de la 1.0.0.8.

## 5.10 Créer le bloc « Transmettre ma version »

1. Arborescence : section G › **sigSI** › cliquez sur **sigSIAction**.
2. **Ctrl + C**, puis cliquez sur **sigSI** et **Ctrl + V**. Une copie apparaît (sigSIAction_1, avec chkApprSI_1 et btnApprSI_1).
3. Renommez : sigSIAction_1 → **sigSITransmettre** ; chkApprSI_1 → **chkTransSI** ; btnApprSI_1 → **btnTransSI**.
4. Glissez **sigSITransmettre** juste **au-dessus de sigSIAction** (sous sigSIDetail).
5. Appliquez les numéros **[56]**, **[57]** et **[58]**, puis vérifiez **[43]** (hauteur de sigSI).

## 5.13 Vérifier

1. Icône **Vérificateur d'application** (stéthoscope, en haut à droite) : **0 erreur**.
2. **Enregistrer**, puis **Publier**.

# 6. La solution

1. Solution › **Variables d'environnement** : la variable « SandBox Annie Audet… » (`rhdsst_shared_sharepointonline_9db72454…`) › **⋯ › Supprimer de cette solution** (pas « Supprimer »).
2. **Publier toutes les personnalisations**.
3. **Exporter** › **Gérée** › version **1.0.0.9**. Exportez aussi une **non gérée** pour vous.

# 7. Tests dans le bac à sable (avant d'envoyer aux TI)

Avec 2 comptes : vous (personne) et un collègue inscrit comme votre supérieur(e) immédiat(e).

| # | Qui | Action | Résultat attendu |
|---|---|---|---|
| 1 | Personne | Nouveau formulaire, remplir, Enregistrer | Dossier créé ; le collègue sans lien ne le voit pas |
| 2 | Personne | **Aviser le supérieur** | Le **supérieur** reçoit le courriel (pas la personne) ; « Approuver et soumettre » grisé |
| 3 | Supérieur | Cotes B, section E, évaluation globale, **Transmettre ma version** | La personne reçoit « la version de votre supérieur(e) est prête » ; étape 2 ✓ |
| 4 | Personne | Coche « Je confirme… », **Approuver et soumettre** | Contenu verrouillé ; le supérieur reçoit « À approuver » |
| 5 | Supérieur | Coche, **Approuver** | Le supérieur hiérarchique reçoit « À approuver » |
| 6 | — | Jusqu'à **Complété** | Courriel aux RH et à tous ; lecture seule |
| 7 | Les deux | **Aperçu PDF** | PDF créé, sans erreur Outlook |
| 8 | Personne | **❓ Comment remplir**, puis le même bouton | Retour au formulaire |

# 8. Ce que les TI doivent faire dans la PréProd

1. Ajouter la colonne **VersionSILe** à la liste SRHVQ_Appreciations (3.1) et vérifier les choix de **Statut** (3.2).
2. Importer la **1.0.0.9** gérée (**mise à niveau**).
3. Vérifier les **références de connexion** (compte de service) et les **valeurs des variables** (site et listes de la nouvelle PréProd).
4. Flux 3 : **Utilisateurs exécutant uniquement** = connexions du compte de service (4.3).
5. Désactiver puis réactiver les **3 flux**.
6. Refaire les tests de la section 7.
