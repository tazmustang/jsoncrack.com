# Crée diagramme-sequence.drawio (formes modifiables) à partir des étapes de generer-sequence.py
import re,html
src=open('generer-sequence.py').read()
ns={}; exec(src.split('W=1560')[0],ns)
L,steps=ns['L'],ns['steps']; P,SI,SH,DIR,APP,SP,PA,RH=range(8)
lw=190; top=90; dy=44; W=lw*len(L)
xs=[lw*i+lw/2 for i in range(len(L))]
cells=[]; cid=[2]
def nid():
    cid[0]+=1; return f"c{cid[0]}"
def esc(t): return html.escape(t,quote=True)
def box(x,y,w,h,val,style):
    i=nid(); cells.append(f'<mxCell id="{i}" value="{esc(val)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>'); return i
def edge(x1,y1,x2,y2,val,dashed):
    i=nid(); st=f"endArrow=block;endFill=1;html=1;strokeWidth=2;fontSize=11;labelBackgroundColor=#FFFFFF;strokeColor={'#8A8C8E' if dashed else '#00285E'};"+("dashed=1;" if dashed else "")
    cells.append(f'<mxCell id="{i}" value="{esc(val)}" style="{st}" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="{x1:.0f}" y="{y1:.0f}" as="sourcePoint"/><mxPoint x="{x2:.0f}" y="{y2:.0f}" as="targetPoint"/></mxGeometry></mxCell>')
box(10,10,900,30,"Appréciation de la contribution (SRHVQ) — diagramme de séquence · version 1.0.0.9","text;fontSize=18;fontStyle=1;fontColor=#00285E;align=left;")
y=top+70; alt=None
for s in steps:
    k=s[0]
    if k=="sec": y+=10; box(10,y-14,W-20,24,s[1],"rounded=1;fillColor=#E8EDF5;strokeColor=none;fontStyle=1;fontColor=#00285E;align=left;spacingLeft=8;"); y+=dy-4
    elif k in("m","r"): edge(xs[s[1]],y,xs[s[2]],y,s[3],k=="r"); y+=dy
    elif k=="self": box(xs[s[1]]-330,y-12,320,26,s[2],"text;fontSize=11;align=right;"); edge(xs[s[1]],y-6,xs[s[1]],y+8,"",False); y+=dy
    elif k=="note": box(xs[s[1]]-70,y-14,xs[s[2]]-xs[s[1]]+140,26,s[3],"rounded=1;fillColor=#FFF7E6;strokeColor=#E0B060;fontColor=#92400E;"); y+=dy
    elif k=="alt": alt=(y-16,s[1]); y+=30
    elif k=="altend": y0,t=alt; box(xs[DIR]-lw/2+10,y0,xs[SP]-xs[DIR]+lw/2,y-y0-12,"alt : "+t,"rounded=1;fillColor=none;dashed=1;strokeColor=#8A8C8E;verticalAlign=top;align=left;spacingLeft=6;fontStyle=2;fontSize=11;"); y+=8
H=y+20
for i,n in enumerate(L):
    box(xs[i]-lw/2+8,top,lw-16,52,n.replace("\n"," "),"rounded=1;fillColor=#00285E;fontColor=#FFFFFF;fontStyle=1;strokeColor=none;whiteSpace=wrap;")
    i2=nid(); cells.insert(0,f'<mxCell id="{i2}" style="endArrow=none;dashed=1;strokeColor=#C9CDD3;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="{xs[i]:.0f}" y="{top+52}" as="sourcePoint"/><mxPoint x="{xs[i]:.0f}" y="{H}" as="targetPoint"/></mxGeometry></mxCell>')
xml=f'<mxfile host="app.diagrams.net"><diagram name="Séquence SRHVQ"><mxGraphModel dx="1600" dy="1600" grid="0" page="1" pageWidth="{W+40}" pageHeight="{H+40}"><root><mxCell id="0"/><mxCell id="1" parent="0"/>{"".join(cells)}</root></mxGraphModel></diagram></mxfile>'
open("diagramme-sequence.drawio","w").write(xml); print(len(cells),"formes")
