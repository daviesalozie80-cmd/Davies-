import fs from 'fs';
import {feature} from 'topojson-client';
import {geoNaturalEarth1, geoPath, geoGraticule10} from 'd3-geo';
const W=2560,H=1440;
const topo=JSON.parse(fs.readFileSync('node_modules/world-atlas/land-50m.json'));
const land=feature(topo,topo.objects.land);
const proj=geoNaturalEarth1().fitExtent([[-40,40],[W+40,H+120]],{type:'Sphere'});
const path=geoPath(proj);
const b64=f=>fs.readFileSync(f).toString('base64');
const bebas=b64('node_modules/@fontsource/bebas-neue/files/bebas-neue-latin-400-normal.woff2');
const elite=b64('node_modules/@fontsource/special-elite/files/special-elite-latin-400-normal.woff2');
// one pin per continent [lon,lat]
const pins=[[-77,38.9],[-55,-24],[2.3,48.8],[27,-27],[105,35],[134,-25]];
const pinSvg=pins.map(([lo,la])=>{const [x,y]=proj([lo,la]);return `
<g transform="translate(${x.toFixed(1)},${y.toFixed(1)})">
 <circle r="46" fill="none" stroke="#d7263d" stroke-opacity=".25" stroke-width="3"/>
 <circle r="24" fill="none" stroke="#d7263d" stroke-opacity=".5" stroke-width="3"/>
 <ellipse cx="0" cy="2" rx="9" ry="4" fill="#000" opacity=".5"/>
 <path d="M0 0 C-6 -14 -18 -24 -18 -38 A18 18 0 1 1 18 -38 C18 -24 6 -14 0 0Z" fill="#d7263d"/>
 <circle cy="-38" r="7" fill="#0b1220"/>
</g>`}).join('');
// dashed route between pins
const pts=pins.map(p=>proj(p));
const route='M'+[pts[0],pts[1],pts[3],pts[2],pts[4],pts[5]].map(p=>p.map(v=>v.toFixed(1)).join(' ')).join(' L');
const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
<defs>
<style>
@font-face{font-family:'Bebas';src:url(data:font/woff2;base64,${bebas}) format('woff2');}
@font-face{font-family:'Elite';src:url(data:font/woff2;base64,${elite}) format('woff2');}
</style>
<radialGradient id="bg" cx="50%" cy="50%" r="75%"><stop offset="0" stop-color="#16213a"/><stop offset="1" stop-color="#070b14"/></radialGradient>
<radialGradient id="shade" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#070b14" stop-opacity=".92"/><stop offset=".6" stop-color="#070b14" stop-opacity=".7"/><stop offset="1" stop-color="#070b14" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="5" cy="5" r="2.2" fill="#e8d9b5"/></pattern>
</defs>
<rect width="${W}" height="${H}" fill="url(#bg)"/>
<path d="${path(geoGraticule10())}" fill="none" stroke="#e8d9b5" stroke-opacity=".06" stroke-width="1.5"/>
<path d="${path(land)}" fill="url(#dots)" opacity=".38"/>
<path d="${path(land)}" fill="none" stroke="#e8d9b5" stroke-opacity=".22" stroke-width="2"/>
<path d="${route}" fill="none" stroke="#d7263d" stroke-opacity=".55" stroke-width="3" stroke-dasharray="14 12"/>
${pinSvg}
<ellipse cx="${W/2}" cy="${H/2}" rx="820" ry="250" fill="url(#shade)"/>
<g text-anchor="middle">
 <text x="${W/2}" y="568" font-family="Elite" font-size="34" letter-spacing="10" fill="#d7263d">· CASE FILES FROM EVERY CONTINENT ·</text>
 <text x="${W/2}" y="790" font-family="Bebas" font-size="250" letter-spacing="16" fill="#f3ead6">THE HIDDEN MAP</text>
 <line x1="${W/2-560}" x2="${W/2+560}" y1="830" y2="830" stroke="#d7263d" stroke-width="4"/>
 <text x="${W/2}" y="900" font-family="Elite" font-size="54" fill="#e8d9b5">Every place has a secret.</text>
</g>
</svg>`;
fs.writeFileSync('banner.svg',svg);
