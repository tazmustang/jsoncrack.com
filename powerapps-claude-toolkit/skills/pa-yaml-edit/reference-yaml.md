# Référence YAML Power Apps (.pa.yaml)

Résumé du format du code source des applications Canvas, d'après la documentation Microsoft
(plugin officiel `canvas-apps` de microsoft/power-platform-skills).

## Structure d'un écran

```yaml
Screens:
  scrAccueil:
    Properties:
      Fill: =fxCouleurFond
      OnVisible: |-
        =Set(locRecherche, "");
        Set(locFiltreStatut, "Tous")
    Children:
      - conAccueilRoot:
          Control: GroupContainer
          Variant: AutoLayout
          Properties:
            LayoutDirection: =LayoutDirection.Vertical
            Width: =Parent.Width
            Height: =Parent.Height
          Children:
            - lblTitre:
                Control: Label
                Properties:
                  Text: ="Mes demandes"
```

- `Control` : type du contrôle (obligatoire). Reprendre les noms exacts vus dans « Afficher le code »
  de votre Studio (ils peuvent porter une version, ex. `Button@0.0.45` — conservez-la telle quelle).
- `Variant` : obligatoire pour certains contrôles (`GroupContainer` : `AutoLayout`, `ManualLayout`,
  `GridLayout` ; `Gallery` : `Vertical`, `Horizontal`, `VariableHeight`…).
- `Properties` : formules Power Fx. `Children` : liste ordonnée des contrôles enfants.
- Les composants : `Control: CanvasComponent` + `ComponentName: …`.

## Objet App (à saisir dans Studio, ne se colle pas)

```yaml
App:
  Properties:
    StartScreen: =scrAccueil
    Formulas: |-
      =fxCouleurPrimaire = ColorValue("#0F6CBD");
      fxUtilisateur = User();
```

## Règles qui font échouer le collage

| Message | Cause | Correction |
|---|---|---|
| `Power Fx expressions must start with '='` | valeur sans `=` | `Text: ="Texte"`, `Width: =320` |
| `found invalid mapping` | valeur non entre apostrophes contenant `: ` | `Text: '="Statut : " & x'` ou bloc `\|-` |
| idem, sur un `{Value: …}` | enregistrement non entre apostrophes | `Default: '={Value: "A"}'` |
| `Expected 'MappingEnd'` (ligne N) | mauvaise indentation | aligner avec les éléments frères |
| `did not find expected '-' indicator` | enfant sans `- ` | `- nomControle:` |
| `Named object value cannot be null` | `Properties:` vide ou propriété sans valeur | supprimer la clé ou donner une valeur |
| `Duplicate name` | même propriété écrite deux fois | supprimer le doublon |
| `found character that cannot start any token` | tabulation | remplacer par des espaces |

## Formules multi-lignes

```yaml
OnSelect: |-
  =IfError(
      Patch(Demandes, Defaults(Demandes), {Title: txtTitre.Value, Statut: {Value: "Soumis"}}),
      Notify("Échec de l'enregistrement", NotificationType.Error),
      Notify("Demande envoyée", NotificationType.Success); Navigate(scrAccueil)
  )
```

(Dans un bloc `|-`, les `{...}` et les `: ` n'ont pas besoin d'apostrophes.)

## Pièges Power Fx fréquents

- Colonne Choix SharePoint : lire `ThisItem.Statut.Value`, écrire `{Value: "Approuvé"}`.
- Colonne Personne : lire `ThisItem.Demandeur.DisplayName` ; écrire un enregistrement complet
  (`Claims`, `DisplayName`, `Email`…) ou utiliser une combo liée à Office365Users.
- Délégation SharePoint : `Filter(Source, Statut.Value = "Soumis")` délègue ; `Search` et `in` ne
  délèguent pas → avertissement (triangle jaune) au-delà de 500/2000 lignes.
- `GroupContainer` n'a pas d'`OnSelect`.
- Pas de `Navigate` dans `App.OnStart`.
