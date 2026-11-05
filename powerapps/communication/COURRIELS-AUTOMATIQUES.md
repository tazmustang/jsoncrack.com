---
title: "Les courriels automatiques de l'application"
subtitle: "Appréciation de la contribution (SRHVQ) · Ordre, destinataires et textes · 3 novembre 2026"
lang: fr-CA
---

# En bref

L'application envoie **6 courriels automatiques** au fil du circuit (flux « Appréciation – Suivi des étapes »), plus 2 courriels de soutien. **Aucun courriel ne contient l'évaluation**, sauf celui destiné aux RH à la toute fin (évaluation globale seulement). Chaque courriel contient un **lien qui ouvre directement le dossier** dans l'application.

| Ordre | Déclencheur (quand) | Destinataire | Objet |
|---|---|---|---|
| 1 | La personne clique sur **Aviser** | Supérieur(e) immédiat(e) | Appréciation de [Nom] : prête pour votre consultation |
| 2 | La personne clique sur **Approuver et soumettre** | Supérieur(e) immédiat(e) | À approuver : appréciation de [Nom] |
| 3 | Le SI clique sur **Approuver** | Supérieur(e) hiérarchique | À approuver : appréciation de [Nom] |
| 4 | Le SH clique sur **Approuver** (*seulement si un directeur de service est requis*) | Directeur / directrice de service | À approuver : appréciation de [Nom] |
| 5 | Dossier **Complété** | RH (adresse de la variable SRHVQ_CourrielPaie) | Évaluation globale – [Nom] ([ID]) – [Année] |
| 6 | Dossier **Complété** | Personne, SI et SH | Appréciation complétée – [Nom] |

Sans directeur de service requis, l'approbation du SH fait passer le dossier directement à **Complété** : le courriel 4 n'est pas envoyé.

> **Ajout d'un directeur de service :** quand un directeur de service est choisi dans la section G, il reçoit l'**accès** au dossier tout de suite, mais **pas de courriel**. Il est avisé seulement à son tour (courriel 4).

# Le texte de chaque courriel

## 1. Prête pour votre consultation

- **Quand :** la personne en appréciation clique sur **Aviser** (statut « Avisé au supérieur »).
- **À :** supérieur(e) immédiat(e).
- **Objet :** Appréciation de [Nom] : prête pour votre consultation

> Bonjour,
>
> [Nom] a rempli sa partie du formulaire d'appréciation de la contribution. Vous pouvez la consulter et planifier la rencontre.
>
> **Ouvrir le dossier** (lien)

## 2. À approuver (supérieur immédiat)

- **Quand :** la personne clique sur **Approuver et soumettre** (statut « Confirmé »). Son contenu est alors verrouillé.
- **À :** supérieur(e) immédiat(e).
- **Objet :** À approuver : appréciation de [Nom]

> Bonjour,
>
> [Nom] a confirmé son formulaire. C'est maintenant votre étape : complétez au besoin le bilan annuel (section E) et l'évaluation globale, puis approuvez.
>
> **Ouvrir le dossier** (lien)

## 3. À approuver (supérieur hiérarchique)

- **Quand :** le SI clique sur **Approuver** (statut « Approuvé SI »).
- **À :** supérieur(e) hiérarchique.
- **Objet :** À approuver : appréciation de [Nom]

> Bonjour,
>
> Le ou la supérieur(e) immédiat(e) a approuvé le dossier de [Nom]. C'est maintenant votre étape.
>
> **Ouvrir le dossier** (lien)

## 4. À approuver (directeur ou directrice de service)

- **Quand :** le SH clique sur **Approuver**, et l'approbation d'un directeur de service est requise (statut « Approuvé SH »).
- **À :** directeur ou directrice de service choisi(e) dans la section G.
- **Objet :** À approuver : appréciation de [Nom]

> Bonjour,
>
> Le dossier de [Nom] attend votre approbation (directeur ou directrice de service).
>
> **Ouvrir le dossier** (lien)

## 5. Évaluation globale transmise aux RH

- **Quand :** le dossier passe à **Complété**.
- **À :** l'adresse inscrite dans la variable **SRHVQ_CourrielPaie** (RH / paie). En PréProd : votre adresse, pour les tests.
- **Objet :** Évaluation globale – [Nom] ([ID]) – [Année]
- **Contenu :** un tableau, **sans aucun commentaire ni cote** :

| | |
|---|---|
| Nom, prénom | [Nom] |
| ID | [ID] |
| Poste | [Poste] |
| Type de poste | [Type de poste] |
| Année | [Année] |
| **Évaluation globale** | **[Évaluation globale]** |
| Supérieur(e) immédiat(e) | [Nom du SI] |

## 6. Appréciation complétée

- **Quand :** le dossier passe à **Complété**, juste après le courriel 5.
- **À :** la personne, le SI et le SH (*le directeur de service n'est pas inclus*).
- **Objet :** Appréciation complétée – [Nom]

> Toutes les étapes d'approbation sont complétées. Le dossier est archivé en lecture seule.
>
> **Consulter le dossier** (lien)

Ensuite, automatiquement : toutes les personnes du dossier passent en **lecture seule**, et la date « Transmis aux RH » est inscrite.

# Les courriels de soutien

| Courriel | Quand | À | Contenu |
|---|---|---|---|
| **Demande de soutien** | Un utilisateur écrit au soutien depuis l'écran **À propos** | Adresse du soutien (liste Parametres, CourrielSoutien) | Le message, le nom et le courriel de la personne, l'environnement et le no de dossier ouvert |
| **Échec d'un flux** | Un des 3 flux échoue (gestion des erreurs, version 1.0.0.4) | Variable SRHVQ_CourrielSoutien | Le nom du flux, l'environnement, la date et un lien vers l'exécution en erreur |

# Points à valider

| ✔ | Question | Réponse |
|---|---|---|
| ☐ | Les textes conviennent-ils (ton, vouvoiement, signature) ? | |
| ☐ | Faut-il ajouter une signature (ex. « Ressources humaines — Ville de Québec ») ? | |
| ☐ | Le directeur de service doit-il recevoir le courriel 6 (« Appréciation complétée ») ? | |
| ☐ | L'adresse RH / paie de Prod pour le courriel 5 (variable SRHVQ_CourrielPaie) | |
| ☐ | L'expéditeur : en PréProd et en Prod, les courriels partent de la boîte du **compte de service** (connexion Outlook des TI). Son nom affiché convient-il ? | |

Les textes se modifient dans le flux « Appréciation – Suivi des étapes » (voir FLUX-FINAUX.txt, flux 2).
