# Version 3.4 — la façon de travailler

Fichier : `appreciation-cadres-v3.4.html` (remplacé depuis par la v3.5 ; remplaçait la v3.3, mêmes formulaires et mêmes adresses).

## Ce qu'on a constaté le 19 octobre 2026
- Ouvert depuis la bibliothèque, le fichier **s'affiche** dans l'aperçu SharePoint. ✅
- Le formulaire de dépôt **Depot_Appreciations** s'ouvre bien, avec « Ajouter des pièces jointes ». ✅
- **💾 Copie locale ne télécharge rien.** L'aperçu SharePoint bloque les téléchargements sans aucun message d'erreur. C'est une règle de Microsoft, pas un défaut du fichier. Le bouton « ☁️ Déposer sur SharePoint » est touché de la même façon, puisqu'il doit lui aussi télécharger un fichier.

## La règle simple
**L'aperçu SharePoint sert à trouver l'application. Le travail se fait dans le fichier ouvert sur le poste.**

1. Dans la bibliothèque, ouvrez `appreciation-cadres-v3.4.html`.
2. Dans la barre SharePoint en haut à gauche, cliquez sur **⤓ Télécharger**.
3. Ouvrez le fichier téléchargé (double-clic : il s'ouvre dans Edge).
4. Là, **tout fonctionne** : mot de passe et brouillon protégé, 💾 Copie locale, ☁️ Déposer sur SharePoint, 🖨️ Aperçu PDF.

Astuce : gardez le fichier téléchargé sur votre Bureau ou dans OneDrive. Retéléchargez-le seulement quand on vous annonce une nouvelle version.

## Ce que fait la v3.4 dans l'aperçu SharePoint
- Le bandeau du haut le dit clairement : « rien ne peut y être enregistré ni téléchargé : cliquez sur ⤓ Télécharger ».
- Si quelqu'un clique quand même sur 💾 Copie locale ou ☁️ Déposer, une fenêtre **« Copier le contenu »** s'ouvre. Elle permet de ne rien perdre : copier, coller dans le Bloc-notes, enregistrer sous le nom indiqué. C'est un dépannage ; la règle simple reste la bonne façon de faire.

Testé le 19 octobre 2026 en navigateur automatisé, sans erreur :
- aperçu isolé sans téléchargement (la situation SharePoint) ;
- aperçu avec téléchargement ;
- fichier ouvert sur le poste ;
- les trois formulaires.
