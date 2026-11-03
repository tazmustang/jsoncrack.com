# Application SST — Guide d'installation et d'utilisation

Déclarations d'accident et d'incident (avec enquête et analyse 5 Pourquoi), signalements de situation dangereuse et déclarations d'évènement traumatisant ou d'acte de violence, réunis dans une seule application Power Apps aux couleurs de l'application « Appréciation de la contribution ».

## 1. Ce que contient le dossier

| Dossier / fichier | Rôle |
|---|---|
| 1_SharePoint/Installer_SharePoint.js | Script à coller dans la console du navigateur : crée les 6 listes, la bibliothèque SST_PDF, les 123 colonnes et charge les 945 valeurs de référence (services, divisions, sections, syndicats, titres d'emploi, adresses, causes, blessures, facteurs d'enquête, etc.). |
| 2_PowerAutomate/Flux_SSTGenererPDF.md | Fiche détaillée du flux qui produit et envoie le PDF (aussi décrite à la section 3). |
| 3_PowerApps/App_Formulas_FR.txt | Formules nommées (couleurs, courriels, zones du schéma corporel) à coller dans la propriété Formulas de l'objet App. |
| 3_PowerApps/App_OnStart_FR.txt | Formule à coller dans la propriété OnStart de l'objet App. |
| 3_PowerApps/App_*_EN.txt | Mêmes formules avec les séparateurs anglais ( , et ; ) si votre Power Apps est en anglais. |
| 3_PowerApps/Ecrans/01 à 09 *.pa.yaml | Les 9 écrans, à coller un par un dans Power Apps Studio (clic droit > Coller le code). |
| outils/ | Générateur Python (facultatif) : modifiez les textes ou les listes puis lancez  python3 generer.py  pour régénérer tous les fichiers. python3 verifier.py contrôle les formules. |

### Architecture (100 % Microsoft 365, sans licence Premium)

- Données : listes SharePoint (SST_Dossiers, SST_Pourquoi, SST_Ref_Listes, SST_Ref_Org, SST_Ref_Titres, SST_Roles) et bibliothèque SST_PDF.
- Application : Power Apps canevas (connecteur SharePoint standard).
- PDF et courriels : un flux Power Automate (OneDrive Entreprise, SharePoint, Outlook — connecteurs standard).

### Écrans de l'application

| Écran | Contenu |
|---|---|
| scrAccueil | Bandeau or, choix du rôle (« VOUS ÊTES : » Gestionnaire / Employé / Conseiller SST), cartes des 3 formulaires, rappel 911. |
| scrDossiers | 📂 Mes dossiers : filtres type / statut / nom, progression des étapes. Le conseiller SST voit tous les dossiers. |
| scrAccident | Déclaration d'accident ou d'incident en 6 onglets : identification (gravité incluse), évènement, premiers soins, blessures (schéma du corps cliquable face/dos), cause et mesures préventives, arrêt et approbation. |
| scrEnquete | Enquête : 3 axes (organisation, environnement, comportement) en cases à cocher, mesures correctives suggérées, version du gestionnaire. |
| scrAnalyse | Arbre des 5 Pourquoi (branches illimitées, détection du piège « erreur humaine »), causes racines, plan d'action (responsable, échéance, statut) et test du « Donc ». |
| scrSituation | Signalement d'une situation dangereuse (ouvert à tous les employés). |
| scrViolence | Évènement traumatisant et acte de violence, avec le Comité bouclier. |
| scrApercu | 🖨️ Aperçu du dossier (identique au PDF), barre des étapes, génération/envoi du PDF, suivi et fermeture par le conseiller SST. |
| scrAide | ❓ Comment remplir (une page par formulaire) et ℹ️ À propos. |

## 2. Installer les listes SharePoint (10 minutes)

1. Créer (ou choisir) un site SharePoint d'équipe pour la SST, dont vous êtes propriétaire. Ex. : https://<votre-tenant>.sharepoint.com/sites/SST
2. Ouvrir la page d'accueil du site dans Edge ou Chrome.
3. Appuyer sur F12 (outils de développement) > onglet « Console ». La première fois, Edge/Chrome demande de taper  allow pasting  puis Entrée.
4. Ouvrir 1_SharePoint/Installer_SharePoint.js dans le Bloc-notes, tout sélectionner (Ctrl+A), copier, coller dans la console, Entrée.
5. Attendre le message vert « INSTALLATION TERMINÉE » (1 à 3 minutes). En cas d'erreur rouge, relancez simplement le script : il saute ce qui existe déjà.
6. Le script vous ajoute automatiquement comme « Conseiller SST » dans la liste SST_Roles.

### Configuration après l'installation

- Liste SST_Ref_Listes, filtrer Title = Config : inscrire dans la colonne Courriel la boîte de la Division SST (ligne CourrielSST) et celle du Comité bouclier (ligne CourrielComiteBouclier). Ces adresses reçoivent les PDF; elles se changent sans republier l'application.
- Même liste, Title = Syndicat : inscrire au besoin le courriel de chaque syndicat (copie des signalements de situation dangereuse quand l'employé le demande).
- Liste SST_Roles : ajouter une ligne par conseiller SST (Title = courriel en minuscules, Role = Conseiller SST).
- Les listes de choix (services, divisions, titres d'emploi, adresses, causes...) se mettent à jour directement dans SST_Ref_Listes, SST_Ref_Org et SST_Ref_Titres (colonne Ordre = ordre d'affichage). Les changements apparaissent au prochain lancement de l'application.

### Permissions recommandées

- Tous les utilisateurs de l'application : « Collaboration » sur SST_Dossiers et SST_Pourquoi, « Lecture » sur les listes SST_Ref_* et SST_Roles.
- Confidentialité (renseignements de santé) : dans SST_Dossiers > Paramètres > Paramètres avancés, choisir « Accès en lecture : éléments créés par l'utilisateur » et « Accès en modification : éléments créés par l'utilisateur ». Les conseillers SST doivent alors être propriétaires du site (ou avoir le niveau « Contrôle total ») pour voir tous les dossiers. Faites la même chose pour SST_Pourquoi.
- Bibliothèque SST_PDF : accès réservé à la Division SST et au compte propriétaire du flux.

## 3. Créer le flux Power Automate (15 minutes)

Ce flux reçoit le HTML du dossier depuis Power Apps, le convertit en PDF, le range dans la bibliothèque SST_PDF, l'envoie par courriel et renvoie le lien à l'application. Il n'utilise que des connecteurs standard inclus dans Microsoft 365 (OneDrive Entreprise, SharePoint, Office 365 Outlook) : aucune licence Premium.

1. Ouvrir https://make.powerautomate.com > « + Créer » > « Flux de cloud instantané ». Nom : SSTGenererPDF (exactement, sans espace). Déclencheur : « Power Apps (V2) » (en anglais : « When Power Apps calls a flow (V2) »). Créer.
2. Dans le déclencheur, ajouter 5 entrées de type Texte, DANS CET ORDRE : NomFichier, ContenuHTML, Destinataires, Objet, Corps. Pour Destinataires, Objet et Corps : « ... » > « Rendre le champ facultatif ».
3. + Nouvelle étape > OneDrive Entreprise > « Créer un fichier ». Chemin du dossier : /SST_temp (créez le dossier au besoin). Nom du fichier : NomFichier (contenu dynamique) suivi de .html. Contenu du fichier : ContenuHTML.
4. + Nouvelle étape > OneDrive Entreprise > « Convertir un fichier » (Convert file). Fichier : Id (de l'étape « Créer un fichier »). Type cible : PDF.
5. + Nouvelle étape > SharePoint > « Créer un fichier ». Adresse du site : votre site SST. Chemin du dossier : /SST_PDF. Nom du fichier : NomFichier suivi de .pdf. Contenu du fichier : Contenu du fichier (de « Convertir un fichier »).
6. + Nouvelle étape > Contrôle > « Condition » : Destinataires « n'est pas égal à » (laisser vide). Dans « Si oui » : Office 365 Outlook > « Envoyer un e-mail (V2) ». À : Destinataires. Objet : Objet. Corps : Corps. Paramètres avancés > Pièces jointes : Nom = NomFichier suivi de .pdf, Contenu = Contenu du fichier (de « Convertir un fichier »).
7. Après la condition (au même niveau) : OneDrive Entreprise > « Supprimer un fichier ». Fichier : Id (de « Créer un fichier »). (Nettoie le fichier HTML temporaire.)
8. + Nouvelle étape > Power Apps > « Répondre à une application ou à un flux PowerApp » (Respond to a PowerApp or flow). Ajouter une sortie Texte nommée lienpdf (en minuscules) avec la valeur : Lien vers l'élément (Link to item) de l'étape SharePoint « Créer un fichier » (ou Chemin si le lien n'est pas proposé).
9. Enregistrer. Tester avec « Test > Manuellement » est facultatif : le vrai test se fait depuis l'application.

Le flux tourne sous le compte de son propriétaire : le PDF est donc envoyé depuis la boîte de ce compte. Idéalement, utilisez un compte de service ou la boîte de la Division SST comme propriétaire. Si la limite quotidienne de courriels de votre compte pose problème, ajoutez un copropriétaire et changez la connexion Outlook.

## 4. Créer l'application Power Apps (30 minutes)

1. https://make.powerapps.com > « + Créer » > « Application vide » > « Application canevas vide ». Nom : SST - Déclarations et enquêtes. Format : Tablette. Créer.
2. Paramètres (engrenage) > Général : « Limite de lignes de données » = 2000. Vérifier que les « Formules nommées » sont actives (Paramètres > Mises à jour > Nouveau, si l'option apparaît).
3. Volet Données (icône cylindre) > « Ajouter des données » > SharePoint > votre site > cocher les 6 listes : SST_Dossiers, SST_Pourquoi, SST_Ref_Listes, SST_Ref_Org, SST_Ref_Titres, SST_Roles.
4. Volet Power Automate (icône …/flux) > « Ajouter un flux » > SSTGenererPDF.
5. Arborescence > sélectionner « App ». Dans la liste des propriétés, choisir Formulas et coller tout le contenu de App_Formulas_FR.txt. Choisir OnStart et coller App_OnStart_FR.txt. (Si votre Studio est en anglais, utilisez les fichiers _EN.)
6. Coller les écrans, dans l'ordre 01 à 09 : ouvrir le fichier .pa.yaml dans le Bloc-notes, Ctrl+A, Ctrl+C; dans Power Apps Studio, clic droit dans l'arborescence (sur un écran existant ou dans la zone vide) > « Coller le code » (Paste code). L'écran apparaît avec tous ses contrôles.
7. Supprimer l'écran vide Screen1 et glisser scrAccueil en premier (ou App > StartScreen = scrAccueil).
8. App > « Exécuter OnStart » (clic droit sur App). Les erreurs restantes disparaissent normalement une fois les données chargées.
9. Bandeau de marque « ON DONNE VIE À LA VILLE » (facultatif) : Média > Charger l'image utilisée dans Appréciation, puis sélectionner le contrôle acc0_imgMarque de scrAccueil et mettre sa propriété Image = le nom de l'image (sans guillemets).
10. Fichier > Enregistrer, puis Publier. Partager l'application (Partager) avec les gestionnaires, employés et conseillers SST; le partage avec un groupe Microsoft 365 est le plus simple.

### Format des formules collées

Les fichiers .pa.yaml utilisent le format standard du code Power Apps (séparateurs anglais , et ;). Power Apps Studio les convertit automatiquement à l'affichage en français ( ; et ;; ). Seules les formules collées directement dans la barre de formule (Formulas et OnStart) doivent correspondre à la langue de votre Studio : d'où les deux versions FR et EN.

## 5. Utilisation

### Gestionnaire — déclarer un accident ou un incident

1. Accueil > « VOUS ÊTES : Gestionnaire » > carte « Accident ou incident de travail » > Commencer.
2. Onglet 1 : choisir Accident ou Incident, puis le niveau de gravité (les définitions s'affichent sous la liste). Gravité élevée ou moyenne = enquête obligatoire (cochée automatiquement à l'onglet 5).
3. Remplir les onglets 2 à 6 avec l'employé. Onglet 4 (accident seulement) : cliquer une zone du corps pour la blessure principale (rouge), puis une autre pour la blessure secondaire (or). La partie du corps et le côté se remplissent automatiquement.
4. ☁️ Enregistrer = brouillon (à reprendre plus tard dans 📂 Mes dossiers). ☁️ Enregistrer et déposer = validation des champs obligatoires (*), dépôt, puis production automatique du PDF envoyé à la Division SST et à l'employé (si copie courriel).
5. Depuis l'aperçu du dossier : 🔍 Enquête, puis 🌳 Analyse 5 Pourquoi. La barre d'étapes passe au vert au fur et à mesure, avec la date.

### Les 7 étapes d'un accident ou d'un incident

| Étape | Passe au vert quand... |
|---|---|
| 1. Déclaration | le formulaire est déposé |
| 2. Mesures immédiates | la mesure préventive immédiate est inscrite |
| 3. Approbation employé | l'employé a approuvé sa version (Oui) |
| 4. Enquête | les 3 axes, les mesures suggérées et la version du gestionnaire sont remplis |
| 5. Analyse 5 Pourquoi | au moins une cause racine est marquée et l'analyse est enregistrée |
| 6. Plan d'action | chaque cause racine a une action, un responsable et une échéance |
| 7. Fermeture | le conseiller SST met le statut « Fermé » |

Situation dangereuse : 4 étapes (signalement, prise en charge, mesure corrective, fermeture). Violence : 5 étapes (déclaration, mesures immédiates, approbation, suivi SST / Comité bouclier, fermeture). Les étapes de suivi sont mises à jour par le conseiller SST dans l'aperçu du dossier (statut + notes).

### Employé

Rôle « Employé » : seule la carte « Situation dangereuse » est offerte. L'employé voit ses propres signalements dans 📂 Mes dossiers.

### Conseiller SST

- Le rôle apparaît seulement pour les personnes inscrites dans SST_Roles.
- 📂 Mes dossiers affiche tous les dossiers, filtrables par type, statut et nom.
- Dans l'aperçu : statut, notes de suivi, fermeture; 📄 Générer le PDF et envoyer pour renvoyer une copie à jour (par exemple après l'analyse).

## 6. Palette et accessibilité

| Nom dans l'app | Couleur | Power Apps |
|---|---|---|
| cOr | #857650 | RGBA(133; 118; 80; 1) |
| cMarine | #00285E | RGBA(0; 40; 94; 1) |
| cBleu | #074B98 | RGBA(7; 75; 152; 1) |
| cVert | #009E49 | RGBA(0; 158; 73; 1) |
| cSarcelle | #00796B | RGBA(0; 121; 107; 1) |
| cViolet | #6B3FA0 | RGBA(107; 63; 160; 1) |
| cRouge | #C80000 | RGBA(200; 0; 0; 1) |
| cTexte | #1F2937 | RGBA(31; 41; 55; 1) |
| cTexte2 | #6B7280 | RGBA(107; 114; 128; 1) |
| cGrisLib | #9CA3AF | RGBA(156; 163; 175; 1) |
| cBordure | #E5E7EB | RGBA(229; 231; 235; 1) |
| cBleuPale | #ECF1F7 | RGBA(236; 241; 247; 1) |
| cFond | #F9FAFB | RGBA(249; 250; 251; 1) |

- Pour changer une couleur : App > Formulas, modifier la ligne correspondante; tout l'écran suit.
- Vert action (#009E49) avec texte blanc = 3,51 : 1, sous le seuil WCAG pour le texte normal; les boutons sont en semi-gras. Pour être conforme, remplacer cVert par RGBA(0; 122; 56; 1) (#007A38).
- Les libellés gris de l'application utilisent #6B7280 (conforme); #9CA3AF n'est utilisé que pour les cercles des étapes à venir (élément non textuel).
- Police : Open Sans (défaut Power Apps). PDF : Segoe UI puis Arial, titre 18 pt marine, sections 12,5 pt marine avec filet or, tableaux 9,5 pt.

## 7. Dépannage

| Problème | Solution |
|---|---|
| « Coller le code » refuse un contrôle (version inconnue) | Votre Studio utilise une autre version de ce contrôle. Insérez le contrôle équivalent manuellement, donnez-lui le même nom et recopiez ses propriétés depuis le fichier .pa.yaml (chaque propriété y est lisible). |
| Erreurs rouges juste après le collage | Normal tant que les sources de données, le flux et les formules App ne sont pas ajoutés. Faire « Exécuter OnStart », puis enregistrer et rouvrir l'application. |
| Listes déroulantes vides | Vérifier que le script SharePoint a chargé les données et que la limite de lignes est à 2000; relancer OnStart. |
| « Le PDF n'a pas pu être généré » | Vérifier que le flux s'appelle exactement SSTGenererPDF, que ses 5 entrées sont dans l'ordre et que la sortie s'appelle lienpdf. Consulter l'historique d'exécution du flux. |
| Aucun courriel reçu | Remplir CourrielSST dans SST_Ref_Listes (Title = Config). Le panneau d'actions de l'aperçu affiche les destinataires prévus. |
| Avertissements de délégation (triangle jaune) | Sans conséquence sous 2 000 dossiers par filtre. Les colonnes filtrées sont indexées par le script. |
| Application lente à l'ouverture | Normal au premier lancement (chargement des listes). L'application compte environ 680 contrôles; si besoin, retirer l'écran Violence ou Situation dans une seconde application. |

## 8. Modifier l'application plus tard

- Petits changements (texte, couleur, champ masqué) : directement dans Power Apps Studio.
- Changements de listes de choix : directement dans les listes SharePoint SST_Ref_*.
- Ajout d'un champ : ajouter la colonne à SST_Dossiers (nom sans accent ni espace), puis un contrôle dans l'écran et la colonne dans la formule Patch du bouton « Enregistrer et déposer » (contrôle *_btnDeposerBas) et du bouton « Enregistrer ».
- Grosse refonte : modifier les fichiers du dossier outils/ et relancer python3 generer.py, puis recoller les écrans modifiés.

© Ville de Québec — Formulaires propriété de la Division de la santé et de la sécurité au travail.
