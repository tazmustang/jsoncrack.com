import sys
src = open(sys.argv[1], encoding='utf-8').read()
ns = {}
exec(src.split("pages = []")[0], ns)
css = src.split("CSS = '''")[1].split("'''")[0]
orig = ns['rend']
ETATS = {'ok':('#1d7a3c','✅ OK'),'dep':('#c76a00','⚠️ À DÉPLACER'),'sup':('#b3261e','✖ À SUPPRIMER'),'add':('#0b5cad','➕ PROCHAINE ÉTAPE'),'ver':('#8a6d00','🔎 PETITE CORRECTION'),'p2':('#8a4b00','⏸ PLUS TARD')}
E = ns['E']
def rend(b):
    if b[0] == 'st':
        _, etat, texte, bloc = b
        col, lab = ETATS[etat]
        t = f'<div class="stt">{E(texte)}</div>' if texte else ''
        return f'<div class="st" style="border-color:{col}"><div class="stl" style="background:{col}">{lab}</div>{t}{rend(bloc)}</div>'
    return orig(b)
ns['rend'] = rend
def st(e, t, b): return ('st', e, t, b)
act, cond, scope, info, page, boucle = ns['act'], ns['cond'], ns['scope'], ns['info'], ns['page'], ns['boucle']
p1 = page('Votre flux 1 au 23 octobre — vérification', 'Redessiné à partir de vos 5 captures. Presque tout est bon : 3 petites corrections, puis on construit la suite (encadrés bleus).', [
 st('ok','Déclencheur et 8 variables.', act('SP','Lorsqu’un élément est créé ou modifié · deposant · motifRefus · message · modeTest · nomDeposant · maintenant · texteDepot · dossier','',[])),
 scope('Traitement','',[
  st('ok','', act('SP','PJ','',[])),
  st('ok','Bien renommée. Le nom « Définir textedepot2 » peut rester : vérifiez seulement Nom = texteDepot.', cond('ContenuVide','empty(…) est égal à true',[act('SP','ContenuPJ','',[]),act('VAR','Définir textedepot2','',[])],[act('VAR','Définir texteDepot','',[])])),
  st('ok','« Sorties » de Controle (contenu dynamique) = outputs(\'Controle\') : correct.', act('DATA','Depot · Controle · Définir motifRefus','',[])),
  cond('DepotValide','✅',[
   st('ok','', act('SP','ChercherDossier','',[])),
   cond('NouveauDossier','✅',[
     cond('ActionPermiseNouveau','✅',[
       st('ok','Bon ordre, ResponsableDir supprimée.', act('U','ResponsableSI · ResponsableSH · Participants · NouveauWorkflow · Définir dossier · CreerDossier · ProprietesNouveau','',[])),
       st('ver','Renommez-la « Définir message » et vérifiez : Nom = message · Valeur = Votre dossier a été créé dans « Mes dossiers ».', act('VAR','Définir une variable','',[])),
       st('ok','Condition et courriel corrects (en mode test, il arrive dans votre boîte).', cond('AviserDesLaCreation','action est égal à aviser',[act('MAIL','Envoyer un e-mail (V2)','À : superieur_immediat',[])],[])),
      ],[st('ver','Le texte contient des apostrophes au début et à la fin et il est coupé. Effacez-le et tapez : Ce dossier n’existe pas encore. Commencez par « Déposer sur SharePoint ».', act('VAR','Définir une variable (motifRefus)','Valeur : \'Ce dossier n’existe pas encore\'',[]))]),
     st('sup','Elle est hors d’ActionPermiseNouveau et sert seulement en phase 2. Si elle est vide : … › Supprimer.', scope('PermissionsDossier','',[])),
    ],[
     st('ok','', act('SP','LireDossier','',[])),
     st('ok','Nom = dossier · json(…) : correct.', act('VAR','Définir dossier1','',[])),
     st('add','À ajouter sous « Définir dossier1 » : Role, Statut, Etape, RoleConnu, ClesPermises, Fusionner (détail dans mon message).', info('Role · Statut · Etape · RoleConnu · ClesPermises · Fusionner')),
     st('add','Ensuite : le commutateur Action, puis l’enregistrement (prochaine séance).', info('Commutateur Action · Enregistrer')),
    ])
  ],[st('ok','Vide : normal.', info('(rien)'))])
 ]),
 st('add','À la toute fin (après Traitement) : EnCasErreur, Accepte + courriels, SupprimerDepot.', info('Fin du flux'))
])
extra = '''.st{border:2px solid; border-radius:8px; margin:0 0 6px; padding:0 0 2px; background:#fff;}
.stl{color:#fff; font-weight:700; font-size:10px; padding:2px 8px; border-radius:5px 5px 0 0; display:inline-block;}
.stt{font-size:10.5px; padding:2px 8px 4px; font-weight:600;}
.st > .card, .st > .cond, .st > .scope, .st > .info{margin:0 6px 4px;}'''
open(sys.argv[2],'w',encoding='utf-8').write(f'<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><title>Flux 1 au 23 octobre</title><style>{css}{extra}</style></head><body>{p1}</body></html>'); print('OK')
