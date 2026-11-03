# -*- coding: utf-8 -*-
"""Vérifications statiques des écrans générés (YAML valide, parenthèses, références)."""
import yaml, re, glob, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_commun import DOSSIER_COLS, listes_generiques
RAC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '3_PowerApps')
cols = {c for c, _, _ in DOSSIER_COLS} | {'ID', 'Title', 'Created', 'Modified'}
listes = {r[0] for r in listes_generiques()}
erreurs = []
noms = set(); formules = []
def walk(ctls, ecran):
    for c in ctls:
        (n, v), = c.items()
        assert n not in noms, 'doublon ' + n
        noms.add(n)
        for k, val in (v.get('Properties') or {}).items():
            formules.append((ecran, n, k, str(val)))
        walk(v.get('Children') or [], ecran)
for f in sorted(glob.glob(os.path.join(RAC, 'Ecrans', '*.yaml'))):
    d = yaml.safe_load(open(f, encoding='utf8'))
    (en, scr), = d['Screens'].items()
    noms.add(en)
    for k, val in scr['Properties'].items():
        formules.append((en, en, k, str(val)))
    walk(scr['Children'], en)
for nm in ['App_Formulas_EN.txt', 'App_OnStart_EN.txt']:
    formules.append(('App', nm, '', '=' + open(os.path.join(RAC, nm), encoding='utf8').read()))

def strip_strings(fx):
    out, i, n = [], 0, len(fx)
    while i < n:
        ch = fx[i]
        if ch == '"':
            j = i + 1
            while True:
                if j >= n: return None
                if fx[j] == '"':
                    if j + 1 < n and fx[j + 1] == '"': j += 2; continue
                    break
                j += 1
            out.append('""'); i = j + 1; continue
        if ch == '/' and fx[i:i+2] == '//':
            j = fx.find('\n', i); i = n if j < 0 else j; continue
        out.append(ch); i += 1
    return ''.join(out)

for ecran, n, k, fx in formules:
    if not fx.startswith('='): erreurs.append((n, k, 'ne commence pas par =')); continue
    t = strip_strings(fx[1:])
    if t is None: erreurs.append((n, k, 'chaîne non fermée')); continue
    pile = []
    for ch in t:
        if ch in '([{': pile.append(ch)
        elif ch in ')]}':
            if not pile or '([{'[')]}'.index(ch)] != pile.pop(): erreurs.append((n, k, 'parenthèse ' + ch)); break
    else:
        if pile: erreurs.append((n, k, 'non fermé ' + ''.join(pile)))
    for ref in re.findall(r'\b((?:acc0|dos|acd|enq|ana|sit|vio|apc|aid)_[A-Za-z0-9_]+)', t):
        if ref not in noms: erreurs.append((n, k, 'contrôle inconnu ' + ref))
    for ref in re.findall(r'\b(?:varDossier|ThisItem)\.([A-Za-z0-9]+)', t):
        if n.startswith('dos_') or 'varDossier.' + ref in t:
            if ref not in cols and ref not in ('n', 't', 'd', 'Value', 'Texte', 'Chemin', 'Niveau', 'CauseRacine', 'ActionTexte', 'ActionResp', 'ActionEcheance', 'ActionStatut'):
                erreurs.append((n, k, 'colonne inconnue ' + ref))
    for ref in re.findall(r'Liste = ""', t):
        pass
for ecran, n, k, fx in formules:
    for l in re.findall(r'Liste = "([^"]+)"', fx):
        if l not in listes: erreurs.append((n, k, 'liste inconnue ' + l))
    for scr in re.findall(r'\b(scr[A-Z][A-Za-z]+)', fx):
        if scr not in noms: erreurs.append((n, k, 'écran inconnu ' + scr))
print('%d contrôles, %d formules vérifiées' % (len(noms), len(formules)))
for e in erreurs[:60]: print('ERREUR', e)
print('OK' if not erreurs else '%d erreurs' % len(erreurs))
