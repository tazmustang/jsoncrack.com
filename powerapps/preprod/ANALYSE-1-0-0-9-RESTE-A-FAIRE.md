---
title: "Votre version 1.0.0.9 (non gérée) : ce qui est fait, ce qui reste"
subtitle: "Analyse de SolutionApplicationApprciation_1_0_0_9.zip · 9 novembre 2026"
lang: fr-CA
---

# Bonne nouvelle : votre bac à sable n'est PAS revenu à la 1.0.0.5

Votre version 1.0.0.9 contient tout le travail de la 1.0.0.8, plus vos corrections. **Vous n'avez pas à tout refaire.** Le guide « TOUT-REFAIRE » ne sert que si un environnement contient encore la 1.0.0.5.

# Déjà fait (vérifié)

| Élément | État |
|---|---|
| Nouvelle étape « Transmettre ma version », barre à 8 étapes | ✓ |
| Hauteur du bloc du supérieur (sigSI.Height) | ✓ corrigée |
| Bannière « Choisissez votre type de poste » hors de la barre d'étapes | ✓ |
| « Comportement démontré » (4 fois) | ✓ |
| Logo de la Ville sur les 2 écrans | ✓ |
| 7ᵉ variable (bac à sable) retirée | ✓ |
| Flux 1 : getbyname('SRHVQ_Utilisateurs') | ✓ |
| Flux 3 : connexions du compte de service (erreur Outlook du PDF) | ✓ |
| Vérificateur d'application | ✓ 0 erreur |

# Reste à faire : 4 choses

## 1. Flux 2 : le courriel « Aviser » part encore vers la personne (IMPORTANT)

C'est la raison principale du blocage : le supérieur immédiat n'est jamais avisé.

1. Ouvrez le flux **Appréciation – Suivi des étapes** › **Modifier**.
2. **Statut changé** › **Selon le statut** › cas **Avisé au supérieur** › **Envoyer un e-mail (V2)**.
3. Champ **À** : supprimez la valeur › **Expression** (fx) › collez › **Ajouter** :

```
triggerOutputs()?['body/CourrielSI']
```

4. **Enregistrer**.

Ne touchez pas au courriel de la condition « Version SI transmise » : lui doit bien aller à `CourrielPersonne`.

## 2. Une étiquette déplacée par erreur (sigSIRoleLabel)

L'étiquette « ✏️ Votre étape / 🔒 Réservé à ce rôle » du **supérieur immédiat** (sigSIRoleLabel) a été glissée par mégarde dans l'en-tête du bloc du **supérieur hiérarchique** (sigSHHead).

1. Arborescence : section G › **sigSH** › **sigSHHead** › trouvez **sigSIRoleLabel**.
2. Glissez-la dans **sigSI** › **sigSIRoleBadge** (ou : clic droit › Couper, cliquez sur sigSIRoleBadge, Ctrl + V).
3. Le conteneur se place tout seul (mise en page automatique) : rien d'autre à régler.
4. Vérifiez : le bloc du supérieur immédiat affiche de nouveau « Votre étape » ou « Réservé à ce rôle » dans sa bande grise, et l'en-tête du supérieur hiérarchique n'en a plus qu'une.

## 3. Bouton d'aide qui ramène au formulaire

Contrôle **btnHelp** (barre de gauche) :

- **OnSelect** : `Set(CurrentTabID; If(CurrentTabID = 2; 1; 2))`
- **Text** : `If(CurrentTabID = 2; "← Retour au formulaire"; "❓ Comment remplir ce formulaire")`

## 4. Texte de l'aide (encore « Les 5 étapes » et « Certifier »)

Contrôle **aideHtml** : **HtmlText** = section 3 du fichier **AIDE-COMMENT-REMPLIR.txt** ; **Height** = `1180`.

# Ensuite

1. **Enregistrer**, **Publier**.
2. Solution › **Exporter** › **Gérée**. Gardez le numéro **1.0.0.9** si cette version n'a jamais été envoyée aux TI ; sinon prenez **1.0.0.10**.
3. Faites les 8 tests de la section 7 du guide TOUT-REFAIRE (2 comptes).

# Pour les TI (nouvelle PréProd)

1. Liste **SRHVQ_Appreciations** : ajouter la colonne **VersionSILe** (Date et heure, avec l'heure). Sans elle, « Transmettre ma version » échoue et le dossier reste bloqué.
2. Vérifier les 7 choix de **Statut** (Brouillon, Avisé au supérieur, Certifié, Approuvé SI, Approuvé SH, Approuvé directeur, Complété).
3. Importer la version gérée (**mise à niveau**), vérifier les références de connexion et les valeurs des variables.
4. Désactiver puis réactiver les 3 flux.
5. Dossiers bloqués existants : dans la liste, **Statut** = Brouillon et vider **AviseLe**, ou les supprimer.
