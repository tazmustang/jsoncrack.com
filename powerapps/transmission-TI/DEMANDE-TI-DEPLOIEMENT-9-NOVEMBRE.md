---
title: "Demande aux TI — Déploiement de l'application « Appréciation de la contribution »"
subtitle: "VERSION FINALE — 29 octobre 2026 · Lancement visé auprès des gestionnaires : lundi 9 novembre 2026"
lang: fr-CA
---

# 1. En une page

| | |
|---|---|
| **Demandeuse** | Annie Audet, conseillère en ressources humaines, Division de la santé et de la sécurité au travail (RH-SST) |
| **Outil** | Application Power Apps « Appréciation de la contribution », qui remplace le formulaire Word |
| **Utilisateurs** | **Plus de 500 personnes** : cadres, professionnels non syndiqués et leurs gestionnaires |
| **Technologies** | Power Apps (canevas), SharePoint Online, Power Automate. **Connecteurs standard seulement, aucune licence Premium** |
| **Date visée** | **Lundi 9 novembre 2026** : ouverture aux gestionnaires |
| **Ce que nous demandons** | **1)** la mise en PréProd puis en Prod ; **2)** une **revue de l'application** par les TI ; **3)** la **validation des groupes de sécurité** ; **4)** vos **recommandations** pour un outil utilisé à grande échelle |

L'application a été construite et testée dans un bac à sable. Toutes les étapes du circuit fonctionnent : création, avis, certification, approbations, transmission aux RH, lecture seule et PDF. Avant de l'ouvrir à plus de 500 personnes, nous voulons l'**œil des TI** : s'assurer que tout est conforme, sécuritaire et maintenable.

# 2. Ce que nous demandons

## 2.1 Mise en PréProd, puis en Prod

Les étapes techniques sont détaillées dans le **GUIDE-MISE-EN-PRODUCTION.docx** (partie 9) et dans l'onglet **Checklist TI** du fichier Excel :

1. Créer le site SharePoint et les listes (*Appreciations*, *Parametres*), le groupe *RH – Appréciations* et les autorisations.
2. Importer la solution gérée *Solution-ApplicationAppreciation* (version 1.0.0.3).
3. Choisir les connexions d'un **compte de service** pour les 4 références de connexion.
4. Saisir les 5 variables d'environnement, puis activer les 3 flux.
5. Partager l'application.
6. Répéter en Prod une fois la PréProd validée.

## 2.2 Une revue de l'application par les TI

Nous aimerions qu'une personne des TI **fasse le tour de l'application** en PréProd et nous donne son avis. Prévoir **1 à 2 heures**. Nous proposons une rencontre Teams de 45 minutes pour la démonstration, puis une exploration libre.

| À revoir | Questions pour les TI |
|---|---|
| **L'application** (2 écrans) | Les formules sont-elles conformes à vos normes ? Y a-t-il des avertissements dans le Vérificateur d'application ou des problèmes de performance ? |
| **Les 3 flux** | Gestion des erreurs, comptes utilisés, nombre d'exécutions prévu : est-ce acceptable ? |
| **SharePoint** | Structure de la liste, index, permissions uniques par dossier : est-ce adapté au volume ? |
| **Le PDF** | Le fichier temporaire passe par le OneDrive du compte de service, puis est supprimé : est-ce acceptable ? |
| **Les courriels** | Expéditeur, contenu (aucune donnée d'évaluation, seulement un lien), boîte de la paie |
| **La solution** | Variables d'environnement, références de connexion, gestion des versions : est-ce conforme à vos pratiques ? |

## 2.3 La validation des groupes de sécurité

C'est le point le plus important pour nous. Chaque dossier contient une **évaluation du rendement**, dont la sensibilité est **élevée**.

| Groupe ou accès | Rôle | Ce que nous demandons |
|---|---|---|
| **Groupe de sécurité de l'environnement** (Entra ID) | Qui peut ouvrir l'application | Quel groupe utiliser pour plus de 500 personnes ? Un groupe dynamique existant (cadres et professionnels) est-il possible ? |
| **Partage de l'application** | Qui la voit dans Power Apps | Le même groupe ? |
| **Membres du site SharePoint** (Collaboration sur la liste) | Pouvoir créer son dossier | Peut-on y mettre le même groupe Entra ID, plutôt que 500 noms ? |
| **Permissions par dossier** (flux 1) | Seuls la personne, ses supérieurs, le directeur et les RH voient le dossier | Valider la méthode : héritage arrêté sur chaque élément par le compte de service |
| **RH – Appréciations** (Lecture) | Équipe RH autorisée | Valider la liste des membres |
| **Propriétaires du site** | Compte de service et administrateurs | Qui doit y être, au minimum ? |
| **Compte de service** | Exécute les flux, propriétaire du site | Lequel utiliser ? Qui le gère ? |

**Test de confidentialité à faire ensemble en PréProd :** une personne sans lien avec un dossier ne doit **ni le voir dans l'application, ni l'ouvrir par un lien direct SharePoint, ni ouvrir son PDF**.

## 2.4 Vos recommandations pour plus de 500 utilisateurs

Nous voulons votre avis sur ces points :

1. **Volume SharePoint.** Environ 500 dossiers par année, chacun avec des **permissions uniques** et un PDF joint. Microsoft recommande de rester sous environ 5 000 éléments à permissions uniques par liste. Faut-il prévoir une **liste par année** ou un archivage annuel ?
2. **Seuil d'affichage de 5 000 éléments.** Les filtres de « Mes dossiers » utilisent des colonnes indexées (Annee, Statut, courriels). Est-ce suffisant ?
3. **Limites Power Automate.** Les flux du compte de service s'exécutent à chaque création et modification de dossier, et à chaque PDF produit. Le volume est-il acceptable ? Des pointes sont possibles en période d'appréciation.
4. **Surveillance.** Qui reçoit les alertes si un flux échoue ? Pouvez-vous recommander un mécanisme simple ?
5. **Soutien.** Le premier niveau (questions d'utilisation) est assuré par les RH. Qui assure le soutien technique ?
6. **Continuité.** Copropriétaires de l'application et des flux, sauvegarde, procédure de mise à jour (bac à sable › PréProd › Prod).

# 3. Échéancier proposé pour le 9 novembre

| Date | Étape | Qui |
|---|---|---|
| **29 et 30 oct.** | Corrections finales dans le bac à sable (type de rencontre, échelle à 4 niveaux) ; export de la solution 1.0.0.3 | Annie |
| **Ven. 30 oct.** | Envoi de la demande et du paquet de transmission | Annie |
| **Lun. 2 nov.** | Création du site PréProd et import de la solution ; ajout des testeurs | TI |
| **Mar. 3 nov.** | **Rencontre de revue** : démonstration, sécurité, questions | TI + Annie |
| **3 au 5 nov.** | Tests en PréProd (15 tests du guide, test de confidentialité) ; revue libre par les TI | Équipe RH + TI |
| **Jeu. 5 nov.** | Recommandations des TI ; corrections s'il y a lieu ; **décision go / no go** | TI + Annie + gestionnaire |
| **Ven. 6 nov.** | Import en Prod, groupes de sécurité de Prod, test rapide en Prod | TI + Annie |
| **Lun. 9 nov.** | **Lancement auprès des gestionnaires** (annonce, guide d'utilisation) | Annie |

**Si l'échéancier ne peut être tenu**, nous proposons :

- un **lancement pilote le 9 novembre** auprès d'un groupe restreint de gestionnaires ;
- puis l'**ouverture à tous** dès la fin des validations.

**Points qui pourraient retarder la date** (en cours de notre côté) :

- l'évaluation des facteurs relatifs à la vie privée (EFVP) ;
- la durée de conservation des dossiers.

Dites-nous s'ils sont **obligatoires avant la Prod** ou s'ils peuvent être complétés en parallèle.

# 4. Votre rétroaction

Merci de nous retourner ce tableau (ou de nous écrire) au plus tard le **jeudi 5 novembre**.

| Sujet | Conforme ? | Recommandation ou correction demandée | Bloquant pour le 9 nov. ? |
|---|---|---|---|
| Application (formules, performance) | ☐ Oui ☐ Non | | ☐ Oui ☐ Non |
| Flux Power Automate | ☐ Oui ☐ Non | | ☐ Oui ☐ Non |
| Structure SharePoint et volume | ☐ Oui ☐ Non | | ☐ Oui ☐ Non |
| Groupes de sécurité et permissions | ☐ Oui ☐ Non | | ☐ Oui ☐ Non |
| Compte de service et connexions | ☐ Oui ☐ Non | | ☐ Oui ☐ Non |
| Courriels et données transmises | ☐ Oui ☐ Non | | ☐ Oui ☐ Non |
| Surveillance, soutien et continuité | ☐ Oui ☐ Non | | ☐ Oui ☐ Non |
| Autre | | | |

**Nom de la personne des TI :** ______________________  **Date :** ______________

# 5. Documents joints (Transmission-TI-PreProd-Appreciation.zip)

| Fichier | Contenu |
|---|---|
| DEMANDE-TI-DEPLOIEMENT-9-NOVEMBRE.docx | Ce document |
| BORDEREAU-TRANSMISSION-TI.docx | Contenu du paquet et marche à suivre |
| Solution-ApplicationAppreciation_1_0_0_3_managed.zip | Solution gérée à importer |
| DOSSIER-AUTORISATION-TI.docx | Réponses au formulaire, renseignements personnels, matrice des accès |
| GUIDE-MISE-EN-PRODUCTION.docx | Guide technique complet |
| Variables-environnement-et-deploiement.xlsx | Variables, SharePoint, composants, checklist TI, testeurs |
| FLUX-FINAUX.txt | Les 3 flux, action par action |
| Schema-solution.jpg | Schéma d'ensemble |

Merci de votre collaboration. Votre apport est essentiel pour que cet outil soit fiable pour plus de 500 personnes dès son lancement.

**Annie Audet**
Conseillère en ressources humaines (RH-SST), Ville de Québec
