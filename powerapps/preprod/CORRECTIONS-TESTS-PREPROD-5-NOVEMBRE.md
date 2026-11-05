---
title: "Corrections après les tests PréProd — Sécurité, ID, curseur et textes"
subtitle: "Application Appréciation de la contribution (SRHVQ) · Analyse de la solution 1.0.0.6 · 5 novembre 2026"
lang: fr-CA
---

# 1. Ce que révèle l'analyse de la solution 1.0.0.6

J'ai ouvert le fichier de la solution 1.0.0.6 pour lire les formules et les flux tels qu'ils sont réellement.

| Élément | État | Conséquence |
|---|---|---|
| Filtre de « Mes dossiers » (galDossiers) | ✅ Correct : lit le courriel directement | N'affiche que vos dossiers |
| Contrôle à l'ouverture d'un dossier | ✅ Présent | Bloque l'affichage d'un dossier où l'on n'est pas nommé |
| **Flux 1 — Permissions à la création** | ❌ **Retire encore le groupe « Membres » du site** (`associatedmembergroup`) | **Chaque dossier garde l'accès de SRHVQ_Utilisateurs, donc de tout le monde.** C'est la faille principale |
| ID de l'employé | ❌ Jamais rempli automatiquement | Il faut le taper (voir partie 3) |
| Saisie des objectifs | ❌ Le tableau se redessine après chaque champ | Le curseur saute ailleurs (voir partie 4) |
| Écrans À propos, Aide, confirmation de création | ⏳ Pas encore ajoutés | Conformité, à finir (guide de conformité, partie C) |

# 2. SÉCURITÉ — à faire en premier

## 2.1 Corriger le flux 1 (bac à sable, 5 minutes)

1. Solution › flux **Appréciation – Permissions à la création** › **Modifier**.
2. Ouvrez l'action **« Groupe Membres »**.
3. Dans le champ **URI**, remplacez `_api/web/associatedmembergroup?$select=Id` par :

```
_api/web/sitegroups/getbyname('SRHVQ_Utilisateurs')?$select=Id
```

4. **Enregistrer.**
5. **Test dans le bac à sable :** créez un dossier fictif, puis liste › ⋯ › **Gérer l'accès**. ✅ Ni SRHVQ_Utilisateurs, ni « Membres ». Seulement Propriétaires, le groupe RH et les personnes du dossier.

> Prérequis : le groupe **SRHVQ_Utilisateurs** existe sur le site du bac à sable, avec **Collaboration** sur la liste Appreciations (guide de conformité, B1).

## 2.2 Vérifier les autorisations de la liste PréProd (vous, sur le site)

Liste PréProd › ⚙️ › Paramètres de la liste › **Autorisations pour cette liste**. Il doit rester **exactement** :

| Nom | Niveau |
|---|---|
| Propriétaires du site | Contrôle total |
| SRHVQ_Utilisateurs (qui **contient** G-IS-APP-RH-SRHVQ-PreProd) | Collaboration |
| SRHVQ_RH | Lecture |

Si **G-IS-APP-RH-SRHVQ-PreProd** est sur la liste **directement**, retirez-le : il doit être **dans** SRHVQ_Utilisateurs (Personnes et groupes › SRHVQ_Utilisateurs). Sinon, le flux ne peut pas le retirer des dossiers.

## 2.3 Les dossiers déjà créés

Le flux 1 n'agit qu'à la **création**. Les dossiers de test existants gardent leur accès ouvert. Deux choix :
- **Recommandé :** les supprimer, puisque ce sont des données fictives.
- Sinon, dans **Gérer l'accès** de chaque dossier, retirer G-IS-APP / SRHVQ_Utilisateurs et ajouter les personnes du dossier.

## 2.4 Tester avec les bons comptes

Les **propriétaires du site** (dont vous) voient **tout**, c'est normal. Testez la confidentialité avec un collègue **non propriétaire** et **non nommé** dans le dossier : il ne doit le voir ni dans l'application, ni dans SharePoint, ni par un lien direct.

# 3. L'ID de l'employé

**Constat :** la formule de l'ID (`txtId.Default = varDossier.IdEmploye`) **relit seulement** ce qui a été enregistré. Rien ne le va chercher dans l'annuaire. Si Lucie voyait son ID, c'est qu'il avait été tapé et enregistré.

**Ce que je recommande :**

1. **Le rendre obligatoire.** La validation de btnDeposer (FORMULES-CONFORMITE, C4) bloque l'enregistrement si l'ID est vide.
2. **Un texte d'aide** dans le champ. txtId › **HintText** : `"Votre numéro d'employé"`
3. **(Facultatif) Essayer l'annuaire.** Dans txtId › Default, tapez `'Utilisateursd’Office365'.MyProfileV2().` et regardez si **employeeId** est proposé dans la liste.
   - S'il l'est, mettez : `Coalesce(varDossier.IdEmploye; 'Utilisateursd’Office365'.MyProfileV2().employeeId)`
   - S'il ne l'est pas, ou s'il reste vide à l'essai, la Ville ne publie pas ce numéro dans l'annuaire. Gardez la saisie manuelle.

# 4. Le curseur qui saute (section A)

**Cause :** à la sortie de chaque champ, l'application modifie la liste du tableau (`Patch(colObjActuels; ThisItem; …)`). Le tableau se **redessine**, et le curseur part ailleurs, parfois jusqu'à la section B.

**Correction :** on ne touche plus à la liste pendant la saisie. On recopie tout le tableau **au moment d'enregistrer**, d'ajouter ou de supprimer une ligne, ou de produire le PDF.

**1. Videz l'OnChange** des 5 champs : sélectionnez le champ › propriété **OnChange** › effacez tout.
- txtActObjectif, txtActIndicateur, txtActActions ;
- txtAveObjectif, txtAveIndicateur.

**2. La formule de recopie** (à placer aux endroits indiqués à l'étape 3) :

```
// Recopie les tableaux de la section A (écran -> collections), sans faire sauter le curseur
ClearCollect(colTmpAct; ForAll(galObjActuels.AllItems;
    {LigneID: LigneID; Objectif: txtActObjectif.Text; Indicateur: txtActIndicateur.Text; Actions: txtActActions.Text}));;
ClearCollect(colObjActuels; colTmpAct);;
ClearCollect(colTmpAve; ForAll(galObjAvenir.AllItems;
    {LigneID: LigneID; Objectif: txtAveObjectif.Text; Indicateur: txtAveIndicateur.Text}));;
ClearCollect(colObjAvenir; colTmpAve);;
```

**3. Où la placer :**

| Contrôle › propriété | Quoi faire |
|---|---|
| **btnDeposer › OnSelect** | Collez la recopie **au tout début** |
| **btnApercuPDF › OnSelect** | Collez la recopie **au tout début** |
| **btnAddActuel › OnSelect** | Recopie, puis la formule actuelle `Collect(colObjActuels; …)` |
| **btnAddAvenir › OnSelect** | Recopie, puis la formule actuelle `Collect(colObjAvenir; …)` |
| **btnActSupprimer › OnSelect** | Recopie, puis `RemoveIf(colObjActuels; LigneID = ThisItem.LigneID)` (remplace `Remove(colObjActuels; ThisItem)`) |
| **btnAveSupprimer › OnSelect** | Recopie, puis `RemoveIf(colObjAvenir; LigneID = ThisItem.LigneID)` |

✅ **Test :** tapez un objectif, faites **Tab** vers l'indicateur, puis cliquez dans les actions. Le curseur reste dans le tableau. Enregistrez, rouvrez : tout est là.

> La section D (développement) utilise le même principe. Si les testeurs y voient le même saut, on appliquera la même correction (colDevPrecedents, colDevNouveaux).

# 5. Les commentaires des testeurs, un à un

| N° | Commentaire | Réponse et correction |
|---|---|---|
| 1 | « Est-ce normal de voir tous les formulaires dans Mes dossiers ? » | **Non.** C'est la faille du flux 1 (partie 2). Dans la 1.0.0.6, le filtre de l'application est correct |
| 2 | Sans choisir le type de poste, on remplit sans la section B : pas clair | Ajouter une **bannière** (5.1) ; la validation bloque déjà l'enregistrement sans type de poste |
| 3 | Mon ID n'est pas renseigné automatiquement | Normal : il n'est jamais lu dans l'annuaire. Obligatoire et texte d'aide (partie 3) |
| 4 | Le curseur descend à la section B pendant la saisie des objectifs | Corrigé (partie 4) |
| 5 | Mettre plus foncés les « Précision » et « Note » | Couleur **RGBA(55; 65; 81; 1)** (5.2) |
| 6 | Changer « comportement attendu » par « démontré » | 4 étiquettes (5.3) |
| 7 | Un correcteur qui souligne les fautes en rouge | Fonction du **navigateur** (5.4), sans changement à l'application |
| 8 | Changer « certification » par « processus d'approbation » | Titre de la section G (5.5) |
| 9 | Préciser qu'il s'agit du directeur de service | Nouveau texte de la case (5.5) |
| 10 | « Avant approbation – aviser votre supérieur(e) immédiat(e) » | Nouveau titre du bloc Aviser (5.5) |
| 11 | Remplacer « il ou elle pourra » par « qui pourra » | Nouveau texte (5.5) |
| 12 | Ne pas pouvoir approuver avant d'avoir avisé le gestionnaire | Bouton « Approuver et soumettre » actif **seulement après Aviser** (5.6) |

## 5.1 Bannière « Choisissez votre type de poste »

En haut du formulaire, sous la barre d'étapes : **Insérer › Étiquette de texte**, nommée **lblChoisirPoste**.

| Propriété | Valeur |
|---|---|
| Text | `"⚠️ Choisissez d'abord votre type de poste (menu de gauche, « 2. Type de poste ») pour afficher le formulaire complet, dont la section B."` |
| Visible | `CurrentPosteID = ""` |
| Fill | `RGBA(255; 247; 230; 1)` |
| Color | `RGBA(146; 64; 14; 1)` |
| FontWeight | `FontWeight.Semibold` |
| AutoHeight | `true` (ou Height `44`) |
| PaddingLeft | `14` |

## 5.2 Notes et précisions plus foncées

Avec la loupe, cherchez **« Note : »** puis **« Précision : »**. Pour chaque étiquette trouvée (4 en tout) :

| Propriété | Valeur |
|---|---|
| Color | `RGBA(55; 65; 81; 1)` (au lieu de RGBA(107; 114; 128; 1)) |
| Italic | `false` (facultatif, plus lisible) |

## 5.3 « Comportement attendu » devient « Comportement démontré »

Loupe › **Comportement attendu** : 4 étiquettes (une par posture). Text : `"Comportement démontré"`

## 5.4 Le correcteur orthographique

Les champs de l'application sont vérifiés par le **navigateur**. Dans **Edge** :
1. **Paramètres** › **Langues** ;
2. activez **« Activer la vérification grammaticale et orthographique »** ;
3. ajoutez **Français (Canada)**.

Les fautes sont alors soulignées en rouge, avec un clic droit pour les corriger. À indiquer dans le guide d'utilisation.

## 5.5 Les textes de la section G

| Où (chercher avec la loupe) | Nouveau texte |
|---|---|
| Section G — Confirmation et chaîne d'approbation | **Section G — Processus d'approbation** |
| Case chkDirRequis (« Une approbation du directeur / de la directrice de service est requise… ») | **Cochez cette case si la directrice ou le directeur de service est une personne autre que la ou le supérieur(e) hiérarchique.** |
| Titre du bloc « 📨 Aviser le supérieur immédiat » (le titre, **pas** le bouton) | **Avant l'approbation — aviser votre supérieur(e) immédiat(e)** |
| « Une fois votre partie remplie, avisez votre supérieur(e) immédiat(e) : il ou elle pourra consulter… » | **Une fois votre partie remplie, avisez votre supérieur(e) immédiat(e), qui pourra consulter votre version dans « Mes dossiers » et planifier la rencontre.** |
| btnCertifier › OnSelect : « Formulaire certifié et soumis au supérieur immédiat. » | **Formulaire approuvé et soumis au supérieur immédiat.** |

Pensez aussi au **PDF** : dans btnApercuPDF, le titre « Section G — Confirmation et chaîne d'approbation » devient « Section G — Processus d'approbation » (Rechercher et remplacer).

## 5.6 Aviser le supérieur avant d'approuver (obligatoire)

**btnCertifier › DisplayMode** :

```
If(chkCert.Checked && Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur";
    DisplayMode.Edit; DisplayMode.Disabled)
```

**chkCert › DisplayMode**, pour ne pas pouvoir cocher avant d'avoir avisé :

```
If(Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur" && CurrentRoleID = "cadre";
    DisplayMode.Edit; DisplayMode.Disabled)
```

Ajoutez une petite étiquette sous la case, **Visible** : `Coalesce(varDossier.Statut.Value; "Brouillon") = "Brouillon"`, avec le texte :

`"Avisez d'abord votre supérieur(e) immédiat(e) et tenez la rencontre : vous pourrez ensuite approuver et soumettre."`

> **À décider avec vous :** le testeur souhaite aussi recevoir la **version de son gestionnaire** avant d'approuver. Aujourd'hui, le SI met ses cotes **après** la confirmation de la personne. Pour inverser cet ordre (le SI remplit, puis la personne approuve), il faudrait une étape de plus dans le circuit. C'est une décision de processus RH : dites-moi si vous la souhaitez.

# 6. Mettre en PréProd

1. Faites les parties 2.1, 3, 4 et 5 dans le **bac à sable**, puis **Enregistrer** et **Publier**.
2. Exportez en **gérée**, version **1.0.0.7**.
3. Les TI importent en **mise à niveau**, puis **désactivent et réactivent** les flux 1 et 2.
4. Supprimez les anciens dossiers de test (2.3).
5. Retestez avec un collègue non propriétaire (2.4).
