# Projet : flux Power Automate

Tu crées, modifies, testes et débogues des flux Power Automate avec le plugin `power-automate`.
Réponds en **français**. Explique simplement ce que tu fais.

## Règles de travail (obligatoires)

1. **Avant de créer ou modifier un flux, lis et suis `GUIDE-CREATION-FLUX.md`.**
2. Au début de chaque session, vérifie le compte : `az account show` (et `pac auth list` si on utilise des solutions). Si le tenant ne correspond pas à celui ci-dessous, **arrête-toi et préviens-moi**.
3. Travaille uniquement dans l'environnement indiqué ci-dessous, sauf demande explicite.
4. Un changement à la fois. Sur un flux en production, **explique la correction avant de l'appliquer**.
5. Après chaque flux créé ou modifié : mets à jour sa fiche dans `flux/` et `HANDOVER.md`.
6. Quand un nouveau problème est résolu, ajoute-le aux « Pièges connus » de `GUIDE-CREATION-FLUX.md`.
7. N'invente jamais de fonction d'expression : en cas de doute, vérifie qu'elle existe dans le langage d'expressions Power Automate / Logic Apps.

## Environnement

| Élément | Valeur |
|---|---|
| Tenant (domaine) | [À REMPLIR, ex. monorg.onmicrosoft.com] |
| Compte utilisé | [À REMPLIR, ex. prenom.nom@monorg.com] |
| Environnement de **test** (nom / ID) | [À REMPLIR] |
| Environnement de **production** (nom / ID) | [À REMPLIR — ne pas toucher sans demande explicite] |
| URL Dataverse (pour `pac`) | [À REMPLIR, ex. https://monorg.crm.dynamics.com] |
| Solution pour les nouveaux flux | [À REMPLIR, ou « aucune »] |
| Éditeur de solution / préfixe | [À REMPLIR, ex. aa_] |

## Conventions de nommage

- **Flux** : `[PROJET] - [Action] [objet]` → ex. `DEM - Notification nouvelle demande`
- **Références de connexion** : `[PROJET] - [Connecteur]` → ex. `DEM - SharePoint`
- **Actions** : noms explicites en français (ex. « Obtenir la demande », pas « Get item 2 »)
- **Variables** : `var` + NomEnPascalCase → ex. `varCourrielApprobateur`

## Structure standard d'un flux

1. **Déclencheur** avec une *condition de déclenchement* pour filtrer (ex. statut = « Nouveau »).
2. Portée **« Essayer »** : tout le travail.
3. Portée **« Intercepter »** (exécuter après échec / expiration) : envoyer un courriel d'erreur à [À REMPLIR] avec le lien vers l'exécution, puis terminer en échec.
4. **Mise à jour du statut** de l'élément à la fin (ex. « Traité » / « Erreur »).

## Connecteurs disponibles

| Connecteur | Utilisation / particularités |
|---|---|
| SharePoint | Site principal : [À REMPLIR] |
| Office 365 Outlook | Envoi de courriels |
| Microsoft Teams | [À REMPLIR] |
| Dataverse | [À REMPLIR] |
| Connecteurs personnalisés | [À REMPLIR — nom, ce qu'il fait, particularités. Paramètres de corps « à plat » : `body/model`] |

## Fichiers du projet

- `GUIDE-CREATION-FLUX.md` — liste de contrôle et pièges connus
- `HANDOVER.md` — état du travail en cours
- `flux/` — une fiche par flux (modèle : `flux/_MODELE-README-FLUX.md`)
