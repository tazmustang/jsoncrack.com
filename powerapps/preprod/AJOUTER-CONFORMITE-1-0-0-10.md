---
title: "Ajouter la conformité TI : validation, confirmation, erreurs, « À propos » et « Aide »"
subtitle: "À faire dans le bac à sable sur votre version 1.0.0.9 · nouvelle version 1.0.0.10 · formules : FORMULES-CONFORMITE-1-0-0-10.txt"
lang: fr-CA
---

# Ce que vous allez ajouter

| Exigence des TI | Ce qui sera fait | Numéros dans le fichier |
|---|---|---|
| Validation des champs | « Enregistrer » et « Aviser » vérifient les champs obligatoires (nom, ID, **type de poste**, type de rencontre, directeur au besoin) | [4] à [9] |
| Confirmation | Fenêtre « Créer votre dossier d'appréciation ? » à la création | [15] [16] |
| Gestion des erreurs | Message clair à l'utilisateur et trace pour le soutien (App.OnError) | [1] |
| Écran « À propos » | Nom, version, environnement, soutien, bouton « Écrire au soutien » | [17] |
| Écran « Aide » | Didacticiel de 5 pages, avec Précédent / Suivant | [18] |
| Accès | Boutons « ℹ️ À propos » et « 📖 Aide » sur l'écran Mes dossiers | [19] |

Les formules ont été faites **à partir de votre 1.0.0.9** : elles gardent tout ce qui existe déjà (nouvelle étape, recopie des tableaux, etc.).

**Pourquoi les boutons « À propos » et « Aide » sont seulement sur Mes dossiers :** quand on revient dans le formulaire, l'écran relit le dossier dans SharePoint. Ce qui n'est pas encore enregistré serait perdu. Dans le formulaire, l'aide « ❓ Comment remplir » et le bouton « ✉️ Écrire à l'équipe » restent disponibles.

# 0. Avant de commencer

1. **Copie de sécurité :** Solutions › votre solution › **Exporter** › **Non gérée**. Gardez le ZIP.
2. **Liste Parametres** du bac à sable (et plus tard celle de la PréProd) : vérifiez qu'elle a ces lignes (colonne Title / colonne Valeur) :

| Title | Valeur |
|---|---|
| Environnement | DEV (bac à sable), PRE-PROD ou PROD |
| CourrielSoutien | annie.audet@ville.quebec.qc.ca |
| SupportNom | Annie Audet, RH-SST |
| SupportTelephone | *(facultatif : laissez vide pour ne pas afficher de téléphone)* |

3. Ouvrez l'application dans Power Apps Studio (**Modifier**). Gardez **FORMULES-CONFORMITE-1-0-0-10.txt** ouvert à côté.

**Méthode pour coller une formule :** cliquez sur le contrôle › choisissez la propriété (liste à gauche de la barre de formule) › **Ctrl + A** dans la barre › collez.

# 1. Gestion des erreurs — [1]

1. Arborescence : tout en haut, cliquez sur **App**.
2. Propriété **OnError** : collez le bloc [1].

# 2. Validation des champs — [2] à [14]

## 2.1 L'étiquette cachée qui liste les champs manquants — [4] [5]

1. Écran **scrFormulaire** › arborescence : cliquez sur **btnDeposer** (barre de gauche, groupe des actions).
2. **Insérer** › **Étiquette de texte**. Elle s'ajoute dans le même groupe.
3. Renommez-la **lblManquants**.
4. **Text** = bloc [4] ; **Visible** = `false`.

## 2.2 Le bouton caché qui enregistre — [2] [3]

1. Cliquez sur **btnDeposer** › **Ctrl + C** › **Ctrl + V**. Une copie apparaît (btnDeposer_1).
2. Renommez la copie **btnDeposerExec**.
3. **OnSelect** = bloc [2] (c'est votre formule actuelle d'enregistrement, avec un commentaire) ; **Visible** = `false`.

Si, au test, rien ne s'enregistre : mettez **Visible** = `true`, **Width** = `1`, **Height** = `1`.

## 2.3 Les boutons visibles — [6] à [14]

| Contrôle | Propriété | Bloc |
|---|---|---|
| btnDeposer | OnSelect | [6] |
| btnDeposer | DisplayMode | [7] |
| btnAviser | OnSelect | [8] |
| btnAviser | DisplayMode | [9] |
| btnCertifier | OnSelect | [10] |
| btnTransSI | OnSelect | [11] |
| btnApprSI | OnSelect | [12] |
| btnApprSH | OnSelect | [13] |
| btnApprDir | OnSelect | [14] |

Pour [10] à [14], la seule différence est `Select(btnDeposerExec)` au lieu de `Select(btnDeposer)` : les approbations ne repassent pas par la validation ni par la confirmation.

Ces formules remplacent aussi celles du document TYPE-DE-POSTE-OBLIGATOIRE : ne les faites pas deux fois.

# 3. Fenêtre de confirmation — [15] [16]

1. **scrFormulaire.OnVisible** : allez à la toute fin de la formule, ajoutez `;;` à la fin de la dernière ligne, puis collez le bloc [15].
2. Arborescence : cliquez sur l'écran **scrFormulaire** lui-même (pour que le conteneur soit posé sur l'écran, pas dans un autre conteneur).
3. **Insérer** › **Disposition** › **Conteneur**. Renommez-le **conConfirmer**.
4. Clic droit sur conConfirmer › **Réorganiser** › **Mettre au premier plan**.
5. Cliquez sur **conConfirmer** › **Insérer** › **Disposition** › **Conteneur** : renommez-le **conBoite**.
6. Cliquez sur **conBoite** › insérez 2 **Étiquettes de texte** (**lblConfirmerTitre**, **lblConfirmerTexte**) et 2 **Boutons** (**btnConfirmerOui**, **btnConfirmerNon**).
7. Appliquez toutes les propriétés du bloc [16].

# 4. Écran « À propos » — [17]

1. **Nouvel écran** › **Vide**. Renommez-le **scrAPropos**.
2. Insérez : 1 **Rectangle** (recAProposBandeau), 5 **Étiquettes de texte** (lblAProposTitre, lblAppNom, lblVersion, lblDescriptionApp, lblSupport) et 2 **Boutons** (btnEcrireSoutien, btnAProposRetour).
3. Appliquez les propriétés du bloc [17].

« Écrire au soutien » ouvre un courriel déjà adressé (Outlook), comme le bouton qui existe déjà dans l'aide : **aucun nouveau connecteur**, donc rien de plus à demander aux TI.

# 5. Écran « Aide » (didacticiel) — [18]

1. **Nouvel écran** › **Vide**. Renommez-le **scrAide**.
2. Insérez : 1 **Rectangle** (recAideBandeau), 3 **Étiquettes de texte** (lblAideEntete, lblAideTitre, lblAideTexte) et 3 **Boutons** (btnAidePrecedent, btnAideSuivant, btnAideFermer).
3. Appliquez les propriétés du bloc [18].

# 6. Boutons d'accès sur Mes dossiers — [19]

1. Écran **scrMesDossiers** › cliquez sur **btnNouveauDossier** › **Ctrl + C** › **Ctrl + V** deux fois.
2. Renommez les copies **btnAPropos** et **btnAide**.
3. Appliquez le bloc [19] (Text et OnSelect).

# 7. Vérifier, publier, exporter

1. **Vérificateur d'application** : 0 erreur.
2. **Enregistrer** › **Publier**.
3. Solution › **Exporter** › **Gérée** › version **1.0.0.10**.

# 8. Tests

| # | Test | Résultat attendu |
|---|---|---|
| 1 | Nouveau formulaire, rien de rempli, « Enregistrer et déposer » | Message : « Avant d'enregistrer, complétez : Nom, ID de l'employé, Type de poste, Type de rencontre » ; rien n'est créé |
| 2 | Tout remplir, « Enregistrer et déposer » | Fenêtre « Créer votre dossier ? » |
| 3 | Cliquer sur **Annuler** | « Création annulée » ; aucun dossier dans la liste |
| 4 | Recommencer, **Oui, créer le dossier** | « Dossier enregistré » ; le dossier est dans la liste |
| 5 | Modifier, « Enregistrer et déposer » | Enregistré directement, sans fenêtre |
| 6 | Vider l'ID, puis « Aviser le supérieur » | Message « complétez : ID de l'employé » ; le statut ne change pas |
| 7 | Circuit complet (Transmettre, Approuver et soumettre, approbations) | Fonctionne comme avant, sans fenêtre de confirmation |
| 8 | Mes dossiers › **ℹ️ À propos** | Nom, version 1.0.0.10, environnement, soutien ; « Écrire au soutien » ouvre un courriel |
| 9 | Mes dossiers › **📖 Aide** | 5 pages, Précédent grisé à la page 1, « Terminer ✓ » à la page 5 ramène à Mes dossiers |

# 9. Documents mis à jour

Le document d'architecture et la révision des versions (Documents TI) sont mis à jour pour la 1.0.0.10 : « À propos » ouvre un courriel au soutien, et l'aide est un didacticiel de 5 pages.
