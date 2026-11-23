# Guide d'installation — Power Automate avec Claude Code

Durée : environ 30 minutes. À faire **une seule fois** sur votre poste personnel.

> Choisissez la section **Windows** ou **Mac** selon votre ordinateur. Les étapes 4 à 7 sont communes.

---

## Étape 0 — Prérequis

- Un abonnement **Claude Pro** (ou supérieur) ou un compte API Anthropic.
- Un compte Microsoft (professionnel ou scolaire) qui a accès à **Power Automate**.
- Les droits administrateur sur votre ordinateur (pour installer des logiciels).
- Récupérer ce dossier sur votre poste :
  - **Option A (sans outil)** : sur GitHub, allez sur le dépôt `tazmustang/jsoncrack.com`, choisissez la branche `claude/beautiful-curie-or48i8`, bouton **Code → Download ZIP**, puis gardez seulement le dossier `power-automate-ia`.
  - **Option B** : téléchargez le fichier `power-automate-ia.zip` envoyé dans la conversation Claude.

---

## Étape 1 (Windows) — Installation automatique

1. Ouvrez le menu Démarrer, tapez **PowerShell**, clic droit → **Exécuter en tant qu'administrateur**.
2. Allez dans le dossier `scripts` (adaptez le chemin) :
   ```powershell
   cd "$HOME\Downloads\power-automate-ia\scripts"
   ```
3. Autorisez l'exécution du script pour cette fenêtre seulement, puis lancez-le :
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\installer-windows.ps1
   ```
4. Le script installe avec `winget` (inclus dans Windows 10/11) : **Git**, **Node.js LTS**, **Azure CLI**, **jq**, puis **Claude Code**. Il vous demande si vous voulez aussi **.NET + Power Platform CLI (pac)** — répondez `o` si vous utiliserez des *solutions* (recommandé pour la production).
5. **Fermez puis rouvrez PowerShell** (normal, pas admin) pour que les nouveaux outils soient reconnus.

<details>
<summary>Installation manuelle (si le script échoue)</summary>

```powershell
winget install -e --id Git.Git
winget install -e --id OpenJS.NodeJS.LTS
winget install -e --id Microsoft.AzureCLI
winget install -e --id jqlang.jq
irm https://claude.ai/install.ps1 | iex
# Optionnel (solutions) :
winget install -e --id Microsoft.DotNet.SDK.8
dotnet tool install --global Microsoft.PowerApps.CLI.Tool
```
</details>

## Étape 1 (Mac) — Installation automatique

1. Ouvrez l'application **Terminal**.
2. Allez dans le dossier `scripts` et lancez le script :
   ```bash
   cd ~/Downloads/power-automate-ia/scripts
   bash installer-mac.sh
   ```
3. Le script installe **Homebrew** (s'il manque), puis **Node.js**, **Azure CLI**, **jq** et **Claude Code**. Il propose aussi **.NET + pac** (répondez `o` si vous utiliserez des solutions).
4. **Fermez puis rouvrez le Terminal.**

<details>
<summary>Installation manuelle (si le script échoue)</summary>

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install node azure-cli jq
curl -fsSL https://claude.ai/install.sh | bash
# Optionnel (solutions) :
brew install --cask dotnet-sdk
dotnet tool install --global Microsoft.PowerApps.CLI.Tool
echo 'export PATH="$PATH:$HOME/.dotnet/tools"' >> ~/.zshrc
```
</details>

---

## Étape 2 — Vérifier les installations

Dans un nouveau terminal :
```
node --version      (doit afficher v18 ou plus)
az --version
jq --version
claude --version
pac help            (seulement si installé)
```

---

## Étape 3 — Se connecter à Microsoft (Azure CLI)

```
az login
```
Une page de navigateur s'ouvre : connectez-vous avec votre compte qui a accès à Power Automate.

- **Message « No subscriptions found » ?** C'est normal si vous n'avez pas d'abonnement Azure (inutile pour Power Automate). Utilisez :
  ```
  az login --allow-no-subscriptions --tenant VOTRE-DOMAINE.onmicrosoft.com
  ```
- Vérifiez l'utilisateur et le tenant (l'organisation) :
  ```
  az account show
  ```

> ⚠️ Si vous avez plusieurs organisations, le tenant actif peut changer sans prévenir. Une erreur « L'utilisateur n'est pas membre de l'organisation » veut dire **mauvais tenant**, pas un problème de droits.

---

## Étape 4 — Préparer le dossier de projet

1. Copiez le dossier `modele-projet` où vous voulez, et renommez-le, par exemple :
   - Windows : `C:\Users\VOUS\Documents\flux-power-automate`
   - Mac : `~/Documents/flux-power-automate`
2. Ouvrez un terminal **dans ce dossier** :
   ```
   cd ~/Documents/flux-power-automate
   ```

---

## Étape 5 — Lancer Claude Code et se connecter

```
claude
```
À la première ouverture, Claude vous demande de vous connecter à votre compte Claude (navigateur). Acceptez ensuite de faire confiance au dossier.

---

## Étape 6 — Installer le plugin Power Automate de Microsoft

Dans Claude Code (tapez ces lignes une par une, elles commencent par `/`) :
```
/plugin marketplace add microsoft/power-platform-skills
/plugin install power-automate@power-platform-skills
```
Quittez (`/exit`) et relancez `claude` pour activer le plugin.

**Test** — demandez simplement :
> Liste mes environnements Power Automate.

- Vous voyez vos environnements → ✅ tout fonctionne.
- Vous voyez les environnements d'une autre organisation → le plugin utilise un autre compte : refaites l'étape 3 avec le bon tenant.
- Erreur de connexion → demandez à Claude : « Utilise la compétence de configuration du plugin Power Automate pour diagnostiquer. »

---

## Étape 7 (optionnelle) — Power Platform CLI pour les solutions

Si vous avez installé `pac` :
```
pac auth create --url https://VOTRE-ORG.crm.dynamics.com
pac auth list
```
(L'adresse se trouve dans le Power Platform admin center → Environnements → URL de l'environnement.)

Puis, **une fois par environnement**, activez la création des flux dans les solutions :
```
pac env list-settings
pac env update-settings --name enableflowsinsolutionbydefault --value true
```

---

## Étape 8 — Remplir CLAUDE.md

Ouvrez `CLAUDE.md` dans le dossier de projet et remplacez les `[À REMPLIR]`.
Astuce : demandez à Claude :
> Liste mes environnements et mes solutions, puis aide-moi à remplir CLAUDE.md.

**C'est terminé !** Passez au `GUIDE-UTILISATION.md`.

---

## Dépannage rapide

| Problème | Solution |
|---|---|
| `claude`, `az` ou `pac` « introuvable » | Fermez et rouvrez le terminal. Sur Mac pour `pac` : `export PATH="$PATH:$HOME/.dotnet/tools"` |
| Script PowerShell bloqué | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` dans la même fenêtre |
| « L'utilisateur n'est pas membre de l'organisation » | Mauvais tenant : `az account show`, puis `az login --tenant ...` |
| `pac` renvoie des résultats d'un autre environnement | `pac auth list` (le profil actif a une `*`), puis `pac auth select --index N` |
| Le plugin n'apparaît pas | `/plugin` dans Claude pour voir la liste ; relancer `claude` |
