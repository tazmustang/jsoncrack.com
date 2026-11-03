# -*- coding: utf-8 -*-
"""Régénère tous les fichiers de l'application :  python3 generer.py"""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
RACINE = os.path.dirname(ICI)
import gen_sharepoint, gen_powerapps
n = gen_sharepoint.build(os.path.join(RACINE, '1_SharePoint', 'Installer_SharePoint.js'))
print('SharePoint : script généré (%d éléments de référence)' % n)
files = gen_powerapps.build(os.path.join(RACINE, '3_PowerApps'))
print('Power Apps : %d écrans' % len(files))
import gen_guide
gen_guide.build(RACINE)
print('Guide : Guide_installation_utilisation.docx, README.md, 2_PowerAutomate/Flux_SSTGenererPDF.md')
