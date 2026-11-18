import fs from 'fs';
import {geoNaturalEarth1, geoPath, geoOrthographic, geoGraticule10} from 'd3-geo';
import {feature, mesh} from 'topojson-client';
const topo = JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-110m.json'));
const countries = feature(topo, topo.objects.countries);
countries.features = countries.features.filter(f => f.properties.name !== 'Antarctica');
const borders = mesh(topo, topo.objects.countries, (a,b)=>a!==b);
// Banner map: full width, slightly larger than canvas
const proj = geoNaturalEarth1().fitExtent([[-40,140],[2600,1480]], countries);
const p = geoPath(proj);
const hubs = {Shanghai:[121.5,31.2], Singapore:[103.8,1.3], Rotterdam:[4.5,51.9], NewYork:[-74,40.7], LosAngeles:[-118.2,33.7], Dubai:[55.3,25.2], Santos:[-46.3,-23.9], Lagos:[3.4,6.5], Mumbai:[72.8,19], Tokyo:[139.7,35.7], Sydney:[151.2,-33.9], Houston:[-95.4,29.8]};
const P = Object.fromEntries(Object.entries(hubs).map(([k,v])=>[k,proj(v).map(x=>+x.toFixed(1))]));
// Profile globe (orthographic centred on Atlantic/Europe-Africa)
const og = geoOrthographic().rotate([-15,-20]).fitExtent([[112,112],[912,912]], {type:'Sphere'});
const op = geoPath(og);
const out = {land: p(countries), borders: p(borders), hubs: P,
  globeLand: op(countries), globeGrat: op(geoGraticule10()), globeSphere: op({type:'Sphere'}),
  globeHubs: Object.fromEntries(Object.entries(hubs).map(([k,v])=>[k, og(v)]))};
fs.writeFileSync('map.json', JSON.stringify(out));
console.log(Object.keys(out), out.land.length, P);
