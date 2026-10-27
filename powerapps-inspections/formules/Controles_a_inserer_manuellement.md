# Deux contrôles à insérer manuellement

Ces deux contrôles ne sont pas inclus dans les fichiers YAML (leur collage n'est pas fiable
d'une version de Power Apps Studio à l'autre). Insérez-les après avoir collé les écrans.

## 1. Signature — écran `scrResume`

*Insérer → Entrée → **Entrée de stylet*** (Pen input). Renommez le contrôle **`penSignature`**.

| Propriété | Valeur |
|---|---|
| X / Y | `16` / `594` |
| Largeur / Hauteur | `420` / `140` |
| Mode | `PenMode.Draw` |
| ShowControls | `false` |
| Color | `ColorValue("#1e293b")` |
| Size | `3` |

Placez-le par-dessus le cadre gris `recCadreSignature`.

## 2. Ajout de photos — écran `scrInspection` (fenêtre de détail)

*Insérer → Média → **Ajouter une image*** (Add picture). Power Apps crée un groupe avec
`AddMediaButton1` et `UploadedImage1` : **supprimez `UploadedImage1`** et gardez le bouton,
renommé **`addPhoto`**.

| Propriété | Valeur |
|---|---|
| X / Y | `207` / `586` |
| Largeur / Hauteur | `300` / `44` |
| Text | `"📷 Ajouter une image"` |
| Visible | `!IsBlank(gblDetail)` |
| OnChange | voir ci-dessous |

**OnChange** (version française, séparateur « ; ») :

```
If(!IsBlank(Self.Media);
    INSAjouterPhoto.Run(
        "Photo_" & gblInspCle & "_" & gblDetail & "_" & Text(Now(); "yyyymmddhhmmss") & ".jpg";
        Substitute(JSON(Self.Media; JSONFormat.IncludeBinaryData); Char(34); "");
        gblInspCle & "_" & gblDetail;
        gblInspCle
    );;
    Refresh('Photos inspections');;
    Reset(Self);;
    Notify("Photo ajoutée."; NotificationType.Success)
)
```

**OnChange** (version anglaise, séparateur « , ») :

```
If(!IsBlank(Self.Media),
    INSAjouterPhoto.Run(
        "Photo_" & gblInspCle & "_" & gblDetail & "_" & Text(Now(), "yyyymmddhhmmss") & ".jpg",
        Substitute(JSON(Self.Media, JSONFormat.IncludeBinaryData), Char(34), ""),
        gblInspCle & "_" & gblDetail,
        gblInspCle
    );
    Refresh('Photos inspections');
    Reset(Self);
    Notify("Photo ajoutée.", NotificationType.Success)
)
```

Après l'insertion : clic droit sur le contrôle → **Réorganiser → Mettre au premier plan**
(il doit être au-dessus du rectangle blanc `recDialogue_Det`).
