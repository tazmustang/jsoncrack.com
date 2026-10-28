const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/dc354050-1149-4e6f-a2b3-a0148470c5da_2ca9fe01-23e4-4ca1-9720-0b46d55a1fe7/pptx/scripts/apply_theme.js");

const OUT = process.argv[2];
const IMG = "/home/user/jsoncrack.com/powerapps";
const THEME = {
  name: "Ville RH",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1F2937", lt1: "FFFFFF", dk2: "00285E", lt2: "F3F5F9",
    accent1: "857650", accent2: "009E49", accent3: "074B98",
    accent4: "6B3FA0", accent5: "B91C1C", accent6: "6B7280",
    hlink: "074B98", folHlink: "6B3FA0",
  },
};
const HEX = THEME.colors;

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625
pres.author = "Annie Audet";
pres.title = "Appréciation de la contribution — du Word à l'application";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;

// ---------- layouts ----------
pres.defineSlideMaster({
  title: "TITRE",
  background: { color: C.text2 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.5, w: 8.8, h: 1.5, fontSize: 38, bold: true, color: C.background1, valign: "bottom" }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 3.15, w: 8.8, h: 1.2, fontSize: 18, color: "D9DEE8", valign: "top" }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "SECTION",
  background: { color: C.text2 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.9, w: 8.8, h: 1.0, fontSize: 36, bold: true, color: C.background1 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 2.95, w: 8.8, h: 0.8, fontSize: 16, color: "D9DEE8" }, text: "" } },
  ],
  slideNumber: { x: 9.2, y: 5.2, w: 0.5, h: 0.3, fontSize: 10, color: "D9DEE8" },
});
pres.defineSlideMaster({
  title: "CONTENU",
  background: { color: C.background1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.3, w: 9.0, h: 0.75, fontSize: 28, bold: true, color: C.text2, valign: "middle" }, text: "" } },
    { text: { text: "Appréciation de la contribution · Ressources humaines", options: { x: 0.5, y: 5.22, w: 6, h: 0.3, fontSize: 9, color: C.accent6 } } },
  ],
  slideNumber: { x: 9.2, y: 5.22, w: 0.4, h: 0.3, fontSize: 9, color: C.accent6 },
});

function contenu(section, titre) {
  const s = pres.addSlide({ masterName: "CONTENU", sectionTitle: section });
  s.addText(titre, { placeholder: "title" });
  return s;
}
function carte(s, x, y, w, h, fill, name) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: fill }, line: { color: fill }, rectRadius: 0.08, objectName: name });
}
function pastille(s, x, y, txt, fill, name) {
  s.addShape(pres.shapes.OVAL, { x, y, w: 0.46, h: 0.46, fill: { color: fill }, line: { color: fill }, objectName: name });
  s.addText(txt, { x, y, w: 0.46, h: 0.46, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0, isTextBox: true });
}

// ---------- 1. Titre ----------
pres.addSection({ title: "Introduction" });
let s = pres.addSlide({ masterName: "TITRE", sectionTitle: "Introduction" });
s.addText("Appréciation de la contribution : du formulaire Word à l'application numérique", { placeholder: "title" });
s.addText("Démarche, options évaluées, tests et résultat\nPrésenté par Annie Audet, conseillère en ressources humaines (RH-SST) — octobre 2026", { placeholder: "body" });
s.addNotes("Présenter l'objectif de la rencontre : faire le point sur la démarche, montrer le résultat et obtenir l'appui pour la mise en production.");

// ---------- 2. En bref ----------
s = contenu("Introduction", "En bref : où en sommes-nous");
const bref = [
  ["1", "Le besoin", "Remplacer les formulaires Word d'appréciation par un outil numérique sécurisé, avec circuit d'approbation.", C.accent1],
  ["2", "La démarche", "Deux approches construites et testées ; l'approche Power Apps a été retenue parce qu'elle est compatible avec notre SharePoint.", C.accent3],
  ["3", "Le résultat", "Application fonctionnelle et testée dans le bac à sable, documentée et prête pour la demande de mise en PréProd.", C.accent2],
];
bref.forEach(([n, t, d, col], i) => {
  const y = 1.3 + i * 1.22;
  carte(s, 0.5, y, 9.0, 1.05, C.background2, "bref" + i);
  pastille(s, 0.75, y + 0.29, n, col, "pastille" + i);
  s.addText(t, { x: 1.45, y: y + 0.12, w: 7.8, h: 0.35, fontSize: 16, bold: true, color: C.text2, margin: 0, isTextBox: true });
  s.addText(d, { x: 1.45, y: y + 0.47, w: 7.8, h: 0.5, fontSize: 14, color: C.text1, margin: 0, isTextBox: true });
});

// ---------- 3. Point de départ ----------
pres.addSection({ title: "Point de départ" });
s = contenu("Point de départ", "Le point de départ : un processus papier-courriel");
const irritants = [
  ["Versions multiples", "Le fichier Word circule par courriel ; on perd la bonne version."],
  ["Confidentialité", "Des copies d'évaluations restent dans les boîtes courriel et les ordinateurs."],
  ["Suivi difficile", "Impossible de savoir où en est une appréciation sans relancer."],
  ["Travail manuel", "Signatures, moyennes, synthèse et transmission aux RH faites à la main."],
];
irritants.forEach(([t, d], i) => {
  const x = 0.5 + (i % 2) * 4.6, y = 1.3 + Math.floor(i / 2) * 1.75;
  carte(s, x, y, 4.4, 1.55, "FDF2F2", "irritant" + i);
  s.addText(t, { x: x + 0.25, y: y + 0.18, w: 3.9, h: 0.4, fontSize: 17, bold: true, color: C.accent5, margin: 0, isTextBox: true });
  s.addText(d, { x: x + 0.25, y: y + 0.62, w: 3.9, h: 0.8, fontSize: 14, color: C.text1, margin: 0, isTextBox: true });
});
s.addNotes("Nouveaux formulaires du 15 octobre 2026 : cadre avec équipe, cadre sans équipe, professionnel non syndiqué. Le contenu ne change pas, c'est la façon de le remplir et de le faire circuler qui change.");

// ---------- 4. Objectifs et contraintes ----------
s = contenu("Point de départ", "Nos objectifs et nos contraintes");
carte(s, 0.5, 1.25, 4.4, 3.75, C.background2, "objectifs");
s.addText("Objectifs", { x: 0.75, y: 1.4, w: 4, h: 0.4, fontSize: 18, bold: true, color: C.text2, margin: 0, isTextBox: true });
s.addText([
  { text: "Intégrer les 3 formulaires du 15 octobre 2026", options: { bullet: true, breakLine: true } },
  { text: "Circuit : personne, supérieur immédiat, hiérarchique, directeur au besoin", options: { bullet: true, breakLine: true } },
  { text: "Courriels de suivi automatiques", options: { bullet: true, breakLine: true } },
  { text: "Transmission de l'évaluation globale aux RH", options: { bullet: true, breakLine: true } },
  { text: "PDF de l'appréciation complète", options: { bullet: true } },
], { x: 0.75, y: 1.9, w: 4.0, h: 3.0, fontSize: 14, color: C.text1, paraSpaceAfter: 6, valign: "top", isTextBox: true });
carte(s, 5.1, 1.25, 4.4, 3.75, "EEF6F1", "contraintes");
s.addText("Contraintes", { x: 5.35, y: 1.4, w: 4, h: 0.4, fontSize: 18, bold: true, color: C.accent2, margin: 0, isTextBox: true });
s.addText([
  { text: "Gratuit : aucune licence Premium", options: { bullet: true, breakLine: true } },
  { text: "Uniquement les outils Microsoft 365 de la Ville", options: { bullet: true, breakLine: true } },
  { text: "Accès limité aux seules personnes concernées", options: { bullet: true, breakLine: true } },
  { text: "Simple à utiliser, sans formation lourde", options: { bullet: true, breakLine: true } },
  { text: "Conforme au processus de mise en production des TI", options: { bullet: true } },
], { x: 5.35, y: 1.9, w: 4.0, h: 3.0, fontSize: 14, color: C.text1, paraSpaceAfter: 6, valign: "top", isTextBox: true });

// ---------- 5. Démarche (ligne du temps) ----------
pres.addSection({ title: "Démarche" });
s = pres.addSlide({ masterName: "SECTION", sectionTitle: "Démarche" });
s.addText("La démarche", { placeholder: "title" });
s.addText("Ce que nous avons construit, testé et pourquoi nous avons changé de cap", { placeholder: "body" });

s = contenu("Démarche", "Les grandes étapes du projet");
const etapes = [
  ["Formulaires", "Mise à jour des 3 formulaires (15 oct.)"],
  ["Prototype 1", "Application web HTML + listes SharePoint"],
  ["Tests SharePoint", "Blocages découverts dans notre SharePoint"],
  ["Réorientation", "Choix de Power Apps (outil Microsoft)"],
  ["Construction", "Application, 3 flux, 5 variables"],
  ["Tests", "Corrections et validation complète"],
  ["Mise en prod", "Documentation, dossier TI, communication"],
];
s.addShape(pres.shapes.LINE, { x: 0.75, y: 2.2, w: 8.5, h: 0, line: { color: HEX.accent6, width: 1.5 }, objectName: "ligneTemps" });
etapes.forEach(([t, d], i) => {
  const x = 0.5 + i * 1.29;
  const col = i === 3 ? C.accent2 : (i < 3 ? C.accent1 : C.accent3);
  pastille(s, x + 0.36, 1.97, String(i + 1), col, "etape" + i);
  s.addText(t, { x, y: 2.6, w: 1.2, h: 0.5, fontSize: 13, bold: true, color: C.text2, align: "center", margin: 0, isTextBox: true });
  s.addText(d, { x, y: 3.1, w: 1.2, h: 1.3, fontSize: 11, color: C.text1, align: "center", valign: "top", margin: 0, isTextBox: true });
});
s.addText("Étape 4 : le changement de cap, appuyé par les résultats des tests du prototype", { x: 0.5, y: 4.55, w: 9, h: 0.4, fontSize: 13, italic: true, color: C.accent2, margin: 0, isTextBox: true });

// ---------- 6. Options évaluées ----------
s = contenu("Démarche", "Les options évaluées");
const rows = [
  ["Critère", "Formulaire Word (actuel)", "Prototype HTML + SharePoint", "Power Apps + SharePoint (retenu)"],
  ["Fonctionne dans notre SharePoint", "Oui", "Non : aperçu bloqué, pas de page HTML autorisée", "Oui"],
  ["Coût / licences", "Aucun", "Aucun", "Aucun (connecteurs standard)"],
  ["Confidentialité", "Faible (copies par courriel)", "Bonne, mais dépôt par copier-coller", "Élevée (accès par dossier)"],
  ["Suivi et courriels automatiques", "Non", "Oui (4 flux, complexes)", "Oui (3 flux)"],
  ["Simplicité pour l'usager", "Connue, mais lourde", "Faible (étapes manuelles)", "Élevée"],
  ["Déploiement par les TI", "—", "Hors processus", "Solution gérée, processus TI standard"],
];
const cell = (t, i, j) => ({ text: t, options: {
  bold: i === 0 || j === 0, color: i === 0 ? C.background1 : (j === 3 && i > 0 ? C.accent2 : C.text1),
  fill: { color: i === 0 ? C.text2 : (j === 3 ? "EEF6F1" : (i % 2 ? C.background2 : C.background1)) },
  fontSize: 11, valign: "middle" } });
s.addTable(rows.map((r, i) => r.map((t, j) => cell(t, i, j))), { x: 0.5, y: 1.2, w: 9.0, colW: [2.1, 2.0, 2.45, 2.45], rowH: 0.48, border: { type: "solid", pt: 0.5, color: "D1D5DB" }, objectName: "tableauOptions" });

// ---------- 7. Leçons du prototype ----------
s = contenu("Démarche", "Ce que le prototype nous a appris");
const lecons = [
  ["Aperçu SharePoint restreint", "SharePoint exécute les pages HTML dans un mode protégé : sauvegarde locale et téléchargements bloqués."],
  ["Autorisations", "La publication de pages HTML personnalisées n'est pas permise dans notre environnement."],
  ["Contournements fragiles", "Le dépôt par copier-coller fonctionnait, mais demandait trop d'étapes manuelles aux usagers."],
  ["Décision", "Passer à Power Apps : outil Microsoft prévu pour ce besoin, encadré par le processus des TI."],
];
lecons.forEach(([t, d], i) => {
  const y = 1.25 + i * 0.95;
  const col = i === 3 ? C.accent2 : C.accent1;
  pastille(s, 0.55, y + 0.12, i === 3 ? "✓" : String(i + 1), col, "lecon" + i);
  s.addText(t, { x: 1.2, y: y, w: 8.2, h: 0.35, fontSize: 15, bold: true, color: i === 3 ? C.accent2 : C.text2, margin: 0, isTextBox: true });
  s.addText(d, { x: 1.2, y: y + 0.36, w: 8.2, h: 0.5, fontSize: 13, color: C.text1, margin: 0, isTextBox: true });
});
s.addNotes("Le prototype n'a pas été du temps perdu : il a servi à valider le contenu des formulaires, les règles d'accès par rôle et le circuit d'approbation, qui ont été repris tels quels dans Power Apps.");

// ---------- 8. Solution retenue ----------
pres.addSection({ title: "Solution" });
s = pres.addSlide({ masterName: "SECTION", sectionTitle: "Solution" });
s.addText("La solution retenue", { placeholder: "title" });
s.addText("Power Apps, SharePoint et Power Automate — tout dans Microsoft 365 de la Ville", { placeholder: "body" });

s = contenu("Solution", "L'architecture en un coup d'œil");
s.addImage({ path: IMG + "/schema/Schema-solution.png", x: 0.9, y: 1.12, w: 8.2, h: 8.2 * 1498 / 3112, altText: "Schéma : application Power Apps, listes SharePoint et 3 flux Power Automate", objectName: "schemaSolution" });

s = contenu("Solution", "Le circuit d'une appréciation");
s.addImage({ path: IMG + "/communication/1-Circuit-des-etapes.png", x: 1.35, y: 1.1, w: 7.3, h: 7.3 * 1754 / 3200, altText: "Circuit en 7 étapes, rôle par rôle", objectName: "schemaCircuit" });

// ---------- 9. Tests ----------
pres.addSection({ title: "Tests" });
s = contenu("Tests", "Tests et validation : les chiffres");
const stats = [["15", "scénarios de test définis"], ["23", "ajustements apportés au guide de construction"], ["3", "flux automatisés validés"], ["4", "rôles testés (personne, SI, SH, directeur)"]];
stats.forEach(([n, t], i) => {
  const x = 0.5 + i * 2.28;
  carte(s, x, 1.35, 2.1, 1.9, C.text2, "stat" + i);
  s.addText(n, { x, y: 1.5, w: 2.1, h: 0.9, fontSize: 44, bold: true, color: "FFD98A", align: "center", margin: 0, isTextBox: true });
  s.addText(t, { x: x + 0.15, y: 2.4, w: 1.8, h: 0.75, fontSize: 13, color: C.background1, align: "center", valign: "top", margin: 0, isTextBox: true });
});
s.addText("Chaque problème rencontré a été documenté avec sa cause et sa solution, pour faciliter l'entretien futur.", { x: 0.5, y: 3.6, w: 9, h: 0.5, fontSize: 14, italic: true, color: C.text2, margin: 0, isTextBox: true });

s = contenu("Tests", "Ce que les tests ont permis de corriger");
const corr = [
  ["Données", "Colonne « Type de rencontre » à choix multiples, index ajustés, sources de données renommées."],
  ["Formules", "Lecture des dossiers enregistrés, cases à cocher, synthèse des cotes, mise en page."],
  ["Flux", "Noms des variables d'environnement, ordre des étapes, tolérance aux cas normaux."],
  ["Accès", "Autorisations de la liste resserrées : chaque dossier n'est visible que par ses personnes et les RH."],
  ["PDF", "PDF complet joint au dossier (une seule version, mêmes accès) ; écran allégé."],
];
corr.forEach(([t, d], i) => {
  const y = 1.2 + i * 0.78;
  carte(s, 0.5, y, 9.0, 0.66, i % 2 ? C.background1 : C.background2, "corr" + i);
  s.addText(t, { x: 0.7, y, w: 1.4, h: 0.66, fontSize: 15, bold: true, color: C.accent3, valign: "middle", margin: 0, isTextBox: true });
  s.addText(d, { x: 2.15, y, w: 7.2, h: 0.66, fontSize: 13, color: C.text1, valign: "middle", margin: 0, isTextBox: true });
});

// ---------- 10. Sécurité ----------
s = contenu("Tests", "Confidentialité : vérifiée dossier par dossier");
carte(s, 0.5, 1.2, 5.3, 3.8, C.background2, "securite");
s.addText([
  { text: "Chaque dossier est automatiquement réservé à la personne, à ses supérieurs, au directeur si requis et aux RH", options: { bullet: true, breakLine: true } },
  { text: "Un collègue ne voit jamais le dossier d'un autre (testé)", options: { bullet: true, breakLine: true } },
  { text: "Les courriels ne contiennent aucune évaluation, seulement un lien", options: { bullet: true, breakLine: true } },
  { text: "À la fin, le dossier passe en lecture seule pour tous", options: { bullet: true, breakLine: true } },
  { text: "Le PDF est joint au dossier, avec les mêmes accès", options: { bullet: true } },
], { x: 0.75, y: 1.4, w: 4.85, h: 3.4, fontSize: 14, color: C.text1, paraSpaceAfter: 8, valign: "top", isTextBox: true });
carte(s, 6.05, 1.2, 3.45, 3.8, "FBF6EA", "aFaire");
s.addText("À compléter avant la Prod", { x: 6.25, y: 1.35, w: 3.1, h: 0.4, fontSize: 15, bold: true, color: C.accent1, margin: 0, isTextBox: true });
s.addText([
  { text: "Évaluation des facteurs relatifs à la vie privée (EFVP)", options: { bullet: true, breakLine: true } },
  { text: "Délai de conservation (gestion documentaire)", options: { bullet: true, breakLine: true } },
  { text: "Compte de service et personne suppléante", options: { bullet: true } },
], { x: 6.25, y: 1.85, w: 3.1, h: 3.0, fontSize: 13, color: C.text1, paraSpaceAfter: 8, valign: "top", isTextBox: true });

// ---------- 11. Avantages ----------
pres.addSection({ title: "Résultat" });
s = contenu("Résultat", "Pourquoi l'application plutôt que le Word");
s.addImage({ path: IMG + "/communication/4-Avantages-vs-Word.png", x: 0.5, y: 1.15, w: 9.0, h: 9.0 * 1306 / 3200, altText: "Comparaison avant (Word) et maintenant (application)", objectName: "avantages" });

s = contenu("Résultat", "Ce qui est livré");
const livr = [
  ["Application", "Formulaire complet, 3 types de poste, barre d'étapes, PDF joint au dossier"],
  ["Automatisation", "3 flux : accès, suivi et courriels, production du PDF"],
  ["Documentation", "Guide de mise en production, formules et flux de référence, dossier TI"],
  ["Déploiement", "Fichier des variables d'environnement, liste de vérification des TI"],
  ["Communication", "Guide d'utilisation, message d'annonce, schémas opérationnels"],
];
livr.forEach(([t, d], i) => {
  const x = 0.5 + (i % 3) * 3.05, y = 1.25 + Math.floor(i / 3) * 1.95;
  carte(s, x, y, 2.85, 1.75, C.background2, "livrable" + i);
  s.addText(t, { x: x + 0.2, y: y + 0.15, w: 2.45, h: 0.4, fontSize: 16, bold: true, color: C.accent3, margin: 0, isTextBox: true });
  s.addText(d, { x: x + 0.2, y: y + 0.6, w: 2.45, h: 1.05, fontSize: 13, color: C.text1, valign: "top", margin: 0, isTextBox: true });
});

// ---------- 12. Prochaines étapes ----------
s = contenu("Résultat", "Prochaines étapes et décisions demandées");
const next = [
  ["Demande de mise en PréProd aux TI", "formulaire, solution gérée et fichier des variables"],
  ["Tests en PréProd", "avec 4 comptes, procès-verbal"],
  ["EFVP et conservation", "responsable PRP et gestion documentaire"],
  ["Mise en production", "puis annonce et courte démonstration aux gestionnaires"],
];
next.forEach(([t, d], i) => {
  const y = 1.25 + i * 0.72;
  pastille(s, 0.55, y + 0.04, String(i + 1), C.accent3, "suite" + i);
  s.addText([{ text: t, options: { bold: true, color: C.text2 } }, { text: " — " + d, options: { color: C.text1 } }], { x: 1.2, y, w: 5.0, h: 0.55, fontSize: 14, valign: "middle", margin: 0, isTextBox: true });
});
carte(s, 6.45, 1.2, 3.05, 3.0, C.text2, "decisions");
s.addText("Nous demandons", { x: 6.65, y: 1.35, w: 2.7, h: 0.4, fontSize: 16, bold: true, color: "FFD98A", margin: 0, isTextBox: true });
s.addText([
  { text: "Votre appui pour la mise en production", options: { bullet: true, breakLine: true } },
  { text: "Une date cible", options: { bullet: true, breakLine: true } },
  { text: "Une personne suppléante", options: { bullet: true, breakLine: true } },
  { text: "Des testeurs gestionnaires", options: { bullet: true } },
], { x: 6.65, y: 1.85, w: 2.7, h: 2.2, fontSize: 14, color: C.background1, paraSpaceAfter: 6, valign: "top", isTextBox: true });

// ---------- 13. Fin ----------
s = pres.addSlide({ masterName: "TITRE", sectionTitle: "Résultat" });
s.addText("Merci — questions et démonstration", { placeholder: "title" });
s.addText("Annie Audet, Ressources humaines (RH-SST)\nAppuis : documentation Microsoft Power Platform et équipe des TI (processus de mise en production)", { placeholder: "body" });

pres.writeFile({ fileName: OUT }).then(() => applyTheme(OUT, THEME)).then(() => console.log("écrit", OUT));
