# -*- coding: utf-8 -*-
"""Construction déclarative des formulaires : contrôles + Patch + validation + HTML du PDF."""
from pa import C, s, uniq, label, rect, cont, button, INPUT_STYLE
from textes import ST_TH, ST_TD, ST_H2, ST_TABLE

DATE_FMT = '"yyyy-mm-dd"'


class Form:
    def __init__(self, p):
        self.p = p                  # préfixe des noms de contrôles
        self.tabs = {}              # n° onglet -> liste de contrôles
        self.cur = None
        self.patch = {}             # colonne -> expression
        self.valid = []             # (libellé, condition_obligatoire, expression_vide)
        self.html = []              # (section, [(libellé, colonne, type)])
        self.refs = {}              # colonne -> (nom_contrôle, type)
        self.n = 0

    # ---------------------------------------------------------------- utilitaires
    def tab(self, n):
        self.tabs.setdefault(n, [])
        self.cur = self.tabs[n]
        return self

    def _nm(self, base):
        self.n += 1
        return '%s_%s' % (self.p, base)

    def val(self, col):
        nm, k = self.refs[col]
        return {'text': nm + '.Text', 'multi': nm + '.Text', 'date': nm + '.SelectedDate',
                'drop': nm + '.Selected.Value', 'radio': nm + '.Selected.Value',
                'combo': 'Concat(%s.SelectedItems, Value, "; ")' % nm,
                'check': 'If(%s.Value, "Oui", "Non")' % nm,
                'checks': 'Concat(Filter(%s.AllItems, %s.Value), Value, "; ")' % (nm, nm.replace('_gal', '_chk')),
                }[k]

    def ctl(self, col):
        return self.refs[col][0]

    def _html_row(self, lbl, col, kind):
        if not self.html:
            self.html.append(('Renseignements', []))
        self.html[-1][1].append((lbl, col, kind))

    # ---------------------------------------------------------------- éléments visuels
    def section(self, titre, visible=None, html=True):
        nm = self._nm('sec%d' % self.n)
        p = {'Size': 16, 'FontWeight': 'FontWeight.Bold', 'Color': 'cMarine', 'AutoHeight': True,
             'PaddingTop': 14, 'PaddingBottom': 2}
        if visible:
            p['Visible'] = visible
        self.cur.append(label(nm, s(titre), **p))
        r = {'Height': 2, 'Fill': 'cOr'}
        if visible:
            r['Visible'] = visible
        self.cur.append(rect(self._nm('ligne%d' % self.n), 'cOr', **r))
        if html:
            self.html.append((titre, []))

    def info(self, texte, visible=None, alerte=False, expr=False):
        nm = self._nm('info%d' % self.n)
        p = {'Size': 11, 'Color': 'cMarine' if alerte else 'cTexte2', 'AutoHeight': True, 'Wrap': True}
        if alerte:
            p.update({'Fill': 'cBleuPale', 'PaddingLeft': 12, 'PaddingRight': 12, 'PaddingTop': 8, 'PaddingBottom': 8,
                      'BorderColor': 'cBleu', 'BorderThickness': 1})
        if visible:
            p['Visible'] = visible
        self.cur.append(label(nm, texte if expr else s(texte), **p))

    def raw(self, *ctls):
        for c in ctls:
            self.cur.append(c)

    # ---------------------------------------------------------------- champ générique
    def _field(self, col, lbl, kind, input_ctl, req=False, visible=None, aide=None, html=True, lbl_expr=False):
        texte_lbl = (lbl if lbl_expr else s(lbl))
        if req:
            texte_lbl += ' & " *"'
        lp = {'Size': 12, 'FontWeight': 'FontWeight.Semibold', 'AutoHeight': True, 'Wrap': True, 'PaddingTop': 6}
        if visible:
            lp['Visible'] = visible
        if kind != 'check':
            self.cur.append(label(self._nm('lbl' + col), texte_lbl, **lp))
        if aide:
            ap = {'Size': 10.5, 'Color': 'cTexte2', 'AutoHeight': True, 'Wrap': True}
            if visible:
                ap['Visible'] = visible
            self.cur.append(label(self._nm('aide' + col), aide if aide.startswith('=') else s(aide), **ap))
        if visible:
            input_ctl.props['Visible'] = visible
        self.cur.append(input_ctl)
        self.refs[col] = (input_ctl.name, kind)
        self.patch[col] = self.val(col)
        if req:
            cond = 'true' if req is True else req
            if visible:
                cond = '(%s) && (%s)' % (visible, cond)
            vide = 'IsBlank(%s)' % self.val(col)
            if kind == 'check':
                vide = '!%s.Value' % input_ctl.name
            self.valid.append((lbl if not lbl_expr else col, cond, vide))
        if html:
            self._html_row(lbl if not lbl_expr else col, col, kind)
        return input_ctl

    def _common(self, extra):
        d = dict(INPUT_STYLE)
        d['Reset'] = 'locReset'
        d.update(extra)
        return d

    # ---------------------------------------------------------------- types de champs
    def text(self, col, lbl, req=False, visible=None, aide=None, default=None, hint='', multi=False, maxlen=None,
             width=None, height=None, html=True, compteur=False):
        nm = self._nm(('txt' if not multi else 'txm') + col)
        p = self._common({'Default': default or 'varDossier.%s' % col, 'HintText': s(hint),
                          'Height': height or (90 if multi else 38)})
        if multi:
            p['Mode'] = 'TextMode.MultiLine'
        if maxlen:
            p['MaxLength'] = maxlen
        if width:
            p['Width'] = width
            p['AlignInContainer'] = 'AlignInContainer.Start'
        c = C(uniq(nm), 'text', p)
        self._field(col, lbl, 'multi' if multi else 'text', c, req, visible, aide, html)
        if compteur and maxlen:
            cp = {'Size': 10, 'Color': 'If(Len(%s.Text) >= %d, cRouge, cTexte2)' % (nm, maxlen), 'Align': 'Align.Right',
                  'Height': 20}
            if visible:
                cp['Visible'] = visible
            self.cur.append(label(self._nm('cpt' + col), 'Len(%s.Text) & " / %d"' % (nm, maxlen), **cp))
        return c

    def date(self, col, lbl, req=False, visible=None, aide=None, default=None, html=True):
        nm = self._nm('dte' + col)
        p = self._common({'DefaultDate': default or 'varDossier.%s' % col, 'Format': DATE_FMT, 'Height': 38,
                          'Width': 260, 'AlignInContainer': 'AlignInContainer.Start'})
        for k in ('Size', 'HoverBorderColor', 'FocusedBorderColor', 'FocusedBorderThickness', 'Fill'):
            p.pop(k, None)
        c = C(uniq(nm), 'date', p)
        return self._field(col, lbl, 'date', c, req, visible, aide, html)

    def drop(self, col, lbl, items, req=False, visible=None, aide=None, default=None, html=True, width=None,
             onchange=None, display=None):
        nm = self._nm('drp' + col)
        p = self._common({'Items': items, 'Default': default or 'varDossier.%s' % col, 'AllowEmptySelection': True,
                          'Height': 38, 'ChevronBackground': 'cBleu', 'ChevronFill': 'Color.White',
                          'SelectionFill': 'cBleu'})
        for k in ('HoverBorderColor', 'FocusedBorderColor', 'FocusedBorderThickness'):
            p.pop(k, None)
        if width:
            p['Width'] = width
            p['AlignInContainer'] = 'AlignInContainer.Start'
        if onchange:
            p['OnChange'] = onchange
        if display:
            p['DisplayMode'] = display
        c = C(uniq(nm), 'drop', p)
        return self._field(col, lbl, 'drop', c, req, visible, aide, html)

    def radio(self, col, lbl, options, req=False, visible=None, aide=None, default=None, html=True,
              vertical=False, display=None, lbl_expr=False):
        nm = self._nm('rdo' + col)
        items = '[' + ', '.join(s(o) for o in options) + ']' if isinstance(options, list) else options
        n = len(options) if isinstance(options, list) else 2
        p = {'Items': items, 'Default': default or 'varDossier.%s' % col, 'Reset': 'locReset', 'Size': 12,
             'Color': 'cTexte', 'RadioSelectionFill': 'cBleu', 'RadioBorderColor': 'cTexte2',
             'Layout': 'Layout.Vertical' if vertical else 'Layout.Horizontal',
             'Height': (34 * n + 6) if vertical else 40}
        if display:
            p['DisplayMode'] = display
        c = C(uniq(nm), 'radio', p)
        return self._field(col, lbl, 'radio', c, req, visible, aide, html, lbl_expr=lbl_expr)

    def combo(self, col, lbl, items, req=False, visible=None, aide=None, html=True, hint='Choisir...'):
        nm = self._nm('cmb' + col)
        p = self._common({'Items': items, 'SelectMultiple': True, 'IsSearchable': False,
                          'DisplayFields': '["Value"]', 'SearchFields': '["Value"]',
                          'DefaultSelectedItems': 'ForAll(Filter(Split(varDossier.%s, "; "), !IsBlank(Value)), {Value: ThisRecord.Value})' % col,
                          'InputTextPlaceholder': s(hint), 'Height': 38, 'ChevronBackground': 'cBleu',
                          'ChevronFill': 'Color.White', 'SelectionFill': 'cBleu'})
        for k in ('HoverBorderColor', 'FocusedBorderColor', 'FocusedBorderThickness', 'Fill'):
            p.pop(k, None)
        c = C(uniq(nm), 'combo', p)
        return self._field(col, lbl, 'combo', c, req, visible, aide, html)

    def check(self, col, texte, req=False, visible=None, html=True):
        nm = self._nm('chk' + col)
        p = {'Text': s(texte), 'Default': 'varDossier.%s = "Oui"' % col, 'Reset': 'locReset', 'Size': 12,
             'Color': 'cTexte', 'CheckboxBorderColor': 'cTexte2', 'CheckmarkFill': 'Color.White',
             'CheckboxBackgroundFill': 'Color.White', 'Height': 40}
        c = C(uniq(nm), 'check', p)
        return self._field(col, texte, 'check', c, req, visible, None, html)

    def checks(self, col, lbl, liste, req=False, visible=None, aide=None, html=True, wrap=2):
        """Grille de cases à cocher (galerie) alimentée par colListes."""
        gal = self._nm('gal' + col)
        chk = gal.replace('_gal', '_chk')
        items = 'Sort(Filter(colListes, Liste = %s), Ordre)' % s(liste)
        inner = C(uniq(chk), 'check', {
            'Text': 'ThisItem.Value', 'Default': 'ThisItem.Value in Split(varDossier.%s, "; ").Value' % col,
            'Reset': 'locReset', 'Size': 11, 'Color': 'cTexte', 'CheckboxBorderColor': 'cTexte2',
            'X': 0, 'Y': 0, 'Width': 'Parent.TemplateWidth - 8', 'Height': 'Parent.TemplateHeight - 4'})
        g = C(uniq(gal), 'gal', {
            'Items': items, 'WrapCount': wrap, 'TemplateSize': 40, 'TemplatePadding': 0, 'ShowScrollbar': False,
            'Height': 'RoundUp(CountRows(%s) / %d, 0) * 40 + 4' % (items, wrap),
            'BorderThickness': 0}, [inner], 'Vertical')
        return self._field(col, lbl, 'checks', g, req, visible, aide, html)

    # ---------------------------------------------------------------- sorties
    def patch_record(self, extra=None):
        d = dict(self.patch)
        d.update(extra or {})
        return '{' + ',\n  '.join('%s: %s' % (k, v) for k, v in d.items()) + '}'

    def manquants(self):
        rows = ',\n    '.join('{c: %s, ok: !(%s) || !(%s)}' % (s(l), cond, vide) for l, cond, vide in self.valid)
        return 'Concat(Filter(Table(\n    %s), !ok), c, " • ")' % rows

    def html_expr(self):
        """Expression Power Fx produisant les sections HTML (à partir de varDossier, donc après enregistrement)."""
        parts = []
        for sec, rows in self.html:
            if not rows:
                continue
            cells = []
            for lbl, col, kind in rows:
                v = 'Text(varDossier.%s, %s)' % (col, DATE_FMT) if kind == 'date' else 'varDossier.%s' % col
                cells.append('If(IsBlank(%s), "", "<tr><th style=\'%s\'>%s</th><td style=\'%s\'>" & Substitute(%s, Char(10), "<br>") & "</td></tr>")'
                             % (v, ST_TH, lbl.replace('"', '""'), ST_TD, v))
            parts.append('"<h2 style=\'%s\'>%s</h2><table style=\'%s\'>" &\n  %s &\n  "</table>"' % (ST_H2, sec.replace('"', '""'), ST_TABLE, ' &\n  '.join(cells)))
        return ' &\n'.join(parts)
