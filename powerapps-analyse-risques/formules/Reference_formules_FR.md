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
="Analyses de risques SST — DSST"
```
- **Size** :
```
=17
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=700, Hauteur=56

### btnNouvelleAnalyse  (Classic/Button)

- **Text** :
```
="+ Nouvelle analyse"
```
- **OnSelect** :
```
=Set(gblAnalyseID; Blank());;
Set(gblMeta; {Service: ""; Division: ""; Localisation: ""; Participants: ""; DateAnalyse: Today(); Commentaires: ""});;
Clear(colLignes);;
Clear(colSupprimes);;
Set(gblModifie; false);;
Set(gblAvertiQuitter; false);;
Navigate(scrAnalyse; ScreenTransition.None)
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
- Position : X=1004, Y=10, Largeur=180, Hauteur=36

### btnAllerImport  (Classic/Button)

- **Text** :
```
="Importer un JSON"
```
- **OnSelect** :
```
=Navigate(scrImport; ScreenTransition.None)
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
- Position : X=1192, Y=10, Largeur=158, Hauteur=36

### lblAccAide  (Label)

- **Text** :
```
="Cliquez sur une analyse pour l'ouvrir. Les analyses sont enregistrées dans la liste SharePoint AR_Analyses."
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
="Rechercher (début du service, de la division ou de la localisation)…"
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
=CountRows(galAnalyses.AllItems) & " analyse(s)"
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
="Service / Division · Localisation"
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
="Date / Résumé"
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

### galAnalyses  (Gallery)

- **Items** :
```
=Sort(Filter(AR_Analyses; IsBlank(txtRechAccueil.Text) || StartsWith(Title; txtRechAccueil.Text) || StartsWith(Division; txtRechAccueil.Text) || StartsWith(Localisation; txtRechAccueil.Text)); DateAnalyse; SortOrder.Descending)
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
=Set(gblAnalyseID; ThisItem.ID);;
Set(gblMeta; {Service: ThisItem.Title; Division: ThisItem.Division; Localisation: ThisItem.Localisation; Participants: ThisItem.Participants; DateAnalyse: Coalesce(ThisItem.DateAnalyse; Today()); Commentaires: ThisItem.Commentaires});;
ClearCollect(
    colLignes;
    ForAll(
        Sort(Filter(AR_Lignes; AnalyseID = gblAnalyseID); Ordre);
        {
            LigneID: ThisRecord.ID;
            Cle: Coalesce(ThisRecord.Cle; Text(GUID()));
            Ordre: Coalesce(ThisRecord.Ordre; 0);
            Environnement: ThisRecord.Environnement;
            Activite: ThisRecord.Title;
            Tache: ThisRecord.Tache;
            CategorieDanger: ThisRecord.CategorieDanger;
            Risque: ThisRecord.Risque;
            Consequence: ThisRecord.Consequence;
            Blessure: ThisRecord.Blessure;
            MesuresExistantes: ThisRecord.MesuresExistantes;
            G1: Coalesce(ThisRecord.G1; 0);
            MP1: Coalesce(ThisRecord.MP1; 0);
            MesuresSuggerees: ThisRecord.MesuresSuggerees;
            Cout: ThisRecord.Cout;
            G2: Coalesce(ThisRecord.G2; 0);
            MP2: Coalesce(ThisRecord.MP2; 0)
        }
    )
);;
Clear(colSupprimes);;
Set(gblModifie; false);;
Set(gblAvertiQuitter; false);;
Navigate(scrAnalyse; ScreenTransition.None)
```
- **ShowScrollbar** :
```
=true
```
- Position : X=16, Y=172, Largeur=1334, Hauteur=586

### lblAccService  (Label)  — dans galAnalyses

- **Text** :
```
=Coalesce(ThisItem.Title; "(sans service)")
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

### lblAccDivision  (Label)  — dans galAnalyses

- **Text** :
```
=ThisItem.Division & If(IsBlank(ThisItem.Localisation); ""; "  ·  " & ThisItem.Localisation)
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

### lblAccDate  (Label)  — dans galAnalyses

- **Text** :
```
=Text(ThisItem.DateAnalyse; "yyyy-mm-dd")
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

### lblAccStats  (Label)  — dans galAnalyses

- **Text** :
```
=Coalesce(ThisItem.NbRisques; 0) & " risque(s)  ·  " & Coalesce(ThisItem.NbCritiques; 0) & " critique(s)  ·  " & Coalesce(ThisItem.NbEleves; 0) & " élevé(s)  ·  IR max " & Coalesce(ThisItem.IRMax; 0)
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

### lblAccStatut  (Label)  — dans galAnalyses

- **Text** :
```
=Coalesce(ThisItem.Statut; "Enregistrée")
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
=If(ThisItem.Statut = "Envoyée"; ColorValue("#16a34a"); ColorValue("#2563eb"))
```
- **Align** :
```
=Align.Center
```
- Position : X=1080, Y=20, Largeur=150, Hauteur=32

### icoAccSupprimer  (Classic/Icon)  — dans galAnalyses

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
="Supprimer cette analyse"
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

### recAccSeparateur  (Rectangle)  — dans galAnalyses

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
="Supprimer définitivement l'analyse « " & gblASupprimer.Title & " » du " & Text(gblASupprimer.DateAnalyse; "yyyy-mm-dd") & " ainsi que toutes ses lignes ?"
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
=Remove(AR_Lignes; Filter(AR_Lignes; AnalyseID = gblASupprimer.ID));;
Remove(AR_Analyses; gblASupprimer);;
Set(gblASupprimer; Blank());;
Notify("Analyse supprimée."; NotificationType.Success)
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

## Écran scrAnalyse (fichier 2_scrAnalyse.yaml)


### recBarre_Ana  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Ana  (Label)

- **Text** :
```
="Grille d'analyse de risques SST"
```
- **Size** :
```
=17
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=400, Hauteur=56

### lblEtat_Ana  (Label)

- **Text** :
```
=If(gblModifie; "● Modifications non enregistrées"; If(IsBlank(gblAnalyseID); "Nouvelle analyse"; "✔ Enregistrée dans SharePoint"))
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
- Position : X=420, Y=0, Largeur=360, Hauteur=56

### btnAccueil  (Classic/Button)

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
- Position : X=790, Y=10, Largeur=110, Hauteur=36

### btnEnregistrer  (Classic/Button)

- **Text** :
```
="Enregistrer"
```
- **OnSelect** :
```
=If(
    IsBlank(Trim(gblMeta.Service));
    Notify("Le champ « Service » est obligatoire avant d'enregistrer."; NotificationType.Error);
    Set(
        gblEnreg;
        Patch(
            AR_Analyses;
            If(IsBlank(gblAnalyseID); Defaults(AR_Analyses); LookUp(AR_Analyses; ID = gblAnalyseID));
            {
                Title: gblMeta.Service;
                Division: gblMeta.Division;
                Localisation: gblMeta.Localisation;
                Participants: gblMeta.Participants;
                DateAnalyse: gblMeta.DateAnalyse;
                Commentaires: gblMeta.Commentaires;
                Statut: "Enregistrée";
                NbRisques: CountRows(colLignes);
                NbCritiques: CountIf(colLignes; G1 * MP1 > 1250);
                NbEleves: CountIf(colLignes; G1 * MP1 > 750 && G1 * MP1 <= 1250);
                NbModeres: CountIf(colLignes; G1 * MP1 > 250 && G1 * MP1 <= 750);
                NbFaibles: CountIf(colLignes; G1 * MP1 <= 250);
                IRMax: Coalesce(Max(colLignes; G1 * MP1); 0)
            }
        )
    );;
    Set(gblAnalyseID; gblEnreg.ID);;
    ForAll(colSupprimes As s; Remove(AR_Lignes; LookUp(AR_Lignes; ID = s.LigneID)));;
    Clear(colSupprimes);;
    ForAll(
        colLignes As l;
        Patch(
            AR_Lignes;
            If(l.LigneID = 0; Defaults(AR_Lignes); LookUp(AR_Lignes; ID = l.LigneID));
            {
                Title: l.Activite;
                AnalyseID: gblAnalyseID;
                Ordre: l.Ordre;
                Cle: l.Cle;
                Environnement: l.Environnement;
                Tache: l.Tache;
                CategorieDanger: l.CategorieDanger;
                Risque: l.Risque;
                Consequence: l.Consequence;
                Blessure: l.Blessure;
                MesuresExistantes: l.MesuresExistantes;
                G1: l.G1;
                MP1: l.MP1;
                MesuresSuggerees: l.MesuresSuggerees;
                Cout: l.Cout;
                G2: l.G2;
                MP2: l.MP2
            }
        )
    );;
    ClearCollect(
        colLignes;
        ForAll(
            Sort(Filter(AR_Lignes; AnalyseID = gblAnalyseID); Ordre);
            {
                LigneID: ThisRecord.ID;
                Cle: Coalesce(ThisRecord.Cle; Text(GUID()));
                Ordre: Coalesce(ThisRecord.Ordre; 0);
                Environnement: ThisRecord.Environnement;
                Activite: ThisRecord.Title;
                Tache: ThisRecord.Tache;
                CategorieDanger: ThisRecord.CategorieDanger;
                Risque: ThisRecord.Risque;
                Consequence: ThisRecord.Consequence;
                Blessure: ThisRecord.Blessure;
                MesuresExistantes: ThisRecord.MesuresExistantes;
                G1: Coalesce(ThisRecord.G1; 0);
                MP1: Coalesce(ThisRecord.MP1; 0);
                MesuresSuggerees: ThisRecord.MesuresSuggerees;
                Cout: ThisRecord.Cout;
                G2: Coalesce(ThisRecord.G2; 0);
                MP2: Coalesce(ThisRecord.MP2; 0)
            }
        )
    );;
    Set(gblModifie; false);;
    Set(gblAvertiQuitter; false);;
    Notify("Analyse enregistrée dans SharePoint (" & CountRows(colLignes) & " ligne(s))."; NotificationType.Success)
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
- Position : X=908, Y=10, Largeur=140, Hauteur=36

### btnEnvoyerSP  (Classic/Button)

- **Text** :
```
="Envoyer à SharePoint (PDF/Excel)"
```
- **OnSelect** :
```
=If(
    IsBlank(gblAnalyseID) || gblModifie;
    Notify("Enregistrez d'abord l'analyse (bouton « Enregistrer ») avant de l'envoyer."; NotificationType.Warning);
    With(
        {
            nom: "AR_SST_" & Substitute(Substitute(Substitute(Trim(gblMeta.Service); " "; "_"); "/"; "-"); "\"; "-") & "_" & Text(gblMeta.DateAnalyse; "yyyy-mm-dd");
            lignes: Sort(AddColumns(colLignes; IR1; G1 * MP1; IR2; G2 * MP2); Ordre)
        };
        Notify("Envoi vers SharePoint en cours…"; NotificationType.Information);;
        IfError(
            ARExporterAnalyse.Run(
                nom;
                "<html><head><meta charset='utf-8'><title>Analyse de risques SST</title></head><body style='font-family:Segoe UI,Arial,sans-serif;font-size:9px;color:#1f2937'><h1 style='font-size:18px;color:#1e293b;margin:0 0 4px 0'>Grille d'analyse de risques SST</h1><p style='margin:0 0 10px 0;color:#64748b'>Division de la santé et de la sécurité au travail — Ville de Québec</p><table style='border-collapse:collapse;width:100%;font-size:10px'><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Service</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & gblMeta.Service & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Division</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & gblMeta.Division & "</td>" & "</tr><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Localisation</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & gblMeta.Localisation & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Date</b>" & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Text(gblMeta.DateAnalyse; "yyyy-mm-dd") & "</td>" & "</tr><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Participants</b>" & "</td>" & "<td colspan='3' style='border:1px solid #cbd5e1;padding:3px'>" & gblMeta.Participants & "</td></tr><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & "<b>Commentaires</b>" & "</td>" & "<td colspan='3' style='border:1px solid #cbd5e1;padding:3px'>" & gblMeta.Commentaires & "</td></tr></table><h2 style='font-size:13px;color:#1e293b;border-bottom:2px solid #2563eb'>Synthèse</h2><table style='border-collapse:collapse;font-size:11px'><tr><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Total</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Critique</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Élevé</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Modéré</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Faible</th></tr><tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & CountRows(lignes) & "</td>" & Concat(Sort(nfNiveaux; Seuil; SortOrder.Descending) As n; "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & CountIf(lignes; IR1 > n.Plancher && IR1 <= n.Seuil) & "</td>") & "</tr></table><h2 style='font-size:13px;color:#1e293b;border-bottom:2px solid #2563eb'>Grille d'analyse</h2><table style='border-collapse:collapse;width:100%'><tr><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>#</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Env.</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Activité</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Tâches</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Catégorie</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Risques</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Conséquences</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Blessures / Maladie</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Mesures en place</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>G</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>MP</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Mesures suggérées</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Coûts</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>G</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>MP</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR rés.</th></tr>" & Concat(lignes; With({n1: LookUp(nfNiveaux; IR1 <= Seuil); n2: LookUp(nfNiveaux; IR2 <= Seuil)}; "<tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Ordre & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Environnement & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Activite & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Tache & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & CategorieDanger & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Risque & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Consequence & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Blessure & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & MesuresExistantes & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & G1 & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & MP1 & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;text-align:center;font-weight:bold;background:" & n1.Couleur & ";color:" & n1.Texte & "'>" & IR1 & "<br>" & n1.Libelle & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & MesuresSuggerees & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Cout & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & G2 & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & MP2 & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;text-align:center;font-weight:bold;background:" & n2.Couleur & ";color:" & n2.Texte & "'>" & IR2 & "<br>" & n2.Libelle & "</td>" & "</tr>")) & "</table><h2 style='font-size:13px;color:#1e293b;border-bottom:2px solid #2563eb'>Plan d'action (par IR décroissant)</h2><table style='border-collapse:collapse;width:100%'><tr><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'># ligne</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Env.</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Activité</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Risque</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Mesures suggérées</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Coûts</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR rés.</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Réduction</th></tr>" & Concat(Sort(lignes; IR1; SortOrder.Descending); With({n1: LookUp(nfNiveaux; IR1 <= Seuil); n2: LookUp(nfNiveaux; IR2 <= Seuil)}; "<tr>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Ordre & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Environnement & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Activite & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Risque & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;text-align:center;font-weight:bold;background:" & n1.Couleur & ";color:" & n1.Texte & "'>" & IR1 & "<br>" & n1.Libelle & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & MesuresSuggerees & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & Cout & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;text-align:center;font-weight:bold;background:" & n2.Couleur & ";color:" & n2.Texte & "'>" & IR2 & "<br>" & n2.Libelle & "</td>" & "<td style='border:1px solid #cbd5e1;padding:3px;vertical-align:top'>" & If(IR1 > 0; Round((1 - IR2 / IR1) * 100; 0) & " %"; "—") & "</td>" & "</tr>")) & "</table><p style='margin-top:12px;color:#64748b'>IR = G × MP · Faible ≤ 250 · Modéré 251–750 · Élevé 751–1250 · Critique > 1250</p></body></html>";
                UniChar(65279) & "Service;" & Char(34) & Substitute(gblMeta.Service; Char(34); "'") & Char(34) & Char(13) & Char(10) & "Division;" & Char(34) & Substitute(gblMeta.Division; Char(34); "'") & Char(34) & Char(13) & Char(10) & "Localisation;" & Char(34) & Substitute(gblMeta.Localisation; Char(34); "'") & Char(34) & Char(13) & Char(10) & "Participants;" & Char(34) & Substitute(gblMeta.Participants; Char(34); "'") & Char(34) & Char(13) & Char(10) & "Date;" & Text(gblMeta.DateAnalyse; "yyyy-mm-dd") & Char(13) & Char(10) & Char(13) & Char(10) & "No;Environnement;Activité de travail;Tâches;Catégorie de danger;Risques;Conséquences;Blessures / Maladie;Mesures préventives en place;G;MP;IR;Niveau;Mesures préventives suggérées;Coûts approx.;G résiduel;MP résiduel;IR résiduel;Niveau résiduel" & Char(13) & Char(10) & Concat(lignes; Ordre & ";" & Char(34) & Substitute(Environnement; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(Activite; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(Tache; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(CategorieDanger; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(Risque; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(Consequence; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(Blessure; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(MesuresExistantes; Char(34); "'") & Char(34) & ";" & G1 & ";" & MP1 & ";" & IR1 & ";" & LookUp(nfNiveaux; IR1 <= Seuil).Libelle & ";" & Char(34) & Substitute(MesuresSuggerees; Char(34); "'") & Char(34) & ";" & Char(34) & Substitute(Cout; Char(34); "'") & Char(34) & ";" & G2 & ";" & MP2 & ";" & IR2 & ";" & LookUp(nfNiveaux; IR2 <= Seuil).Libelle & Char(13) & Char(10));
                JSON(
                    {
                        version: "1.0";
                        meta: {service: gblMeta.Service; division: gblMeta.Division; localisation: gblMeta.Localisation; participants: gblMeta.Participants; date: Text(gblMeta.DateAnalyse; "yyyy-mm-dd"); commentaires: gblMeta.Commentaires};
                        rows: ForAll(lignes; {id: Cle; environnement: Environnement; activite: Activite; tache: Tache; categorie_danger: CategorieDanger; risque: Risque; consequence: Consequence; blessure: Blessure; mesures_existantes: MesuresExistantes; g1: G1; mp1: MP1; mesures_suggerees: MesuresSuggerees; cout: Cout; g2: G2; mp2: MP2})
                    };
                    JSONFormat.IndentFour
                )
            );;
            Patch(AR_Analyses; LookUp(AR_Analyses; ID = gblAnalyseID); {Statut: "Envoyée"});;
            Notify("Analyse envoyée : PDF, Excel (CSV) et JSON déposés dans SharePoint, courriel transmis."; NotificationType.Success);
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
- Position : X=1056, Y=10, Largeur=294, Hauteur=36

### recOnglets_Ana  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngGrille_Ana  (Classic/Button)

- **Text** :
```
="Grille d'analyse"
```
- **OnSelect** :
```
=Navigate(scrAnalyse; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=16, Y=62, Largeur=170, Hauteur=36

### btnOngMatrice_Ana  (Classic/Button)

- **Text** :
```
="Matrice de risque"
```
- **OnSelect** :
```
=Navigate(scrMatrice; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=194, Y=62, Largeur=170, Hauteur=36

### btnOngAide_Ana  (Classic/Button)

- **Text** :
```
="Aide-mémoire"
```
- **OnSelect** :
```
=Navigate(scrAideMemoire; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=372, Y=62, Largeur=170, Hauteur=36

### btnOngSynthese_Ana  (Classic/Button)

- **Text** :
```
="Synthèse"
```
- **OnSelect** :
```
=Navigate(scrSynthese; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=550, Y=62, Largeur=170, Hauteur=36

### btnOngPlan_Ana  (Classic/Button)

- **Text** :
```
="Plan d'action"
```
- **OnSelect** :
```
=Navigate(scrPlanAction; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=728, Y=62, Largeur=170, Hauteur=36

### lblM_Service  (Label)

- **Text** :
```
="Service *"
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
- Position : X=16, Y=110, Largeur=320, Hauteur=16

### txtService  (Classic/TextInput)

- **Default** :
```
=gblMeta.Service
```
- **OnChange** :
```
=If(Self.Text <> gblMeta.Service; Set(gblMeta; Patch(gblMeta; {Service: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Ex. : Maintenance"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=16, Y=126, Largeur=320, Hauteur=34

### lblM_Division  (Label)

- **Text** :
```
="Division"
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
- Position : X=344, Y=110, Largeur=320, Hauteur=16

### txtDivision  (Classic/TextInput)

- **Default** :
```
=gblMeta.Division
```
- **OnChange** :
```
=If(Self.Text <> gblMeta.Division; Set(gblMeta; Patch(gblMeta; {Division: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Ex. : Atelier mécanique"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=344, Y=126, Largeur=320, Hauteur=34

### lblM_Local  (Label)

- **Text** :
```
="Localisation"
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
- Position : X=672, Y=110, Largeur=320, Hauteur=16

### txtLocalisation  (Classic/TextInput)

- **Default** :
```
=gblMeta.Localisation
```
- **OnChange** :
```
=If(Self.Text <> gblMeta.Localisation; Set(gblMeta; Patch(gblMeta; {Localisation: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Ex. : Garage principal"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=672, Y=126, Largeur=320, Hauteur=34

### lblM_Date  (Label)

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
- Position : X=1000, Y=110, Largeur=200, Hauteur=16

### dpDate  (Classic/DatePicker)

- **DefaultDate** :
```
=gblMeta.DateAnalyse
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
=If(Self.SelectedDate <> gblMeta.DateAnalyse; Set(gblMeta; Patch(gblMeta; {DateAnalyse: Self.SelectedDate}));; Set(gblModifie; true))
```
- Position : X=1000, Y=126, Largeur=200, Hauteur=34

### lblM_Part  (Label)

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
- Position : X=16, Y=164, Largeur=648, Hauteur=16

### txtParticipants  (Classic/TextInput)

- **Default** :
```
=gblMeta.Participants
```
- **OnChange** :
```
=If(Self.Text <> gblMeta.Participants; Set(gblMeta; Patch(gblMeta; {Participants: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Ex. : J. Dupont, M. Tremblay"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=16, Y=180, Largeur=648, Hauteur=34

### lblM_Comm  (Label)

- **Text** :
```
="Commentaires / Notes spéciales"
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
- Position : X=672, Y=164, Largeur=678, Hauteur=16

### txtCommentaires  (Classic/TextInput)

- **Default** :
```
=gblMeta.Commentaires
```
- **OnChange** :
```
=If(Self.Text <> gblMeta.Commentaires; Set(gblMeta; Patch(gblMeta; {Commentaires: Self.Text}));; Set(gblModifie; true))
```
- **HintText** :
```
="Notes supplémentaires…"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=672, Y=180, Largeur=678, Hauteur=34

### btnAjouterLigne  (Classic/Button)

- **Text** :
```
="+ Ajouter une ligne"
```
- **OnSelect** :
```
=Collect(colLignes; Patch(nfLigneVide; {Cle: Text(GUID()); Ordre: CountRows(colLignes) + 1}));;
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
- Position : X=16, Y=224, Largeur=170, Hauteur=34

### btnAjouter5  (Classic/Button)

- **Text** :
```
="+ 5 lignes"
```
- **OnSelect** :
```
=With({n: CountRows(colLignes)};
    ForAll(Sequence(5) As i; Collect(colLignes; Patch(nfLigneVide; {Cle: Text(GUID()); Ordre: n + i.Value})))
);;
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
- Position : X=194, Y=224, Largeur=100, Hauteur=34

### lblNbLignes  (Label)

- **Text** :
```
="Lignes : " & CountRows(colLignes)
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#475569")
```
- Position : X=302, Y=224, Largeur=110, Hauteur=34

### txtFiltre  (Classic/TextInput)

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
="Rechercher…"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=412, Y=224, Largeur=240, Hauteur=34

### ddFiltreEnv  (Classic/DropDown)

- **Items** :
```
=["Tous"; "Garage"; "Atelier"; "Bureau"; "Extérieur"; "Autre"]
```
- **Default** :
```
="Tous"
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=660, Y=224, Largeur=150, Hauteur=34

### lblLegende  (Label)

- **Text** :
```
="G : 5 Mineure · 25 Majeure · 35 Grave · 40 Décès" & Char(10) & "MP : 0 Élimination · 10 Contrôle technique · 20 PST+Audit · 30 PST/Formation · 40 Affichage+EPI · 50 Aucune"
```
- **Size** :
```
=8
```
- **Color** :
```
=ColorValue("#475569")
```
- Position : X=820, Y=218, Largeur=530, Hauteur=46

### galLignes  (Gallery)

- **Items** :
```
=Sort(
    Filter(
        colLignes;
        (ddFiltreEnv.Selected.Value = "Tous" || Environnement = ddFiltreEnv.Selected.Value) &&
        (IsBlank(txtFiltre.Text) || txtFiltre.Text in Activite || txtFiltre.Text in Tache || txtFiltre.Text in Risque || txtFiltre.Text in Consequence || txtFiltre.Text in MesuresSuggerees)
    );
    Ordre
)
```
- **TemplateSize** :
```
=220
```
- **TemplatePadding** :
```
=0
```
- **ShowScrollbar** :
```
=true
```
- Position : X=8, Y=268, Largeur=1350, Hauteur=496

### recCarte  (Rectangle)  — dans galLignes

- **Width** :
```
=Parent.TemplateWidth
```
- **Height** :
```
=Parent.TemplateHeight - 8
```
- **Fill** :
```
=ColorValue("#f8fafc")
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- **BorderThickness** :
```
=1
```
- Position : X=0, Y=0, Largeur=Parent.TemplateWidth, Hauteur=Parent.TemplateHeight - 8

### lblNo  (Label)  — dans galLignes

- **Text** :
```
=ThisItem.Ordre
```
- **Size** :
```
=16
```
- **Color** :
```
=ColorValue("#1e293b")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Align** :
```
=Align.Center
```
- Position : X=4, Y=8, Largeur=46, Hauteur=40

### lblC_Env  (Label)  — dans galLignes

- **Text** :
```
="Environnement"
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
- Position : X=56, Y=4, Largeur=150, Hauteur=16

### ddEnv  (Classic/DropDown)  — dans galLignes

- **Items** :
```
=nfEnvironnements
```
- **Default** :
```
=ThisItem.Environnement
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.Environnement; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {Environnement: Self.Selected.Value});; Set(gblModifie; true))
```
- **AllowEmptySelection** :
```
=true
```
- **Size** :
```
=10
```
- Position : X=56, Y=20, Largeur=150, Hauteur=34

### lblC_Act  (Label)  — dans galLignes

- **Text** :
```
="Activité de travail"
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
- Position : X=214, Y=4, Largeur=330, Hauteur=16

### txtActivite  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.Activite
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Activite; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {Activite: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Ex. : Travail en hauteur"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=214, Y=20, Largeur=330, Hauteur=34

### lblC_Tache  (Label)  — dans galLignes

- **Text** :
```
="Tâches"
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
- Position : X=552, Y=4, Largeur=330, Hauteur=16

### txtTache  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.Tache
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Tache; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {Tache: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Ex. : Monter sur la plateforme"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=552, Y=20, Largeur=330, Hauteur=34

### lblC_Cat  (Label)  — dans galLignes

- **Text** :
```
="Catégorie de danger"
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
- Position : X=890, Y=4, Largeur=190, Hauteur=16

### ddCategorie  (Classic/DropDown)  — dans galLignes

- **Items** :
```
=ForAll(nfCategories; Categorie)
```
- **Default** :
```
=ThisItem.CategorieDanger
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.CategorieDanger; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {CategorieDanger: Self.Selected.Value});; Set(gblModifie; true))
```
- **AllowEmptySelection** :
```
=true
```
- **Size** :
```
=10
```
- Position : X=890, Y=20, Largeur=190, Hauteur=34

### icoMonter  (Classic/Icon)  — dans galLignes

- **Icon** :
```
=Icon.ChevronUp
```
- **OnSelect** :
```
=With({o: ThisItem.Ordre; k: ThisItem.Cle};
    If(o > 1;
        Patch(colLignes; LookUp(colLignes; Ordre = o - 1); {Ordre: o});;
        Patch(colLignes; LookUp(colLignes; Cle = k); {Ordre: o - 1});;
        Set(gblModifie; true)
    )
)
```
- **Color** :
```
=ColorValue("#475569")
```
- **Tooltip** :
```
="Monter la ligne"
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
- Position : X=1140, Y=16, Largeur=40, Hauteur=40

### icoDescendre  (Classic/Icon)  — dans galLignes

- **Icon** :
```
=Icon.ChevronDown
```
- **OnSelect** :
```
=With({o: ThisItem.Ordre; k: ThisItem.Cle};
    If(o < CountRows(colLignes);
        Patch(colLignes; LookUp(colLignes; Ordre = o + 1); {Ordre: o});;
        Patch(colLignes; LookUp(colLignes; Cle = k); {Ordre: o + 1});;
        Set(gblModifie; true)
    )
)
```
- **Color** :
```
=ColorValue("#475569")
```
- **Tooltip** :
```
="Descendre la ligne"
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
- Position : X=1184, Y=16, Largeur=40, Hauteur=40

### icoSupprimerLigne  (Classic/Icon)  — dans galLignes

- **Icon** :
```
=Icon.Trash
```
- **OnSelect** :
```
=With({k: ThisItem.Cle; id: ThisItem.LigneID};
    If(id > 0; Collect(colSupprimes; {LigneID: id}));;
    Remove(colLignes; LookUp(colLignes; Cle = k));;
    ClearCollect(colTmp; Sort(colLignes; Ordre));;
    ClearCollect(colLignes; ForAll(Sequence(CountRows(colTmp)) As i; Patch(Index(colTmp; i.Value); {Ordre: i.Value})));;
    Set(gblModifie; true)
)
```
- **Color** :
```
=ColorValue("#dc2626")
```
- **Tooltip** :
```
="Supprimer la ligne"
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
- Position : X=1262, Y=16, Largeur=40, Hauteur=40

### lblC_Risque  (Label)  — dans galLignes

- **Text** :
```
="Risques"
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
- Position : X=56, Y=58, Largeur=250, Hauteur=16

### txtRisque  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.Risque
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Risque; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {Risque: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Risque"
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
- Position : X=56, Y=74, Largeur=250, Hauteur=56

### lblC_Cons  (Label)  — dans galLignes

- **Text** :
```
="Conséquences"
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
- Position : X=314, Y=58, Largeur=250, Hauteur=16

### txtConsequence  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.Consequence
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Consequence; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {Consequence: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Conséquences"
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
- Position : X=314, Y=74, Largeur=250, Hauteur=56

### lblC_Bless  (Label)  — dans galLignes

- **Text** :
```
="Blessures / Maladie (pire scénario)"
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
- Position : X=572, Y=58, Largeur=250, Hauteur=16

### txtBlessure  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.Blessure
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Blessure; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {Blessure: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Blessure / maladie"
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
- Position : X=572, Y=74, Largeur=250, Hauteur=56

### lblC_MesEx  (Label)  — dans galLignes

- **Text** :
```
="Mesures préventives en place"
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
- Position : X=830, Y=58, Largeur=240, Hauteur=16

### txtMesuresExistantes  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.MesuresExistantes
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.MesuresExistantes; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {MesuresExistantes: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Mesures en place"
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
- Position : X=830, Y=74, Largeur=240, Hauteur=56

### lblC_G1  (Label)  — dans galLignes

- **Text** :
```
="G"
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
- Position : X=1078, Y=58, Largeur=64, Hauteur=16

### ddG1  (Classic/DropDown)  — dans galLignes

- **Items** :
```
=[0; 5; 25; 35; 40]
```
- **Default** :
```
=ThisItem.G1
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.G1; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {G1: Self.Selected.Value});; Set(gblModifie; true))
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=1078, Y=74, Largeur=64, Hauteur=34

### lblC_MP1  (Label)  — dans galLignes

- **Text** :
```
="MP"
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
- Position : X=1148, Y=58, Largeur=64, Hauteur=16

### ddMP1  (Classic/DropDown)  — dans galLignes

- **Items** :
```
=[0; 10; 20; 30; 40; 50]
```
- **Default** :
```
=ThisItem.MP1
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.MP1; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {MP1: Self.Selected.Value});; Set(gblModifie; true))
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=1148, Y=74, Largeur=64, Hauteur=34

### lblIR1  (Label)  — dans galLignes

- **Text** :
```
=With({ir: ThisItem.G1 * ThisItem.MP1}; "IR " & ir & Char(10) & LookUp(nfNiveaux; ir <= Seuil).Libelle)
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue(LookUp(nfNiveaux; ThisItem.G1 * ThisItem.MP1 <= Seuil).Texte)
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Align** :
```
=Align.Center
```
- **Fill** :
```
=ColorValue(LookUp(nfNiveaux; ThisItem.G1 * ThisItem.MP1 <= Seuil).Couleur)
```
- Position : X=1218, Y=74, Largeur=104, Hauteur=56

### lblC_MesSug  (Label)  — dans galLignes

- **Text** :
```
="Mesures préventives suggérées"
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
- Position : X=56, Y=134, Largeur=766, Hauteur=16

### txtMesuresSuggerees  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.MesuresSuggerees
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.MesuresSuggerees; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {MesuresSuggerees: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Mesures correctives proposées"
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
- Position : X=56, Y=150, Largeur=766, Hauteur=56

### lblC_Cout  (Label)  — dans galLignes

- **Text** :
```
="Coûts approx."
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
- Position : X=830, Y=134, Largeur=240, Hauteur=16

### txtCout  (Classic/TextInput)  — dans galLignes

- **Default** :
```
=ThisItem.Cout
```
- **OnChange** :
```
=If(Self.Text <> ThisItem.Cout; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {Cout: Self.Text});; Set(gblModifie; true))
```
- **HintText** :
```
="Coût"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=830, Y=150, Largeur=240, Hauteur=56

### lblC_G2  (Label)  — dans galLignes

- **Text** :
```
="G rés."
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
- Position : X=1078, Y=134, Largeur=64, Hauteur=16

### ddG2  (Classic/DropDown)  — dans galLignes

- **Items** :
```
=[0; 5; 25; 35; 40]
```
- **Default** :
```
=ThisItem.G2
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.G2; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {G2: Self.Selected.Value});; Set(gblModifie; true))
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=1078, Y=150, Largeur=64, Hauteur=34

### lblC_MP2  (Label)  — dans galLignes

- **Text** :
```
="MP rés."
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
- Position : X=1148, Y=134, Largeur=64, Hauteur=16

### ddMP2  (Classic/DropDown)  — dans galLignes

- **Items** :
```
=[0; 10; 20; 30; 40; 50]
```
- **Default** :
```
=ThisItem.MP2
```
- **OnChange** :
```
=If(Self.Selected.Value <> ThisItem.MP2; Patch(colLignes; LookUp(colLignes; Cle = ThisItem.Cle); {MP2: Self.Selected.Value});; Set(gblModifie; true))
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=1148, Y=150, Largeur=64, Hauteur=34

### lblIR2  (Label)  — dans galLignes

- **Text** :
```
=With({ir: ThisItem.G2 * ThisItem.MP2}; "IR rés. " & ir & Char(10) & LookUp(nfNiveaux; ir <= Seuil).Libelle)
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue(LookUp(nfNiveaux; ThisItem.G2 * ThisItem.MP2 <= Seuil).Texte)
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Align** :
```
=Align.Center
```
- **Fill** :
```
=ColorValue(LookUp(nfNiveaux; ThisItem.G2 * ThisItem.MP2 <= Seuil).Couleur)
```
- Position : X=1218, Y=150, Largeur=104, Hauteur=56

## Écran scrMatrice (fichier 3_scrMatrice.yaml)


### recBarre_Mat  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Mat  (Label)

- **Text** :
```
="Matrice de risque"
```
- **Size** :
```
=17
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=600, Hauteur=56

### lblInfo_Mat  (Label)

- **Text** :
```
=If(IsBlank(gblMeta.Service); ""; gblMeta.Service & "  ·  " & Text(gblMeta.DateAnalyse; "yyyy-mm-dd") & "  ·  " & CountRows(colLignes) & " ligne(s)")
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#cbd5e1")
```
- **Align** :
```
=Align.Right
```
- **PaddingRight** :
```
=16
```
- Position : X=620, Y=0, Largeur=730, Hauteur=56

### recOnglets_Mat  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngGrille_Mat  (Classic/Button)

- **Text** :
```
="Grille d'analyse"
```
- **OnSelect** :
```
=Navigate(scrAnalyse; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=16, Y=62, Largeur=170, Hauteur=36

### btnOngMatrice_Mat  (Classic/Button)

- **Text** :
```
="Matrice de risque"
```
- **OnSelect** :
```
=Navigate(scrMatrice; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=194, Y=62, Largeur=170, Hauteur=36

### btnOngAide_Mat  (Classic/Button)

- **Text** :
```
="Aide-mémoire"
```
- **OnSelect** :
```
=Navigate(scrAideMemoire; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=372, Y=62, Largeur=170, Hauteur=36

### btnOngSynthese_Mat  (Classic/Button)

- **Text** :
```
="Synthèse"
```
- **OnSelect** :
```
=Navigate(scrSynthese; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=550, Y=62, Largeur=170, Hauteur=36

### btnOngPlan_Mat  (Classic/Button)

- **Text** :
```
="Plan d'action"
```
- **OnSelect** :
```
=Navigate(scrPlanAction; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=728, Y=62, Largeur=170, Hauteur=36

### htmMatrice  (HtmlViewer)

- **HtmlText** :
```
="<div style='height:600px;overflow-y:auto;font-family:Segoe UI,Arial,sans-serif'><h3 style='margin:4px 0 4px 0;color:#1e293b'>Matrice de risque — IR = Gravité (G) × Mesure préventive (MP)</h3><table style='border-collapse:collapse;width:100%'><tr><th style='background:#1e293b;color:#fff;padding:8px'>Gravité \ MP</th>" & Concat(nfMP; "<th style='background:#334155;color:#fff;padding:8px;font-size:12px'>" & Libelle & "<br>(" & Valeur & ")</th>") & "</tr>" & Concat(nfGravite As g; "<tr><td style='background:#f1f5f9;padding:8px;font-size:12px'><b>" & g.Libelle & " (" & g.Valeur & ")</b><br><span style='color:#64748b'>" & g.Description & "</span></td>" & Concat(nfMP As m; With({ir: g.Valeur * m.Valeur}; With({n: LookUp(nfNiveaux; ir <= Seuil)}; "<td style='padding:14px;text-align:center;font-weight:bold;font-size:15px;border:2px solid #fff;background:" & n.Couleur & ";color:" & n.Texte & "'>" & ir & "</td>"))) & "</tr>") & "</table><h4 style='margin:18px 0 6px 0;color:#1e293b'>Niveaux de risque</h4><table style='border-collapse:collapse'>" & Concat(nfNiveaux; "<tr><td style='background:" & Couleur & ";color:" & Texte & ";padding:6px 14px;font-weight:bold;width:120px'>" & Libelle & "</td><td style='padding:6px 14px'>" & If(Plancher < 0; "IR ≤ " & Seuil; If(Seuil > 99999; "IR > " & Plancher; (Plancher + 1) & " ≤ IR ≤ " & Seuil)) & "</td></tr>") & "</table></div>"
```
- Position : X=16, Y=112, Largeur=1334, Hauteur=646

## Écran scrAideMemoire (fichier 4_scrAideMemoire.yaml)


### recBarre_Aide  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Aide  (Label)

- **Text** :
```
="Aide-mémoire SST"
```
- **Size** :
```
=17
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=600, Hauteur=56

### lblInfo_Aide  (Label)

- **Text** :
```
=If(IsBlank(gblMeta.Service); ""; gblMeta.Service & "  ·  " & Text(gblMeta.DateAnalyse; "yyyy-mm-dd") & "  ·  " & CountRows(colLignes) & " ligne(s)")
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#cbd5e1")
```
- **Align** :
```
=Align.Right
```
- **PaddingRight** :
```
=16
```
- Position : X=620, Y=0, Largeur=730, Hauteur=56

### recOnglets_Aide  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngGrille_Aide  (Classic/Button)

- **Text** :
```
="Grille d'analyse"
```
- **OnSelect** :
```
=Navigate(scrAnalyse; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=16, Y=62, Largeur=170, Hauteur=36

### btnOngMatrice_Aide  (Classic/Button)

- **Text** :
```
="Matrice de risque"
```
- **OnSelect** :
```
=Navigate(scrMatrice; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=194, Y=62, Largeur=170, Hauteur=36

### btnOngAide_Aide  (Classic/Button)

- **Text** :
```
="Aide-mémoire"
```
- **OnSelect** :
```
=Navigate(scrAideMemoire; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=372, Y=62, Largeur=170, Hauteur=36

### btnOngSynthese_Aide  (Classic/Button)

- **Text** :
```
="Synthèse"
```
- **OnSelect** :
```
=Navigate(scrSynthese; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=550, Y=62, Largeur=170, Hauteur=36

### btnOngPlan_Aide  (Classic/Button)

- **Text** :
```
="Plan d'action"
```
- **OnSelect** :
```
=Navigate(scrPlanAction; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=728, Y=62, Largeur=170, Hauteur=36

### lblAM_Cat  (Label)

- **Text** :
```
="Catégorie"
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
- Position : X=16, Y=112, Largeur=220, Hauteur=16

### ddAMCategorie  (Classic/DropDown)

- **Items** :
```
=["Toutes"; "Physique"; "Mécanique"; "Électrique"; "Chimique"; "Biologique"; "Humain"; "Ergonomique"]
```
- **Default** :
```
="Toutes"
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=16, Y=128, Largeur=220, Hauteur=34

### lblAM_Rech  (Label)

- **Text** :
```
="Recherche"
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
- Position : X=252, Y=112, Largeur=400, Hauteur=16

### txtAMRecherche  (Classic/TextInput)

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
="Ex. : chute, bruit, coupure…"
```
- **Size** :
```
=10
```
- **BorderColor** :
```
=ColorValue("#cbd5e1")
```
- Position : X=252, Y=128, Largeur=400, Hauteur=34

### htmAideMemoire  (HtmlViewer)

- **HtmlText** :
```
="<div style='height:580px;overflow-y:auto;font-family:Segoe UI,Arial,sans-serif'>" & Concat(Filter(nfCategories; ddAMCategorie.Selected.Value = "Toutes" || Categorie = ddAMCategorie.Selected.Value) As c; With({lst: Filter(nfAideMemoire As a; a.Categorie = c.Categorie && (IsBlank(txtAMRecherche.Text) || txtAMRecherche.Text in a.Danger || txtAMRecherche.Text in a.Risque || txtAMRecherche.Text in a.Consequence))}; If(CountRows(lst) = 0; ""; "<h3 style='color:#fff;background:" & c.Couleur & ";padding:6px 10px;margin:14px 0 0 0'>" & c.Categorie & "</h3><table style='border-collapse:collapse;width:100%'><tr><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Danger</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Risque</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Conséquence</th></tr>" & Concat(lst; "<tr><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Danger & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Risque & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Consequence & "</td></tr>") & "</table>"))) & "</div>"
```
- Position : X=16, Y=172, Largeur=1334, Hauteur=590

## Écran scrSynthese (fichier 5_scrSynthese.yaml)


### recBarre_Syn  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Syn  (Label)

- **Text** :
```
="Synthèse"
```
- **Size** :
```
=17
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=600, Hauteur=56

### lblInfo_Syn  (Label)

- **Text** :
```
=If(IsBlank(gblMeta.Service); ""; gblMeta.Service & "  ·  " & Text(gblMeta.DateAnalyse; "yyyy-mm-dd") & "  ·  " & CountRows(colLignes) & " ligne(s)")
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#cbd5e1")
```
- **Align** :
```
=Align.Right
```
- **PaddingRight** :
```
=16
```
- Position : X=620, Y=0, Largeur=730, Hauteur=56

### recOnglets_Syn  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngGrille_Syn  (Classic/Button)

- **Text** :
```
="Grille d'analyse"
```
- **OnSelect** :
```
=Navigate(scrAnalyse; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=16, Y=62, Largeur=170, Hauteur=36

### btnOngMatrice_Syn  (Classic/Button)

- **Text** :
```
="Matrice de risque"
```
- **OnSelect** :
```
=Navigate(scrMatrice; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=194, Y=62, Largeur=170, Hauteur=36

### btnOngAide_Syn  (Classic/Button)

- **Text** :
```
="Aide-mémoire"
```
- **OnSelect** :
```
=Navigate(scrAideMemoire; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=372, Y=62, Largeur=170, Hauteur=36

### btnOngSynthese_Syn  (Classic/Button)

- **Text** :
```
="Synthèse"
```
- **OnSelect** :
```
=Navigate(scrSynthese; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=550, Y=62, Largeur=170, Hauteur=36

### btnOngPlan_Syn  (Classic/Button)

- **Text** :
```
="Plan d'action"
```
- **OnSelect** :
```
=Navigate(scrPlanAction; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=728, Y=62, Largeur=170, Hauteur=36

### lblCarteTotal  (Label)

- **Text** :
```
=CountRows(colLignes) & Char(10) & "Total des risques"
```
- **Size** :
```
=15
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
- Position : X=16, Y=112, Largeur=254, Hauteur=80

### lblCarteCritique  (Label)

- **Text** :
```
=CountIf(colLignes; G1 * MP1 > 1250) & Char(10) & "Critique (> 1250)"
```
- **Size** :
```
=15
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
=ColorValue("#ef4444")
```
- **Align** :
```
=Align.Center
```
- Position : X=286, Y=112, Largeur=254, Hauteur=80

### lblCarteEleve  (Label)

- **Text** :
```
=CountIf(colLignes; G1 * MP1 > 750 && G1 * MP1 <= 1250) & Char(10) & "Élevé (751–1250)"
```
- **Size** :
```
=15
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
=ColorValue("#f97316")
```
- **Align** :
```
=Align.Center
```
- Position : X=556, Y=112, Largeur=254, Hauteur=80

### lblCarteModere  (Label)

- **Text** :
```
=CountIf(colLignes; G1 * MP1 > 250 && G1 * MP1 <= 750) & Char(10) & "Modéré (251–750)"
```
- **Size** :
```
=15
```
- **Color** :
```
=ColorValue("#1f2937")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- **Fill** :
```
=ColorValue("#fbbf24")
```
- **Align** :
```
=Align.Center
```
- Position : X=826, Y=112, Largeur=254, Hauteur=80

### lblCarteFaible  (Label)

- **Text** :
```
=CountIf(colLignes; G1 * MP1 <= 250) & Char(10) & "Faible (≤ 250)"
```
- **Size** :
```
=15
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
=ColorValue("#22c55e")
```
- **Align** :
```
=Align.Center
```
- Position : X=1096, Y=112, Largeur=254, Hauteur=80

### htmSyntheseNiveaux  (HtmlViewer)

- **HtmlText** :
```
="<div style='height:250px;overflow-y:auto;font-family:Segoe UI,Arial,sans-serif'><h3 style='font-size:13px;color:#1e293b;margin:6px 0'>Niveau de risque — AVANT mesures correctives</h3>" & With({t: ForAll(Sort(nfNiveaux; Seuil; SortOrder.Descending) As n; {Libelle: n.Libelle; Couleur: n.Couleur; N: CountIf(colLignes; G1 * MP1 > n.Plancher && G1 * MP1 <= n.Seuil)})}; With({m: Max(1; Max(t; N))}; If(CountRows(t) = 0; "<p style='color:#6b7280'>Aucune donnée</p>"; "<table style='width:100%;border-collapse:collapse'>" & Concat(t; "<tr><td style='width:120px;font-size:12px;padding:3px'>" & Libelle & "</td><td style='padding:3px'><div style='background:" & Couleur & ";height:16px;width:" & Round(N / m * 100; 0) & "%'></div></td><td style='width:36px;text-align:right;font-size:12px;font-weight:bold'>" & N & "</td></tr>") & "</table>"))) & "<h3 style='font-size:13px;color:#1e293b;margin:6px 0'>Niveau de risque — APRÈS mesures correctives</h3>" & With({t: ForAll(Sort(nfNiveaux; Seuil; SortOrder.Descending) As n; {Libelle: n.Libelle; Couleur: n.Couleur; N: CountIf(colLignes; G2 * MP2 > n.Plancher && G2 * MP2 <= n.Seuil)})}; With({m: Max(1; Max(t; N))}; If(CountRows(t) = 0; "<p style='color:#6b7280'>Aucune donnée</p>"; "<table style='width:100%;border-collapse:collapse'>" & Concat(t; "<tr><td style='width:120px;font-size:12px;padding:3px'>" & Libelle & "</td><td style='padding:3px'><div style='background:" & Couleur & ";height:16px;width:" & Round(N / m * 100; 0) & "%'></div></td><td style='width:36px;text-align:right;font-size:12px;font-weight:bold'>" & N & "</td></tr>") & "</table>"))) & "</div>"
```
- Position : X=16, Y=202, Largeur=660, Hauteur=262

### htmSyntheseRepartition  (HtmlViewer)

- **HtmlText** :
```
="<div style='height:250px;overflow-y:auto;font-family:Segoe UI,Arial,sans-serif'><h3 style='font-size:13px;color:#1e293b;margin:6px 0'>Par environnement</h3>" & With({t: ForAll(Distinct(Filter(colLignes; !IsBlank(Environnement)); Environnement) As e; {Libelle: e.Value; Couleur: "#3b82f6"; N: CountIf(colLignes; Environnement = e.Value)})}; With({m: Max(1; Max(t; N))}; If(CountRows(t) = 0; "<p style='color:#6b7280'>Aucune donnée</p>"; "<table style='width:100%;border-collapse:collapse'>" & Concat(t; "<tr><td style='width:120px;font-size:12px;padding:3px'>" & Libelle & "</td><td style='padding:3px'><div style='background:" & Couleur & ";height:16px;width:" & Round(N / m * 100; 0) & "%'></div></td><td style='width:36px;text-align:right;font-size:12px;font-weight:bold'>" & N & "</td></tr>") & "</table>"))) & "<h3 style='font-size:13px;color:#1e293b;margin:6px 0'>Par catégorie de danger</h3>" & With({t: ForAll(Distinct(Filter(colLignes; !IsBlank(CategorieDanger)); CategorieDanger) As d; {Libelle: d.Value; Couleur: Coalesce(LookUp(nfCategories; Categorie = d.Value).Couleur; "#6b7280"); N: CountIf(colLignes; CategorieDanger = d.Value)})}; With({m: Max(1; Max(t; N))}; If(CountRows(t) = 0; "<p style='color:#6b7280'>Aucune donnée</p>"; "<table style='width:100%;border-collapse:collapse'>" & Concat(t; "<tr><td style='width:120px;font-size:12px;padding:3px'>" & Libelle & "</td><td style='padding:3px'><div style='background:" & Couleur & ";height:16px;width:" & Round(N / m * 100; 0) & "%'></div></td><td style='width:36px;text-align:right;font-size:12px;font-weight:bold'>" & N & "</td></tr>") & "</table>"))) & "</div>"
```
- Position : X=690, Y=202, Largeur=660, Hauteur=262

### htmTop10  (HtmlViewer)

- **HtmlText** :
```
=With({t: FirstN(Sort(AddColumns(colLignes; IR1; G1 * MP1; IR2; G2 * MP2); IR1; SortOrder.Descending); 10)}; "<div style='height:270px;overflow-y:auto;font-family:Segoe UI,Arial,sans-serif'><h3 style='font-size:13px;color:#1e293b;margin:6px 0'>Top 10 des risques (IR initial)</h3><table style='border-collapse:collapse;width:100%'><tr><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'># ligne</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Activité</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Risque</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR initial</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR résiduel</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Réduction</th></tr>" & Concat(t; With({n1: LookUp(nfNiveaux; IR1 <= Seuil); n2: LookUp(nfNiveaux; IR2 <= Seuil)}; "<tr><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Ordre & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Coalesce(Activite; "(vide)") & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Coalesce(Risque; "(vide)") & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & "<span style='background:" & n1.Couleur & ";color:" & n1.Texte & ";padding:2px 8px;border-radius:4px;font-weight:bold'>" & IR1 & "</span>" & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & "<span style='background:" & n2.Couleur & ";color:" & n2.Texte & ";padding:2px 8px;border-radius:4px;font-weight:bold'>" & IR2 & "</span>" & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & If(IR1 > 0; Round((1 - IR2 / IR1) * 100; 0) & " %"; "—") & "</td></tr>")) & "</table></div>")
```
- Position : X=16, Y=474, Largeur=1334, Hauteur=284

## Écran scrPlanAction (fichier 6_scrPlanAction.yaml)


### recBarre_Plan  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Plan  (Label)

- **Text** :
```
="Plan d'action"
```
- **Size** :
```
=17
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=600, Hauteur=56

### lblInfo_Plan  (Label)

- **Text** :
```
=If(IsBlank(gblMeta.Service); ""; gblMeta.Service & "  ·  " & Text(gblMeta.DateAnalyse; "yyyy-mm-dd") & "  ·  " & CountRows(colLignes) & " ligne(s)")
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#cbd5e1")
```
- **Align** :
```
=Align.Right
```
- **PaddingRight** :
```
=16
```
- Position : X=620, Y=0, Largeur=730, Hauteur=56

### recOnglets_Plan  (Rectangle)

- **Fill** :
```
=ColorValue("#e2e8f0")
```
- Position : X=0, Y=56, Largeur=1366, Hauteur=48

### btnOngGrille_Plan  (Classic/Button)

- **Text** :
```
="Grille d'analyse"
```
- **OnSelect** :
```
=Navigate(scrAnalyse; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAnalyse"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=16, Y=62, Largeur=170, Hauteur=36

### btnOngMatrice_Plan  (Classic/Button)

- **Text** :
```
="Matrice de risque"
```
- **OnSelect** :
```
=Navigate(scrMatrice; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrMatrice"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=194, Y=62, Largeur=170, Hauteur=36

### btnOngAide_Plan  (Classic/Button)

- **Text** :
```
="Aide-mémoire"
```
- **OnSelect** :
```
=Navigate(scrAideMemoire; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrAideMemoire"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=372, Y=62, Largeur=170, Hauteur=36

### btnOngSynthese_Plan  (Classic/Button)

- **Text** :
```
="Synthèse"
```
- **OnSelect** :
```
=Navigate(scrSynthese; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrSynthese"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=550, Y=62, Largeur=170, Hauteur=36

### btnOngPlan_Plan  (Classic/Button)

- **Text** :
```
="Plan d'action"
```
- **OnSelect** :
```
=Navigate(scrPlanAction; ScreenTransition.None)
```
- **Fill** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#2563eb"); ColorValue("#ffffff"))
```
- **Color** :
```
=If(App.ActiveScreen.Name = "scrPlanAction"; ColorValue("#ffffff"); ColorValue("#1e293b"))
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
- Position : X=728, Y=62, Largeur=170, Hauteur=36

### lblPA_Niv  (Label)

- **Text** :
```
="Niveau (IR initial)"
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
- Position : X=16, Y=112, Largeur=180, Hauteur=16

### ddPANiveau  (Classic/DropDown)

- **Items** :
```
=["Tous"; "Critique"; "Élevé"; "Modéré"; "Faible"]
```
- **Default** :
```
="Tous"
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=16, Y=128, Largeur=180, Hauteur=34

### lblPA_Env  (Label)

- **Text** :
```
="Environnement"
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
- Position : X=210, Y=112, Largeur=180, Hauteur=16

### ddPAEnv  (Classic/DropDown)

- **Items** :
```
=["Tous"; "Garage"; "Atelier"; "Bureau"; "Extérieur"; "Autre"]
```
- **Default** :
```
="Tous"
```
- **AllowEmptySelection** :
```
=false
```
- **Size** :
```
=10
```
- Position : X=210, Y=128, Largeur=180, Hauteur=34

### lblPACompte  (Label)

- **Text** :
```
=CountRows(Filter(Sort(AddColumns(colLignes; IR1; G1 * MP1; IR2; G2 * MP2; Niv1; LookUp(nfNiveaux; G1 * MP1 <= Seuil).Libelle); IR1; SortOrder.Descending); (ddPANiveau.Selected.Value = "Tous" || Niv1 = ddPANiveau.Selected.Value) && (ddPAEnv.Selected.Value = "Tous" || Environnement = ddPAEnv.Selected.Value))) & " élément(s) — triés du risque le plus élevé au plus faible"
```
- **Size** :
```
=10
```
- **Color** :
```
=ColorValue("#475569")
```
- Position : X=404, Y=128, Largeur=300, Hauteur=34

### btnImprimerPlan  (Classic/Button)

- **Text** :
```
="Imprimer"
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
- Position : X=1190, Y=126, Largeur=160, Hauteur=36

### htmPlanAction  (HtmlViewer)

- **HtmlText** :
```
=With({t: Filter(Sort(AddColumns(colLignes; IR1; G1 * MP1; IR2; G2 * MP2; Niv1; LookUp(nfNiveaux; G1 * MP1 <= Seuil).Libelle); IR1; SortOrder.Descending); (ddPANiveau.Selected.Value = "Tous" || Niv1 = ddPANiveau.Selected.Value) && (ddPAEnv.Selected.Value = "Tous" || Environnement = ddPAEnv.Selected.Value))}; "<div style='height:580px;overflow-y:auto;font-family:Segoe UI,Arial,sans-serif'>" & If(CountRows(t) = 0; "<p style='color:#6b7280;padding:20px'>Aucun élément à afficher.</p>"; "<table style='border-collapse:collapse;width:100%'><tr>" & "<th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Priorité</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Env.</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Activité</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Risque / Conséquences</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Niveau</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Mesures préventives suggérées</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Coûts</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>IR rés.</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Niveau rés.</th><th style='background:#1e293b;color:#fff;padding:4px;text-align:left'>Réduction</th></tr>" & Concat(Sequence(CountRows(t)) As i; With({r: Index(t; i.Value)}; With({n1: LookUp(nfNiveaux; r.IR1 <= Seuil); n2: LookUp(nfNiveaux; r.IR2 <= Seuil)}; "<tr><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'><b>" & i.Value & "</b></td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & r.Environnement & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Coalesce(r.Activite; "(vide)") & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & Coalesce(r.Risque; "(vide)") & If(IsBlank(r.Consequence); ""; "<br><span style='color:#6b7280'>" & r.Consequence & "</span>") & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & "<span style='background:" & n1.Couleur & ";color:" & n1.Texte & ";padding:2px 8px;border-radius:4px;font-weight:bold'>" & r.IR1 & "</span>" & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & n1.Libelle & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & r.MesuresSuggerees & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & r.Cout & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & "<span style='background:" & n2.Couleur & ";color:" & n2.Texte & ";padding:2px 8px;border-radius:4px;font-weight:bold'>" & r.IR2 & "</span>" & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'>" & n2.Libelle & "</td><td style='border-bottom:1px solid #e2e8f0;padding:6px;font-size:12px;vertical-align:top'><b>" & If(r.IR1 > 0; Round((1 - r.IR2 / r.IR1) * 100; 0) & " %"; "—") & "</b></td></tr>"))) & "</table>") & "</div>")
```
- Position : X=16, Y=172, Largeur=1334, Hauteur=590

## Écran scrImport (fichier 7_scrImport.yaml)


### recBarre_Imp  (Rectangle)

- **Fill** :
```
=ColorValue("#1e293b")
```
- Position : X=0, Y=0, Largeur=1366, Hauteur=56

### lblTitre_Imp  (Label)

- **Text** :
```
="Importer une analyse (fichier .json de l'application HTML)"
```
- **Size** :
```
=17
```
- **Color** :
```
=ColorValue("#ffffff")
```
- **FontWeight** :
```
=FontWeight.Bold
```
- Position : X=16, Y=0, Largeur=1000, Hauteur=56

### lblInstructions_Imp  (Label)

- **Text** :
```
="1. Ouvrez le fichier .json (ex. : AR_SST_Maintenance_2026-04-15.json) avec le Bloc-notes." & Char(10) & "2. Sélectionnez tout (Ctrl+A), copiez (Ctrl+C) et collez (Ctrl+V) dans la zone ci-dessous." & Char(10) & "3. Cliquez sur « Importer », vérifiez l'analyse, puis cliquez sur « Enregistrer » pour la créer dans SharePoint."
```
- **Size** :
```
=11
```
- **Color** :
```
=ColorValue("#334155")
```
- Position : X=16, Y=64, Largeur=1334, Hauteur=80

### txtJSON  (Classic/TextInput)

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
="Collez ici le contenu du fichier .json…"
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
- Position : X=16, Y=150, Largeur=1334, Hauteur=520

### btnImporter  (Classic/Button)

- **Text** :
```
="Importer"
```
- **OnSelect** :
```
=IfError(
    With({j: ParseJSON(txtJSON.Text)};
        With({r: Table(j.rows)};
            Set(gblAnalyseID; Blank());;
            Set(gblMeta; {Service: Text(j.meta.service); Division: Text(j.meta.division); Localisation: Text(j.meta.localisation); Participants: Text(j.meta.participants); DateAnalyse: IfError(DateValue(Text(j.meta.date)); Today()); Commentaires: Text(j.meta.commentaires)});;
            ClearCollect(
                colLignes;
                ForAll(
                    Sequence(CountRows(r)) As i;
                    With({x: Index(r; i.Value).Value};
                        {
                            LigneID: 0;
                            Cle: Coalesce(Text(x.id); Text(GUID()));
                            Ordre: i.Value;
                            Environnement: Text(x.environnement);
                            Activite: Text(x.activite);
                            Tache: Text(x.tache);
                            CategorieDanger: Text(x.categorie_danger);
                            Risque: Text(x.risque);
                            Consequence: Text(x.consequence);
                            Blessure: Text(x.blessure);
                            MesuresExistantes: Text(x.mesures_existantes);
                            G1: Coalesce(Value(x.g1); 0);
                            MP1: Coalesce(Value(x.mp1); 0);
                            MesuresSuggerees: Text(x.mesures_suggerees);
                            Cout: Text(x.cout);
                            G2: Coalesce(Value(x.g2); 0);
                            MP2: Coalesce(Value(x.mp2); 0)
                        }
                    )
                )
            );;
            Clear(colSupprimes);;
            Set(gblModifie; true);;
            Set(gblAvertiQuitter; false);;
            Reset(txtJSON);;
            Notify("Analyse importée (" & CountRows(colLignes) & " ligne(s)). Vérifiez puis cliquez sur « Enregistrer »."; NotificationType.Success);;
            Navigate(scrAnalyse; ScreenTransition.None)
        )
    );
    Notify("Le texte collé n'est pas un fichier JSON valide de l'application Analyse de risques."; NotificationType.Error)
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
- Position : X=16, Y=684, Largeur=220, Hauteur=44

### btnRetourImp  (Classic/Button)

- **Text** :
```
="Retour"
```
- **OnSelect** :
```
=Reset(txtJSON);; Navigate(scrAccueil; ScreenTransition.None)
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
- Position : X=244, Y=684, Largeur=160, Hauteur=44