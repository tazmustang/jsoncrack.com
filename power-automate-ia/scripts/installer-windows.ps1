# Installation des outils pour Power Automate avec Claude Code (Windows 10/11)
# Usage (PowerShell administrateur) :
#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#   .\installer-windows.ps1

$ErrorActionPreference = "Continue"

function Installer-Winget($id, $nom) {
    Write-Host "`n=== $nom ===" -ForegroundColor Cyan
    winget list -e --id $id *> $null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "$nom est deja installe." -ForegroundColor Green
    } else {
        winget install -e --id $id --accept-source-agreements --accept-package-agreements
    }
}

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Host "winget est introuvable. Installez 'App Installer' depuis le Microsoft Store, puis relancez ce script." -ForegroundColor Red
    exit 1
}

Installer-Winget "Git.Git"             "Git (requis par Claude Code sous Windows)"
Installer-Winget "OpenJS.NodeJS.LTS"   "Node.js LTS"
Installer-Winget "Microsoft.AzureCLI"  "Azure CLI"
Installer-Winget "jqlang.jq"           "jq"

Write-Host "`n=== Claude Code ===" -ForegroundColor Cyan
if (Get-Command claude -ErrorAction SilentlyContinue) {
    Write-Host "Claude Code est deja installe." -ForegroundColor Green
} else {
    irm https://claude.ai/install.ps1 | iex
}

$rep = Read-Host "`nInstaller aussi .NET SDK + Power Platform CLI (pac) pour les solutions ? (o/n)"
if ($rep -match '^[oOyY]') {
    Installer-Winget "Microsoft.DotNet.SDK.8" ".NET SDK 8"
    $env:Path += ";$HOME\.dotnet\tools"
    Write-Host "`n=== Power Platform CLI (pac) ===" -ForegroundColor Cyan
    dotnet tool install --global Microsoft.PowerApps.CLI.Tool
    if ($LASTEXITCODE -ne 0) { dotnet tool update --global Microsoft.PowerApps.CLI.Tool }
}

Write-Host "`nTermine ! FERMEZ puis ROUVREZ PowerShell, puis passez a l'etape 2 du guide (verification)." -ForegroundColor Green
