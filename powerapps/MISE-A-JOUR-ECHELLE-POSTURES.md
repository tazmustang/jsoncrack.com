---
title: "Mise à jour — Échelle des postures de leadership (4 niveaux)"
subtitle: "VERSION FINALE — mise à jour du 30 octobre 2026 · Cadre avec équipe et cadre sans équipe · 20 minutes"
lang: fr-CA
---

# Ce qui change

| Avant (5 niveaux) | Maintenant (4 niveaux) |
|---|---|
| Non démontré | **Insatisfaisant** |
| Partiellement démontré | **Partiellement satisfaisant** |
| Conforme aux attentes | **Complètement satisfaisant** |
| Dépasse les attentes | **Supérieur** |
| Exemplaire | *(retiré)* |

Les descriptions changent aussi, et une **note 1** s'ajoute sous le tableau de l'échelle.

**Ce qui se met à jour automatiquement.** Les listes de cotes de chaque comportement (colonne de la personne et colonne du supérieur) sont alimentées par la liste **colEchelle**. Dès que l'étape 1 est faite, elles offrent les 4 nouveaux niveaux, pour les 4 postures et pour les deux types de cadre. Le PDF reprend les cotes choisies.

**Les professionnels ne sont pas touchés** : ils ont la section Compétences, sans échelle.

# Étape 1 — Les 4 niveaux (scrFormulaire.OnVisible)

1. Ouvrez l'application en **Modifier**.
2. Dans l'arborescence, cliquez sur l'écran **scrFormulaire**, puis choisissez la propriété **OnVisible**.
3. Dans la barre fx, trouvez le bloc qui commence par `ClearCollect(colEchelle;` et qui se termine par `{Niveau: "Exemplaire"; Ordre: 5});;`
4. Remplacez **seulement ce bloc** par :

```
ClearCollect(colEchelle;
    {Niveau: "Insatisfaisant"; Ordre: 1;
     Desc: "Ne répond pas aux attentes. Les comportements associés aux postures de leadership sont peu ou pas observés malgré les occasions de les démontrer."};
    {Niveau: "Partiellement satisfaisant"; Ordre: 2;
     Desc: "Répond partiellement aux attentes. Les comportements associés aux postures de leadership sont présents, mais leur démonstration manque de constance, de profondeur ou d'autonomie dans certaines situations."};
    {Niveau: "Complètement satisfaisant"; Ordre: 3;
     Desc: "Répond pleinement aux attentes en démontrant de façon régulière et autonome les comportements associés aux postures de leadership dans les situations pertinentes à son rôle."};
    {Niveau: "Supérieur"; Ordre: 4;
     Desc: "Dépasse les attentes en démontrant les comportements associés aux postures de leadership de façon remarquable, constante et mobilisatrice. Fait preuve d'une grande maîtrise des comportements attendus et exerce une influence positive dans les situations rencontrées."});;
```

Vous pouvez aussi recoller tout le fichier **scrFormulaire-OnVisible-corrige.txt** (mis à jour le 30 octobre).

> 💡 Pour que l'écran utilise tout de suite la nouvelle liste pendant la modification : allez à l'écran **scrMesDossiers**, puis revenez à **scrFormulaire**. OnVisible s'exécute à nouveau.

# Étape 2 — Le tableau de l'échelle (echelleLegend)

Le tableau affiché dans la section B est le contrôle **echelleLegend** (texte HTML). Il lit maintenant directement la liste colEchelle : il n'y a qu'un seul endroit à modifier si l'échelle change un jour.

1. Dans l'arborescence, cliquez sur **echelleLegend** (dans la section B).
2. Choisissez la propriété **HtmlText**.
3. Effacez tout, puis collez :

```
"<div style='font-family:Segoe UI, Arial, sans-serif; font-size:14px; color:#1F2937'>" &
"<table style='width:100%; border-collapse:collapse'>" &
"<tr style='background:#E8EEF5'><th colspan='2' style='text-align:left; padding:8px 10px; color:#0B2D5B'>Échelle de démonstration des comportements associés aux postures de leadership<sup>1</sup></th></tr>" &
"<tr style='background:#E8EEF5'><th style='text-align:left; padding:8px 10px; width:230px; color:#0B2D5B'>Niveau</th><th style='text-align:left; padding:8px 10px; color:#0B2D5B'>Description synthèse</th></tr>" &
Concat(Sort(colEchelle; Ordre) As n;
    "<tr><td style='padding:8px 10px; border:1px solid #E5E7EB; font-weight:bold; vertical-align:top'>" & n.Niveau &
    "</td><td style='padding:8px 10px; border:1px solid #E5E7EB'>" & n.Desc & "</td></tr>") &
"</table>" &
"<p style='font-size:12px; color:#6B7280; font-style:italic; margin:6px 0 0 0'><sup>1</sup> Bien que les niveaux de l'échelle utilisés pour l'appréciation des postures de leadership et pour l'appréciation globale de la contribution soient identiques, leur utilisation répond à des objectifs différents. Les définitions ont donc été adaptées afin de refléter adéquatement l'objet à apprécier.</p>" &
"</div>"
```

4. Propriété **AutoHeight** : `true`. Si elle n'existe pas, mettez **Height** à `330`.

# Étape 3 — Les textes de la section B

Cliquez sur chaque texte de la section B, propriété **Text**, et remplacez-le. Gardez les guillemets au début et à la fin.

**Texte d'introduction :**

```
"La Ville valorise un leadership soutenant la réalisation de sa mission et l’atteinte des orientations de sa planification stratégique. À cet effet, quatre postures clés sont attendues de l’ensemble des cadres, tous niveaux confondus."
```

**Question :**

```
"3. Dans quelle mesure les comportements associés à chacune des postures de leadership sont-ils démontrés de façon concrète à travers les actions, les décisions et les interactions de la personne en appréciation ?"
```

**Précision :**

```
"Précision : Cette section est remplie par les deux parties. La personne en appréciation réalise une autoévaluation de l’application concrète des comportements liés aux postures de leadership. Par ailleurs, la ou le supérieur(e) immédiat(e) évalue ces mêmes comportements à partir de ses observations sur le terrain."
```

# Étape 4 — Chercher les anciens niveaux

1. Dans Power Apps Studio, cliquez sur la **loupe** (Rechercher) dans la barre de gauche.
2. Cherchez **Exemplaire**, puis **Non démontré**, puis **Conforme aux attentes**.
3. Si un résultat apparaît, par exemple dans le texte de l'aide « Comment remplir ce formulaire » (aideHtml), remplacez-le par les nouveaux niveaux.

Résultat attendu : **aucun résultat**.

# Vérifier

1. **Enregistrer**, puis **Publier**.
2. Ouvrez l'application et choisissez **Cadre avec équipe**.
   ✅ La section B affiche le tableau à **4 niveaux** et la **note 1**.
3. Ouvrez la liste de cotes d'un comportement.
   ✅ Elle offre **Insatisfaisant, Partiellement satisfaisant, Complètement satisfaisant, Supérieur**.
4. Choisissez des cotes, cliquez sur **Enregistrer et déposer**, puis rouvrez le dossier.
   ✅ Les cotes sont toujours là.
5. Refaites les points 2 à 4 avec **Cadre sans équipe**.
6. Cliquez sur **🖨️ Aperçu PDF**, puis **📄 Ouvrir le PDF**.
   ✅ Les nouvelles cotes apparaissent dans les tableaux des postures.

# Les dossiers de test existants

Une cote enregistrée avec l'ancienne échelle (ex. « Exemplaire ») n'existe plus dans la nouvelle liste : la case paraîtra **vide** à l'ouverture. C'est sans conséquence pour les **dossiers de test**, qui seront supprimés. Aucun vrai dossier n'existe encore.

# Avant d'envoyer la solution aux TI

Faites cette mise à jour **avant** d'exporter la solution. Exportez ensuite en version **1.0.0.3** (au lieu de 1.0.0.2).
