---
title: "Nouvelle étape « Version du supérieur transmise », sécurité, ID et barre d'étapes"
subtitle: "Application Appréciation de la contribution (SRHVQ) · Version 1.0.0.7 · 6 novembre 2026"
lang: fr-CA
---

# Partie A — Urgent : la barre d'étapes est en erreur

Dans la solution 1.0.0.6, la propriété **galEtapes › Items** contient **tout le texte du fichier** (« 1) Contrôle : galEtapes Propriété : Items », les lignes « ----- », les autres formules). Ce n'est pas une formule valide : la barre d'étapes ne s'affiche pas correctement, et le vérificateur d'application montre une trentaine d'erreurs en cascade (stepDot, stepLabel, stepDate…).

**Correction :**

1. Cliquez sur **galEtapes** › propriété **Items** › **Ctrl + A**, puis **Suppr**.
2. Ouvrez **barre-etapes-formules.txt** (mis à jour, 8 étapes). Copiez **seulement** ce qui est **entre** les deux premières lignes `-----`, c'est-à-dire de `With(` jusqu'à `false}))`. Ne copiez ni le titre, ni les lignes `-----`.
3. Collez.
4. **galEtapes › TemplateSize** : `Self.Width / 8`
5. **stepLineRight › Visible** : `ThisItem.Ordre < 8`

✅ Le vérificateur d'application n'indique plus d'erreur dans galEtapes.

# Partie B — Sécurité : ce que montrent vos captures

- La page des autorisations du **site** affiche seulement Propriétaires, Membres et Visiteurs. C'est **normal** : les groupes SRHVQ_Utilisateurs et SRHVQ_RH n'ont aucun droit sur le site, donc ils n'y apparaissent pas.
- Vos testeurs sont dans le groupe Entra **G-IS-APP-RH-SRHVQ-PreProd**. C'est la bonne façon de faire.
- Mais dans « Gérer l'accès » d'un dossier, on voyait **G-IS-APP-RH-SRHVQ-PreProd directement**. Il a donc été ajouté **directement sur la liste**, au lieu de passer par SRHVQ_Utilisateurs. Le flux ne peut pas le retirer des dossiers.

**À faire sur le site PréProd, dans l'ordre :**

| N° | Où | Action |
|---|---|---|
| 1 | ⚙️ › Paramètres du site › **Personnes et groupes** | Vérifiez que **SRHVQ_Utilisateurs** existe. Sinon, créez-le (aucun droit sur le site) |
| 2 | Ouvrez **SRHVQ_Utilisateurs** › Nouveau › Ajouter des utilisateurs | Ajoutez **G-IS-APP-RH-SRHVQ-PreProd** |
| 3 | Liste **SRHVQ_Appréciation de la contribution des cadres** › Paramètres › **Autorisations pour cette liste** | **Retirez G-IS-APP-RH-SRHVQ-PreProd** s'il y est directement |
| 4 | Même page › **Accorder des autorisations** | **SRHVQ_Utilisateurs** › **Collaboration** (et **SRHVQ_RH** › **Lecture**) |
| 5 | Même page | Il doit rester : Propriétaires (Contrôle total), SRHVQ_Utilisateurs (Collaboration), SRHVQ_RH (Lecture) |

Ensuite, **flux 1** (bac à sable) : URI de l'action « Groupe Membres » = `_api/web/sitegroups/getbyname('SRHVQ_Utilisateurs')?$select=Id`. Voir CORRECTIONS-TESTS-PREPROD-5-NOVEMBRE, partie 2.

# Partie C — L'ID de l'employé (annuaire)

**txtId › Default** (remplacez la formule) :

```
// ID : celui du dossier ; sinon, pour la personne en appréciation, celui de l'annuaire
If(!IsBlank(varDossier.IdEmploye);
    varDossier.IdEmploye;
    CurrentRoleID = "cadre";
    'Utilisateursd’Office365'.MyProfileV2().employeeId;
    "")
```

- Tapez `'Utilisateursd’Office365'.MyProfileV2().` et vérifiez que **employeeId** est proposé dans la liste.
- La condition `CurrentRoleID = "cadre"` est importante : sans elle, un supérieur qui ouvre le dossier verrait **son propre** numéro.
- **Test :** Nouveau formulaire › l'ID s'affiche automatiquement. S'il reste vide, votre fiche n'a pas de numéro d'employé dans l'annuaire : il faut alors le taper (et le signaler aux TI).

# Partie D — La nouvelle étape : le supérieur transmet sa version avant la confirmation

## D1. Le nouveau circuit

| N° | Étape | Qui | Ce qui change |
|---|---|---|---|
| 1 | Brouillon, puis **Aviser** | Personne | — |
| 2 | **Version du sup. immédiat transmise** | Supérieur immédiat | **Nouveau :** le SI remplit ses cotes (B), son bilan (E) et l'évaluation globale, puis clique sur **Transmettre ma version**. La personne reçoit un courriel |
| 3 | **Approuver et soumettre** (confirmation) | Personne | Possible **seulement après** l'étape 2 (et la rencontre) |
| 4 | Approuvé SI | Supérieur immédiat | Approbation finale (il peut encore ajuster sa partie) |
| 5 à 8 | SH, directeur de service (si requis), transmis aux RH, archivé | — | Inchangé |

**Principe :** les **statuts ne changent pas**. On ajoute seulement une **date**, « VersionSILe », qui indique que la version du SI a été transmise. Ainsi, aucune des formules existantes n'est brisée.

## D2. SharePoint : ajouter une colonne (bac à sable ET PréProd)

Sur **chaque** liste des dossiers (bac à sable, puis PréProd, puis Prod plus tard) :

1. ⚙️ › Paramètres de la liste › **Créer une colonne**.
2. Nom : `VersionSILe`, exactement, sans espace ni accent.
3. Type : **Date et heure**, format **Date et heure**.
4. **OK.**

Puis, dans l'application (bac à sable) : panneau **Données** › ⋯ sur **Appreciations** › **Actualiser**.

## D3. Application : le bouton « Transmettre ma version » (section G, carte du supérieur immédiat)

1. Dans l'arborescence, dépliez **sigSI** et sélectionnez **sigSIAction**.
2. **Ctrl + C**, puis **Ctrl + V** : une copie apparaît (sigSIAction_1, avec chkApprSI_1 et btnApprSI_1).
3. Renommez-les : **sigSITransmettre**, **chkTransSI**, **btnTransSI**.
4. Glissez **sigSITransmettre** juste **au-dessus** de sigSIAction (dans sigSI).
5. Propriétés :

| Contrôle › propriété | Formule |
|---|---|
| sigSITransmettre › Visible | `Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur" And CurrentRoleID = "superieur_immediat" And IsBlank(varDossier.VersionSILe)` |
| sigSITransmettre › Height | `Self.PaddingTop + chkTransSI.Height + 8 + btnTransSI.Height + Self.PaddingBottom` |
| chkTransSI › Label | `"Ma version est complète (cotes de la section B, bilan de la section E et évaluation globale). Je la transmets à la personne pour la rencontre."` |
| btnTransSI › Text | `"📨 Transmettre ma version"` |
| btnTransSI › DisplayMode | `If(chkTransSI.Checked; DisplayMode.Edit; DisplayMode.Disabled)` |

**btnTransSI › OnSelect** :

```
// Transmet la version du supérieur immédiat à la personne, avant sa confirmation (le flux 2 l'avise par courriel)
Set(varDossier; Patch(Appreciations; varDossier; {VersionSILe: Now()}));;
Select(btnDeposer);;
Reset(chkTransSI);;
Notify("Votre version est transmise. La personne en appréciation est avisée par courriel."; NotificationType.Success)
```

6. **sigSI › Height** : à la fin de la formule actuelle, ajoutez :

```
 + If(sigSITransmettre.Visible; 8 + sigSITransmettre.Height; 0)
```

## D4. Application : la personne ne confirme qu'après avoir reçu la version

| Contrôle › propriété | Formule |
|---|---|
| **chkCert › DisplayMode** | `If(!IsBlank(varDossier.VersionSILe) && Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur" && CurrentRoleID = "cadre"; DisplayMode.Edit; DisplayMode.Disabled)` |
| **chkCert › Label** | `If(IsBlank(varDossier.VersionSILe); "En attente de la version de votre supérieur(e) immédiat(e) : vous recevrez un courriel quand elle sera prête."; "Je confirme avoir pris connaissance du contenu de ce formulaire et je l'approuve.")` |
| **btnCertifier › DisplayMode** | `If(chkCert.Checked && !IsBlank(varDossier.VersionSILe) && Coalesce(varDossier.Statut.Value; "Brouillon") = "Avisé au supérieur"; DisplayMode.Edit; DisplayMode.Disabled)` |

## D5. Application : la personne voit la partie du SI seulement après la transmission

| Contrôle(s) › Visible | Nouvelle formule |
|---|---|
| **p1HdrSup, p2HdrSup, p3HdrSup, p4HdrSup** et **p1CboSup, p2CboSup, p3CboSup, p4CboSup** (8 contrôles, même formule) | `CurrentRoleID <> "cadre" Or (!IsBlank(varDossier.VersionSILe) And CountRows(Filter(colComportements; CoteSup <> "")) > 0)` |
| **cardSectionE** | `CurrentRoleID = "superieur_immediat" Or (Not(IsBlank(varDossier.BilanSuperieur)) And (CurrentRoleID <> "cadre" Or !IsBlank(varDossier.VersionSILe)))` |
| **cardEval** | `CurrentRoleID = "superieur_immediat" Or (varEvalGlobale <> "" And (CurrentRoleID <> "cadre" Or !IsBlank(varDossier.VersionSILe)))` |

> Il s'agit de l'**affichage** dans l'application : la personne n'est pas dérangée par une version incomplète. Les données restent protégées par les autorisations du dossier.

## D6. Application : « À approuver par moi » inclut la nouvelle étape

Dans **galDossiers › Items**, remplacez le bloc `"afaire"; …` par :

```
"afaire"; (CourrielSI = moi And Statut.Value = "Avisé au supérieur" And IsBlank(VersionSILe))
    Or (CourrielSI = moi And Statut.Value = "Certifié")
    Or (CourrielSH = moi And Statut.Value = "Approuvé SI")
    Or (CourrielDirecteur = moi And Statut.Value = "Approuvé SH");
```

## D7. Barre d'étapes et PDF

- **Barre d'étapes** : partie A ci-dessus. La nouvelle formule a **8 étapes**, dont « Version du sup. immédiat transmise ».
- **PDF** : recollez **btnApercuPDF-OnSelect.txt**. La section G a une ligne de plus, « Version transmise par le supérieur immédiat », avec sa date.

## D8. Flux 2 : le courriel à la personne

Dans le flux **Appréciation – Suivi des étapes**, ajoutez une **Condition « Version SI transmise »**, **sous** « Directeur ajouté » et **avant** « Statut changé », au même niveau.

1. **Ligne 1 :** `body('Changements')?['ColumnHasChanged']?['VersionSILe']` **est égal à** `true`
2. **Ligne 2 (ET) :** `triggerOutputs()?['body/VersionSILe']` **n'est pas égal à** (vide)
3. **Si oui :** **Envoyer un courriel (V2)**
   - **À :** CourrielPersonne
   - **Objet :** Appréciation : la version de votre supérieur(e) immédiat(e) est prête
   - **Corps :** voir FLUX-FINAUX.txt (4c)

Mettez aussi à jour 2 textes existants (FLUX-FINAUX.txt) :
- **Avisé au supérieur** : le SI est invité à compléter sa partie, puis à la transmettre ;
- **Certifié** : « … a confirmé et approuvé son formulaire après la rencontre… ».

# Partie E — Tester (bac à sable), puis PréProd

| N° | Qui | Action | Attendu |
|---|---|---|---|
| 1 | Personne | Remplit, puis **Aviser** | Le SI reçoit « prête pour votre consultation » |
| 2 | Personne | Regarde la section G | « En attente de la version de votre supérieur(e) immédiat(e) » ; bouton grisé |
| 3 | Personne | Regarde la section B | **Pas** encore de cotes du SI |
| 4 | SI | Met ses cotes, la section E et l'évaluation globale, coche, puis **Transmettre ma version** | Message vert ; barre d'étapes : étape 2 ✓ avec la date |
| 5 | Personne | Reçoit le courriel, ouvre le dossier | Voit les cotes du SI, la section E et l'évaluation globale |
| 6 | Personne | Coche « Je confirme… », puis **Approuver et soumettre** | Statut « Confirmé » ; le SI reçoit « À approuver » |
| 7 | SI | **Approuver** | Suite normale : SH, directeur de service, RH |
| 8 | Tous | Aperçu PDF | Ligne « Version transmise par le supérieur immédiat » avec sa date |

**Ensuite :**
1. Colonne **VersionSILe** créée dans la liste **PréProd**.
2. Export **1.0.0.7** en gérée.
3. Import par les TI, puis flux 1 et 2 désactivés et réactivés.
4. Retests avec un collègue **non propriétaire**.
