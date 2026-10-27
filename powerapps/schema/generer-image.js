const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
  const p = await (await b.newContext({viewport:{width:1556,height:500}, deviceScaleFactor:2})).newPage();
  await p.goto('file:///home/user/jsoncrack.com/powerapps/schema/schema-solution.html');
  await p.screenshot({path:'/home/user/jsoncrack.com/powerapps/schema/Schema-solution.png', fullPage:true});
  await b.close(); })();
