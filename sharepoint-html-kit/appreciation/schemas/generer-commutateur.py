import sys
src = open(sys.argv[1], encoding='utf-8').read()
ns = {}
exec(src.split("pages = []")[0], ns)
css = src.split("CSS = '''")[1].split("'''")[0]
orig = ns['rend']; E = ns['E']
ETATS = {'ici':('#0b5cad','📍 VOUS ÊTES ICI'),'auj':('#1d7a3c','① AUJOURD’HUI'),'ens':('#6b3fa0','② ENSUITE')}
def rend(b):
    if b[0] == 'st':
        _, e, t, bl = b; col, lab = ETATS[e]
        tt = f'<div class="stt">{E(t)}</div>' if t else ''
        return f'<div class="st" style="border-color:{col}"><div class="stl" style="background:{col}">{lab}</div>{tt}{rend(bl)}</div>'
    return orig(b)
ns['rend'] = rend
def st(e,t,b): return ('st',e,t,b)
act, cond, info, page, switch, boucle = ns['act'], ns['cond'], ns['info'], ns['page'], ns['switch'], ns['boucle']
MR = lambda txt: act('VAR','Définir motifRefus (2, 3…)','Définir la variable · Nom : motifRefus',[txt])
MS = lambda txt: act('VAR','Définir message (2, 3…)','Définir la variable · Nom : message',[txt])
p = page('Le commutateur « Action » — où le mettre et quoi y mettre',
 'Il trie chaque dépôt selon son action (sauvegarder · aviser · certifier · approuver) et l’envoie dans la bonne case. Les expressions à copier sont dans mon message.', [
 cond('RoleConnu','empty(outputs(\'Role\')) est égal à true',
  [MR('Vous n’avez aucun rôle dans ce dossier.')],
  [act('DATA','ClesPermises','Composer',[]),
   boucle('Fusionner','outputs(\'ClesPermises\') · simultanéité 1',[act('DATA','Fusion','Composer',[]),act('VAR','Définir une variable 2','Nom : dossier',[])]),
   st('ici','SOUS la boucle Fusionner (pas dedans) : cliquez sur « Ajouter une action » tout en bas de la case « Si Non », cherchez « Commutateur », puis renommez-le « Action ».',
    switch('Action','Activé (fx) : outputs(\'Depot\')?[\'action\']',[
     ('sauvegarder', [st('auj','', cond('PeutSauvegarder','length(outputs(\'ClesPermises\')) est supérieur à 0',[MS('Votre version a été enregistrée.')],[MR('Rien à enregistrer pour votre rôle à cette étape.')]))]),
     ('aviser', [st('auj','', cond('PeutAviser','Et : outputs(\'Role\') est égal à personne · outputs(\'Statut\') est égal à brouillon',
        [act('DATA','AvisTemp','Composer',['date de l’avis = maintenant']), act('VAR','Définir dossier (2…)','Nom : dossier · Valeur : outputs(\'AvisTemp\')',[]),
         act('MAIL','Courriel avis','Office 365 Outlook · Envoyer un courriel (V2)',['À : courriel du supérieur immédiat']), MS('Votre supérieur(e) a été avisé(e).')],
        [MR('Seule la personne en appréciation peut aviser, avant la certification.')]))]),
     ('certifier', [st('ens','', cond('PeutCertifier','Et : Role = personne · Statut = brouillon · type de poste choisi',
        [act('DATA','CertTemp','Composer',['statut « approbation » + certification signée']), act('VAR','Définir dossier','Nom : dossier · outputs(\'CertTemp\')',[]),
         act('MAIL','Courriel approbation','Office 365 Outlook',['À : supérieur immédiat']), MS('Votre certification est enregistrée.')],
        [MR('Certification impossible à cette étape.')]))]),
     ('approuver', [st('ens','', cond('BonneEtape','outputs(\'Role\') est égal à outputs(\'Etape\')',
        [act('DATA','AvecSignature · Suivant','Composer (2 cartes)',[]), act('VAR','Définir dossier','Nom : dossier',[]),
         cond('DerniereApprobation','empty(outputs(\'Suivant\')) est égal à true',[act('MAIL','Courriel « approbations complétées »','',[])],[act('MAIL','Courriel « approbation requise » au suivant','',[])]),
         MS('Votre approbation est enregistrée.')],
        [MR('Ce n’est pas votre étape d’approbation.')]))]),
    ])),
   info('Sous le commutateur (étape suivante) : la condition « Enregistrer » qui écrit le dossier dans SharePoint.')
  ])
])
extra = '''.st{border:2px solid; border-radius:8px; margin:0 0 6px; padding:0 0 2px; background:#fff;}
.stl{color:#fff; font-weight:700; font-size:10px; padding:2px 8px; border-radius:5px 5px 0 0; display:inline-block;}
.stt{font-size:10.5px; padding:2px 8px 4px; font-weight:600;}
.st > .card, .st > .cond, .st > .scope, .st > .info, .st > .switch{margin:0 6px 4px;}'''
open(sys.argv[2],'w',encoding='utf-8').write(f'<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><title>Commutateur Action</title><style>{css}{extra}</style></head><body>{p}</body></html>'); print('OK')
