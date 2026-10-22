# Génère les schémas des 4 flux (HTML paginé) pour impression en PDF
import html, sys
E = html.escape
C = {'SP':('#036c70','SP'),'U':('#0f6cbd','U'),'MAIL':('#0f6cbd','✉'),'OD':('#1957a6','OD'),'APP':('#107c41','✓'),'VAR':('#7719aa','x'),'DATA':('#8a3b00','{}'),'PLAN':('#2b88d8','⏱')}

def act(kind, nom, typ, lignes=(), note=None, phase2=False):
    return ('act', kind, nom, typ, list(lignes), note, phase2)
def cond(nom, expr, oui, non, note=None, phase2=False):
    return ('cond', nom, expr, oui, non, note, phase2)
def scope(nom, sous, enfants, phase2=False, note=None):
    return ('scope', nom, sous, enfants, phase2, note)
def boucle(nom, expr, enfants, phase2=False):
    return ('loop', nom, expr, enfants, phase2)
def switch(nom, expr, cas):
    return ('switch', nom, expr, cas)
def info(t, rouge=False):
    return ('info', t, rouge)

def badge2(p): return '<span class="p2">Phase 2</span>' if p else ''

def rend(b):
    t = b[0]
    if t == 'act':
        _, kind, nom, typ, lignes, note, p2 = b
        col, ic = C[kind]
        l = ''.join(f'<div class="code">{E(x)}</div>' for x in lignes)
        n = f'<div class="note">{E(note)}</div>' if note else ''
        return f'<div class="card{" ph2" if p2 else ""}"><div class="ic" style="background:{col}">{E(ic)}</div><div class="bd"><div class="nm">{E(nom)} {badge2(p2)}</div><div class="ty">{E(typ)}</div>{l}{n}</div></div>'
    if t == 'cond':
        _, nom, expr, oui, non, note, p2 = b
        n = f'<div class="note">{E(note)}</div>' if note else ''
        o = ''.join(rend(x) for x in oui) or '<div class="rien">(rien)</div>'
        no = ''.join(rend(x) for x in non) or '<div class="rien">(rien)</div>'
        return f'<div class="cond{" ph2" if p2 else ""}"><div class="hd"><span class="tag tc">CONDITION</span> <b>{E(nom)}</b> {badge2(p2)}<div class="code">{E(expr)}</div>{n}</div><div class="br"><div class="col"><div class="oui">Si oui</div>{o}</div><div class="col"><div class="non">Si non</div>{no}</div></div></div>'
    if t == 'scope':
        _, nom, sous, enf, p2, note = b
        n = f'<div class="note">{E(note)}</div>' if note else ''
        return f'<div class="scope{" ph2" if p2 else ""}"><div class="hd"><span class="tag ts">ÉTENDUE</span> <b>{E(nom)}</b> {badge2(p2)}<div class="ty">{E(sous)}</div>{n}</div><div class="in">{"".join(rend(x) for x in enf)}</div></div>'
    if t == 'loop':
        _, nom, expr, enf, p2 = b
        return f'<div class="loop{" ph2" if p2 else ""}"><div class="hd"><span class="tag tl">APPLIQUER À CHACUN</span> <b>{E(nom)}</b> {badge2(p2)}<div class="code">{E(expr)}</div></div><div class="in">{"".join(rend(x) for x in enf)}</div></div>'
    if t == 'switch':
        _, nom, expr, cas = b
        cs = ''.join(f'<div class="cas"><div class="cl">Cas « {E(l)} »</div>{"".join(rend(x) for x in bl)}</div>' for l, bl in cas)
        return f'<div class="switch"><div class="hd"><span class="tag tw">COMMUTATEUR</span> <b>{E(nom)}</b><div class="code">{E(expr)}</div></div>{cs}</div>'
    if t == 'info':
        _, txt, rouge = b
        return f'<div class="info{" rouge" if rouge else ""}">{E(txt)}</div>'

LEG = ''.join(f'<span><i style="background:{c}"></i>{n}</span>' for n, c in [('SharePoint','#036c70'),('Office 365 Utilisateurs','#0f6cbd'),('Office 365 Outlook','#0f6cbd'),('OneDrive','#1957a6'),('Approbations','#107c41'),('Variables','#7719aa'),('Opérations de données','#8a3b00'),('Planification','#2b88d8')]) + '<span><span class="p2">Phase 2</span> = avant le déploiement réel, pas nécessaire pour tester</span>'

def page(titre, sous, blocs):
    return f'<section class="page"><h1>{E(titre)}</h1><p class="sous">{E(sous)}</p><div class="leg">{LEG}</div>{"".join(rend(b) for b in blocs)}</section>'

pages = []

# ---------- Page de garde
garde = '''<section class="page garde">
<h1 style="font-size:28px">Schémas des flux Power Automate — Appréciation de la contribution</h1>
<p class="sous">Version 3.8 de l'application · 22 octobre 2026 · site de test SandBox Annie Audet. Ces schémas remplacent ceux d'octobre (avant le dépôt par copier-coller).</p>
<table class="t">
<tr><th>Flux</th><th>Rôle</th><th>Déclencheur</th><th>Quand le construire</th><th>Pages</th></tr>
<tr><td><b>1 · AC - Traiter un dépôt</b></td><td>Lit chaque dépôt (champ « Contenu » ou fichier joint), vérifie l'identité et l'étape, crée ou met à jour le dossier, envoie les courriels</td><td>Élément créé ou modifié dans Depot_Appreciations</td><td><b>Phase 1 — pour tester</b> (mode test)</td><td>2 à 7</td></tr>
<tr><td>1 · étendue PreparationApprobationFinale</td><td>Produit le PDF final après la dernière approbation</td><td>(dans le flux 1)</td><td>Phase 2</td><td>8</td></tr>
<tr><td><b>2 · AC - Approbation finale</b></td><td>Fait approuver le document final par tous, archive le PDF et l'attestation</td><td>PDF déposé dans Archives_Appreciations/A_approuver</td><td>Phase 2</td><td>9</td></tr>
<tr><td><b>3 · AC - Recalcul hebdomadaire des accès</b></td><td>Ajuste les accès si un gestionnaire change</td><td>Chaque lundi 6 h</td><td>Phase 2</td><td>10</td></tr>
<tr><td><b>4 · AC - Nettoyage du dépôt</b></td><td>Supprime les dépôts restés dans la liste</td><td>Chaque jour 2 h</td><td>Phase 2</td><td>11</td></tr>
</table>
<h2>Composantes SharePoint</h2>
<table class="t">
<tr><th>Composante</th><th>Phase</th><th>Remarque</th></tr>
<tr><td>Liste <b>Depot_Appreciations</b> + colonne <b>Contenu</b> (texte brut)</td><td>1</td><td>Pièces jointes activées · chacun ne voit que ses dépôts</td></tr>
<tr><td>Bibliothèque <b>Dossiers_Appreciations</b></td><td>1</td><td>DossierId, NomPersonne, TypePoste, Statut, EtapeEnCours, DerniereMaj · versions activées</td></tr>
<tr><td>Liste Journal_Appreciations · bibliothèques Archives_Appreciations et Config_Appreciations</td><td>2</td><td>Voir le guide du 7 octobre (référentiel, gabarits, parametres.json)</td></tr>
</table>
<h2>Règles de construction</h2>
<ul>
<li>Les noms en gras sont les noms exacts à donner aux actions (menu … › Renommer) : les expressions en dépendent.</li>
<li>Les expressions complètes sont dans <b>5-GUIDE-FLUX-DEPOT</b> (numéros de section indiqués sur les cartes). Collez-les dans l'onglet Expression (fx).</li>
<li>Mode test : variable <b>modeTest</b> = true → tous les participants ont votre adresse et le rôle est celui choisi dans l'application. Pour le pilote réel : false.</li>
<li>Phase 1 : construisez avec votre compte, dans le site de test, avec des données fictives. Phase 2 : compte de service et site dédié (TI).</li>
<li>Ancien schéma → nouveau : la variable <b>fusion</b> s'appelle maintenant <b>dossier</b>, <b>messageSucces</b> devient <b>message</b>, et role / clesPermises / nomFichierDossier / idElementDossier sont remplacés par les actions Composer <b>Role</b>, <b>ClesPermises</b>, etc.</li>
</ul>
</section>'''
pages.append(garde)

S5 = 'Expression complète : 5-GUIDE-FLUX-DEPOT, section '

# ---------- Flux 1 — 1/6
pages.append(page('Flux 1 « AC - Traiter un dépôt » — 1/6 : déclencheur, variables, lecture et contrôle',
 'Flux de cloud automatisé. Les blocs à partir de « PJ » sont dans l’étendue « Traitement ».', [
 act('SP','Lorsqu’un élément est créé ou modifié','SharePoint · Déclencheur',[
   'Adresse du site : SandBox Annie Audet · Nom de la liste : Depot_Appreciations',
   'Paramètres › Contrôle de la simultanéité : activé, degré de parallélisme 1',
   "Paramètres › Conditions de déclenchement : @or(not(empty(triggerOutputs()?['body/Contenu'])), equals(triggerOutputs()?['body/Attachments'], true))"],
   note='La condition attend qu’il y ait un contenu collé ou une pièce jointe (SharePoint ajoute le fichier juste après avoir créé l’élément).'),
 act('VAR','modeTest','Variables · Initialiser une variable',['Type : Booléen · Valeur : true']),
 act('VAR','deposant','Variables · Initialiser une variable',["Type : Chaîne · Valeur : toLower(triggerBody()?['Author']?['Email'])"]),
 act('VAR','nomDeposant','Variables · Initialiser une variable',["Type : Chaîne · Valeur : triggerBody()?['Author']?['DisplayName']"]),
 act('VAR','maintenant','Variables · Initialiser une variable',["Type : Chaîne · Valeur : formatDateTime(convertFromUtc(utcNow(),'Eastern Standard Time'),'yyyy-MM-dd HH:mm')"]),
 act('VAR','texteDepot · dossier · motifRefus · message','Variables · Initialiser une variable (4 actions)',['texteDepot : Chaîne · dossier : Objet · motifRefus : Chaîne · message : Chaîne — toutes vides']),
 scope('Traitement','Toutes les étapes de traitement', [
   act('SP','PJ','SharePoint · Obtenir les pièces jointes',["ID : triggerBody()?['ID']"]),
   cond('ContenuVide',"empty(coalesce(triggerBody()?['Contenu'],'')) est égal à true",
     [act('SP','ContenuPJ','SharePoint · Obtenir le contenu de la pièce jointe',["Id de l’élément : triggerBody()?['ID']","Identificateur du fichier : first(body('PJ'))?['Id']"]),
      act('VAR','Définir texteDepot','Variables · Définir la variable',["base64ToString(body('ContenuPJ')?['$content'])"],note="Si erreur « json » : string(body('ContenuPJ'))")],
     [act('VAR','Définir texteDepot','Variables · Définir la variable',["triggerBody()?['Contenu']"])],
     note='Oui = dépôt par fichier joint (sur le poste) · Non = dépôt par copier-coller (dans SharePoint)'),
   act('DATA','Depot','Opérations de données · Composer',["json(variables('texteDepot'))"]),
   act('DATA','Controle','Opérations de données · Composer',['if(… 4 contrôles : contenu ou une seule pièce jointe, format, action, identifiant …)'],note=S5+'4.4 (variante recommandée)'),
   act('VAR','Définir motifRefus','Variables · Définir la variable',["outputs('Controle')"]),
   cond('DepotValide',"empty(variables('motifRefus')) est égal à true",
     [act('SP','ChercherDossier','SharePoint · Obtenir les fichiers (propriétés uniquement)',['Bibliothèque : Dossiers_Appreciations',"Requête de filtre : DossierId eq '@{outputs('Depot')?['dossierId']}'",'Nombre maximal : 1']),
      cond('NouveauDossier',"length(body('ChercherDossier')?['value']) est égal à 0",
        [info('Premier dépôt : page 2/6')],[info('Dossier existant : pages 3/6, 4/6 et 5/6')])],
     [])
 ]),
 info('Après « Traitement » : étendue « EnCasErreur », réponse au déposant et nettoyage (page 6/6).')
]))

# ---------- Flux 1 — 2/6
pages.append(page('Flux 1 — 2/6 : branche « Si oui » de NouveauDossier (premier dépôt)',
 'Le dossier est créé à partir de l’annuaire. Les sections du supérieur que la personne aurait pu remplir sont vidées.', [
 cond('ActionPermiseNouveau',"contains(createArray('sauvegarder','aviser'), outputs('Depot')?['action']) est égal à true",
  [act('U','ResponsableSI','Office 365 Utilisateurs · Obtenir le responsable (V2)',["Utilisateur : variables('deposant')"]),
   act('U','ResponsableSH','Office 365 Utilisateurs · Obtenir le responsable (V2)',["Utilisateur : body('ResponsableSI')?['userPrincipalName']"]),
   act('U','ResponsableDir','Office 365 Utilisateurs · Obtenir le responsable (V2)',["Utilisateur : body('ResponsableSH')?['userPrincipalName']",'Paramètres › Exécuter après : « a réussi » et « a échoué »'],phase2=True),
   act('DATA','Participants','Opérations de données · Composer',['personne, supérieur immédiat, supérieur hiérarchique (nom + courriel)','en mode test : votre adresse partout'],note=S5+'5.3'),
   act('DATA','NouveauWorkflow','Opérations de données · Composer',['statut brouillon · version 1 · certification et approbations vides · date de l’avis si « aviser »'],note=S5+'5.4'),
   act('VAR','Définir dossier','Variables · Définir la variable',["setProperty(… formulaire, 'leadershipSup' = {}, 'bilanSuperieur' = '', 'evaluationGlobale' = '', 'workflow' = NouveauWorkflow)"],note=S5+'5.5'),
   act('SP','CreerDossier','SharePoint · Créer un fichier',['Chemin : /Dossiers_Appreciations',"Nom : concat(outputs('Depot')?['dossierId'],'.json')","Contenu : string(variables('dossier'))"]),
   act('SP','ProprietesNouveau','SharePoint · Mettre à jour les propriétés du fichier',["Id : body('CreerDossier')?['ItemId']",'DossierId, NomPersonne, TypePoste, Statut = Brouillon, EtapeEnCours, DerniereMaj']),
   scope('PermissionsDossier','Le dossier n’est visible que par ses participants',[
     act('SP','CasserHeritage','SharePoint · Envoyer une requête HTTP à SharePoint',["POST _api/web/lists/getbytitle('Dossiers_Appreciations')/items(ItemId)/breakroleinheritance(copyRoleAssignments=false,clearSubscopes=true)"]),
     act('SP','GroupeProprietaires · AccesProprietaires','SharePoint · Envoyer une requête HTTP (2 actions)',['GET _api/web/associatedownergroup · POST …/roleassignments/addroleassignment(principalid=…,roledefid=1073741829)']),
     boucle('DonnerLecture','createArray(personne, supérieur immédiat, supérieur hiérarchique)',[
       act('SP','AssurerUtilisateur','SharePoint · Envoyer une requête HTTP',['POST _api/web/ensureuser']),
       act('SP','AjouterLecture','SharePoint · Envoyer une requête HTTP',['POST …/roleassignments/addroleassignment(principalid=…,roledefid=1073741826)'])])],phase2=True),
   act('VAR','Définir message','Variables · Définir la variable',['Votre dossier a été créé dans « Mes dossiers ».']),
   cond('AviserDesLaCreation',"outputs('Depot')?['action'] est égal à aviser",
     [act('MAIL','Courriel avis','Office 365 Outlook · Envoyer un courriel (V2)',["À : outputs('Participants')?['superieur_immediat']?['email']",'Modèle « Avis au supérieur » (section 8)'])],[])],
  [act('VAR','Définir motifRefus','Variables · Définir la variable',['Ce dossier n’existe pas encore. Commencez par « Déposer sur SharePoint ».'])])
]))

# ---------- Flux 1 — 3/6
pages.append(page('Flux 1 — 3/6 : branche « Si non » de NouveauDossier (dossier existant)',
 'Le rôle vient du compte qui a déposé, jamais du fichier (sauf en mode test). Seules les sections permises sont recopiées.', [
 act('SP','LireDossier','SharePoint · Obtenir le contenu du fichier',["Identificateur : first(body('ChercherDossier')?['value'])?['{Identifier}']"]),
 act('VAR','Définir dossier','Variables · Définir la variable',["json(base64ToString(body('LireDossier')?['$content']))"],note="Si erreur : json(string(body('LireDossier')))"),
 act('DATA','Role','Opérations de données · Composer',["mode test : roleDeclare · sinon : deposant = personne / supérieur immédiat / hiérarchique / directeur, ou ''"],note=S5+'6.2'),
 act('DATA','Statut','Opérations de données · Composer',["variables('dossier')?['workflow']?['status']"]),
 act('DATA','Etape','Opérations de données · Composer',['qui doit approuver maintenant : supérieur immédiat › hiérarchique › directeur, ou vide'],note=S5+'6.4'),
 cond('RoleConnu',"empty(outputs('Role')) est égal à true",
   [act('VAR','Définir motifRefus','Variables · Définir la variable',['Vous n’avez aucun rôle dans ce dossier.'])],
   [act('DATA','ClesPermises','Opérations de données · Composer',['sections modifiables selon le rôle et le statut (personne / supérieur immédiat, brouillon / approbation)'],note=S5+'6.6'),
    boucle('Fusionner',"outputs('ClesPermises') · Paramètres : simultanéité 1",[
      act('DATA','Fusion','Opérations de données · Composer',["setProperty(variables('dossier'), item(), outputs('Depot')?['formulaire']?[item()])"]),
      act('VAR','Définir dossier','Variables · Définir la variable',["outputs('Fusion')"])]),
    info('Ensuite, toujours dans cette branche : le commutateur « Action » (page 4/6), puis l’enregistrement (page 5/6).')])
]))

# ---------- Flux 1 — 4/6
pages.append(page('Flux 1 — 4/6 : commutateur « Action » (branche « dossier existant »)',
 'Chaque cas vérifie que c’est la bonne personne, à la bonne étape. Sinon, motifRefus est rempli et rien n’est enregistré.', [
 switch('Action',"outputs('Depot')?['action']",[
  ('sauvegarder',[cond('PeutSauvegarder',"greater(length(outputs('ClesPermises')),0) est égal à true",
     [act('VAR','Définir message','Variables',['Votre version a été enregistrée.'])],
     [act('VAR','Définir motifRefus','Variables',['Rien à enregistrer pour votre rôle à cette étape.'])])]),
  ('aviser',[cond('PeutAviser',"and(Role = personne, Statut = brouillon)",
     [act('DATA','AvisTemp','Composer',["setProperty(… workflow.avisSuperieur.date = maintenant)"],note=S5+'6.8'),
      act('VAR','Définir dossier','Variables',["outputs('AvisTemp')"]),
      act('MAIL','Courriel avis','Office 365 Outlook · Envoyer un courriel (V2)',['À : supérieur immédiat · modèle « Avis au supérieur »']),
      act('VAR','Définir message','Variables',['Votre supérieur(e) a été avisé(e).'])],
     [act('VAR','Définir motifRefus','Variables',['Seule la personne en appréciation peut aviser, avant la certification.'])])]),
  ('certifier',[cond('PeutCertifier',"and(Role = personne, Statut = brouillon, type de poste choisi)",
     [act('DATA','CertTemp','Composer',["setProperty(… status = 'approbation', certification = {signed, nom, email, date})"],note=S5+'6.8'),
      act('VAR','Définir dossier','Variables',["outputs('CertTemp')"]),
      act('SP','LectureDirecteur','SharePoint · requêtes HTTP (si directeur applicable)',['ensureuser + addroleassignment (lecture)'],phase2=True),
      act('MAIL','Courriel approbation','Office 365 Outlook · Envoyer un courriel (V2)',['À : supérieur immédiat · modèle « Approbation requise »']),
      act('VAR','Définir message','Variables',['Votre certification est enregistrée. Le dossier est verrouillé.'])],
     [act('VAR','Définir motifRefus','Variables',['Certification impossible à cette étape.'])])]),
  ('approuver',[cond('BonneEtape',"equals(outputs('Role'), outputs('Etape'))",
     [act('DATA','AvecSignature','Composer',["approbations[Role] = {signed, nom, email, date}"],note=S5+'6.8 b'),
      act('DATA','Suivant','Composer',['prochain rôle à approuver, ou vide']),
      act('VAR','Définir dossier','Variables',["si Suivant vide : status = 'signature' · sinon : outputs('AvecSignature')"]),
      cond('DerniereApprobation',"empty(outputs('Suivant')) est égal à true",
        [act('MAIL','Courriel approbations complétées','Office 365 Outlook',['À : personne + supérieur immédiat']),
         info('Phase 2 : étendue « PreparationApprobationFinale » (page 8)'),
         act('VAR','Définir message','Variables',['Votre approbation est enregistrée.'])],
        [act('MAIL','Courriel suivant','Office 365 Outlook',['À : personne de « Suivant » (mode test : vous) · « Approbation requise »']),
         act('VAR','Définir message','Variables',['Votre approbation est enregistrée. La personne suivante a été avisée.'])])],
     [act('VAR','Définir motifRefus','Variables',['Ce n’est pas votre étape d’approbation.'])])])
 ])
]))

# ---------- Flux 1 — 5/6
pages.append(page('Flux 1 — 5/6 : enregistrement du dossier (fin de la branche « dossier existant »)',
 'Exécuté seulement si aucun refus. Chaque enregistrement laisse une version dans la bibliothèque : c’est l’historique du dossier.', [
 cond('Enregistrer',"empty(variables('motifRefus')) est égal à true",
  [act('DATA','Versionne','Opérations de données · Composer',["setProperty(… workflow.version + 1, workflow.derniereMaj = maintenant)"],note=S5+'6.9'),
   act('SP','Mettre à jour le dossier','SharePoint · Mettre à jour le fichier',["Fichier : first(body('ChercherDossier')?['value'])?['{Identifier}']","Contenu : string(outputs('Versionne'))"]),
   act('SP','Proprietes du dossier','SharePoint · Mettre à jour les propriétés du fichier',["Id : first(body('ChercherDossier')?['value'])?['ID']",'NomPersonne, Statut (Brouillon / En approbation / En approbation finale), EtapeEnCours, DerniereMaj'])],
  [])
]))

# ---------- Flux 1 — 6/6
pages.append(page('Flux 1 — 6/6 : erreurs, réponse au déposant et nettoyage',
 'Ces blocs sont au niveau principal du flux, après l’étendue « Traitement ». Réglez « Configurer l’exécution après » dans les paramètres de chaque bloc.', [
 scope('EnCasErreur','Exécuter après « Traitement » : a échoué, a expiré',[
   cond('SansMotif',"empty(variables('motifRefus')) est égal à true",
     [act('VAR','Définir motifRefus','Variables',['Le dépôt n’a pas pu être lu. Recommencez avec le bouton « Copier le contenu du dépôt ».'])],[])]),
 cond('Accepte',"empty(variables('motifRefus')) est égal à true",
   [act('MAIL','Courriel accepté','Office 365 Outlook · Envoyer un courriel (V2)',["À : variables('deposant') · « Dépôt accepté » + variables('message')"]),
    act('SP','Journal accepté','SharePoint · Créer un élément',['Journal_Appreciations · Resultat = Accepté'],phase2=True)],
   [act('MAIL','Courriel refusé','Office 365 Outlook · Envoyer un courriel (V2)',["À : variables('deposant') · « Dépôt refusé » + variables('motifRefus')"]),
    act('SP','Journal refusé','SharePoint · Créer un élément',['Journal_Appreciations · Resultat = Refusé · Motif'],phase2=True)],
   note='Exécuter après « EnCasErreur » : a réussi, a été ignoré'),
 act('SP','SupprimerDepot','SharePoint · Supprimer l’élément',["Liste : Depot_Appreciations · ID : triggerBody()?['ID']",'Exécuter après : toutes les cases cochées'])
]))

# ---------- Phase 2 : PreparationApprobationFinale
pages.append(page('Flux 1 — phase 2 : étendue « PreparationApprobationFinale »',
 'Placée dans le cas « approuver », quand la dernière approbation est obtenue. Le PDF est produit à partir du dossier officiel (variable dossier), jamais du dépôt. EmailsApprobateurs est rempli en dernier : c’est ce qui déclenche le flux 2.', [
 scope('PreparationApprobationFinale','Phase 2',[
  act('SP','Referentiel · Ref','SharePoint · Obtenir le contenu du fichier à l’aide du chemin, puis Composer',['/Config_Appreciations/referentiel-formulaires.json · json(…)']),
  act('SP','Gabarit','SharePoint · Obtenir le contenu du fichier à l’aide du chemin',['/Config_Appreciations/gabarit-document-final.html']),
  act('DATA','F · TypePoste','Opérations de données · Composer (2 actions)',["variables('dossier') · outputs('F')?['identification']?['typePoste']"]),
  act('DATA','Tables du document','Opérations de données · Créer une table HTML (plusieurs actions)',['objectifs, postures ou compétences, valeurs retenues, développement, évaluation globale']),
  act('DATA','Doc1 … DocFinal','Opérations de données · Composer',['remplacements [[…]] dans le gabarit · retrait du bloc directeur si non applicable']),
  act('OD','HtmlTemp → Pdf','OneDrive · Créer un fichier, puis Convertir un fichier',['/AC_Temp/<dossierId>.html → PDF']),
  act('SP','PdfAApprouver','SharePoint · Créer un fichier',['/Archives_Appreciations/A_approuver · contenu : body(\'Pdf\')']),
  act('OD','SupprimerHtml','OneDrive · Supprimer le fichier',["body('HtmlTemp')?['Id']"]),
  act('SP','Permissions du PDF','SharePoint · requêtes HTTP',['breakroleinheritance · lecture pour chaque participant']),
  act('SP','ProprietesPdf','SharePoint · Mettre à jour les propriétés du fichier',['DossierId, NomPersonne, TypeDocument, Annee …'],note='EmailsApprobateurs EN DERNIER : il déclenche le flux 2')],phase2=True)
]))

# ---------- Flux 2
pages.append(page('Flux 2 « AC - Approbation finale » — phase 2',
 'Flux de cloud automatisé. Une exécution par document final. Délai de 28 jours (une exécution ne peut pas dépasser 30 jours).', [
 act('SP','Lorsqu’un fichier est créé ou modifié (propriétés uniquement)','SharePoint · Déclencheur',['Bibliothèque : Archives_Appreciations · Dossier : /Archives_Appreciations/A_approuver',"Conditions de déclenchement : @not(empty(triggerOutputs()?['body/EmailsApprobateurs']))"]),
 act('SP','Param · P','SharePoint · Obtenir le contenu du fichier à l’aide du chemin, puis Composer',['/Config_Appreciations/parametres.json · json(…)']),
 act('APP','Approbation','Approbations · Démarrer et attendre une approbation',['Type : Approuver/Refuser — Tout le monde doit approuver',"Attribué à : triggerOutputs()?['body/EmailsApprobateurs'] · Lien : le PDF · Délai : P28D"]),
 act('DATA','Resultat · Reponses','Opérations de données · Composer, Créer une table HTML',['approuvé par tous / refusé · table des réponses']),
 act('SP','Attestation','SharePoint + OneDrive (plusieurs actions)',['gabarit-attestation-approbation.html → PDF → /Archives_Appreciations/<année>']),
 act('SP','DeplacerFinal','SharePoint · Déplacer un fichier',['A_approuver › /Archives_Appreciations/<année>']),
 act('SP','ChercherDossierFinal → ContenuDossierFinal','SharePoint',["Dossiers_Appreciations · DossierId eq '…'"]),
 cond('TousApprouvent',"body('Approbation')?['outcome'] est égal à Approve",
   [act('SP','Dossier complété','SharePoint · Mettre à jour le fichier + les propriétés',["workflow.status = 'complete' · Statut = Complété"]),
    cond('AvisPaie','avisPaie.actif = true ET AvisPaieEnvoye vide',
      [act('MAIL','Courriel paie','Office 365 Outlook',['évaluation globale seulement; le PDF n’est pas joint']),
       act('SP','AvisPaieEnvoye','SharePoint · Mettre à jour les propriétés',['AvisPaieEnvoye = utcNow()'])],[])],
   [act('SP','Dossier refusé','SharePoint · Mettre à jour les propriétés du fichier',['Statut = Refusé à l’approbation finale']),
    act('MAIL','Courriel refus','Office 365 Outlook',['À : propriétaires et RH · table des réponses'])]),
 act('SP','Journal','SharePoint · Créer un élément',['Journal_Appreciations · Action = approbation finale']),
 scope('SiDelaiExpire','Branche parallèle après « Approbation » · Exécuter après : a expiré',[
   act('MAIL','Courriel rappel','Office 365 Outlook',['personnes sans réponse + propriétaires · relancer : vider puis réinscrire EmailsApprobateurs'])])
]))

# ---------- Flux 3
pages.append(page('Flux 3 « AC - Recalcul hebdomadaire des accès » — phase 2',
 'Flux de cloud planifié. Ajuste les accès si un gestionnaire change pendant le brouillon; alerte seulement si le dossier est déjà en approbation.', [
 act('PLAN','Périodicité','Planification · Déclencheur',['Intervalle : 1 semaine · lundi 06:00 · fuseau Est']),
 act('SP','Ouverts','SharePoint · Obtenir les fichiers (propriétés uniquement)',["Dossiers_Appreciations · Filtre : Statut eq 'Brouillon' or Statut eq 'En approbation'"]),
 boucle('ChaqueDossier',"body('Ouverts')?['value'] · simultanéité 1",[
   act('U','Profil','Office 365 Utilisateurs · Obtenir le profil utilisateur (V2)',['courriel de la personne (lu dans le dossier)','Exécuter après : a réussi + a échoué']),
   cond('CompteInactif','statut 404 OU accountEnabled = false',
     [act('MAIL','Courriel compte inactif','Office 365 Outlook',['À : propriétaires']),act('SP','Journal compte inactif','SharePoint · Créer un élément',['Journal_Appreciations'])],
     [act('U','NouveauSupImm · NouveauSupHier','Office 365 Utilisateurs · Obtenir le responsable (V2) (2 actions)',[]),
      cond('Changement','nouveau supérieur immédiat ou hiérarchique ≠ celui du dossier',
        [cond('EncoreBrouillon','Statut est égal à Brouillon',
           [act('SP','Reinitialiser','SharePoint · requêtes HTTP',['réinitialiser puis redonner les accès aux 3 participants']),
            act('SP','MajParticipants','SharePoint · Mettre à jour le fichier + les propriétés',['participants du dossier']),
            act('MAIL','Courriel nouveau supérieur','Office 365 Outlook',[]),
            act('SP','Journal réassignation','SharePoint · Créer un élément',[])],
           [act('MAIL','Courriel décision requise','Office 365 Outlook',['À : propriétaires et RH · aucun changement automatique']),
            act('SP','Journal','SharePoint · Créer un élément',[])])],[])])])
]))

# ---------- Flux 4
pages.append(page('Flux 4 « AC - Nettoyage du dépôt » — phase 2',
 'Flux de cloud planifié. Filet de sécurité : supprime les dépôts restés dans la liste (flux 1 en échec ou dépôt incomplet).', [
 act('PLAN','Périodicité','Planification · Déclencheur',['Intervalle : 1 jour · 02:00 · fuseau Est']),
 act('SP','Orphelins','SharePoint · Obtenir les éléments',['Liste : Depot_Appreciations',"Requête de filtre : Created lt '@{addHours(utcNow(), -2)}'"]),
 boucle('ChaqueOrphelin',"body('Orphelins')?['value']",[
   act('SP','SupprimerOrphelin','SharePoint · Supprimer l’élément',["ID : items('ChaqueOrphelin')?['ID']"]),
   act('SP','JournalOrphelin','SharePoint · Créer un élément',['Journal_Appreciations · Action = dépôt orphelin supprimé'])])
]))

CSS = '''
@page{size:A4 landscape; margin:10mm;}
*{box-sizing:border-box;}
body{margin:0; font-family:"Segoe UI",Arial,sans-serif; color:#1d2633; font-size:11px;}
.page{page-break-after:always; padding:2px;}
.page:last-child{page-break-after:auto;}
h1{font-size:18px; margin:0 0 3px; color:#12355b;}
h2{font-size:14px; margin:14px 0 6px; color:#12355b;}
.sous{margin:0 0 6px; color:#5b6675;}
.leg{display:flex; flex-wrap:wrap; gap:10px; margin:0 0 8px; font-size:10px; color:#5b6675;}
.leg span{display:inline-flex; align-items:center; gap:4px;}
.leg i{width:10px; height:10px; border-radius:2px; display:inline-block;}
.card{display:flex; border:1px solid #c9d1db; border-radius:6px; background:#fff; margin:0 0 6px; overflow:hidden; break-inside:avoid;}
.card .ic{width:30px; color:#fff; font-weight:700; display:flex; align-items:center; justify-content:center; font-size:11px; flex:0 0 30px;}
.card .bd{padding:4px 8px; min-width:0;}
.nm{font-weight:700; font-size:11.5px;}
.ty{color:#5b6675; font-size:10px;}
.code{font-family:Consolas,monospace; font-size:9.5px; white-space:pre-wrap; word-break:break-word;}
.note{background:#fff4e0; color:#8a4b00; font-size:9.5px; padding:1px 5px; border-radius:3px; margin-top:2px; display:inline-block;}
.cond,.scope,.loop,.switch{border:1px solid #9fc5a8; border-radius:7px; margin:0 0 6px; background:#f4faf5;}
.scope{border-color:#9aa6b6; background:#f7f8fa;}
.loop{border-color:#8fb3d9; background:#f3f7fc;}
.switch{border-color:#b9a3d9; background:#f8f5fc;}
.hd{padding:5px 8px; border-bottom:1px solid rgba(0,0,0,.08);}
.in{padding:6px 8px;}
.tag{color:#fff; font-size:9px; font-weight:700; padding:1px 5px; border-radius:3px;}
.tc{background:#2e7d32;} .ts{background:#5b6675;} .tl{background:#2b6cb0;} .tw{background:#6b3fa0;}
.br{display:flex; gap:8px; padding:6px 8px;}
.br .col{flex:1; min-width:0;}
.oui{color:#1d7a3c; font-weight:700; font-size:10px; margin-bottom:3px;}
.non{color:#b3261e; font-weight:700; font-size:10px; margin-bottom:3px;}
.rien{color:#8a96a6; font-style:italic; font-size:10px;}
.cas{padding:5px 8px; border-top:1px dashed #cdbfe2;}
.cl{font-weight:700; font-size:10.5px; margin-bottom:3px;}
.info{border:1px dashed #8fb3d9; background:#eef4fb; color:#12355b; border-radius:5px; padding:4px 8px; margin:0 0 6px; font-size:10.5px;}
.p2{background:#fde7c8; color:#8a4b00; border:1px solid #e0a960; font-size:9px; font-weight:700; padding:0 5px; border-radius:8px; white-space:nowrap;}
.ph2{border-style:dashed !important; opacity:.92;}
table.t{border-collapse:collapse; width:100%; font-size:11px; margin:6px 0;}
table.t th, table.t td{border:1px solid #c9d1db; padding:4px 6px; text-align:left; vertical-align:top;}
table.t th{background:#eef2f7;}
.garde ul{font-size:11px; line-height:1.5;}
'''
out = f'<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><title>Schémas des flux Power Automate</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(sys.argv[1],'w',encoding='utf-8').write(out)
print(len(pages),'pages')
