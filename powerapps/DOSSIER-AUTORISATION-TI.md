---
title: "Dossier de demande d'autorisation de déploiement"
subtitle: "Application « Appréciation de la contribution » (Power Apps, SharePoint, Power Automate) — VERSION FINALE — 28 octobre 2026, mise à jour du 29 octobre (transmission PréProd)"
lang: fr-CA
---

# 1. Le formulaire des TI : « Demande de mise en PréProd/Prod Power Apps »

Le formulaire des TI est **court**. Avec le *Guide de mise en production* et le fichier Excel, **vous avez tout ce qu'il demande**. Il reste seulement à **exporter le .zip** et à remplir les champs ci-dessous.

| Champ du formulaire | Quoi mettre |
|---|---|
| **Type de mise en production** | **PréProd** pour la première demande. Faites une **2ᵉ demande « Prod »** une fois les tests de pré-prod réussis. |
| **Nom de l'application** | Appréciation de la contribution |
| **Acronyme de l'application** | Proposition : **SRHVQ**. Vérifiez s'il existe une convention d'acronymes, ou demandez-la aux TI. |
| **Libraire** | Choisissez dans la liste la personne des TI qui fait habituellement les mises en production. Pour une 1ʳᵉ demande, prenez celle de votre secteur, ou demandez à votre répondant TI. |
| **Date souhaitée** | Laissez **au moins 2 semaines** : les TI doivent créer le site et les listes avant l'import. |
| **Pièces jointes** | Le tout est regroupé dans `Transmission-TI-PreProd-Appreciation.zip` (voir le BORDEREAU-TRANSMISSION-TI) : 1) `Solution-ApplicationAppreciation_1_0_0_4_managed.zip` (guide 9.1 et 9.2) · 2) `Variables-environnement-et-deploiement.xlsx`, avec la **colonne Pré-prod remplie** · 3) conseillé : `GUIDE-MISE-EN-PRODUCTION.docx` et `Schema-solution.jpg` |
| **Commentaires** | Le texte ci-dessous, à copier-coller |

**Texte pour « Commentaires » :**

> Première mise en PréProd de la solution Solution-ApplicationAppreciation (version 1.0.0.4, gérée). Contenu : 1 application canevas, 3 flux (Appréciation – Permissions à la création, Appréciation – Suivi des étapes, GenererPDFAppreciation), 5 variables d'environnement et 4 références de connexion (SharePoint Appreciation, Utilisateurs Office 365 Appreciations, Outlook Appreciations, OneDrive Appreciations). Connecteurs standard seulement, aucune licence Premium.
>
> Préalables à l'import : un site SharePoint de PréProd avec la liste Appreciations (35 colonnes), la liste Parametres (pièces jointes activées sur Appreciations) et le groupe RH – Appréciations. La structure et les autorisations sont dans l'onglet « SharePoint » du fichier Excel et dans la partie 4 du guide joint.
>
> Connexions : merci d'utiliser un compte de service, propriétaire du site, pour les 4 références de connexion.
>
> Testeurs : merci d'ajouter au groupe de sécurité de l'environnement PréProd (et au groupe Membres du site SharePoint de PréProd) les personnes suivantes, qui feront les tests avec du contenu fictif : *[noms des collègues]*. Actuellement, elles reçoivent le message « You are not a member of the environment's security group ».
>
> Après l'import : inscrire le lien web de l'application dans la variable Lienapplication, activer les 3 flux et partager l'application avec *[groupe de gestionnaires]*. La liste de vérification est dans l'onglet « Checklist TI » du fichier Excel.
>
> Données RH confidentielles (appréciations) : l'accès est limité dossier par dossier par le flux 1.

## Avant d'envoyer le formulaire

1. **Faites les tests** de la partie 8 du guide dans le bac à sable. Au minimum : un circuit complet jusqu'à « Complété », et le PDF.
2. **Préparez et exportez la solution** (guide 9.1 et 9.2) :
   - retirez la valeur actuelle des 5 variables ;
   - publiez ;
   - passez en version 1.0.0.4 ;
   - exportez en **Gérée**.
3. **Remplissez la colonne Pré-prod** de l'onglet Variables du fichier Excel. Pour le site et les listes, écrivez « à créer par les TI » si vous ne connaissez pas encore l'adresse.

# 2. Au-delà du formulaire : ce qui est recommandé

Le formulaire des TI ne demande pas les éléments ci-dessous. Ils restent **importants pour une application qui contient des évaluations d'employés**, et certains sont **obligatoires par la loi** (partie 5). Ils ne bloquent pas l'envoi du formulaire, mais **réglez-les avant la mise en production (Prod)**. Les plus importants :

- l'**EFVP** auprès du responsable de la protection des renseignements personnels ;
- le **délai de conservation**, avec la gestion documentaire ;
- le **compte de service** ;
- un **suppléant** ;
- un **guide d'utilisation** pour les employés.

# 3. Questions utiles à poser aux TI

1. Avez-vous un **formulaire de demande de mise en production** ou une **liste d'exigences** pour les applications Power Platform ?
2. Quel est le processus d'**autorisation** : comité des changements, architecture, sécurité, délais ?
3. Qui crée et gère les environnements **pré-prod** et **prod**, ainsi que les **sites SharePoint** correspondants ?
4. Qui fournit le **compte de service** des flux, et selon quel processus (licence, mot de passe, authentification multifacteur) ?
5. Quelle **stratégie de prévention des pertes de données (DLP)** s'applique à ces environnements ? SharePoint, Office 365 Users, Office 365 Outlook et OneDrive Entreprise doivent être permis **ensemble**.
6. Exigez-vous un rapport du **Vérificateur de solution** (Solution Checker) sans erreur critique ?
7. Qui doit approuver le volet **protection des renseignements personnels** (responsable de l'accès et de la PRP, comité) ?
8. Quelle **classification** et quel **délai de conservation** s'appliquent aux appréciations ? Faut-il consulter la gestion documentaire ?
9. Quelles sont vos exigences d'**accessibilité** (ex. WCAG 2.1 AA, standard gouvernemental SGQRI 008) ?
10. Quelle **boîte aux lettres de la paie** doit recevoir les évaluations ?

# 4. Tableau de conformité : où en êtes-vous

Légende : ✅ prêt · ⚠️ partiel · ❌ à produire

| N° | Exigence habituelle des TI | État | Ce qui existe | Ce qu'il manque |
|---|---|---|---|---|
| 1 | Description du besoin, du contexte et des bénéfices | ⚠️ | Quelques lignes dans le guide | Fiche projet (partie 6.1) |
| 2 | Architecture et composants | ✅ | Schéma, guide parties 2 et 4, fichier Excel (onglet Solution) | — |
| 3 | Solution gérée, versionnée, avec variables d'environnement | ✅ | Guide parties 9.1 à 9.5 | Le .zip lui-même, au moment de la remise |
| 4 | Connecteurs uniquement standard, sans Premium | ✅ | Guide partie 2 | Confirmation des TI pour la DLP (question 5) |
| 5 | Compte de service pour les flux | ❌ | Les flux tournent avec **votre** compte dans le bac à sable | Demande aux TI (partie 6.6) |
| 6 | Modèle d'accès et de sécurité | ⚠️ | Guide partie 4 | Matrice des accès et risques résiduels (partie 6.3) |
| 7 | **Évaluation des facteurs relatifs à la vie privée (EFVP)** | ❌ | — | **Obligatoire** (partie 5.1) |
| 8 | Classification et calendrier de conservation | ❌ | — | Partie 5.4 |
| 9 | Plan de tests **et résultats** (procès-verbal) | ⚠️ | 15 tests décrits (guide partie 8) | Les faire, les dater, joindre des captures (partie 6.5) |
| 10 | Vérificateur de solution | ❌ | Vérificateur d'application : 0 erreur de formule | Lancer le Vérificateur de solution et joindre le rapport |
| 11 | Accessibilité | ⚠️ | 540 avertissements dans le Vérificateur d'application | Corriger les principaux ou documenter un plan (partie 6.8) |
| 12 | Soutien, responsables et continuité | ❌ | Liste Parametres › CourrielSoutien | Matrice RACI et propriétaire suppléant (partie 6.6) |
| 13 | Plan de déploiement et de retour arrière | ⚠️ | Guide parties 9.3 et 9.4 | Retour arrière et calendrier (partie 6.7) |
| 14 | Formation et communication aux utilisateurs | ❌ | — | **Guide d'utilisation** pour les employés et gestionnaires, et message d'annonce |
| 15 | Approbation du secteur d'affaires (RH) | ❌ | — | Signature de la direction responsable (partie 7) |
| 16 | Licences des utilisateurs | ✅ | Microsoft 365 suffit (connecteurs standard) | Confirmation des TI |
| 17 | Données de test supprimées avant la prod | ⚠️ | — | Les dossiers de test restent en dev : ne jamais copier de données |

**Ce qui bloquera presque sûrement l'autorisation s'il manque :** les n° 5, 7, 8, 9, 12, 14 et 15.

# 5. Les obligations légales à ne pas oublier

## 4.1 Protection des renseignements personnels (Loi 25)

La Ville est un **organisme public**. La *Loi sur l'accès aux documents des organismes publics et sur la protection des renseignements personnels* exige une **EFVP** pour tout projet d'acquisition, de développement ou de refonte d'un système d'information qui recueille, utilise, communique, conserve ou détruit des renseignements personnels.

L'appréciation de la contribution est exactement ce cas.

- **Qui :** le **responsable de l'accès aux documents et de la protection des renseignements personnels** de la Ville, avec le comité désigné s'il y en a un.
- **Quand :** **avant** la mise en production.
- **Ce que vous devez leur fournir :** les réponses de la partie 6.2 (données, finalités, accès, conservation, sécurité, hébergement). Vous avez déjà presque tout.

## 4.2 Conservation et destruction

Les appréciations sont des documents de **gestion des ressources humaines**. Leur durée de conservation est fixée par le **calendrier de conservation** de la Ville. Consultez la **gestion documentaire** (archives) pour savoir :

- combien de temps garder les dossiers (liste Appreciations) et les PDF (joints à chaque dossier) ;
- qui les détruit, et comment (manuellement ou par une étiquette de rétention Microsoft 365) ;
- si le PDF final doit être versé au **dossier de l'employé**.

# 6. Les documents à produire (contenu prérempli)

Complétez les passages *[entre crochets]*.

## 5.1 Fiche projet

| Rubrique | Contenu |
|---|---|
| Nom | Appréciation de la contribution |
| Secteur requérant | Service des ressources humaines — *[division]* |
| Responsable d'affaires | *[nom, titre]* |
| Responsable de la solution | Annie Audet, conseillère en ressources humaines (RH-SST) |
| Suppléant(e) | *[nom]* |
| Besoin | Remplacer le formulaire Word par un formulaire numérique, avec circuit d'avis, de certification et d'approbation (personne, supérieur immédiat, supérieur hiérarchique, directeur au besoin), puis transmission à la paie |
| Bénéfices | Suivi des étapes en temps réel, courriels automatiques, fin des échanges de fichiers par courriel, accès limité aux seules personnes concernées, PDF uniforme, transmission automatique à la paie |
| Utilisateurs | Cadres et professionnels non syndiqués évalués, et leurs gestionnaires : environ *[nombre]* personnes, environ *[nombre]* appréciations par année |
| Formulaires couverts | Version du 15 octobre 2026 : cadre avec équipe, cadre sans équipe, professionnel non syndiqué |
| Technologie | Power Apps (application canevas), SharePoint Online, Power Automate. Connecteurs standard seulement |
| Date visée | *[date]* (pré-prod), *[date]* (prod) |

## 5.2 Inventaire des renseignements personnels (pour l'EFVP)

| Question | Réponse |
|---|---|
| Quels renseignements ? | Nom, numéro d'employé, poste, type de poste, courriels de la personne et de ses gestionnaires, objectifs, cotes des postures ou compétences, commentaires, bilans, évaluation globale, dates des étapes |
| Sensibilité | **Élevée** : évaluation du rendement d'un employé |
| Finalité | Appréciation annuelle de la contribution et transmission de l'évaluation globale à la paie |
| Provenance | Saisis par la personne et ses gestionnaires. Nom, poste et gestionnaires sont lus dans l'annuaire Microsoft 365 |
| Où sont-ils stockés ? | SharePoint Online de la Ville (Microsoft 365, locataire de la Ville) : liste Appreciations (le PDF est joint à chaque dossier, avec les mêmes accès) |
| Qui y a accès ? | Voir la partie 6.3 |
| Communication | Courriel à la paie avec l'évaluation globale seulement (pas les commentaires) ; courriels d'avis aux personnes du dossier (sans contenu d'évaluation) |
| Fichiers temporaires | Le flux PDF crée un fichier .html dans le OneDrive du compte de service, puis le supprime aussitôt après la conversion |
| Conservation | *[selon le calendrier de conservation — partie 5.2]* |
| Destruction | *[procédure à définir avec la gestion documentaire]* |
| Journalisation | Historique des versions de la liste (qui a modifié quoi, et quand) ; journaux d'audit Microsoft 365 ; historique des exécutions des flux (28 jours) |
| Droits des personnes | La personne voit son dossier en tout temps et peut en produire le PDF |

## 5.3 Matrice des accès

| Qui | Liste Appreciations | Son propre dossier | Dossiers des autres | PDF joint au dossier |
|---|---|---|---|---|
| Personne évaluée | Peut créer | Modifier jusqu'à la certification, puis lecture | Aucun accès | Celui de son dossier |
| Supérieur(e) immédiat(e) / hiérarchique / directeur | Peut créer | Modifier selon l'étape, puis lecture à « Complété » | Seulement les dossiers où il ou elle est nommé(e) | Ceux de ses dossiers |
| RH – Appréciations | Lecture de tout | — | Lecture | Lecture |
| Propriétaires du site | Contrôle total | — | Contrôle total | Contrôle total |
| Compte de service | Propriétaire (exécution des flux) | — | — | — |
| Autres employés | Peut créer (Membres) | — | **Aucun** (retiré par le flux 1) | Aucun |

**Risques résiduels à déclarer** :

- **Délai d'application des droits.** Pendant les secondes entre la création d'un dossier et l'exécution du flux 1, le dossier a les droits de la liste. Ils sont limités aux Propriétaires, aux RH et à la Collaboration des Membres. *Atténuation :* le dossier ne contient alors que l'identification. Les autres employés ne le voient pas dans l'application, qui filtre par courriel.
- **Échec du flux 1.** Si le flux 1 échoue, un dossier peut garder les droits de la liste. *Atténuation :* surveillance de l'historique des exécutions et alerte d'échec envoyée au propriétaire. Il reste à activer la notification d'échec dans Power Automate.
- **Propriétaires du site.** Ils voient tout. *Atténuation :* limiter ce groupe aux administrateurs RH et TI autorisés.

## 5.4 Classification et conservation

| Élément | Proposition à valider |
|---|---|
| Classification | **Confidentiel** (le site affiche déjà « Confidentiel ») |
| Étiquette de sensibilité Microsoft 365 | *[celle exigée par les TI]* |
| Conservation de la liste | *[x ans après l'année de l'appréciation — calendrier de conservation]* |
| Conservation des PDF | *[idem, ou versement au dossier de l'employé]* |
| Versions | Historique des versions activé sur la liste |

## 5.5 Procès-verbal des tests

Reprenez les **15 tests** de la partie 8 du guide, et ajoutez pour chacun :

| N° | Date | Testeur | Résultat (réussi / échec) | Preuve (capture) | Commentaire |
|---|---|---|---|---|---|

Faites les tests **en pré-prod** avec au moins **4 comptes** : la personne, le SI, le SH, et un collègue sans lien. Joignez les captures.

**Il reste à tester au minimum :**

- le circuit complet jusqu'à « Complété » (courriel paie, lecture seule, date paie) ;
- le cas avec directeur ;
- le PDF ;
- l'accès refusé à un collègue.

## 5.6 Soutien et exploitation (RACI)

R = réalise, A = approuve, C = consulté, I = informé.

| Activité | RH (Annie) | Suppléant(e) RH | TI | Direction RH |
|---|---|---|---|---|
| Questions des utilisateurs (CourrielSoutien) | R | R | I | — |
| Surveiller les échecs des flux | R | R | C | — |
| Modifications de l'application | R | C | A (import) | A |
| Import pré-prod et prod, connexions | C | — | R | I |
| Compte de service (licence, mot de passe) | I | — | R | — |
| Mise à jour annuelle des formulaires | R | C | A (import) | A |
| Conservation et destruction | C | — | C | A |

**À demander aux TI :**

- un **compte de service** avec une licence Microsoft 365 incluant Power Automate (usage standard) et une boîte aux lettres pour envoyer les courriels ;
- l'ajout de ce compte comme **propriétaire** du site et **copropriétaire** des 3 flux ;
- un **propriétaire suppléant** de la solution, pour éviter qu'elle dépende d'une seule personne.

## 5.7 Plan de déploiement et de retour arrière

| Étape | Qui | Quand |
|---|---|---|
| 1. Remise du .zip, du fichier Excel et du dossier | Annie | *[date]* |
| 2. Création du site et des listes de pré-prod | TI | *[date]* |
| 3. Import en pré-prod, connexions, variables | TI | *[date]* |
| 4. Tests en pré-prod et procès-verbal | Annie + testeurs | *[date]* |
| 5. Autorisation de mise en production | TI + direction RH | *[date]* |
| 6. Import en prod | TI | *[date]* |
| 7. Annonce et formation | RH | *[date]* |

**Retour arrière :** si un problème bloquant survient en production, il y a trois niveaux.

1. **Désactiver les 3 flux.**
2. **Retirer le partage** de l'application.
3. **Revenir au formulaire Word**, qui reste disponible.

Les données déjà saisies restent dans la liste SharePoint, sans perte. Une version corrigée se réimporte en *Mise à niveau*.

## 5.8 Accessibilité

Le Vérificateur d'application signale 540 avertissements d'accessibilité, surtout des étiquettes accessibles (AccessibleLabel) manquantes. **Proposition à présenter aux TI :**

- corriger avant la prod les contrôles de saisie (champs, cases, boutons) en remplissant leur propriété **AccessibleLabel** ;
- documenter le reste dans un plan de correction ;
- noter que le **PDF** et le formulaire Word restent disponibles comme solutions de rechange.

# 7. Les pièces à joindre à la demande

| N° | Pièce | État |
|---|---|---|
| 1 | Formulaire « Demande de mise en PréProd/Prod Power Apps » | ✅ réponses prêtes (partie 1) |
| 2 | Solution gérée `.zip` (version 1.0.0.x) | à exporter (guide 9.1 et 9.2) |
| 3 | `Variables-environnement-et-deploiement.xlsx` | ✅ (colonnes pré-prod et prod à compléter) |
| 4 | `GUIDE-MISE-EN-PRODUCTION.docx` et `Schema-solution.jpg` | ✅ |
| 5 | Étape 3 du Guide complet (35 colonnes de la liste) | ✅ |
| 6 | Rapport du **Vérificateur de solution** | ❌ |
| 7 | **EFVP** signée par le responsable de la PRP | ❌ |
| 8 | Avis de la **gestion documentaire** (conservation) | ❌ |
| 9 | **Procès-verbal des tests** avec captures | ❌ |
| 10 | Matrice RACI et nom du suppléant | ❌ (partie 6.6) |
| 11 | **Guide d'utilisation** pour les employés et gestionnaires, et message d'annonce | ❌ |
| 12 | Approbation de la **direction RH** | ❌ |

**Signature du secteur d'affaires**

Nom : ______________________ Titre : ______________________ Date : __________ Signature : ______________________
