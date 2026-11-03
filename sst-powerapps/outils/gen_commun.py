# -*- coding: utf-8 -*-
"""Données communes : listes de référence, colonnes SharePoint, palette."""
import json, os
from refdata import ORG, SYNDICATS, CLASSES, TITRES, ADRESSES, SERVICES, SFMQ

ICI = os.path.dirname(os.path.abspath(__file__))
LISTES_PDF = json.load(open(os.path.join(ICI, 'listes.json'), encoding='utf8'))

# ---------------------------------------------------------------- Palette
PALETTE = [
    ('cOr', '#857650', (133, 118, 80)),
    ('cMarine', '#00285E', (0, 40, 94)),
    ('cBleu', '#074B98', (7, 75, 152)),
    ('cVert', '#009E49', (0, 158, 73)),
    ('cSarcelle', '#00796B', (0, 121, 107)),
    ('cViolet', '#6B3FA0', (107, 63, 160)),
    ('cRouge', '#C80000', (200, 0, 0)),
    ('cTexte', '#1F2937', (31, 41, 55)),
    ('cTexte2', '#6B7280', (107, 114, 128)),
    ('cGrisLib', '#9CA3AF', (156, 163, 175)),
    ('cBordure', '#E5E7EB', (229, 231, 235)),
    ('cBleuPale', '#ECF1F7', (236, 241, 247)),
    ('cFond', '#F9FAFB', (249, 250, 251)),
]

# ---------------------------------------------------------------- Gravité (texte fourni)
GRAVITE_AIDE = {
    'Élevée': "Gravité ou gravité potentielle ÉLEVÉE (enquête obligatoire) : ex. le décès d'un employé; la perte totale ou partielle d'un membre ou de son usage; un traumatisme physique important; des blessures à plusieurs employés occasionnant une absence de 1 jour ouvrable, excluant la journée de l'accident; des dommages matériels de 150 000 $ et plus.",
    'Moyenne': "Gravité ou gravité potentielle MOYENNE (enquête obligatoire) : accident provoquant une absence qui dépasse la journée de l'évènement, électrisation ou incident qui aurait pu entraîner une blessure ou une maladie réversible. Si l'employé est en assignation temporaire.",
    'Faible': "Gravité ou gravité potentielle FAIBLE : accident sans aucune perte de temps (blessure mineure) ou incident qui aurait pu causer une blessure mineure.",
}
GRAVITES = [
    ('Accident gravité élevée', 'Élevée'), ('Accident gravité moyenne', 'Moyenne'), ('Accident gravité faible', 'Faible'),
    ('Incident à potentiel de gravité élevée', 'Élevée'), ('Incident à potentiel de gravité moyenne', 'Moyenne'),
    ('Incident à potentiel de gravité faible', 'Faible'),
]

MOTS_ERREUR = ["erreur humaine", "erreur de manipulation", "a oublié", "oubli de", "négligence", "négligé", "inattention",
               "distraction", "mauvaise manipulation", "n'a pas fait attention", "imprudence", "étourderie"]

# ---------------------------------------------------------------- Listes génériques (SST_Ref_Listes)
def listes_generiques():
    rows = []  # (Liste, Valeur, Ordre, Aide, Courriel)
    def add(liste, valeurs, aide=None):
        for i, v in enumerate(valeurs):
            a = aide(v) if aide else ''
            rows.append((liste, v, i + 1, a, ''))
    add('Service', SERVICES)
    add('Syndicat', SYNDICATS)
    add('ClasseSFMQ', CLASSES)
    add('Adresse', ADRESSES)
    add('Horaire', ['Jour', 'Soir', 'Nuit', 'Heures supplémentaires'])
    add('Transport', ['Aucun', 'Ambulance', 'Taxi', 'Autre'])
    add('Cote', ['Gauche', 'Droit', 'Non applicable'])
    for i, (g, niv) in enumerate(GRAVITES):
        rows.append(('Gravite', g, i + 1, GRAVITE_AIDE[niv], ''))
    for k in ['CauseAccident', 'Activite', 'NatureBlessure', 'PartieCorps', 'FacteurOrganisation',
              'FacteurEnvironnement', 'FacteurComportement', 'MesureCorrective', 'TypeViolence',
              'MesuresPrisesViolence']:
        add(k, LISTES_PDF[k])
    add('MotErreurHumaine', MOTS_ERREUR)
    add('StatutAction', ['À faire', 'En cours', 'Fait', 'Efficacité vérifiée'])
    add('Statut', ['Brouillon', 'Déposé', 'Pris en charge', 'Enquête en cours', 'Analyse en cours', "Plan d'action", 'Fermé'])
    # Configuration modifiable sans republier l'application (colonne Courriel)
    rows.append(('Config', 'CourrielSST', 1, "Boîte courriel de la Division SST qui reçoit une copie PDF de chaque dépôt", ''))
    rows.append(('Config', 'CourrielComiteBouclier', 2, "Courriel du Comité bouclier (copie quand le gestionnaire sollicite son aide)", ''))
    return rows

# ---------------------------------------------------------------- Colonnes SharePoint
# Types : T = texte 1 ligne, M = plusieurs lignes, D = date, N = nombre, B = oui/non
DOSSIER_COLS = [
    ('TypeFormulaire', 'T', 'Accident, Incident, Situation dangereuse ou Violence'),
    ('Statut', 'T', 'Brouillon, Déposé, Pris en charge, Enquête en cours, Analyse en cours, Plan d\'action, Fermé'),
    ('Gravite', 'T', 'Niveau de gravité / gravité potentielle'),
    ('CreeParCourriel', 'T', 'Courriel (minuscules) de la personne qui a créé le dossier'),
    ('CreeParNom', 'T', ''),
    ('DateDeclaration', 'D', 'Étape 1 - dépôt'), ('DateMesures', 'D', 'Étape 2 - mesures immédiates'),
    ('DateApprobation', 'D', 'Étape 3 - approbation de l\'employé'), ('DateEnquete', 'D', 'Étape 4 - enquête / prise en charge'),
    ('DateAnalyse', 'D', 'Étape 5 - analyse 5 Pourquoi'), ('DatePlanAction', 'D', 'Étape 6 - plan d\'action'),
    ('DateFermeture', 'D', 'Étape 7 - fermeture'),
    ('EmpNom', 'T', ''), ('EmpPrenom', 'T', ''), ('EmpID', 'T', 'ID à 6 chiffres'), ('EmpCourriel', 'T', ''),
    ('EmpService', 'T', ''), ('EmpDirection', 'T', ''), ('EmpDivision', 'T', ''), ('EmpSection', 'T', ''),
    ('EmpSyndicat', 'T', ''), ('EmpClasse', 'T', ''), ('EmpTitre', 'T', ''), ('EmpTitreAutre', 'T', ''),
    ('EmpAdresseEtab', 'T', ''), ('EmpAdresseAutre', 'T', ''), ('EmpSuperieur', 'T', ''),
    ('GestNom', 'T', ''), ('GestTitre', 'T', ''), ('RempliSeul', 'T', ''),
    ('TrousseRemise', 'T', ''), ('TrousseRaison', 'M', ''), ('AbsenceAuDela', 'T', ''),
    ('EvtDate', 'D', ''), ('EvtHeure', 'T', ''), ('EvtDateDeclEmp', 'D', ''), ('EvtAdresse', 'T', ''),
    ('Horaire', 'T', ''), ('Temoins', 'T', ''), ('TemoinsNoms', 'M', ''), ('TemoinsCoord', 'M', ''),
    ('Vehicule', 'T', ''), ('VehiculeDesc', 'T', ''), ('Tache', 'M', ''), ('Description', 'M', ''),
    ('PSDonnes', 'T', ''), ('PSHeure', 'T', ''), ('PSNature', 'M', ''), ('PSSecouriste', 'T', ''),
    ('Transport', 'T', ''), ('TransportAutre', 'T', ''),
    ('CauseType', 'T', ''), ('Activite', 'T', ''),
    ('MesurePrev', 'M', ''), ('MesureResp', 'T', ''), ('MesureCollab', 'M', ''), ('MesureEcheance', 'D', ''),
    ('EnqueteRequise', 'T', ''),
    ('B1Zone', 'T', ''), ('B1Nature', 'T', ''), ('B1Partie', 'T', ''), ('B1Cote', 'T', ''), ('B1Precision', 'T', ''),
    ('B2Zone', 'T', ''), ('B2Nature', 'T', ''), ('B2Partie', 'T', ''), ('B2Cote', 'T', ''), ('B2Precision', 'T', ''),
    ('ArretTravail', 'T', ''), ('DateDernierJour', 'D', ''), ('RetourTravail', 'T', ''), ('DateRetour', 'D', ''),
    ('ModaliteRetour', 'T', ''),
    ('ApprobationEmp', 'T', ''), ('FormatCopie', 'T', ''),
    ('FactOrganisation', 'M', ''), ('FactOrgAutre', 'T', ''), ('FactEnvironnement', 'M', ''), ('FactEnvAutre', 'T', ''),
    ('FactComportement', 'M', ''), ('FactCompAutre', 'T', ''), ('MesuresSuggerees', 'M', ''), ('MesuresSuggAutre', 'T', ''),
    ('GestAccord', 'T', ''), ('GestVersion', 'M', ''), ('EnqueteurNom', 'T', ''),
    ('Probleme', 'M', ''), ('AnalysteNom', 'T', ''),
    ('DiscuteGest', 'T', ''), ('SyndicatCopie', 'T', ''),
    ('DeclarantRole', 'T', ''), ('ViolTypes', 'M', ''), ('AuteurNom', 'T', ''), ('AuteurAdresse', 'T', ''),
    ('AuteurInfo', 'M', ''), ('Recidive', 'T', ''), ('RecidiveDetails', 'M', ''), ('ViolMesuresPrises', 'M', ''),
    ('ViolMesuresPar', 'T', ''), ('ComiteBouclier', 'T', ''),
    ('NotesSST', 'M', 'Notes de suivi du conseiller SST'), ('PdfLien', 'M', 'Lien du dernier PDF généré'),
]
POURQUOI_COLS = [('DossierID', 'N', 'ID du dossier (SST_Dossiers)'), ('Chemin', 'T', 'ex. 001.002'),
                 ('Niveau', 'N', ''), ('Texte', 'M', ''), ('CauseRacine', 'B', ''), ('ActionTexte', 'M', ''),
                 ('ActionResp', 'T', ''), ('ActionEcheance', 'D', ''), ('ActionStatut', 'T', '')]
LISTES = [
    ('SST_Dossiers', 'Dossiers SST : accidents, incidents, situations dangereuses, violence', DOSSIER_COLS,
     ['TypeFormulaire', 'Statut', 'EmpNom', 'EmpPrenom', 'EvtDate', 'CreeParCourriel'], ['CreeParCourriel', 'Statut', 'TypeFormulaire']),
    ('SST_Pourquoi', 'Nœuds des analyses 5 Pourquoi', POURQUOI_COLS, ['DossierID', 'Chemin', 'Texte', 'CauseRacine'], ['DossierID']),
    ('SST_Ref_Listes', 'Listes de choix (Title = nom de la liste)', [('Valeur', 'T', ''), ('Ordre', 'N', ''), ('Aide', 'M', ''), ('Courriel', 'T', '')],
     ['Valeur', 'Ordre', 'Courriel'], []),
    ('SST_Ref_Org', 'Organigramme (Title = service)', [('Niveau', 'T', 'Direction, Division ou Section'), ('Valeur', 'T', ''), ('Ordre', 'N', '')],
     ['Niveau', 'Valeur', 'Ordre'], []),
    ('SST_Ref_Titres', "Titres d'emploi (Title = syndicat)", [('Classe', 'T', 'Classe SFMQ seulement'), ('Valeur', 'T', ''), ('Ordre', 'N', '')],
     ['Classe', 'Valeur', 'Ordre'], []),
    ('SST_Roles', 'Conseillers SST (Title = courriel en minuscules)', [('Role', 'T', ''), ('Nom', 'T', '')], ['Role', 'Nom'], []),
]
