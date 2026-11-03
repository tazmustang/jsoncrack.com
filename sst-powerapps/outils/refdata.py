import json,re,os
qs={q['n']:q for q in json.load(open(os.path.join(os.path.dirname(__file__),'qs.json'),encoding='utf8'))}
SERVICES=qs[8]['opts']
def norm(s): return re.sub(r'[^a-z]','',s.lower().replace('é','e').replace('è','e').replace('ô','o').replace('É','e'))
def cp(a,b):
    i=0
    while i<min(len(a),len(b)) and a[i]==b[i]: i+=1
    return i
def best(t):
    return max(SERVICES,key=lambda s:max(cp(norm(s),norm(t)),cp(norm(s).replace('service','').replace('desdes','des'),norm(t))))
ORG=[]
for n in range(9,58):
    q=qs[n]; meta=q['meta']; svc=best(q['q'])
    niv='Section' if meta.startswith('Section') else 'Direction' if meta.startswith('Direction') else 'Division'
    for i,o in enumerate(q['opts']): ORG.append((svc,niv,o,i+1))
SYNDICATS=qs[58]['opts']
CLASSES=qs[59]['opts']
SFMQ='Syndicat des fonctionnaires municipaux de Québec (SFMQ)'
TITRES=[]
def addt(s,c,n,prefix=''):
    for i,o in enumerate(qs[n]['opts']):
        if o=='Option 2': continue
        if o.startswith('Classe '): o='('+o
        TITRES.append((s,c,prefix+o,len(TITRES)+1))
for c,n in zip(CLASSES,range(60,65)): addt(SFMQ,c,n)
M={'Syndicat des employés manuels de la Ville de Québec (SEMVQ)':65,
'Alliance des professionnels et des professionnelles de la Ville de Québec (ALLPPVQ)':66,
'Association du personnel de direction de la Ville de Québec (APDVQ)':67,
"Union des commis de bar d'ExpoCité (FISA)":68,'Occasionnels Loisir (SFMQ)':69,
"Personnel de stationnement d'ExpoCité (CSN)":70,'Personnel aquatique (SCFP)':71,
'Alliance internationale des employés de scène et de théâtre (IATSÉ)':72,'Employé Non-syndiqué':73,'Autre':74}
for s,n in M.items():
    assert s in SYNDICATS,s
    addt(s,'',n)
addt('Employé Non-syndiqué','',75,'Occasionnels non syndiqués ExpoCité – ')
ADRESSES=qs[76]['opts']
if __name__=='__main__':
    from collections import Counter
    print(Counter((o[0],o[1]) for o in ORG))
    print(len(TITRES),len(ADRESSES),ADRESSES[-1], [s for s in SYNDICATS if s not in M and s!=SFMQ])
