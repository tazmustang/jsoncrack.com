---
title: "SRHVQ — Résumé des modifications, version 1.0.0.10"
subtitle: "Nouvelle mise en PréProd · Application « Appréciation de la contribution » · Solution-ApplicationAppréciation"
lang: fr-CA
---

# 1. Liste de vérification avant de publier (bac à sable)

Cochez chaque ligne avant l'export.

| ☐ | Élément | Où | Guide |
|---|---|---|---|
| ☐ | Flux 2 : le courriel « Aviser » va au **supérieur immédiat** (`CourrielSI`) | Flux Suivi des étapes, cas « Avisé au supérieur » | ANALYSE-1-0-0-9, point 1 |
| ☐ | Étiquette sigSIRoleLabel remise dans sigSI › sigSIRoleBadge | Section G | ANALYSE-1-0-0-9, point 2 |
| ☐ | Bouton « Comment remplir » qui ramène au formulaire | btnHelp | AIDE-COMMENT-REMPLIR [1] |
| ☐ | Texte de l'aide à jour (7 étapes, « Confirmer ») | aideHtml | AIDE-COMMENT-REMPLIR [3] |
| ☐ | Gestion des erreurs | App.OnError | CONFORMITE [1] |
| ☐ | Validation des champs obligatoires, dont le type de poste | lblManquants, btnDeposer, btnDeposerExec, btnAviser | CONFORMITE [2] à [14] |
| ☐ | Fenêtre de confirmation à la création | conConfirmer | CONFORMITE [15] [16] |
| ☐ | Écran « À propos » (version **1.0.0.10**) | scrAPropos | CONFORMITE [17] |
| ☐ | Écran « Aide » (didacticiel) | scrAide | CONFORMITE [18] |
| ☐ | Boutons « À propos » et « Aide » | scrMesDossiers | CONFORMITE [19] |
| ☐ | Vérificateur d'application : **0 erreur** | Power Apps Studio | |
| ☐ | Tests réussis (circuit complet avec 2 comptes, validation, confirmation, PDF) | Bac à sable | CONFORMITE, section 8 |

# 2. Publier et exporter

1. Power Apps Studio : **Enregistrer** › **Publier** › **Publier cette version**.
2. make.powerapps.com › bac à sable › **Solutions** › Solution-ApplicationAppréciation.
3. **Publier toutes les personnalisations** (en haut).
4. **Exporter la solution** › **Publier** (si demandé) › **Suivant**.
5. Version : **1.0.0.10** › **Gérée** › **Exporter**. Le fichier arrive dans Téléchargements.
6. Refaites l'export en **Non gérée** et gardez-le pour vous (copie de sécurité).

# 3. Résumé des modifications depuis la version installée en PréProd

**Nouvelle étape du circuit**

- « Version du supérieur immédiat transmise » : le supérieur immédiat remplit ses cotes, son bilan et l'évaluation globale, puis clique sur « Transmettre ma version ». La personne reçoit un courriel et peut lire cette version avant la rencontre ; elle approuve seulement après.
- Barre d'étapes à 8 étapes. Nouvelle colonne SharePoint **VersionSILe** (Date et heure).

**Corrections**

- Courriel « Aviser » envoyé au supérieur immédiat (il partait vers la personne).
- Sécurité : le flux 1 retire le groupe **SRHVQ_Utilisateurs** de chaque dossier (getbyname). Chacun ne voit que ses dossiers.
- Curseur qui sautait dans les tableaux de la section A.
- Flux 3 (PDF) : connexions du compte de service (erreur « MissingConnectionReference Office 365 Outlook »).
- Variable d'environnement inutilisée du bac à sable retirée (6 variables).

**Conformité aux exigences des TI**

- Validation des champs obligatoires (nom, ID, type de poste, type de rencontre, directeur au besoin) avant « Enregistrer » et « Aviser ».
- Confirmation avant la création d'un dossier.
- Gestion des erreurs (App.OnError) : message clair et trace.
- Écrans « À propos » (version, environnement, soutien, écrire au soutien) et « Aide » (didacticiel de 5 pages).

**Libellés et apparence**

- « Directeur / directrice de service », « Processus d'approbation », « Approuver et soumettre », « Confirmé », « Comportement démontré ».
- Bandeau bleu Ville #00285E, logo de la Ville, numéro d'employé obligatoire.

# 4. Ce que les TI doivent faire dans la PréProd

1. Liste **SRHVQ_Appreciations** : ajouter la colonne **VersionSILe** (Date et heure, inclure l'heure) **avant** l'import.
2. Vérifier les 7 choix de **Statut** : Brouillon, Avisé au supérieur, Certifié, Approuvé SI, Approuvé SH, Approuvé directeur, Complété.
3. Liste **SRHVQ_Parametres** : lignes Environnement (PRE-PROD), CourrielSoutien, SupportNom (SupportTelephone facultatif).
4. Importer la solution **gérée 1.0.0.10** : **mise à niveau** (Upgrade).
5. Vérifier les **références de connexion** (compte de service) et les **valeurs des 6 variables** (site et listes de la nouvelle PréProd).
6. Flux 3 GenererPDFAppreciation : **Utilisateurs exécutant uniquement** = connexions du compte de service.
7. Désactiver puis réactiver les **3 flux**.
8. Partager l'application avec le groupe **G-IS-APP-RH-SRHVQ-PreProd** ; ce groupe doit être membre de **SRHVQ_Utilisateurs**.
9. Dossiers de test bloqués : les supprimer, ou remettre **Statut** = Brouillon et vider **AviseLe**.

# 5. Texte pour le champ « Commentaires » de la demande aux TI

> Mise à niveau de la solution Solution-ApplicationAppréciation (SRHVQ) en PréProd : version 1.0.0.10 gérée. Nouvelle étape « Version du supérieur immédiat transmise » (nouvelle colonne VersionSILe à ajouter à la liste SRHVQ_Appreciations avant l'import), correction du courriel d'avis au supérieur, sécurité des dossiers (groupe SRHVQ_Utilisateurs), connexions du flux PDF sur le compte de service, et ajout des éléments de conformité (validation, confirmation, gestion des erreurs, écrans À propos et Aide). Après l'import : vérifier les références de connexion et les 6 variables, régler les utilisateurs exécutant uniquement du flux 3, puis désactiver et réactiver les 3 flux. Détails : RESUME-MODIFICATIONS-1-0-0-10.docx.
