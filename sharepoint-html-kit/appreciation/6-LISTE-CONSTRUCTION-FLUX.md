# Liste de construction du flux « AC - Traiter un dépôt » — à cocher

Suivez les lignes **dans l'ordre, de haut en bas**, comme elles apparaissent à l'écran. Cochez au fur et à mesure.

**Comment remplir une carte :**
- **Nom** : renommez la carte avec **… › Renommer**.
- **Valeur « (fx) »** : cliquez dans le champ, ouvrez l'onglet **Expression (fx)**, collez, puis cliquez sur **OK**.
- **Valeur « texte »** : tapez ou collez directement dans le champ.

---

## Partie A — Le haut du flux (hors de l'étendue)

| ☐ | Carte | Action Power Automate | À remplir |
|---|---|---|---|
| ☐ | **Lorsqu'un élément est créé ou modifié** | SharePoint (déclencheur) | Site : SandBox Annie Audet · Liste : Depot_Appreciations · **… › Paramètres** : simultanéité **activée, 1** · Condition de déclenchement (voir la note sous le tableau) |
| ☐ | **deposant** | Initialiser une variable | Type **Chaîne** · Valeur (fx) : `toLower(triggerBody()?['Author']?['Email'])` |
| ☐ | **motifRefus** | Initialiser une variable | Type **Chaîne** · Valeur : *(vide)* |
| ☐ | **message** | Initialiser une variable | Type **Chaîne** · Valeur : *(vide)* |
| ☐ | **modeTest** | Initialiser une variable | Type **Booléen** · Valeur : **true** |
| ☐ | **nomDeposant** | Initialiser une variable | Type **Chaîne** · Valeur (fx) : `triggerBody()?['Author']?['DisplayName']` |
| ☐ | **maintenant** | Initialiser une variable | Type **Chaîne** · Valeur (fx) : `formatDateTime(convertFromUtc(utcNow(),'Eastern Standard Time'),'yyyy-MM-dd HH:mm')` |
| ☐ | **texteDepot** | Initialiser une variable | Type **Chaîne** · Valeur : *(vide)* |
| ☐ | **dossier** | Initialiser une variable | Type **Objet** · Valeur : *(vide)* |

**Condition de déclenchement** : à coller directement dans la case de **Conditions de déclenchement** (le texte commence par `@`), pas dans l'onglet fx :
`@or(not(empty(triggerOutputs()?['body/Contenu'])), equals(triggerOutputs()?['body/Attachments'], true))`

L'ordre des variables n'a pas d'importance, pourvu qu'elles soient toutes **au-dessus** de l'étendue.

**À supprimer s'ils existent encore** (anciennes variables) : **role**, **fusion**, **clePermises**, **messageSucces**, **nomFichierDossier**, **idElementDossier**. Pour chacune : **… › Supprimer**. Si Power Automate refuse, une autre action l'utilise encore : envoyez-moi une capture.

## Partie B — Dans l'étendue « Traitement » (début)

| ☐ | Carte | Action Power Automate | À remplir |
|---|---|---|---|
| ☐ | **Traitement** | Étendue | Renommez l'ancienne « Étendue » en `Traitement` |
| ☐ | **PJ** | SharePoint · Obtenir les pièces jointes | Site · Liste : Depot_Appreciations · ID (fx) : `triggerBody()?['ID']` |
| ☐ | **ContenuVide** | Condition | Gauche (fx) : `empty(coalesce(triggerBody()?['Contenu'],''))` · **est égal à** · Droite (fx) : `true` |
| ☐ | ↳ *Si oui* : **ContenuPJ** | SharePoint · Obtenir le contenu de la pièce jointe | Site · Liste · ID (fx) : `triggerBody()?['ID']` · Identificateur du fichier (fx) : `first(body('PJ'))?['Id']` |
| ☐ | ↳ *Si oui* : **Définir texteDepot** | Définir la variable | Nom : texteDepot · Valeur (fx) : `base64ToString(body('ContenuPJ')?['$content'])` |
| ☐ | ↳ *Si non* : **Définir texteDepot** | Définir la variable | Nom : texteDepot · Valeur (fx) : `triggerBody()?['Contenu']` |
| ☐ | **Depot** *(sous la condition)* | Composer | Entrées (fx) : `json(variables('texteDepot'))` |
| ☐ | **Controle** | Composer | Entrées (fx) : l'expression du guide 5, section 4.4 (variante recommandée) |
| ☐ | **Définir motifRefus** | Définir la variable | Nom : motifRefus · Valeur (fx) : `outputs('Controle')` |
| ☐ | **DepotValide** | Condition | Gauche (fx) : `empty(variables('motifRefus'))` · **est égal à** · Droite (fx) : `true` |
| ☐ | ↳ *Si oui* : **ChercherDossier** | SharePoint · Obtenir les fichiers (propriétés uniquement) | Bibliothèque : Dossiers_Appreciations · Requête de filtre et nombre maximal : guide 5, section 4.5 |
| ☐ | ↳ *Si oui* : **NouveauDossier** | Condition | Gauche (fx) : `length(body('ChercherDossier')?['value'])` · **est égal à** · Droite : `0` |

**Point de contrôle :** cliquez sur **Enregistrer**. Le **Vérificateur de flux** doit afficher **Erreurs (0)**. Envoyez-moi une capture : ensuite on attaque la partie C.

## Partie C — Branche « Si oui » de NouveauDossier (premier dépôt)
Guide 5, section 5 · schéma page 2/6. *(On la fera ensemble après la partie B.)*

## Partie D — Branche « Si non » de NouveauDossier (dossier existant)
Guide 5, section 6 · schémas pages 3/6, 4/6 et 5/6.

## Partie E — Après l'étendue (refus, courriels, nettoyage)
Guide 5, section 7 · schéma page 6/6.
