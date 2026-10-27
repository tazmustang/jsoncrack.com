const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
  const p = await (await b.newContext({viewport:{width:1600,height:400}, deviceScaleFactor:2})).newPage();
  await p.goto('file:///home/user/jsoncrack.com/powerapps/communication/schemas-operationnels.html');
  const noms=['1-Circuit-des-etapes','2-Qui-remplit-quoi','3-En-coulisses','4-Avantages-vs-Word'];
  for(let i=0;i<4;i++){
    await p.evaluate(i=>document.querySelectorAll('section.page').forEach((s,j)=>s.style.display = j===i ? '' : 'none'), i);
    await p.screenshot({path:`/home/user/jsoncrack.com/powerapps/communication/${noms[i]}.png`, fullPage:true});
  }
  await b.close(); })();
