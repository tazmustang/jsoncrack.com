---
title: "Sécuriser les dossiers — Chacun ne voit que SES dossiers"
subtitle: "Application Appréciation de la contribution (SRHVQ) · Correction PréProd · 3 novembre 2026"
lang: fr-CA
---

# Ce qu'on veut

Une personne voit et ouvre **seulement** les dossiers où elle est nommée :

- **son propre dossier** (personne en appréciation) ;
- les dossiers où elle est **supérieur(e) immédiat(e)**, **supérieur(e) hiérarchique** ou **directeur / directrice**.

Les **RH** (groupe SRHVQ_RH) consultent tous les dossiers, en lecture, dans SharePoint.

# Les 3 protections

| N° | Protection | Où | Rôle |
|---|---|---|---|
| 1 | **Autorisations de chaque dossier** | Flux 1 (SharePoint) | **La vraie sécurité.** Même avec un lien direct, ou dans SharePoint, une personne non nommée ne peut pas ouvrir le dossier |
| 2 | **Filtre de « Mes dossiers »** | Application (galDossiers.Items) | N'affiche que les dossiers où le courriel de la personne apparaît |
| 3 | **Contrôle à l'ouverture** (nouveau) | Application (scrFormulaire.OnVisible) | Refuse d'ouvrir un dossier où la personne n'est pas nommée, même par un lien |

# Étape 1 — Diagnostic (vous, sur le site PréProd, 2 minutes)

1. Ouvrez la liste des dossiers sur le site **RH Power Apps Données PréProd**.
2. Cliquez sur les **⋯** d'un dossier de test › **Gérer l'accès** (ou Paramètres › Autorisations avancées).

| Ce que vous voyez | Conclusion |
|---|---|
| « Cet élément hérite des autorisations » ou **SRHVQ_Utilisateurs** dans la liste | **Le flux 1 n'a pas fonctionné** (protection 1 absente) : tout le monde voit tout |
| Seulement Propriétaires, SRHVQ_RH et les personnes du dossier | Protection 1 correcte : le problème est seulement l'affichage (étape 3) |

Dans 99 % des cas, ce sera la première ligne. Les deux raisons probables :
- la version **1.0.0.1** importée en PréProd retire le groupe « Membres », alors que la liste donne accès par **SRHVQ_Utilisateurs** ;
- la liste a été **recréée**, et le flux 1 est resté branché sur l'ancienne liste. Il faut le désactiver puis le réactiver.

# Étape 2 — Corriger le flux 1 (bac à sable)

Si ce n'est pas déjà fait (guide de conformité, parties B1 et B5) :

1. Le groupe **SRHVQ_Utilisateurs** existe sur le site du bac à sable, et il a **Collaboration** sur la liste Appreciations.
2. Flux 1, action **« Groupe Membres »**, URI :

```
_api/web/sitegroups/getbyname('SRHVQ_Utilisateurs')?$select=Id
```

3. Testez dans le bac à sable avec un dossier fictif : **Gérer l'accès** ne doit plus montrer SRHVQ_Utilisateurs.

# Étape 3 — Vérifier le filtre de « Mes dossiers » (application)

1. Ouvrez l'application en **Modifier**, écran **scrMesDossiers**.
2. Cliquez sur la galerie **galDossiers** › propriété **Items**.
3. La formule doit commencer par `With({mesDossiers: Filter(Appreciations; CourrielPersonne = varMoi Or …`. Sinon, remplacez **toute** la formule par :

```
// galDossiers.Items — Seulement les dossiers où la personne connectée est nommée
With(
    {mesDossiers: Filter(Appreciations;
        CourrielPersonne = varMoi Or CourrielSI = varMoi Or
        CourrielSH = varMoi Or CourrielDirecteur = varMoi)};
    SortByColumns(
        Filter(mesDossiers;
            StartsWith(Title; txtRecherche.Text) And
            Switch(CurrentFiltreID;
                "encours"; Coalesce(Statut.Value; "Brouillon") <> "Complété";
                "completes"; Statut.Value = "Complété";
                "afaire"; (CourrielSI = varMoi And Statut.Value = "Certifié")
                    Or (CourrielSH = varMoi And Statut.Value = "Approuvé SI")
                    Or (CourrielDirecteur = varMoi And Statut.Value = "Approuvé SH");
                true));
        "Modified"; SortOrder.Descending))
```

4. Vérifiez aussi que **scrMesDossiers.OnVisible** contient bien `Set(varMoi; Lower(User().Email));;`.

# Étape 4 — Ajouter le contrôle à l'ouverture (application)

Écran **scrFormulaire** › propriété **OnVisible**. Juste **après** ces lignes :

```
If(!IsBlank(varDossier);
    Set(varDossier; LookUp(Appreciations; ID = varDossier.ID)));;
```

collez :

```
// Sécurité : on n'ouvre un dossier que si la personne connectée y est nommée
If(!IsBlank(varDossier) &&
    With({moi: Lower(User().Email)};
        IsBlank(moi) ||
        Not(moi in [Lower(varDossier.CourrielPersonne); Lower(varDossier.CourrielSI);
                    Lower(varDossier.CourrielSH); Lower(varDossier.CourrielDirecteur)]));
    Notify("Vous n'avez pas accès à ce dossier."; NotificationType.Error);;
    Set(varDossier; Blank());;
    Navigate(scrMesDossiers; ScreenTransition.None));;
```

Ou recollez tout le fichier **scrFormulaire-OnVisible-corrige.txt**, mis à jour le 3 novembre.

**Enregistrer**, puis **Publier**.

# Étape 5 — Mettre en PréProd (TI)

1. Exportez la solution en **gérée**, avec une version plus haute (ex. **1.0.0.4**).
2. Les TI l'importent en **mise à niveau**, avec la bonne liste pour la variable (« Appréciation de la contribution des cadres »).
3. Les TI **désactivent puis réactivent** les flux 1 et 2.

**Message aux TI :**

> Bonjour Bruno,
>
> En PréProd, tous les utilisateurs voient et ouvrent tous les dossiers : le flux « Appréciation – Permissions à la création » ne restreint pas l'accès (version 1.0.0.1, et liste recréée). Je t'envoie la version 1.0.0.4 corrigée. Pourrais-tu l'importer en mise à niveau (variable de la liste : « Appréciation de la contribution des cadres », ID cf908dbc-7a12-440c-9e44-1653437fa3bd), puis désactiver et réactiver les flux 1 et 2 ? Si possible, peux-tu aussi me transmettre une capture de l'historique d'exécution du flux 1 ?
>
> Merci !
> Annie

# Étape 6 — Les dossiers de test déjà créés

Les dossiers créés **avant** la correction ne seront **pas** corrigés automatiquement : le flux 1 ne s'exécute qu'à la **création** d'un dossier.

**Le plus simple :** comme ce sont des données fictives, **supprimez-les** dans la liste PréProd (cochez-les, puis Supprimer), et recommencez les tests avec de nouveaux dossiers.

# Étape 7 — Tester la confidentialité (avec 3 comptes)

| N° | Qui | Action | Résultat attendu |
|---|---|---|---|
| 1 | Testeur A | Crée son dossier (rôle Personne en appréciation) | Message vert |
| 2 | Vous | Liste PréProd › ce dossier › Gérer l'accès | Propriétaires, SRHVQ_RH, testeur A, son SI et son SH. **Pas SRHVQ_Utilisateurs** |
| 3 | Testeur B (sans lien avec A) | Ouvre Mes dossiers | **Ne voit pas** le dossier de A |
| 4 | Testeur B | Ouvre le lien direct du dossier de A (…&ID=n) | « Vous n'avez pas accès à ce dossier », ou dossier vide |
| 5 | Testeur B | Ouvre la liste dans SharePoint | **Ne voit pas** le dossier de A |
| 6 | SI de A | Ouvre Mes dossiers | Voit le dossier de A, avec le rôle « Supérieur(e) immédiat(e) » |
| 7 | Membre de SRHVQ_RH | Ouvre la liste dans SharePoint | Voit le dossier, en lecture seulement |

✅ Les 7 tests réussis : les dossiers sont sécurisés.

# Note pour l'avenir

Les tests de confidentialité (3 à 5) font partie de la liste de vérification avant **chaque** mise en production : PréProd, puis Prod.
