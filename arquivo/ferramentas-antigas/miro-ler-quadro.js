const {chromium}=require('playwright');
(async()=>{const out=process.argv[2];const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1600,height:1000},deviceScaleFactor:2});
await pg.goto('https://miro.com/app/board/uXjVH0FzMVY=/?share_link_id=553889528753',{waitUntil:'domcontentloaded',timeout:60000});
await pg.waitForTimeout(18000);
const zoom=async()=>pg.evaluate(()=>{const els=[...document.querySelectorAll('*')].filter(e=>e.children.length===0&&/^[\d,.]+%$/.test(e.textContent.trim()));return els.length?parseFloat(els[els.length-1].textContent.trim().replace(',','')):0});
try{await pg.getByText('Fit to screen').first().click({timeout:5000});}catch(e){await pg.keyboard.press('Shift+1');}
await pg.waitForTimeout(4000);
await pg.mouse.move(915,222);
let z=await zoom();
for(let i=0;i<100&&z<95;i++){await pg.keyboard.down('Control');await pg.mouse.wheel(0,-6);await pg.keyboard.up('Control');await pg.waitForTimeout(200);z=await zoom();}
console.log('zoom',z);
await pg.waitForTimeout(2000);
await pg.mouse.move(1000,500);await pg.mouse.down();await pg.mouse.move(250,450,{steps:20});await pg.mouse.up();
await pg.waitForTimeout(2000);
for(let k=0;k<8;k++){await pg.screenshot({path:out+'/d'+k+'.png'});await pg.mouse.move(1200,900);await pg.mouse.down();await pg.mouse.move(1200,150,{steps:25});await pg.mouse.up();await pg.waitForTimeout(2000);}
await b.close();})();
