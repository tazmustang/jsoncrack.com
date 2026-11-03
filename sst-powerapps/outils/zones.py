# -*- coding: utf-8 -*-
"""Schéma corporel : zones cliquables (repris du prototype HTML), correspondance avec la liste « Partie du corps »."""

# (id_face, libellé_face, partie_face, id_dos, libellé_dos, partie_dos, côté, forme_svg, bbox x,y,w,h)
_Z = [
    ('thorax', 'Thorax / poitrine', 'Poitrine/thorax', 'hautDos', 'Haut du dos', 'Dos', 'Non applicable', "path d='M72,76 L128,76 L121,150 L79,150 Z'", (72, 76, 56, 74)),
    ('abdomen', 'Abdomen', 'Abdomen', 'basDos', 'Bas du dos / lombaires', 'Dos', 'Non applicable', "path d='M79,150 L121,150 L116,183 L84,183 Z'", (79, 150, 42, 33)),
    ('tete', 'Tête', 'Tête', 'crane', 'Arrière de la tête', 'Tête', 'Non applicable', "ellipse cx='100' cy='38' rx='19' ry='21'", (81, 17, 38, 42)),
    ('cou', 'Cou / gorge', 'Gorge', 'nuque', 'Nuque', 'Nuque', 'Non applicable', "path d='M92,58 L108,58 L106,74 L94,74 Z'", (92, 58, 16, 17)),
    ('brasG', 'Bras gauche', 'Bras', 'brasGdos', 'Bras gauche', 'Bras', 'Gauche', "rect x='45' y='95' width='17' height='48' rx='8.5'", (45, 95, 17, 44)),
    ('brasD', 'Bras droit', 'Bras', 'brasDdos', 'Bras droit', 'Bras', 'Droit', "rect x='138' y='95' width='17' height='48' rx='8.5'", (138, 95, 17, 44)),
    ('epauleG', 'Épaule gauche', 'Épaule', 'epauleGdos', 'Épaule gauche', 'Épaule', 'Gauche', "circle cx='64' cy='88' r='13'", (51, 75, 26, 26)),
    ('epauleD', 'Épaule droite', 'Épaule', 'epauleDdos', 'Épaule droite', 'Épaule', 'Droit', "circle cx='136' cy='88' r='13'", (123, 75, 26, 26)),
    ('coudeG', 'Coude gauche', 'Coude', 'coudeGdos', 'Coude gauche', 'Coude', 'Gauche', "circle cx='53.5' cy='147' r='9'", (44, 138, 19, 18)),
    ('coudeD', 'Coude droit', 'Coude', 'coudeDdos', 'Coude droit', 'Coude', 'Droit', "circle cx='146.5' cy='147' r='9'", (137, 138, 19, 18)),
    ('avantbrasG', 'Avant-bras gauche', 'Avant-bras', 'avantbrasGdos', 'Avant-bras gauche', 'Avant-bras', 'Gauche', "rect x='45' y='156' width='15' height='45' rx='7.5'", (45, 156, 15, 43)),
    ('avantbrasD', 'Avant-bras droit', 'Avant-bras', 'avantbrasDdos', 'Avant-bras droit', 'Avant-bras', 'Droit', "rect x='140' y='156' width='15' height='45' rx='7.5'", (140, 156, 15, 43)),
    ('mainG', 'Main gauche', 'Main', 'mainGdos', 'Main gauche', 'Main', 'Gauche', "ellipse cx='52.5' cy='212' rx='10' ry='13'", (42, 199, 21, 26)),
    ('mainD', 'Main droite', 'Main', 'mainDdos', 'Main droite', 'Main', 'Droit', "ellipse cx='147.5' cy='212' rx='10' ry='13'", (137, 199, 21, 26)),
    ('hancheG', 'Hanche / bassin gauche', 'Hanche', 'fessierG', 'Fessier gauche', 'Fessier', 'Gauche', "path d='M84,183 L100,183 L102,215 L80,215 Z'", (80, 183, 20, 32)),
    ('hancheD', 'Hanche / bassin droit', 'Hanche', 'fessierD', 'Fessier droit', 'Fessier', 'Droit', "path d='M100,183 L116,183 L120,215 L98,215 Z'", (100, 183, 20, 32)),
    ('cuisseG', 'Cuisse gauche', 'Cuisse', 'cuisseGdos', 'Arrière cuisse gauche', 'Cuisse', 'Gauche', "rect x='79' y='215' width='19' height='70' rx='9.5'", (79, 215, 19, 65)),
    ('cuisseD', 'Cuisse droite', 'Cuisse', 'cuisseDdos', 'Arrière cuisse droite', 'Cuisse', 'Droit', "rect x='102' y='215' width='19' height='70' rx='9.5'", (102, 215, 19, 65)),
    ('genouG', 'Genou gauche', 'Genou', 'genouGdos', 'Genou gauche', 'Genou', 'Gauche', "circle cx='88.5' cy='290' r='10'", (78, 280, 21, 20)),
    ('genouD', 'Genou droit', 'Genou', 'genouDdos', 'Genou droit', 'Genou', 'Droit', "circle cx='111.5' cy='290' r='10'", (101, 280, 21, 20)),
    ('jambeG', 'Jambe gauche', 'Jambes', 'molletG', 'Mollet gauche', 'Jambes', 'Gauche', "rect x='80' y='300' width='17' height='60' rx='8.5'", (80, 300, 17, 57)),
    ('jambeD', 'Jambe droite', 'Jambes', 'molletD', 'Mollet droit', 'Jambes', 'Droit', "rect x='103' y='300' width='17' height='60' rx='8.5'", (103, 300, 17, 57)),
    ('chevilleG', 'Cheville gauche', 'Cheville', 'chevilleGdos', 'Cheville gauche', 'Cheville', 'Gauche', "circle cx='88.5' cy='365' r='8'", (80, 357, 17, 16)),
    ('chevilleD', 'Cheville droite', 'Cheville', 'chevilleDdos', 'Cheville droite', 'Cheville', 'Droit', "circle cx='111.5' cy='365' r='8'", (103, 357, 17, 16)),
    ('piedG', 'Pied gauche', 'Pied', 'talonG', 'Talon gauche', 'Pied', 'Gauche', "ellipse cx='86' cy='384' rx='13' ry='8'", (73, 376, 26, 16)),
    ('piedD', 'Pied droit', 'Pied', 'talonD', 'Talon droit', 'Pied', 'Droit', "ellipse cx='114' cy='384' rx='13' ry='8'", (101, 376, 26, 16)),
]

ZONES = [dict(f=z[0], d=z[3], x=z[8][0], y=z[8][1], w=z[8][2], h=z[8][3]) for z in _Z]


def tzones_expr():
    recs = []
    for z in _Z:
        recs.append('{Id: "%s", Libelle: "%s", Partie: "%s", Cote: "%s"}' % (z[0], z[1], z[2], z[6]))
        recs.append('{Id: "%s", Libelle: "%s", Partie: "%s", Cote: "%s"}' % (z[3], z[4], z[5], z[6]))
    return 'Table(\n  ' + ',\n  '.join(recs) + ')'


def svg_expr():
    parts = ['"data:image/svg+xml;utf8," & EncodeUrl(',
             '"<svg xmlns=\'http://www.w3.org/2000/svg\' width=\'200\' height=\'400\' viewBox=\'0 0 200 400\'>" &',
             '"<rect width=\'200\' height=\'400\' fill=\'white\'/>" &',
             '"<text x=\'100\' y=\'11\' text-anchor=\'middle\' font-family=\'Segoe UI,Arial\' font-size=\'10\' fill=\'#6B7280\'>" & If(varVue = "face", "Vue de face", "Vue de dos") & "</text>" &',
             '"<text x=\'30\' y=\'60\' font-family=\'Segoe UI,Arial\' font-size=\'12\' font-weight=\'bold\' fill=\'#00285E\'>G</text><text x=\'162\' y=\'60\' font-family=\'Segoe UI,Arial\' font-size=\'12\' font-weight=\'bold\' fill=\'#00285E\'>D</text>" &']
    for z in _Z:
        zid = 'If(varVue = "face", "%s", "%s")' % (z[0], z[3])
        fill = 'If(varB1Zone = %s, "%%23C80000", varB2Zone = %s, "%%23857650", "%%23ECF1F7")' % (zid, zid)
        # EncodeUrl encode # ; on écrit donc les couleurs en clair dans la chaîne avant encodage
        fill = 'If(varB1Zone = %s, "#C80000", varB2Zone = %s, "#857650", "#ECF1F7")' % (zid, zid)
        parts.append('"<%s fill=\'" & %s & "\' stroke=\'#6B7280\' stroke-width=\'1\'/>" &' % (z[7], fill))
    parts.append('"</svg>")')
    return '\n'.join(parts)
