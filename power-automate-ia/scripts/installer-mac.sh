#!/usr/bin/env bash
# Installation des outils pour Power Automate avec Claude Code (macOS)
# Usage : bash installer-mac.sh

set -u

titre() { printf "\n\033[36m=== %s ===\033[0m\n" "$1"; }

titre "Homebrew"
if ! command -v brew >/dev/null 2>&1; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Rendre brew disponible tout de suite (Mac Apple Silicon ou Intel)
  [ -x /opt/homebrew/bin/brew ] && eval "$(/opt/homebrew/bin/brew shellenv)"
  [ -x /usr/local/bin/brew ] && eval "$(/usr/local/bin/brew shellenv)"
else
  echo "Homebrew est deja installe."
fi

for paquet in node azure-cli jq; do
  titre "$paquet"
  if brew list "$paquet" >/dev/null 2>&1; then
    echo "$paquet est deja installe."
  else
    brew install "$paquet"
  fi
done

titre "Claude Code"
if command -v claude >/dev/null 2>&1; then
  echo "Claude Code est deja installe."
else
  curl -fsSL https://claude.ai/install.sh | bash
fi

printf "\nInstaller aussi .NET SDK + Power Platform CLI (pac) pour les solutions ? (o/n) "
read -r rep
if [[ "$rep" =~ ^[oOyY] ]]; then
  titre ".NET SDK"
  brew list --cask dotnet-sdk >/dev/null 2>&1 || brew install --cask dotnet-sdk
  titre "Power Platform CLI (pac)"
  dotnet tool install --global Microsoft.PowerApps.CLI.Tool || dotnet tool update --global Microsoft.PowerApps.CLI.Tool
  ligne='export PATH="$PATH:$HOME/.dotnet/tools"'
  grep -qxF "$ligne" ~/.zshrc 2>/dev/null || echo "$ligne" >> ~/.zshrc
fi

printf "\n\033[32mTermine ! FERMEZ puis ROUVREZ le Terminal, puis passez a l'etape 2 du guide (verification).\033[0m\n"
