# Flux « SSTGenererPDF » — étape par étape

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
