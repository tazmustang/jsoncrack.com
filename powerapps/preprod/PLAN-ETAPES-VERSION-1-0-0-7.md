---
title: "Plan unique — Toutes les modifications de la version 1.0.0.7, une étape à la fois"
subtitle: "Application Appréciation de la contribution (SRHVQ) · Remplace les documents du 5 et du 6 novembre · Cochez chaque case"
lang: fr-CA
---

# Comment utiliser ce plan

- Faites les étapes **dans l'ordre**, et cochez ☐ chaque étape terminée.
- J'ai vérifié votre solution **1.0.0.6** : ce plan contient **seulement ce qui reste à faire**.
- Partout : **gardez les guillemets** des textes, et collez les formules dans la **barre fx**.
- Durée totale : environ **2 h 30**. Vous pouvez arrêter entre deux parties.

| Partie | Où | Durée |
|---|---|---|
| 1 | Site SharePoint **PréProd** | 20 min |
| 2 | Site SharePoint du **bac à sable** | 10 min |
| 3 | **Application** (bac à sable) | 1 h 30 |
| 4 | **Flux** (bac à sable) | 20 min |
| 5 | **Tests** (bac à sable) | 20 min |
| 6 | **Export** et PréProd | 10 min, puis les TI |

# PARTIE 1 — Site SharePoint PréProd (RH Power Apps Données PréProd)

## ☐ Étape 1 — Le groupe SRHVQ_Utilisateurs contient le groupe des testeurs

1. Site PréProd › ⚙️ › **Paramètres du site** › **Personnes et groupes**.
2. Dans la colonne de gauche, cliquez sur **SRHVQ_Utilisateurs**.
   - S'il n'existe pas : ⚙️ › Autorisations du site › Paramètres d'autorisations avancés › **Créer un groupe**, nom `SRHVQ_Utilisateurs`, **aucune case cochée** en bas › **Créer**.
3. Dans le groupe : **Nouveau** › **Ajouter des utilisateurs** › tapez `G-IS-APP-RH-SRHVQ-PreProd` › choisissez-le › **Partager**.

✅ Le groupe SRHVQ_Utilisateurs contient **G-IS-APP-RH-SRHVQ-PreProd**.

## ☐ Étape 2 — Les autorisations de la liste des dossiers

1. Ouvrez la liste **SRHVQ_Appréciation de la contribution des cadres** › ⚙️ › **Paramètres de la liste** › **Autorisations pour cette liste**.
2. Si **G-IS-APP-RH-SRHVQ-PreProd** apparaît **directement** dans la liste : cochez-le › **Supprimer les autorisations utilisateur** › OK.
3. **Accorder des autorisations** › `SRHVQ_Utilisateurs` › **Afficher les options** › niveau **Collaboration** › décochez l'invitation › **Partager**.
4. **Accorder des autorisations** › `SRHVQ_RH` › niveau **Lecture** › **Partager**.

✅ Il reste **exactement** :

| Nom | Niveau |
|---|---|
| Propriétaires de RH Power Apps Données PréProd | Contrôle total |
| SRHVQ_Utilisateurs | Collaboration |
| SRHVQ_RH | Lecture |

## ☐ Étape 3 — Nouvelle colonne VersionSILe

1. Même liste › ⚙️ › Paramètres de la liste › **Créer une colonne**.
2. Nom : `VersionSILe` (exactement, sans espace ni accent).
3. Type : **Date et heure** › format **Date et heure** › **OK**.

## ☐ Étape 4 — Supprimer les dossiers de test

Dans la liste, cochez tous les dossiers de test › **Supprimer**. Ils ont été créés sans la bonne protection ; on recommencera avec de nouveaux dossiers.

# PARTIE 2 — Site SharePoint du bac à sable (SandBoxAnnieAudet)

## ☐ Étape 5 — Le groupe SRHVQ_Utilisateurs dans le bac à sable

1. Même démarche qu'aux étapes 1 et 2, sur le site **SandBoxAnnieAudet**, liste **Appreciations** :
   - groupe **SRHVQ_Utilisateurs** créé (aucun droit sur le site), avec vos **testeurs** dedans ;
   - liste Appreciations : héritage arrêté, **Membres** et **Visiteurs** retirés, **SRHVQ_Utilisateurs = Collaboration**.

> Sans ce groupe, le flux 1 corrigé (étape 19) échouera dans le bac à sable.

## ☐ Étape 6 — Colonne VersionSILe dans le bac à sable

Liste **Appreciations** du bac à sable › Créer une colonne `VersionSILe`, **Date et heure** (comme l'étape 3).

# PARTIE 3 — L'application (bac à sable)

Ouvrez la solution › **Appréciation de la contribution** › **Modifier**.

## ☐ Étape 7 — Actualiser la liste dans l'application

Barre de gauche › icône **Données** (cylindre) › **⋯** à côté de **Appreciations** › **Actualiser**.

## ☐ Étape 8 — Réparer la barre d'étapes (8 étapes)

Votre formule actuelle contient tout le texte du fichier (« 1) Contrôle : galEtapes… »), ce qui cause une trentaine d'erreurs.

1. Arborescence : **galEtapes** › propriété **Items** › **Ctrl + A** › **Suppr**.
2. Ouvrez **barre-etapes-formules.txt**. Copiez **seulement** de `With(` jusqu'à `false}))`, sans le titre ni les lignes `-----`. Collez.
3. **galEtapes › TemplateSize** : `Self.Width / 8`
4. Dans galEtapes, **stepLineRight › Visible** : `ThisItem.Ordre < 8`

✅ Le vérificateur (stéthoscope) n'indique plus d'erreur dans galEtapes.

## ☐ Étape 9 — L'ID de l'employé

> **Mise à jour du 7 novembre :** `employeeId` n'est pas disponible dans le connecteur. Utilisez simplement `varDossier.IdEmploye` dans Default (voir ID-COULEURS-LOGO-FLUX-7-NOVEMBRE.docx). La formule ci-dessous est remplacée.

1. **txtId › Default** :

```
// ID : celui du dossier ; sinon, pour la personne en appréciation, celui de l'annuaire
If(!IsBlank(varDossier.IdEmploye);
    varDossier.IdEmploye;
    CurrentRoleID = "cadre";
    'Utilisateursd’Office365'.MyProfileV2().employeeId;
    "")
```

> En tapant `MyProfileV2().`, vérifiez que **employeeId** est proposé. Tapez « Util » et choisissez le connecteur dans la liste plutôt que de coller son nom.

2. **txtId › HintText** (ou Placeholder) : `"Votre numéro d'employé"`

## ☐ Étape 10 — Bannière « Choisissez votre type de poste »

1. Cliquez dans le conteneur juste **sous la barre d'étapes** › **Insérer › Étiquette de texte**. Renommez-la **lblChoisirPoste**.
2. Propriétés :

| Propriété | Valeur |
|---|---|
| Text | `"⚠️ Choisissez d'abord votre type de poste (menu de gauche, « 2. Type de poste ») pour afficher le formulaire complet, dont la section B."` |
| Visible | `CurrentPosteID = ""` |
| Fill | `RGBA(255; 247; 230; 1)` |
| Color | `RGBA(146; 64; 14; 1)` |
| FontWeight | `FontWeight.Semibold` |
| AutoHeight | `true` |
| PaddingLeft | `14` |

## ☐ Étape 11 — Le curseur qui saute (section A)

**a) Videz l'OnChange de ces 5 champs** (sélectionnez le champ › propriété **OnChange** › effacez tout) :
- txtActObjectif, txtActIndicateur, txtActActions ;
- txtAveObjectif, txtAveIndicateur.

**b) btnDeposer › OnSelect** : cliquez **au tout début** de la formule et collez :

```
// Recopie les tableaux de la section A (écran -> collections), sans faire sauter le curseur
ClearCollect(colTmpAct; ForAll(galObjActuels.AllItems;
    {LigneID: LigneID; Objectif: txtActObjectif.Text; Indicateur: txtActIndicateur.Text; Actions: txtActActions.Text}));;
ClearCollect(colObjActuels; colTmpAct);;
ClearCollect(colTmpAve; ForAll(galObjAvenir.AllItems;
    {LigneID: LigneID; Objectif: txtAveObjectif.Text; Indicateur: txtAveIndicateur.Text}));;
ClearCollect(colObjAvenir; colTmpAve);;
```

**c) Les 4 boutons des tableaux** : collez **le même bloc au début**, puis gardez ou remplacez la suite comme suit.

| Bouton › OnSelect | Après le bloc de recopie |
|---|---|
| btnAddActuel | garder la formule actuelle `Collect(colObjActuels; …)` |
| btnAddAvenir | garder la formule actuelle `Collect(colObjAvenir; …)` |
| btnActSupprimer | remplacer `Remove(colObjActuels; ThisItem)` par `RemoveIf(colObjActuels; LigneID = ThisItem.LigneID)` |
| btnAveSupprimer | remplacer `Remove(colObjAvenir; ThisItem)` par `RemoveIf(colObjAvenir; LigneID = ThisItem.LigneID)` |

## ☐ Étape 12 — Recoller la formule du PDF

**btnApercuPDF › OnSelect** › Ctrl + A › Suppr › collez tout **btnApercuPDF-OnSelect.txt** (mis à jour le 6 novembre). Il contient déjà :
- la recopie des tableaux ;
- la section G « Processus d'approbation » ;
- la ligne « Version transmise par le supérieur immédiat » ;
- le type « Autre » et « Directeur / directrice de service ».

## ☐ Étape 13 — Les textes demandés par les testeurs

Pour chaque ligne : **loupe 🔍** (barre de gauche) › tapez le début du texte actuel › cliquez sur le résultat › remplacez dans la barre fx.

| Contrôle (ce que vous trouverez) | Propriété | Nouveau texte |
|---|---|---|
| 4 étiquettes « Comportement attendu » | Text | `"Comportement démontré"` |
| gTitle (« Section G — Confirmation et chaîne d'approbation ») | Text | `"Section G — Processus d'approbation"` |
| chkDirRequis | Label | `"Cochez cette case si la directrice ou le directeur de service est une personne autre que la ou le supérieur(e) hiérarchique."` |
| avisTitle (« 📨 Aviser le supérieur immédiat », le **titre** du bloc, pas le bouton) | Text | `"Avant l'approbation — aviser votre supérieur(e) immédiat(e)"` |
| avisText (« … il ou elle pourra consulter… ») | Text | `"Une fois votre partie remplie, avisez votre supérieur(e) immédiat(e), qui pourra consulter votre version dans « Mes dossiers » et planifier la rencontre."` |
| btnCertifier | OnSelect | dans la formule, remplacez `"Formulaire certifié et soumis au supérieur immédiat."` par `"Formulaire approuvé et soumis au supérieur immédiat."` |
| Message « 🔒 Le contenu est verrouillé depuis la certification… » | Text | `"🔒 Le contenu est verrouillé depuis votre approbation. Seules les étapes d'approbation restent actives."` |
| Aide « Comment remplir » (aideHtml) : « coche la certification et soumet » | HtmlText | Rechercher et remplacer : `coche la certification et soumet` par `approuve et soumet` ; `Après la certification` par `Après son approbation` |

**Notes et précisions plus foncées** : loupe › **« Note : »**, puis **« Précision : »**. Pour chacune des 4 étiquettes :
- **Color** : `RGBA(55; 65; 81; 1)` ;
- **Italic** : `false`.

## ☐ Étape 14 — Nouvelle étape : le bouton « Transmettre ma version » (supérieur immédiat)

1. Arborescence : dépliez **sigSI** › cliquez sur **sigSIAction**.
2. **Ctrl + C**, puis **Ctrl + V**. Une copie apparaît : sigSIAction_1, avec chkApprSI_1 et btnApprSI_1.
3. Renommez (double-clic sur le nom) : **sigSITransmettre**, **chkTransSI**, **btnTransSI**.
4. Glissez **sigSITransmettre** juste **au-dessus** de sigSIAction (toujours dans sigSI).
5. Propriétés :

| Contrôle › propriété | Formule |
|---|---|
| sigSITransmettre › Visible | `Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur" And CurrentRoleID = "superieur_immediat" And IsBlank(varDossier.VersionSILe)` |
| sigSITransmettre › Height | `Self.PaddingTop + chkTransSI.Height + 8 + btnTransSI.Height + Self.PaddingBottom` |
| chkTransSI › Label | `"Ma version est complète (cotes de la section B, bilan de la section E et évaluation globale). Je la transmets à la personne pour la rencontre."` |
| btnTransSI › Text | `"📨 Transmettre ma version"` |
| btnTransSI › DisplayMode | `If(chkTransSI.Checked; DisplayMode.Edit; DisplayMode.Disabled)` |

6. **btnTransSI › OnSelect** (remplacez tout) :

```
// Transmet la version du supérieur immédiat à la personne, avant sa confirmation (le flux 2 l'avise par courriel)
Set(varDossier; Patch(Appreciations; varDossier; {VersionSILe: Now()}));;
Select(btnDeposer);;
Reset(chkTransSI);;
Notify("Votre version est transmise. La personne en appréciation est avisée par courriel."; NotificationType.Success)
```

7. **sigSI › Height** : cliquez **à la fin** de la formule actuelle et ajoutez :

```
 + If(sigSITransmettre.Visible; 8 + sigSITransmettre.Height; 0)
```

## ☐ Étape 15 — La personne approuve seulement après avoir reçu la version

| Contrôle › propriété | Formule |
|---|---|
| chkCert › DisplayMode | `If(!IsBlank(varDossier.VersionSILe) && Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur" && CurrentRoleID = "cadre"; DisplayMode.Edit; DisplayMode.Disabled)` |
| chkCert › Label | `If(IsBlank(varDossier.VersionSILe); "En attente de la version de votre supérieur(e) immédiat(e) : vous recevrez un courriel quand elle sera prête."; "Je confirme avoir pris connaissance du contenu de ce formulaire et je l'approuve.")` |
| btnCertifier › DisplayMode | `If(chkCert.Checked && !IsBlank(varDossier.VersionSILe) && Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur"; DisplayMode.Edit; DisplayMode.Disabled)` |

## ☐ Étape 16 — La partie du supérieur s'affiche à la personne après la transmission

| Contrôle(s) › Visible | Formule |
|---|---|
| **8 contrôles** : p1HdrSup, p2HdrSup, p3HdrSup, p4HdrSup, p1CboSup, p2CboSup, p3CboSup, p4CboSup | `CurrentRoleID <> "cadre" Or (!IsBlank(varDossier.VersionSILe) And CountRows(Filter(colComportements; CoteSup <> "")) > 0)` |
| cardSectionE | `CurrentRoleID = "superieur_immediat" Or (Not(IsBlank(varDossier.BilanSuperieur)) And (CurrentRoleID <> "cadre" Or !IsBlank(varDossier.VersionSILe)))` |
| cardEval | `CurrentRoleID = "superieur_immediat" Or (varEvalGlobale <> "" And (CurrentRoleID <> "cadre" Or !IsBlank(varDossier.VersionSILe)))` |

> Astuce pour les 8 contrôles : sélectionnez le premier, mettez la formule, puis Ctrl + C dans la barre fx et Ctrl + V dans les 7 autres.

## ☐ Étape 17 — « À approuver par moi » inclut la nouvelle étape

Écran **scrMesDossiers** › **galDossiers › Items**. Remplacez **seulement** les 4 lignes qui commencent par `"afaire";` :

```
"afaire"; (CourrielSI = moi And Statut.Value = "Avisé au supérieur" And IsBlank(VersionSILe))
    Or (CourrielSI = moi And Statut.Value = "Certifié")
    Or (CourrielSH = moi And Statut.Value = "Approuvé SI")
    Or (CourrielDirecteur = moi And Statut.Value = "Approuvé SH");
```

## ☐ Étape 18 — Vérifier, enregistrer, publier

1. **Vérificateur d'application** (stéthoscope) : **0 erreur** dans « Formules ».
2. **Enregistrer** › **Publier**.

# PARTIE 4 — Les flux (bac à sable)

## ☐ Étape 19 — Flux 1 : retirer SRHVQ_Utilisateurs (la sécurité)

1. Solution › **Appréciation – Permissions à la création** › **Modifier**.
2. Action **« Groupe Membres »** › champ **URI** : remplacez `_api/web/associatedmembergroup?$select=Id` par :

```
_api/web/sitegroups/getbyname('SRHVQ_Utilisateurs')?$select=Id
```

3. **Enregistrer.**

## ☐ Étape 20 — Flux 2 : le courriel « la version de votre supérieur est prête »

1. Solution › **Appréciation – Suivi des étapes** › **Modifier**.
2. Sous la condition **« Directeur ajouté »**, à l'extérieur de celle-ci, cliquez sur **+** › **Condition**. Renommez-la `Version SI transmise`. Elle doit être **avant** « Statut changé ».
3. **Ligne 1** :
   - à gauche (expression fx) : `body('Changements')?['ColumnHasChanged']?['VersionSILe']`
   - **est égal à**
   - à droite (expression fx) : `true`
4. **+ Ajouter une ligne (ET)** :
   - à gauche (expression fx) : `triggerOutputs()?['body/VersionSILe']`
   - **n'est pas égal à**
   - à droite : laissez **vide**
5. **Si oui** › **+** › **Office 365 Outlook › Envoyer un courriel (V2)** (connexion **Outlook Appreciations**) :
   - **À** : CourrielPersonne (contenu dynamique) ;
   - **Objet** : `Appréciation : la version de votre supérieur(e) immédiat(e) est prête` ;
   - **Corps** (bouton **</>**, mode code) :

```
Bonjour,<br><br>Votre supérieur(e) immédiat(e) a complété sa partie de votre formulaire d'appréciation de la contribution (cotes, bilan et évaluation globale). Vous pouvez la consulter avant votre rencontre. Après la rencontre, vous pourrez approuver et soumettre le formulaire.<br><br><a href="@{variables('LienApp')}">Ouvrir le dossier</a>
```

6. Dans **« Selon le statut »**, mettez à jour 2 textes :
   - **cas « Avisé au supérieur »**, corps : remplacez « Vous pouvez la consulter et planifier la rencontre. » par « Vous pouvez la consulter, compléter votre partie (cotes de la section B, bilan de la section E et évaluation globale), puis la lui transmettre avec le bouton « Transmettre ma version » avant la rencontre. »
   - **cas « Certifié »**, corps : « … a confirmé et approuvé son formulaire après la rencontre. C'est maintenant votre étape : ajustez au besoin votre partie, puis approuvez. »
7. **Enregistrer.**

# PARTIE 5 — Tester dans le bac à sable

Avec 2 comptes : vous (personne en appréciation) et votre supérieur immédiat (ou un collègue nommé SI dans le dossier).

| ☐ | Qui | Action | Attendu |
|---|---|---|---|
| ☐ | Personne | Nouveau formulaire | L'**ID** s'affiche (sinon, le taper) ; la **bannière** jaune demande le type de poste |
| ☐ | Personne | Tape des objectifs, Tab, clique dans le champ suivant | Le **curseur reste** dans le tableau |
| ☐ | Personne | Enregistrer et déposer, puis **Aviser** | Le SI reçoit « prête pour votre consultation » ; Gérer l'accès : **pas** de SRHVQ_Utilisateurs |
| ☐ | Personne | Section G | « En attente de la version de votre supérieur(e)… » ; bouton grisé ; pas de cotes du SI en section B |
| ☐ | SI | Cotes, section E, évaluation globale, coche, puis **Transmettre ma version** | Message vert ; barre d'étapes : étape 2 ✓ avec la date |
| ☐ | Personne | Reçoit le courriel, ouvre le dossier | Voit la partie du SI ; peut cocher, puis **Approuver et soumettre** |
| ☐ | SI | **Approuver** | Suite normale (SH, directeur de service, RH) |
| ☐ | Tous | Aperçu PDF | Section G « Processus d'approbation » avec la ligne « Version transmise » |

# PARTIE 6 — Mettre en PréProd

| ☐ | Étape | Qui |
|---|---|---|
| ☐ | Solution › **Publier toutes les personnalisations** | Vous |
| ☐ | Exporter › version **1.0.0.7** › **Gérée** | Vous |
| ☐ | Envoyer le .zip à Bruno : import en **mise à niveau**, puis **désactiver et réactiver les flux 1 et 2** | Vous, puis les TI |
| ☐ | Tests en PréProd avec un collègue **non propriétaire** du site : il ne voit pas les dossiers des autres (application, SharePoint, lien direct) | Vous et un testeur |

**Message à Bruno :**

> Bonjour Bruno,
>
> Voici la version 1.0.0.7 de l'application Appréciation de la contribution (solution gérée). Elle corrige la sécurité des dossiers (flux 1) et ajoute une étape au circuit. J'ai déjà créé la colonne VersionSILe dans la liste PréProd.
>
> Pourrais-tu l'importer en mise à niveau, puis désactiver et réactiver les flux « Appréciation – Permissions à la création » et « Appréciation – Suivi des étapes » ?
>
> Merci !
> Annie
