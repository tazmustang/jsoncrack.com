# -*- coding: utf-8 -*-
"""Génère les écrans Power Apps (.pa.yaml) et les formules de l'objet App."""
import os
from pa import C, s, uniq, label, rect, button, pill, cont, card_props, emit_screen, INPUT_STYLE
from formbuilder import Form
from gen_commun import PALETTE, SFMQ
import textes

HB = 64      # hauteur du bandeau or
HT = 52      # barre d'outils
HS = 76      # barre d'étapes
HO = 44      # onglets

# ======================================================================= Étapes (7 cercles)
ETAPES = '''Switch(varDossier.TypeFormulaire,
  "Situation dangereuse", Table(
    {n: 1, t: "Signalement", d: varDossier.DateDeclaration},
    {n: 2, t: "Prise en charge", d: varDossier.DateEnquete},
    {n: 3, t: "Mesure corrective", d: varDossier.DatePlanAction},
    {n: 4, t: "Fermeture", d: varDossier.DateFermeture}),
  "Violence", Table(
    {n: 1, t: "Déclaration", d: varDossier.DateDeclaration},
    {n: 2, t: "Mesures immédiates", d: varDossier.DateMesures},
    {n: 3, t: "Approbation employé", d: varDossier.DateApprobation},
    {n: 4, t: "Suivi SST / Bouclier", d: varDossier.DateEnquete},
    {n: 5, t: "Fermeture", d: varDossier.DateFermeture}),
  Table(
    {n: 1, t: "Déclaration", d: varDossier.DateDeclaration},
    {n: 2, t: "Mesures immédiates", d: varDossier.DateMesures},
    {n: 3, t: "Approbation employé", d: varDossier.DateApprobation},
    {n: 4, t: "Enquête", d: varDossier.DateEnquete},
    {n: 5, t: "Analyse 5 Pourquoi", d: varDossier.DateAnalyse},
    {n: 6, t: "Plan d'action", d: varDossier.DatePlanAction},
    {n: 7, t: "Fermeture", d: varDossier.DateFermeture}))'''

COULEUR_TYPE = 'Switch(%s, "Accident", cBleu, "Incident", cSarcelle, "Situation dangereuse", cOr, "Violence", cViolet, cTexte2)'


def stepbar(p, y):
    w = 150
    tpl = [
        rect(p + '_stpLigne', 'If(!IsBlank(LookUp(%s, n = ThisItem.n + 1).d), cVert, cBordure)' % ETAPES.replace('\n', ' '),
             X=w / 2, Y=21, Width=w, Height=3, Visible='ThisItem.n < CountRows(%s)' % ETAPES.replace('\n', ' ')),
        pill(p + '_stpRond', 'If(IsBlank(ThisItem.d), Text(ThisItem.n), "✓")', 'If(IsBlank(ThisItem.d), cGrisLib, cVert)',
             X=w / 2 - 16, Y=6, Width=32, Height=32, Size=12,
             RadiusTopLeft=16, RadiusTopRight=16, RadiusBottomLeft=16, RadiusBottomRight=16),
        label(p + '_stpNom', 'ThisItem.t', X=0, Y=40, Width=w, Height=18, Size=10, Align='Align.Center',
              Color='If(IsBlank(ThisItem.d), cTexte2, cTexte)', FontWeight='FontWeight.Semibold'),
        label(p + '_stpDate', 'If(IsBlank(ThisItem.d), "", Text(ThisItem.d, "yyyy-mm-dd"))', X=0, Y=56, Width=w,
              Height=16, Size=9, Align='Align.Center', Color='cTexte2'),
    ]
    return [
        C(uniq(p + '_galEtapes'), 'gal', {
            'Items': ETAPES, 'TemplateSize': w, 'TemplatePadding': 0, 'ShowScrollbar': False,
            'X': 'Max(210, (Parent.Width - %d * CountRows(%s)) / 2)' % (w, ETAPES.replace('\n', ' ')), 'Y': y,
            'Width': '%d * CountRows(%s)' % (w, ETAPES.replace('\n', ' ')),
            'Height': HS - 4, 'BorderThickness': 0}, tpl, 'Horizontal'),
        pill(p + '_pilNo', 'If(IsBlank(varDossier.ID), "Nouveau dossier", "Dossier n° " & varDossier.ID)', 'cBleuPale',
             'cMarine', X=24, Y=y + 6, Width=170),
        pill(p + '_pilStatut', 'Coalesce(varDossier.Statut, "Brouillon")', 'cBordure', 'cMarine', X=24, Y=y + 40, Width=170),
    ]


def header(p, titre, sous_titre, boutons_droite=(), etapes=False, retour=True):
    """Bandeau or + barre d'outils (+ étapes)."""
    cs = [
        rect(p + '_bandeau', 'cOr', X=0, Y=0, Width='Parent.Width', Height=HB),
        label(p + '_titre', s(titre) if not titre.startswith('=') else titre[1:], X=0, Y=6, Width='Parent.Width',
              Height=32, Size=20, FontWeight='FontWeight.Bold', Color='Color.White', Align='Align.Center'),
        label(p + '_sousTitre', sous_titre, X=0, Y=36, Width='Parent.Width', Height=22, Size=12, Color='Color.White',
              Align='Align.Center'),
        pill(p + '_pilRole', '"👤 " & varRole', 'cVert', X='Parent.Width - 224', Y=18, Width=200),
        rect(p + '_barre', 'Color.White', X=0, Y=HB, Width='Parent.Width', Height=HT),
        rect(p + '_barreLigne', 'cBordure', X=0, Y=HB + HT - 1, Width='Parent.Width', Height=1),
    ]
    x = 24
    if retour:
        cs.append(button(p + '_btnAccueil', '"🏠 Accueil"', 'Navigate(scrAccueil, ScreenTransition.None)', 'contour',
                         'cBleu', X=x, Y=HB + 8, Width=120, Height=36))
        x += 128
        cs.append(button(p + '_btnDossiers', '"📂 Mes dossiers"', 'Navigate(scrDossiers, ScreenTransition.None)',
                         'contour', 'cBleu', X=x, Y=HB + 8, Width=150, Height=36))
        x += 158
    cs.append(button(p + '_btnAide', '"❓ Comment remplir"', 'Navigate(scrAide, ScreenTransition.None)', 'plein', 'cOr',
                     X=x, Y=HB + 8, Width=170, Height=36))
    xr = 24
    for (nm, txt, act, style, col, w) in boutons_droite:
        xr += w
        cs.append(button(p + '_' + nm, txt, act, style, col, X='Parent.Width - %d' % xr, Y=HB + 8, Width=w - 8, Height=36))
    if etapes:
        cs += [rect(p + '_fondEtapes', 'Color.White', X=0, Y=HB + HT, Width='Parent.Width', Height=HS)]
        cs += stepbar(p, HB + HT + 2)
        cs.append(rect(p + '_ligneEtapes', 'cBordure', X=0, Y=HB + HT + HS - 1, Width='Parent.Width', Height=1))
    return cs


BTN_NOUVEAU = ('btnNouveau', '"📝 Nouveau formulaire"', 'Navigate(scrAccueil, ScreenTransition.None)', 'contour', 'cRouge', 210)


def body(name, y, children, visible=None, x=24, width='Parent.Width - 48'):
    p = card_props()
    p.update({'X': x, 'Y': y, 'Width': width, 'Height': 'Parent.Height - %d' % (y + 16) if isinstance(y, int) else 'Parent.Height - Self.Y - 16',
              'LayoutDirection': 'LayoutDirection.Vertical', 'LayoutGap': 6,
              'LayoutAlignItems': 'LayoutAlignItems.Stretch', 'LayoutOverflowY': 'LayoutOverflow.Scroll',
              'PaddingTop': 16, 'PaddingBottom': 32, 'PaddingLeft': 'Max(24, (Self.Width - 940) / 2)',
              'PaddingRight': 'Max(24, (Self.Width - 940) / 2)'})
    if visible:
        p['Visible'] = visible
    c = cont(name, 'AutoLayout', children, **p)
    return c


def nav_row(name, prev=None, nxt=None, extra=()):
    kids = []
    if prev:
        kids.append(button(name + 'Prec', '"← Précédent"', prev, 'contour', 'cBleu', Width=150, Height=38))
    for e in extra:
        kids.append(e)
    if nxt:
        kids.append(button(name + 'Suiv', '"Suivant →"', nxt, 'plein', 'cBleu', Width=150, Height=38))
    return cont(name, 'AutoLayout', kids, LayoutDirection='LayoutDirection.Horizontal', LayoutGap=12,
                LayoutJustifyContent='LayoutJustifyContent.End', LayoutAlignItems='LayoutAlignItems.Center',
                Height=60, PaddingTop=16, FillPortions=0)


def screen_props(onvisible=''):
    d = {'Fill': 'cFond'}
    if onvisible:
        d['OnVisible'] = onvisible
    return d


RESET = 'UpdateContext({locReset: true});\nUpdateContext({locReset: false})'

# ======================================================================= Sauvegarde générique
def save_formula(f, type_expr, titre_expr, deposer, extra=None, apres_depot='Set(varAutoEnvoi, true);\n  Navigate(scrApercu, ScreenTransition.None)'):
    sys_ = {
        'TypeFormulaire': type_expr,
        'Title': titre_expr,
        'CreeParCourriel': 'Coalesce(varDossier.CreeParCourriel, varMoi)',
        'CreeParNom': 'Coalesce(varDossier.CreeParNom, User().FullName)',
    }
    sys_.update(extra or {})
    if deposer:
        sys_['Statut'] = 'If(IsBlank(varDossier.Statut) || varDossier.Statut = "Brouillon", "Déposé", varDossier.Statut)'
        sys_['DateDeclaration'] = 'Coalesce(varDossier.DateDeclaration, Today())'
    else:
        sys_['Statut'] = 'Coalesce(varDossier.Statut, "Brouillon")'
    rec = f.patch_record(sys_)
    patch = ('IfError(\n  Set(varDossier, Patch(SST_Dossiers, If(IsBlank(varDossier.ID), Defaults(SST_Dossiers), varDossier),\n  %s));\n  ' % rec)
    if deposer:
        body_ = patch + 'Notify("Dossier n° " & varDossier.ID & " déposé.", NotificationType.Success);\n  ' + apres_depot + \
            ',\n  Notify("Erreur d\'enregistrement : " & FirstError.Message, NotificationType.Error))'
        return 'UpdateContext({locManquants: %s});\nIf(!IsBlank(locManquants),\n  Notify("Champs obligatoires à compléter : " & locManquants, NotificationType.Error),\n  %s)' % (f.manquants(), body_)
    return patch + 'Notify("Brouillon enregistré (dossier n° " & varDossier.ID & ").", NotificationType.Success),\n  Notify("Erreur d\'enregistrement : " & FirstError.Message, NotificationType.Error))'


# ======================================================================= Champs communs employé
def champs_employe(f, req_cond='true', avec_courriel=True, prefix_lbl=''):
    f.text('EmpNom', 'Nom de l\'employé', req=req_cond)
    f.text('EmpPrenom', 'Prénom de l\'employé', req=req_cond)
    f.text('EmpID', 'ID de l\'employé', req=req_cond, aide='Inscrire les 6 chiffres de l\'ID (incluant le ou les 0).',
           width=200, maxlen=6)
    f.valid.append(('ID de l\'employé (6 chiffres)', 'true', '!IsMatch(%s.Text, "\\d{6}")' % f.ctl('EmpID')))
    champs_org(f, req_cond)
    f.drop('EmpSyndicat', 'Syndicat auquel l\'employé est rattaché', 'Sort(Filter(colListes, Liste = "Syndicat"), Ordre).Value', req=req_cond)
    syn = f.val('EmpSyndicat')
    f.drop('EmpClasse', 'Classe d\'emploi (SFMQ) de l\'employé', 'Sort(Filter(colListes, Liste = "ClasseSFMQ"), Ordre).Value',
           req=req_cond, visible='%s = %s' % (syn, s(SFMQ)))
    titres = 'Sort(Filter(colTitres, Syndicat = %s && (IsBlank(Classe) || Classe = %s)), Ordre).Value' % (syn, f.val('EmpClasse'))
    f.drop('EmpTitre', 'Titre d\'emploi de l\'employé', titres, req=req_cond,
           visible='!IsBlank(%s) && CountRows(%s) > 0' % (syn, titres))
    f.text('EmpTitreAutre', 'Titre d\'emploi (préciser)', req=req_cond,
           visible='!IsBlank(%s) && (CountRows(%s) = 0 || %s = "Autre")' % (syn, titres, f.val('EmpTitre')))
    if avec_courriel:
        pass
    return syn


def champs_org(f, req_cond='true'):
    f.drop('EmpService', 'Service auquel est rattaché l\'employé (unité administrative)',
           'Sort(Filter(colListes, Liste = "Service"), Ordre).Value', req=req_cond)
    svc = f.val('EmpService')
    for col, niv in (('EmpDirection', 'Direction'), ('EmpDivision', 'Division'), ('EmpSection', 'Section')):
        items = 'Sort(Filter(colOrg, Service = %s && Niveau = "%s"), Ordre).Value' % (svc, niv)
        f.drop(col, niv, items, visible='CountRows(%s) > 0' % items)


# ======================================================================= Écran : Accueil
def scr_accueil():
    p = 'acc0'
    cs = header(p, 'Santé et sécurité au travail', '"Déclarations, enquêtes et analyses d\'évènements"', retour=False,
                boutons_droite=[('btnDossiers', '"📂 Mes dossiers"', 'Navigate(scrDossiers, ScreenTransition.None)', 'contour', 'cBleu', 170),
                                ('btnApropos', '"ℹ️ À propos"', 'Navigate(scrAide, ScreenTransition.None, {locAideOnglet: 5})', 'contour', 'cBleu', 140)])
    y = HB + HT + 16
    cs.append(C(uniq(p + '_imgMarque'), 'image', {
        'Image': '""', 'X': '(Parent.Width - 520) / 2', 'Y': y, 'Width': 520, 'Height': 60,
        'ImagePosition': 'ImagePosition.Fit', 'Visible': '!IsBlank(Self.Image)'}))
    y2 = y + 70
    cs.append(label(p + '_lblVous', '"VOUS ÊTES :"', X='(Parent.Width - 640) / 2', Y=y2, Width=120, Height=36, Size=11,
                    FontWeight='FontWeight.Bold', Color='cTexte2'))
    roles = [('Gestionnaire', 'true'), ('Employé', 'true'), ('Conseiller SST', 'varEstSST')]
    for i, (r, vis) in enumerate(roles):
        cs.append(button(p + '_btnRole%d' % i, s(r), 'Set(varRole, %s)' % s(r), 'plein', 'If(varRole = %s, cVert, Color.White)' % s(r),
                         Color='If(varRole = %s, Color.White, cVert)' % s(r), BorderColor='cVert', BorderThickness=2,
                         HoverFill='If(varRole = %s, ColorFade(cVert, -0.15), cBleuPale)' % s(r),
                         HoverColor='If(varRole = %s, Color.White, cVert)' % s(r),
                         X='(Parent.Width - 640) / 2 + %d' % (130 + i * 172), Y=y2, Width=160, Height=36, Visible=vis))
    # Cartes des formulaires
    cartes = [
        ('Acc', 'Accident ou incident de travail', textes.CARTE_ACCIDENT, 'cBleu', 'varRole <> "Employé"',
         'Set(varDossier, Defaults(SST_Dossiers)); Set(varNouveauType, "Accident"); Navigate(scrAccident, ScreenTransition.None)', '🩹'),
        ('Sit', 'Situation dangereuse', textes.CARTE_SITUATION, 'cOr', 'true',
         'Set(varDossier, Defaults(SST_Dossiers)); Navigate(scrSituation, ScreenTransition.None)', '⚠️'),
        ('Vio', 'Évènement traumatisant ou acte de violence', textes.CARTE_VIOLENCE, 'cViolet', 'varRole <> "Employé"',
         'Set(varDossier, Defaults(SST_Dossiers)); Navigate(scrViolence, ScreenTransition.None)', '🛡️'),
    ]
    kids = []
    for k, t, d, col, vis, act, ico in cartes:
        kids.append(cont(p + '_carte' + k, 'ManualLayout', [
            rect(p + '_barre' + k, col, X=0, Y=0, Width=6, Height='Parent.Height'),
            label(p + '_ico' + k, s(ico), X=20, Y=16, Width=50, Height=40, Size=24),
            label(p + '_tit' + k, s(t), X=20, Y=60, Width='Parent.Width - 40', Height=52, Size=15,
                  FontWeight='FontWeight.Bold', Color='cMarine', Wrap=True, VerticalAlign='VerticalAlign.Top'),
            label(p + '_des' + k, s(d), X=20, Y=112, Width='Parent.Width - 40', Height=92, Size=11, Color='cTexte2',
                  Wrap=True, VerticalAlign='VerticalAlign.Top'),
            button(p + '_btn' + k, '"Commencer →"', act, 'plein', col, X=20, Y='Parent.Height - 56', Width='Parent.Width - 40', Height=38),
        ], Width=320, Height=270, Visible=vis, FillPortions=0, **card_props()))
    cs.append(cont(p + '_cartes', 'AutoLayout', kids, X=24, Y=y2 + 60, Width='Parent.Width - 48', Height=290,
                   LayoutDirection='LayoutDirection.Horizontal', LayoutGap=20,
                   LayoutJustifyContent='LayoutJustifyContent.Center', LayoutAlignItems='LayoutAlignItems.Start'))
    cs.append(label(p + '_urgence', s(textes.URGENCE), X='(Parent.Width - 1000) / 2', Y=y2 + 360, Width=1000, Height=60,
                    Size=11, Color='cMarine', Fill='cBleuPale', Align='Align.Center', Wrap=True,
                    BorderColor='cBordure', BorderThickness=1))
    cs.append(label(p + '_pied', '"© Ville de Québec — Division de la santé et de la sécurité au travail · Version " & cVersion',
                    X=0, Y='Parent.Height - 30', Width='Parent.Width', Height=24, Size=9, Color='cTexte2', Align='Align.Center'))
    return emit_screen('scrAccueil', screen_props(), cs)


# ======================================================================= Écran : Mes dossiers
def scr_dossiers():
    p = 'dos'
    cs = header(p, 'Mes dossiers', 'If(varRole = "Conseiller SST", "Tous les dossiers (conseiller SST)", "Dossiers que vous avez créés")',
                boutons_droite=[BTN_NOUVEAU])
    y = HB + HT + 12
    style = dict(INPUT_STYLE)
    cs.append(label(p + '_lblType', '"Type"', X=24, Y=y, Width=200, Height=20, Size=10, Color='cTexte2', FontWeight='FontWeight.Semibold'))
    cs.append(C(uniq(p + '_drpType'), 'drop', {'Items': '["Tous", "Accident", "Incident", "Situation dangereuse", "Violence"]',
                                              'X': 24, 'Y': y + 20, 'Width': 220, 'Height': 36, 'ChevronBackground': 'cBleu', 'SelectionFill': 'cBleu',
                                              'BorderColor': 'cBordure', 'Size': 11}))
    cs.append(label(p + '_lblStatut', '"Statut"', X=260, Y=y, Width=200, Height=20, Size=10, Color='cTexte2', FontWeight='FontWeight.Semibold'))
    cs.append(C(uniq(p + '_drpStatut'), 'drop', {'Items': 'Ungroup(Table({t: ["Tous"]}, {t: Sort(Filter(colListes, Liste = "Statut"), Ordre).Value}), t)',
                                                'X': 260, 'Y': y + 20, 'Width': 220, 'Height': 36, 'ChevronBackground': 'cBleu', 'SelectionFill': 'cBleu',
                                                'BorderColor': 'cBordure', 'Size': 11}))
    cs.append(label(p + '_lblRech', '"Recherche (nom de l\'employé, début)"', X=496, Y=y, Width=300, Height=20, Size=10, Color='cTexte2', FontWeight='FontWeight.Semibold'))
    style.update({'X': 496, 'Y': y + 20, 'Width': 300, 'Height': 36, 'HintText': '"ex. : Tremblay"', 'Default': '""', 'Size': 11})
    cs.append(C(uniq(p + '_txtRech'), 'text', style))
    items = '''SortByColumns(Filter(SST_Dossiers,
  (varRole = "Conseiller SST" || CreeParCourriel = varMoi) &&
  (dos_drpType.Selected.Value = "Tous" || TypeFormulaire = dos_drpType.Selected.Value) &&
  (dos_drpStatut.Selected.Value = "Tous" || Statut = dos_drpStatut.Selected.Value) &&
  (IsBlank(dos_txtRech.Text) || StartsWith(EmpNom, dos_txtRech.Text))),
  "ID", SortOrder.Descending)'''
    nb_etapes = 'Switch(ThisItem.TypeFormulaire, "Situation dangereuse", 4, "Violence", 5, 7)'
    faites = ('CountRows(Filter(Table({d: ThisItem.DateDeclaration}, {d: If(ThisItem.TypeFormulaire <> "Situation dangereuse", ThisItem.DateMesures)}, '
              '{d: If(ThisItem.TypeFormulaire <> "Situation dangereuse", ThisItem.DateApprobation)}, {d: ThisItem.DateEnquete}, '
              '{d: If(ThisItem.TypeFormulaire in ["Accident", "Incident"], ThisItem.DateAnalyse)}, '
              '{d: If(ThisItem.TypeFormulaire <> "Violence", ThisItem.DatePlanAction)}, {d: ThisItem.DateFermeture}), !IsBlank(d)))')
    tpl = [
        rect(p + '_carte', 'Color.White', X=0, Y=0, Width='Parent.TemplateWidth', Height='Parent.TemplateHeight - 8',
             BorderColor='cBordure', BorderThickness=1),
        rect(p + '_barreType', COULEUR_TYPE % 'ThisItem.TypeFormulaire', X=0, Y=0, Width=6, Height='Parent.TemplateHeight - 8'),
        label(p + '_galTitre', '"N° " & ThisItem.ID & " — " & Coalesce(ThisItem.Title, "(sans titre)")', X=20, Y=8,
              Width='Parent.TemplateWidth - 420', Height=28, Size=13, FontWeight='FontWeight.Semibold', Color='cMarine'),
        label(p + '_galDetails', '"Évènement : " & Coalesce(Text(ThisItem.EvtDate, "yyyy-mm-dd"), "—") & "   ·   Déposé : " & Coalesce(Text(ThisItem.DateDeclaration, "yyyy-mm-dd"), "—") & "   ·   Créé par : " & ThisItem.CreeParNom',
              X=20, Y=38, Width='Parent.TemplateWidth - 420', Height=24, Size=10.5, Color='cTexte2'),
        pill(p + '_galType', 'ThisItem.TypeFormulaire', COULEUR_TYPE % 'ThisItem.TypeFormulaire', X='Parent.TemplateWidth - 400', Y=10, Width=170),
        pill(p + '_galStatut', 'Coalesce(ThisItem.Statut, "Brouillon")', 'cBordure', 'cMarine', X='Parent.TemplateWidth - 220', Y=10, Width=150),
        label(p + '_galEtapes', '"Étapes : " & %s & " / " & %s' % (faites, nb_etapes), X='Parent.TemplateWidth - 400', Y=42,
              Width=330, Height=22, Size=10, Color='cTexte2', Align='Align.Right'),
        label(p + '_galChevron', '"›"', X='Parent.TemplateWidth - 50', Y=10, Width=40, Height=50, Size=26, Color='cBleu'),
    ]
    yg = y + 72
    cs.append(C(uniq(p + '_galDossiers'), 'gal', {
        'Items': items, 'TemplateSize': 84, 'TemplatePadding': 0, 'X': 24, 'Y': yg, 'Width': 'Parent.Width - 48',
        'Height': 'Parent.Height - %d' % (yg + 16), 'OnSelect': 'Set(varDossier, ThisItem); Navigate(scrApercu, ScreenTransition.None)',
        'BorderThickness': 0}, tpl, 'Vertical'))
    cs.append(label(p + '_vide', '"Aucun dossier à afficher."', X=24, Y=yg + 20, Width='Parent.Width - 48', Height=40,
                    Color='cTexte2', Align='Align.Center', Visible='CountRows(dos_galDossiers.AllItems) = 0', Italic=True))
    return emit_screen('scrDossiers', screen_props(), cs)


# ======================================================================= Écran : Accident / incident
def schema_corps(f):
    """Schéma du corps cliquable : image SVG + 26 zones transparentes."""
    from zones import ZONES, svg_expr
    p = f.p
    kids = [
        button(p + '_btnFace', '"Vue de face"', 'Set(varVue, "face")', 'plein', 'If(varVue = "face", cBleu, Color.White)',
               Color='If(varVue = "face", Color.White, cBleu)', BorderColor='cBleu', BorderThickness=2,
               HoverFill='If(varVue = "face", ColorFade(cBleu, -0.15), cBleuPale)', HoverColor='If(varVue = "face", Color.White, cBleu)',
               X=0, Y=0, Width=110, Height=32),
        button(p + '_btnDos', '"Vue de dos"', 'Set(varVue, "dos")', 'plein', 'If(varVue = "dos", cBleu, Color.White)',
               Color='If(varVue = "dos", Color.White, cBleu)', BorderColor='cBleu', BorderThickness=2,
               HoverFill='If(varVue = "dos", ColorFade(cBleu, -0.15), cBleuPale)', HoverColor='If(varVue = "dos", Color.White, cBleu)',
               X=118, Y=0, Width=110, Height=32),
        C(uniq(p + '_imgCorps'), 'image', {'Image': svg_expr(), 'X': 14, 'Y': 44, 'Width': 200, 'Height': 400,
                                          'ImagePosition': 'ImagePosition.Fit', 'PaddingTop': 0, 'PaddingBottom': 0,
                                          'PaddingLeft': 0, 'PaddingRight': 0}),
    ]
    for i, z in enumerate(ZONES):
        idf, idd, x, y, w, h = z['f'], z['d'], z['x'], z['y'], z['w'], z['h']
        zid = 'If(varVue = "face", "%s", "%s")' % (idf, idd)
        kids.append(button(p + '_zone%02d' % i, '""',
                           'With({z: %s}, If(varB1Zone = z, Set(varB1Zone, ""), varB2Zone = z, Set(varB2Zone, ""), IsBlank(varB1Zone), Set(varB1Zone, z), Set(varB2Zone, z)))' % zid,
                           'plein', 'Color.Transparent', HoverFill='RGBA(7, 75, 152, 0.25)', PressedFill='RGBA(7, 75, 152, 0.4)',
                           X=14 + x, Y=44 + y, Width=w, Height=h, Tooltip='LookUp(tZones, Id = %s, Libelle)' % zid,
                           AccessibleLabel='LookUp(tZones, Id = %s, Libelle)' % zid,
                           RadiusTopLeft=0, RadiusTopRight=0, RadiusBottomLeft=0, RadiusBottomRight=0))
    leg = ('"■ Blessure principale : " & Coalesce(LookUp(tZones, Id = varB1Zone, Libelle), "—") & Char(10) & '
           '"■ Blessure secondaire : " & Coalesce(LookUp(tZones, Id = varB2Zone, Libelle), "—") & Char(10) & Char(10) & '
           '"Cliquez une zone pour la blessure principale, puis une autre pour la blessure secondaire. Cliquez de nouveau une zone pour la retirer."')
    kids.append(label(p + '_lgdCorps', leg, X=240, Y=44, Width='Parent.Width - 250', Height=160, Size=11, Wrap=True,
                      VerticalAlign='VerticalAlign.Top'))
    return cont(p + '_conCorps', 'ManualLayout', kids, Height=452, FillPortions=0, Visible='%s = "Accident"' % f.val('TypeFormulaire'))


def blessure(f, n, acc):
    z = 'varB%dZone' % n
    titre = 'Blessure principale' if n == 1 else 'Blessure secondaire (optionnelle)'
    f.section(titre, visible=acc)
    req = acc if n == 1 else False
    f.drop('B%dNature' % n, 'Description de la blessure (siège de la blessure)', 'Sort(Filter(colListes, Liste = "NatureBlessure"), Ordre).Value',
           req=req, visible=acc)
    f.drop('B%dPartie' % n, 'Partie du corps', 'Sort(Filter(colListes, Liste = "PartieCorps"), Ordre).Value', req=req, visible=acc,
           default='If(IsBlank(%s) || %s = varDossier.B%dZone, varDossier.B%dPartie, LookUp(tZones, Id = %s, Partie))' % (z, z, n, n, z))
    f.radio('B%dCote' % n, 'Côté', ['Gauche', 'Droit', 'Non applicable'], req=req, visible=acc,
            default='If(IsBlank(%s) || %s = varDossier.B%dZone, varDossier.B%dCote, LookUp(tZones, Id = %s, Cote))' % (z, z, n, n, z))
    f.text('B%dPrecision' % n, 'Précision (optionnel)', visible=acc)
    f.patch['B%dZone' % n] = z


def scr_accident():
    f = Form('acd')
    cat = 'acd_rdoTypeFormulaire.Selected.Value'
    acc = '%s = "Accident"' % cat
    # ---------------- Onglet 1 : Identification
    f.tab(1)
    f.section('Catégorie de déclaration')
    f.radio('TypeFormulaire', 'Catégorie de déclaration', ['Accident', 'Incident'], req=True,
            default='Coalesce(varDossier.TypeFormulaire, varNouveauType, "Accident")',
            aide='Accident = l\'employé a eu une blessure physique apparente ou non. Incident = passé proche : l\'employé aurait pu se blesser (aucune blessure ni douleur, sinon il s\'agit d\'un accident).')
    grav_items = 'Sort(Filter(colListes, Liste = "Gravite" && StartsWith(Value, %s)), Ordre).Value' % cat
    f.drop('Gravite', 'Niveau de gravité (accident) ou de gravité potentielle (incident)', grav_items, req=True,
           aide='=Concat(Sort(Filter(colListes, Liste = "Gravite" && StartsWith(Value, "Accident")), Ordre), Aide, Char(10))')
    f.radio('TrousseRemise', 'Avez-vous remis une trousse d\'assignation temporaire à votre employé ?', ['Oui', 'Non'], req=acc, visible=acc,
            aide='La trousse d\'assignation temporaire est obligatoire dans toutes les situations, à l\'exception d\'un incident.')
    f.text('TrousseRaison', 'Pour quelle raison la trousse d\'assignation temporaire n\'a pas été remise ?', multi=True, req=True,
           visible='%s && %s = "Non"' % (acc, 'acd_rdoTrousseRemise.Selected.Value'))
    f.radio('AbsenceAuDela', 'Selon les premières constatations, est-ce que cet accident impliquera une absence de l\'employé au-delà de sa journée de travail ?',
            ['Oui (cet accident impliquera une absence)', 'Non (employé au travail)'], vertical=True, req=acc, visible=acc)
    f.section('Identification de l\'employé impliqué')
    champs_employe(f)
    f.drop('EmpAdresseEtab', 'Adresse de l\'établissement auquel est rattaché l\'employé', 'Sort(Filter(colListes, Liste = "Adresse"), Ordre).Value', req=True,
           aide='Si l\'adresse n\'est pas dans la liste, choisir « Autre » et l\'inscrire comme ceci : 160, 76e Rue Est')
    f.text('EmpAdresseAutre', 'Adresse de l\'établissement (autre)', req=True, visible='acd_drpEmpAdresseEtab.Selected.Value = "Autre"')
    f.text('EmpSuperieur', 'Nom du supérieur immédiat', req=True)
    f.section('Personne qui remplit la déclaration')
    f.text('GestNom', 'Nom du gestionnaire', req=True, default='Coalesce(varDossier.GestNom, User().FullName)')
    f.text('GestTitre', 'Titre / fonction')
    f.check('RempliSeul', 'Formulaire rempli seul par le gestionnaire (l\'état de santé de l\'employé ne permet pas de le remplir avec lui aujourd\'hui)')
    f.info(textes.NOTE_REMPLI_SEUL, alerte=True, visible='acd_chkRempliSeul.Value')
    f.raw(nav_row('acd_nav1', nxt='UpdateContext({locOnglet: 2})'))
    # ---------------- Onglet 2 : Évènement
    f.tab(2)
    f.section('Description de l\'évènement')
    f.date('EvtDate', 'Date de l\'évènement', req=True)
    f.text('EvtHeure', 'Heure de l\'évènement', req=True, hint='ex. : 18:45', width=200)
    f.date('EvtDateDeclEmp', 'Date de déclaration de l\'employé', req=True,
           aide='Date à laquelle l\'employé a informé son gestionnaire ou toute autre personne en autorité de la survenue de l\'évènement.')
    f.text('EvtAdresse', 'Adresse où est survenu l\'évènement', req=True,
           aide='S\'il n\'y a aucune adresse, indiquer l\'adresse civique la plus proche de l\'évènement.')
    f.combo('Horaire', 'Horaire de travail au moment de l\'évènement', 'Sort(Filter(colListes, Liste = "Horaire"), Ordre).Value', req=True,
            aide='Plusieurs choix possibles (au plus 2 pour un incident).')
    f.valid.append(('Horaire : au plus 2 choix pour un incident', '%s = "Incident"' % cat, 'CountRows(acd_cmbHoraire.SelectedItems) > 2'))
    f.radio('Temoins', 'Est-ce qu\'il y a des témoins ?', ['Oui', 'Aucun'], req=True)
    f.text('TemoinsNoms', 'Nom du/des témoin(s)', multi=True, visible='acd_rdoTemoins.Selected.Value = "Oui"')
    f.radio('Vehicule', 'Véhicule / équipement motorisé impliqué lors de l\'évènement', ['Oui', 'Non', 'Autre'], req=True,
            aide='Répondre « Oui » si le véhicule appartient à la Ville, « Autre » s\'il s\'agit d\'un véhicule personnel.')
    f.text('VehiculeDesc', 'Description et numéro du véhicule / équipement motorisé impliqué',
           visible='acd_rdoVehicule.Selected.Value in ["Oui", "Autre"]')
    f.section('Description détaillée')
    f.text('Tache', 'Tâche au moment de l\'évènement', multi=True, req=True, aide=textes.AIDE_TACHE, height=70)
    f.text('Description', 'Description détaillée selon la version du travailleur', multi=True, req=True, maxlen=255,
           compteur=True, aide=textes.AIDE_MELITO, height=110)
    f.raw(nav_row('acd_nav2', prev='UpdateContext({locOnglet: 1})', nxt='UpdateContext({locOnglet: 3})'))
    # ---------------- Onglet 3 : Premiers soins
    f.tab(3)
    f.section('Registre des premiers soins')
    f.radio('PSDonnes', 'Est-ce que des premiers secours ont été donnés par un secouriste ou un paramédic ?', ['Oui', 'Non'], req=True)
    ps = 'acd_rdoPSDonnes.Selected.Value = "Oui"'
    f.text('PSHeure', 'Heure des premiers secours', hint='ex. : 18:45', width=200, visible=ps)
    f.text('PSNature', 'Nature des premiers secours', multi=True, maxlen=255, compteur=True, visible=ps)
    f.text('PSSecouriste', 'Nom du secouriste', visible=ps)
    f.radio('Transport', 'Moyen de transport utilisé', ['Aucun', 'Ambulance', 'Taxi', 'Autre'])
    f.text('TransportAutre', 'Préciser le moyen de transport', visible='acd_rdoTransport.Selected.Value = "Autre"')
    f.raw(nav_row('acd_nav3', prev='UpdateContext({locOnglet: 2})', nxt='UpdateContext({locOnglet: If(%s, 4, 5)})' % acc))
    # ---------------- Onglet 4 : Blessures
    f.tab(4)
    f.section('Localisation de la ou des blessures', visible=acc)
    f.info('Les côtés « gauche » et « droit » correspondent à la gauche et à la droite de l\'employé (vue de face : comme si vous vous regardiez dans un miroir).', visible=acc)
    f.raw(schema_corps(f))
    blessure(f, 1, acc)
    blessure(f, 2, acc)
    f.raw(nav_row('acd_nav4', prev='UpdateContext({locOnglet: 3})', nxt='UpdateContext({locOnglet: 5})'))
    # ---------------- Onglet 5 : Cause et mesures
    f.tab(5)
    f.section('Type et cause principale de l\'évènement')
    f.drop('CauseType', 'Description de la cause (type d\'évènement)', 'Sort(Filter(colListes, Liste = "CauseAccident"), Ordre).Value', req=True)
    f.drop('Activite', 'Description de l\'activité (activité principale lors de l\'évènement)', 'Sort(Filter(colListes, Liste = "Activite"), Ordre).Value', req=True)
    f.section('Mesures préventives immédiates')
    f.text('MesurePrev', 'Mesure préventive immédiate', multi=True, req=True, aide='Que doit-on mettre en place pour éviter d\'autres évènements ?')
    f.text('MesureResp', 'Responsable de la mesure préventive immédiate',
           aide='Indiquer le nom d\'un seul gestionnaire responsable. S\'il y a plus d\'une personne responsable, compléter le champ « Collaborateur(s) ».')
    f.text('MesureCollab', 'Nom du/des collaborateur(s)', multi=True, height=60)
    f.date('MesureEcheance', 'Date d\'échéance (fin souhaitée) de la mesure préventive immédiate', req=True)
    oblig = '("élevée" in acd_drpGravite.Selected.Value || "moyenne" in acd_drpGravite.Selected.Value)'
    f.radio('EnqueteRequise', 'Une enquête et analyse d\'évènement est-elle requise ?', ['Oui', 'Non'],
            default='If(%s, "Oui", varDossier.EnqueteRequise)' % oblig,
            display='If(%s, DisplayMode.Disabled, DisplayMode.Edit)' % oblig,
            aide='=If(%s, "Enquête OBLIGATOIRE : gravité élevée ou moyenne.", "Si oui, un plan d\'action de mesures correctives sera élaboré par un comité d\'enquête paritaire SST.")' % oblig)
    f.raw(nav_row('acd_nav5', prev='UpdateContext({locOnglet: If(%s, 4, 3)})' % acc, nxt='UpdateContext({locOnglet: 6})'))
    # ---------------- Onglet 6 : Arrêt et approbation
    f.tab(6)
    f.section('Arrêt de travail', visible=acc)
    f.radio('ArretTravail', 'Arrêt de travail ?', ['Oui', 'Non'], visible=acc)
    arr = '%s && acd_rdoArretTravail.Selected.Value = "Oui"' % acc
    f.date('DateDernierJour', 'Date du dernier jour travaillé', visible=arr)
    f.radio('RetourTravail', 'Retour au travail ?', ['Oui', 'Non'], visible=arr)
    ret = '%s && acd_rdoRetourTravail.Selected.Value = "Oui"' % arr
    f.date('DateRetour', 'Date du retour', visible=ret)
    f.radio('ModaliteRetour', 'Modalité de retour', ['Même emploi', 'Assignation temporaire', 'Autre'], visible=ret)
    f.section('Signature / consentement')
    f.radio('ApprobationEmp', 'Employé impliqué : « J\'étais présent(e) lorsque mon gestionnaire a complété ce formulaire. Il s\'agit de ma version des faits et je confirme que la description de l\'évènement est exacte. »',
            ['Oui', 'Non, pour des raisons médicales l\'employé est incapable de compléter sa déclaration'], vertical=True, req=True,
            aide='Approbation de l\'employé (fait office de signature).')
    f.radio('FormatCopie', 'Format souhaité pour la copie de la déclaration', ['Copie courriel', 'Copie papier', 'Copie courriel et papier'],
            vertical=True, req=True)
    em = '"courriel" in Lower(acd_rdoFormatCopie.Selected.Value)'
    f.text('EmpCourriel', 'Courriel de l\'employé', req=True, visible=em, aide='Inscrire un seul courriel (personnel ou Ville).')
    f.valid.append(('Courriel de l\'employé (format invalide)', em, '!IsMatch(acd_txtEmpCourriel.Text, Match.Email)'))
    f.info(textes.CONTACT_REPONDANT, alerte=True)
    titre = '%s & " – " & acd_txtEmpNom.Text & ", " & acd_txtEmpPrenom.Text & " – " & Text(acd_dteEvtDate.SelectedDate, "yyyy-mm-dd")' % cat
    extra = {
        'DateMesures': 'If(IsBlank(acd_txmMesurePrev.Text), varDossier.DateMesures, Coalesce(varDossier.DateMesures, Today()))',
        'DateApprobation': 'If(acd_rdoApprobationEmp.Selected.Value = "Oui", Coalesce(varDossier.DateApprobation, Today()), varDossier.DateApprobation)',
    }
    sauver = save_formula(f, cat, titre, False, extra)
    deposer = save_formula(f, cat, titre, True, extra)
    f.raw(nav_row('acd_nav6', prev='UpdateContext({locOnglet: 5})', extra=[
        button('acd_btnDeposerBas', '"☁️ Enregistrer et déposer"', deposer, 'plein', 'cVert', Width=240, Height=38)]))

    # ---------------- Écran
    onglets = ['1. Identification', '2. Évènement', '3. Premiers soins', '4. Blessures', '5. Cause et mesures', '6. Approbation']
    cs = header('acd', '=If(IsBlank(varDossier.ID), "Déclaration d\'accident ou d\'incident", varDossier.TypeFormulaire & " — dossier n° " & varDossier.ID)',
                '"Formulaire : " & Coalesce(acd_rdoTypeFormulaire.Selected.Value, "Accident") & " · " & Coalesce(acd_drpGravite.Selected.Value, "gravité à préciser")',
                boutons_droite=[('btnDeposer', '"☁️ Enregistrer et déposer"', 'Select(%s_btnDeposerBas)' % f.p, 'plein', 'cVert', 250),
                                ('btnSauver', '"☁️ Enregistrer"', sauver, 'contour', 'cBleu', 150), BTN_NOUVEAU],
                etapes=True)
    yo = HB + HT + HS + 8
    w = 'Min(190, (Parent.Width - 48) / 6)'
    for i, t in enumerate(onglets):
        n = i + 1
        cs.append(button('acd_ong%d' % n, s(t), 'UpdateContext({locOnglet: %d})' % n, 'plein',
                         'If(locOnglet = %d, cBleu, Color.White)' % n, Color='If(locOnglet = %d, Color.White, cBleu)' % n,
                         BorderColor='cBleu', BorderThickness=1, HoverFill='If(locOnglet = %d, ColorFade(cBleu, -0.15), cBleuPale)' % n,
                         HoverColor='If(locOnglet = %d, Color.White, cBleu)' % n,
                         X='24 + %d * (%s + 4)' % (i, w), Y=yo, Width=w, Height=36,
                         RadiusBottomLeft=0, RadiusBottomRight=0,
                         Visible='true' if n != 4 else acc))
    yb = yo + HO
    for n in range(1, 7):
        cs.append(body('acd_conOnglet%d' % n, yb, f.tabs[n], visible='locOnglet = %d' % n))
    onv = 'UpdateContext({locOnglet: 1});\nSet(varB1Zone, varDossier.B1Zone);\nSet(varB2Zone, varDossier.B2Zone);\nSet(varVue, "face");\n' + RESET
    return emit_screen('scrAccident', screen_props(onv), cs), f


# ======================================================================= Écran : Enquête
def scr_enquete():
    f = Form('enq')
    f.tab(1)
    f.info(textes.ENQUETE_INTRO, alerte=True)
    f.section('L\'organisation du travail')
    f.checks('FactOrganisation', 'Facteurs constatés', 'FacteurOrganisation', req=True, aide=textes.AXE_ORG)
    f.text('FactOrgAutre', 'Autre (préciser)')
    f.section('L\'environnement et les équipements')
    f.checks('FactEnvironnement', 'Facteurs constatés', 'FacteurEnvironnement', req=True, aide=textes.AXE_ENV)
    f.text('FactEnvAutre', 'Autre (préciser)')
    f.section('Le comportement des personnes concernées')
    f.checks('FactComportement', 'Facteurs constatés', 'FacteurComportement', req=True, aide=textes.AXE_COMP)
    f.text('FactCompAutre', 'Autre (préciser)')
    f.section('Mesures correctives suggérées')
    f.checks('MesuresSuggerees', 'Mesures suggérées', 'MesureCorrective', req=True, aide=textes.AXE_MESURES)
    f.text('MesuresSuggAutre', 'Autre (préciser)')
    f.section('Version de l\'employeur ou tout autre commentaire')
    f.radio('GestAccord', 'Le gestionnaire opérationnel est-il en accord avec la version du travailleur ?', ['Oui', 'Non'], req=True)
    f.text('GestVersion', 'Description détaillée de l\'évènement selon le gestionnaire opérationnel', multi=True, maxlen=255, compteur=True,
           req=True, visible='enq_rdoGestAccord.Selected.Value = "Non"', aide=textes.AIDE_MELITO_GEST)
    f.text('EnqueteurNom', 'Enquête réalisée par', default='Coalesce(varDossier.EnqueteurNom, User().FullName)')
    complet = 'IsBlank(%s)' % f.manquants()
    sauver = ('UpdateContext({locManquants: %s});\nIfError(\n  Set(varDossier, Patch(SST_Dossiers, varDossier, %s));\n'
              '  Notify(If(IsBlank(locManquants), "Enquête enregistrée et complète.", "Enquête enregistrée (incomplète : " & locManquants & ")"), If(IsBlank(locManquants), NotificationType.Success, NotificationType.Warning)),\n'
              '  Notify("Erreur : " & FirstError.Message, NotificationType.Error))') % (
        f.manquants(),
        f.patch_record({'DateEnquete': 'If(IsBlank(locManquants), Coalesce(varDossier.DateEnquete, Today()), varDossier.DateEnquete)',
                        'Statut': 'If(varDossier.Statut = "Fermé", "Fermé", IsBlank(locManquants), If(varDossier.Statut in ["Plan d\'action"], varDossier.Statut, "Analyse en cours"), "Enquête en cours")'}))
    f.raw(nav_row('enq_navBas', extra=[
        button('enq_btnSauverBas', '"☁️ Enregistrer l\'enquête"', sauver, 'plein', 'cVert', Width=230, Height=38),
        button('enq_btnVersAnalyse', '"🌳 Passer à l\'analyse 5 Pourquoi →"', 'Select(enq_btnSauverBas);\nNavigate(scrAnalyse, ScreenTransition.None)', 'plein', 'cBleu', Width=300, Height=38)]))
    cs = header('enq', 'Enquête — la collecte des faits', '"Dossier n° " & varDossier.ID & " · " & varDossier.Title',
                boutons_droite=[('btnSauver', '"☁️ Enregistrer l\'enquête"', 'Select(enq_btnSauverBas)', 'plein', 'cVert', 240),
                                ('btnApercu', '"🖨️ Aperçu PDF"', 'Navigate(scrApercu, ScreenTransition.None)', 'contour', 'cBleu', 160)],
                etapes=True)
    cs.append(body('enq_conCorps', HB + HT + HS + 12, f.tabs[1]))
    return emit_screen('scrEnquete', screen_props(RESET), cs), f


# ======================================================================= Écran : Analyse 5 Pourquoi
def scr_analyse():
    p = 'ana'
    kids = []
    kids.append(button(p + '_btnGuide', 'If(locGuide, "▾ ", "▸ ") & "Qu\'est-ce que la méthode des 5 Pourquoi ? (cliquez pour déplier)"',
                       'UpdateContext({locGuide: !locGuide})', 'lien', 'cBleu', Height=36))
    kids.append(C(uniq(p + '_htmGuide'), 'html', {'HtmlText': s(textes.GUIDE_5P_HTML), 'AutoHeight': True, 'Visible': 'locGuide',
                                                 'Size': 11, 'Color': 'cTexte'}))
    kids.append(label(p + '_secInfo', '"Informations générales"', Size=16, FontWeight='FontWeight.Bold', Color='cMarine', AutoHeight=True, PaddingTop=10))
    kids.append(rect(p + '_lig1', 'cOr', Height=2))
    kids.append(label(p + '_lblProb', '"Problème identifié"', FontWeight='FontWeight.Semibold', AutoHeight=True))
    kids.append(label(p + '_aideProb', s(textes.AIDE_PROBLEME), Size=10.5, Color='cTexte2', AutoHeight=True, Wrap=True))
    st = dict(INPUT_STYLE)
    st.update({'Default': 'varDossier.Probleme', 'Mode': 'TextMode.MultiLine', 'Height': 70, 'Reset': 'locReset',
               'HintText': '"ex. : Pourquoi l\'employé a-t-il glissé dans l\'entrée du garage ?"'})
    kids.append(C(uniq(p + '_txtProbleme'), 'text', st))
    kids.append(label(p + '_lblAnalyste', '"Analyse menée par"', FontWeight='FontWeight.Semibold', AutoHeight=True))
    st2 = dict(INPUT_STYLE)
    st2.update({'Default': 'Coalesce(varDossier.AnalysteNom, User().FullName)', 'Height': 38, 'Reset': 'locReset'})
    kids.append(C(uniq(p + '_txtAnalyste'), 'text', st2))
    kids.append(label(p + '_lblSugg', '"Pistes de mesures correctives suggérées lors de l\'enquête : " & Coalesce(Substitute(varDossier.MesuresSuggerees, "; ", " • "), "aucune") & If(IsBlank(varDossier.MesuresSuggAutre), "", " • " & varDossier.MesuresSuggAutre)',
                      Size=11, Color='cMarine', Fill='cBleuPale', AutoHeight=True, Wrap=True, PaddingLeft=10, PaddingRight=10, PaddingTop=6, PaddingBottom=6))
    nouveau_racine = ('Collect(colNoeuds, {Chemin: Text(Coalesce(Max(Filter(colNoeuds, Niveau = 1), Value(Chemin)), 0) + 1, "000"), Niveau: 1, '
                      'Texte: "", CauseRacine: false, ActionTexte: "", ActionResp: "", ActionEcheance: Blank(), ActionStatut: "À faire"})')
    facteurs = '''Clear(colTmp);
Collect(colTmp, ForAll(Split(varDossier.FactOrganisation, "; "), {T: "[Organisation du travail] " & ThisRecord.Value, V: ThisRecord.Value}));
Collect(colTmp, ForAll(Split(varDossier.FactEnvironnement, "; "), {T: "[Environnement et équipements] " & ThisRecord.Value, V: ThisRecord.Value}));
Collect(colTmp, ForAll(Split(varDossier.FactComportement, "; "), {T: "[Comportement des personnes concernées] " & ThisRecord.Value, V: ThisRecord.Value}));
Collect(colTmp,
  {T: "[Organisation du travail] " & varDossier.FactOrgAutre, V: varDossier.FactOrgAutre},
  {T: "[Environnement et équipements] " & varDossier.FactEnvAutre, V: varDossier.FactEnvAutre},
  {T: "[Comportement des personnes concernées] " & varDossier.FactCompAutre, V: varDossier.FactCompAutre});
UpdateContext({
  locAjout: Filter(colTmp, !IsBlank(V) && !("pas en cause" in V) && !(T in colNoeuds.Texte)),
  locBase: Coalesce(Max(Filter(colNoeuds, Niveau = 1), Value(Chemin)), 0)});
ForAll(Sequence(CountRows(locAjout)),
  Collect(colNoeuds, {Chemin: Text(locBase + Value, "000"), Niveau: 1, Texte: Index(locAjout, Value).T,
    CauseRacine: false, ActionTexte: "", ActionResp: "", ActionEcheance: Blank(), ActionStatut: "À faire"}));
Notify(If(CountRows(locAjout) = 0, "Aucun nouveau facteur à ajouter (cochez des facteurs dans l'enquête, ou ils sont déjà dans l'arbre).", CountRows(locAjout) & " branche(s) « Pourquoi 1 » créée(s)."), NotificationType.Information)'''
    nb_rac = 'CountRows(Filter(colNoeuds, CauseRacine))'
    sauver = '''IfError(
  Set(varDossier, Patch(SST_Dossiers, varDossier, {
    Probleme: ana_txtProbleme.Text,
    AnalysteNom: ana_txtAnalyste.Text,
    DateAnalyse: If(%(n)s > 0, Coalesce(varDossier.DateAnalyse, Today()), varDossier.DateAnalyse),
    DatePlanAction: If(%(n)s > 0 && CountRows(Filter(colNoeuds, CauseRacine && (IsBlank(ActionTexte) || IsBlank(ActionResp) || IsBlank(ActionEcheance)))) = 0,
      Coalesce(varDossier.DatePlanAction, Today()), varDossier.DatePlanAction),
    Statut: If(varDossier.Statut = "Fermé", "Fermé", %(n)s > 0, "Plan d'action", "Analyse en cours")}));
  RemoveIf(SST_Pourquoi, DossierID = varDossier.ID);
  ForAll(colNoeuds, Patch(SST_Pourquoi, Defaults(SST_Pourquoi), {
    Title: Left(ThisRecord.Texte, 250), DossierID: varDossier.ID, Chemin: ThisRecord.Chemin, Niveau: ThisRecord.Niveau,
    Texte: ThisRecord.Texte, CauseRacine: ThisRecord.CauseRacine, ActionTexte: ThisRecord.ActionTexte,
    ActionResp: ThisRecord.ActionResp, ActionEcheance: ThisRecord.ActionEcheance, ActionStatut: ThisRecord.ActionStatut}));
  Notify("Analyse enregistrée.", NotificationType.Success),
  Notify("Erreur : " & FirstError.Message, NotificationType.Error))''' % {'n': nb_rac}
    kids.append(cont(p + '_barreOutils', 'AutoLayout', [
        button(p + '_btnAjouter', '"+ Ajouter un Pourquoi"', nouveau_racine, 'plein', 'cBleu', Width=200, Height=38),
        button(p + '_btnFacteurs', '"Créer les branches à partir des facteurs de l\'enquête"', facteurs, 'contour', 'cBleu', Width=400, Height=38),
    ], LayoutDirection='LayoutDirection.Horizontal', LayoutGap=12, Height=54, PaddingTop=8, FillPortions=0))
    kids.append(C(uniq(p + '_htmLegende'), 'html', {'HtmlText': s(textes.LEGENDE_5P_HTML), 'Height': 30}))
    kids.append(label(p + '_secArbre', '"Arbre des causes"', Size=16, FontWeight='FontWeight.Bold', Color='cMarine', AutoHeight=True, PaddingTop=10))
    kids.append(rect(p + '_lig2', 'cOr', Height=2))
    kids.append(label(p + '_videArbre', s(textes.ARBRE_VIDE), Color='cTexte2', Italic=True, AutoHeight=True, Wrap=True,
                      Visible='CountRows(colNoeuds) = 0'))
    coul = 'Switch(Min(ThisItem.Niveau, 5), 1, cMarine, 2, cBleu, 3, cSarcelle, 4, cViolet, cOr)'
    xo = '(ThisItem.Niveau - 1) * 28'
    ajout_enfant = ('With({m: Coalesce(Max(Filter(colNoeuds, StartsWith(Chemin, ThisItem.Chemin & ".") && Niveau = ThisItem.Niveau + 1), Value(Right(Chemin, 3))), 0)}, '
                    'Collect(colNoeuds, {Chemin: ThisItem.Chemin & "." & Text(m + 1, "000"), Niveau: ThisItem.Niveau + 1, Texte: "", CauseRacine: false, '
                    'ActionTexte: "", ActionResp: "", ActionEcheance: Blank(), ActionStatut: "À faire"}))')
    erreur = 'CountIf(Filter(colListes, Liste = "MotErreurHumaine"), Value in Lower(ThisItem.Texte)) > 0'
    tin = dict(INPUT_STYLE)
    tin.update({'Default': 'ThisItem.Texte', 'OnChange': 'Patch(colNoeuds, ThisItem, {Texte: Self.Text})',
                'HintText': '"Réponse factuelle..."', 'X': '%s + 12' % xo, 'Y': 30, 'Width': 'Parent.TemplateWidth - %s - 30' % xo,
                'Height': 36, 'Size': 11})
    tpl = [
        rect(p + '_nCarte', 'Color.White', X=xo, Y=0, Width='Parent.TemplateWidth - %s - 6' % xo, Height='Parent.TemplateHeight - 8',
             BorderColor=coul, BorderThickness=2),
        label(p + '_nTag', '"POURQUOI " & ThisItem.Niveau & " ?"', X='%s + 12' % xo, Y=4, Width=120, Height=24, Size=10,
              FontWeight='FontWeight.Bold', Color=coul),
        pill(p + '_nRacine', '"CAUSE RACINE"', 'cRouge', X='%s + 136' % xo, Y=4, Width=120, Height=22, Size=9, Visible='ThisItem.CauseRacine'),
        pill(p + '_nPiege', '"⚠ Piège « erreur humaine » ?"', 'cBleuPale', 'cMarine', X='%s + 262' % xo, Y=4, Width=230, Height=22, Size=9,
             Visible=erreur, Tooltip=s(textes.PIEGE_TOOLTIP), DisplayMode='DisplayMode.Edit', OnSelect='Notify(%s, NotificationType.Warning)' % s(textes.PIEGE_TOOLTIP)),
        C(uniq(p + '_nTexte'), 'text', tin),
        button(p + '_nAjout', '"+ Pourquoi (nouvelle cause)"', ajout_enfant, 'contour', 'cBleu', X='%s + 12' % xo, Y=72, Width=210, Height=28, Size=10),
        button(p + '_nCause', 'If(ThisItem.CauseRacine, "✓ Cause racine", "Marquer cause racine")', 'Patch(colNoeuds, ThisItem, {CauseRacine: !ThisItem.CauseRacine})',
               'plein', 'If(ThisItem.CauseRacine, cRouge, Color.White)', Color='If(ThisItem.CauseRacine, Color.White, cRouge)', BorderColor='cRouge',
               BorderThickness=2, HoverFill='If(ThisItem.CauseRacine, ColorFade(cRouge, -0.15), cBleuPale)', HoverColor='If(ThisItem.CauseRacine, Color.White, cRouge)',
               X='%s + 230' % xo, Y=72, Width=180, Height=28, Size=10),
        button(p + '_nSupp', '"Supprimer"', 'RemoveIf(colNoeuds, Chemin = ThisItem.Chemin || StartsWith(Chemin, ThisItem.Chemin & "."))',
               'lien', 'cRouge', X='%s + 418' % xo, Y=72, Width=110, Height=28, Size=10, Align='Align.Center'),
    ]
    kids.append(C(uniq(p + '_galArbre'), 'gal', {'Items': 'Sort(colNoeuds, Chemin)', 'TemplateSize': 116, 'TemplatePadding': 0,
                                                'Height': 'CountRows(colNoeuds) * 116 + 4', 'ShowScrollbar': False, 'BorderThickness': 0,
                                                'Visible': 'CountRows(colNoeuds) > 0'}, tpl, 'Vertical'))
    # Synthèse
    kids.append(label(p + '_secSynth', '"Causes racines et suivi des actions (plan d\'action)"', Size=16, FontWeight='FontWeight.Bold', Color='cMarine', AutoHeight=True, PaddingTop=10))
    kids.append(rect(p + '_lig3', 'cOr', Height=2))
    kids.append(label(p + '_videSynth', s(textes.SYNTH_VIDE), Color='cTexte2', Italic=True, AutoHeight=True, Wrap=True, Visible='%s = 0' % nb_rac))
    chemin = 'Concat(Sort(Filter(colNoeuds, StartsWith(ThisItem.Chemin, Chemin)), Niveau), Coalesce(Texte, "(réponse vide)"), " → ")'
    st_a = dict(INPUT_STYLE); st_a.update({'Default': 'ThisItem.ActionTexte', 'OnChange': 'Patch(colNoeuds, ThisItem, {ActionTexte: Self.Text})',
                                           'HintText': '"Action corrective à mettre en place..."', 'X': 12, 'Y': 86, 'Width': '(Parent.TemplateWidth - 60) * 0.45', 'Height': 38, 'Size': 11})
    st_r = dict(INPUT_STYLE); st_r.update({'Default': 'ThisItem.ActionResp', 'OnChange': 'Patch(colNoeuds, ThisItem, {ActionResp: Self.Text})',
                                           'HintText': '"Responsable"', 'X': '12 + (Parent.TemplateWidth - 60) * 0.45 + 8', 'Y': 86, 'Width': '(Parent.TemplateWidth - 60) * 0.2', 'Height': 38, 'Size': 11})
    tpl2 = [
        rect(p + '_sCarte', 'cBleuPale', X=0, Y=0, Width='Parent.TemplateWidth', Height='Parent.TemplateHeight - 8'),
        label(p + '_sCause', '"Cause racine : " & ThisItem.Texte', X=12, Y=4, Width='Parent.TemplateWidth - 24', Height=26, Size=12,
              FontWeight='FontWeight.Semibold', Color='cMarine'),
        label(p + '_sChemin', '"Chemin : " & %s' % chemin, X=12, Y=30, Width='Parent.TemplateWidth - 24', Height=36, Size=10, Color='cTexte2', Wrap=True),
        label(p + '_sEnt', '"Action corrective · Responsable · Échéance · Statut"', X=12, Y=64, Width=500, Height=20, Size=10, Color='cTexte2'),
        C(uniq(p + '_sAction'), 'text', st_a),
        C(uniq(p + '_sResp'), 'text', st_r),
        C(uniq(p + '_sEch'), 'date', {'DefaultDate': 'ThisItem.ActionEcheance', 'OnChange': 'Patch(colNoeuds, ThisItem, {ActionEcheance: Self.SelectedDate})',
                                     'Format': '"yyyy-mm-dd"', 'X': '12 + (Parent.TemplateWidth - 60) * 0.65 + 16', 'Y': 86,
                                     'Width': '(Parent.TemplateWidth - 60) * 0.17', 'Height': 38, 'BorderColor': 'cBordure'}),
        C(uniq(p + '_sStatut'), 'drop', {'Items': 'Sort(Filter(colListes, Liste = "StatutAction"), Ordre).Value', 'Default': 'ThisItem.ActionStatut',
                                        'OnChange': 'Patch(colNoeuds, ThisItem, {ActionStatut: Self.Selected.Value})',
                                        'X': '12 + (Parent.TemplateWidth - 60) * 0.82 + 24', 'Y': 86, 'Width': '(Parent.TemplateWidth - 60) * 0.18',
                                        'Height': 38, 'BorderColor': 'cBordure', 'ChevronBackground': 'cBleu', 'SelectionFill': 'cBleu', 'Size': 11}),
    ]
    kids.append(C(uniq(p + '_galSynth'), 'gal', {'Items': 'Filter(Sort(colNoeuds, Chemin), CauseRacine)', 'TemplateSize': 140, 'TemplatePadding': 0,
                                                'Height': '%s * 140 + 4' % nb_rac, 'ShowScrollbar': False, 'BorderThickness': 0,
                                                'Visible': '%s > 0' % nb_rac}, tpl2, 'Vertical'))
    kids.append(label(p + '_secDonc', '"Vérification logique (test du « Donc »)"', Size=13, FontWeight='FontWeight.Bold', Color='cTexte2', AutoHeight=True,
                      PaddingTop=8, Visible='%s > 0' % nb_rac))
    donc = ('Concat(Sort(Filter(colNoeuds, StartsWith(ThisItem.Chemin, Chemin)), Niveau, SortOrder.Descending), Coalesce(Texte, "(vide)"), ", donc ") & ", donc " & Coalesce(ana_txtProbleme.Text, "(problème non défini)")')
    tpl3 = [
        rect(p + '_dBarre', 'cBleu', X=0, Y=0, Width=4, Height='Parent.TemplateHeight - 8'),
        label(p + '_dTexte', donc, X=12, Y=0, Width='Parent.TemplateWidth - 16', Height='Parent.TemplateHeight - 8', Size=11, Wrap=True,
              Fill='cFond', VerticalAlign='VerticalAlign.Middle'),
    ]
    kids.append(C(uniq(p + '_galDonc'), 'gal', {'Items': 'Filter(Sort(colNoeuds, Chemin), CauseRacine)', 'TemplateSize': 70, 'TemplatePadding': 0,
                                               'Height': '%s * 70 + 4' % nb_rac, 'ShowScrollbar': False, 'BorderThickness': 0,
                                               'Visible': '%s > 0' % nb_rac}, tpl3, 'Vertical'))
    kids.append(nav_row(p + '_navBas', extra=[button(p + '_btnSauverBas', '"☁️ Enregistrer l\'analyse"', sauver, 'plein', 'cVert', Width=230, Height=38)]))
    cs = header(p, 'Analyse des causes — 5 Pourquoi', '"Dossier n° " & varDossier.ID & " · " & varDossier.Title',
                boutons_droite=[('btnSauver', '"☁️ Enregistrer l\'analyse"', 'Select(ana_btnSauverBas)', 'plein', 'cVert', 240),
                                ('btnApercu', '"🖨️ Aperçu PDF"', 'Navigate(scrApercu, ScreenTransition.None)', 'contour', 'cBleu', 160),
                                ('btnEnquete', '"🔍 Enquête"', 'Navigate(scrEnquete, ScreenTransition.None)', 'contour', 'cBleu', 130)],
                etapes=True)
    cs.append(body(p + '_conCorps', HB + HT + HS + 12, kids))
    onv = ('ClearCollect(colNoeuds, ForAll(Filter(SST_Pourquoi, DossierID = varDossier.ID), {Chemin: Chemin, Niveau: Niveau, Texte: Texte, '
           'CauseRacine: CauseRacine, ActionTexte: ActionTexte, ActionResp: ActionResp, ActionEcheance: ActionEcheance, ActionStatut: ActionStatut}));\n'
           'UpdateContext({locGuide: false});\n' + RESET)
    return emit_screen('scrAnalyse', screen_props(onv), cs)


# ======================================================================= Écran : Situation dangereuse
def scr_situation():
    f = Form('sit')
    f.tab(1)
    f.info(textes.SITUATION_INTRO, alerte=True)
    f.section('Vos coordonnées')
    f.text('EmpNom', 'Votre nom', req=True)
    f.text('EmpPrenom', 'Votre prénom', req=True)
    f.text('EmpID', 'Votre ID', req=True, width=200, maxlen=6, aide='Les 6 chiffres de votre ID (incluant le ou les 0).')
    f.drop('EmpService', 'Votre unité administrative', 'Sort(Filter(colListes, Liste = "Service"), Ordre).Value', req=True)
    f.text('EmpCourriel', 'Votre courriel', req=True, default='Coalesce(varDossier.EmpCourriel, User().Email)', aide='Inscrire un seul courriel (personnel ou Ville).')
    f.valid.append(('Courriel (format invalide)', 'true', '!IsMatch(sit_txtEmpCourriel.Text, Match.Email)'))
    f.section('Situation dangereuse observée')
    f.radio('DiscuteGest', 'En avez-vous discuté avec votre gestionnaire ?', ['Oui', 'Non'], req=True)
    f.radio('SyndicatCopie', 'Désirez-vous que votre syndicat / association soit mis en copie de votre signalement ?', ['Oui', 'Non'], req=True)
    f.drop('EmpSyndicat', 'Syndicat / association auquel vous êtes rattaché et qui sera mis en copie', 'Sort(Filter(colListes, Liste = "Syndicat"), Ordre).Value',
           req=True, visible='sit_rdoSyndicatCopie.Selected.Value = "Oui"')
    f.text('EvtAdresse', 'Indiquez l\'adresse et le lieu précis où vous avez observé la situation dangereuse', req=True)
    f.date('EvtDate', 'Date de l\'observation', req=True)
    f.text('Description', 'Décrire brièvement la situation dangereuse que vous avez observée', multi=True, req=True, height=110)
    f.text('MesurePrev', 'Décrire les mesures de prévention immédiates ou correctives que vous suggérez', multi=True, req=True, height=110)
    f.info('En cas de besoin, conservez une ou vos photos dans vos dossiers personnels pour la suite des choses.')
    titre = '"Situation dangereuse – " & sit_txtEmpNom.Text & ", " & sit_txtEmpPrenom.Text & " – " & Text(sit_dteEvtDate.SelectedDate, "yyyy-mm-dd")'
    sauver = save_formula(f, '"Situation dangereuse"', titre, False)
    deposer = save_formula(f, '"Situation dangereuse"', titre, True)
    f.raw(nav_row('sit_navBas', extra=[button('sit_btnDeposerBas', '"☁️ Enregistrer et déposer"', deposer, 'plein', 'cVert', Width=240, Height=38)]))
    cs = header('sit', 'Signalement d\'une situation dangereuse', '"Formulaire : situation dangereuse"',
                boutons_droite=[('btnDeposer', '"☁️ Enregistrer et déposer"', 'Select(%s_btnDeposerBas)' % f.p, 'plein', 'cVert', 250),
                                ('btnSauver', '"☁️ Enregistrer"', sauver, 'contour', 'cBleu', 150), BTN_NOUVEAU], etapes=True)
    cs.append(body('sit_conCorps', HB + HT + HS + 12, f.tabs[1]))
    return emit_screen('scrSituation', screen_props(RESET), cs), f


# ======================================================================= Écran : Violence
def scr_violence():
    f = Form('vio')
    f.tab(1)
    f.info(textes.VIOLENCE_INTRO, alerte=True)
    f.section('Informations générales')
    f.radio('DeclarantRole', 'Identification de la personne qui déclare la situation', ['La victime', 'Le témoin de la situation'], req=True)
    f.text('EmpNom', 'Nom de l\'employé qui déclare la situation', req=True)
    f.text('EmpPrenom', 'Prénom de l\'employé qui déclare la situation', req=True)
    f.text('EmpID', 'Numéro d\'employé (ID)', req=True, width=200, maxlen=6,
           aide='Inscrire seulement les 6 chiffres (si plus d\'un employé, inscrire seulement un ID ici).')
    f.valid.append(('ID (6 chiffres)', 'true', '!IsMatch(vio_txtEmpID.Text, "\\d{6}")'))
    f.drop('EmpSyndicat', 'Syndicat auquel l\'employé est rattaché', 'Sort(Filter(colListes, Liste = "Syndicat"), Ordre).Value', req=True)
    f.text('EmpSuperieur', 'Prénom et nom du supérieur immédiat', req=True)
    champs_org(f)
    f.date('EvtDate', 'Date de l\'évènement', req=True)
    f.text('EvtHeure', 'Heure exacte ou approximative de l\'évènement', req=True, width=200, hint='ex. : 18:45')
    f.text('EvtAdresse', 'Lieu de l\'évènement', req=True, maxlen=255, aide='S\'il n\'y a pas d\'adresse, indiquez le numéro civique le plus près.')
    f.text('Tache', 'Précisez les tâches au moment de l\'évènement', req=True, multi=True, maxlen=255, compteur=True, height=70)
    f.section('Circonstances et type d\'évènement')
    f.checks('ViolTypes', 'Type d\'évènement', 'TypeViolence', req=True, aide='Plusieurs choix possibles.', wrap=2)
    f.text('Description', 'Description de l\'évènement, selon la version de l\'employé', multi=True, req=True, maxlen=255, compteur=True,
           aide='Inscrivez le maximum de détails (ex. : les paroles dites, les gestes posés, les causes probables...).', height=110)
    f.section('Informations sur le ou les auteurs de l\'acte')
    f.text('AuteurNom', 'Nom et prénom de l\'individu (si connu)')
    f.text('AuteurAdresse', 'Adresse de l\'individu (si connue)')
    f.text('AuteurInfo', 'Informations supplémentaires', multi=True, height=70)
    f.radio('Recidive', 'Récidive (employé ayant déjà été victime d\'un évènement similaire)', ['Oui', 'Non'], req=True)
    f.text('RecidiveDetails', 'Détails supplémentaires sur la récidive', multi=True, height=70, visible='vio_rdoRecidive.Selected.Value = "Oui"')
    f.section('Témoins')
    f.radio('Temoins', 'Est-ce qu\'il y a des témoins ?', ['Oui', 'Aucun'], req=True)
    tem = 'vio_rdoTemoins.Selected.Value = "Oui"'
    f.text('TemoinsNoms', 'Nom du/des témoin(s)', multi=True, height=60, visible=tem)
    f.text('TemoinsCoord', 'Coordonnées du/des témoin(s)', multi=True, height=60, visible=tem)
    f.section('Mesures correctives immédiates')
    f.checks('ViolMesuresPrises', 'Mesures prises (plusieurs choix possibles)', 'MesuresPrisesViolence')
    f.text('MesurePrev', 'Mesures correctives immédiates', multi=True, req=True, aide='Décrivez les mesures correctives immédiates mises en œuvre après l\'évènement.')
    f.text('ViolMesuresPar', 'Mesures correctives mises en œuvre par', req=True)
    f.section('Comité bouclier')
    f.info(textes.BOUCLIER)
    f.radio('ComiteBouclier', 'En plus de déclarer cet évènement à la Division SST, j\'aimerais, en tant que gestionnaire, solliciter l\'aide du Comité bouclier', ['Oui', 'Non'], req=True)
    f.section('Confirmation de la déclaration')
    f.text('GestNom', 'Nom du gestionnaire qui complète le formulaire', req=True, default='Coalesce(varDossier.GestNom, User().FullName)')
    f.radio('ApprobationEmp', 'Employé impliqué : « J\'étais présent(e) lorsque mon gestionnaire a complété ce formulaire. Il s\'agit de ma version des faits et je confirme que la description de l\'évènement est exacte. »',
            ['Oui', 'Non, pour des raisons exceptionnelles, l\'employé n\'est pas en mesure d\'approuver la déclaration'], vertical=True, req=True,
            aide='Approbation de l\'employé (fait office de signature).')
    f.radio('FormatCopie', 'L\'employé désire recevoir sa copie de la déclaration dans le format suivant', ['Copie courriel', 'Copie papier', 'Copie courriel et papier'], vertical=True, req=True)
    f.text('EmpCourriel', 'Courriel de l\'employé', req=True, aide='Inscrire un seul courriel (personnel ou Ville).')
    f.valid.append(('Courriel de l\'employé (format invalide)', 'true', '!IsMatch(vio_txtEmpCourriel.Text, Match.Email)'))
    titre = '"Violence – " & vio_txtEmpNom.Text & ", " & vio_txtEmpPrenom.Text & " – " & Text(vio_dteEvtDate.SelectedDate, "yyyy-mm-dd")'
    extra = {
        'DateMesures': 'If(IsBlank(vio_txmMesurePrev.Text), varDossier.DateMesures, Coalesce(varDossier.DateMesures, Today()))',
        'DateApprobation': 'If(vio_rdoApprobationEmp.Selected.Value = "Oui", Coalesce(varDossier.DateApprobation, Today()), varDossier.DateApprobation)',
    }
    sauver = save_formula(f, '"Violence"', titre, False, extra)
    deposer = save_formula(f, '"Violence"', titre, True, extra)
    f.raw(nav_row('vio_navBas', extra=[button('vio_btnDeposerBas', '"☁️ Enregistrer et déposer"', deposer, 'plein', 'cVert', Width=240, Height=38)]))
    cs = header('vio', 'Évènement traumatisant et acte de violence', '"Formulaire : déclaration à l\'égard d\'un employé (citoyen ou partenaire externe)"',
                boutons_droite=[('btnDeposer', '"☁️ Enregistrer et déposer"', 'Select(%s_btnDeposerBas)' % f.p, 'plein', 'cVert', 250),
                                ('btnSauver', '"☁️ Enregistrer"', sauver, 'contour', 'cBleu', 150), BTN_NOUVEAU], etapes=True)
    cs.append(body('vio_conCorps', HB + HT + HS + 12, f.tabs[1]))
    return emit_screen('scrViolence', screen_props(RESET), cs), f


# ======================================================================= Écran : Aperçu / dossier / PDF
def scr_apercu(f_acc, f_enq, f_sit, f_vio):
    p = 'apc'
    css = textes.CSS_PDF
    entete = ('"<html><head><meta charset=\'utf-8\'><style>' + css.replace('"', '""') + '</style></head><body>" & '
              '"<div style=\'%s\'><div style=\'height:8px;background:#857650;margin-bottom:10px\'></div><h1 style=\'%s\'>" &' % (textes.ST_BODY, textes.ST_H1) + ' Switch(varDossier.TypeFormulaire, "Situation dangereuse", "Signalement d\'une situation dangereuse", '
              '"Violence", "Déclaration d\'un évènement traumatisant et d\'acte de violence", "Déclaration d\'" & Lower(varDossier.TypeFormulaire) & " de travail") & "</h1>" & '
              '"<p style=\'color:#6B7280;font-size:9pt;margin:0 0 12px\'>Dossier n° " & varDossier.ID & " · Statut : " & varDossier.Statut & " · Déposé le " & Coalesce(Text(varDossier.DateDeclaration, "yyyy-mm-dd"), "—") & '
              '" · Document généré le " & Text(Now(), "yyyy-mm-dd hh:mm") & "</p>"')
    pied = '"<p style=\'margin-top:24px;color:#6B7280;font-size:8pt;border-top:1px solid #857650;padding-top:6px\'>Formulaire propriété de la Division de la santé et de la sécurité au travail — Ville de Québec</p></div></body></html>"'
    pq = textes.HTML_5P
    html_acc = '%s &\n%s &\n If(IsBlank(varDossier.DateEnquete) && IsBlank(varDossier.FactOrganisation), "", %s) &\n%s &\n%s' % (
        entete, f_acc.html_expr(), f_enq.html_expr(), pq, pied)
    html = 'Switch(varDossier.TypeFormulaire,\n "Situation dangereuse", %s &\n%s &\n%s,\n "Violence", %s &\n%s &\n%s,\n %s)' % (
        entete, f_sit.html_expr(), pied, entete, f_vio.html_expr(), pied, html_acc)
    dest = ('Concat(Filter(Table({v: cCourrielSST}, '
            '{v: If("courriel" in Lower(varDossier.FormatCopie) || varDossier.TypeFormulaire = "Situation dangereuse", varDossier.EmpCourriel)}, '
            '{v: If(varDossier.SyndicatCopie = "Oui", LookUp(colListes, Liste = "Syndicat" && Value = varDossier.EmpSyndicat, Courriel))}, '
            '{v: If(varDossier.ComiteBouclier = "Oui", cCourrielBouclier)}), !IsBlank(v)), v, ";")')
    envoyer = '''With({dest: %s},
  IfError(
    Set(varLienPdf, SSTGenererPDF.Run(
      "SST-" & Text(varDossier.ID, "00000") & "_" & Substitute(varDossier.TypeFormulaire, " ", "-") & "_" & Text(Now(), "yyyymmdd-hhmm"),
      apc_htmApercu.HtmlText,
      dest,
      "SST – " & varDossier.TypeFormulaire & " – dossier n° " & varDossier.ID,
      "Bonjour,<br><br>Vous trouverez ci-joint la copie PDF du dossier SST n° " & varDossier.ID & " (" & varDossier.TypeFormulaire & ").<br><br>Ceci est un message automatique de l'application SST."
    ).lienpdf);
    Set(varDossier, Patch(SST_Dossiers, varDossier, {PdfLien: varLienPdf}));
    Notify("PDF généré" & If(IsBlank(dest), ".", " et envoyé à : " & dest), NotificationType.Success),
    Notify("Le PDF n'a pas pu être généré (vérifiez le flux SSTGenererPDF) : " & FirstError.Message, NotificationType.Error)))''' % dest
    est_ai = 'varDossier.TypeFormulaire in ["Accident", "Incident"]'
    sst = 'varRole = "Conseiller SST"'
    modifier = 'Navigate(Switch(varDossier.TypeFormulaire, "Situation dangereuse", scrSituation, "Violence", scrViolence, scrAccident), ScreenTransition.None)'
    yb = HB + HT + HS + 12
    stn = dict(INPUT_STYLE)
    stn.update({'Default': 'varDossier.NotesSST', 'Mode': 'TextMode.MultiLine', 'X': 16, 'Y': 0, 'Width': 'Parent.Width - 32', 'Height': 110,
                'Reset': 'locReset', 'HintText': '"Notes de suivi du conseiller SST..."', 'Size': 11})
    panneau = [
        label(p + '_titActions', '"Actions"', X=16, Y=12, Width=280, Height=28, Size=14, FontWeight='FontWeight.Bold', Color='cMarine'),
        button(p + '_btnModifier', '"✏️ Modifier le formulaire"', modifier, 'contour', 'cBleu', X=16, Y=48, Width='Parent.Width - 32', Height=38),
        button(p + '_btnEnquete', '"🔍 Enquête (collecte des faits)"', 'Navigate(scrEnquete, ScreenTransition.None)', 'contour', 'cBleu',
               X=16, Y=94, Width='Parent.Width - 32', Height=38, Visible=est_ai),
        button(p + '_btnAnalyse', '"🌳 Analyse 5 Pourquoi"', 'Navigate(scrAnalyse, ScreenTransition.None)', 'contour', 'cBleu',
               X=16, Y=140, Width='Parent.Width - 32', Height=38, Visible=est_ai),
        button(p + '_btnEnvoyer', '"📄 Générer le PDF et envoyer"', envoyer, 'plein', 'cVert', X=16, Y=192, Width='Parent.Width - 32', Height=40,
               DisplayMode='If(IsBlank(varDossier.ID), DisplayMode.Disabled, DisplayMode.Edit)'),
        button(p + '_btnOuvrir', '"📄 Ouvrir le PDF"', 'Launch(varDossier.PdfLien)', 'contour', 'cBleu', X=16, Y=240, Width='Parent.Width - 32', Height=38,
               Visible='!IsBlank(varDossier.PdfLien)'),
        label(p + '_noteEnvoi', '"Destinataires : " & Coalesce(%s, "aucun (configurer CourrielSST dans SST_Ref_Listes)")' % dest, X=16, Y=284,
              Width='Parent.Width - 32', Height=60, Size=9.5, Color='cTexte2', Wrap=True, VerticalAlign='VerticalAlign.Top'),
        cont(p + '_conSST', 'ManualLayout', [
            rect(p + '_ligSST', 'cOr', X=16, Y=0, Width='Parent.Width - 32', Height=2),
            label(p + '_titSST', '"Suivi du conseiller SST"', X=16, Y=8, Width=280, Height=28, Size=14, FontWeight='FontWeight.Bold', Color='cMarine'),
            label(p + '_lblStat', '"Statut"', X=16, Y=40, Width=200, Height=20, Size=10, Color='cTexte2'),
            C(uniq(p + '_drpStatut'), 'drop', {'Items': 'Sort(Filter(colListes, Liste = "Statut"), Ordre).Value', 'Default': 'varDossier.Statut', 'Reset': 'locReset',
                                              'X': 16, 'Y': 60, 'Width': 'Parent.Width - 32', 'Height': 36, 'BorderColor': 'cBordure',
                                              'ChevronBackground': 'cBleu', 'SelectionFill': 'cBleu', 'Size': 11}),
            label(p + '_lblNotes', '"Notes de suivi"', X=16, Y=102, Width=200, Height=20, Size=10, Color='cTexte2'),
            C(uniq(p + '_txtNotes'), 'text', dict(stn, Y=122)),
            button(p + '_btnSuivi', '"☁️ Enregistrer le suivi"', 'Set(varDossier, Patch(SST_Dossiers, varDossier, {Statut: apc_drpStatut.Selected.Value, NotesSST: apc_txtNotes.Text, '
                   'DateEnquete: If(varDossier.TypeFormulaire in ["Situation dangereuse", "Violence"] && apc_drpStatut.Selected.Value <> "Déposé", Coalesce(varDossier.DateEnquete, Today()), varDossier.DateEnquete), '
                   'DatePlanAction: If(varDossier.TypeFormulaire = "Situation dangereuse" && apc_drpStatut.Selected.Value in ["Plan d\'action", "Fermé"], Coalesce(varDossier.DatePlanAction, Today()), varDossier.DatePlanAction), '
                   'DateFermeture: If(apc_drpStatut.Selected.Value = "Fermé", Coalesce(varDossier.DateFermeture, Today()), Blank())})); '
                   'Notify("Suivi enregistré.", NotificationType.Success)',
                   'plein', 'cVert', X=16, Y=240, Width='Parent.Width - 32', Height=38),
        ], X=0, Y=350, Width='Parent.Width', Height=300, Visible=sst),
    ]
    cs = header(p, '=Coalesce(varDossier.Title, "Dossier")', '"Aperçu du dossier et du PDF"',
                boutons_droite=[BTN_NOUVEAU], etapes=True)
    cs.append(body(p + '_conApercu', yb, [C(uniq(p + '_htmApercu'), 'html', {'HtmlText': html, 'AutoHeight': True})],
                   width='Parent.Width - 400'))
    cs.append(cont(p + '_conActions', 'ManualLayout', panneau, X='Parent.Width - 360', Y=yb, Width=336, Height='Parent.Height - %d' % (yb + 16),
                   **card_props()))
    onv = ('ClearCollect(colNoeudsPdf, Filter(SST_Pourquoi, DossierID = varDossier.ID));\n' + RESET + ';\n'
           'If(varAutoEnvoi, Set(varAutoEnvoi, false); Select(apc_btnEnvoyer))')
    return emit_screen('scrApercu', screen_props(onv), cs)


# ======================================================================= Écran : Aide / À propos
def scr_aide():
    p = 'aid'
    onglets = ['Accident / incident', 'Enquête et 5 Pourquoi', 'Situation dangereuse', 'Violence', 'À propos']
    cs = header(p, 'Comment remplir', '"Aide et informations"', boutons_droite=[BTN_NOUVEAU])
    yo = HB + HT + 12
    for i, t in enumerate(onglets):
        n = i + 1
        cs.append(button(p + '_ong%d' % n, s(t), 'UpdateContext({locAideOnglet: %d})' % n, 'plein',
                         'If(locAideOnglet = %d, cBleu, Color.White)' % n, Color='If(locAideOnglet = %d, Color.White, cBleu)' % n,
                         BorderColor='cBleu', BorderThickness=1, HoverFill='If(locAideOnglet = %d, ColorFade(cBleu, -0.15), cBleuPale)' % n,
                         HoverColor='If(locAideOnglet = %d, Color.White, cBleu)' % n,
                         X='24 + %d * 214' % i, Y=yo, Width=210, Height=36, RadiusBottomLeft=0, RadiusBottomRight=0))
    html = 'Switch(locAideOnglet, %s)' % ', '.join('%d, %s' % (i + 1, s(h)) for i, h in enumerate(textes.AIDE_HTML))
    cs.append(body(p + '_conCorps', yo + HO, [C(uniq(p + '_htmAide'), 'html', {'HtmlText': html, 'AutoHeight': True})]))
    return emit_screen('scrAide', screen_props('If(IsBlank(locAideOnglet) || locAideOnglet = 0, UpdateContext({locAideOnglet: 1}))'), cs)


# ======================================================================= Objet App (formules FR à coller)
def app_formulas():
    from zones import tzones_expr
    lines = ['// Couleurs de la palette (Appréciation de la contribution)']
    for n, hx, (r, g, b) in PALETTE:
        lines.append('%s = RGBA(%d, %d, %d, 1); // %s' % (n, r, g, b, hx))
    lines += [
        'cVersion = "2026-11";',
        '// Courriels configurables dans la liste SST_Ref_Listes (Liste = Config, colonne Courriel)',
        'cCourrielSST = LookUp(SST_Ref_Listes, Title = "Config" && Valeur = "CourrielSST", Courriel);',
        'cCourrielBouclier = LookUp(SST_Ref_Listes, Title = "Config" && Valeur = "CourrielComiteBouclier", Courriel);',
        '// Zones du schéma corporel',
        'tZones = ' + tzones_expr() + ';',
    ]
    return '\n'.join(lines) + '\n'


def app_onstart():
    return '''Set(varMoi, Lower(User().Email));
Concurrent(
  ClearCollect(colListes, ForAll(SST_Ref_Listes, {Liste: Title, Value: Valeur, Ordre: Ordre, Aide: Aide, Courriel: Courriel})),
  ClearCollect(colOrg, ForAll(SST_Ref_Org, {Service: Title, Niveau: Niveau, Value: Valeur, Ordre: Ordre})),
  ClearCollect(colTitres, ForAll(SST_Ref_Titres, {Syndicat: Title, Classe: Classe, Value: Valeur, Ordre: Ordre})),
  ClearCollect(colRoles, ForAll(SST_Roles, {Courriel: Lower(Title), Role: Role}))
);
Set(varEstSST, CountRows(Filter(colRoles, Courriel = varMoi && Role = "Conseiller SST")) > 0);
Set(varRole, If(varEstSST, "Conseiller SST", "Gestionnaire"));
Set(varDossier, Defaults(SST_Dossiers));
Set(varNouveauType, "Accident");
Set(varAutoEnvoi, false);
Set(varVue, "face");
Set(varB1Zone, "");
Set(varB2Zone, "")
'''


def to_fr(code):
    """Convertit une formule Power Fx (séparateurs en-US) vers les séparateurs français (; ;; ,)."""
    out, i, n = [], 0, len(code)
    while i < n:
        ch = code[i]
        if ch == '"':
            j = i + 1
            while j < n:
                if code[j] == '"':
                    if j + 1 < n and code[j + 1] == '"':
                        j += 2
                        continue
                    break
                j += 1
            out.append(code[i:j + 1]); i = j + 1; continue
        if ch == "'":
            j = code.index("'", i + 1); out.append(code[i:j + 1]); i = j + 1; continue
        if ch == '/' and code[i:i + 2] == '//':
            j = code.find('\n', i); j = n if j < 0 else j
            out.append(code[i:j]); i = j; continue
        if ch == ';':
            out.append(';;')
        elif ch == ',':
            out.append(';')
        elif ch == '.' and i > 0 and code[i - 1].isdigit() and i + 1 < n and code[i + 1].isdigit():
            out.append(',')
        else:
            out.append(ch)
        i += 1
    return ''.join(out)


def build(outdir):
    from pa import NAMES
    NAMES.clear()
    ecr = os.path.join(outdir, 'Ecrans')
    os.makedirs(ecr, exist_ok=True)
    files = {}
    files['01_scrAccueil.pa.yaml'] = scr_accueil()
    files['02_scrDossiers.pa.yaml'] = scr_dossiers()
    y_acc, f_acc = scr_accident()
    files['03_scrAccident.pa.yaml'] = y_acc
    y_enq, f_enq = scr_enquete()
    files['04_scrEnquete.pa.yaml'] = y_enq
    files['05_scrAnalyse.pa.yaml'] = scr_analyse()
    y_sit, f_sit = scr_situation()
    files['06_scrSituation.pa.yaml'] = y_sit
    y_vio, f_vio = scr_violence()
    files['07_scrViolence.pa.yaml'] = y_vio
    files['08_scrApercu.pa.yaml'] = scr_apercu(f_acc, f_enq, f_sit, f_vio)
    files['09_scrAide.pa.yaml'] = scr_aide()
    for k, v in files.items():
        open(os.path.join(ecr, k), 'w', encoding='utf8').write(v)
    fo = app_formulas()
    ost = app_onstart()
    open(os_path(outdir, 'App_Formulas_FR.txt'), 'w', encoding='utf8').write(to_fr(fo))
    open(os_path(outdir, 'App_OnStart_FR.txt'), 'w', encoding='utf8').write(to_fr(ost))
    open(os_path(outdir, 'App_Formulas_EN.txt'), 'w', encoding='utf8').write(fo)
    open(os_path(outdir, 'App_OnStart_EN.txt'), 'w', encoding='utf8').write(ost)
    return files


def os_path(*a):
    return os.path.join(*a)
