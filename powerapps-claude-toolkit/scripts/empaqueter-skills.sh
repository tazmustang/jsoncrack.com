#!/usr/bin/env bash
# Crée un fichier .zip par skill dans dist/ (format attendu par claude.ai : dossier/SKILL.md).
# Usage : bash scripts/empaqueter-skills.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
for dossier in skills/*/; do
  nom=$(basename "$dossier")
  rm -f "dist/$nom.zip"
  (cd skills && zip -qr "../dist/$nom.zip" "$nom")
  echo "dist/$nom.zip"
done
