# Trousse « Power Automate avec Claude Code »

Tout ce qu'il faut pour créer, tester et déboguer des flux Power Automate avec Claude Code sur votre **poste personnel**.
Inspiré de l'article de Tom Riha (septembre 2026).

## Contenu du dossier

| Fichier | À quoi il sert |
|---|---|
| `GUIDE-INSTALLATION.md` | Installation pas à pas (Windows et Mac) — **commencez ici** |
| `GUIDE-UTILISATION.md` | Comment travailler au quotidien avec Claude, exemples de demandes |
| `scripts/installer-windows.ps1` | Installe automatiquement les outils sous Windows |
| `scripts/installer-mac.sh` | Installe automatiquement les outils sous Mac |
| `scripts/verifier-connexions.ps1` | Vérifie vos connexions (Windows) avant chaque session |
| `scripts/verifier-connexions.sh` | Vérifie vos connexions (Mac) avant chaque session |
| `modele-projet/` | Dossier de projet prêt à copier : c'est l'espace de travail de Claude |
| `modele-projet/CLAUDE.md` | La « carte » de votre environnement, lue automatiquement par Claude |
| `modele-projet/GUIDE-CREATION-FLUX.md` | La liste de contrôle que Claude suit pour chaque flux (avec les pièges connus) |
| `modele-projet/HANDOVER.md` | Où en est le travail, pour reprendre d'une session à l'autre |
| `modele-projet/flux/_MODELE-README-FLUX.md` | Modèle de fiche pour documenter chaque flux |
| `modele-projet/.claude/settings.json` | Autorise les commandes de vérification sans demande de permission |

## Coût

Tout est gratuit **sauf** l'abonnement Claude (Pro ou supérieur) ou un compte API Anthropic, nécessaire pour Claude Code.
Vous devez aussi avoir une licence Power Automate (souvent incluse avec Microsoft 365).

## En 4 étapes

1. Suivre `GUIDE-INSTALLATION.md` (~30 minutes).
2. Copier `modele-projet/` à l'endroit de votre choix (ex. `Documents/flux-power-automate`).
3. Remplir `CLAUDE.md` (environnement, conventions) — Claude peut vous aider.
4. Lancer `claude` dans ce dossier et demander votre premier flux (voir `GUIDE-UTILISATION.md`).
