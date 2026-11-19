# Flux 1 : « Approbation - Nouvelle demande »

**Rôle :** quand une demande est créée, envoyer un courriel à l'approbateur.

Connecteurs utilisés (standards, inclus avec Microsoft 365) : SharePoint, Office 365 Outlook.

## Création
1. https://make.powerautomate.com > **+ Créer** > **Flux de cloud automatisé**
2. Nom : `Approbation - Nouvelle demande`
3. Déclencheur : **SharePoint – Lors de la création d'un élément** (*When an item is created*) > **Créer**

## Étape 1 : déclencheur
| Champ | Valeur |
|---|---|
| Adresse du site | votre site SharePoint |
| Nom de la liste | `ApprovalRequests` |

## Étape 2 : Office 365 Outlook – Envoyer un e-mail (V2)
| Champ | Valeur (expression à coller avec le bouton **fx**) |
|---|---|
| À | `triggerOutputs()?['body/Approver/Email']` |
| Objet | `concat('Nouvelle demande à approuver : ', triggerOutputs()?['body/Title'])` |
| Importance | Normal |

**Corps** : passez en mode code (`</>`) et collez :

```html
<p>Bonjour @{triggerOutputs()?['body/Approver/DisplayName']},</p>
<p><b>@{triggerOutputs()?['body/Author/DisplayName']}</b> vous a soumis une demande d'approbation.</p>
<table border="1" cellpadding="6" style="border-collapse:collapse">
  <tr><td><b>Titre</b></td><td>@{triggerOutputs()?['body/Title']}</td></tr>
  <tr><td><b>Catégorie</b></td><td>@{triggerOutputs()?['body/Category/Value']}</td></tr>
  <tr><td><b>Montant</b></td><td>@{triggerOutputs()?['body/Amount']} $</td></tr>
  <tr><td><b>Description</b></td><td>@{triggerOutputs()?['body/Description']}</td></tr>
</table>
<p><a href="COLLEZ_ICI_LE_LIEN_DE_VOTRE_APPLICATION">Ouvrir l'application pour approuver ou rejeter</a></p>
```

> Le lien de l'application se trouve dans Power Apps > **Applications** > `...` > **Détails** > **Lien web**.

4. **Enregistrer**. Pour tester, créez une demande depuis l'application.
