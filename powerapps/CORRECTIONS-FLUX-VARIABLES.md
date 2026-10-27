---
title: "Corrections des flux — noms des variables d'environnement"
subtitle: "Appréciation de la contribution — 27 octobre 2026"
lang: fr-CA
---

# Pourquoi ces corrections

Les flux du guide écrivent les variables d'environnement avec des noms un peu différents de ceux de **votre** solution. Power Automate ne les trouve donc pas, et c'est l'erreur « The workflow parameter … is not found ».

| Le guide écrit | Le vrai nom dans votre solution |
|---|---|
| `Liste Appréciations (rhdsst_ListeAppreciations)` | **`Liste Appreciations (rhdsst_ListeAppreciations)`** (sans accent) |
| `Lien application (rhdsst_LienApplication)` | **`Lienapplication (rhdsst_Lienapplication)`** |
| `Courriel paie (rhdsst_CourrielPaie)` | **`Courriel paie (rhdsst_Courrielpaie)`** |
| `Site Appréciations (rhdsst_SiteAppreciations)` | **`Site Appréciations (rhdsst_SiteApprciations)`** |

**Ce qui ne change pas :** les champs **Adresse du site** et **Nom de la liste** où vous avez **choisi** la variable dans une liste déroulante. Les déclencheurs ont fonctionné ✅, donc ces champs sont bons. Seuls les champs où le nom a été **tapé ou collé** sont à corriger.

**Comment remplacer un champ URI :**

1. Ouvrez l'action en cliquant sur son titre.
2. Cliquez dans le champ **URI**.
3. Faites **Ctrl+A**, puis **Suppr** : le champ est vide.
4. Collez la ligne donnée ici (**Ctrl+V**).
5. Ne touchez à aucun autre champ (Méthode, En-têtes, Corps).

Les lignes à coller sont aussi dans le fichier texte `CORRECTIONS-FLUX-VARIABLES.txt`, pour copier sans risque d'erreur.

# Flux 1 — « Appréciation – Permissions à la création »

Ce flux a **3 actions** à corriger. Elles sont toutes du type **« Envoyer une requête HTTP à SharePoint »**.

Voici le flux dans l'ordre, pour vous repérer :

| N° | Nom de l'action dans votre flux | À corriger ? |
|---|---|---|
| D | Lorsqu'un élément est créé | Non |
| 1 | Id dossier | Non |
| 2 | **Couper l'héritage** | **Oui : URI** |
| 3 | Groupe Membres | Non |
| 4 | **Retirer les Membres** | **Oui : URI** |
| 5 | Personnes du dossier | Non |
| 6 | Pour chaque personne (une boucle qui contient 2 actions) | Ouvrez-la |
| 6a | ↳ Assurer utilisateur (1ʳᵉ action dans la boucle) | Non |
| 6b | ↳ **Donner Collaboration** (2ᵉ action dans la boucle) | **Oui : URI** |

## Correction 1 — action « Couper l'héritage » › URI

```
_api/web/lists(guid'@{parameters('Liste Appreciations (rhdsst_ListeAppreciations)')}')/items(@{variables('IdDossier')})/breakroleinheritance(copyRoleAssignments=true,clearSubscopes=true)
```

## Correction 2 — action « Retirer les Membres » › URI

```
_api/web/lists(guid'@{parameters('Liste Appreciations (rhdsst_ListeAppreciations)')}')/items(@{variables('IdDossier')})/roleassignments/getbyprincipalid(@{body('Groupe_Membres')?['Id']})
```

## Correction 3 — action « Donner Collaboration » › URI

**Où la trouver :**

1. Cliquez sur la carte **Pour chaque personne** pour l'ouvrir.
2. À l'intérieur, il y a **2 cartes**. La **2ᵉ** s'appelle **Donner Collaboration**. C'est elle qui donne aux personnes du dossier le droit de le modifier.
3. Ouvrez-la et remplacez son **URI** par :

```
_api/web/lists(guid'@{parameters('Liste Appreciations (rhdsst_ListeAppreciations)')}')/items(@{variables('IdDossier')})/roleassignments/addroleassignment(principalid=@{body('Assurer_utilisateur')?['Id']},roledefid=1073741827)
```

> La 1ʳᵉ carte de la boucle, **Assurer utilisateur**, a pour URI `_api/web/ensureuser` : elle n'utilise pas de variable, n'y touchez pas.

**Attention aux noms :** la formule fait référence aux actions **Groupe_Membres** et **Assurer_utilisateur**. Les actions doivent donc s'appeler exactement **Groupe Membres** et **Assurer utilisateur**. Power Automate remplace les espaces par « _ » dans les formules. Si votre action porte un autre nom, renommez-la : … › **Renommer**.

Cliquez sur **Enregistrer**.

# Flux 2 — « Appréciation – Suivi des étapes »

Ce flux a **5 endroits** à corriger.

| N° | Nom de l'action | Où | À corriger |
|---|---|---|---|
| 1 | **LienApp (Chaîne)** | au début | **Valeur** |
| 2 | **CourrielPaie (Chaîne)** | au début | **Valeur** |
| 4b | **Accès directeur** | dans la condition « Directeur ajouté », branche **Si oui**, 2ᵉ carte | **URI** |
| 6.4b | **Retirer accès** | dans le commutateur, cas **Complété**, boucle « Lecture seule », 2ᵉ carte | **URI** |
| 6.4c | **Donner Lecture** | même boucle « Lecture seule », 3ᵉ carte | **URI** |

## Correction 4 — « LienApp (Chaîne) » › Valeur

1. Cliquez dans le champ **Valeur** et effacez ce qu'il contient.
2. Ouvrez l'éditeur d'**expression** (**fx**), collez la ligne suivante, puis cliquez sur **Ajouter** (ou **OK**) :

```
concat(parameters('Lienapplication (rhdsst_Lienapplication)'), '&ID=', triggerOutputs()?['body/ID'])
```

## Correction 5 — « CourrielPaie (Chaîne) » › Valeur

1. Cliquez dans le champ **Valeur** et effacez ce qu'il contient.
2. Ouvrez l'éditeur d'**expression** (**fx**), collez la ligne suivante, puis cliquez sur **Ajouter** :

```
parameters('Courriel paie (rhdsst_Courrielpaie)')
```

## Correction 6 — « Accès directeur » › URI

```
_api/web/lists(guid'@{parameters('Liste Appreciations (rhdsst_ListeAppreciations)')}')/items(@{triggerOutputs()?['body/ID']})/roleassignments/addroleassignment(principalid=@{body('Assurer_directeur')?['Id']},roledefid=1073741827)
```

## Correction 7 — « Retirer accès » › URI

```
_api/web/lists(guid'@{parameters('Liste Appreciations (rhdsst_ListeAppreciations)')}')/items(@{triggerOutputs()?['body/ID']})/roleassignments/getbyprincipalid(@{body('Assurer_personne')?['Id']})
```

## Correction 8 — « Donner Lecture » › URI

```
_api/web/lists(guid'@{parameters('Liste Appreciations (rhdsst_ListeAppreciations)')}')/items(@{triggerOutputs()?['body/ID']})/roleassignments/addroleassignment(principalid=@{body('Assurer_personne')?['Id']},roledefid=1073741826)
```

**Noms à vérifier :** les actions **Assurer directeur** et **Assurer personne** doivent porter exactement ces noms.

Cliquez sur **Enregistrer**.

# Flux 3 — « GenererPDFAppreciation » (PDF)

Ce flux ne tape aucun nom de variable. Aux actions 3, 4 et 5, choisissez l'adresse du site dans le **contenu dynamique › Variables d'environnement › Site Appréciations**. Ne tapez pas le nom vous-même.

# Vérification finale (2 minutes par flux)

1. Dans le flux, cliquez sur **…**, puis **Afficher le code** (ou **Peek code**, sur une action).
2. Faites **Ctrl+F** et tapez `parameters(`.
3. Chaque résultat doit contenir **exactement** un de ces noms :
   - `Liste Appreciations (rhdsst_ListeAppreciations)`
   - `Liste Parametres (rhdsst_ListeParametres)`
   - `Lienapplication (rhdsst_Lienapplication)`
   - `Courriel paie (rhdsst_Courrielpaie)`
   - `Site Appréciations (rhdsst_SiteApprciations)`
4. Faites aussi **Ctrl+F** sur `Appréciations (rhdsst_ListeAppreciations` (avec accent) : il ne doit y avoir **aucun** résultat.

# Relancer les exécutions en échec

1. Ouvrez le flux, puis **Historique des exécutions 28 jours**.
2. Cliquez sur l'exécution en échec (rouge).
3. Cliquez sur **Renvoyer** en haut. Le flux reprend avec le même dossier.
4. Toutes les actions doivent être vertes ✅.
5. Pour le flux 1, contrôlez le résultat : dans la liste Appreciations, ouvrez le dossier, puis **…** › **Gérer l'accès**. Seuls les Propriétaires, RH – Appréciations et les personnes du dossier doivent apparaître.

# Note pour plus tard (TI)

En pré-prod et en prod, les TI importeront la solution avec **ces mêmes variables**, donc avec les mêmes noms techniques. Les flux corrigés fonctionneront partout. Ne renommez pas les variables : leur nom technique (`rhdsst_…`) ne peut de toute façon pas changer.
