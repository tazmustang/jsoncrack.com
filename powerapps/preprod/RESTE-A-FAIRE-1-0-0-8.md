---
title: "Reste à faire avant d'exporter la version 1.0.0.9"
subtitle: "Analyse de SolutionApplicationApprciation_1_0_0_8_managed.zip · 7 novembre 2026"
lang: fr-CA
---

# Bonne nouvelle

La version 1.0.0.8 est très avancée. Ces éléments sont **corrects** :

- flux 1 : `getbyname('SRHVQ_Utilisateurs')` ;
- flux 2 : condition « Version SI transmise » et destinataire `triggerOutputs()?['body/CourrielPersonne']` ;
- bouton « Transmettre ma version », colonne VersionSILe, barre à 8 étapes ;
- couleurs olive retirées, Placeholder du numéro d'employé ;
- recopie des tableaux (curseur), nouveaux textes.

Il reste **7 petites choses**. Faites-les dans l'ordre, enregistrez, puis exportez la **1.0.0.9**.

# 1. Hauteur du bloc du SI (sigSI.Height) — erreur

1. Écran **scrFormulaire** › arborescence › cliquez sur **sigSI**.
2. Propriété **Height** : effacez tout et collez :

```
Self.PaddingTop + sigSIHead.Height + 8 + sigSIRoleBadge.Height + 8 + sigSIDetail.Height + If(sigSITransmettre.Visible; 8 + sigSITransmettre.Height; 0) + If(sigSIAction.Visible; 8 + sigSIAction.Height; 0) + Self.PaddingBottom
```

Il manquait un **+** dans votre version.

# 2. Bannière « Choisissez votre type de poste » (lblChoisirPoste) — erreur

Elle est **à l'intérieur de la barre d'étapes** (galerie galEtapes). Elle se répète dans chaque case et cause des erreurs.

1. Arborescence : ouvrez **galEtapes** › trouvez **lblChoisirPoste**.
2. Clic droit › **Couper** (Ctrl + X).
3. Cliquez sur le conteneur **mainScroll** (sous **stepperWrap**), puis **Ctrl + V**.
4. Déplacez-la juste sous la barre d'étapes et ajustez sa largeur (**Width** = `Parent.Width`). Vérifiez qu'elle n'apparaît qu'une seule fois.

# 3. « Comportement attendu » → « Comportement démontré »

1. Barre de recherche de l'arborescence (loupe) : tapez **Comportement attendu**.
2. Remplacez le texte dans les **4** contrôles trouvés par **Comportement démontré**.

# 4. Gris de la Ville (#8A8C8E)

Il reste d'anciens gris : `RGBA(107; 114; 128; 1)` (52 fois) et `RGBA(156; 163; 175; 1)` (26 fois).

1. Ouvrez la recherche de Power Apps Studio (loupe en haut de l'arborescence, ou **Ctrl + F**), puis cliquez sur la flèche **Remplacer**.
2. Rechercher `RGBA(107; 114; 128; 1)` › Remplacer par `ColorValue("#8A8C8E")` › **Tout remplacer**.
3. Même chose pour `RGBA(156; 163; 175; 1)`.

# 5. Logo de la Ville

1. **Médias › Charger** : `logo/logo-ville-quebec-blanc.png`.
2. Dans le bandeau bleu de **scrMesDossiers** et **scrFormulaire** : **Insérer › Image**, propriété **Image** = `'logo-ville-quebec-blanc'`, **Height** = 40, à gauche du titre.

# 6. Couleur des notes

Contrôles des notes (texte gris pâle sous les sections) : **Color** = `RGBA(55; 65; 81; 1)` pour une meilleure lisibilité.

# 7. Retirer la 7ᵉ variable d'environnement

La solution contient encore `rhdsst_shared_sharepointonline_9db72454…` (« SandBox Annie Audet… »). Elle n'est pas utilisée et exporte l'adresse du bac à sable.

1. **Solutions** › Solution-ApplicationAppréciation › **Variables d'environnement**.
2. Cochez cette variable › **⋯ › Supprimer de cette solution** (pas « Supprimer »).

# Ensuite

1. **Enregistrer**, **Publier**.
2. Solution › **Exporter** › géré › version **1.0.0.9**.
3. Envoyez le ZIP aux TI avec `transmission-TI/Transmission-TI-PreProd.zip`.
