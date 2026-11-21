const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [svg, out, w, h, scale] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:+w,height:+h}, deviceScaleFactor:+(scale||1)});
  await p.goto('file://' + path.resolve(svg)); await p.waitForTimeout(400);
  await p.screenshot({path: out}); await b.close();
})();
