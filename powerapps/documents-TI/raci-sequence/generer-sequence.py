# Génère le diagramme de séquence (SVG dans une page HTML) — python3 generer-sequence.py
L=["Personne en\nappréciation","Supérieur(e)\nimmédiat(e)","Supérieur(e)\nhiérarchique","Directeur(trice)\nde service","Application\nPower Apps","Liste SharePoint\nSRHVQ_Appreciations","Power Automate\n(flux 1, 2, 3)","Ressources\nhumaines"]
P,SI,SH,DIR,APP,SP,PA,RH=range(8)
B="#00285E";G="#8A8C8E"
steps=[
 ("sec","1. Création du dossier"),
 ("m",P,APP,"Nouveau formulaire · choisit le type de poste · remplit A, B, C, D, F"),
 ("m",APP,SP,"Enregistrer et déposer : crée le dossier (Statut Brouillon)"),
 ("m",SP,PA,"Flux 1 : nouvel élément"),
 ("self",PA,"Coupe l'héritage · retire SRHVQ_Utilisateurs · Collaboration aux personnes du dossier"),
 ("sec","2. Avis au supérieur et version du supérieur"),
 ("m",P,APP,"Aviser le supérieur"),
 ("m",APP,SP,"Statut = Avisé au supérieur · AviseLe"),
 ("m",SP,PA,"Flux 2 : élément modifié"),
 ("r",PA,SI,"Courriel : « prête pour votre consultation » + lien"),
 ("m",SI,APP,"Cotes B · bilan E · évaluation globale · Transmettre ma version"),
 ("m",APP,SP,"VersionSILe = maintenant"),
 ("r",PA,P,"Courriel : « la version de votre supérieur(e) est prête »"),
 ("note",P,SI,"Rencontre d'appréciation (hors application)"),
 ("sec","3. Confirmation et approbations"),
 ("m",P,APP,"Je confirme… · Approuver et soumettre"),
 ("m",APP,SP,"Statut = Certifié (affiché « Confirmé ») · contenu de la personne verrouillé"),
 ("r",PA,SI,"Courriel : « À approuver »"),
 ("m",SI,APP,"J'approuve · Approuver"),
 ("m",APP,SP,"Statut = Approuvé SI"),
 ("r",PA,SH,"Courriel : « À approuver »"),
 ("m",SH,APP,"J'approuve · Approuver"),
 ("m",APP,SP,"Statut = Approuvé SH (directeur requis) ou Complété"),
 ("alt","Si un directeur ou une directrice de service est requis(e)"),
 ("r",PA,DIR,"Courriel : « À approuver »"),
 ("m",DIR,APP,"J'approuve · Approuver"),
 ("m",APP,SP,"Statut = Complété"),
 ("altend",),
 ("sec","4. Clôture"),
 ("m",SP,PA,"Flux 2 : Statut = Complété"),
 ("r",PA,RH,"Courriel : évaluation globale seulement"),
 ("r",PA,P,"Avis à tous (personne, SI, SH) · dossier en lecture seule · date de transmission"),
 ("sec","En tout temps : PDF"),
 ("m",P,APP,"Aperçu PDF (toute personne du dossier)"),
 ("m",APP,PA,"Flux 3 GenererPDFAppreciation (HTML)"),
 ("m",PA,SP,"PDF joint au dossier (remplace l'ancien)"),
 ("r",PA,APP,"Lien du PDF : bouton « Ouvrir le PDF »"),
]
W=1560; lw=W/len(L); top=135; dy=38
xs=[lw*i+lw/2 for i in range(len(L))]
y=top+40; items=[]
def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace("«","«")
altstart=None
for s in steps:
    k=s[0]
    if k=="sec":
        y+=14; items.append(f'<rect x="8" y="{y-16}" width="{W-16}" height="24" fill="#E8EDF5" rx="4"/><text x="18" y="{y+1}" font-weight="700" fill="{B}" font-size="14">{esc(s[1])}</text>'); y+=dy-6
    elif k in("m","r"):
        a,b,t=s[1],s[2],s[3]; x1,x2=xs[a],xs[b]; d=1 if x2>x1 else -1
        dash='stroke-dasharray="6 4"' if k=="r" else ''
        col=G if k=="r" else B
        items.append(f'<line x1="{x1}" y1="{y}" x2="{x2-d*9}" y2="{y}" stroke="{col}" stroke-width="2" {dash}/><polygon points="{x2},{y} {x2-d*10},{y-5} {x2-d*10},{y+5}" fill="{col}"/>')
        tx=(x1+x2)/2; items.append(f'<text x="{tx}" y="{y-7}" text-anchor="middle" font-size="12.5" fill="#1f2937">{esc(t)}</text>'); y+=dy
    elif k=="self":
        a,t=s[1],s[2]; x=xs[a]
        items.append(f'<path d="M{x} {y-8} h28 v18 h-22" fill="none" stroke="{B}" stroke-width="2"/><polygon points="{x+2},{y+10} {x+12},{y+5} {x+12},{y+15}" fill="{B}"/>')
        items.append(f'<text x="{x-10}" y="{y+5}" text-anchor="end" font-size="12.5" fill="#1f2937">{esc(t)}</text>'); y+=dy+4
    elif k=="note":
        a,b,t=s[1],s[2],s[3]; x1,x2=xs[a]-60,xs[b]+60
        items.append(f'<rect x="{x1}" y="{y-16}" width="{x2-x1}" height="26" fill="#FFF7E6" stroke="#E0B060" rx="4"/><text x="{(x1+x2)/2}" y="{y+2}" text-anchor="middle" font-size="12.5" fill="#92400E">{esc(t)}</text>'); y+=dy
    elif k=="alt":
        altstart=(y-14,s[1]); y+=34
    elif k=="altend":
        y0,t=altstart
        items.append(f'<rect x="{xs[SH]+lw/2-20}" y="{y0}" width="{xs[SP]-xs[SH]+20}" height="{y-y0-14}" fill="none" stroke="{G}" stroke-dasharray="4 3" rx="6"/><text x="{xs[SH]+lw/2-12}" y="{y0+14}" font-size="12" font-style="italic" fill="#4b5563">alt : {esc(t)}</text>')
        y+=6
H=y+30
heads=""
for i,n in enumerate(L):
    x=xs[i]; l1,l2=n.split("\n")
    heads+=f'<rect x="{x-lw/2+8}" y="{top-62}" width="{lw-16}" height="50" rx="8" fill="{B}"/><text x="{x}" y="{top-42}" text-anchor="middle" fill="#fff" font-weight="700" font-size="13">{esc(l1)}</text><text x="{x}" y="{top-24}" text-anchor="middle" fill="#fff" font-size="12.5">{esc(l2)}</text>'
    heads+=f'<line x1="{x}" y1="{top-12}" x2="{x}" y2="{H-10}" stroke="#C9CDD3" stroke-width="1.5" stroke-dasharray="3 4"/>'
legend=f'<line x1="{W-430}" y1="22" x2="{W-390}" y2="22" stroke="{B}" stroke-width="2"/><text x="{W-384}" y="26" font-size="12">action d\'une personne ou de l\'application</text><line x1="{W-430}" y1="40" x2="{W-390}" y2="40" stroke="{G}" stroke-width="2" stroke-dasharray="6 4"/><text x="{W-384}" y="44" font-size="12">courriel ou réponse automatique</text>'
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Arial, sans-serif"><rect width="100%" height="100%" fill="#fff"/><text x="12" y="26" font-size="20" font-weight="700" fill="{B}">Appréciation de la contribution (SRHVQ) — diagramme de séquence</text><text x="12" y="46" font-size="12.5" fill="#4b5563">Version 1.0.0.9 · circuit complet, de la création à la clôture</text>{legend}{heads}{"".join(items)}</svg>'
open("diagramme-sequence.svg","w").write(svg)
open("diagramme-sequence.html","w").write(f'<!doctype html><html lang="fr"><meta charset="utf-8"><title>Diagramme de séquence SRHVQ</title><body style="margin:0;background:#fff">{svg}</body></html>')
print(W,H)
