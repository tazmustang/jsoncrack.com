---
title: "Échelle des postures à 4 niveaux — Pas à pas détaillé"
subtitle: "VERSION FINALE — mise à jour du 30 octobre 2026 · Cadre avec équipe et cadre sans équipe · 30 minutes"
lang: fr-CA
---

# Pourquoi « ça ne fonctionne pas » après le point 1

Le point 1 change seulement la **liste des niveaux** (`colEchelle`) qui alimente les **listes déroulantes de cotes**. Il ne change pas tout seul ce qui est affiché. Quatre raisons expliquent le plus souvent que rien ne semble changer :

| Ce que vous voyez | Cause | Partie à faire |
|---|---|---|
| Le **tableau de l'échelle** affiche encore « Non démontré… Exemplaire » | Ce tableau est un texte HTML séparé (**echelleLegend**). Il n'est pas touché par le point 1 | **Partie 5** |
| Les **listes de cotes** offrent encore 5 niveaux | **OnVisible ne s'est pas encore exécuté** : dans le studio, il ne s'exécute qu'en arrivant sur l'écran | **Partie 3** |
| Toujours 5 niveaux, même après la partie 3 | Une **autre formule** crée aussi la liste (ex. App.OnStart), ou les listes de cotes ont leurs propres choix | **Parties 4 et 6** |
| Une **ligne rouge** dans OnVisible | Le bloc a été mal collé (un `;;` manquant ou un morceau de l'ancien bloc) | **Partie 2** |

Faites les parties **dans l'ordre**. Après chacune, il y a un ✅ pour vérifier.

# Partie 1 — Ouvrir l'application en modification

1. Allez sur **make.powerapps.com**. En haut à droite, vérifiez que l'**environnement** est votre bac à sable.
2. Menu de gauche : **Solutions**, puis cliquez sur **Solution-ApplicationAppreciation**.
3. Cliquez sur les **⋯** à côté de l'application **Appréciation de la contribution**, puis sur **Modifier**.
4. Si un message parle d'une version plus récente ou d'un verrou, choisissez **Modifier quand même**.

✅ Le studio Power Apps s'ouvre, avec l'**Arborescence** à gauche.

# Partie 2 — Remplacer TOUTE la formule OnVisible (le plus sûr)

Plutôt que de chercher le bloc au milieu de la formule, on remplace **toute** la formule par le fichier à jour. Ça évite les morceaux oubliés.

1. Sur votre ordinateur, ouvrez le fichier **scrFormulaire-OnVisible-corrige.txt** avec le **Bloc-notes** : clic droit › Ouvrir avec › Bloc-notes.
2. Vérifiez la **1re ligne** : elle doit indiquer « mises à jour du 29 et du 30 octobre ». Sinon, vous avez une ancienne copie : téléchargez celle jointe à ce document.
3. Dans le Bloc-notes : **Ctrl + A**, puis **Ctrl + C**.
4. Dans le studio, dans l'**Arborescence** à gauche, cliquez sur le nom de l'écran **scrFormulaire**. Cliquez sur l'écran lui-même, pas sur un contrôle à l'intérieur.
5. En haut à gauche, sous le ruban, ouvrez la **liste des propriétés** (elle affiche souvent « Fill ») et choisissez **OnVisible**.
6. Cliquez **dans la barre de formule fx**, à droite de la liste des propriétés. Pour l'agrandir, cliquez sur la flèche **⌄** au bout de la barre.
7. **Ctrl + A**, puis **Suppr** : la barre est vide.
8. **Ctrl + V** pour coller.
9. Attendez 5 à 10 secondes.

✅ Aucun texte n'est souligné en **rouge**, et l'icône du Vérificateur d'application (stéthoscope, en haut à droite) n'indique pas de nouvelle erreur.

**Si du rouge apparaît :** placez la souris sur le mot souligné et faites une capture du message. La cause la plus fréquente est le nom du connecteur Office 365 : retapez **Util** et choisissez `'Utilisateursd’Office365'` dans la liste.

# Partie 3 — Faire exécuter OnVisible

OnVisible s'exécute **quand on arrive sur l'écran**. Coller la formule ne suffit pas.

1. Dans l'Arborescence, cliquez sur l'écran **scrMesDossiers**.
2. Appuyez sur **F5** (ou cliquez sur ▶ **Aperçu** en haut à droite).
3. Dans l'application, cliquez sur **📝 Nouveau formulaire**, ou sur **Ouvrir** à côté d'un dossier. Vous arrivez sur scrFormulaire et OnVisible s'exécute.
4. Choisissez le type de poste **Cadre avec équipe**.
5. Fermez l'aperçu avec **Échap** ou le **X** en haut à droite.

# Partie 4 — Vérifier la liste colEchelle

1. Dans la barre de gauche du studio, cliquez sur l'icône **(x) Variables**.
2. Ouvrez **Collections**, puis cliquez sur **colEchelle**.

✅ Vous voyez **4 lignes** : Insatisfaisant, Partiellement satisfaisant, Complètement satisfaisant, Supérieur, avec les colonnes **Niveau**, **Ordre** et **Desc**.

**Si vous voyez encore 5 lignes avec « Exemplaire » :**

1. Une autre formule recrée l'ancienne liste. Cliquez sur la **loupe 🔍** dans la barre de gauche et cherchez **colEchelle**.
2. Les résultats montrent chaque endroit où le nom apparaît. Si un résultat est dans **App** (propriété **OnStart**) ou ailleurs qu'OnVisible avec `ClearCollect(colEchelle` :
   1. cliquez sur le résultat ;
   2. dans la barre fx, sélectionnez le bloc `ClearCollect(colEchelle; … "Exemplaire"; Ordre: 5});;` en entier ;
   3. supprimez-le. OnVisible suffit.
3. Refaites la **partie 3**, puis cette vérification.

# Partie 5 — Le tableau de l'échelle (echelleLegend)

1. Dans l'**Arborescence**, dépliez **scrFormulaire**, puis la section B. Le plus simple : tapez **echelle** dans la zone **Rechercher** en haut de l'Arborescence.
2. Cliquez sur **echelleLegend**.
3. Liste des propriétés en haut à gauche : choisissez **HtmlText**.
4. Cliquez dans la barre fx, **Ctrl + A**, **Suppr**, puis collez la formule ci-dessous. Elle se trouve aussi dans **FORMULES-POWERAPPS-FINALES.txt**, section 13.

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

5. Dans le **panneau de droite**, onglet **Propriétés** (ou **Avancé**), cherchez **Hauteur automatique** (AutoHeight) et mettez-la à **Activé**. Si elle n'existe pas, mettez **Hauteur** (Height) à **330**.

✅ Dans le studio, le tableau affiche les **4 niveaux**, les nouvelles descriptions et la **note 1** en italique.

**Si le tableau est vide :** colEchelle n'est pas encore chargée. Refaites la **partie 3**.

**Si le tableau chevauche ce qui est en dessous :** augmentez la Height, ou vérifiez que le contrôle sous le tableau a un **Y** qui dépend de `echelleLegend.Y + echelleLegend.Height`.

# Partie 6 — Les listes de cotes des comportements

Il y a une galerie par posture (**galP1** à **galP4**). Chacune contient 2 listes : la cote de la personne (**…CboCadre**) et celle du supérieur (**…CboSup**). Vérifiez au moins la première, puis les autres de la même façon.

1. Dans l'Arborescence, dépliez **galP1** et cliquez sur **p1CboCadre**.
2. Propriété **Items** : la formule doit être exactement `colEchelle`. Sinon, remplacez-la par `colEchelle`.
3. Propriété **DefaultSelectedItems** : `Filter(colEchelle; Niveau = ThisItem.CoteCadre)`
4. Panneau de droite, **Champs** › **Modifier** : le champ affiché doit être **Niveau**. Il ne doit pas être **Desc**, sinon la liste afficherait les longues descriptions.
5. Refaites la même chose pour **p1CboSup**. Sa propriété DefaultSelectedItems utilise `ThisItem.CoteSup`.
6. Répétez pour **p2…**, **p3…** et **p4…**.

✅ En aperçu (**F5**), la liste d'une cote offre **les 4 nouveaux niveaux**.

# Partie 7 — Les textes de la section B

1. En mode modification, cliquez **directement sur le texte** dans l'écran. Le nom du contrôle se surligne dans l'Arborescence.
2. Liste des propriétés : **Text**.
3. Dans la barre fx, **Ctrl + A**, **Suppr**, puis collez le texte correspondant, **avec les guillemets** :

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

# Partie 8 — Chercher les restes de l'ancienne échelle

1. Cliquez sur la **loupe 🔍** dans la barre de gauche.
2. Cherchez, l'un après l'autre : **Exemplaire**, **Non démontré**, **Conforme aux attentes**, **Dépasse les attentes**.
3. Pour chaque résultat, cliquez dessus et remplacez l'ancien niveau par le nouveau (voir le tableau ci-dessous). Le texte de l'aide « Comment remplir » (**aideHtml**) peut en contenir.

| Ancien | Nouveau |
|---|---|
| Non démontré | Insatisfaisant |
| Partiellement démontré | Partiellement satisfaisant |
| Conforme aux attentes | Complètement satisfaisant |
| Dépasse les attentes | Supérieur |
| Exemplaire | *(supprimer)* |

✅ La recherche ne trouve plus aucun des 4 anciens niveaux.

# Partie 9 — Enregistrer, publier, tester

1. En haut à droite : **💾 Enregistrer**.
2. Puis **Publier** › **Publier cette version**.
3. Fermez le studio. Ouvrez l'application **dans un nouvel onglet** avec son lien habituel. Si l'ancienne version apparaît encore, faites **Ctrl + F5**.
4. Testez :
   1. **Cadre avec équipe** : tableau à 4 niveaux et note 1 ; les listes de cotes offrent les 4 niveaux.
   2. Choisissez des cotes, faites **Enregistrer et déposer**, revenez à **Mes dossiers**, puis rouvrez le dossier : les cotes sont toujours là.
   3. Refaites le test avec **Cadre sans équipe**.
   4. **🖨️ Aperçu PDF**, puis **📄 Ouvrir le PDF** : les nouvelles cotes apparaissent.

# Si ça ne fonctionne toujours pas

Envoyez-moi **3 captures d'écran** :

1. le panneau **(x) Variables › Collections › colEchelle** (partie 4) ;
2. la barre fx de **p1CboCadre**, propriété **Items** ;
3. ce que vous voyez dans l'application (tableau et liste déroulante ouverte).

Avec ces 3 images, je pourrai trouver la cause exacte.
