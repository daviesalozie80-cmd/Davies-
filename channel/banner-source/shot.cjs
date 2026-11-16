const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2560,height:1440}});
await p.goto('file://'+__dirname+'/banner.svg');await p.waitForTimeout(500);
await p.screenshot({path:'banner.png'});await b.close();})();
