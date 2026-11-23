# Verifie les connexions avant une session de travail (Windows)
# Usage : .\verifier-connexions.ps1

Write-Host "`n=== Azure CLI (az) : compte actif ===" -ForegroundColor Cyan
az account show --query "{utilisateur:user.name, tenant:tenantId, abonnement:name}" -o table
if ($LASTEXITCODE -ne 0) { Write-Host "Non connecte : lancez 'az login'" -ForegroundColor Red }

Write-Host "`n=== Power Platform CLI (pac) : profils (* = actif) ===" -ForegroundColor Cyan
if (Get-Command pac -ErrorAction SilentlyContinue) {
    pac auth list
} else {
    Write-Host "pac non installe (optionnel)." -ForegroundColor Yellow
}

Write-Host "`nVerifiez que l'utilisateur, le tenant et le profil pac sont les BONS avant de lancer 'claude'." -ForegroundColor Green
Write-Host "Puis, dans Claude, demandez : 'Liste mes environnements Power Automate.'"
