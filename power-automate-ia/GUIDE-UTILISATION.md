# Guide d'utilisation — Créer des flux Power Automate avec Claude Code

## Routine à chaque session (2 minutes)

1. Ouvrez un terminal dans votre dossier de projet.
2. Vérifiez vos connexions :
   - Windows : `.\verifier-connexions.ps1` (copiez le script dans le dossier de projet, ou indiquez son chemin)
   - Mac : `bash verifier-connexions.sh`
3. Vérifiez que l'utilisateur, le tenant et le profil `pac` sont les bons. Sinon : `az login --tenant ...` / `pac auth select --index N`.
4. Lancez `claude`.
5. Si un travail était en cours, dites : **« Lis HANDOVER.md et reprends où on en était. »**

> `az`, `pac` et le plugin ont chacun **leur propre connexion**. Corriger l'un ne corrige pas les autres.

---

## Créer un flux — la méthode

1. **Décrivez le besoin** en langage courant, avec le déclencheur, les étapes et le résultat attendu.
2. **Laissez Claude suivre `GUIDE-CREATION-FLUX.md`** (il le fait automatiquement grâce à `CLAUDE.md`).
3. **Vérifiez dans l'éditeur Power Automate** (make.powerautomate.com) avant d'activer : champs vides, références de connexion.
4. **Testez avec un vrai enregistrement** (pas une simulation), flux activé *avant* de créer l'enregistrement.
5. **En cas d'échec**, demandez à Claude de diagnostiquer l'exécution.
6. **Faites mettre à jour la documentation** : fiche du flux, `HANDOVER.md` et, si un nouveau problème a été rencontré, `GUIDE-CREATION-FLUX.md`.

---

## Exemples de demandes à copier

**Créer**
> Crée un flux dans la solution indiquée dans CLAUDE.md : quand un élément est ajouté à la liste SharePoint « Demandes » avec le statut « Nouveau », envoie un courriel au responsable indiqué dans la colonne « Approbateur », puis passe le statut à « Envoyé ». Suis GUIDE-CREATION-FLUX.md.

**Modifier**
> Dans le flux « DEM - Notification nouvelle demande », ajoute une copie conforme à l'adresse du demandeur. Ne change rien d'autre.

**Déboguer**
> La dernière exécution du flux « DEM - Notification nouvelle demande » a échoué. Diagnostique la cause, propose une correction, et explique-la-moi avant de l'appliquer.

**Lister / comprendre**
> Liste mes flux de l'environnement de CLAUDE.md, avec leur état et leur dernière exécution.
> Explique-moi simplement ce que fait le flux « X », étape par étape.

**Documenter**
> Crée la fiche flux/DEM-notification.md à partir du modèle et mets à jour HANDOVER.md.

**Apprendre d'une erreur**
> Ajoute ce problème et sa solution dans la section « Pièges connus » de GUIDE-CREATION-FLUX.md.

---

## Ce que Claude fait / ce qui reste à vous

| Claude (avec le plugin) | Vous |
|---|---|
| Créer un flux complet | Vous connecter et vérifier le tenant à chaque session |
| Modifier une action précise | Corriger les **références de connexion** dans l'éditeur |
| Publier, activer, exécuter | Dernier coup d'œil dans l'éditeur avant publication |
| Diagnostiquer une exécution échouée (jusqu'à l'itération de boucle fautive) | Créer et nettoyer les données de test (ou le faire faire par Claude) |
| Tenir la documentation à jour | Valider les changements importants |

---

## Bonnes pratiques

- **Une demande = un changement.** Plus facile à vérifier et à annuler.
- **Demandez une explication avant toute correction** sur un flux en production.
- **Travaillez d'abord dans un environnement de test** (Developer ou Sandbox), jamais directement en production.
- **Erreur « non définie ou non valide » ?** L'IA a peut-être inventé une fonction : demandez-lui de vérifier qu'elle existe dans le langage d'expressions Power Automate.
- **Sauvegardez le dossier de projet** (OneDrive, GitHub privé…) : la documentation est votre vrai capital.
