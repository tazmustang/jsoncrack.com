# Étape 1 — Créer la liste de dépôt et la bibliothèque des dossiers (30 minutes)

Site : **SandBox Annie Audet**. Aucune demande au TI n'est nécessaire pour cette étape. Rien à payer.

Le fichier `appreciation-cadres-v3.3.html` pointe déjà vers ces deux adresses. **Respectez les noms à la lettre** (majuscules et trait de soulignement compris), sinon les boutons de l'application ouvriront une page introuvable.

| À créer | Adresse attendue par l'application |
|---|---|
| Liste **Depot_Appreciations** | `…/sites/SandBoxAnnieAudet/Lists/Depot_Appreciations/NewForm.aspx` |
| Bibliothèque **Dossiers_Appreciations** | `…/sites/SandBoxAnnieAudet/Dossiers_Appreciations` |

---

## A. La liste « Depot_Appreciations » (la porte d'entrée)

C'est là que chaque personne joint son fichier `depot-….json`. SharePoint y note automatiquement **qui** l'a déposé, et ce nom ne peut pas être falsifié.

1. Dans le site, cliquez sur **+ Nouveau › Liste › Liste vide**.
2. Nom : `Depot_Appreciations`. Décochez « Afficher dans la navigation du site ». Cliquez sur **Créer**.
3. ⚙️ (en haut à droite) › **Paramètres de la liste**.
4. Cliquez sur la colonne **Titre**. Réglez « Exiger que cette colonne contienne des informations » sur **Non**, puis **OK**.
5. Revenez aux paramètres, puis cliquez sur **Paramètres avancés** :
   - **Pièces jointes** : *Activées* ;
   - **Accès en lecture** : *Lire les éléments créés par l'utilisateur* ;
   - **Accès en création et modification** : *Créer des éléments et modifier les éléments créés par l'utilisateur* ;
   - cliquez sur **OK** en bas de la page.
6. Vérification : ouvrez cette adresse dans le navigateur :
   `https://villedequebec.sharepoint.com/sites/SandBoxAnnieAudet/Lists/Depot_Appreciations/NewForm.aspx`
   Un formulaire « Nouvel élément » doit apparaître, avec **« Ajouter des pièces jointes »**.

> Dans le site de test, vous seule y avez accès : c'est parfait pour essayer. L'ouverture à tous les cadres (permissions « Collaboration ») se fera plus tard, sur le site officiel.

## B. La bibliothèque « Dossiers_Appreciations » (les dossiers officiels)

C'est là que le flux rangera la version officielle de chaque dossier. Les gens la rechargent ensuite avec « 📁 Charger un dossier ».

1. **+ Nouveau › Bibliothèque de documents › Bibliothèque vide**.
2. Nom : `Dossiers_Appreciations`. Cliquez sur **Créer**.
3. Ajoutez ces colonnes (**+ Ajouter une colonne** au-dessus de la liste des fichiers) :

| Colonne | Type |
|---|---|
| DossierId | Une seule ligne de texte |
| NomPersonne | Une seule ligne de texte |
| TypePoste | Une seule ligne de texte |
| Statut | Choix : Brouillon · En approbation · En approbation finale · Complété |
| EtapeEnCours | Une seule ligne de texte |
| DerniereMaj | Date et heure |

4. ⚙️ › **Paramètres de la bibliothèque** › **Paramètres de contrôle de version** : *Créer des versions principales*, conserver **50** versions, puis **OK**. Chaque dépôt accepté laissera une version : c'est l'historique du dossier.

## C. Vérifier dans l'application

1. Déposez le nouveau `appreciation-cadres-v3.3.html` dans votre bibliothèque « Appréciation de la contribution des cadres ». Choisissez **Remplacer**.
2. Ouvrez-le et remplissez un champ.
3. Cliquez sur **☁️ Déposer sur SharePoint**, puis **Ouvrir le formulaire de dépôt** : le formulaire de la liste A doit s'ouvrir.
4. Cliquez sur **📂 Ouvrir « Mes dossiers »** : la bibliothèque B doit s'ouvrir.

**À ce stade**, un dépôt est enregistré dans la liste, mais **rien d'autre ne se passe** : pas de courriel et pas de dossier officiel. C'est le rôle du flux Power Automate « AC - Traiter un dépôt », qui est l'étape 2.

## D. Plus tard : l'ancienne liste

`AppreciationsCadres_Suivi` appartient à l'ancienne version (avec ses 3 anciens flux). Ne la supprimez pas tout de suite. Le moment venu, désactivez ses anciens flux et videz-la de toute donnée réelle saisie pendant les essais.
