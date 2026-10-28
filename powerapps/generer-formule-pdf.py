# Génère la formule Power Fx (syntaxe française) du bouton btnApercuPDF.
# Usage : python3 generer-formule-pdf.py  (écrit btnApercuPDF-OnSelect.txt et btnImprimer-Plan-OnSelect.txt)

def E(x):
    """Texte saisi -> HTML sûr (& < > et retours de ligne)."""
    return ('Substitute(Substitute(Substitute(Substitute(' + x +
            '; "&"; "&amp;"); "<"; "&lt;"); ">"; "&gt;"); Char(10); "<br>")')

def s(t):
    """Texte fixe -> chaîne Power Fx."""
    return '"' + t.replace('"', '""') + '"'

def vide(cond, contenu, msg="Aucun élément."):
    return f'If({cond}; {s("<p class=vide>" + msg + "</p>")}; {contenu})'

DATE = '"d mmmm yyyy"'  # pas de « [$-fr-CA] » : refusé par l'environnement (« Code de langue fr-CA non pris en charge »)
def d(x):
    return f'If(IsBlank({x}); "—"; Text({x}; {DATE}))'

CSS = ("body{font-family:Segoe UI,Arial,sans-serif;font-size:10pt;color:#1f2937}"
       "h1{font-size:18pt;color:#00285e;margin:0}"
       ".sous{color:#6b7280;margin:2px 0 14px 0}"
       "h2{font-size:12.5pt;color:#00285e;border-bottom:2px solid #857650;padding-bottom:3px;margin:18px 0 6px 0}"
       "h3{font-size:11pt;color:#074b98;margin:12px 0 4px 0}"
       "table{border-collapse:collapse;width:100%;margin:4px 0 8px 0}"
       "th{background:#e8eef7;color:#00285e;text-align:left;padding:5px;border:1px solid #c7d2e3;font-size:9.5pt}"
       "td{padding:5px;border:1px solid #d1d5db;vertical-align:top;font-size:9.5pt}"
       "td.lbl{background:#f3f4f6;font-weight:bold;width:28%}"
       ".vide{color:#9ca3af;font-style:italic}"
       ".desc{color:#4b5563;font-style:italic;margin:0 0 4px 0}"
       ".bloc{border:1px solid #d1d5db;padding:8px;min-height:30px}"
       ".pied{margin-top:24px;color:#9ca3af;font-size:8pt;border-top:1px solid #e5e7eb;padding-top:4px}")

def ligne(lbl, val):
    return f'"<tr><td class=lbl>{lbl}</td><td>" & {val} & "</td></tr>"'

parts = []
P = parts.append

# En-tête
P(s("<html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>"))
P(s("<h1>Appréciation de la contribution</h1><p class=sous>") +
  ' & LookUp(colPostes; PosteID = CurrentPosteID).PosteLabel & ' +
  s(" — formulaire du 15 octobre 2026 — dossier no ") + ' & varDossier.ID & ' +
  s(" — statut : ") + ' & Coalesce(varDossier.Statut.Value; "Brouillon") & ' + s("</p>"))

# Identification
P(s("<h2>Identification de la personne en appréciation et du type de rencontre</h2><table>"))
P(ligne("Nom, prénom", E('Coalesce(txtNom.Text; varDossier.Title)')))
P(ligne("ID", E('Coalesce(txtId.Text; varDossier.IdEmploye)')))
P(ligne("Poste", E('Coalesce(txtPoste.Text; varDossier.Poste)')))
P(ligne("Type de poste", 'LookUp(colPostes; PosteID = CurrentPosteID).PosteLabel'))
P(ligne("Année", 'Coalesce(Text(varDossier.Annee); Text(Year(Today())))'))
rencontres = ('Concat(Filter(Table('
              '{T: "Période d\'essai ou progression salariale"; C: chkEssai.Checked}; '
              '{T: "Première rencontre annuelle"; C: chkPremiere.Checked}; '
              '{T: "Bilan de mi-année"; C: chkMiAnnee.Checked}; '
              '{T: "Bilan annuel"; C: chkBilan.Checked}; '
              '{T: "Autre : " & Coalesce(txtAutre.Text; varDossier.TypeRencontreAutre); C: chkAutre.Checked}); C); T; ", ")')
P(ligne("Type de rencontre", E(rencontres)))
P(s("</table><h3>Participants</h3><table>"))
P(ligne("Personne en appréciation", 'Coalesce(varDossier.PersonneAppreciation.DisplayName; "—")'))
P(ligne("Supérieur(e) immédiat(e)", 'Coalesce(varDossier.SuperieurImmediat.DisplayName; "—")'))
P(ligne("Supérieur(e) hiérarchique", 'Coalesce(varDossier.SuperieurHierarchique.DisplayName; "—")'))
P(ligne("Directeur / directrice", 'If(chkDirRequis.Checked; Coalesce(varDossier.Directeur.DisplayName; "à choisir"); "non requis")'))
P(s("</table>"))

# Section A
P(s("<h2>Section A — Les objectifs annuels</h2><h3>Objectifs de l'année en cours</h3>"))
fa = 'Filter(colObjActuels; Objectif <> "" Or Indicateur <> "" Or Actions <> "")'
P(vide(f'CountRows({fa}) = 0',
       s("<table><tr><th>Objectifs</th><th>Indicateurs de mesure</th><th>Actions réalisées / commentaires</th></tr>") +
       f' & Concat({fa}; "<tr><td>" & {E("Objectif")} & "</td><td>" & {E("Indicateur")} & "</td><td>" & {E("Actions")} & "</td></tr>") & ' +
       s("</table>")))
P(s("<h3>Objectifs de l'année à venir</h3>"))
fv = 'Filter(colObjAvenir; Objectif <> "" Or Indicateur <> "")'
P(vide(f'CountRows({fv}) = 0',
       s("<table><tr><th>Objectifs à venir</th><th>Indicateurs de mesure</th></tr>") +
       f' & Concat({fv}; "<tr><td>" & {E("Objectif")} & "</td><td>" & {E("Indicateur")} & "</td></tr>") & ' +
       s("</table>")))

# Section B
postures = ('Concat(Sort(colPostures; Ordre) As p; Concatenate("<h3>"; p.Titre; "</h3><p class=desc>"; '
            'If(CurrentPosteID = "sans_equipe"; p.DescSans; p.DescAvec); '
            '"</p><table><tr><th>Comportements</th><th>Cote de la personne</th><th>Cote du supérieur</th></tr>"; '
            'Concat(Filter(colComportements; PostureID = p.PostureID) As c; Concatenate("<tr><td>"; '
            'If(CurrentPosteID = "sans_equipe"; c.TexteSans; c.TexteAvec); "</td><td>"; '
            'Coalesce(c.CoteCadre; "—"); "</td><td>"; Coalesce(c.CoteSup; "—"); "</td></tr>")); '
            '"</table>"; If(IsBlank(p.Commentaire); ""; Concatenate("<p><b>Exemples et commentaires :</b><br>"; '
            + E('p.Commentaire') + '; "</p>"))))')
competences = ('Concatenate("<table><tr><th>Compétence</th><th>Exemples d\'application</th></tr>"; '
               'Concat(Sort(colCompetences; Ordre) As k; Concatenate("<tr><td><b>"; k.Label; "</b>"; '
               'If(IsBlank(k.Desc); ""; "<br><span class=desc>" & k.Desc & "</span>"); "</td><td>"; '
               'If(IsBlank(k.Exemple); "—"; ' + E('k.Exemple') + '); "</td></tr>")); "</table>")')
P('If(CurrentPosteID = "professionnel"; ' + s("<h2>Section B — Les compétences</h2>") + '; ' +
  s("<h2>Section B — Les postures de leadership</h2>") + ')')
P('If(CurrentPosteID = "professionnel"; ' + competences + '; ' + postures + ')')

# Section C
fc = 'Filter(colValeurs; Coche)'
P(s("<h2>Section C — Les grands fondements et les valeurs organisationnelles</h2>"))
P(vide(f'CountRows({fc}) = 0',
       s("<table><tr><th>Thème</th><th>Exemples d'application</th><th>Commentaires</th></tr>") +
       f' & Concat(Sort({fc}; Ordre); "<tr><td><b>" & Label & "</b></td><td>" & {E("Ex1")} & "</td><td>" & {E("Ex2")} & "</td></tr>") & ' +
       s("</table>"), "Aucun thème coché."))

# Section D
P(s("<h2>Section D — Le développement des compétences</h2><h3>Résultats des actions de développement réalisées</h3>"))
fp = 'Filter(colDevPrecedents; Objectif <> "" Or Moyens <> "" Or Impacts <> "")'
P(vide(f'CountRows({fp}) = 0',
       s("<table><tr><th>Objectifs précédents</th><th>Moyens choisis</th><th>Impacts / résultats</th></tr>") +
       f' & Concat({fp}; "<tr><td>" & {E("Objectif")} & "</td><td>" & {E("Moyens")} & "</td><td>" & {E("Impacts")} & "</td></tr>") & ' +
       s("</table>")))
P(s("<h3>Nouveaux besoins et moyens de développement</h3>"))
fn = 'Filter(colDevNouveaux; Besoin <> "" Or Moyen <> "")'
P(vide(f'CountRows({fn}) = 0',
       s("<table><tr><th>Besoins de développement</th><th>Moyens de développement</th></tr>") +
       f' & Concat({fn}; "<tr><td>" & {E("Besoin")} & "</td><td>" & {E("Moyen")} & "</td></tr>") & ' +
       s("</table>")))

# Sections E, F, évaluation globale
for titre, champ in [("Section E — Bilan annuel complété par le supérieur immédiat", 'Coalesce(txtBilanSup.Text; varDossier.BilanSuperieur)'),
                     ("Section F — Bilan annuel complété par la personne en appréciation", 'Coalesce(txtBilanPersonne.Text; varDossier.BilanPersonne)')]:
    P(s(f"<h2>{titre}</h2>"))
    P(f'If(IsBlank({champ}); {s("<p class=vide>Non rempli.</p>")}; "<div class=bloc>" & {E(champ)} & "</div>")')
P(s("<h2>Évaluation globale</h2>"))
P('If(IsBlank(varEvalGlobale); ' + s("<p class=vide>Non remplie.</p>") +
  '; "<p><b>" & varEvalGlobale & "</b><br><span class=desc>" & LookUp(colEvalGlobale; Label = varEvalGlobale).Desc & "</span></p>")')

# Section G
P(s("<h2>Section G — Avis, certification et approbations</h2><table><tr><th>Étape</th><th>Personne</th><th>Date</th></tr>"))
def g(etape, qui, date):
    return f'"<tr><td>{etape}</td><td>" & {qui} & "</td><td>" & {d(date)} & "</td></tr>"'
P(g("Avis au supérieur immédiat", 'Coalesce(varDossier.PersonneAppreciation.DisplayName; "—")', 'varDossier.AviseLe'))
P(g("Certification (personne en appréciation)", 'Coalesce(varDossier.PersonneAppreciation.DisplayName; "—")', 'varDossier.CertifieLe'))
P(g("Approbation du supérieur immédiat", 'Coalesce(varDossier.SuperieurImmediat.DisplayName; "—")', 'varDossier.ApprouveSILe'))
P(g("Approbation du supérieur hiérarchique", 'Coalesce(varDossier.SuperieurHierarchique.DisplayName; "—")', 'varDossier.ApprouveSHLe'))
P('If(chkDirRequis.Checked; ' + g("Approbation du directeur", 'Coalesce(varDossier.Directeur.DisplayName; "—")', 'varDossier.ApprouveDirLe') + '; "")')
P(g("Transmis aux RH", '"—"', 'varDossier.TransmisPaieLe'))
P(s("</table><p class=pied>Document produit le ") + ' & Text(Now(); "d mmmm yyyy") & " à " & Text(Now(); "hh:mm") & ' +
  s(" à partir de l'application Appréciation de la contribution. Version du formulaire : 15 octobre 2026.</p></body></html>"))

# ---------------------------------------------------------------------------
# PDF « Plan de développement » (bouton « Imprimer ce plan » de l'onglet Plan)
# ---------------------------------------------------------------------------
plan = []
Q = plan.append
Q(parts[0])
Q(s("<h1>Plan de développement</h1><p class=sous>") + ' & LookUp(colPostes; PosteID = CurrentPosteID).PosteLabel & ' +
  s(" — dossier no ") + ' & varDossier.ID & ' + s("</p><table>"))
Q(ligne("Nom, prénom", E('Coalesce(txtNom.Text; varDossier.Title)')))
Q(ligne("Poste", E('Coalesce(txtPoste.Text; varDossier.Poste)')))
Q(ligne("Supérieur(e) immédiat(e)", 'Coalesce(varDossier.SuperieurImmediat.DisplayName; "—")'))
Q(ligne("Année", 'Coalesce(Text(varDossier.Annee); Text(Year(Today())))'))
Q(s("</table><h2>Objectifs pour l'année à venir</h2>"))
Q(vide(f'CountRows({fv}) = 0',
       s("<table><tr><th>Objectifs à venir</th><th>Indicateurs de mesure</th></tr>") +
       f' & Concat({fv}; "<tr><td>" & {E("Objectif")} & "</td><td>" & {E("Indicateur")} & "</td></tr>") & ' +
       s("</table>")))
Q(s("<h2>Développement des compétences — résultats des actions réalisées</h2>"))
Q(vide(f'CountRows({fp}) = 0',
       s("<table><tr><th>Objectifs précédents</th><th>Moyens choisis</th><th>Impacts / résultats</th></tr>") +
       f' & Concat({fp}; "<tr><td>" & {E("Objectif")} & "</td><td>" & {E("Moyens")} & "</td><td>" & {E("Impacts")} & "</td></tr>") & ' +
       s("</table>")))
Q(s("<h2>Nouveaux besoins et moyens de développement</h2>"))
Q(vide(f'CountRows({fn}) = 0',
       s("<table><tr><th>Besoins de développement</th><th>Moyens de développement</th></tr>") +
       f' & Concat({fn}; "<tr><td>" & {E("Besoin")} & "</td><td>" & {E("Moyen")} & "</td></tr>") & ' +
       s("</table>")))
Q(s("<p class=pied>Document produit le ") + ' & Text(Now(); "d mmmm yyyy") & " à " & Text(Now(); "hh:mm") & ' +
  s(" à partir de l'application Appréciation de la contribution.</p></body></html>"))

# Une seule longue chaîne de « & » dépasse la profondeur permise par Power Apps
# (« L'imbrication d'expressions est trop profonde ») : on assemble donc la page
# morceau par morceau dans la variable varHtmlPDF.
def formule(morceaux, titre, nom):
    etapes = ['Set(varHtmlPDF; ' + morceaux[0] + ')'] + \
             ['Set(varHtmlPDF; varHtmlPDF & ' + x + ')' for x in morceaux[1:]]
    assemblage = ';;\n    '.join(etapes)
    return f"""// {titre}
// 1) assemble la page HTML dans varHtmlPDF ; 2) le flux GenererPDFAppreciation la convertit
// en PDF et la joint au dossier (liste Appreciations) en remplaçant la version précédente ;
// 3) le bouton « 📄 Ouvrir le PDF » (ou Mes dossiers) l'ouvre.
If(IsBlank(varDossier);
    Notify("Enregistrez d'abord le dossier avec « Enregistrer et déposer »."; NotificationType.Warning);
    Set(varLienPDF; Blank());;
    Notify("Création du PDF en cours… Comptez de 10 à 30 secondes."; NotificationType.Information);;
    {assemblage};;
    Set(varLienPDF;
        GenererPDFAppreciation.Run(
            {nom};
            varHtmlPDF;
            varDossier.ID).lien);;
    If(IsBlank(varLienPDF);
        Notify("Le PDF n'a pas pu être créé. Réessayez dans un moment."; NotificationType.Error);
        Notify("PDF prêt : cliquez sur « 📄 Ouvrir le PDF »."; NotificationType.Success)))
"""

import os
ici = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(ici, 'btnApercuPDF-OnSelect.txt'), 'w').write(
    formule(parts, "btnApercuPDF.OnSelect — PDF de l'appréciation complète",
            '"Appreciation_dossier" & varDossier.ID'))
open(os.path.join(ici, 'btnImprimer-Plan-OnSelect.txt'), 'w').write(
    formule(plan, "btnImprimer.OnSelect (onglet Plan) — PDF du plan de développement",
            '"Plan_developpement_dossier" & varDossier.ID'))
print("btnApercuPDF-OnSelect.txt et btnImprimer-Plan-OnSelect.txt écrits")
