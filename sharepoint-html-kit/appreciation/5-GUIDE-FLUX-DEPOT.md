# Guide — Flux « AC - Traiter un dépôt » (version pilote)

Pour tester tout le cheminement de l'appréciation dans le site de test. Mis à jour le 21 octobre 2026. Durée : environ une demi-journée de construction, puis 1 heure de test.

Connecteurs utilisés : **SharePoint**, **Office 365 Outlook** et **Office 365 Utilisateurs**. Ils sont tous **standard** : aucune licence Premium.

> ⚠️ Je ne peux pas exécuter Power Automate de mon côté. Les expressions ci-dessous suivent la structure exacte des fichiers de l'application v3.8, mais il faudra peut-être ajuster une étape au premier essai. Envoyez-moi une capture de l'**historique d'exécution** si une étape devient rouge.

---

## 0. Ce que fait le flux

À chaque nouvel élément dans **Depot_Appreciations**, le flux :

1. lit le dépôt : le champ **Contenu**, ou sinon le fichier joint ;
2. identifie le déposant à partir de son compte de la Ville (champ « Créé par », impossible à falsifier) ;
3. traite le cas selon que le dossier existe ou non :
   - **premier dépôt** : il crée le dossier `<dossierId>.json` dans **Dossiers_Appreciations** et trouve les supérieurs dans l'annuaire ;
   - **dossier existant** : il trouve le rôle du déposant, ne recopie que les sections que ce rôle peut modifier, puis traite l'action (sauvegarder, aviser, certifier, approuver) ;
4. envoie un courriel de confirmation ou de refus, avise la personne suivante, puis supprime l'élément de dépôt.

**Mode test.** Avec la variable `modeTest` à **true**, tous les participants reçoivent **votre** adresse, et le rôle est celui choisi dans l'application. Vous pouvez ainsi jouer les 4 rôles seule, sans déranger personne. Pour le pilote avec de vraies personnes, mettez `modeTest` à **false**.

**Pas encore dans cette version pilote :**
- permissions par dossier ;
- approbation finale par tous et PDF archivé ;
- journal des dépôts ;
- nettoyage automatique.

C'est la phase 2, avant le déploiement réel (section 9). D'ici là, **utilisez seulement des données fictives**.

## 1. Avant de commencer

- La liste **Depot_Appreciations** existe, avec la colonne **Contenu** (texte brut). ✅
- La bibliothèque **Dossiers_Appreciations** existe, avec ses colonnes : DossierId, NomPersonne, TypePoste, Statut, EtapeEnCours, DerniereMaj (guide d'installation, section 3).
- Règles de construction :
  - **Renommez chaque action exactement** comme indiqué : clic sur **…** de l'action › **Renommer**. Les expressions en dépendent.
  - Collez les expressions dans l'onglet **Expression (fx)**, jamais comme simple texte.
  - Les guillemets sont des apostrophes droites `'`.

## 2. Créer le flux et son déclencheur

1. Ouvrez **Power Automate** › **+ Créer** › **Flux de cloud automatisé**.
2. Nom : `AC - Traiter un dépôt`. Déclencheur : **SharePoint — Lorsqu'un élément est créé**.
3. Adresse du site : **SandBox Annie Audet**. Nom de la liste : **Depot_Appreciations**.
4. Dans le déclencheur, ouvrez **… › Paramètres** : activez **Contrôle de la simultanéité**, avec un **degré de parallélisme de 1**. Les dépôts sont ainsi traités un à la fois.

## 3. Les variables (8 actions « Initialiser une variable »)

| Nom | Type | Valeur |
|---|---|---|
| `modeTest` | Booléen | `true` |
| `deposant` | Chaîne | expression : `toLower(triggerBody()?['Author']?['Email'])` |
| `nomDeposant` | Chaîne | expression : `triggerBody()?['Author']?['DisplayName']` |
| `maintenant` | Chaîne | expression : `formatDateTime(convertFromUtc(utcNow(),'Eastern Standard Time'),'yyyy-MM-dd HH:mm')` |
| `texteDepot` | Chaîne | (vide) |
| `dossier` | Objet | (vide) |
| `motifRefus` | Chaîne | (vide) |
| `message` | Chaîne | (vide) |

## 4. Étendue « Traitement » : lire le dépôt

Ajoutez une action **Étendue** et renommez-la `Traitement`. Toutes les actions des sections 4 à 7 vont **dedans**.

**4.1 — Les pièces jointes.** Action SharePoint **Obtenir les pièces jointes**, renommée `PJ`. Site et liste : comme le déclencheur. Id : **ID** du déclencheur.

**4.2 — Condition `ContenuVide`.** Expression `empty(coalesce(triggerBody()?['Contenu'],''))`, **est égal à** `true`.
- **Si oui** (dépôt par fichier joint) :
  - action SharePoint **Obtenir le contenu de la pièce jointe**, renommée `ContenuPJ` ; Id de l'élément : **ID** ; Identificateur du fichier : `first(body('PJ'))?['Id']` ;
  - **Définir une variable** `texteDepot` = `base64ToString(body('ContenuPJ')?['$content'])`.
- **Si non** (dépôt par copier-coller) : **Définir une variable** `texteDepot` = `triggerBody()?['Contenu']`.

> Si l'étape `ContenuPJ` produit une erreur « json » au test, remplacez l'expression par `string(body('ContenuPJ'))`.

**4.3 — Composer, renommé `Depot`.** Expression : `json(variables('texteDepot'))`

**4.4 — Condition `DepotValide`.** Expression :
`and(equals(outputs('Depot')?['format'],'appreciation-depot-v1'), not(empty(outputs('Depot')?['dossierId'])))`, **est égal à** `true`.
- **Si non** : **Définir une variable** `motifRefus` = `Le contenu collé n'est pas un dépôt de l'application. Recommencez avec le bouton « Copier le contenu du dépôt ».`
- **Si oui** : toutes les étapes suivantes (4.5 à 7) vont **dans cette branche**.

**4.5 — Chercher le dossier.** Action SharePoint **Obtenir les fichiers (propriétés uniquement)**, renommée `ChercherDossier`. Bibliothèque : **Dossiers_Appreciations**. Requête de filtre : `DossierId eq '` puis le contenu dynamique `@{outputs('Depot')?['dossierId']}`, puis `'`. Nombre maximal : `1`.

**4.6 — Condition `NouveauDossier`.** Expression `length(body('ChercherDossier')?['value'])`, **est égal à** `0`.

## 5. Branche « Oui » de `NouveauDossier` : premier dépôt

**5.1 — Condition `ActionPermiseNouveau`.** Expression `contains(createArray('sauvegarder','aviser'), outputs('Depot')?['action'])`, **est égal à** `true`.
- **Si non** : `motifRefus` = `Ce dossier n'existe pas encore. Commencez par « Déposer sur SharePoint ».`
- **Si oui** : les étapes 5.2 à 5.8.

**5.2 — Supérieurs dans l'annuaire.** Deux actions Office 365 Utilisateurs **Obtenir le responsable (V2)** :
- `ResponsableSI` : Utilisateur = `variables('deposant')` ;
- `ResponsableSH` : Utilisateur = `body('ResponsableSI')?['userPrincipalName']`.

**5.3 — Composer `Participants`.** Expression, sur une seule ligne :
```
setProperty(setProperty(setProperty(json('{}'),'personne',setProperty(setProperty(json('{}'),'nom',variables('nomDeposant')),'email',variables('deposant'))),'superieur_immediat',setProperty(setProperty(json('{}'),'nom',body('ResponsableSI')?['displayName']),'email',if(variables('modeTest'),variables('deposant'),toLower(body('ResponsableSI')?['mail'])))),'superieur_hierarchique',setProperty(setProperty(json('{}'),'nom',body('ResponsableSH')?['displayName']),'email',if(variables('modeTest'),variables('deposant'),toLower(body('ResponsableSH')?['mail']))))
```

> **Directeur ou directrice** : dans cette version pilote, si une approbation du directeur est cochée, son nom n'est pas tiré de l'annuaire. En mode test, c'est votre adresse qui est utilisée (étape 6.1). Ce sera complété à la phase 2.

**5.4 — Composer `NouveauWorkflow`.** Expression :
```
setProperty(setProperty(setProperty(setProperty(setProperty(setProperty(setProperty(setProperty(json('{}'),'dossierId',outputs('Depot')?['dossierId']),'status','brouillon'),'participants',outputs('Participants')),'certification',json('{"signed":false,"nom":"","email":"","date":""}')),'approbations',json('{"superieur_immediat":{"signed":false,"nom":"","email":"","date":""},"superieur_hierarchique":{"signed":false,"nom":"","email":"","date":""},"directeur":{"signed":false,"nom":"","email":"","date":""}}')),'avisSuperieur',setProperty(json('{}'),'date',if(equals(outputs('Depot')?['action'],'aviser'),variables('maintenant'),''))),'version',1),'derniereMaj',variables('maintenant'))
```

**5.5 — Définir une variable `dossier`.** Expression : elle reprend le formulaire, mais vide les sections du supérieur que la personne aurait pu remplir.
```
setProperty(setProperty(setProperty(setProperty(outputs('Depot')?['formulaire'],'leadershipSup',json('{}')),'bilanSuperieur',''),'evaluationGlobale',''),'workflow',outputs('NouveauWorkflow'))
```

**5.6 — Créer le fichier.** Action SharePoint **Créer un fichier**, renommée `CreerDossier` :
- Chemin du dossier : `/Dossiers_Appreciations` ;
- Nom du fichier : `concat(outputs('Depot')?['dossierId'],'.json')` ;
- Contenu du fichier : `string(variables('dossier'))`.

**5.7 — Propriétés.** Action SharePoint **Mettre à jour les propriétés du fichier**, renommée `ProprietesNouveau`. Bibliothèque : Dossiers_Appreciations. Id : `body('CreerDossier')?['ItemId']`.
- DossierId : `outputs('Depot')?['dossierId']`
- NomPersonne : `variables('dossier')?['identification']?['nom']`
- TypePoste : `variables('dossier')?['identification']?['typePoste']`
- Statut : **Brouillon**
- EtapeEnCours : `Brouillon`
- DerniereMaj : `utcNow()`

**5.8 — Message.** **Définir une variable** `message` = `Votre dossier a été créé dans « Mes dossiers ».`
Si l'action est **aviser**, ajoutez une condition `equals(outputs('Depot')?['action'],'aviser')`. Dans sa branche Oui, ajoutez **Envoyer un courriel (V2)** (Office 365 Outlook) :
- À : `outputs('Participants')?['superieur_immediat']?['email']` ;
- modèle « Avis au supérieur » de la section 8.

## 6. Branche « Non » de `NouveauDossier` : dossier existant

**6.1 — Lire le dossier.** Action SharePoint **Obtenir le contenu du fichier**, renommée `LireDossier`. Identificateur du fichier : `first(body('ChercherDossier')?['value'])?['{Identifier}']`.
Ensuite, **Définir une variable** `dossier` = `json(base64ToString(body('LireDossier')?['$content']))`.
> Si cette étape échoue, essayez plutôt `json(string(body('LireDossier')))`.

**6.2 — Composer `Role`.** Le rôle est trouvé en comparant votre adresse à celles du dossier. En mode test, c'est le rôle choisi dans l'application qui compte.
```
if(variables('modeTest'), outputs('Depot')?['roleDeclare'], if(equals(variables('deposant'),toLower(coalesce(variables('dossier')?['workflow']?['participants']?['personne']?['email'],''))),'personne', if(equals(variables('deposant'),toLower(coalesce(variables('dossier')?['workflow']?['participants']?['superieur_immediat']?['email'],''))),'superieur_immediat', if(equals(variables('deposant'),toLower(coalesce(variables('dossier')?['workflow']?['participants']?['superieur_hierarchique']?['email'],''))),'superieur_hierarchique', if(equals(variables('deposant'),toLower(coalesce(variables('dossier')?['workflow']?['participants']?['directeur']?['email'],''))),'directeur','')))))
```

**6.3 — Composer `Statut`.** `variables('dossier')?['workflow']?['status']`

**6.4 — Composer `Etape`** (la personne qui doit approuver maintenant) :
```
if(not(equals(outputs('Statut'),'approbation')),'', if(not(variables('dossier')?['workflow']?['approbations']?['superieur_immediat']?['signed']),'superieur_immediat', if(not(variables('dossier')?['workflow']?['approbations']?['superieur_hierarchique']?['signed']),'superieur_hierarchique', if(and(equals(variables('dossier')?['options']?['directeurApplicable'],true), not(variables('dossier')?['workflow']?['approbations']?['directeur']?['signed'])),'directeur',''))))
```

**6.5 — Condition `RoleConnu`.** `empty(outputs('Role'))`, **est égal à** `true` :
- **Si oui** : `motifRefus` = `Vous n'avez aucun rôle dans ce dossier.`
- **Si non** : les étapes 6.6 à 6.9.

**6.6 — Composer `ClesPermises`** (les sections que ce rôle peut modifier à cette étape) :
```
if(and(equals(outputs('Role'),'personne'),equals(outputs('Statut'),'brouillon')), createArray('identification','options','objectifsActuels','objectifsAvenir','leadershipCommentaires','competences','valeurs','developpement','leadershipCadre','bilanCadre'), if(and(equals(outputs('Role'),'superieur_immediat'),equals(outputs('Statut'),'brouillon')), createArray('identification','options','objectifsActuels','objectifsAvenir','leadershipCommentaires','competences','valeurs','developpement','leadershipSup','bilanSuperieur','evaluationGlobale'), if(and(equals(outputs('Role'),'superieur_immediat'),equals(outputs('Statut'),'approbation'),not(variables('dossier')?['workflow']?['approbations']?['superieur_immediat']?['signed'])), createArray('leadershipSup','bilanSuperieur','evaluationGlobale'), createArray())))
```

**6.7 — Boucle `Fusionner`.** Action **Appliquer à chacun** sur `outputs('ClesPermises')`. Dans ses **Paramètres**, contrôle de la simultanéité **activé, degré 1**. Dedans :
- **Composer** `Fusion` : `setProperty(variables('dossier'), item(), outputs('Depot')?['formulaire']?[item()])`
- **Définir une variable** `dossier` = `outputs('Fusion')`

> Le bloc `workflow` (statut, noms, dates) n'est **jamais** recopié du dépôt : seul le flux l'écrit.

**6.8 — Commutateur `Action`** sur `outputs('Depot')?['action']`. Pour les cas qui modifient le dossier, faites toujours deux temps : un **Composer** qui calcule le nouveau dossier, puis **Définir une variable** `dossier` = la sortie de ce Composer.

| Cas | Contrôle (sinon `motifRefus`) | Nouveau dossier (Composer) | Courriel | `message` |
|---|---|---|---|---|
| `sauvegarder` | `greater(length(outputs('ClesPermises')),0)`, sinon « Rien à enregistrer pour votre rôle à cette étape. » | — | — | `Votre version a été enregistrée.` |
| `aviser` | `and(equals(outputs('Role'),'personne'),equals(outputs('Statut'),'brouillon'))`, sinon « Seule la personne en appréciation peut aviser, avant la certification. » | `setProperty(variables('dossier'),'workflow',setProperty(variables('dossier')?['workflow'],'avisSuperieur',setProperty(json('{}'),'date',variables('maintenant'))))` | « Avis au supérieur », au supérieur immédiat | `Votre supérieur(e) a été avisé(e).` |
| `certifier` | `and(equals(outputs('Role'),'personne'),equals(outputs('Statut'),'brouillon'),not(empty(variables('dossier')?['identification']?['typePoste'])))`, sinon « Certification impossible à cette étape. » | `setProperty(variables('dossier'),'workflow',setProperty(setProperty(variables('dossier')?['workflow'],'status','approbation'),'certification',json(concat('{"signed":true,"nom":"',replace(variables('nomDeposant'),'"',''),'","email":"',variables('deposant'),'","date":"',variables('maintenant'),'"}'))))` | « Approbation requise », au supérieur immédiat | `Votre certification est enregistrée. Le dossier est verrouillé.` |
| `approuver` | `equals(outputs('Role'),outputs('Etape'))`, sinon « Ce n'est pas votre étape d'approbation. » | voir 6.8 b | voir 6.8 b | `Votre approbation est enregistrée.` |

**6.8 b — Le cas `approuver`, en trois actions :**
1. Composer `AvecSignature` :
```
setProperty(variables('dossier'),'workflow',setProperty(variables('dossier')?['workflow'],'approbations',setProperty(variables('dossier')?['workflow']?['approbations'],outputs('Role'),json(concat('{"signed":true,"nom":"',replace(variables('nomDeposant'),'"',''),'","email":"',variables('deposant'),'","date":"',variables('maintenant'),'"}')))))
```
2. Composer `Suivant` :
```
if(equals(outputs('Role'),'superieur_immediat'),'superieur_hierarchique', if(and(equals(outputs('Role'),'superieur_hierarchique'),equals(variables('dossier')?['options']?['directeurApplicable'],true)),'directeur',''))
```
3. Définir la variable `dossier` :
```
if(empty(outputs('Suivant')), setProperty(outputs('AvecSignature'),'workflow',setProperty(outputs('AvecSignature')?['workflow'],'status','signature')), outputs('AvecSignature'))
```

Ensuite, une condition `empty(outputs('Suivant'))` :
- **Si non** : courriel « Approbation requise », envoyé à l'adresse suivante :
```
if(variables('modeTest'), variables('deposant'), coalesce(variables('dossier')?['workflow']?['participants']?[outputs('Suivant')]?['email'], variables('deposant')))
```
- **Si oui** : courriel « Toutes les approbations sont obtenues », à la personne en appréciation et au supérieur immédiat.

**6.9 — Enregistrer, si aucun refus.** Condition `empty(variables('motifRefus'))`, **est égal à** `true`. Dans la branche Oui :
1. Composer `Versionne` :
```
setProperty(variables('dossier'),'workflow',setProperty(setProperty(variables('dossier')?['workflow'],'version',add(coalesce(variables('dossier')?['workflow']?['version'],0),1)),'derniereMaj',variables('maintenant')))
```
2. Action SharePoint **Mettre à jour le fichier**. Identificateur : `first(body('ChercherDossier')?['value'])?['{Identifier}']`. Contenu : `string(outputs('Versionne'))`.
3. Action **Mettre à jour les propriétés du fichier**. Id : `first(body('ChercherDossier')?['value'])?['ID']`.
   - NomPersonne : `outputs('Versionne')?['identification']?['nom']`
   - Statut, expression :
```
if(equals(outputs('Versionne')?['workflow']?['status'],'brouillon'),'Brouillon',if(equals(outputs('Versionne')?['workflow']?['status'],'approbation'),'En approbation','En approbation finale'))
```
   - EtapeEnCours : `outputs('Versionne')?['workflow']?['status']`
   - DerniereMaj : `utcNow()`

## 7. Après l'étendue : répondre et nettoyer

Ces actions vont **après** l'étendue `Traitement`, pas dedans.

1. **Étendue `EnCasErreur`.** Dans **… › Configurer l'exécution après**, cochez **a échoué** et **a expiré**, et décochez **a réussi**. Dedans : **Définir une variable** `motifRefus` = `Le dépôt n'a pas pu être lu. Recommencez avec le bouton « Copier le contenu du dépôt ».`
2. **Condition `Accepte`.** `empty(variables('motifRefus'))`, **est égal à** `true`. Dans **Configurer l'exécution après**, cochez **a réussi** et **a été ignoré**.
   - **Si oui** : courriel « Dépôt accepté » au déposant.
   - **Si non** : courriel « Dépôt refusé » au déposant.
3. **Supprimer l'élément de dépôt.** Action SharePoint **Supprimer l'élément**, liste Depot_Appreciations, Id = **ID** du déclencheur. Dans **Configurer l'exécution après**, cochez **toutes** les cases.

## 8. Les courriels (Office 365 Outlook — Envoyer un courriel (V2))

Les courriels ne contiennent **jamais** de cote, de commentaire ni d'évaluation.

- **Avis au supérieur** — Objet : `Appréciation de la contribution — dossier prêt pour votre lecture`. Texte : « Bonjour, [nom de la personne] a complété sa partie du formulaire d'appréciation. Ouvrez « Mes dossiers » (lien de la bibliothèque Dossiers_Appreciations), puis chargez le dossier dans l'application (lien de la bibliothèque de l'application). »
- **Approbation requise** — Objet : `Appréciation de la contribution — votre approbation est requise`. Texte : « Bonjour, le dossier d'appréciation de [nom] attend votre approbation. Ouvrez l'application, cochez votre rôle, chargez le dossier depuis « Mes dossiers », cochez « J'approuve » et déposez. »
- **Toutes les approbations sont obtenues** — Objet : `Appréciation de la contribution — approbations complétées`.
- **Dépôt accepté** — Objet : `Appréciation de la contribution — dépôt accepté`. Texte : `variables('message')`, puis « Rechargez la version officielle depuis « Mes dossiers » avant de continuer. »
- **Dépôt refusé** — Objet : `Appréciation de la contribution — dépôt refusé`. Texte : « Votre dépôt n'a pas été traité. Raison : » `variables('motifRefus')`, puis « Rien n'a été modifié dans votre dossier. »

Pour le nom de la personne : `variables('dossier')?['identification']?['nom']`.

## 9. Tester le cheminement complet, seule (mode test = true)

Utilisez des **données fictives**. À chaque étape, attendez le courriel (1 à 2 minutes), puis rechargez le dossier : **📂 Mes dossiers** › téléchargez `<dossierId>.json` › **📁 Charger un dossier**. Pour changer de rôle, cliquez sur **🔓 Changer de rôle**.

| # | Rôle dans l'application | Action | Résultat attendu |
|---|---|---|---|
| 1 | Personne en appréciation | Choisir le poste, remplir, **☁️ Déposer** | Courriel « dépôt accepté » ; le fichier `<dossierId>.json` est dans Dossiers_Appreciations ; le numéro de dossier et les noms des supérieurs s'affichent après rechargement |
| 2 | Personne en appréciation | **📨 Aviser le supérieur** | Courriel « Avis au supérieur » |
| 3 | Supérieur(e) immédiat(e) | Recharger, coter, remplir E et l'évaluation globale, **☁️ Déposer** | Les cotes et la section E sont enregistrées |
| 4 | (facultatif) Personne en appréciation | Ouvrir le fichier `.json` dans le Bloc-notes, changer le texte de `bilanSuperieur`, le charger, puis déposer | Le bilan E **n'est pas** recopié : la protection fonctionne |
| 5 | Personne en appréciation | Recharger, cocher la certification, **✔ Certifier** | Statut « En approbation » ; contenu verrouillé |
| 6 | Supérieur(e) hiérarchique | Recharger, cocher « J'approuve », déposer | Refusé : « Ce n'est pas votre étape » (le supérieur immédiat n'a pas encore approuvé) |
| 7 | Supérieur(e) immédiat(e) | Approuver | Approbation enregistrée ; courriel au supérieur hiérarchique |
| 8 | Supérieur(e) hiérarchique | Approuver | Statut « En approbation finale » ; courriel « approbations complétées » |
| 9 | — | Coller un texte quelconque dans « Contenu » | Courriel « dépôt refusé » ; l'élément est supprimé |

Quand tout est ✅, mettez `modeTest` à **false**. Faites ensuite un pilote avec 2 ou 3 vraies personnes (une personne en appréciation, son supérieur immédiat et son supérieur hiérarchique), toujours avec des données fictives. Le flux trouvera alors les supérieurs dans l'annuaire et vérifiera les vraies identités.

## 10. Phase 2, avant le déploiement réel (avec le TI)

- Site SharePoint dédié et **compte de service** propriétaire des flux.
- **Permissions par dossier** : chaque dossier n'est visible que par ses participants (requêtes HTTP SharePoint, connecteur standard).
- Directeur tiré de l'annuaire quand son approbation est requise.
- **Approbation finale** par tous (Approbations Power Automate), **PDF** final et **archives** en lecture seule.
- **Journal** des dépôts et **nettoyage** quotidien de la liste.
- Tests exigés par l'EFVP.
