#!/usr/bin/env bash
# Verifie les connexions avant une session de travail (macOS)
# Usage : bash verifier-connexions.sh

printf "\n\033[36m=== Azure CLI (az) : compte actif ===\033[0m\n"
az account show --query "{utilisateur:user.name, tenant:tenantId, abonnement:name}" -o table \
  || printf "\033[31mNon connecte : lancez 'az login'\033[0m\n"

printf "\n\033[36m=== Power Platform CLI (pac) : profils (* = actif) ===\033[0m\n"
export PATH="$PATH:$HOME/.dotnet/tools"
if command -v pac >/dev/null 2>&1; then
  pac auth list
else
  echo "pac non installe (optionnel)."
fi

printf "\n\033[32mVerifiez que l'utilisateur, le tenant et le profil pac sont les BONS avant de lancer 'claude'.\033[0m\n"
echo "Puis, dans Claude, demandez : 'Liste mes environnements Power Automate.'"
