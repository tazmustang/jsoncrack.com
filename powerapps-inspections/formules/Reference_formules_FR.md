# Référence des formules (version navigateur en français : séparateur « ; »)

À utiliser seulement si le collage YAML ne fonctionne pas : créez le contrôle manuellement puis copiez chaque propriété.


## Écran scrAccueil (fichier 1_scrAccueil.yaml)


### recBarre_Acc  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Acc  (Label)

- **Text** :
```
="Inspections du milieu de travail — Bâtiments, cours et accès"
```
- **Size** :
```
=16
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=760, Hauteur=56

### btnNouvelleInspection  (Classic/Button)

- **Text** :
```
="+ Nouvelle inspection"
```
- **OnSelect** :
```
=Set(gblInspID; Blank());;
Set(gblInspCle; Text(GUID()));;
Set(gblInfo; {Endroit: ""; Service: ""; Inspecteur: User().FullName; DateInspection: Today(); Participants: ""});;
Set(gblNA; "");;
Set(gblSignature; "");;
ClearCollect(colReponses; ForAll(nfItems As it; Patch(nfReponseVide; {Cle: it.Cle; SectionNo: it.SectionNo; Element: it.Element; Echeance: Blank(); DateRealise: Blank()})));;
Clear(colSupprimes);;
Set(gblSection; 1);;
Set(gblDetail; "");;
Set(gblModifie; false);;
Set(gblAvertiQuitter; false);;
Navigate(scrInspection; ScreenTransition.None)
```
- **Fill** :
```
=ColorValue("#16a34a")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#16a34a"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=968, Y=10, Largeur=190, Hauteur=36

### btnAllerSuivi  (Classic/Button)

- **Text** :
```
="Suivi des correctifs"
```
- **OnSelect** :
```
=Navigate(scrSuivi; ScreenTransition.None)
```
- **Fill** :
```
=ColorValue("#475569")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#475569"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1166, Y=10, Largeur=184, Hauteur=36

### lblAccAide  (Label)

- **Text** :
```
="Cliquez sur une inspection pour l'ouvrir. Les inspections sont enregistrées dans les listes SharePoint INS_Inspections et INS_Reponses."
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- Position : X=16, Y=64, Largeur=1000, Hauteur=28

### txtRechAccueil  (Classic/TextInput)

- **Default** :
```
=""
```
- **OnChange** :
```
=false
```
- **HintText** :
```
="Rechercher (début de l'endroit, du service ou de l'inspecteur)…"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=16, Y=96, Largeur=420, Hauteur=36

### lblAccNombre  (Label)

- **Text** :
```
=CountRows(galInspections.AllItems) & " inspection(s)"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- Position : X=450, Y=96, Largeur=400, Hauteur=36

### recAccEntetes  (Rectangle)

- **Fill** :
```
=ColorValue("#f1f5f9")
```
- Position : X=16, Y=140, Largeur=1334, Hauteur=30

### lblAccH1  (Label)

- **Text** :
```
="Endroit / Service · Inspecteur"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#475569")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=28, Y=140, Largeur=560, Hauteur=30

### lblAccH2  (Label)

- **Text** :
```
="Date / Suivi"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#475569")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=606, Y=140, Largeur=480, Hauteur=30

### lblAccH3  (Label)

- **Text** :
```
="Statut"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#475569")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=1096, Y=140, Largeur=150, Hauteur=30

### galInspections  (Gallery)

- **Items** :
```
=Sort(Filter(INS_Inspections; IsBlank(txtRechAccueil.Text) || StartsWith(Title; txtRechAccueil.Text) || StartsWith(Service; txtRechAccueil.Text) || StartsWith(Inspecteur; txtRechAccueil.Text)); DateInspection; SortOrder.Descending)
```
- **TemplateSize** :
```
=76
```
- **TemplatePadding** :
```
=0
```
- **OnSelect** :
```
=With({i: LookUp(INS_Inspections; ID = ThisItem.ID)};
    Set(gblInspID; i.ID);;
    Set(gblInspCle; Coalesce(i.IdInspection; Text(GUID())));;
    Set(gblInfo; {Endroit: i.Title; Service: i.Service; Inspecteur: i.Inspecteur; DateInspection: Coalesce(i.DateInspection; Today()); Participants: i.Participants});;
    Set(gblNA; Coalesce(i.SectionsNA; ""));;
    Set(gblSignature; Coalesce(i.Signature; ""))
);;
ClearCollect(colSaved; Filter(INS_Reponses; InspectionID = gblInspID));;
ClearCollect(
    colReponses;
    ForAll(
        nfItems As it;
        With({s: LookUp(colSaved; ItemID = it.Cle)};
            {LigneID: Coalesce(s.ID; 0); Cle: it.Cle; SectionNo: it.SectionNo; Element: it.Element; EstAutre: false; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
        )
    )
);;
Collect(
    colReponses;
    ForAll(
        Sort(Filter(colSaved; SectionNo = 21); ID) As s;
        {LigneID: s.ID; Cle: s.ItemID; SectionNo: 21; Element: s.Title; EstAutre: true; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
    )
);;
Clear(colSupprimes);;
Set(gblSection; 1);;
Set(gblDetail; "");;
Set(gblModifie; false);;
Set(gblAvertiQuitter; false);;
Navigate(scrInspection; ScreenTransition.None)
```
- **ShowScrollbar** :
```
=true
```
- Position : X=16, Y=172, Largeur=1334, Hauteur=586

### lblAccEndroit  (Label)  — dans galInspections

- **Text** :
```
=Coalesce(ThisItem.Title; "(sans endroit)")
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#1f2937")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=12, Y=6, Largeur=560, Hauteur=30

### lblAccService  (Label)  — dans galInspections

- **Text** :
```
=ThisItem.Service & If(IsBlank(ThisItem.Inspecteur); ""; "  ·  " & ThisItem.Inspecteur)
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- Position : X=12, Y=38, Largeur=560, Hauteur=28

### lblAccDate  (Label)  — dans galInspections

- **Text** :
```
=Text(ThisItem.DateInspection; "yyyy-mm-dd")
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#1f2937")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=590, Y=6, Largeur=160, Hauteur=30

### lblAccStats  (Label)  — dans galInspections

- **Text** :
```
=Coalesce(ThisItem.NbNonConformes; 0) & " non-conformité(s)  ·  " & Coalesce(ThisItem.NbGraviteElevee; 0) & " gravité E  ·  " & Coalesce(ThisItem.CorrectifsOuverts; 0) & " à réaliser" & If(IsBlank(ThisItem.ProchaineEcheance); ""; "  ·  prochaine éch. " & Text(ThisItem.ProchaineEcheance; "yyyy-mm-dd"))
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- Position : X=590, Y=38, Largeur=480, Hauteur=28

### lblAccStatut  (Label)  — dans galInspections

- **Text** :
```
=Coalesce(ThisItem.StatutSuivi; "—")
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=Switch(ThisItem.StatutSuivi; "Ouvert"; ColorValue("#dc2626"); "En cours"; ColorValue("#ea580c"); "Fermé"; ColorValue("#16a34a"); ColorValue("#64748b"))
```
- **Align** :
```
=Align.Center
```
- Position : X=1080, Y=20, Largeur=150, Hauteur=32

### icoAccSupprimer  (Classic/Icon)  — dans galInspections

- **Icon** :
```
=Icon.Trash
```
- **OnSelect** :
```
=Set(gblASupprimer; ThisItem)
```
- **Color** :
```
=ColorValue("#dc2626")
```
- **Tooltip** :
```
="Supprimer cette inspection"
```
- **PaddingTop** :
```
=6
```
- **PaddingBottom** :
```
=6
```
- **PaddingLeft** :
```
=6
```
- **PaddingRight** :
```
=6
```
- Position : X=1250, Y=16, Largeur=44, Hauteur=44

### recAccSep  (Rectangle)  — dans galInspections

- **Y** :
```
=Parent.TemplateHeight - 1
```
- **Width** :
```
=Parent.TemplateWidth
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=Parent.TemplateHeight - 1, Largeur=Parent.TemplateWidth, Hauteur=1

### recVoile_Acc  (Rectangle)

- **Fill** :
```
=RGBA(0; 0; 0; 0,45)
```
- **Visible** :
```
=!IsBlank(gblASupprimer)
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=768

### recDialogue_Acc  (Rectangle)

- **Fill** :
```
=ColorValue("#ffffff")
```
- **Visible** :
```
=!IsBlank(gblASupprimer)
```
- Position : X=403, Y=244, Largeur=560, Hauteur=230

### lblDialogue_Acc  (Label)

- **Text** :
```
="Supprimer définitivement l'inspection « " & gblASupprimer.Title & " » du " & Text(gblASupprimer.DateInspection; "yyyy-mm-dd") & " et toutes ses réponses ?"
```
- **Size** :
```
=12
```
- **Color** :
```
=ColorValue("#1f2937")
```
- **Visible** :
```
=!IsBlank(gblASupprimer)
```
- Position : X=427, Y=260, Largeur=512, Hauteur=120

### btnConfirmerSuppr  (Classic/Button)

- **Text** :
```
="Supprimer"
```
- **OnSelect** :
```
=Remove(INS_Reponses; Filter(INS_Reponses; InspectionID = gblASupprimer.ID));;
Remove(INS_Inspections; gblASupprimer);;
Set(gblASupprimer; Blank());;
Notify("Inspection supprimée."; NotificationType.Success)
```
- **Fill** :
```
=ColorValue("#dc2626")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#dc2626"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **Visible** :
```
=!IsBlank(gblASupprimer)
```
- Position : X=427, Y=400, Largeur=240, Hauteur=44

### btnAnnulerSuppr  (Classic/Button)

- **Text** :
```
="Annuler"
```
- **OnSelect** :
```
=Set(gblASupprimer; Blank())
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- **Color** :
```
=ColorValue("#1e293b")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#e2e8f0"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **Visible** :
```
=!IsBlank(gblASupprimer)
```
- Position : X=699, Y=400, Largeur=240, Hauteur=44

## Écran scrInspection (fichier 2_scrInspection.yaml)


### recBarre_Ins  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Ins  (Label)

- **Text** :
```
="Inspection — Bâtiments, cours et accès"
```
- **Size** :
```
=16
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=520, Hauteur=56

### lblEtat_Ins  (Label)

- **Text** :
```
=If(gblModifie; "● Modifications non enregistrées"; If(IsBlank(gblInspID); "Nouvelle inspection"; "✔ Enregistrée dans SharePoint"))
```
- **Size** :
```
=10
```
- **Color** :
```
=If(gblModifie; ColorValue("#fbbf24"); ColorValue("#86efac"))
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=540, Y=0, Largeur=380, Hauteur=56

### btnAccueil_Ins  (Classic/Button)

- **Text** :
```
="Accueil"
```
- **OnSelect** :
```
=If(
    gblModifie && !gblAvertiQuitter;
    Set(gblAvertiQuitter; true);;
    Notify("Modifications non enregistrées ! Cliquez sur « Enregistrer », ou cliquez de nouveau sur « Accueil » pour quitter sans enregistrer."; NotificationType.Warning);
    Set(gblAvertiQuitter; false);;
    Set(gblModifie; false);;
    Navigate(scrAccueil; ScreenTransition.None)
)
```
- **Fill** :
```
=ColorValue("#475569")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#475569"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1072, Y=10, Largeur=120, Hauteur=36

### btnEnregistrer_Ins  (Classic/Button)

- **Text** :
```
="Enregistrer"
```
- **OnSelect** :
```
=If(
    IsBlank(Trim(gblInfo.Endroit));
    Notify("Le champ « Endroit » est obligatoire avant d'enregistrer."; NotificationType.Error);
    With({nonNA: Filter(colReponses; !(("|" & SectionNo & "|") in gblNA))};
        Set(
            gblEnreg;
            Patch(
                INS_Inspections;
                If(IsBlank(gblInspID); Defaults(INS_Inspections); LookUp(INS_Inspections; ID = gblInspID));
                {
                    Title: gblInfo.Endroit;
                    Service: gblInfo.Service;
                    Inspecteur: gblInfo.Inspecteur;
                    DateInspection: gblInfo.DateInspection;
                    Participants: gblInfo.Participants;
                    SectionsNA: gblNA;
                    Signature: gblSignature;
                    IdInspection: gblInspCle;
                    NbApplicables: CountRows(nonNA);
                    NbRepondus: CountIf(nonNA; !IsBlank(Reponse));
                    NbNonConformes: CountIf(nonNA; Reponse = "N");
                    NbGraviteElevee: CountIf(nonNA; Reponse = "N" && Gravite = "E");
                    CorrectifsOuverts: CountIf(nonNA; Reponse = "N" && Statut <> "Réalisé");
                    ProchaineEcheance: Min(Filter(nonNA; Reponse = "N" && Statut <> "Réalisé" && !IsBlank(Echeance)); Echeance);
                    StatutSuivi: If(
                        CountIf(nonNA; Reponse = "N") = 0; "Aucun correctif";
                        CountIf(nonNA; Reponse = "N" && Statut <> "Réalisé") = 0; "Fermé";
                        CountIf(nonNA; Reponse = "N" && (Statut = "En cours" || Statut = "Réalisé")) > 0; "En cours";
                        "Ouvert"
                    )
                }
            )
        )
    );;
    Set(gblInspID; gblEnreg.ID);;
    ForAll(colSupprimes As d; Remove(INS_Reponses; LookUp(INS_Reponses; ID = d.LigneID)));;
    Clear(colSupprimes);;
    // Mise à jour des réponses déjà enregistrées
    ForAll(
        Filter(colReponses; LigneID > 0) As r;
        Patch(INS_Reponses; LookUp(INS_Reponses; ID = r.LigneID); {
                Title: r.Element;
                InspectionID: gblInspID;
                IdInspection: gblInspCle;
                ItemID: r.Cle;
                SectionNo: r.SectionNo;
                Sujet: LookUp(nfSections; Numero = r.SectionNo).Titre;
                Reponse: r.Reponse;
                Applicable: If(("|" & r.SectionNo & "|") in gblNA; "Non"; "Oui");
                Gravite: r.Gravite;
                Commentaire: r.Commentaire;
                Emplacement: r.Emplacement;
                Responsable: r.Responsable;
                Echeance: r.Echeance;
                StatutCorrectif: r.Statut;
                DateRealise: r.DateRealise;
                Endroit: gblInfo.Endroit;
                Service: gblInfo.Service;
                DateInspection: gblInfo.DateInspection
            })
    );;
    // Création des nouvelles réponses (en un seul envoi)
    With(
        {nouv: ForAll(Filter(colReponses; LigneID = 0 && (!IsBlank(Reponse) || !IsBlank(Commentaire) || EstAutre)) As r; {
                    Title: r.Element;
                    InspectionID: gblInspID;
                    IdInspection: gblInspCle;
                    ItemID: r.Cle;
                    SectionNo: r.SectionNo;
                    Sujet: LookUp(nfSections; Numero = r.SectionNo).Titre;
                    Reponse: r.Reponse;
                    Applicable: If(("|" & r.SectionNo & "|") in gblNA; "Non"; "Oui");
                    Gravite: r.Gravite;
                    Commentaire: r.Commentaire;
                    Emplacement: r.Emplacement;
                    Responsable: r.Responsable;
                    Echeance: r.Echeance;
                    StatutCorrectif: r.Statut;
                    DateRealise: r.DateRealise;
                    Endroit: gblInfo.Endroit;
                    Service: gblInfo.Service;
                    DateInspection: gblInfo.DateInspection
                })};
        If(CountRows(nouv) > 0; Patch(INS_Reponses; ForAll(nouv; Defaults(INS_Reponses)); nouv))
    );;
    ClearCollect(colSaved; Filter(INS_Reponses; InspectionID = gblInspID));;
    ClearCollect(
        colReponses;
        ForAll(
            nfItems As it;
            With({s: LookUp(colSaved; ItemID = it.Cle)};
                {LigneID: Coalesce(s.ID; 0); Cle: it.Cle; SectionNo: it.SectionNo; Element: it.Element; EstAutre: false; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
            )
        )
    );;
    Collect(
        colReponses;
        ForAll(
            Sort(Filter(colSaved; SectionNo = 21); ID) As s;
            {LigneID: s.ID; Cle: s.ItemID; SectionNo: 21; Element: s.Title; EstAutre: true; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
        )
    );;
    Set(gblModifie; false);;
    Set(gblAvertiQuitter; false);;
    Notify("Inspection enregistrée dans SharePoint."; NotificationType.Success)
)
```
- **Fill** :
```
=ColorValue("#16a34a")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#16a34a"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1200, Y=10, Largeur=150, Hauteur=36

### recOnglets_Ins  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngInsp_Ins  (Classic/Button)

- **Text** :
```
="Inspection"
```
- **OnSelect** :
```
=Navigate(scrInspection; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrInspection"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrInspection"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=16, Y=62, Largeur=210, Hauteur=36

### btnOngResume_Ins  (Classic/Button)

- **Text** :
```
="Résumé et envoi"
```
- **OnSelect** :
```
=Navigate(scrResume; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrResume"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrResume"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=234, Y=62, Largeur=210, Hauteur=36

### btnOngSuivi_Ins  (Classic/Button)

- **Text** :
```
="Suivi des correctifs"
```
- **OnSelect** :
```
=Navigate(scrSuivi; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSuivi"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSuivi"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=452, Y=62, Largeur=210, Hauteur=36

### lblI_Endroit  (Label)

- **Text** :
```
="Endroit *"
```
- **Size** :
```
=8
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **PaddingLeft** :
```
=0
```
- **PaddingTop** :
```
=0
```
- **PaddingBottom** :
```
=0
```
- Position : X=16, Y=108, Largeur=300, Hauteur=16

### txtEndroit  (Classic/TextInput)

- **Default** :
```
=gblInfo.Endroit
```
- **OnChange** :
```
=If(Self.Text <> gblInfo.Endroit; Set(gblInfo; Patch(gblInfo; {Endroit: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Ex. : Garage municipal…"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=16, Y=124, Largeur=300, Hauteur=34

### lblI_Service  (Label)

- **Text** :
```
="Service"
```
- **Size** :
```
=8
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **PaddingLeft** :
```
=0
```
- **PaddingTop** :
```
=0
```
- **PaddingBottom** :
```
=0
```
- Position : X=324, Y=108, Largeur=260, Hauteur=16

### txtService  (Classic/TextInput)

- **Default** :
```
=gblInfo.Service
```
- **OnChange** :
```
=If(Self.Text <> gblInfo.Service; Set(gblInfo; Patch(gblInfo; {Service: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Service"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=324, Y=124, Largeur=260, Hauteur=34

### lblI_Insp  (Label)

- **Text** :
```
="Inspection réalisée par"
```
- **Size** :
```
=8
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **PaddingLeft** :
```
=0
```
- **PaddingTop** :
```
=0
```
- **PaddingBottom** :
```
=0
```
- Position : X=592, Y=108, Largeur=260, Hauteur=16

### txtInspecteur  (Classic/TextInput)

- **Default** :
```
=gblInfo.Inspecteur
```
- **OnChange** :
```
=If(Self.Text <> gblInfo.Inspecteur; Set(gblInfo; Patch(gblInfo; {Inspecteur: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Nom de l'inspecteur"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=592, Y=124, Largeur=260, Hauteur=34

### lblI_Date  (Label)

- **Text** :
```
="Date"
```
- **Size** :
```
=8
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **PaddingLeft** :
```
=0
```
- **PaddingTop** :
```
=0
```
- **PaddingBottom** :
```
=0
```
- Position : X=860, Y=108, Largeur=170, Hauteur=16

### dpDateInspection  (Classic/DatePicker)

- **DefaultDate** :
```
=gblInfo.DateInspection
```
- **Format** :
```
="yyyy-mm-dd"
```
- **Size** :
```
=10
```
- **OnChange** :
```
=If(Self.SelectedDate <> gblInfo.DateInspection; Set(gblInfo; Patch(gblInfo; {DateInspection: Self.SelectedDate}));; Set(gblModifie; true))
```
- Position : X=860, Y=124, Largeur=170, Hauteur=34

### lblI_Part  (Label)

- **Text** :
```
="Participants"
```
- **Size** :
```
=8
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **PaddingLeft** :
```
=0
```
- **PaddingTop** :
```
=0
```
- **PaddingBottom** :
```
=0
```
- Position : X=1038, Y=108, Largeur=312, Hauteur=16

### txtParticipants  (Classic/TextInput)

- **Default** :
```
=gblInfo.Participants
```
- **OnChange** :
```
=If(Self.Text <> gblInfo.Participants; Set(gblInfo; Patch(gblInfo; {Participants: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Autres participants"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=1038, Y=124, Largeur=312, Hauteur=34

### recProgFond  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=16, Y=170, Largeur=600, Hauteur=14

### recProgBarre  (Rectangle)

- **Fill** :
```
=ColorValue("#2563eb")
```
- Position : X=16, Y=170, Largeur=With({a: CountIf(colReponses, !(("|" & SectionNo & "|") in gblNA)), r: CountIf(colReponses, !(("|" & SectionNo & "|") in gblNA) && !IsBlank(Reponse))}, If(a = 0, 0, 600 * r / a)), Hauteur=14

### lblProgression  (Label)

- **Text** :
```
=With({a: CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA)); r: CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && !IsBlank(Reponse))}; "" & r & "/" & a & " éléments répondus (" & If(a = 0; 0; Round(100 * r / a; 0)) & " %)  ·  " & CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N") & " non-conformité(s)")
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#334155")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=628, Y=162, Largeur=720, Hauteur=30

### galSections  (Gallery)

- **Items** :
```
=nfSections
```
- **TemplateSize** :
```
=54
```
- **TemplatePadding** :
```
=0
```
- **ShowScrollbar** :
```
=true
```
- **TemplateFill** :
```
=If(ThisItem.Numero = gblSection; ColorValue("#dbeafe"); ColorValue("#ffffff"))
```
- **OnSelect** :
```
=Set(gblSection; ThisItem.Numero)
```
- Position : X=8, Y=200, Largeur=370, Hauteur=560

### lblSecTitre  (Label)  — dans galSections

- **Text** :
```
=ThisItem.Numero & ". " & ThisItem.Titre
```
- **Size** :
```
=11
```
- **Color** :
```
=If((("|" & ThisItem.Numero & "|") in gblNA); ColorValue("#94a3b8"); ColorValue("#1e293b"))
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=10, Y=2, Largeur=330, Hauteur=28

### lblSecCompte  (Label)  — dans galSections

- **Text** :
```
=If((("|" & ThisItem.Numero & "|") in gblNA); "Non applicable"; With({n: CountIf(colReponses; SectionNo = ThisItem.Numero); r: CountIf(colReponses; SectionNo = ThisItem.Numero && !IsBlank(Reponse)); nc: CountIf(colReponses; SectionNo = ThisItem.Numero && Reponse = "N")}; r & "/" & n & " répondus" & If(nc > 0; "  ·  " & nc & " non conforme(s)"; "")))
```
- **Size** :
```
=9
```
- **Color** :
```
=If(CountIf(colReponses; SectionNo = ThisItem.Numero && Reponse = "N") > 0 && !(("|" & ThisItem.Numero & "|") in gblNA); ColorValue("#b91c1c"); ColorValue("#64748b"))
```
- Position : X=10, Y=28, Largeur=330, Hauteur=22

### recSecSep  (Rectangle)  — dans galSections

- **Y** :
```
=Parent.TemplateHeight - 1
```
- **Width** :
```
=Parent.TemplateWidth
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=Parent.TemplateHeight - 1, Largeur=Parent.TemplateWidth, Hauteur=1

### lblSujetCourant  (Label)

- **Text** :
```
=gblSection & ". " & LookUp(nfSections; Numero = gblSection).Titre
```
- **Size** :
```
=14
```
- **Color** :
```
=ColorValue("#1e293b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=392, Y=200, Largeur=480, Hauteur=40

### btnApplicable  (Classic/Button)

- **Text** :
```
=If((("|" & gblSection & "|") in gblNA); "Non applicable ✔ (rétablir)"; "Marquer non applicable")
```
- **OnSelect** :
```
=If((("|" & gblSection & "|") in gblNA); Set(gblNA; Substitute(gblNA; "|" & gblSection & "|"; "")); Set(gblNA; gblNA & "|" & gblSection & "|"));; Set(gblModifie; true)
```
- **Fill** :
```
=ColorValue("#64748b")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#64748b"); -15%)
```
- **Size** :
```
=9
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=880, Y=204, Largeur=210, Hauteur=34

### btnSansReponse  (Classic/Button)

- **Text** :
```
=If(gblSansReponse; "☑ Seulement sans réponse"; "☐ Seulement sans réponse")
```
- **OnSelect** :
```
=Set(gblSansReponse; !gblSansReponse)
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- **Color** :
```
=ColorValue("#1e293b")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#e2e8f0"); -15%)
```
- **Size** :
```
=9
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1098, Y=204, Largeur=252, Hauteur=34

### lblSujetNA  (Label)

- **Text** :
```
="Ce sujet est marqué « Non applicable » : ses éléments ne sont pas comptés."
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#64748b")
```
- **Visible** :
```
=(("|" & gblSection & "|") in gblNA)
```
- Position : X=392, Y=250, Largeur=958, Hauteur=60

### galElements  (Gallery)

- **Items** :
```
=Filter(colReponses; SectionNo = gblSection && (!gblSansReponse || IsBlank(Reponse)))
```
- **TemplateSize** :
```
=74
```
- **TemplatePadding** :
```
=0
```
- **ShowScrollbar** :
```
=true
```
- **Visible** :
```
=!(("|" & gblSection & "|") in gblNA)
```
- Position : X=386, Y=246, Largeur=972, Hauteur=470

### lblElement  (Label)  — dans galElements

- **Text** :
```
=ThisItem.Element
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#1f2937")
```
- **Visible** :
```
=!ThisItem.EstAutre
```
- Position : X=12, Y=4, Largeur=530, Hauteur=46

### txtAutreElement  (Classic/TextInput)  — dans galElements

- **Default** :
```
=ThisItem.Element
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Element; Patch(colReponses; LookUp(colReponses; Cle = ThisItem.Cle); {Element: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Décrire l'élément vérifié"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- **Visible** :
```
=ThisItem.EstAutre
```
- Position : X=12, Y=10, Largeur=530, Hauteur=36

### lblResumeItem  (Label)  — dans galElements

- **Text** :
```
=If(ThisItem.Reponse = "N"; "Gravité : " & Coalesce(ThisItem.Gravite; "—") & If(IsBlank(ThisItem.Responsable); ""; " · " & ThisItem.Responsable) & If(IsBlank(ThisItem.Echeance); ""; " · éch. " & Text(ThisItem.Echeance; "yyyy-mm-dd")) & " · " & ThisItem.Statut; "") & If(IsBlank(ThisItem.Commentaire); ""; "   💬 " & Left(ThisItem.Commentaire; 70))
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#b91c1c")
```
- Position : X=12, Y=50, Largeur=530, Hauteur=22

### btnOui  (Classic/Button)  — dans galElements

- **Text** :
```
="Oui"
```
- **OnSelect** :
```
=With({k: ThisItem.Cle; nv: If(ThisItem.Reponse = "O"; ""; "O"); st: ThisItem.Statut};
    Patch(colReponses; LookUp(colReponses; Cle = k); {Reponse: nv; Statut: If(nv = "N" && IsBlank(st); "À faire"; st)});;
    If(nv = "N"; Set(gblDetail; k));;
    Set(gblModifie; true)
)
```
- **Fill** :
```
=If(ThisItem.Reponse = "O"; ColorValue("#16a34a"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(ThisItem.Reponse = "O"; ColorValue("#ffffff"); ColorValue("#334155"))
```
- **HoverFill** :
```
=ColorValue("#e2e8f0")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=1
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **BorderColor** :
```
=ColorValue("#94a3b8")
```
- **DisplayMode** :
```
=If((("|" & ThisItem.SectionNo & "|") in gblNA); DisplayMode.View; DisplayMode.Edit)
```
- Position : X=560, Y=14, Largeur=80, Hauteur=40

### btnNon  (Classic/Button)  — dans galElements

- **Text** :
```
="Non"
```
- **OnSelect** :
```
=With({k: ThisItem.Cle; nv: If(ThisItem.Reponse = "N"; ""; "N"); st: ThisItem.Statut};
    Patch(colReponses; LookUp(colReponses; Cle = k); {Reponse: nv; Statut: If(nv = "N" && IsBlank(st); "À faire"; st)});;
    If(nv = "N"; Set(gblDetail; k));;
    Set(gblModifie; true)
)
```
- **Fill** :
```
=If(ThisItem.Reponse = "N"; ColorValue("#dc2626"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(ThisItem.Reponse = "N"; ColorValue("#ffffff"); ColorValue("#334155"))
```
- **HoverFill** :
```
=ColorValue("#e2e8f0")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=1
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **BorderColor** :
```
=ColorValue("#94a3b8")
```
- **DisplayMode** :
```
=If((("|" & ThisItem.SectionNo & "|") in gblNA); DisplayMode.View; DisplayMode.Edit)
```
- Position : X=646, Y=14, Largeur=80, Hauteur=40

### btnNA  (Classic/Button)  — dans galElements

- **Text** :
```
="N/A"
```
- **OnSelect** :
```
=With({k: ThisItem.Cle; nv: If(ThisItem.Reponse = "NA"; ""; "NA"); st: ThisItem.Statut};
    Patch(colReponses; LookUp(colReponses; Cle = k); {Reponse: nv; Statut: If(nv = "N" && IsBlank(st); "À faire"; st)});;
    If(nv = "N"; Set(gblDetail; k));;
    Set(gblModifie; true)
)
```
- **Fill** :
```
=If(ThisItem.Reponse = "NA"; ColorValue("#64748b"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(ThisItem.Reponse = "NA"; ColorValue("#ffffff"); ColorValue("#334155"))
```
- **HoverFill** :
```
=ColorValue("#e2e8f0")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=1
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **BorderColor** :
```
=ColorValue("#94a3b8")
```
- **DisplayMode** :
```
=If((("|" & ThisItem.SectionNo & "|") in gblNA); DisplayMode.View; DisplayMode.Edit)
```
- Position : X=732, Y=14, Largeur=80, Hauteur=40

### icoDetail  (Classic/Icon)  — dans galElements

- **Icon** :
```
=Icon.Edit
```
- **OnSelect** :
```
=Set(gblDetail; ThisItem.Cle)
```
- **Color** :
```
=ColorValue("#475569")
```
- **Tooltip** :
```
="Commentaire, correctif et photos"
```
- **PaddingTop** :
```
=6
```
- **PaddingBottom** :
```
=6
```
- **PaddingLeft** :
```
=6
```
- **PaddingRight** :
```
=6
```
- Position : X=826, Y=14, Largeur=44, Hauteur=44

### icoSupprAutre  (Classic/Icon)  — dans galElements

- **Icon** :
```
=Icon.Trash
```
- **OnSelect** :
```
=With({k: ThisItem.Cle; id: ThisItem.LigneID};
    If(id > 0; Collect(colSupprimes; {LigneID: id}));;
    Remove(colReponses; LookUp(colReponses; Cle = k));;
    Set(gblModifie; true)
)
```
- **Color** :
```
=ColorValue("#dc2626")
```
- **Tooltip** :
```
="Retirer cet élément"
```
- **PaddingTop** :
```
=6
```
- **PaddingBottom** :
```
=6
```
- **PaddingLeft** :
```
=6
```
- **PaddingRight** :
```
=6
```
- **Visible** :
```
=ThisItem.EstAutre
```
- Position : X=880, Y=14, Largeur=44, Hauteur=44

### recItemSep  (Rectangle)  — dans galElements

- **Y** :
```
=Parent.TemplateHeight - 1
```
- **Width** :
```
=Parent.TemplateWidth
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=Parent.TemplateHeight - 1, Largeur=Parent.TemplateWidth, Hauteur=1

### btnAjouterAutre  (Classic/Button)

- **Text** :
```
="+ Ajouter un élément"
```
- **OnSelect** :
```
=Collect(colReponses; Patch(nfReponseVide; {Cle: "s21-" & Text(GUID()); SectionNo: 21; EstAutre: true; Echeance: Blank(); DateRealise: Blank()}));;
Set(gblModifie; true)
```
- **Fill** :
```
=ColorValue("#2563eb")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#2563eb"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **Visible** :
```
=gblSection = 21 && !(("|" & gblSection & "|") in gblNA)
```
- Position : X=392, Y=722, Largeur=220, Hauteur=36

### recVoile_Det  (Rectangle)

- **Fill** :
```
=RGBA(0; 0; 0; 0,45)
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=768

### recDialogue_Det  (Rectangle)

- **Fill** :
```
=ColorValue("#ffffff")
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=183, Y=40, Largeur=1000, Hauteur=690

### lblDTitre  (Label)

- **Text** :
```
=With({r: LookUp(colReponses; Cle = gblDetail)}; LookUp(nfSections; Numero = r.SectionNo).Titre & " — " & r.Element & If(r.Reponse = "N"; "   (NON CONFORME)"; ""))
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#1e293b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=207, Y=52, Largeur=952, Hauteur=60

### lblDGravite  (Label)

- **Text** :
```
="Potentiel de gravité"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail) && LookUp(colReponses; Cle = gblDetail).Reponse = "N"
```
- Position : X=207, Y=120, Largeur=400, Hauteur=26

### btnGravE  (Classic/Button)

- **Text** :
```
="Élevé (E)"
```
- **OnSelect** :
```
=Patch(colReponses; LookUp(colReponses; Cle = gblDetail); {Gravite: If(LookUp(colReponses; Cle = gblDetail).Gravite = "E"; ""; "E")});; Set(gblModifie; true)
```
- **Fill** :
```
=If(LookUp(colReponses; Cle = gblDetail).Gravite = "E"; ColorValue("#dc2626"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(LookUp(colReponses; Cle = gblDetail).Gravite = "E"; ColorValue("#ffffff"); ColorValue("#334155"))
```
- **HoverFill** :
```
=ColorValue("#e2e8f0")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=1
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **Visible** :
```
=!IsBlank(gblDetail) && LookUp(colReponses; Cle = gblDetail).Reponse = "N"
```
- **BorderColor** :
```
=ColorValue("#94a3b8")
```
- Position : X=207, Y=150, Largeur=150, Hauteur=36

### btnGravF  (Classic/Button)

- **Text** :
```
="Faible (F)"
```
- **OnSelect** :
```
=Patch(colReponses; LookUp(colReponses; Cle = gblDetail); {Gravite: If(LookUp(colReponses; Cle = gblDetail).Gravite = "F"; ""; "F")});; Set(gblModifie; true)
```
- **Fill** :
```
=If(LookUp(colReponses; Cle = gblDetail).Gravite = "F"; ColorValue("#ea580c"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(LookUp(colReponses; Cle = gblDetail).Gravite = "F"; ColorValue("#ffffff"); ColorValue("#334155"))
```
- **HoverFill** :
```
=ColorValue("#e2e8f0")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=1
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **Visible** :
```
=!IsBlank(gblDetail) && LookUp(colReponses; Cle = gblDetail).Reponse = "N"
```
- **BorderColor** :
```
=ColorValue("#94a3b8")
```
- Position : X=365, Y=150, Largeur=150, Hauteur=36

### lblDCom  (Label)

- **Text** :
```
="Correctifs et/ou commentaires"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=207, Y=194, Largeur=600, Hauteur=22

### txtDCommentaire  (Classic/TextInput)

- **Default** :
```
=LookUp(colReponses; Cle = gblDetail).Commentaire
```
- **OnChange** :
```
=false
```
- **HintText** :
```
="Décrire le correctif ou le commentaire"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- **Mode** :
```
=TextMode.MultiLine
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=207, Y=216, Largeur=952, Hauteur=90

### lblDEmpl  (Label)

- **Text** :
```
="Emplacement"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=207, Y=314, Largeur=300, Hauteur=22

### txtDEmplacement  (Classic/TextInput)

- **Default** :
```
=LookUp(colReponses; Cle = gblDetail).Emplacement
```
- **OnChange** :
```
=false
```
- **HintText** :
```
="Emplacement"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=207, Y=336, Largeur=300, Hauteur=36

### lblDResp  (Label)

- **Text** :
```
="Responsable"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=515, Y=314, Largeur=260, Hauteur=22

### txtDResponsable  (Classic/TextInput)

- **Default** :
```
=LookUp(colReponses; Cle = gblDetail).Responsable
```
- **OnChange** :
```
=false
```
- **HintText** :
```
="Responsable"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=515, Y=336, Largeur=260, Hauteur=36

### lblDEch  (Label)

- **Text** :
```
="Échéancier"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=783, Y=314, Largeur=180, Hauteur=22

### dpDEcheance  (Classic/DatePicker)

- **Visible** :
```
=!IsBlank(gblDetail)
```
- **DefaultDate** :
```
=LookUp(colReponses; Cle = gblDetail).Echeance
```
- **Format** :
```
="yyyy-mm-dd"
```
- **Size** :
```
=10
```
- Position : X=783, Y=336, Largeur=180, Hauteur=36

### lblDStatut  (Label)

- **Text** :
```
="Statut du correctif"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail) && LookUp(colReponses; Cle = gblDetail).Reponse = "N"
```
- Position : X=971, Y=314, Largeur=188, Hauteur=22

### ddDStatut  (Classic/DropDown)

- **Items** :
```
=["À faire"; "En cours"; "Réalisé"]
```
- **Default** :
```
=Coalesce(LookUp(colReponses; Cle = gblDetail).Statut; "À faire")
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- **Visible** :
```
=!IsBlank(gblDetail) && LookUp(colReponses; Cle = gblDetail).Reponse = "N"
```
- Position : X=971, Y=336, Largeur=188, Hauteur=36

### lblDPhotos  (Label)

- **Text** :
```
="Photos (" & CountRows(Filter('Photos inspections'; CleReponse = gblInspCle & "_" & gblDetail)) & ")  —  cliquez sur une photo pour l'ouvrir"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#64748b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=207, Y=384, Largeur=700, Hauteur=22

### galDPhotos  (Gallery)

- **Visible** :
```
=!IsBlank(gblDetail)
```
- **Items** :
```
=Filter('Photos inspections'; CleReponse = gblInspCle & "_" & gblDetail)
```
- **TemplateSize** :
```
=120
```
- **TemplatePadding** :
```
=4
```
- **ShowScrollbar** :
```
=true
```
- Position : X=207, Y=410, Largeur=952, Hauteur=124

### imgPhoto  (Image)  — dans galDPhotos

- **Image** :
```
=ThisItem.Thumbnail.Large
```
- **ImagePosition** :
```
=ImagePosition.Fill
```
- **OnSelect** :
```
=Launch(ThisItem.'Link to item')
```
- Position : X=4, Y=4, Largeur=112, Hauteur=112

### lblDPhotoAide  (Label)

- **Text** :
```
="Ajouter une photo : bouton « Ajouter une image » ci-dessous (la photo est déposée dans la bibliothèque SharePoint « Photos inspections »)."
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#64748b")
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=207, Y=540, Largeur=952, Hauteur=40

### btnDFermer  (Classic/Button)

- **Text** :
```
="Fermer"
```
- **OnSelect** :
```
=With({r: LookUp(colReponses; Cle = gblDetail)};
    Patch(
        colReponses;
        r;
        {
            Commentaire: txtDCommentaire.Text;
            Emplacement: txtDEmplacement.Text;
            Responsable: txtDResponsable.Text;
            Echeance: dpDEcheance.SelectedDate;
            Statut: If(r.Reponse = "N"; ddDStatut.Selected.Value; r.Statut);
            DateRealise: If(r.Reponse = "N" && ddDStatut.Selected.Value = "Réalisé"; Coalesce(r.DateRealise; Today()); Blank())
        }
    )
);;
Set(gblModifie; true);;
Set(gblDetail; "")
```
- **Fill** :
```
=ColorValue("#2563eb")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#2563eb"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- **Visible** :
```
=!IsBlank(gblDetail)
```
- Position : X=959, Y=670, Largeur=200, Hauteur=44

## Écran scrResume (fichier 3_scrResume.yaml)


### recBarre_Res  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Res  (Label)

- **Text** :
```
="Résumé et envoi"
```
- **Size** :
```
=16
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=520, Hauteur=56

### lblEtat_Res  (Label)

- **Text** :
```
=If(gblModifie; "● Modifications non enregistrées"; If(IsBlank(gblInspID); "Nouvelle inspection"; "✔ Enregistrée dans SharePoint"))
```
- **Size** :
```
=10
```
- **Color** :
```
=If(gblModifie; ColorValue("#fbbf24"); ColorValue("#86efac"))
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=540, Y=0, Largeur=380, Hauteur=56

### btnAccueil_Res  (Classic/Button)

- **Text** :
```
="Accueil"
```
- **OnSelect** :
```
=If(
    gblModifie && !gblAvertiQuitter;
    Set(gblAvertiQuitter; true);;
    Notify("Modifications non enregistrées ! Cliquez sur « Enregistrer », ou cliquez de nouveau sur « Accueil » pour quitter sans enregistrer."; NotificationType.Warning);
    Set(gblAvertiQuitter; false);;
    Set(gblModifie; false);;
    Navigate(scrAccueil; ScreenTransition.None)
)
```
- **Fill** :
```
=ColorValue("#475569")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#475569"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1072, Y=10, Largeur=120, Hauteur=36

### btnEnregistrer_Res  (Classic/Button)

- **Text** :
```
="Enregistrer"
```
- **OnSelect** :
```
=If(
    IsBlank(Trim(gblInfo.Endroit));
    Notify("Le champ « Endroit » est obligatoire avant d'enregistrer."; NotificationType.Error);
    With({nonNA: Filter(colReponses; !(("|" & SectionNo & "|") in gblNA))};
        Set(
            gblEnreg;
            Patch(
                INS_Inspections;
                If(IsBlank(gblInspID); Defaults(INS_Inspections); LookUp(INS_Inspections; ID = gblInspID));
                {
                    Title: gblInfo.Endroit;
                    Service: gblInfo.Service;
                    Inspecteur: gblInfo.Inspecteur;
                    DateInspection: gblInfo.DateInspection;
                    Participants: gblInfo.Participants;
                    SectionsNA: gblNA;
                    Signature: gblSignature;
                    IdInspection: gblInspCle;
                    NbApplicables: CountRows(nonNA);
                    NbRepondus: CountIf(nonNA; !IsBlank(Reponse));
                    NbNonConformes: CountIf(nonNA; Reponse = "N");
                    NbGraviteElevee: CountIf(nonNA; Reponse = "N" && Gravite = "E");
                    CorrectifsOuverts: CountIf(nonNA; Reponse = "N" && Statut <> "Réalisé");
                    ProchaineEcheance: Min(Filter(nonNA; Reponse = "N" && Statut <> "Réalisé" && !IsBlank(Echeance)); Echeance);
                    StatutSuivi: If(
                        CountIf(nonNA; Reponse = "N") = 0; "Aucun correctif";
                        CountIf(nonNA; Reponse = "N" && Statut <> "Réalisé") = 0; "Fermé";
                        CountIf(nonNA; Reponse = "N" && (Statut = "En cours" || Statut = "Réalisé")) > 0; "En cours";
                        "Ouvert"
                    )
                }
            )
        )
    );;
    Set(gblInspID; gblEnreg.ID);;
    ForAll(colSupprimes As d; Remove(INS_Reponses; LookUp(INS_Reponses; ID = d.LigneID)));;
    Clear(colSupprimes);;
    // Mise à jour des réponses déjà enregistrées
    ForAll(
        Filter(colReponses; LigneID > 0) As r;
        Patch(INS_Reponses; LookUp(INS_Reponses; ID = r.LigneID); {
                Title: r.Element;
                InspectionID: gblInspID;
                IdInspection: gblInspCle;
                ItemID: r.Cle;
                SectionNo: r.SectionNo;
                Sujet: LookUp(nfSections; Numero = r.SectionNo).Titre;
                Reponse: r.Reponse;
                Applicable: If(("|" & r.SectionNo & "|") in gblNA; "Non"; "Oui");
                Gravite: r.Gravite;
                Commentaire: r.Commentaire;
                Emplacement: r.Emplacement;
                Responsable: r.Responsable;
                Echeance: r.Echeance;
                StatutCorrectif: r.Statut;
                DateRealise: r.DateRealise;
                Endroit: gblInfo.Endroit;
                Service: gblInfo.Service;
                DateInspection: gblInfo.DateInspection
            })
    );;
    // Création des nouvelles réponses (en un seul envoi)
    With(
        {nouv: ForAll(Filter(colReponses; LigneID = 0 && (!IsBlank(Reponse) || !IsBlank(Commentaire) || EstAutre)) As r; {
                    Title: r.Element;
                    InspectionID: gblInspID;
                    IdInspection: gblInspCle;
                    ItemID: r.Cle;
                    SectionNo: r.SectionNo;
                    Sujet: LookUp(nfSections; Numero = r.SectionNo).Titre;
                    Reponse: r.Reponse;
                    Applicable: If(("|" & r.SectionNo & "|") in gblNA; "Non"; "Oui");
                    Gravite: r.Gravite;
                    Commentaire: r.Commentaire;
                    Emplacement: r.Emplacement;
                    Responsable: r.Responsable;
                    Echeance: r.Echeance;
                    StatutCorrectif: r.Statut;
                    DateRealise: r.DateRealise;
                    Endroit: gblInfo.Endroit;
                    Service: gblInfo.Service;
                    DateInspection: gblInfo.DateInspection
                })};
        If(CountRows(nouv) > 0; Patch(INS_Reponses; ForAll(nouv; Defaults(INS_Reponses)); nouv))
    );;
    ClearCollect(colSaved; Filter(INS_Reponses; InspectionID = gblInspID));;
    ClearCollect(
        colReponses;
        ForAll(
            nfItems As it;
            With({s: LookUp(colSaved; ItemID = it.Cle)};
                {LigneID: Coalesce(s.ID; 0); Cle: it.Cle; SectionNo: it.SectionNo; Element: it.Element; EstAutre: false; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
            )
        )
    );;
    Collect(
        colReponses;
        ForAll(
            Sort(Filter(colSaved; SectionNo = 21); ID) As s;
            {LigneID: s.ID; Cle: s.ItemID; SectionNo: 21; Element: s.Title; EstAutre: true; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
        )
    );;
    Set(gblModifie; false);;
    Set(gblAvertiQuitter; false);;
    Notify("Inspection enregistrée dans SharePoint."; NotificationType.Success)
)
```
- **Fill** :
```
=ColorValue("#16a34a")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#16a34a"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1200, Y=10, Largeur=150, Hauteur=36

### recOnglets_Res  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngInsp_Res  (Classic/Button)

- **Text** :
```
="Inspection"
```
- **OnSelect** :
```
=Navigate(scrInspection; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrInspection"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrInspection"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=16, Y=62, Largeur=210, Hauteur=36

### btnOngResume_Res  (Classic/Button)

- **Text** :
```
="Résumé et envoi"
```
- **OnSelect** :
```
=Navigate(scrResume; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrResume"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrResume"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=234, Y=62, Largeur=210, Hauteur=36

### btnOngSuivi_Res  (Classic/Button)

- **Text** :
```
="Suivi des correctifs"
```
- **OnSelect** :
```
=Navigate(scrSuivi; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSuivi"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSuivi"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=452, Y=62, Largeur=210, Hauteur=36

### lblCRepondus  (Label)

- **Text** :
```
=With({a: CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA)); r: CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && !IsBlank(Reponse))}; r & "/" & a & Char(10) & "éléments répondus")
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#1e293b")
```
- **Align** :
```
=Align.Center
```
- Position : X=16, Y=112, Largeur=324, Hauteur=66

### lblCNC  (Label)

- **Text** :
```
=CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N") & Char(10) & "non-conformités"
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#dc2626")
```
- **Align** :
```
=Align.Center
```
- Position : X=348, Y=112, Largeur=324, Hauteur=66

### lblCGravE  (Label)

- **Text** :
```
=CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N" && Gravite = "E") & Char(10) & "gravité élevée (E)"
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#ea580c")
```
- **Align** :
```
=Align.Center
```
- Position : X=680, Y=112, Largeur=324, Hauteur=66

### lblCOuverts  (Label)

- **Text** :
```
=CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N" && Statut <> "Réalisé") & Char(10) & "correctifs à réaliser"
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#2563eb")
```
- **Align** :
```
=Align.Center
```
- Position : X=1012, Y=112, Largeur=324, Hauteur=66

### lblValidation  (Label)

- **Text** :
```
=With({a: CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA)); r: CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && !IsBlank(Reponse)); sg: CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N" && IsBlank(Gravite))}; With({msg: If(IsBlank(gblInfo.Endroit) || IsBlank(gblInfo.Service) || IsBlank(gblInfo.Inspecteur); "Renseignements incomplets (endroit, service, inspecteur). "; "") & If(r < a; (a - r) & " élément(s) applicable(s) sans réponse. "; "") & If(sg > 0; sg & " non-conformité(s) sans potentiel de gravité. "; "") & If(IsBlank(gblSignature); "Signature non validée."; "")}; If(IsBlank(msg); "✔ Inspection complète."; "⚠ " & msg)))
```
- **Size** :
```
=10
```
- **Color** :
```
=If(StartsWith(Self.Text; "✔"); ColorValue("#16a34a"); ColorValue("#b45309"))
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=184, Largeur=1334, Hauteur=34

### recNCEntetes  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=16, Y=222, Largeur=1334, Hauteur=28

### lblNCH1  (Label)

- **Text** :
```
="Sujet — Élément"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=24, Y=222, Largeur=380, Hauteur=28

### lblNCH2  (Label)

- **Text** :
```
="Grav."
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=404, Y=222, Largeur=60, Hauteur=28

### lblNCH3  (Label)

- **Text** :
```
="Correctif / commentaire (emplacement)"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=462, Y=222, Largeur=330, Hauteur=28

### lblNCH4  (Label)

- **Text** :
```
="Responsable"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=800, Y=222, Largeur=180, Hauteur=28

### lblNCH5  (Label)

- **Text** :
```
="Échéance"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=988, Y=222, Largeur=160, Hauteur=28

### lblNCH6  (Label)

- **Text** :
```
="Statut"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=1156, Y=222, Largeur=150, Hauteur=28

### lblAucuneNC  (Label)

- **Text** :
```
="Aucune non-conformité."
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#64748b")
```
- **Visible** :
```
=CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N") = 0
```
- Position : X=24, Y=256, Largeur=800, Hauteur=40

### galNC  (Gallery)

- **Items** :
```
=Sort(Filter(colReponses; Reponse = "N" && !(("|" & SectionNo & "|") in gblNA)); If(Gravite = "E"; 0; 1))
```
- **TemplateSize** :
```
=64
```
- **TemplatePadding** :
```
=0
```
- **ShowScrollbar** :
```
=true
```
- Position : X=16, Y=252, Largeur=1334, Hauteur=308

### lblNCElement  (Label)  — dans galNC

- **Text** :
```
=LookUp(nfSections; Numero = ThisItem.SectionNo).Titre & " — " & ThisItem.Element
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#1f2937")
```
- Position : X=8, Y=4, Largeur=380, Hauteur=56

### lblNCGravite  (Label)  — dans galNC

- **Text** :
```
=Coalesce(ThisItem.Gravite; "—")
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=Switch(ThisItem.Gravite; "E"; ColorValue("#dc2626"); "F"; ColorValue("#ea580c"); ColorValue("#94a3b8"))
```
- **Align** :
```
=Align.Center
```
- Position : X=394, Y=16, Largeur=44, Hauteur=32

### lblNCCorrectif  (Label)  — dans galNC

- **Text** :
```
=ThisItem.Commentaire & If(IsBlank(ThisItem.Emplacement); ""; " (" & ThisItem.Emplacement & ")")
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#334155")
```
- Position : X=446, Y=4, Largeur=330, Hauteur=56

### txtNCResp  (Classic/TextInput)  — dans galNC

- **Default** :
```
=ThisItem.Responsable
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Responsable; Patch(colReponses; LookUp(colReponses; Cle = ThisItem.Cle); {Responsable: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Responsable"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=784, Y=14, Largeur=180, Hauteur=36

### dpNCEch  (Classic/DatePicker)  — dans galNC

- **DefaultDate** :
```
=ThisItem.Echeance
```
- **Format** :
```
="yyyy-mm-dd"
```
- **Size** :
```
=9
```
- **BorderColor** :
```
=If(!IsBlank(ThisItem.Echeance) && ThisItem.Echeance < Today() && ThisItem.Statut <> "Réalisé"; ColorValue("#dc2626"); ColorValue("#cbd5e1"))
```
- **OnChange** :
```
=If(Self.SelectedDate <> ThisItem.Echeance; Patch(colReponses; LookUp(colReponses; Cle = ThisItem.Cle); {Echeance: Self.SelectedDate});; Set(gblModifie; true))
```
- Position : X=972, Y=14, Largeur=160, Hauteur=36

### ddNCStatut  (Classic/DropDown)  — dans galNC

- **Items** :
```
=["À faire"; "En cours"; "Réalisé"]
```
- **Default** :
```
=Coalesce(ThisItem.Statut; "À faire")
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.Statut; Patch(colReponses; LookUp(colReponses; Cle = ThisItem.Cle); {Statut: Self.Selected.Value; DateRealise: If(Self.Selected.Value = "Réalisé"; Today(); Blank())});; Set(gblModifie; true))
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=1140, Y=14, Largeur=150, Hauteur=36

### recNCSep  (Rectangle)  — dans galNC

- **Y** :
```
=Parent.TemplateHeight - 1
```
- **Width** :
```
=Parent.TemplateWidth
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=Parent.TemplateHeight - 1, Largeur=Parent.TemplateWidth, Hauteur=1

### lblSignature  (Label)

- **Text** :
```
="Signature de l'inspecteur (souris, doigt ou stylet) — insérer le contrôle penSignature ici"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#334155")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=568, Largeur=600, Hauteur=24

### recCadreSignature  (Rectangle)

- **Fill** :
```
=ColorValue("#f8fafc")
```
- **BorderColor** :
```
=ColorValue("#94a3b8")
```
- **BorderThickness** :
```
=1
```
- Position : X=16, Y=594, Largeur=420, Hauteur=140

### btnValiderSignature  (Classic/Button)

- **Text** :
```
="Valider la signature"
```
- **OnSelect** :
```
=Set(gblSignature; Substitute(JSON(penSignature.Image; JSONFormat.IncludeBinaryData); Char(34); ""));; Set(gblModifie; true);; Notify("Signature validée — pensez à enregistrer."; NotificationType.Success)
```
- **Fill** :
```
=ColorValue("#2563eb")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#2563eb"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=444, Y=594, Largeur=180, Hauteur=40

### btnEffacerSignature  (Classic/Button)

- **Text** :
```
="Effacer la signature"
```
- **OnSelect** :
```
=Reset(penSignature);; Set(gblSignature; "");; Set(gblModifie; true)
```
- **Fill** :
```
=ColorValue("#64748b")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#64748b"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=444, Y=642, Largeur=180, Hauteur=40

### lblSigEnreg  (Label)

- **Text** :
```
=If(IsBlank(gblSignature); "Aucune signature validée"; "Signature validée :")
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#64748b")
```
- Position : X=640, Y=568, Largeur=360, Hauteur=24

### imgSignature  (Image)

- **Image** :
```
=gblSignature
```
- **ImagePosition** :
```
=ImagePosition.Fit
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- **BorderThickness** :
```
=1
```
- Position : X=640, Y=594, Largeur=360, Hauteur=140

### btnEnvoyer  (Classic/Button)

- **Text** :
```
="Envoyer (PDF + Excel + courriel)"
```
- **OnSelect** :
```
=If(
    IsBlank(gblInspID) || gblModifie;
    Notify("Enregistrez d'abord l'inspection (bouton « Enregistrer ») avant de l'envoyer."; NotificationType.Warning);
    With(
        {nom: "Inspection_" & Substitute(Substitute(Substitute(Trim(gblInfo.Endroit); " "; "_"); "/"; "-"); "\"; "-") & "_" & Text(gblInfo.DateInspection; "yyyy-mm-dd")};
        Notify("Envoi en cours…"; NotificationType.Information);;
        IfError(
            INSExporterInspection.Run(
                nom;
                "<html><head><meta charset='utf-8'><title>Inspection du milieu de travail</title></head><body style='font-family:Segoe UI,Arial,sans-serif;font-size:9px;color:#1f2937'><h1 style='font-size:16px;color:#1e293b;margin:0'>Liste de vérification / inspection du milieu de travail</h1><p style='margin:0 0 8px 0;color:#64748b'>Bâtiments, cours et accès — Division santé et sécurité au travail, Ville de Québec</p><table style='border-collapse:collapse;width:100%;font-size:10px'><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Endroit</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & gblInfo.Endroit & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Service</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & gblInfo.Service & "</td>" & "</tr><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Inspection réalisée par</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & gblInfo.Inspecteur & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Date</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Text(gblInfo.DateInspection; "yyyy-mm-dd") & "</td>" & "</tr><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Participants</b>" & "</td>" & "<td colspan='3' style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & gblInfo.Participants & "</td></tr></table><p style='font-size:11px'><b>" & CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N") & "</b> non-conformité(s), dont <b>" & CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N" && Gravite = "E") & "</b> à gravité élevée · <b>" & CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N" && Statut <> "Réalisé") & "</b> correctif(s) à réaliser</p><h2 style='font-size:12px;color:#1e293b;border-bottom:2px solid #2563eb'>Non-conformités et correctifs</h2><table style='border-collapse:collapse;width:100%'><tr><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Sujet</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Élément</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Gravité</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Correctif / commentaire</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Emplacement</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Responsable</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Échéance</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Statut</th></tr>" & If(CountIf(colReponses; !(("|" & SectionNo & "|") in gblNA) && Reponse = "N") = 0; "<tr><td colspan='8' style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>Aucune non-conformité.</td></tr>"; Concat(Sort(Filter(colReponses; Reponse = "N" && !(("|" & SectionNo & "|") in gblNA)); If(Gravite = "E"; 0; 1)) As r; "<tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & LookUp(nfSections; Numero = r.SectionNo).Titre & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Element & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Gravite & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Commentaire & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Emplacement & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Responsable & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Text(r.Echeance; "yyyy-mm-dd") & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Statut & "</td>" & "</tr>")) & "</table><h2 style='font-size:12px;color:#1e293b;border-bottom:2px solid #2563eb'>Liste de vérification</h2><table style='border-collapse:collapse;width:100%'><tr><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Élément</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Oui</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Non</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>N/A</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Correctifs / commentaires</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Responsable / échéance / statut</th></tr>" & Concat(nfSections As sec; "<tr><td colspan='6' style='background:#e2e8f0;padding:4px'><b>" & sec.Numero & ". " & sec.Titre & "</b>" & If((("|" & sec.Numero & "|") in gblNA); " — Non applicable"; "") & "</td></tr>" & If((("|" & sec.Numero & "|") in gblNA); ""; Concat(Filter(colReponses; SectionNo = sec.Numero) As r; "<tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Element & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top;text-align:center'>" & If(r.Reponse = "O"; "X"; "") & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top;text-align:center;color:#dc2626;font-weight:bold'>" & If(r.Reponse = "N"; "X"; "") & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top;text-align:center'>" & If(r.Reponse = "NA"; "X"; "") & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & r.Commentaire & If(IsBlank(r.Emplacement); ""; "<br>Emplacement : " & r.Emplacement) & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & If(r.Reponse = "N"; r.Responsable & If(IsBlank(r.Echeance); ""; "<br>" & Text(r.Echeance; "yyyy-mm-dd")) & "<br>Statut : " & r.Statut & If(IsBlank(r.Gravite); ""; " · Gravité " & r.Gravite); "") & "</td>" & "</tr>"))) & "</table><h2 style='font-size:12px;color:#1e293b;border-bottom:2px solid #2563eb'>Signature de l'inspecteur</h2>" & If(IsBlank(gblSignature); "<p>(non signée)</p>"; "<img src='" & gblSignature & "' style='height:90px'>") & "<p>" & gblInfo.Inspecteur & " — " & Text(gblInfo.DateInspection; "yyyy-mm-dd") & "</p></body></html>";
                UniChar(65279) & "Endroit;" & Char(34) & Substitute(gblInfo.Endroit; Char(34); "'") & Char(34) & Char(13) & Char(10) & "Service;" & Char(34) & Substitute(gblInfo.Service; Char(34); "'") & Char(34) & Char(13) & Char(10) & "Inspecteur;" & Char(34) & Substitute(gblInfo.Inspecteur; Char(34); "'") & Char(34) & Char(13) & Char(10) & "Date;" & Text(gblInfo.DateInspection; "yyyy-mm-dd") & Char(13) & Char(10) & Char(13) & Char(10) & "No sujet;Sujet;Applicable;Élément;Réponse;Gravité;Correctif / commentaire;Emplacement;Responsable;Échéance;Statut;Date réalisé" & Char(13) & Char(10) & Concat(colReponses As r; r.SectionNo & ";" & Char(34) & Substitute(LookUp(nfSections; Numero = r.SectionNo).Titre; Char(34); "'") & Char(34) & ";" & If((("|" & r.SectionNo & "|") in gblNA); "Non"; "Oui") & ";" & Char(34) & Substitute(r.Element; Char(34); "'") & Char(34) & ";" & Switch(r.Reponse; "O"; "Oui"; "N"; "Non"; "NA"; "N/A"; "") & ";" & r.Gravite & ";" & Char(34) & Substitute(r.Commentaire; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(r.Emplacement; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(r.Responsable; Char(34); "'") & Char(34) & ";" & Text(r.Echeance; "yyyy-mm-dd") & ";" & r.Statut & ";" & Text(r.DateRealise; "yyyy-mm-dd") & Char(13) & Char(10))
            );;
            Notify("PDF et fichier Excel (CSV) déposés dans « Inspections complétées », courriel envoyé."; NotificationType.Success);
            Notify("L'envoi a échoué : " & FirstError.Message; NotificationType.Error)
        )
    )
)
```
- **Fill** :
```
=ColorValue("#2563eb")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#2563eb"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1040, Y=594, Largeur=310, Hauteur=44

### btnImprimer  (Classic/Button)

- **Text** :
```
="Imprimer cet écran"
```
- **OnSelect** :
```
=Print()
```
- **Fill** :
```
=ColorValue("#475569")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#475569"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1040, Y=646, Largeur=310, Hauteur=40

### lblAideEnvoi  (Label)

- **Text** :
```
="L'envoi dépose le PDF et le CSV (Excel) dans « Inspections complétées » et envoie le PDF par courriel."
```
- **Size** :
```
=8
```
- **Color** :
```
=ColorValue("#64748b")
```
- Position : X=1040, Y=690, Largeur=310, Hauteur=60

## Écran scrSuivi (fichier 4_scrSuivi.yaml)


### recBarre_Sui  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Sui  (Label)

- **Text** :
```
="Suivi des correctifs (toutes inspections)"
```
- **Size** :
```
=16
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=520, Hauteur=56

### btnAccueil_Sui  (Classic/Button)

- **Text** :
```
="Accueil"
```
- **OnSelect** :
```
=Navigate(scrAccueil; ScreenTransition.None)
```
- **Fill** :
```
=ColorValue("#475569")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#475569"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=1230, Y=10, Largeur=120, Hauteur=36

### recOnglets_Sui  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngInsp_Sui  (Classic/Button)

- **Text** :
```
="Inspection"
```
- **OnSelect** :
```
=Navigate(scrInspection; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrInspection"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrInspection"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=16, Y=62, Largeur=210, Hauteur=36

### btnOngResume_Sui  (Classic/Button)

- **Text** :
```
="Résumé et envoi"
```
- **OnSelect** :
```
=Navigate(scrResume; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrResume"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrResume"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=234, Y=62, Largeur=210, Hauteur=36

### btnOngSuivi_Sui  (Classic/Button)

- **Text** :
```
="Suivi des correctifs"
```
- **OnSelect** :
```
=Navigate(scrSuivi; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSuivi"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSuivi"; ColorValue("#ffffff"); ColorValue("#1e293b"))
```
- **HoverFill** :
```
=ColorValue("#bfdbfe")
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=452, Y=62, Largeur=210, Hauteur=36

### lblSuiInsp  (Label)

- **Text** :
```
=CountRows(INS_Inspections) & Char(10) & "inspections"
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#1e293b")
```
- **Align** :
```
=Align.Center
```
- Position : X=16, Y=112, Largeur=324, Hauteur=66

### lblSuiNC  (Label)

- **Text** :
```
=CountRows(Filter(INS_Reponses; Reponse = "N" && Applicable = "Oui")) & Char(10) & "non-conformités"
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#dc2626")
```
- **Align** :
```
=Align.Center
```
- Position : X=348, Y=112, Largeur=324, Hauteur=66

### lblSuiOuverts  (Label)

- **Text** :
```
=CountRows(Filter(INS_Reponses; Reponse = "N" && Applicable = "Oui" && StatutCorrectif <> "Réalisé")) & Char(10) & "correctifs à réaliser"
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#2563eb")
```
- **Align** :
```
=Align.Center
```
- Position : X=680, Y=112, Largeur=324, Hauteur=66

### lblSuiRetard  (Label)

- **Text** :
```
=CountRows(Filter(INS_Reponses; Reponse = "N" && Applicable = "Oui" && StatutCorrectif <> "Réalisé" && Echeance < Today())) & Char(10) & "correctifs en retard"
```
- **Size** :
```
=13
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#b91c1c")
```
- **Align** :
```
=Align.Center
```
- Position : X=1012, Y=112, Largeur=324, Hauteur=66

### txtSuiviRech  (Classic/TextInput)

- **Default** :
```
=""
```
- **OnChange** :
```
=false
```
- **HintText** :
```
="Rechercher (début de l'endroit ou du responsable)…"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=16, Y=186, Largeur=420, Hauteur=36

### btnVoirRealises  (Classic/Button)

- **Text** :
```
=If(gblVoirRealises; "☑ Afficher aussi les correctifs réalisés"; "☐ Afficher aussi les correctifs réalisés")
```
- **OnSelect** :
```
=Set(gblVoirRealises; !gblVoirRealises)
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- **Color** :
```
=ColorValue("#1e293b")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#e2e8f0"); -15%)
```
- **Size** :
```
=9
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=444, Y=186, Largeur=300, Hauteur=36

### btnActualiserSuivi  (Classic/Button)

- **Text** :
```
="Actualiser"
```
- **OnSelect** :
```
=Refresh(INS_Reponses);; Refresh(INS_Inspections)
```
- **Fill** :
```
=ColorValue("#475569")
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **HoverFill** :
```
=ColorFade(ColorValue("#475569"); -15%)
```
- **Size** :
```
=11
```
- **BorderThickness** :
```
=0
```
- **RadiusTopLeft** :
```
=4
```
- **RadiusTopRight** :
```
=4
```
- **RadiusBottomLeft** :
```
=4
```
- **RadiusBottomRight** :
```
=4
```
- Position : X=752, Y=186, Largeur=140, Hauteur=36

### lblSuiAide  (Label)

- **Text** :
```
="Modifications enregistrées immédiatement · retards en rouge · cliquez sur l'endroit pour ouvrir l'inspection."
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#64748b")
```
- Position : X=900, Y=186, Largeur=450, Hauteur=36

### recSEntetes  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=16, Y=228, Largeur=1334, Hauteur=28

### lblSH1  (Label)

- **Text** :
```
="Endroit / service / date"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=24, Y=228, Largeur=250, Hauteur=28

### lblSH2  (Label)

- **Text** :
```
="Sujet — Élément"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=280, Y=228, Largeur=300, Hauteur=28

### lblSH3  (Label)

- **Text** :
```
="Grav."
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=582, Y=228, Largeur=50, Hauteur=28

### lblSH4  (Label)

- **Text** :
```
="Correctif"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=632, Y=228, Largeur=250, Hauteur=28

### lblSH5  (Label)

- **Text** :
```
="Responsable"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=898, Y=228, Largeur=160, Hauteur=28

### lblSH6  (Label)

- **Text** :
```
="Échéance"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=1064, Y=228, Largeur=150, Hauteur=28

### lblSH7  (Label)

- **Text** :
```
="Statut"
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=1220, Y=228, Largeur=120, Hauteur=28

### galSuivi  (Gallery)

- **Items** :
```
=Sort(Filter(INS_Reponses; Reponse = "N" && Applicable = "Oui" && (gblVoirRealises || StatutCorrectif <> "Réalisé") && (IsBlank(txtSuiviRech.Text) || StartsWith(Endroit; txtSuiviRech.Text) || StartsWith(Responsable; txtSuiviRech.Text))); Echeance; SortOrder.Ascending)
```
- **TemplateSize** :
```
=70
```
- **TemplatePadding** :
```
=0
```
- **ShowScrollbar** :
```
=true
```
- **OnSelect** :
```
=With({i: LookUp(INS_Inspections; ID = ThisItem.InspectionID)};
    Set(gblInspID; i.ID);;
    Set(gblInspCle; Coalesce(i.IdInspection; Text(GUID())));;
    Set(gblInfo; {Endroit: i.Title; Service: i.Service; Inspecteur: i.Inspecteur; DateInspection: Coalesce(i.DateInspection; Today()); Participants: i.Participants});;
    Set(gblNA; Coalesce(i.SectionsNA; ""));;
    Set(gblSignature; Coalesce(i.Signature; ""))
);;
ClearCollect(colSaved; Filter(INS_Reponses; InspectionID = gblInspID));;
ClearCollect(
    colReponses;
    ForAll(
        nfItems As it;
        With({s: LookUp(colSaved; ItemID = it.Cle)};
            {LigneID: Coalesce(s.ID; 0); Cle: it.Cle; SectionNo: it.SectionNo; Element: it.Element; EstAutre: false; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
        )
    )
);;
Collect(
    colReponses;
    ForAll(
        Sort(Filter(colSaved; SectionNo = 21); ID) As s;
        {LigneID: s.ID; Cle: s.ItemID; SectionNo: 21; Element: s.Title; EstAutre: true; Reponse: s.Reponse; Gravite: s.Gravite; Commentaire: s.Commentaire; Emplacement: s.Emplacement; Responsable: s.Responsable; Echeance: s.Echeance; Statut: s.StatutCorrectif; DateRealise: s.DateRealise}
    )
);;
Clear(colSupprimes);;
Set(gblSection; 1);;
Set(gblDetail; "");;
Set(gblModifie; false);;
Set(gblAvertiQuitter; false);;
Navigate(scrInspection; ScreenTransition.None)
```
- Position : X=16, Y=258, Largeur=1334, Hauteur=500

### lblSEndroit  (Label)  — dans galSuivi

- **Text** :
```
=ThisItem.Endroit & Char(10) & ThisItem.Service & "  ·  " & Text(ThisItem.DateInspection; "yyyy-mm-dd")
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#1f2937")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=8, Y=4, Largeur=250, Hauteur=60

### lblSElement  (Label)  — dans galSuivi

- **Text** :
```
=ThisItem.Sujet & " — " & ThisItem.Title
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#1f2937")
```
- Position : X=264, Y=4, Largeur=300, Hauteur=60

### lblSGravite  (Label)  — dans galSuivi

- **Text** :
```
=Coalesce(ThisItem.Gravite; "—")
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=Switch(ThisItem.Gravite; "E"; ColorValue("#dc2626"); "F"; ColorValue("#ea580c"); ColorValue("#94a3b8"))
```
- **Align** :
```
=Align.Center
```
- Position : X=570, Y=18, Largeur=40, Hauteur=32

### lblSCorrectif  (Label)  — dans galSuivi

- **Text** :
```
=ThisItem.Commentaire & If(IsBlank(ThisItem.Emplacement); ""; " (" & ThisItem.Emplacement & ")")
```
- **Size** :
```
=9
```
- **Color** :
```
=ColorValue("#334155")
```
- Position : X=616, Y=4, Largeur=260, Hauteur=60

### txtSResp  (Classic/TextInput)  — dans galSuivi

- **Default** :
```
=ThisItem.Responsable
```
- **OnChange** :
```
=If(Self.Text <> Coalesce(ThisItem.Responsable; "");
    With({x: ThisItem.InspectionID};
        Patch(INS_Reponses; ThisItem; {Responsable: Self.Text});;
        With({lst: Filter(INS_Reponses; InspectionID = x && Reponse = "N" && Applicable = "Oui")};
        Patch(
            INS_Inspections;
            LookUp(INS_Inspections; ID = x);
            {
                CorrectifsOuverts: CountIf(lst; StatutCorrectif <> "Réalisé");
                ProchaineEcheance: Min(Filter(lst; StatutCorrectif <> "Réalisé" && !IsBlank(Echeance)); Echeance);
                StatutSuivi: If(
                    CountRows(lst) = 0; "Aucun correctif";
                    CountIf(lst; StatutCorrectif <> "Réalisé") = 0; "Fermé";
                    CountIf(lst; StatutCorrectif = "En cours" || StatutCorrectif = "Réalisé") > 0; "En cours";
                    "Ouvert"
                )
            }
        )
    );;
        Notify("Correctif mis à jour."; NotificationType.Success)
    )
)
```
- **HintText** :
```
="Responsable"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=882, Y=16, Largeur=160, Hauteur=36

### dpSEch  (Classic/DatePicker)  — dans galSuivi

- **DefaultDate** :
```
=ThisItem.Echeance
```
- **Format** :
```
="yyyy-mm-dd"
```
- **Size** :
```
=9
```
- **BorderColor** :
```
=If(!IsBlank(ThisItem.Echeance) && ThisItem.Echeance < Today() && ThisItem.StatutCorrectif <> "Réalisé"; ColorValue("#dc2626"); ColorValue("#cbd5e1"))
```
- **BorderThickness** :
```
=2
```
- **OnChange** :
```
=If(Self.SelectedDate <> ThisItem.Echeance;
    With({x: ThisItem.InspectionID};
        Patch(INS_Reponses; ThisItem; {Echeance: Self.SelectedDate});;
        With({lst: Filter(INS_Reponses; InspectionID = x && Reponse = "N" && Applicable = "Oui")};
        Patch(
            INS_Inspections;
            LookUp(INS_Inspections; ID = x);
            {
                CorrectifsOuverts: CountIf(lst; StatutCorrectif <> "Réalisé");
                ProchaineEcheance: Min(Filter(lst; StatutCorrectif <> "Réalisé" && !IsBlank(Echeance)); Echeance);
                StatutSuivi: If(
                    CountRows(lst) = 0; "Aucun correctif";
                    CountIf(lst; StatutCorrectif <> "Réalisé") = 0; "Fermé";
                    CountIf(lst; StatutCorrectif = "En cours" || StatutCorrectif = "Réalisé") > 0; "En cours";
                    "Ouvert"
                )
            }
        )
    );;
        Notify("Correctif mis à jour."; NotificationType.Success)
    )
)
```
- Position : X=1048, Y=16, Largeur=150, Hauteur=36

### ddSStatut  (Classic/DropDown)  — dans galSuivi

- **Items** :
```
=["À faire"; "En cours"; "Réalisé"]
```
- **Default** :
```
=Coalesce(ThisItem.StatutCorrectif; "À faire")
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.StatutCorrectif;
    With({x: ThisItem.InspectionID};
        Patch(INS_Reponses; ThisItem; {StatutCorrectif: Self.Selected.Value; DateRealise: If(Self.Selected.Value = "Réalisé"; Today(); Blank())});;
        With({lst: Filter(INS_Reponses; InspectionID = x && Reponse = "N" && Applicable = "Oui")};
        Patch(
            INS_Inspections;
            LookUp(INS_Inspections; ID = x);
            {
                CorrectifsOuverts: CountIf(lst; StatutCorrectif <> "Réalisé");
                ProchaineEcheance: Min(Filter(lst; StatutCorrectif <> "Réalisé" && !IsBlank(Echeance)); Echeance);
                StatutSuivi: If(
                    CountRows(lst) = 0; "Aucun correctif";
                    CountIf(lst; StatutCorrectif <> "Réalisé") = 0; "Fermé";
                    CountIf(lst; StatutCorrectif = "En cours" || StatutCorrectif = "Réalisé") > 0; "En cours";
                    "Ouvert"
                )
            }
        )
    );;
        Notify("Correctif mis à jour."; NotificationType.Success)
    )
)
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=1204, Y=16, Largeur=112, Hauteur=36

### recSSep  (Rectangle)  — dans galSuivi

- **Y** :
```
=Parent.TemplateHeight - 1
```
- **Width** :
```
=Parent.TemplateWidth
```
- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=Parent.TemplateHeight - 1, Largeur=Parent.TemplateWidth, Hauteur=1