# -*- coding: utf-8 -*-
"""Génère 1_SharePoint/Installer_SharePoint.js (à coller dans la console du navigateur)."""
import json, os
from gen_commun import LISTES, listes_generiques, ORG, TITRES

TYPES = {
    'T': "<Field Type='Text' MaxLength='255' DisplayName='{n}' Name='{n}' StaticName='{n}' Description='{d}'/>",
    'M': "<Field Type='Note' NumLines='6' RichText='FALSE' DisplayName='{n}' Name='{n}' StaticName='{n}' Description='{d}'/>",
    'D': "<Field Type='DateTime' Format='DateOnly' DisplayName='{n}' Name='{n}' StaticName='{n}' Description='{d}'/>",
    'N': "<Field Type='Number' Decimals='0' DisplayName='{n}' Name='{n}' StaticName='{n}' Description='{d}'/>",
    'B': "<Field Type='Boolean' DisplayName='{n}' Name='{n}' StaticName='{n}' Description='{d}'><Default>0</Default></Field>",
}


def esc_xml(s):
    return s.replace('&', '&amp;').replace("'", '&apos;').replace('<', '&lt;')


def build(out_path):
    listes = []
    for titre, desc, cols, vue, index in LISTES:
        listes.append({
            'titre': titre, 'description': desc,
            'champs': [{'nom': n, 'xml': TYPES[t].format(n=n, d=esc_xml(d))} for n, t, d in cols],
            'vue': vue, 'index': index,
        })
    donnees = {
        'SST_Ref_Listes': [{'Title': l, 'Valeur': v, 'Ordre': o, 'Aide': a, 'Courriel': c} for l, v, o, a, c in listes_generiques()],
        'SST_Ref_Org': [{'Title': s, 'Niveau': n, 'Valeur': v, 'Ordre': o} for s, n, v, o in ORG],
        'SST_Ref_Titres': [{'Title': s, 'Classe': c, 'Valeur': v, 'Ordre': o} for s, c, v, o in TITRES],
    }
    js = JS.replace('__LISTES__', json.dumps(listes, ensure_ascii=False, indent=1)) \
           .replace('__DONNEES__', json.dumps(donnees, ensure_ascii=False))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, 'w', encoding='utf8').write(js)
    return sum(len(v) for v in donnees.values())


JS = r"""/* =====================================================================
   Installation SharePoint — Application SST (Déclarations, enquêtes, analyses)
   ---------------------------------------------------------------------
   UTILISATION (voir le guide, section 2) :
   1. Ouvrir le site SharePoint qui hébergera les données (ex. https://<tenant>.sharepoint.com/sites/SST).
      Vous devez en être propriétaire.
   2. Appuyer sur F12 > onglet « Console ». (Chrome/Edge : taper d'abord  allow pasting  puis Entrée.)
   3. Coller TOUT ce fichier, puis Entrée. Attendre le message « INSTALLATION TERMINÉE » (1 à 3 min).
   Le script peut être relancé sans risque : il saute ce qui existe déjà.
   Aucune donnée ne quitte votre organisation : le script utilise votre propre session SharePoint.
   ===================================================================== */
(async () => {
  const site = (window._spPageContextInfo && _spPageContextInfo.webAbsoluteUrl) ||
               location.href.split('/SitePages')[0].split('/Lists')[0].split('/Shared')[0].split('/_layouts')[0].replace(/\/$/, '');
  const LISTES = __LISTES__;
  const DONNEES = __DONNEES__;
  const JSON_H = { 'Accept': 'application/json;odata=nometadata', 'Content-Type': 'application/json;odata=nometadata' };
  let digest = '';
  async function majDigest() {
    const r = await fetch(site + '/_api/contextinfo', { method: 'POST', headers: { 'Accept': 'application/json;odata=nometadata' } });
    digest = (await r.json()).FormDigestValue;
  }
  async function api(url, method = 'GET', body = null, extra = {}) {
    const h = Object.assign({}, JSON_H, extra);
    if (method !== 'GET') h['X-RequestDigest'] = digest;
    const r = await fetch(site + url, { method, headers: h, body: body ? JSON.stringify(body) : null });
    if (!r.ok && r.status !== 404) { const t = await r.text(); throw new Error(method + ' ' + url + ' -> ' + r.status + ' ' + t.slice(0, 300)); }
    if (r.status === 404) return null;
    const t = await r.text(); return t ? JSON.parse(t) : {};
  }
  const L = t => "/_api/web/lists/getbytitle('" + t + "')";
  console.log('%cInstallation SST sur ' + site, 'color:#00285E;font-weight:bold');
  await majDigest();

  for (const liste of LISTES) {
    let info = await api(L(liste.titre) + '?$select=Id');
    if (!info) {
      await api('/_api/web/lists', 'POST', { Title: liste.titre, Description: liste.description, BaseTemplate: 100 });
      console.log('Liste créée : ' + liste.titre);
    } else console.log('Liste existante : ' + liste.titre);
    // Title non obligatoire
    await api(L(liste.titre) + "/fields/getbyinternalnameortitle('Title')", 'POST', { Required: false }, { 'X-HTTP-Method': 'MERGE', 'IF-MATCH': '*' });
    const existants = (await api(L(liste.titre) + '/fields?$select=InternalName&$top=500')).value.map(f => f.InternalName);
    for (const c of liste.champs) {
      if (existants.includes(c.nom)) continue;
      await api(L(liste.titre) + '/fields/createfieldasxml', 'POST', { parameters: { SchemaXml: c.xml, Options: 8 } });
    }
    console.log('  Colonnes OK (' + liste.champs.length + ')');
    for (const c of liste.index) {
      await api(L(liste.titre) + "/fields/getbyinternalnameortitle('" + c + "')", 'POST', { Indexed: true }, { 'X-HTTP-Method': 'MERGE', 'IF-MATCH': '*' });
    }
    // Colonnes dans l'affichage par défaut
    const vue = L(liste.titre) + '/defaultview/viewfields';
    const dejaVue = (await api(vue)).Items || [];
    for (const c of liste.vue) if (!dejaVue.includes(c)) await api(vue + '/addviewfield', 'POST', { strField: c });
  }

  // Bibliothèque des PDF
  if (!(await api(L('SST_PDF') + '?$select=Id'))) {
    await api('/_api/web/lists', 'POST', { Title: 'SST_PDF', Description: 'PDF générés par l\'application SST', BaseTemplate: 101 });
    console.log('Bibliothèque créée : SST_PDF');
  }

  // Données de référence (seulement si la liste est vide)
  for (const [titre, items] of Object.entries(DONNEES)) {
    const n = (await api(L(titre) + '/items?$select=Id&$top=1')).value.length;
    if (n > 0) { console.log(titre + ' contient déjà des données : chargement sauté.'); continue; }
    let i = 0;
    for (const it of items) {
      if (i % 100 === 0) await majDigest();
      await api(L(titre) + '/items', 'POST', it);
      i++; if (i % 50 === 0) console.log('  ' + titre + ' : ' + i + '/' + items.length);
    }
    console.log(titre + ' : ' + i + ' éléments ajoutés');
  }

  // Vous êtes ajouté(e) comme conseiller SST (à retirer au besoin dans la liste SST_Roles)
  const moi = await api('/_api/web/currentuser?$select=Email,Title');
  const roles = (await api(L('SST_Roles') + '/items?$select=Title&$top=500')).value.map(r => (r.Title || '').toLowerCase());
  if (moi.Email && !roles.includes(moi.Email.toLowerCase())) {
    await api(L('SST_Roles') + '/items', 'POST', { Title: moi.Email.toLowerCase(), Role: 'Conseiller SST', Nom: moi.Title });
    console.log('Ajouté(e) à SST_Roles : ' + moi.Email);
  }
  console.log('%cINSTALLATION TERMINÉE. Prochaine étape : guide, section 3 (Power Automate).', 'color:#009E49;font-weight:bold;font-size:14px');
})().catch(e => console.error('ERREUR — notez ce message et relancez le script :', e));
"""

if __name__ == '__main__':
    import sys
    print(build(sys.argv[1]))
