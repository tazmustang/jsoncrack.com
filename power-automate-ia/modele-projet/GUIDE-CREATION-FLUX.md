# Guide de création d'un flux (à suivre par Claude, de A à Z)

## A. Avant de commencer

- [ ] `az account show` : bon utilisateur et bon tenant (voir `CLAUDE.md`).
- [ ] Si solution : `pac auth list` → le profil actif (`*`) est le bon environnement.
- [ ] Le plugin liste bien les environnements attendus.
- [ ] Si solution : le paramètre `enableflowsinsolutionbydefault` est à `true` dans l'environnement (piège n° 1).
- [ ] Le besoin est clair : déclencheur, étapes, résultat, personnes notifiées. Sinon, **poser les questions avant de construire**.

## B. Conception

- [ ] Résumer le flux prévu en 5 à 10 lignes et le faire valider par l'utilisateur.
- [ ] Respecter la structure standard et les conventions de `CLAUDE.md`.
- [ ] Prévoir la condition de déclenchement.
- [ ] Prévoir la gestion d'erreurs (Essayer / Intercepter).

## C. Construction

- [ ] Créer le flux avec la définition complète, dans l'environnement de **test**.
- [ ] Toutes les expressions dans des valeurs JSON sont **entre guillemets** : `"Title": "@{...}"` (piège n° 4).
- [ ] Paramètres de connecteur personnalisé **à plat** (`body/model`) (piège n° 3).
- [ ] Chaque fonction d'expression utilisée existe vraiment (piège n° 5).
- [ ] Si une action d'IA est utilisée dans le flux : ajouter une vérification de la réponse (piège n° 7).

## D. Vérification

- [ ] Demander à l'utilisateur d'ouvrir le flux dans l'éditeur : **aucun champ vide**, actions lisibles.
- [ ] Vérifier les **références de connexion** de chaque action ; les faire corriger dans l'éditeur si besoin (piège n° 2).

## E. Test

- [ ] **Activer** le flux **avant** de créer les données de test (piège n° 6).
- [ ] Créer un **vrai** enregistrement de test qui doit déclencher le flux.
- [ ] Créer aussi un enregistrement qui **ne doit pas** le déclencher (teste la condition).
- [ ] Vérifier l'exécution ; en cas d'échec, diagnostiquer (y compris chaque itération de boucle).
- [ ] Nettoyer les données de test.

## F. Clôture

- [ ] Créer ou mettre à jour la fiche `flux/NOM-DU-FLUX.md`.
- [ ] Mettre à jour `HANDOVER.md`.
- [ ] Nouveau problème rencontré ? L'ajouter ci-dessous.

---

## Pièges connus

1. **Flux dans les solutions** — Si `enableflowsinsolutionbydefault` est désactivé, le flux créé n'est pas enregistré dans Dataverse et ne peut pas être ajouté plus tard à une solution sans être recréé.
   `pac env update-settings --name enableflowsinsolutionbydefault --value true`
2. **Références de connexion choisies automatiquement** — Dans une solution, la plateforme associe chaque action à une référence existante du connecteur, pas forcément la bonne. Le plugin ne peut pas les changer : correction dans l'éditeur.
3. **Paramètres à plat** — Pour les connecteurs personnalisés avec corps JSON : clés `body/model`, pas un objet `body` imbriqué. La version imbriquée s'enregistre sans erreur mais les champs sont vides et l'action échoue.
4. **Guillemets autour des expressions** — `"Title": "@{...}"` et non `"Title": @{...}` (JSON invalide après évaluation).
5. **Fonctions inventées** — Erreur « non définie ou non valide » : vérifier d'abord que la fonction existe (ex. `createObject()` n'existe pas).
6. **Tester avec le vrai déclencheur** — Pas de corps de déclencheur simulé. Un déclencheur par interrogation (« Lorsqu'un élément est créé ») ne voit que les éléments créés **après** l'activation.
7. **Vérifier les réponses d'IA dans un flux** — Contrôler longueur, format ou préfixe ; si la vérification échoue, sauter l'étape pour ne pas écrire de données erronées.

<!-- Ajouter les nouveaux pièges ici : n°. Titre — symptôme — cause — solution -->
