# Flux 2 : « Approbation - Décision »

**Rôle :** quand une demande passe à *Approuvé* ou *Rejeté*, envoyer un courriel au demandeur,
puis cocher `NotificationSent` pour ne jamais envoyer ce courriel deux fois.

## Création
1. **+ Créer** > **Flux de cloud automatisé**
2. Nom : `Approbation - Décision`
3. Déclencheur : **SharePoint – Lors de la création ou de la modification d'un élément**
   (*When an item is created or modified*)

## Étape 1 : déclencheur
| Champ | Valeur |
|---|---|
| Adresse du site | votre site SharePoint |
| Nom de la liste | `ApprovalRequests` |

### Condition de déclenchement (très important : elle empêche les boucles)
Cliquez sur le déclencheur > **Paramètres** > **Conditions de déclenchement** > **+ Ajouter** et collez :

```
@and(or(equals(triggerBody()?['Status']?['Value'],'Approuvé'),equals(triggerBody()?['Status']?['Value'],'Rejeté')),not(equals(triggerBody()?['NotificationSent'],true)))
```

En clair : le flux démarre seulement si le statut est Approuvé ou Rejeté **et** si la notification n'a pas encore été envoyée.

## Étape 2 : Office 365 Outlook – Envoyer un e-mail (V2)
| Champ | Expression |
|---|---|
| À | `triggerOutputs()?['body/Author/Email']` |
| Objet | `concat('Votre demande « ', triggerOutputs()?['body/Title'], ' » a été ', toLower(triggerOutputs()?['body/Status/Value']))` |

**Corps** (mode code `</>`) :

```html
<p>Bonjour @{triggerOutputs()?['body/Author/DisplayName']},</p>
<p>Votre demande <b>@{triggerOutputs()?['body/Title']}</b> a été
<b>@{toLower(triggerOutputs()?['body/Status/Value'])}</b>
par @{triggerOutputs()?['body/Approver/DisplayName']}.</p>
<p><b>Commentaire :</b> @{coalesce(triggerOutputs()?['body/ApproverComments'], '(aucun)')}</p>
<p><a href="COLLEZ_ICI_LE_LIEN_DE_VOTRE_APPLICATION">Ouvrir l'application</a></p>
```

## Étape 3 : SharePoint – Mettre à jour l'élément (*Update item*)
| Champ | Valeur |
|---|---|
| Adresse du site | votre site |
| Nom de la liste | `ApprovalRequests` |
| Id | `triggerOutputs()?['body/ID']` |
| Titre | `triggerOutputs()?['body/Title']` |
| NotificationSent | **Oui** |

Laissez les autres champs vides : ils ne seront pas modifiés.

4. **Enregistrer**.

---

## Option : approbation par Teams/Outlook au lieu de l'application
Vous pouvez remplacer le Flux 1 par l'action **Approbations – Démarrer et attendre une approbation**
(type *Approuver/Refuser – Premier à répondre*, assigné à `triggerOutputs()?['body/Approver/Email']`).
Ensuite, une **Condition** `outcome = Approve` > **Mettre à jour l'élément** avec Status = `Approuvé` ou `Rejeté`,
ApproverComments = `first(body('Démarrer_et_attendre_une_approbation')?['responses'])?['comments']`
et DecisionDate = `utcNow()`. Le Flux 2 enverra alors le courriel de décision automatiquement.
