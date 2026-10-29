# Crée un fichier .zip par skill dans dist\ (format attendu par claude.ai : dossier\SKILL.md).
# Usage (PowerShell, depuis le dossier du kit) : .\scripts\empaqueter-skills.ps1
$racine = Split-Path -Parent $PSScriptRoot
New-Item -ItemType Directory -Force -Path "$racine\dist" | Out-Null
Get-ChildItem -Directory "$racine\skills" | ForEach-Object {
    $zip = "$racine\dist\$($_.Name).zip"
    if (Test-Path $zip) { Remove-Item $zip }
    Compress-Archive -Path $_.FullName -DestinationPath $zip
    Write-Output $zip
}
