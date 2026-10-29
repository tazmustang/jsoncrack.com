---
title: "Correction — Le type de rencontre ne reste pas dans le dossier"
subtitle: "VERSION FINALE — mise à jour du 29 octobre 2026 · 15 minutes"
lang: fr-CA
---

# Le problème

Vous cochez un **type de rencontre**, vous cliquez sur **Enregistrer et déposer**, et les cases se décochent. Le type de rencontre n'apparaît pas non plus dans le PDF.

Le PDF lit les cases à l'écran : s'il est vide, c'est que les cases se sont décochées après l'enregistrement. On corrige donc l'enregistrement et la relecture. Le PDF se corrige ensuite tout seul.

# Les deux causes possibles

1. **Le texte des choix dans SharePoint n'est pas identique à celui de la formule.** Une seule différence suffit : une apostrophe courbe ’ au lieu de ', un accent, un espace en trop. Aucun choix ne correspond, et rien n'est enregistré.
2. **Le dossier ouvert depuis « Mes dossiers » arrive incomplet** : la colonne TypeRencontre est vide dans l'application, même si elle est remplie dans SharePoint.

La correction règle les deux. Faites les **3 étapes**.

# Étape 1 — Les 5 cases à cocher (propriété Checked)

1. Ouvrez l'application en **Modifier**, écran **scrFormulaire**.
2. Cliquez sur la case **chkEssai**.
3. En haut à gauche, choisissez la propriété **Checked**.
4. Dans la **barre fx**, effacez tout et collez la formule ci-dessous.
5. Refaites la même chose pour les 4 autres cases.

| Case | Formule à coller dans Checked |
|---|---|
| chkEssai | `!IsEmpty(Filter(varDossier.TypeRencontre; "essai" in Value))` |
| chkPremiere | `!IsEmpty(Filter(varDossier.TypeRencontre; "premi" in Value))` |
| chkMiAnnee | `!IsEmpty(Filter(varDossier.TypeRencontre; "mi-ann" in Value))` |
| chkBilan | `!IsEmpty(Filter(varDossier.TypeRencontre; "bilan annuel" in Value))` |
| chkAutre | `!IsEmpty(Filter(varDossier.TypeRencontre; StartsWith(Value; "Autre")))` |

> 💡 L'application cherche maintenant un **mot-clé** (« essai », « premi »…) au lieu du texte exact. Une apostrophe ou une majuscule différente ne bloque plus rien.

# Étape 2 — Le bouton « Enregistrer et déposer » (btnDeposer)

1. Cliquez sur **btnDeposer**, propriété **OnSelect**.
2. Dans la barre fx, trouvez le bloc qui commence par `TypeRencontre: Filter(Choices(`.
3. Remplacez **seulement ce bloc**, jusqu'à `chkAutre.Checked));` inclus, par :

```
        TypeRencontre: Filter(Choices(Appreciations.TypeRencontre);
            ("essai" in Value And chkEssai.Checked) Or
            ("premi" in Value And chkPremiere.Checked) Or
            ("mi-ann" in Value And chkMiAnnee.Checked) Or
            ("bilan annuel" in Value And chkBilan.Checked) Or
            (StartsWith(Value; "Autre") And chkAutre.Checked));
```

La formule complète est aussi dans **FORMULES-POWERAPPS-FINALES.txt**, section 3.

# Étape 3 — Relire le dossier complet à l'ouverture (scrFormulaire.OnVisible)

1. Cliquez sur l'écran **scrFormulaire** (dans l'arborescence à gauche), propriété **OnVisible**.
2. Trouvez cette ligne, au début :

   `Set(varDossier; LookUp(Appreciations; ID = Value(Param("ID")))));;`

3. **Juste en dessous**, collez :

```
If(!IsBlank(varDossier);
    Set(varDossier; LookUp(Appreciations; ID = varDossier.ID)));;
```

Vous pouvez aussi recoller tout le fichier **scrFormulaire-OnVisible-corrige.txt** (mis à jour le 29 octobre).

# Vérifier

1. **Enregistrer**, puis **Publier**.
2. Ouvrez l'application, ouvrez un dossier, cochez **2 types de rencontre**, puis **Enregistrer et déposer**.
   ✅ Les cases **restent cochées**.
3. Revenez à **Mes dossiers**, puis rouvrez le dossier.
   ✅ Les 2 cases sont **toujours cochées**.
4. Cliquez sur **🖨️ Aperçu PDF**, puis **📄 Ouvrir le PDF**.
   ✅ La ligne **Type de rencontre** affiche vos 2 choix.
5. Dans SharePoint, ouvrez la liste **Appreciations**.
   ✅ La colonne **TypeRencontre** de ce dossier contient les 2 choix.

# Si ça ne fonctionne toujours pas

Ajoutez temporairement une **étiquette** (Insérer › Étiquette de texte) avec ce Text :

```
"Choix SharePoint : " & Concat(Choices(Appreciations.TypeRencontre); "[" & Value & "]"; " ") & Char(10) & "Dans le dossier : " & Concat(varDossier.TypeRencontre; Value; ", ")
```

Faites une **capture d'écran** de l'étiquette après un enregistrement. Elle montre le texte exact des choix et ce qui est enregistré. Supprimez l'étiquette ensuite.

Vérifiez aussi dans SharePoint, sous **Paramètres de la liste › TypeRencontre**, que **« Autoriser plusieurs sélections »** est bien à **Oui**.

# Avant d'envoyer la solution aux TI

Faites cette correction **avant** d'exporter la solution. Sinon, la PréProd aura le même problème.
