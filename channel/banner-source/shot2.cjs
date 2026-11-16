const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:800,height:800}});
await p.goto('file://'+__dirname+'/pfp.svg');await p.screenshot({path:'pfp.png'});
const d='data:image/png;base64,'+fs.readFileSync(__dirname+'/pfp.png').toString('base64');
await p.goto('about:blank');await p.setViewportSize({width:300,height:140});
await p.setContent(`<body style="margin:0;background:#fff;display:flex;align-items:center;gap:20px;padding:20px"><img src="${d}" style="width:98px;border-radius:50%"><img src="${d}" style="width:40px;border-radius:50%"><div style="background:#0f0f0f;padding:6px"><img src="${d}" style="width:88px;border-radius:50%;display:block"></div></body>`);
await p.waitForTimeout(300);await p.screenshot({path:'pfp-preview.png'});await b.close();})();
