---
title: "Appréciation de la contribution — Transmission aux TI pour la PréProd"
subtitle: "VERSION FINALE — 29 octobre 2026 · Bordereau de transmission"
lang: fr-CA
---

# 1. Ce qu'Annie fait avant d'envoyer (dans l'ordre)

| ✔ | Action | Où |
|---|---|---|
| ☐ | Faire la **correction du type de rencontre**, puis la tester | CORRECTION-TYPE-RENCONTRE.docx |
| ☐ | Refaire rapidement les tests 2, 5 et 14 du guide | GUIDE-MISE-EN-PRODUCTION.docx, partie 8 |
| ☐ | Inscrire les **testeurs** (nom et courriel) | Excel, onglet **Testeurs PréProd** |
| ☐ | Dans DOSSIER-AUTORISATION-TI, remplacer *[noms des collègues]* et *[groupe de gestionnaires]* | DOSSIER-AUTORISATION-TI.docx |
| ☐ | **Préparer et exporter la solution** en **gérée**, version **1.0.0.2** | Guide, parties 9.1 et 9.2 |
| ☐ | Ajouter le .zip de la solution au ZIP de transmission (voir partie 3) | — |
| ☐ | Remplir le formulaire des TI et envoyer le courriel de la partie 4 | — |

# 2. Le contenu du ZIP « Transmission-TI-PreProd.zip »

| N° | Fichier | À quoi il sert |
|---|---|---|
| 1 | **Solution-ApplicationAppreciation_1_0_0_2_managed.zip** | La solution à importer. **À ajouter par Annie** (partie 3) |
| 2 | **DEMANDE-TI-DEPLOIEMENT-9-NOVEMBRE.docx** | **La demande : PréProd et Prod, revue de l'application, groupes de sécurité, recommandations, échéancier du 9 novembre** |
| 3 | BORDEREAU-TRANSMISSION-TI.docx | Ce document |
| 4 | DOSSIER-AUTORISATION-TI.docx | Réponses au formulaire des TI : texte « Commentaires », testeurs, renseignements personnels |
| 5 | GUIDE-MISE-EN-PRODUCTION.docx | Guide technique : SharePoint (partie 4), flux (partie 6), tests (partie 8), remise (partie 9) |
| 6 | Variables-environnement-et-deploiement.xlsx | Variables, SharePoint, composants, checklist TI, testeurs |
| 7 | FLUX-FINAUX.txt | Les 3 flux, action par action |
| 8 | Schema-solution.jpg | Schéma d'ensemble |

**Ce qui n'est PAS dans le ZIP** (inutile pour les TI) : les fichiers de formules (.txt), le guide d'utilisation, le message d'annonce, la présentation et les schémas opérationnels. Les formules sont déjà dans la solution.

# 3. Ajouter la solution au ZIP (5 minutes)

1. Téléchargez **Transmission-TI-PreProd.zip** et le **.zip de la solution** exporté de Power Apps.
2. Dans l'Explorateur de fichiers, faites un **clic droit** sur Transmission-TI-PreProd.zip › **Extraire tout** › **Extraire**.
3. **Glissez** le .zip de la solution dans le dossier extrait. **Ne l'ouvrez pas et ne le décompressez pas** : les TI l'importent tel quel.
4. Sélectionnez tous les fichiers du dossier (**Ctrl + A**), puis **clic droit › Compresser dans un fichier ZIP**.
5. Renommez le nouveau ZIP : **Transmission-TI-PreProd-Appreciation.zip**.

> 💡 Si le ZIP est trop lourd pour un courriel, déposez-le dans votre OneDrive et envoyez un **lien de partage** limité aux personnes des TI.

# 4. Le courriel aux TI

**Objet :** Demande de déploiement pour le 9 novembre — application Appréciation de la contribution (RH-SST)

> Bonjour,
>
> Je vous transmets la demande de déploiement de la solution **Solution-ApplicationAppreciation** (version 1.0.0.2, gérée). Elle remplace le formulaire Word d'appréciation de la contribution par une application Power Apps qui sera utilisée par **plus de 500 personnes**. Nous visons un lancement auprès des gestionnaires le **lundi 9 novembre**.
>
> En plus de la mise en PréProd puis en Prod, nous aimerions que votre équipe **fasse le tour de l'application**, **valide les groupes de sécurité** et nous fasse part de ses **recommandations**. Tout est expliqué dans le document **DEMANDE-TI-DEPLOIEMENT-9-NOVEMBRE.docx**, avec l'échéancier proposé et une grille de rétroaction. Je propose une rencontre de revue le **mardi 3 novembre**.
>
> Vous trouverez dans le fichier joint **Transmission-TI-PreProd-Appreciation.zip** :
> - la demande et l'échéancier ;
> - la solution gérée à importer ;
> - le dossier d'autorisation (réponses au formulaire) ;
> - le guide de mise en production ;
> - le fichier Excel des variables d'environnement, de la structure SharePoint et de la liste de vérification ;
> - le détail des 3 flux et le schéma de la solution.
>
> Points importants :
> - **Connecteurs standard seulement**, aucune licence Premium.
> - Les listes SharePoint peuvent être recréées avec « **À partir d'une liste existante** » (listes du bac à sable), puis les réglages de l'onglet SharePoint du fichier Excel.
> - Merci d'utiliser un **compte de service** pour les 4 références de connexion.
> - Merci d'ajouter les **testeurs** (onglet « Testeurs PréProd ») au groupe de sécurité de l'environnement PréProd et au groupe Membres du site. Actuellement, ils reçoivent le message « You are not a member of the environment's security group ».
>
> Je suis disponible pour une rencontre si cela facilite l'import.
>
> Merci beaucoup !
>
> Annie Audet
> Conseillère en ressources humaines (RH-SST)

# 5. Ce que les TI feront

Voir l'onglet **Checklist TI** du fichier Excel :

1. Créer les listes à partir des listes existantes, puis appliquer les réglages.
2. Remplir la liste Parametres (Environnement = PRE-PROD).
3. Importer la solution gérée.
4. Choisir les connexions du compte de service.
5. Saisir les variables, puis le lien de l'application.
6. Activer les 3 flux.
7. Ajouter les testeurs au groupe de sécurité et au site.
8. Vous transmettre le **lien PréProd**.

**Ensuite :** envoyez à votre équipe le courriel de tests (dossier tests-equipe), avec le **lien PréProd**.

# 6. Personne-ressource

Annie Audet — Conseillère en ressources humaines, Division de la santé et de la sécurité au travail.
