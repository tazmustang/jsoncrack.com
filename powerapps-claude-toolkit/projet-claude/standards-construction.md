# Mes standards de construction Power Apps — À PERSONNALISER

> C'est ce fichier qui fait que Claude construit **comme vous**. Modifiez librement chaque valeur.
> Les valeurs ci-dessous sont un point de départ raisonnable. Ajoutez ce fichier aux **Connaissances**
> de votre projet Claude.

## 1. Format et mise en page

- Format par défaut : **Tablette 1366 × 768** (application interne) — téléphone 640 × 1136 si précisé.
- Mise en page **responsive** : conteneurs `GroupContainer` en `AutoLayout` (vertical / horizontal),
  pas de positions X/Y codées en dur sauf exception.
- Structure de chaque écran :
  1. `con<Écran>Root` (vertical, remplit l'écran)
  2. `con<Écran>Header` (horizontal, hauteur 64) : titre + boutons d'action
  3. `con<Écran>Body` (remplit le reste) : contenu
- Marges : `PaddingTop/Bottom/Left/Right = 16`, espacement entre éléments (`LayoutGap`) = 12.

## 2. Conventions de nommage

| Élément | Préfixe | Exemple |
|---|---|---|
| Écran | `scr` | `scrAccueil`, `scrDetail` |
| Conteneur | `con` | `conAccueilHeader` |
| Galerie | `gal` | `galDemandes` |
| Formulaire | `frm` | `frmDemande` |
| Étiquette / texte | `lbl` | `lblTitre` |
| Bouton | `btn` | `btnEnregistrer` |
| Zone de saisie | `txt` | `txtRecherche` |
| Liste déroulante | `drp` | `drpStatut` |
| Liste modifiable (combo) | `cmb` | `cmbProjet` |
| Sélecteur de date | `dte` | `dteDebut` |
| Icône | `ico` | `icoRetour` |
| Variable globale | `gbl` | `gblUtilisateur` |
| Variable de contexte | `loc` | `locModeEdition` |
| Collection | `col` | `colDemandes` |

Jamais de noms par défaut (`Button1`, `Label3`…).

## 3. Thème et couleurs

Déclarées une seule fois dans `App.Formulas` (formules nommées) :

```
fxCouleurPrimaire = ColorValue("#0F6CBD");
fxCouleurFond     = ColorValue("#F5F5F5");
fxCouleurTexte    = ColorValue("#242424");
fxCouleurSucces   = ColorValue("#107C10");
fxCouleurErreur   = ColorValue("#C50F1F");
fxPolice          = Font.'Segoe UI';
```

Tous les contrôles référencent ces formules, jamais une couleur en dur.

## 4. Données et performance

- Respecter la **délégation** : `Filter`, `Sort`, `Search` directement sur la source ; pas de
  `CountRows` sur une grosse liste ; pas de `in` ni de `Len` dans un `Filter` délégué SharePoint.
- Utilisateur courant chargé une fois : `App.Formulas` → `fxUtilisateur = User();`
- Préférer `Patch` + validation manuelle pour les écrans simples, `EditForm`/`SubmitForm` pour les
  formulaires de plus de 6 champs.
- Toujours un message de confirmation (`Notify(... , NotificationType.Success)`) après un
  enregistrement et un message d'erreur clair en cas d'échec (`IfError`).

## 5. Ergonomie

- Bouton principal à droite dans l'en-tête, bouton retour (`icoRetour`) à gauche.
- Galeries : état vide affiché (« Aucune demande pour le moment »).
- Les champs obligatoires sont marqués d'un astérisque et le bouton Enregistrer est désactivé tant
  qu'ils ne sont pas remplis (`DisplayMode`).
- Accessibilité : `AccessibleLabel` renseigné sur les icônes et boutons, contraste suffisant.

## 6. À ne JAMAIS faire

- `Navigate` dans `App.OnStart` (utiliser `App.StartScreen`).
- Charger toute une liste dans une collection au démarrage « pour aller plus vite ».
- Couleurs, tailles de police ou textes répétés en dur dans 20 contrôles.
- Laisser un `Screen1` vide dans l'application.

## 7. Mes leçons apprises (s'allonge avec le temps)

- (ajoutez ici les erreurs que Claude a faites et la bonne façon de faire)
