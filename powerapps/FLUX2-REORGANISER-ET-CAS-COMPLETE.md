---
title: "Flux « Appréciation – Suivi des étapes » : réorganiser et construire le cas « Complété »"
subtitle: "D'après votre capture du 27 octobre 2026"
lang: fr-CA
---

# Ce que montre votre capture

Votre flux contient presque toutes les pièces. Il manque le contenu du cas **Complété**, et deux cartes ne sont pas à la bonne place.

| Ce que je vois | Bon ? | Pourquoi |
|---|---|---|
| LienApp, CourrielPaie, Changements | ✅ | Bon ordre |
| **Condition** (Directeur ajouté) › Si oui : Assurer directeur, Accès directeur | ✅ | Bon |
| **Condition 2** (Statut changé), avec le commutateur « Selon le statut » | ❌ **Mal placée** | Elle est **à l'intérieur** du « Si oui » de la 1ʳᵉ condition. Les courriels ne partiraient donc **que** quand on ajoute un directeur. Elle doit être **sous** la 1ʳᵉ condition, au même niveau. |
| Cas Avisé au supérieur, Certifié, Approuvé SI, Approuvé SH | ✅ (à vérifier) | Chaque cas doit contenir son courriel (guide 13.3) |
| Cas **Complété** | ❌ **Vide** | C'est pour ça que vous ne trouvez pas « Retirer accès » ni « Donner Lecture » : elles n'ont **pas encore été créées**. |
| **Date paie**, tout en bas | ❌ **Mal placée** | Elle est **hors** de tout, donc elle s'exécuterait à **chaque** modification du dossier. Elle doit être la **dernière action du cas Complété**. |

> ⚠️ Corrigez la place de **Date paie** **avant** tout nouveau test. Dans sa position actuelle, elle inscrit une date de paie à chaque enregistrement.

# Partie 1 — Remettre les 2 cartes à leur place (5 minutes)

## 1.1 Sortir « Condition 2 »

1. Repliez les cartes pour y voir clair : cliquez sur le titre de **Condition 2** pour la refermer.
2. **Glissez-déposez** la carte **Condition 2** (cliquez sur son titre, gardez le bouton enfoncé et déplacez la souris) jusqu'à la **flèche sous la grande carte « Condition »**, entre « Condition » et « Date paie ».
3. Relâchez quand une zone de dépôt apparaît sur la flèche.
4. Résultat attendu : Changements → Condition → **Condition 2** → Date paie, les uns sous les autres.

**Si le glisser-déposer ne fonctionne pas :**

1. Sur Condition 2, cliquez sur **…** › **Copier dans mon presse-papiers**.
2. Cliquez sur le **+** de la flèche sous « Condition », puis sur **Ajouter une action** › onglet **Mon presse-papiers**, et choisissez la carte copiée.
3. Supprimez ensuite l'ancienne Condition 2 (celle qui est dans le « Si oui »).

## 1.2 Renommer (conseillé)

- **Condition** → `Directeur ajouté`
- **Condition 2** → `Statut changé`

Pour renommer : **…** › **Renommer**. Ça facilite le repérage, et les formules ne font pas référence à ces deux noms.

## 1.3 Déplacer « Date paie »

Glissez-déposez **Date paie** à l'intérieur du cas **Complété** du commutateur. On la placera **en dernier** dans la partie 2.

# Partie 2 — Construire le cas « Complété » (20 minutes)

Ouvrez le cas **Complété** du commutateur « Selon le statut ». Ajoutez les actions **dans cet ordre**. Les lignes à copier sont dans le fichier `FLUX2-CAS-COMPLETE.txt`.

| N° | Action à ajouter | Renommer en (exactement) |
|---|---|---|
| 6.1 | Office 365 Outlook › Envoyer un courriel (V2) | `Courriel paie` |
| 6.2 | Office 365 Outlook › Envoyer un courriel (V2) | `Avis à tous` |
| 6.3 | Opérations de données › Filtrer un tableau | `Personnes finales` |
| 6.4 | Contrôle › Appliquer à chacun | `Lecture seule` |
| 6.4a | *(dans la boucle)* SharePoint › Envoyer une requête HTTP à SharePoint | `Assurer personne` |
| 6.4b | *(dans la boucle)* SharePoint › Envoyer une requête HTTP à SharePoint | `Retirer accès` |
| 6.4c | *(dans la boucle)* SharePoint › Envoyer une requête HTTP à SharePoint | `Donner Lecture` |
| 6.5 | **Date paie** (déjà créée, déplacée en partie 1) | `Date paie` |

> **Renommez chaque action dès qu'elle est créée, avant de remplir les suivantes.** Les formules de 6.4, 6.4b et 6.4c utilisent les noms `Personnes_finales` et `Assurer_personne`. Power Automate remplace les espaces par « _ ».

## 6.1 — Courriel paie

- **À :** la variable **CourrielPaie** (contenu dynamique, section Variables).
- **Objet :** ligne [6.1-Objet] du fichier .txt.
- **Corps :** cliquez sur **</>** (mode code) dans l'éditeur du corps, puis collez le bloc [6.1-Corps].

## 6.2 — Avis à tous

- **À (expression fx) :** ligne [6.2-À].
- **Objet :** ligne [6.2-Objet].
- **Corps (mode code </>) :** ligne [6.2-Corps].

## 6.3 — Personnes finales

- **De (expression fx) :** ligne [6.3-De].
- Cliquez sur **Modifier en mode avancé**, puis collez la ligne [6.3-Condition].

## 6.4 — Lecture seule (la boucle)

- **Sélectionner une sortie des étapes précédentes (expression fx) :** ligne [6.4-Sortie].
- Dans **… › Paramètres** de la boucle : **Contrôle d'accès concurrentiel** activé, degré **1**.

## 6.4a — Assurer personne (dans la boucle)

- **Adresse du site :** variable **Site Appréciations** (contenu dynamique).
- **Méthode :** POST
- **URI :** `_api/web/ensureuser`
- **En-têtes**, 2 lignes :
  - `Accept` = `application/json;odata=nometadata`
  - `Content-Type` = `application/json;odata=nometadata`
- **Corps :** ligne [6.4a-Corps].

## 6.4b — Retirer accès (dans la boucle, sous 6.4a)

- **Adresse du site :** variable **Site Appréciations**
- **Méthode :** POST
- **URI :** ligne [6.4b-URI]
- **En-têtes**, 2 lignes :
  - `Accept` = `application/json;odata=nometadata`
  - `X-HTTP-Method` = `DELETE`

## 6.4c — Donner Lecture (dans la boucle, sous 6.4b)

- **Adresse du site :** variable **Site Appréciations**
- **Méthode :** POST
- **URI :** ligne [6.4c-URI]
- **En-têtes :** `Accept` = `application/json;odata=nometadata`

## 6.5 — Date paie (en dernier, **sous** la boucle « Lecture seule »)

Votre carte est presque prête. Vérifiez :

- **ID :** contenu dynamique **ID**, et **Titre :** contenu dynamique **Titre**. ✅ C'est déjà fait.
- **TransmisPaieLe :** faites défiler la carte jusqu'à ce champ et mettez l'expression `utcNow()`.
- **Tous les autres champs restent vides.** Laissez aussi « DirecteurRequis » sur son choix actuel s'il est imposé.

> 6.5 modifie le dossier, ce qui relance le flux. Le statut n'a pas changé, donc « Statut changé » arrête le flux : il n'y a **pas de boucle sans fin**. C'est pour ça que Date paie doit être **dans** le cas Complété.

# Partie 3 — Vérifier et tester

1. Cliquez sur **Enregistrer**. Le **Vérificateur de flux** (en haut) doit être vide.
2. Le schéma final doit ressembler à ceci :

```
LienApp → CourrielPaie → Changements
→ Directeur ajouté  (Si oui : Assurer directeur → Accès directeur)
→ Statut changé     (Si oui : Selon le statut)
      ├ Avisé au supérieur : courriel
      ├ Certifié : courriel
      ├ Approuvé SI : courriel
      ├ Approuvé SH : courriel
      └ Complété : Courriel paie → Avis à tous → Personnes finales
                   → Lecture seule (Assurer personne → Retirer accès → Donner Lecture)
                   → Date paie
```

3. Pour tester : dans l'application, utilisez **Aviser le supérieur** sur votre dossier. Le flux doit envoyer le courriel « prête pour votre consultation » à Pierre Raymond.

> **En mode test**, prévenez Pierre Raymond, ou mettez temporairement **votre** adresse dans la colonne CourrielSI du dossier n° 1 dans SharePoint, pour recevoir le courriel vous-même.
