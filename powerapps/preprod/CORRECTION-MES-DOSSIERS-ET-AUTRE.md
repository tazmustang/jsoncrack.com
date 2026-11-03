---
title: "Correction — « Mes dossiers » affiche tout après un rafraîchissement, et « Autre » absent du PDF"
subtitle: "Application Appréciation de la contribution (SRHVQ) · 3 novembre 2026 · 20 minutes"
lang: fr-CA
---

# Problème 1 — Après un rafraîchissement, « Mes dossiers » affiche tous les dossiers

## La cause

Le filtre de « Mes dossiers » compare chaque colonne de courriel à **votre** courriel, rangé dans la variable `varMoi`. Après un rafraîchissement, cette variable est parfois **vide** au moment où la liste se charge. La comparaison « courriel du directeur = vide » devient alors **vraie pour tous les dossiers sans directeur**. Tout s'affiche, et la colonne « Mon rôle » indique **« Directeur / directrice »** partout.

## La correction : lire le courriel directement

On remplace `varMoi` par `Lower(User().Email)`, qui n'est **jamais vide**.

**1. galDossiers › Items** (écran scrMesDossiers). Effacez tout et collez :

```
// galDossiers.Items — Seulement les dossiers où la personne connectée est nommée
// (le courriel est lu directement : jamais vide, même après un rafraîchissement)
With({moi: Lower(User().Email)};
    With({mesDossiers: Filter(Appreciations;
            CourrielPersonne = moi Or CourrielSI = moi Or
            CourrielSH = moi Or CourrielDirecteur = moi)};
        SortByColumns(
            Filter(mesDossiers;
                StartsWith(Title; txtRecherche.Text) And
                Switch(CurrentFiltreID;
                    "encours"; Coalesce(Statut.Value; "Brouillon") <> "Complété";
                    "completes"; Statut.Value = "Complété";
                    "afaire"; (CourrielSI = moi And Statut.Value = "Certifié")
                        Or (CourrielSH = moi And Statut.Value = "Approuvé SI")
                        Or (CourrielDirecteur = moi And Statut.Value = "Approuvé SH");
                    true));
            "Modified"; SortOrder.Descending)))
```

> Si `Title` est souligné en rouge, remplacez-le par `Titre`, comme dans votre formule actuelle.

**2. cellRole › Text** (la colonne « Mon rôle », dans la galerie) :

```
// Rôle de la personne connectée dans ce dossier
With({moi: Lower(User().Email)};
    Switch(true;
        ThisItem.CourrielPersonne = moi; "Personne en appréciation";
        ThisItem.CourrielSI = moi; "Supérieur(e) immédiat(e)";
        ThisItem.CourrielSH = moi; "Supérieur(e) hiérarchique";
        ThisItem.CourrielDirecteur = moi; "Directeur / directrice";
        ""))
```

**3. scrFormulaire › OnVisible** : recollez tout le fichier **scrFormulaire-OnVisible-corrige.txt**, mis à jour. Le contrôle de sécurité à l'ouverture lit aussi le courriel directement.

**4. Enregistrer**, puis **Publier**.

✅ **Test :** ouvrez Mes dossiers, puis **F5** (rafraîchir) plusieurs fois. Seuls vos dossiers restent, avec le bon rôle (« Personne en appréciation » pour le vôtre).

## ⚠️ Important : vous voyez tout dans SharePoint parce que vous êtes propriétaire

Vous êtes dans le groupe **Propriétaires** du site. Les propriétaires voient et ouvrent **tous** les dossiers, et c'est normal : c'est leur rôle. **Vous ne pouvez donc pas tester la confidentialité avec votre propre compte.**

Faites les tests de confidentialité avec un **collègue** qui :
- est membre de **SRHVQ_Utilisateurs** (via G-IS-APP) ;
- n'est **pas** propriétaire du site ;
- n'est **pas** nommé dans le dossier testé.

**Rappel :** la vraie protection reste le **flux 1** (autorisations de chaque dossier). Tant qu'il ne fonctionne pas en PréProd, un collègue pourrait encore ouvrir un dossier par SharePoint. Voir SECURISER-LES-DOSSIERS.docx.

# Problème 2 — Le type « Autre » n'apparaît pas dans le PDF

## La cause

Le texte « Autre » était écrit (ex. « TEST »), mais la **case Autre n'était pas cochée**. Le PDF et l'enregistrement ne tenaient compte du texte que si la case était cochée.

## La correction : le texte suffit

Désormais, si le champ « Autre » contient du texte, il compte comme coché.

**1. btnDeposerExec › OnSelect** (et btnDeposer, si btnDeposerExec n'existe pas encore). Dans le bloc `TypeRencontre`, remplacez la dernière ligne :

```
(StartsWith(Value; "Autre") And chkAutre.Checked));
```

par :

```
(StartsWith(Value; "Autre") And (chkAutre.Checked Or !IsBlank(Trim(txtAutre.Text)))));
```

**2. chkAutre › Checked** :

```
!IsEmpty(Filter(varDossier.TypeRencontre; StartsWith(Value; "Autre"))) Or !IsBlank(varDossier.TypeRencontreAutre)
```

**3. btnApercuPDF › OnSelect** : recollez tout le fichier **btnApercuPDF-OnSelect.txt**, mis à jour. Il corrige aussi le titre du PDF, qui n'affiche plus « formulaire du 15 octobre 2026 ».

> Plus rapide pour le PDF : dans la barre fx du bouton, **Rechercher et remplacer** :
> remplacer `C: chkAutre.Checked}` par `C: chkAutre.Checked Or !IsBlank(Coalesce(txtAutre.Text; varDossier.TypeRencontreAutre))}`

**4. Enregistrer**, puis **Publier**.

✅ **Test :** un dossier avec seulement « Autre : TEST » › **Enregistrer et déposer**, puis **Aperçu PDF**. La ligne **Type de rencontre** affiche « Autre : TEST ».

# Ensuite

Ces corrections partent avec la prochaine version exportée (**1.0.0.4**), en même temps que la correction du flux 1.
