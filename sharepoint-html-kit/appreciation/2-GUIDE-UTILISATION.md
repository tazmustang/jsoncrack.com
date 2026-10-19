# Guide d'utilisation — Appréciation de la contribution

Pour les personnes en appréciation et les gestionnaires. Version 3.7, formulaires du 15 octobre 2026.

---

## 1. Ouvrir l'application

1. Ouvrez la bibliothèque SharePoint « Appréciation de la contribution des cadres ».
2. Cliquez sur le fichier `appreciation-cadres-v3.7.html`, puis sur **⤓ Télécharger** (en haut à gauche).
3. Ouvrez le fichier téléchargé (double-clic) : il s'ouvre dans Edge.

> Ne travaillez pas dans l'aperçu SharePoint : rien ne peut y être enregistré ni téléchargé. L'application vous le rappelle dans un bandeau.

**Première ouverture :** créez un mot de passe d'au moins 4 caractères. Il protège votre brouillon sur ce poste. Il n'est jamais envoyé, ni à SharePoint ni ailleurs. Aux ouvertures suivantes, entrez-le pour retrouver votre brouillon.

## 2. Commencer : deux choix

**1. Qui êtes-vous ?** Cochez votre rôle dans cette appréciation :

| Rôle | Ce que vous faites |
|---|---|
| Personne en appréciation | Vous remplissez votre partie, votre autoévaluation et votre bilan (section F), puis vous certifiez |
| Supérieur(e) immédiat(e) | Vous remplissez vos observations, le bilan annuel (section E) et l'évaluation globale, puis vous approuvez en premier |
| Supérieur(e) hiérarchique | Vous prenez connaissance du dossier et vous approuvez |
| Directeur / directrice | Vous approuvez en dernier, si votre approbation est requise |

**2. Type de poste — seulement pour la personne en appréciation.** C'est elle qui choisit son formulaire : cadre avec équipe, cadre sans équipe ou professionnel non syndiqué.

**Gestionnaires** (supérieur immédiat, hiérarchique, directeur) : vous ne choisissez pas le type de poste. L'application vous demande d'ouvrir le dossier de la personne :
1. **📂 Ouvrir « Mes dossiers »** et téléchargez son dossier ;
2. **📁 Charger un dossier** et choisissez ce fichier.

Le formulaire s'ouvre alors avec le type de poste qu'elle a choisi.

Une fois faits, les choix se verrouillent et restent gardés jusqu'à **« 🗑️ Nouveau formulaire »**. En cas d'erreur, utilisez le lien « 🔓 Changer de rôle » ou, pour la personne en appréciation, « 🔓 Changer de type de poste », dans la barre de gauche.

**Vous ne voyez que ce qui vous concerne.** Les sections réservées à un autre rôle restent cachées **tant qu'elles sont vides**. Dès qu'elles sont remplies, elles apparaissent en lecture seule. Par exemple, la personne en appréciation voit le bilan du supérieur avant de certifier.

## 3. Remplir

- **Introduction et identification** : nom, ID, poste et type de rencontre.
- **Section A** : objectifs de l'année en cours (objectif, indicateurs de mesure, actions réalisées / commentaires) et objectifs de l'année à venir.
- **Section B** :
  - cadres : postures de leadership, cotées sur l'échelle de 5 niveaux affichée dans la section ;
  - professionnels : exemples d'application pour chaque compétence.
- **Section C** : cochez les thèmes ayant fait l'objet d'actions ou d'efforts particuliers, puis donnez des exemples.
- **Section D** : résultats des actions de développement passées et nouveaux besoins.
- **Sections E, F et évaluation globale** : selon votre rôle.

Le bouton **❓ Comment remplir** (en haut à gauche, et en haut du formulaire) résume tout cela en 2 minutes.

## 4. Enregistrer votre travail

| Bouton | Ce qu'il fait |
|---|---|
| (automatique) | Le brouillon est sauvegardé, protégé par votre mot de passe, sur ce poste |
| **💾 Copie locale** | Télécharge une copie `.json` de votre travail. Faites-le avant de changer d'ordinateur |
| **📁 Charger un dossier** | Rouvre une copie `.json` ou un dossier officiel téléchargé depuis « Mes dossiers » |
| **↶ Annuler / ↷ Refaire** | Annule ou rétablit la dernière modification |

## 5. Déposer sur SharePoint (sauvegarder, aviser, certifier, approuver)

1. Cliquez sur le bouton de dépôt de votre étape (« ☁️ Déposer sur SharePoint », « 📨 Aviser le supérieur immédiat », « ✔ Certifier et soumettre », « Approuver — déposer sur SharePoint »). Un fichier `depot-….json` est téléchargé.
2. Cliquez sur **Ouvrir le formulaire de dépôt** : SharePoint s'ouvre avec votre compte de la Ville.
3. Cliquez sur **Ajouter des pièces jointes**, choisissez le fichier `depot-….json` le plus récent, puis **Enregistrer**.
4. Vous recevrez un courriel de confirmation ou de refus (avec la raison).
5. Pour continuer, rechargez la version officielle depuis **📂 Mes dossiers**, puis supprimez le fichier `depot-….json` de vos Téléchargements.

> Le traitement automatique des dépôts (courriels, dossier officiel) sera actif dès que le flux Power Automate sera en place. D'ici là, le dépôt est enregistré dans la liste, sans autre effet.

## 6. Le cheminement

**Brouillon → Certifié (personne en appréciation) → Approuvé (supérieur immédiat) → Approuvé (supérieur hiérarchique) → Approuvé (directeur, si requis) → Approbation finale → Archivé.**

La barre d'étapes, en haut du formulaire, montre où en est le dossier. Après la certification, le contenu se verrouille. Seul le supérieur immédiat peut encore compléter ses cotes, la section E et l'évaluation globale, jusqu'à son approbation. Le numéro de dossier apparaît dès que SharePoint a traité le premier dépôt.

## 7. Questions fréquentes

| Question | Réponse |
|---|---|
| Rien n'est téléchargé quand je clique sur « Copie locale » | Vous êtes dans l'aperçu SharePoint. Téléchargez le fichier (⤓) et ouvrez-le sur votre poste. Une fenêtre « Copier le contenu » vous permet de ne rien perdre en attendant |
| J'ai oublié mon mot de passe | Sur l'écran du mot de passe, cliquez sur « Mot de passe oublié ? Recommencer à neuf ». Le brouillon de ce poste est effacé ; rechargez votre dernière copie `.json` ou votre dossier depuis « Mes dossiers » |
| Je me suis trompé de rôle ou de type de poste | Utilisez « 🔓 Changer de rôle » ou « 🔓 Changer de type de poste » (personne en appréciation seulement), dans la barre de gauche |
| Je suis gestionnaire et je ne peux pas choisir le type de poste | C'est normal : ouvrez le dossier de la personne avec « 📂 Mes dossiers », puis « 📁 Charger un dossier » |
| Je ne vois pas la section E (ou F) | Elle est réservée à un autre rôle et reste cachée tant qu'elle est vide |
| Mon dépôt a été refusé | Le courriel en donne la raison (par exemple : ce n'est pas votre étape). Rechargez la dernière version depuis « Mes dossiers » et recommencez |
| Que faire des fichiers `depot-….json` ? | Supprimez-les une fois le dépôt confirmé : ils contiennent les données de l'appréciation |

Besoin d'aide ? Dans l'onglet **❓ Comment remplir**, utilisez « ✉️ Envoyer » pour écrire à l'équipe.
