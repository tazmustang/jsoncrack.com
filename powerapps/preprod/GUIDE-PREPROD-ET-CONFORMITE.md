---
title: "Appréciation de la contribution (APCONT) — Site PréProd et conformité aux exigences des TI"
subtitle: "VERSION FINALE — 30 octobre 2026 · Tout ce qu'il faut faire, dans l'ordre"
lang: fr-CA
---

# 0. Vue d'ensemble

Ce guide couvre **toutes** les exigences du document des TI (points 1 à 10, conventions de nommage, groupes d'application) et la préparation du **site PréProd**.

| Partie | Quoi | Où | Durée estimée |
|---|---|---|---|
| A | Préparer le **site PréProd** : bibliothèque Documents TI, groupes, listes, autorisations | Site SharePoint PréProd | 1 h 30 |
| B | Ajuster la **solution** dans le bac à sable : noms des variables, bascule d'export, flux | Bac à sable (Power Apps et Power Automate) | 2 h |
| C | Ajuster l'**application** : commentaires, mise en forme, confirmation, validation, erreurs, À propos, Aide | Bac à sable (Power Apps) | 3 à 4 h |
| D | Exporter la solution **gérée 1.0.0.4** et la remettre aux TI | Bac à sable | 30 min |
| E | Déposer la **documentation** dans Documents TI | Site PréProd | 30 min |
| F | **Tester** en PréProd | Application PréProd | 1 h |

**Fichiers qui accompagnent ce guide :**

| Fichier | Sert à |
|---|---|
| `FORMULES-CONFORMITE.txt` | Toutes les formules de la partie C, commentées et prêtes à coller |
| `FLUX-FINAUX.txt` (mis à jour) | Les 3 flux avec les nouveaux noms de variables et la gestion des erreurs |
| `documents-TI/` | Les 5 documents exigés (point 1) : matrice de sécurité, matrice de métadonnées, architecture, liste des utilisateurs, révision des versions |

## Les noms à utiliser partout (convention des TI)

Acronyme de l'application : **APCONT**. Acronyme du service : **RHSST** (à remplacer par l'acronyme officiel du service s'il est différent).

| Élément | Nom à utiliser |
|---|---|
| Variable du site | **APCONT_SiteWeb-RHSST-AppreciationContribution** |
| Variable de la liste des dossiers | **APCONT_Appreciations** |
| Variable de la liste des paramètres | **APCONT_Parametres** |
| Variable courriel de la paie | **APCONT_CourrielPaie** |
| Variable lien de l'application | **APCONT_LienApplication** |
| Variable courriel du soutien (**nouvelle**) | **APCONT_CourrielSoutien** |
| Liste des dossiers (PréProd et Prod) | **APCONT_Appreciations** |
| Liste des paramètres (PréProd et Prod) | **APCONT_Parametres** |
| Groupe SharePoint local des utilisateurs | **APCONT_Utilisateurs** (contient le groupe Entra **G-IS-APP-xxxxx** de l'environnement) |
| Groupe SharePoint local des RH | **APCONT_RH** |
| Bibliothèque de documentation | **Documents TI** |

> ⚠️ **Le nom de schéma** des variables (`rhdsst_…`) **ne peut pas être changé** dans Power Platform. Seul le **nom d'affichage** change. C'est normal et accepté.

# Partie A — Le site PréProd

Ouvrez le site PréProd créé par les TI. Notez son adresse : *[adresse du site PréProd]*.

## A1. La bibliothèque « Documents TI »

1. Si elle n'existe pas : **+ Nouveau › Bibliothèque de documents › Bibliothèque vide**, nom **Documents TI**, puis **Créer**.
2. Vous y déposerez les documents à la **partie E**.

## A2. Les deux groupes locaux de l'application

Les groupes **n'ont aucun droit sur le site** : ils reçoivent leurs droits seulement sur les listes (partie A4).

1. Roue ⚙️ en haut à droite › **Autorisations du site** › **Paramètres d'autorisations avancés**.
2. Dans le ruban : **Créer un groupe**.
3. Nom : **APCONT_Utilisateurs**. Description : « Utilisateurs de l'application Appréciation de la contribution ».
4. Propriétaire du groupe : vous-même (ou le compte de service).
5. En bas, section **Accorder des autorisations au groupe sur ce site** : **ne cochez aucune case**.
6. **Créer**.
7. Dans le groupe : **Nouveau › Ajouter des utilisateurs**, tapez le nom du groupe Entra **G-IS-APP-xxxxx** de l'environnement PréProd (fourni par les TI), puis **Partager**.
8. Recommencez les étapes 2 à 6 pour **APCONT_RH**. Ajoutez-y les personnes des RH autorisées à consulter **tous** les dossiers.
9. Vérifiez que le **compte de service** des flux est dans le groupe **Propriétaires** du site (sinon, demandez-le aux TI).

✅ Les deux groupes apparaissent dans la liste des groupes, **sans niveau d'autorisation** sur le site.

## A3. Les deux listes

La méthode la plus sûre : recopier les listes du bac à sable. Toutes les colonnes, leurs noms internes et leurs choix sont recopiés exactement.

1. Accueil du site PréProd : **+ Nouveau › Liste**.
2. Choisissez **À partir d'une liste existante**.
3. Choisissez le **site du bac à sable** (SandBoxAnnieAudet), puis la liste **Appreciations**, puis **Suivant**.
4. Nom : **APCONT_Appreciations**. Description : « Dossiers de l'application Appréciation de la contribution ». **Créer**.
5. Recommencez avec la liste **Parametres** du bac à sable, nom **APCONT_Parametres**.

**Vérifiez les réglages de APCONT_Appreciations** (⚙️ › **Paramètres de la liste**) :

| Réglage | Où | Valeur |
|---|---|---|
| Versions | Paramètres de contrôle de version | Historique des versions : **Oui** |
| Pièces jointes | Paramètres avancés | Pièces jointes : **Activé** |
| Colonne TypeRencontre | Cliquez sur la colonne | **Cases à cocher (autoriser plusieurs sélections)** |
| Index | Colonnes indexées › Créer un index | **Annee, Statut, CourrielPersonne, CourrielSI, CourrielSH, CourrielDirecteur** (6 index, un à la fois). **Pas** TypeRencontre |
| Choix de Statut | Cliquez sur la colonne Statut | Brouillon · Avisé au supérieur · Certifié · Approuvé SI · Approuvé SH · Approuvé directeur · Complété (défaut : Brouillon) |

**Remplissez APCONT_Parametres** (**+ Nouveau** élément, colonnes **Title** et **Valeur**) :

| Title | Valeur |
|---|---|
| Environnement | **PRE-PROD** |
| CourrielSoutien | *[adresse courriel du soutien]* |
| SupportNom | *[nom de la personne responsable du soutien]* |
| SupportTelephone | *[numéro de téléphone du soutien]* |

Supprimez les éléments recopiés qui ne sont pas dans ce tableau, s'il y en a.

## A4. Les autorisations des listes

**APCONT_Appreciations :**

1. ⚙️ › **Paramètres de la liste** › **Autorisations pour cette liste**.
2. Ruban : **Arrêter l'héritage des autorisations** › **OK**.
3. Cochez **Membres** et **Visiteurs** du site › **Supprimer les autorisations utilisateur** › **OK**.
4. **Accorder des autorisations** : tapez **APCONT_Utilisateurs**, niveau **Collaboration**, décochez « Envoyer une invitation » › **Partager**.
5. **Accorder des autorisations** : **APCONT_RH**, niveau **Lecture** › **Partager**.

✅ Il reste exactement : **Propriétaires** (Contrôle total), **APCONT_Utilisateurs** (Collaboration), **APCONT_RH** (Lecture).

**APCONT_Parametres :** mêmes étapes, mais **APCONT_Utilisateurs** et **APCONT_RH** en **Lecture** : les utilisateurs lisent les paramètres, ils ne les modifient jamais.

> 💡 Pourquoi Collaboration sur APCONT_Appreciations ? Chaque personne doit pouvoir **créer** son dossier. Dès la création, le flux 1 coupe l'héritage du dossier et retire **APCONT_Utilisateurs** : seules les personnes du dossier, les RH et les propriétaires y ont accès.

## A5. Ce que les TI font ensuite (à leur fournir)

| Variable | Valeur PréProd |
|---|---|
| APCONT_SiteWeb-RHSST-AppreciationContribution | *[adresse du site PréProd]* |
| APCONT_Appreciations | liste **APCONT_Appreciations** |
| APCONT_Parametres | liste **APCONT_Parametres** |
| APCONT_CourrielPaie | votre adresse (tests) |
| APCONT_LienApplication | lien web de l'application PréProd (après import) |
| APCONT_CourrielSoutien | *[adresse du soutien]* |

Ce tableau est aussi dans l'onglet **Variables** du fichier Excel.

# Partie B — La solution dans le bac à sable

## B1. Créer le groupe APCONT_Utilisateurs dans le bac à sable aussi

Le flux 1 va maintenant retirer le groupe **APCONT_Utilisateurs** de chaque dossier. Ce groupe doit donc exister **dans tous les sites**, bac à sable compris.

1. Sur le site du bac à sable, refaites l'étape **A2** pour **APCONT_Utilisateurs** et ajoutez-y vos testeurs.
2. Sur la liste **Appreciations** du bac à sable, refaites l'étape **A4** : retirez Membres et Visiteurs, puis ajoutez APCONT_Utilisateurs (Collaboration) et RH – Appréciations (Lecture).

> Ne renommez **pas** les listes du bac à sable pour l'instant : un changement de nom de liste peut changer le nom de la source de données dans l'application et créer des centaines d'erreurs. Les listes PréProd et Prod portent déjà les bons noms, et la variable d'environnement fait le lien.

## B2. Renommer les variables d'environnement

1. **make.powerapps.com** › **Solutions** › **Solution-ApplicationAppreciation**.
2. Cliquez sur chaque variable d'environnement, changez le **Nom d'affichage** (le nom de schéma ne bouge pas), puis **Enregistrer** :

| Ancien nom d'affichage | Nouveau nom d'affichage | Nom de schéma (inchangé) |
|---|---|---|
| Site Appréciations | APCONT_SiteWeb-RHSST-AppreciationContribution | rhdsst_SiteApprciations |
| Liste Appreciations | APCONT_Appreciations | rhdsst_ListeAppreciations |
| Liste Parametres | APCONT_Parametres | rhdsst_ListeParametres |
| Courriel paie | APCONT_CourrielPaie | rhdsst_Courrielpaie |
| Lienapplication | APCONT_LienApplication | rhdsst_Lienapplication |

3. **Nouvelle variable :** **+ Nouveau › Plus › Variable d'environnement**.
   - Nom d'affichage : **APCONT_CourrielSoutien** ; Type : **Texte**.
   - Valeur actuelle : votre adresse.
   - **Enregistrer**.

## B3. La bascule « Exporter la valeur » = Non (pour les 6 variables)

1. Cliquez sur la variable.
2. Dans le panneau, ouvrez **Avancé**.
3. Mettez la bascule **Exporter la valeur actuelle** (ou « Ne pas exporter la valeur ») de façon à ce que la valeur **ne soit pas exportée** : la bascule d'export doit être à **Non**.
4. **Enregistrer**.

Cette méthode **remplace** celle de l'ancien guide (« Retirer de cette solution » la valeur actuelle). Laissez la **valeur par défaut** vide.

## B4. Mettre à jour les 3 flux

Après le renommage, les expressions qui contiennent l'ancien nom (ex. `parameters('Liste Appreciations (rhdsst_ListeAppreciations)')`) ne trouvent plus la variable. Il faut les mettre à jour. **FLUX-FINAUX.txt** contient toutes les expressions avec les nouveaux noms.

**Pour chaque flux** (Solutions › la solution › le flux › **Modifier**) :

1. **Champs « Adresse du site » et « Nom de la liste »** (déclencheurs et actions SharePoint) : cliquez dans le champ, effacez, puis choisissez la variable dans le **contenu dynamique**, section **Variables d'environnement** (ex. APCONT_Appreciations).
2. **Champs avec une expression** (URI des requêtes HTTP, variables LienApp et CourrielPaie) : recopiez l'expression de FLUX-FINAUX.txt.
3. **Enregistrer**. Le vérificateur de flux ne doit indiquer aucune erreur.

| Flux | Endroits à mettre à jour |
|---|---|
| **Flux 1** | Déclencheur (site, liste) ; actions 2, 4 et 6b (URI) ; toutes les actions HTTP (adresse du site) ; **action 3 : nouvelle URI** (voir B5) |
| **Flux 2** | Déclencheur ; LienApp ; CourrielPaie ; Changements ; 4a, 4b ; 6.4a, 6.4b, 6.4c ; Date paie |
| **Flux 3** | Pièces jointes ; Supprimer la pièce jointe ; Ajouter PDF |

## B5. Flux 1 : retirer le groupe APCONT_Utilisateurs (au lieu des Membres)

Dans le flux 1, action **« Groupe Membres »** : **gardez le nom de l'action** et remplacez seulement l'**URI** par :

```
_api/web/sitegroups/getbyname('APCONT_Utilisateurs')?$select=Id
```

L'action 4 « Retirer les Membres » n'a pas à changer : elle retire maintenant APCONT_Utilisateurs du dossier.

## B6. Gestion des erreurs dans les 3 flux (exigence 6)

Pour **chaque** flux :

1. Juste sous le déclencheur, ajoutez **Contrôle › Étendue** et renommez-la **Essayer**.
2. **Glissez toutes les actions** du flux **dans** l'étendue Essayer, en gardant leur ordre.
3. **Sous** l'étendue (à l'extérieur), ajoutez **Office 365 Outlook › Envoyer un courriel (V2)** et renommez-la **Courriel erreur**.
4. Sur Courriel erreur : **⋯ › Paramètres** (ou « Configurer l'exécution après ») : cochez **a échoué** et **a expiré**, décochez **a réussi**.
5. Remplissez :
   - **À :** variable **APCONT_CourrielSoutien** ;
   - **Objet** et **Corps** : voir FLUX-FINAUX.txt, section « Gestion des erreurs ».
6. **Flux 3 seulement :** ajoutez, sous Courriel erreur, une action **Répondre à une application ou à un flux Power Apps** avec la sortie **lien** vide. L'application affiche alors un message clair au lieu d'une erreur.
7. **Enregistrer.**

# Partie C — L'application (exigences 2 à 8)

Ouvrez l'application en **Modifier** (Solutions › la solution › l'application). Toutes les formules sont dans **FORMULES-CONFORMITE.txt**, numérotées comme ci-dessous.

## C1. Commentaires dans toutes les fonctions (exigence 2)

- Chaque formule importante commence par une ligne de commentaire `// …` qui dit **ce qu'elle fait**.
- Les formules longues (OnVisible, btnDeposer, PDF) sont déjà commentées par section.
- Pour les autres, la section **C1** du fichier donne la ligne de commentaire à ajouter **au début** de chaque formule.

**Comment faire :** cliquez sur le contrôle, choisissez la propriété, cliquez au tout début de la barre fx, collez la ligne de commentaire, puis faites **Entrée**.

## C2. Formules lisibles (exigence 3)

Pour **chaque** formule de plus d'une ligne : cliquez dans la barre fx, puis sur **Mettre en forme le texte** (Format text), sous la barre fx, à droite. Power Apps indente la formule automatiquement.

Faites-le au minimum pour : scrFormulaire.OnVisible, btnDeposer, btnDeposerExec, btnApercuPDF, App.OnError, les boutons Aviser, Certifier et Approuver, et btnEnvoyerSoutien.

## C3. Confirmation de création (exigence 4)

L'application **crée** un enregistrement (le dossier) au premier **Enregistrer et déposer**. Elle demandera maintenant une confirmation. Voir la section **C3** du fichier :

1. **Copiez btnDeposer** (Ctrl + C, Ctrl + V). Renommez la copie **btnDeposerExec** et mettez sa propriété **Visible** à `false`. Sa formule OnSelect reste l'**ancienne formule complète** : c'est elle qui enregistre.
2. Créez la **fenêtre de confirmation** (conteneur **conConfirmer**, 2 boutons Oui et Non), selon les propriétés du fichier.
3. Remplacez la formule **btnDeposer.OnSelect** par la nouvelle formule (C4). Elle valide les champs, demande la confirmation si c'est une création, puis lance btnDeposerExec.

**Suppression :** l'application **ne supprime aucun enregistrement**. Il n'y a pas de bouton Supprimer. Les seules suppressions se font :
- dans SharePoint, par les propriétaires, avec la **corbeille** comme filet de sécurité (gestion du cycle de vie, partie E) ;
- par le flux 3, qui **remplace** l'ancien PDF du dossier par le nouveau. C'est annoncé à l'écran : « le PDF remplace la version précédente ».

Ces règles sont inscrites dans le document d'architecture.

## C4. Validation des champs (exigence 5)

La nouvelle formule de **btnDeposer** (section **C4**) vérifie, avant tout enregistrement :

- le **nom** ;
- l'**ID** de l'employé ;
- le **type de poste** ;
- au moins un **type de rencontre** ;
- la **précision « Autre »** si Autre est coché ;
- le **directeur** si « Approbation du directeur requise » est cochée.

S'il manque quelque chose, un message jaune liste les champs à compléter, et **rien n'est enregistré**.

## C5. Gestion des erreurs dans l'application (exigence 6)

1. Arborescence › **App** › propriété **OnError** : collez la formule **C5**. Toute erreur imprévue affiche un message clair et invite à utiliser « À propos » pour joindre le soutien.
2. **btnDeposerExec** affiche déjà l'erreur précise si SharePoint refuse l'enregistrement.
3. **btnApercuPDF** affiche un message si le PDF n'a pas pu être créé.
4. Les **flux** envoient un courriel au soutien en cas d'échec (B6).

## C6. Écran « À propos… » (exigence 7)

1. **Ajouter une source de données** : **Office 365 Outlook**. Choisissez la référence de connexion **Outlook Appreciations** si elle est proposée.
2. **Nouvel écran › Vide**, renommez-le **scrAPropos**.
3. Ajoutez les contrôles de la section **C6** : titre, nom de l'application, version, responsable du soutien, **téléphone**, courriel, et un **formulaire d'envoi de courriel** (sujet, message, bouton Envoyer).
4. Ajoutez un bouton **ℹ️ À propos** :
   - sur **scrMesDossiers** (en haut à droite) ;
   - sur **scrFormulaire** (barre de gauche).

   OnSelect : `Navigate(scrAPropos; ScreenTransition.None)`

Le nom, le téléphone et le courriel du soutien sont lus dans la liste **APCONT_Parametres**. On les change sans republier l'application.

## C7. Écran d'aide (modèle Didacticiel) (exigence 8)

1. **Nouvel écran** › modèle **Didacticiel** (Tutorial). Renommez-le **scrAide**.
2. Le modèle contient des **étapes** : titre, texte, image, et des boutons Précédent/Suivant. Remplacez le contenu des étapes par les **5 pages** de la section **C7** :
   1. Bienvenue ;
   2. Mes dossiers ;
   3. Le formulaire ;
   4. Le circuit d'approbation et le PDF ;
   5. À propos et soutien.
3. **Images :** prenez une capture de chaque écran (Windows + Maj + S), puis **Médias › Charger**, et choisissez-les dans les étapes.
4. Ajoutez un bouton **❓ Aide** sur scrMesDossiers et sur scrFormulaire. OnSelect : `Navigate(scrAide; ScreenTransition.None)`
5. Sur scrAide, le bouton de fin ou de retour : `Back()`

> Si la structure du modèle Didacticiel diffère, gardez la même idée : **une étape par écran**, avec une image et la description.

## C8. Enregistrer et publier

1. **Vérificateur d'application** (stéthoscope) : **0 erreur**.
2. **Enregistrer**, puis **Publier**.

# Partie D — Exporter et remettre aux TI

1. Solution › **Objets** : vérifiez la présence de l'application, des **3 flux**, des **6 variables** et des **4 références de connexion**. Ajoutez celle d'**Outlook** si elle n'y est pas.
2. **Publier toutes les personnalisations**.
3. Version : **1.0.0.4**.
4. **Exporter** › **Gérée** › **Exporter**. Téléchargez `Solution-ApplicationAppreciation_1_0_0_4_managed.zip`.
5. Remettez-le aux TI avec le tableau des valeurs PréProd (A5).
6. Mettez à jour le document **APCONT_Revision-versions** (partie E).

# Partie E — La documentation dans « Documents TI » (exigence 1)

Déposez dans la bibliothèque **Documents TI** du site PréProd (et plus tard du site Prod) :

| Exigence | Fichier fourni (dossier documents-TI) |
|---|---|
| 1a. Matrice de sécurité | **APCONT_Matrice-securite.xlsx** |
| 1b. Matrice de métadonnées | **APCONT_Matrice-metadonnees.xlsx** |
| 1c. Architecture et fonctionnalités | **APCONT_Architecture-application.docx** |
| 1d. Pipeline (dev, PréProd, Prod et sites) | Inclus dans **APCONT_Architecture-application.docx**, partie 4 |
| 1e. Liste des utilisateurs | **APCONT_Liste-utilisateurs.xlsx** |
| 1f. Révision des versions | **APCONT_Revision-versions.docx** |
| Complément | GUIDE-MISE-EN-PRODUCTION.docx, FLUX-FINAUX.txt, Schema-solution.jpg |

Avant de déposer : remplacez les ***[éléments entre crochets]*** (adresses des sites, groupes Entra, téléphone du soutien, durée de conservation).

**Cycle de vie des données (exigence 9) :** il est décrit dans l'architecture, partie 6. La **durée de conservation** et la **procédure de destruction** doivent être confirmées avec la **gestion documentaire** et les TI : demandez-leur l'information, comme le guide des TI le recommande.

# Partie F — Tests en PréProd

| N° | Test | Résultat attendu | ✓ |
|---|---|---|---|
| 1 | Un testeur ouvre l'application | Elle s'ouvre (pas de message de groupe de sécurité) | |
| 2 | Enregistrer et déposer avec un champ obligatoire vide | Message jaune ; rien n'est créé | |
| 3 | Enregistrer et déposer un nouveau dossier complet | Fenêtre de confirmation ; Oui › message vert | |
| 4 | Gérer l'accès du dossier, dans SharePoint | Propriétaires, APCONT_RH, personnes du dossier. **Pas** APCONT_Utilisateurs | |
| 5 | Un autre testeur, sans lien avec ce dossier | Ne le voit pas, ni dans l'application ni dans SharePoint | |
| 6 | Circuit complet jusqu'à Complété | Courriels reçus ; lecture seule ; Transmis aux RH | |
| 7 | Aperçu PDF, puis Ouvrir le PDF | PDF joint au dossier, type de rencontre et cotes à 4 niveaux visibles | |
| 8 | À propos | Nom, version, responsable, **téléphone** ; message envoyé reçu par le soutien | |
| 9 | Aide | 5 étapes avec images | |
| 10 | Provoquer une erreur de flux (ex. CourrielSI vide sur un dossier test) | Courriel d'erreur reçu par le soutien | |
| 11 | Parametres : Environnement = PRE-PROD | La version et l'environnement sont affichés dans À propos | |

Notez les résultats dans le **DOSSIER-AUTORISATION-TI**, tableau des tests.
