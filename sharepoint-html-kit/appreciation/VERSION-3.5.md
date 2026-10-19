# Version 3.5 — affichage allégé

Fichier : `appreciation-cadres-v3.5.html` (remplace la v3.4 ; mêmes formulaires et mêmes adresses).

## Ce qui change

| Demande | Ce que fait la v3.5 |
|---|---|
| Pas de numéro de dossier sur un formulaire neuf | Le numéro n'apparaît qu'une fois le dossier connu de SharePoint (après un premier dépôt traité) |
| Fusionner l'aide-mémoire et « Comment remplir » et les mettre en évidence | Un seul onglet **❓ Comment remplir**. On y accède par le bouton doré en tête de la barre de gauche et par l'encadré « 👋 Première fois ? » en haut du formulaire. La section « Pour commencer » ajoute 3 étapes : ouvrir sur le poste, type de poste, qui vous êtes |
| Retirer le rappel de l'échelle de l'aide | Retiré : l'échelle reste dans la section B du formulaire |
| Cocher qui l'on est et ne voir que ce qui nous concerne | Après le type de poste, un écran **« Qui êtes-vous ? »** propose 4 choix. Le choix se verrouille (« 🔓 Changer de rôle » au besoin) et reste gardé jusqu'à **Nouveau formulaire** |
| Bouton Configuration | Retiré : les adresses sont inscrites dans le fichier |
| La version seulement au bas de la page | Retirée de l'en-tête, des pastilles, des cartes de choix et de la synthèse. Elle reste au pied de page (« Formulaire : … — Version du 15 octobre 2026 ») et au bas du PDF |

## Ce que voit chaque rôle

Règle simple : **les sections réservées à un autre rôle sont cachées tant qu'elles sont vides.** Dès qu'elles sont remplies, elles apparaissent, en lecture seule, pour que chacun puisse en prendre connaissance avant de certifier ou d'approuver.

| Rôle | Voit tout le temps | Caché tant que c'est vide |
|---|---|---|
| Personne en appréciation | Introduction, identification, sections A à D, section F, sa certification | Cotes du supérieur, section E, évaluation globale |
| Supérieur(e) immédiat(e) | Tout, sauf ce qui est à droite | Section F, certification |
| Supérieur(e) hiérarchique et directeur | Le contenu du dossier, en lecture | Sections E, F, évaluation globale, certification |

## Inchangé, à votre demande
- Ordre des postures selon le PBRI : Performant, Bienveillant, Responsable, Innovant.
- Cadre sans équipe, section C : la question du Word du 15 octobre.
- « Pour chacune des compétences suivantes, donnez… » : avec la virgule.

Testé le 19 octobre 2026 en navigateur automatisé, sans erreur :
- les 4 rôles ;
- le rôle gardé après actualisation, puis effacé par « Nouveau formulaire » ;
- l'aperçu SharePoint isolé ;
- l'usage sur le poste ;
- le PDF.
