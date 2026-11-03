---
title: "Liste des appréciations — La rendre lisible et exporter les données"
subtitle: "Application Appréciation de la contribution (SRHVQ) · Outils inclus : SharePoint et Excel · 3 novembre 2026"
lang: fr-CA
---

# 1. Pourquoi la liste affiche du « code »

Les sections à **plusieurs lignes** du formulaire (objectifs, postures, valeurs, développement, compétences) sont rangées chacune dans **une seule colonne**, sous forme de texte structuré (format **JSON**). Exemple : `{"besoin":"…","moyen":"…"}`.

- C'est **voulu**. L'application relit ce texte pour réafficher les tableaux, ligne par ligne.
- **Il ne faut pas modifier ces colonnes à la main** dans SharePoint. Un guillemet de trop, et l'application ne peut plus relire la section.
- **La version lisible d'un dossier, c'est son PDF** (bouton Aperçu PDF), joint au dossier.

Ce guide propose 3 solutions, de la plus simple à la plus complète :

| Besoin | Solution | Partie |
|---|---|---|
| Une liste claire pour suivre les dossiers | Un **affichage** sans les colonnes de code | 2 |
| Une fiche de dossier propre dans SharePoint | **Masquer** les colonnes de code dans le formulaire | 3 |
| Exporter et analyser des colonnes | **Export Excel**, et **Power Query** pour les colonnes de code | 4 |

# 2. Un affichage « Suivi » clair (10 minutes)

Un affichage est une façon de voir la liste. On en crée un qui montre seulement les colonnes utiles.

1. Ouvrez la liste des appréciations dans SharePoint.
2. En haut à droite, cliquez sur le nom de l'affichage (ex. « Tous les éléments ») › **Créer un affichage**.
3. Nom : **Suivi des appréciations** · Afficher en tant que : **Liste** · **Créer**.
4. Cliquez sur l'en-tête d'une colonne › **Paramètres de colonne** › **Afficher/masquer les colonnes**. Cochez seulement :

| Colonne | Pourquoi |
|---|---|
| Nom, prénom (Titre) | Qui |
| IdEmploye | ID |
| Annee | Année |
| TypePoste | Formulaire utilisé |
| Statut | Où en est le dossier |
| SuperieurImmediat | Gestionnaire |
| EvaluationGlobale | Résultat (RH) |
| CertifieLe, ApprouveSILe, TransmisPaieLe | Dates clés |
| Pièces jointes | Le trombone indique que le PDF est joint |

5. **Appliquer**. Glissez les colonnes pour les mettre dans l'ordre voulu.
6. **Regrouper par Statut** (facultatif) : en-tête **Statut** › **Regrouper par Statut**.
7. En haut à droite : nom de l'affichage › **Enregistrer l'affichage sous** › cochez **Faire de cet affichage l'affichage par défaut** (si vous le souhaitez) › **Enregistrer**.

✅ La liste devient un tableau de bord lisible. Pour lire un dossier en détail, ouvrez son PDF (trombone, ou panneau de l'élément › Pièces jointes).

# 3. Une fiche de dossier propre (5 minutes)

La fiche d'un élément (le panneau qui s'ouvre quand on clique sur un dossier) peut cacher les colonnes de code.

1. Ouvrez un dossier dans la liste.
2. En haut du panneau : icône **Modifier le formulaire** (crayon) › **Modifier les colonnes**.
3. **Décochez** : ObjectifsActuels, ObjectifsAvenir, Postures, Competences, Valeurs, DevPrecedents, DevNouveaux. Décochez aussi, au besoin, les colonnes techniques : CourrielPersonne, CourrielSI, CourrielSH, CourrielDirecteur, VersionFormulaire.
4. **Enregistrer**.

✅ La fiche affiche l'identification, le statut, les bilans (E et F : déjà en texte clair), l'évaluation globale, les dates et le **PDF en pièce jointe**.

> Ce réglage cache les colonnes **dans SharePoint seulement**. L'application et ses données ne changent pas.

# 4. Exporter des colonnes

## 4.1 Export simple vers Excel (colonnes ordinaires)

1. Choisissez l'affichage **Suivi des appréciations** (partie 2) : seules ses colonnes seront exportées.
2. Filtrez au besoin (ex. Année = 2026, Statut = Complété) : clic sur l'en-tête › **Filtrer par**.
3. Barre du haut : **Exporter** › **Exporter au format CSV** (le plus simple), ou **Exporter vers Excel**.
4. Ouvrez le fichier dans Excel, puis **Fichier › Enregistrer sous** › classeur Excel (.xlsx).

✅ Une ligne par dossier, avec les colonnes choisies.

## 4.2 Les colonnes de code en tableaux lisibles (Excel, Power Query)

Pour exporter les **objectifs**, les **cotes des postures**, les **valeurs** ou le **développement** sous forme de vrai tableau (une ligne par objectif, par cote, etc.), Excel peut **lire le code** et le transformer, avec Power Query (inclus dans Excel). Les requêtes sont prêtes à coller dans **REQUETES-EXCEL-POWER-QUERY.txt**.

**La première fois (10 minutes) :**

1. Ouvrez **Excel** (un classeur vide).
2. **Données › Obtenir des données › À partir d'autres sources › Requête vide**. L'éditeur Power Query s'ouvre.
3. **Accueil › Éditeur avancé**. Effacez tout.
4. Ouvrez REQUETES-EXCEL-POWER-QUERY.txt, copiez **une** requête (de `let` jusqu'au `Renomme` final), collez-la, puis **Terminé**.
5. Si Excel demande une connexion : choisissez **Compte Microsoft** › **Se connecter** avec votre compte de la Ville › **Se connecter** (en bas).
6. Dans la liste de droite, renommez la requête (ex. « Objectifs de l'année »).
7. **Accueil › Fermer et charger**. Le tableau s'affiche dans une feuille Excel.
8. Recommencez les étapes 2 à 7 pour chaque autre requête voulue : chacune crée sa propre feuille.
9. **Enregistrez** le classeur (ex. « Extraction-appreciations.xlsx »), dans un endroit **sécurisé** (voir 4.3).

**Les fois suivantes :** ouvrez le classeur, puis **Données › Actualiser tout**. Les tableaux se mettent à jour avec les nouveaux dossiers.

| Requête | Contenu, une ligne par… |
|---|---|
| 1. Objectifs de l'année | objectif : objectif, indicateur, actions |
| 2. Objectifs à venir | objectif à venir : objectif, indicateur |
| 3. Postures — cotes | comportement : cote de la personne, cote du supérieur |
| 4. Postures — commentaires | posture : exemples et commentaires |
| 5. Compétences | compétence (professionnels) : exemples |
| 6. Grands fondements | thème coché : exemples 1 et 2 |
| 7. Développement passé | objectif : moyens, résultats |
| 8. Nouveaux besoins | besoin : moyen |

Chaque ligne indique aussi le **no de dossier**, le **nom**, l'**ID** et l'**année**, pour filtrer ou faire un tableau croisé dynamique.

**À adapter au besoin :** les 2 premières lignes de chaque requête.
- `Site` : l'adresse du site (PréProd, puis Prod).
- `NomListe` : le **nom affiché** de la liste. Si vous la renommez (ex. SRHVQ_Appreciations), changez-le ici aussi.

**Si un message d'erreur apparaît :**

| Message | Solution |
|---|---|
| « La clé ne correspond à aucune ligne de la table » | Le nom de la liste (`NomListe`) n'est pas exact : copiez-le tel qu'il s'affiche dans SharePoint |
| « La colonne … est introuvable » | Une colonne a un autre nom interne dans cette liste : envoyez-moi le message |
| « Accès refusé » | Votre compte n'a pas accès à la liste ou à certains dossiers |

## 4.3 Confidentialité des exports (important)

- Excel ne voit **que les dossiers auxquels votre compte a accès**. Les permissions de SharePoint s'appliquent.
- Un fichier exporté **contient des évaluations du rendement**. Une fois exporté, il n'est **plus protégé** par les autorisations de la liste.
- Enregistrez-le seulement dans un **espace RH sécurisé**. Ne l'envoyez jamais par courriel, et supprimez-le quand il n'est plus nécessaire (gestion du cycle de vie).

# 5. En résumé

| Je veux… | Je fais… |
|---|---|
| Suivre où en sont les dossiers | Affichage **Suivi des appréciations** (partie 2) |
| Lire un dossier complet | Son **PDF** joint au dossier |
| Une fiche SharePoint sans code | **Modifier le formulaire › Modifier les colonnes** (partie 3) |
| Une liste de dossiers dans Excel | **Exporter au format CSV** depuis l'affichage (4.1) |
| Les objectifs, cotes, valeurs… en tableau | **Power Query** avec les requêtes fournies (4.2) |
