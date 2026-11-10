---
title: "Rendre le type de poste obligatoire"
subtitle: "Version 1.0.0.9 · 10 novembre 2026"
lang: fr-CA
---

# Ce que fait la version actuelle (vérifié dans votre 1.0.0.9)

**Elle indique, mais elle n'empêche pas.**

| Ce qui existe | Effet |
|---|---|
| Bannière orange « ⚠️ Choisissez d'abord votre type de poste… » sous la barre d'étapes | Visible tant qu'aucun type n'est choisi |
| Encadré « Choisissez d'abord le type de poste… » à la place de la section B | La section B reste cachée |
| Sections A, C, D, F | **Restent modifiables** |
| « Enregistrer et déposer » | **Fonctionne** : le dossier est créé sans type de poste |
| « Aviser le supérieur » | **Fonctionne** sans type de poste |

# La correction proposée (2 propriétés)

La personne peut commencer à écrire, mais elle ne peut **ni créer le dossier, ni aviser son supérieur** tant que le type de poste n'est pas choisi.

## 1. Bouton « Enregistrer et déposer » (btnDeposer)

Propriété **DisplayMode** (aujourd'hui vide) : collez

```
If(CurrentRoleID = "cadre" && CurrentPosteID = ""; DisplayMode.Disabled; DisplayMode.Edit)
```

## 2. Bouton « Aviser le supérieur » (btnAviser)

Propriété **DisplayMode** : effacez et collez

```
If(CurrentRoleID = "cadre" && CurrentPosteID <> ""; DisplayMode.Edit; DisplayMode.Disabled)
```

## 3. Texte de la bannière (lblChoisirPoste)

Propriété **Text** : effacez et collez

```
"⚠️ Choisissez d'abord votre type de poste (menu de gauche, « 2. Type de poste »). Sans ce choix, vous ne pouvez pas enregistrer votre formulaire ni aviser votre supérieur(e)."
```

# Tester

1. Nouveau formulaire, **sans** choisir de type de poste : les 2 boutons sont grisés, la bannière est visible.
2. Choisissez un type de poste : la bannière disparaît, les boutons redeviennent actifs.
3. Ouvrez un dossier existant comme supérieur(e) : « Enregistrer et déposer » reste actif.

# À savoir (exigences des TI)

Votre 1.0.0.9 ne contient **pas** non plus les autres éléments de conformité préparés le 1er novembre (fichier FORMULES-CONFORMITE.txt) : la vérification des champs obligatoires avant l'enregistrement, la fenêtre de confirmation à la création, les écrans « À propos » et « Aide », et la gestion des erreurs (App.OnError). Seuls la sécurité à l'ouverture et « Mes dossiers » y sont. Si les TI les exigent pour la PréProd ou la Prod, il faudra les ajouter.
