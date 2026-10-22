import sys
src = open(sys.argv[1], encoding='utf-8').read()
ns = {}
exec(src.split("pages = []")[0] + "\nCSS0 = None\n", ns)
# récupérer le CSS du générateur
css = src.split("CSS = '''")[1].split("'''")[0]
orig = ns['rend']
ETATS = {'ok':('#1d7a3c','✅ OK'),'dep':('#c76a00','⚠️ À DÉPLACER'),'sup':('#b3261e','✖ À SUPPRIMER'),'add':('#0b5cad','➕ À AJOUTER'),'ver':('#8a6d00','🔎 À VÉRIFIER'),'ren':('#8a6d00','✏️ À RENOMMER'),'p2':('#8a4b00','⏸ PLUS TARD (phase 2)')}
def rend(b):
    if b[0] == 'st':
        _, etat, texte, bloc = b
        col, lab = ETATS[etat]
        return f'<div class="st st-{etat}" style="border-color:{col}"><div class="stl" style="background:{col}">{lab}</div><div class="stt">{ns["E"](texte)}</div>{rend(bloc)}</div>'
    return orig(b)
ns['rend'] = rend
def st(etat, texte, bloc): return ('st', etat, texte, bloc)
act, cond, scope, info, page = ns['act'], ns['cond'], ns['scope'], ns['info'], ns['page']

p1 = page('Votre flux 1 au 22 octobre — vérification carte par carte',
 'Redessiné à partir de vos captures. Chaque carte porte un statut. Les cartes marquées ✅ sont bonnes; corrigez celles marquées ⚠️ ✖ ✏️ ➕.', [
 st('ok','Bon déclencheur.', act('SP','Lorsqu’un élément est créé ou modifié','SharePoint · Déclencheur',['Vérifiez … › Paramètres : simultanéité 1 + condition de déclenchement'])),
 st('ok','Les 8 variables sont présentes; les anciennes sont supprimées.', act('VAR','deposant · motifRefus · message · modeTest · nomDeposant · maintenant · texteDepot · dossier','Variables · 8 cartes',[])),
 scope('Traitement','',[
  st('ok','', act('SP','PJ','SharePoint · Obtenir les pièces jointes',[])),
  st('ren','Renommez « Condition » en ContenuVide et vérifiez qu’elle contient ContenuPJ + Définir texteDepot (Si oui) et Définir texteDepot (Si non).', cond('Condition','empty(coalesce(triggerBody()?[\'Contenu\'],\'\')) est égal à true',[act('SP','ContenuPJ','',[]),act('VAR','Définir texteDepot','',[])],[act('VAR','Définir texteDepot','',[])])),
  st('ok','', act('DATA','Depot','Composer',['json(variables(\'texteDepot\'))'])),
  st('ok','', act('DATA','Controle','Composer',['if(… 4 contrôles …)'])),
  st('ok','', act('VAR','Définir motifRefus','Définir la variable',['outputs(\'Controle\')'])),
  cond('DepotValide','empty(variables(\'motifRefus\')) est égal à true ✅',[
    st('ok','', act('SP','ChercherDossier','SharePoint · Obtenir les fichiers (propriétés uniquement)',[])),
    cond('NouveauDossier','length(body(\'ChercherDossier\')?[\'value\']) est égal à 0 ✅',[
      cond('ActionPermiseNouveau','contains(createArray(\'sauvegarder\',\'aviser\'), …) est égal à true ✅',[
        st('ok','', act('U','ResponsableSI','Office 365 Utilisateurs',[])),
        st('ok','', act('U','ResponsableSH','Office 365 Utilisateurs',[])),
        st('sup','Pas utilisée; elle échoue s’il n’y a pas de 3e niveau dans l’annuaire. … › Supprimer.', act('U','ResponsableDir','Office 365 Utilisateurs',[])),
        st('dep','Elle est AVANT CreerDossier : elle doit venir APRÈS (elle utilise l’ItemId du fichier créé). Glissez-la sous CreerDossier.', act('SP','ProprietesNouveau','SharePoint · Mettre à jour les propriétés du fichier',[])),
       ],[st('ok','', act('VAR','Définir une variable (motifRefus)','« Ce dossier n’existe pas encore… »',[]))]),
      st('dep','Ces 4 cartes sont SOUS la condition ActionPermiseNouveau, donc hors de son « Si oui ». Glissez-les DANS le « Si oui », sous ResponsableSH.', act('DATA','Participants · NouveauWorkflow · Définir dossier · CreerDossier','4 cartes',[])),
      st('p2','Vide = sans effet. Si elle contient des actions, supprimez-la pour l’instant.', scope('PermissionsDossier','',[])),
      st('add','Il manque la fin du premier dépôt (guide 5.8) : Définir message + condition AviserDesLaCreation avec le courriel.', info('Définir message · AviserDesLaCreation')),
    ],[
      st('ok','', act('SP','LireDossier','SharePoint · Obtenir le contenu du fichier',['Identificateur : first(body(\'ChercherDossier\')?[\'value\'])?[\'{Identifier}\']'])),
      st('ver','Le nom de la carte peut rester « Définir dossier1 ». Vérifiez seulement : Nom = dossier · Valeur = json(base64ToString(body(\'LireDossier\')?[\'$content\'])).', act('VAR','Définir dossier1','Définir la variable',[])),
      st('add','Prochaine étape : Role, Statut, Etape, RoleConnu, ClesPermises, Fusionner, commutateur Action, enregistrement (guide 6.2 à 6.9).', info('Suite du dossier existant')),
    ])
  ],[st('ok','Vide : c’est normal.', info('(rien)'))])
 ]),
 st('add','À construire à la fin (guide 7) : EnCasErreur, Accepte + courriels, SupprimerDepot.', info('Après l’étendue Traitement'))
])

p2 = page('Branche « premier dépôt » — l’ordre final attendu',
 'Toutes ces cartes vont dans le « Si oui » d’ActionPermiseNouveau, exactement dans cet ordre (de haut en bas).', [
 cond('NouveauDossier','length(body(\'ChercherDossier\')?[\'value\']) est égal à 0',[
  cond('ActionPermiseNouveau','contains(createArray(\'sauvegarder\',\'aviser\'), outputs(\'Depot\')?[\'action\']) est égal à true',[
    act('U','1 · ResponsableSI','Office 365 Utilisateurs · Obtenir le responsable (V2)',['Utilisateur : variables(\'deposant\')']),
    act('U','2 · ResponsableSH','Office 365 Utilisateurs · Obtenir le responsable (V2)',['Utilisateur : body(\'ResponsableSI\')?[\'userPrincipalName\']']),
    act('DATA','3 · Participants','Composer',['guide 5.3']),
    act('DATA','4 · NouveauWorkflow','Composer',['guide 5.4']),
    act('VAR','5 · Définir dossier','Définir la variable · Nom : dossier',['guide 5.5']),
    act('SP','6 · CreerDossier','SharePoint · Créer un fichier',['/Dossiers_Appreciations · <dossierId>.json · string(variables(\'dossier\'))']),
    act('SP','7 · ProprietesNouveau','SharePoint · Mettre à jour les propriétés du fichier',['Id : body(\'CreerDossier\')?[\'ItemId\'] · guide 5.7']),
    act('VAR','8 · Définir message','Définir la variable · Nom : message',['Votre dossier a été créé dans « Mes dossiers ».']),
    cond('9 · AviserDesLaCreation','outputs(\'Depot\')?[\'action\'] est égal à aviser',[
      act('MAIL','Courriel avis','Office 365 Outlook · Envoyer un courriel (V2)',['À : outputs(\'Participants\')?[\'superieur_immediat\']?[\'email\']','Objet et texte : guide, section 8 « Avis au supérieur »'])],[])
  ],[act('VAR','Définir motifRefus','Définir la variable',['Ce dossier n’existe pas encore. Commencez par « Déposer sur SharePoint ».'])])
 ],[info('Dossier existant : LireDossier · Définir dossier · puis la suite (guide 6)')]),
 info('Astuce pour déplacer une carte : cliquez sur son titre et glissez-la jusqu’au « + » à l’endroit voulu. Commencez par la carte du bas (CreerDossier), puis remontez.')
])


boucle = ns['boucle']
p3 = page('Votre flux 2 « AC - Approbation finale » — vérification',
 'PHASE 2 : ce flux a besoin de composantes qui n’existent pas encore (Archives_Appreciations, dossier A_approuver, Config_Appreciations, parametres.json). Il ne pourra pas fonctionner avant. Conseil : mettez-le de côté et terminez d’abord le flux 1.', [
 st('sup','Mauvais déclencheur (« déconseillé ») et « ID du dossier » rempli avec le texte du tableau. Supprimez-le et remplacez-le par le déclencheur ci-dessous.', act('SP','Quand un fichier est créé ou modifié dans un dossier (déconseillé)','SharePoint · Déclencheur',['ID du dossier : /bibliothqes Archives_Appreciations et Config_Appreciations ✖'])),
 st('add','Le bon déclencheur, quand la bibliothèque Archives_Appreciations et son dossier A_approuver existeront.', act('SP','Lorsqu’un fichier est créé ou modifié (propriétés uniquement)','SharePoint · Déclencheur',['Site : SandBox Annie Audet · Bibliothèque : Archives_Appreciations','Dossier : choisir /Archives_Appreciations/A_approuver avec l’icône 📁 (ne pas taper)',"… › Paramètres › Conditions de déclenchement : @not(empty(triggerOutputs()?['body/EmailsApprobateurs']))"])),
 st('ver','Renommez la carte « Param ». Le chemin doit respecter la majuscule : /Config_Appreciations/parametres.json — et ce fichier doit exister (je vous le fournirai en phase 2).', act('SP','Obtenir le contenu du fichier à l’aide du chemin d’accès','SharePoint',['Chemin : /config_Appreciations/parametres.json ⚠️ minuscule'])),
 st('add','La suite du flux 2 (P, Approbation, Resultat, attestation, archivage…) : schémas-flux, page 9 — en phase 2.', info('Suite du flux 2'))
])
p4 = page('Votre flux 3 « AC - Recalcul hebdomadaire des accès » — vérification',
 'PHASE 2 aussi : il lit des colonnes (EmailPersonne, EmailSupImm, EmailSupHier) qui ne sont pas encore dans Dossiers_Appreciations. Vous pouvez le garder, mais ne l’activez pas avant la phase 2.', [
 st('ok','1 semaine · lundi · 6 h · fuseau Est : parfait.', act('PLAN','Périodicité','Planification · Déclencheur',['Intervalle 1 · Semaine · Lundi · 6'])),
 st('ok','Bibliothèque et filtre corrects.', act('SP','Ouverts','SharePoint · Obtenir les fichiers (propriétés uniquement)',["Dossiers_Appreciations · Statut eq 'Brouillon' or Statut eq 'En approbation'"])),
 boucle('ChaqueDossier','body(…) → doit être, en Expression : body(\'Ouverts\')?[\'value\']',[
   st('sup','Boucle en double : Power Automate l’a ajoutée parce que ChaqueDossier reçoit body(…) au lieu de body(\'Ouverts\')?[\'value\']. Corrigez ChaqueDossier, glissez les cartes de cette boucle dans ChaqueDossier, puis supprimez-la.', boucle('Appliquer à chacun','value',[])),
   st('ren','Renommez-la « Profil ». Utilisateur = le courriel de la personne (colonne EmailPersonne, phase 2). … › Configurer l’exécution après : cochez « a réussi » ET « a échoué ».', act('U','Obtenir le profil de l’utilisateur (V2)','Office 365 Utilisateurs',[])),
   st('ver','Les deux lignes ne sont pas bonnes. Ligne 1 (fx) : outputs(\'Profil\')?[\'statusCode\'] est égal à 404 · Ligne 2 (fx) : body(\'Profil\')?[\'accountEnabled\'] est égal à false · « Ou » : correct.', cond('CompteInactif','Ou · Statut404 est égal à false ✖ · accountEnabled est égal à false ⚠️',
     [st('ver','Une boîte partagée RH_Info-SST n’est pas indiquée pour l’appréciation. Utilisez plutôt « Envoyer un courriel (V2) » (votre compte) · À : votre adresse (propriétaire) · Objet : Compte inactif.', act('MAIL','Envoyer un e-mail à partir d’une boîte aux lettres partagée (V2)','Office 365 Outlook',['Boîte : RH_Info-SST ⚠️ · À : Person…'])),
      st('add','Phase 2 : Journal compte inactif (liste Journal_Appreciations).', info('Journal compte inactif'))],
     [st('ver','Renommez « NouveauSupImm ». Utilisateur : le COURRIEL de la personne, pas son « Nom d’affichage » (le service ne trouve personne avec un nom).', act('U','Obtenir le responsable (V2)','Office 365 Utilisateurs',['Utilisateur (UPN) : Nom d’affichage ✖'])),
      st('add','Suite : NouveauSupHier, condition Changement, EncoreBrouillon… (schémas-flux, page 10).', info('Suite du flux 3'))]))
 ])
])

p5 = page('Votre flux 4 « AC - Nettoyage du dépôt » — vérification',
 'Presque terminé ! Ce flux est simple et peut servir dès la phase 1 (il supprime chaque nuit les dépôts que le flux 1 n’a pas traités).', [
 st('ver','Intervalle 1 · Jour · fuseau Est : correct. Mais « Aux heures indiquées » est vide : inscrivez 2 (sinon il s’exécute à l’heure de création du flux).', act('PLAN','Périodicité','Planification · Déclencheur',['Aux heures indiquées : (vide) ⚠️ → 2'])),
 st('ver','Site et liste corrects. IMPORTANT : cliquez sur « Afficher les options avancées » et remplissez la Requête de filtre. Sans filtre, il supprime TOUS les dépôts, même ceux de la dernière minute.', act('SP','Orphelins','SharePoint · Obtenir les éléments',['Liste : Depot_Appreciations ✅',"Requête de filtre : Created lt '@{addHours(utcNow(), -2)}' ⚠️ à ajouter"])),
 boucle('ChaqueOrphelin','body(…) ✅ — vérifiez, en Expression : body(\'Orphelins\')?[\'value\']',[
   st('ok','Site, liste et ID corrects.', act('SP','SupprimerOrphelin','SharePoint · Supprimer l’élément',["ID : items('ChaqueOrphelin')?['ID']"])),
   st('ver','La liste Journal_Appreciations existe : bien. Le Titre est vide : inscrivez le n° du dépôt, en Expression : concat(\'Dépôt orphelin supprimé #\', items(\'ChaqueOrphelin\')?[\'ID\']). (Les autres colonnes du journal : phase 2.)', act('SP','JournalOrphelin','SharePoint · Créer un élément',['Liste : Journal_Appreciations ✅ · Titre : (vide) ⚠️'])),
 ])
])

extra = '''.st{border:2px solid; border-radius:8px; margin:0 0 6px; padding:0 0 2px; background:#fff;}
.stl{color:#fff; font-weight:700; font-size:10px; padding:2px 8px; border-radius:5px 5px 0 0; display:inline-block;}
.stt{font-size:10.5px; padding:2px 8px 4px; font-weight:600;}
.st > .card, .st > .cond, .st > .scope, .st > .info{margin:0 6px 4px;}'''
out = f'<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><title>Vérification du flux 1</title><style>{css}{extra}</style></head><body>{p1}{p2}{p3}{p4}{p5}</body></html>'
open(sys.argv[2],'w',encoding='utf-8').write(out); print('OK')
