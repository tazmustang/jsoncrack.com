# -*- coding: utf-8 -*-
"""Textes affichés dans l'application (repris des formulaires Forms et des prototypes HTML)."""

CARTE_ACCIDENT = "Déclarer immédiatement tout accident ou incident, peu importe sa gravité. Rempli par le gestionnaire avec l'employé, la journée même. Mène à l'enquête et à l'analyse 5 Pourquoi."
CARTE_SITUATION = "Vous observez une situation dangereuse qui ne peut être corrigée immédiatement ? Sécurisez les lieux, avisez votre gestionnaire et signalez-la ici."
CARTE_VIOLENCE = "Évènement potentiellement traumatique, agression, incivilité ou harcèlement subi par un employé de la part d'un citoyen ou d'un partenaire externe."
URGENCE = "En cas d'urgence, composez le 911 (assistance policière ou transport par ambulance). Les situations entre collègues ou avec un gestionnaire relèvent de la Politique pour contrer l'incivilité, le harcèlement et la violence au travail."

NOTE_REMPLI_SEUL = "Important : si l'état de santé de l'employé ne lui permet pas de remplir le formulaire avec son gestionnaire la journée même de l'évènement, le gestionnaire remplit seul le formulaire et rencontrera l'employé dès que son état de santé le permettra, afin de valider l'information soumise."
AIDE_TACHE = "Préciser exactement ce que l'employé était en train de faire lorsque l'évènement est survenu (ex. : en dévissant un tuyau, en déposant des documents dans le classeur, en changeant une conduite d'aqueduc, en me dirigeant à une réunion)."
AIDE_MELITO = ("Décrire clairement la série d'évènements qui a entraîné l'accident ou l'incident. Donnez des précisions sur les faits reliés au MELITO "
               "(Moment/Temps, Équipement/Matériel, Lieu/Environnement, Individu, Tâche, Organisation) et décrire la blessure subie. "
               "Trucs : écrire au « JE »; répondre aux questions Qui? Quoi? Où? Quand? Comment?; toute personne qui lit doit comprendre ce qui s'est réellement passé, même sans connaître le milieu de travail. Moins de 255 caractères.")
AIDE_MELITO_GEST = ("Décrivez clairement la série d'évènements qui a entraîné l'accident ou l'incident (MELITO : Moment/Temps, Équipement/Matériel, Lieu/Environnement, Individu, Tâche, Organisation). "
                    "Répondre aux questions Qui? Quoi? Où? Quand? Comment? Moins de 255 caractères.")
CONTACT_REPONDANT = "Pour signaler une problématique relative à ce formulaire ou en cas de désaccord avec la version du travailleur, communiquez avec votre répondant SST."

ENQUETE_INTRO = ("L'enquête et l'analyse d'accident forment un processus en deux étapes pour éviter qu'un accident ne se reproduise. "
                 "L'ENQUÊTE (la collecte) : la recherche immédiate des faits. On recueille les indices, prend des photos et interroge les témoins pour savoir ce qui s'est passé. "
                 "Cette collecte s'appuie sur trois axes : l'organisation du travail (consignes, formations, planification et répartition des tâches); "
                 "l'environnement et les équipements (état du matériel, aménagement des lieux et contraintes physiques); "
                 "le comportement des personnes concernées (actions, faits et décisions observés lors de l'évènement). "
                 "L'ANALYSE (la compréhension) : la recherche des causes. On étudie les faits collectés pour comprendre pourquoi cela s'est passé et identifier les failles. "
                 "En résumé : l'enquête rassemble les pièces du puzzle, l'analyse les assemble pour corriger le problème.")
AXE_ORG = ("Cet axe examine le cadre, les méthodes et la planification mis en place par l'organisation avant que l'évènement ne survienne. On cherche à savoir si les conditions de travail théoriques étaient adéquates et sécuritaires. "
           "Ce qu'on évalue : la clarté des consignes et des procédures de travail; la formation reçue par le travailleur (était-il qualifié/informé des risques ?); "
           "la gestion du temps, le rythme de travail, la charge de travail et le niveau de fatigue; la répartition des tâches et la qualité de la supervision sur le terrain. Plusieurs choix possibles.")
AXE_ENV = ("Cet axe examine le milieu physique et le matériel utilisé au moment de l'évènement. L'objectif est d'identifier toutes les anomalies ou contraintes matérielles ayant pu jouer un rôle déclencheur ou aggravant. "
           "Ce qu'on évalue : l'état des équipements (outils, machines, équipements de protection individuelle); l'entretien, le bon fonctionnement et la présence des protecteurs/dispositifs de sécurité; "
           "les conditions des lieux (éclairage, bruit, température, ventilation, encombrement du sol, état des surfaces); la disposition et l'ergonomie du poste de travail. Plusieurs choix possibles.")
AXE_COMP = ("Cet axe documente les actions, les faits et les décisions des personnes impliquées juste avant et pendant l'évènement. Attention : il ne s'agit pas de blâmer, mais de comprendre pourquoi une action a été posée dans ce contexte précis. "
            "Ce qu'on évalue : les gestes effectifs et la position du corps au moment de l'évènement; le respect ou l'écart par rapport aux méthodes de travail habituelles ou prescrites; "
            "la perception du danger par le travailleur (était-il conscient du risque ?); la communication ou la coordination entre les membres de l'équipe au moment des faits. Plusieurs choix possibles.")
AXE_MESURES = "Proposer des mesures correctives réalistes afin d'éviter qu'une situation semblable ne survienne à nouveau. Plusieurs choix possibles."

AIDE_PROBLEME = "Décrivez le problème de façon précise, factuelle et sans désigner de responsable (ex. : « Pourquoi les évaluations de risque sont-elles incomplètes pour ce type de dossier ? » plutôt qu'un énoncé vague ou accusateur)."
ARBRE_VIDE = "Aucun « Pourquoi » pour l'instant. Cliquez sur « + Ajouter un Pourquoi » pour démarrer, ou créez les branches à partir des facteurs cochés dans l'enquête."
SYNTH_VIDE = "Aucune cause n'est encore marquée « cause racine ». Utilisez « Marquer cause racine » sur la réponse où l'équipe a réellement le pouvoir d'agir, puis décrivez l'action corrective ici."
PIEGE_TOOLTIP = "Une erreur ou un oubli n'est jamais la cause profonde : cherchez plutôt pourquoi le système a permis cette erreur (formation, charge de travail, ergonomie, consignes...)."
LEGENDE_5P_HTML = ("<div style='font-size:12px;color:#6B7280'>"
                   "<span style='color:#00285E'>■</span> Pourquoi 1 &nbsp; <span style='color:#074B98'>■</span> Pourquoi 2 &nbsp; "
                   "<span style='color:#00796B'>■</span> Pourquoi 3 &nbsp; <span style='color:#6B3FA0'>■</span> Pourquoi 4 &nbsp; "
                   "<span style='color:#857650'>■</span> Pourquoi 5 et plus</div>")

GUIDE_5P_HTML = """<div style='font-size:13px;line-height:1.55;color:#1F2937'>
<p>Cette méthode consiste à demander « Pourquoi ? » de façon répétée face à un problème, afin de dépasser sa cause apparente et de remonter jusqu'à sa cause profonde. En général, cinq questions suffisent, mais une chaîne peut être plus courte ou plus longue.</p>
<p style='color:#00285E;font-weight:bold;margin-bottom:2px'>1. Bien poser le problème</p>
<ul><li>Énoncez un fait observable, pas un jugement.</li><li>L'objectif est de comprendre un processus, pas de désigner une personne responsable.</li></ul>
<p style='color:#00285E;font-weight:bold;margin-bottom:2px'>2. Creuser, puis savoir quand s'arrêter</p>
<ul><li>Restez factuel à chaque réponse : appuyez-vous sur ce qui est observé ou vérifiable.</li>
<li>Un problème peut avoir plusieurs causes contributives : ouvrez une branche séparée pour chacune.</li>
<li>Arrêtez de creuser une branche dès que la réponse devient illogique, se répète ou sort du champ d'action de l'équipe : revenez à la réponse précédente et cherchez une autre piste.</li>
<li>Une cause racine est atteinte quand la réponse décrit quelque chose sur lequel l'équipe peut réellement agir.</li></ul>
<p style='color:#00285E;font-weight:bold;margin-bottom:2px'>3. Agir et vérifier</p>
<ul><li>Pour chaque cause racine, définissez une action corrective concrète, avec un responsable et une échéance.</li>
<li>Revenez vérifier que l'action a réellement empêché le problème de se reproduire (statut « Efficacité vérifiée »).</li></ul>
<p style='color:#00285E;font-weight:bold;margin-bottom:2px'>4. Quatre pièges classiques</p>
<ul><li><b>S'arrêter à « l'erreur humaine »</b> : c'est le symptôme d'un système qui l'a rendue possible. L'application signale ces réponses.</li>
<li><b>S'enfermer dans une seule ligne</b> : ouvrez une branche par facteur.</li>
<li><b>S'arrêter à une cause « acceptable »</b> pour éviter un sujet délicat.</li>
<li><b>Remonter trop loin</b>, jusqu'à des causes générales sur lesquelles personne n'a de prise.</li></ul>
<p style='color:#00285E;font-weight:bold;margin-bottom:2px'>5. Test du « Donc »</p>
<p>Relisez la chaîne à l'envers en remplaçant chaque « Pourquoi » par « donc ». Si l'enchaînement ne sonne pas juste, un maillon manque. L'application génère cette relecture automatiquement sous le plan d'action.</p>
<div style='background:#ECF1F7;border-left:4px solid #857650;padding:8px 10px'><b>Astuce :</b> si une réponse dépend de quelque chose hors du contrôle de l'équipe, revenez à la réponse précédente et cherchez une piste qui relève de votre sphère d'influence.</div>
</div>"""

SITUATION_INTRO = ("Si vous observez dans votre milieu de travail une situation dangereuse, sécurisez immédiatement les lieux et avisez votre gestionnaire afin qu'il prenne en charge la problématique. "
                   "Si la situation dangereuse ne peut être corrigée immédiatement, vous devez remplir ce formulaire.")
VIOLENCE_INTRO = ("Ce formulaire vise à déclarer un évènement potentiellement traumatique, un acte violent, une agression, une situation impliquant un manque de respect, de l'incivilité ou du harcèlement subi par un employé de la Ville, "
                  "de la part d'un citoyen ou d'un partenaire externe (sous-traitants, fournisseurs, etc.). Avant de le compléter : 1) composez le 911 si la situation requiert l'assistance de la police ou un transport par ambulance; "
                  "2) gérez la situation et les priorités sur le terrain, si possible. ATTENTION : les évènements en lien avec des collègues ou des gestionnaires ne doivent pas être adressés via ce formulaire "
                  "(voir la Politique pour contrer l'incivilité, le harcèlement et la violence au travail). Ce formulaire ne s'applique pas au service de police et de protection contre les incendies.")
BOUCLIER = ("Le Comité bouclier a pour mission : 1) de soutenir et protéger les employés victimes de harcèlement, d'intimidation, de diffamation ou de gestes violents commis par un citoyen, un fournisseur ou tout autre tiers externe; "
            "2) d'accompagner les gestionnaires dans la gestion de ces situations; 3) d'analyser chaque situation dénoncée et, le cas échéant, de prendre des mesures pour la corriger. "
            "Actions possibles : juridiques, policières, communications internes ou externes, soutien à l'employé. Le comité est formé de gestionnaires de la Direction générale, du Service de police, des Ressources humaines, "
            "de l'Interaction citoyenne, des Communications, des Affaires juridiques, de l'Arrondissement de La Cité-Limoilou, de la Gestion du territoire et de la Gestion des matières résiduelles et de la valorisation.")

# ---------------------------------------------------------------- Styles en ligne du PDF (Segoe UI / Arial)
ST_BODY = "font-family:Segoe UI,Arial,sans-serif;color:#1F2937;font-size:10pt"
ST_H1 = "color:#00285E;font-size:18pt;margin:6px 0"
ST_H2 = "color:#00285E;font-size:12.5pt;border-bottom:2px solid #857650;padding-bottom:3px;margin:18px 0 8px"
ST_TABLE = "width:100%;border-collapse:collapse;font-size:9.5pt"
ST_TH = "border:1px solid #E5E7EB;padding:5px 7px;text-align:left;vertical-align:top;background:#ECF1F7;width:38%;color:#00285E"
ST_TD = "border:1px solid #E5E7EB;padding:5px 7px;text-align:left;vertical-align:top"
ST_THG = "border:1px solid #E5E7EB;padding:5px 7px;text-align:left;background:#ECF1F7;color:#00285E"
CSS_PDF = "@page{margin:18mm} body{margin:0}"

HTML_5P = ('If(CountRows(colNoeudsPdf) = 0, "",\n'
           ' "<h2 style=\'' + ST_H2 + '\'>Analyse des causes (5 Pourquoi)</h2><p><b>Problème identifié :</b> " & varDossier.Probleme & "<br><b>Analyse menée par :</b> " & varDossier.AnalysteNom & "</p>" &\n'
           ' Concat(Sort(colNoeudsPdf, Chemin), "<div style=\'margin:4px 0 4px " & (Niveau - 1) * 18 & "px;border-left:3px solid " & Switch(Min(Niveau, 5), 1, "#00285E", 2, "#074B98", 3, "#00796B", 4, "#6B3FA0", "#857650") & ";padding:3px 8px;background:#F9FAFB\'><b>Pourquoi " & Niveau & " ?</b> " & Texte & If(CauseRacine, " <span style=\'background:#C80000;color:#FFFFFF;padding:1px 6px;font-size:8pt\'>CAUSE RACINE</span>", "") & "</div>") &\n'
           ' If(CountRows(Filter(colNoeudsPdf, CauseRacine)) = 0, "",\n'
           '  "<h2 style=\'' + ST_H2 + '\'>Plan d\'action — causes racines</h2><table style=\'' + ST_TABLE + '\'><tr><th style=\'' + ST_THG + '\'>Cause racine</th><th style=\'' + ST_THG + '\'>Action corrective</th><th style=\'' + ST_THG + '\'>Responsable</th><th style=\'' + ST_THG + '\'>Échéance</th><th style=\'' + ST_THG + '\'>Statut</th></tr>" &\n'
           '  Concat(Filter(Sort(colNoeudsPdf, Chemin), CauseRacine), "<tr><td style=\'' + ST_TD + '\'>" & Texte & "</td><td style=\'' + ST_TD + '\'>" & ActionTexte & "</td><td style=\'' + ST_TD + '\'>" & ActionResp & "</td><td style=\'' + ST_TD + '\'>" & Text(ActionEcheance, "yyyy-mm-dd") & "</td><td style=\'' + ST_TD + '\'>" & ActionStatut & "</td></tr>") & "</table>"))')

# ---------------------------------------------------------------- Pages d'aide
def _p(t):
    return "<p>" + t + "</p>"


def _h(t):
    return "<h3 style='color:#00285E;font-size:16px;border-bottom:2px solid #857650;padding-bottom:3px'>" + t + "</h3>"


def _ul(items):
    return "<ul>" + "".join("<li>" + i + "</li>" for i in items) + "</ul>"


_DIV = "<div style='font-size:13px;line-height:1.55;color:#1F2937'>"
AIDE_HTML = [
    _DIV + _h("Déclaration d'accident ou d'incident de travail")
    + _p("Ce formulaire permet de déclarer immédiatement tous les accidents et tous les incidents de travail aux instances concernées, peu importe leur gravité, afin d'établir les mesures appropriées pour éviter qu'un tel évènement se reproduise.")
    + "<p><b>Étape 1</b> — Le gestionnaire remplit ce formulaire conjointement avec l'employé, la journée même de l'évènement.</p>"
    + "<p style='background:#ECF1F7;padding:8px'><b>Important :</b> si l'état de santé de l'employé ne lui permet pas de remplir le formulaire avec son gestionnaire la journée même, le gestionnaire le remplit seul et rencontrera l'employé dès que possible pour valider l'information.</p>"
    + "<p><b>Étape 2</b> — Le gestionnaire identifie, documente et applique des mesures préventives immédiates. Lorsqu'une enquête et analyse d'évènement est requise, un plan d'action de mesures correctives est élaboré par un comité d'enquête paritaire SST.</p>"
    + _h("Accident ou incident ?")
    + _ul(["<b>Accident</b> : l'employé a eu une blessure physique apparente ou non.", "<b>Incident</b> : passé proche, l'employé aurait pu se blesser (aucune blessure ni douleur; sinon, c'est un accident)."])
    + _h("Niveau de gravité (ou de gravité potentielle pour un incident)")
    + _ul(["<b>Élevée (enquête obligatoire)</b> : ex. le décès d'un employé; la perte totale ou partielle d'un membre ou de son usage; un traumatisme physique important; des blessures à plusieurs employés occasionnant une absence de 1 jour ouvrable, excluant la journée de l'accident; des dommages matériels de 150 000 $ et plus.",
           "<b>Moyenne (enquête obligatoire)</b> : accident provoquant une absence qui dépasse la journée de l'évènement, électrisation ou incident qui aurait pu entraîner une blessure ou une maladie réversible. Si l'employé est en assignation temporaire.",
           "<b>Faible</b> : accident sans aucune perte de temps (blessure mineure) ou incident qui aurait pu causer une blessure mineure."])
    + _h("Bien décrire l'évènement (MELITO)")
    + _ul(["<b>M</b>oment / temps, <b>É</b>quipement / matériel, <b>L</b>ieu / environnement, <b>I</b>ndividu, <b>T</b>âche, <b>O</b>rganisation.", "Écrire au « JE ».", "Répondre à : Qui? Quoi? Où? Quand? Comment?", "Toute personne qui lit doit comprendre ce qui s'est réellement passé, même sans connaître le milieu de travail."])
    + _h("Dans l'application")
    + _ul(["Remplissez les onglets dans l'ordre (le n° 4 « Blessures » apparaît seulement pour un accident).", "<b>☁️ Enregistrer</b> conserve un brouillon que vous retrouvez dans <b>📂 Mes dossiers</b>.", "<b>☁️ Enregistrer et déposer</b> vérifie les champs obligatoires (*), dépose la déclaration, produit le PDF et l'envoie à la Division SST (et à l'employé s'il a choisi une copie courriel).", "La barre d'étapes (7 cercles) montre l'avancement : vert ✓ = étape faite (avec la date), gris = à venir."])
    + _p(CONTACT_REPONDANT) + "</div>",

    _DIV + _h("Enquête — la collecte des faits") + _p(ENQUETE_INTRO.replace(". ", ".<br>", 0))
    + _ul(["<b>L'organisation du travail</b> — " + AXE_ORG, "<b>L'environnement et les équipements</b> — " + AXE_ENV, "<b>Le comportement des personnes concernées</b> — " + AXE_COMP, "<b>Mesures correctives suggérées</b> — " + AXE_MESURES])
    + _h("Analyse — la méthode des 5 Pourquoi") + GUIDE_5P_HTML
    + _h("Dans l'application")
    + _ul(["Depuis un dossier (📂 Mes dossiers), ouvrez <b>🔍 Enquête</b>, cochez les facteurs constatés puis enregistrez : l'étape 4 passe au vert.", "Dans <b>🌳 Analyse 5 Pourquoi</b>, cliquez « Créer les branches à partir des facteurs de l'enquête » pour démarrer l'arbre, puis creusez chaque branche avec « + Pourquoi ».", "Marquez la ou les causes racines, puis remplissez l'action, le responsable, l'échéance et le statut : l'étape 5 (analyse) puis l'étape 6 (plan d'action complet) passent au vert.", "Le PDF du dossier inclut l'enquête, l'arbre et le plan d'action."]) + "</div>",

    _DIV + _h("Signalement d'une situation dangereuse") + _p(SITUATION_INTRO)
    + _p("En cas de besoin, conservez une ou vos photos dans vos dossiers personnels pour la suite des choses.")
    + _ul(["Tous les employés peuvent remplir ce formulaire (rôle « Employé »).", "Si vous le demandez, votre syndicat ou association est mis en copie du PDF (si son courriel est configuré par la Division SST).", "Le conseiller SST indique la prise en charge, la mesure corrective et la fermeture du dossier (4 étapes)."]) + "</div>",

    _DIV + _h("Évènement traumatisant et acte de violence") + _p(VIOLENCE_INTRO) + _h("Comité bouclier") + _p(BOUCLIER)
    + _ul(["Le formulaire est complété par le gestionnaire avec l'employé; l'approbation de l'employé fait office de signature.", "Si vous sollicitez le Comité bouclier, le PDF lui est aussi transmis (si son courriel est configuré)."]) + "</div>",

    _DIV + _h("À propos")
    + _p("Application de déclaration et de suivi en santé et sécurité au travail : accidents et incidents (avec enquête et analyse 5 Pourquoi), situations dangereuses, évènements traumatisants et actes de violence.")
    + _ul(["<b>Rôles</b> : Gestionnaire (déclarations de son équipe), Employé (situation dangereuse), Conseiller SST (voit tous les dossiers, assure le suivi et la fermeture). Le rôle Conseiller SST est accordé par la liste SharePoint SST_Roles.",
           "<b>Données</b> : listes SharePoint de la Ville (SST_Dossiers, SST_Pourquoi) et PDF dans la bibliothèque SST_PDF. Aucune donnée n'est stockée hors de Microsoft 365.",
           "<b>Confidentialité</b> : les renseignements de santé sont confidentiels; ne les transmettez qu'aux personnes autorisées.",
           "Formulaires propriété de la Division de la santé et de la sécurité au travail — Ville de Québec."])
    + "</div>",
]
