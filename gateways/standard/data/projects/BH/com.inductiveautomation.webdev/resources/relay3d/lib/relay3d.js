// HLCO Safety Relay 3D: Allen-Bradley Guardmaster 440C-CR30-22BBB + 440C-ENET + 2080-IQ4-OB4 plug-ins, read only.
// Source: .cursor/tasks/safety-relay-3d/src/relay3d.js -> copied by build.py into the WebDev resource relay3d/lib.
// docs/safety-relay-3d.md. Units: millimetres (1 scene unit = 1 mm). Dimensions / layout: Rockwell 440C-UM001
// (CR30 100 x 90 x 80 mm, terminal assignments table 2, status LED table 19, 440C-ENET indicators). Geometry plus
// procedural canvas textures only (no product photos). Nothing here writes anything: it polls GET state every 2 s.
import * as THREE from 'three';
import { OrbitControls } from '/system/webdev/BH/rack3d/lib/OrbitControls.js';
import { RoomEnvironment } from '/system/webdev/BH/rack3d/lib/RoomEnvironment.js';

const qs = new URLSearchParams(location.search);
const DEVICE = /^[A-Za-z0-9 _-]{1,60}$/.test(qs.get('device') || '') ? qs.get('device') : 'HLCO Safety Relay';
const PLC = /^[A-Za-z0-9_-]{1,40}$/.test(qs.get('plc') || '') ? qs.get('plc') : 'RCP1';
const DARK = document.documentElement.getAttribute('data-theme') === 'dark';
const DEMO = qs.get('demo') === '1';
const POLL_MS = 2000;
const $ = (id) => document.getElementById(id);

// ------------------------------------------------------------------ real dimensions (mm), 440C-UM001 Figure 3 / 4
const W = 100, H = 90, D = 80;     // housing incl. terminal blocks (DIN rail mounting, without feet / latch)
const FACE_Z = 62;                 // recessed centre band (LEDs, plug-ins); terminal blocks stand proud to z = D
const BAND = 58;                   // height of the centre band
const PITCH = 7.0;                 // terminal pitch (12 per row)
const PI_W = 31.5, PI_H = BAND;    // Micro800 plug-in module footprint
const PI_FRONT = 78;               // plug-in front face z
const SCENE_W = 300;

const THEME = DARK
  ? { bg: 0x161a1d, panel: 0x23282c, duct: 0x8c8982, ductCover: 0xa19e96, slot: '#2b3034', hemiSky: 0x9fb3c8, hemiGround: 0x1b1e21,
      hemi: 0.55, sun: 2.1, env: 0.55, hover: 0x53baed, sel: 0x3cb371 }
  : { bg: 0xe6e9ec, panel: 0xa9b0b6, duct: 0xd9d5cc, ductCover: 0xe8e4db, slot: '#9aa0a6', hemiSky: 0xffffff, hemiGround: 0x8a8f94,
      hemi: 0.6, sun: 2.1, env: 0.55, hover: 0x114599, sel: 0x228b22 };
const LED = { on: new THREE.Color(0x2ee66b), off: new THREE.Color(DARK ? 0x4a5055 : 0x5d6368),
  fault: new THREE.Color(0xff3b30), amber: new THREE.Color(0xffb000) };

// ------------------------------------------------------------------ renderer (graceful without WebGL)
function webglOk() {
  try {
    const c = document.createElement('canvas');
    return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl')));
  } catch (e) { return false; }
}
let renderer;
if (webglOk()) {
  try { renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' }); }
  catch (e) { renderer = null; }
}
if (!renderer) {
  $('nogl').hidden = false;
  $('bar').hidden = true;
  throw new Error('relay3d: WebGL unavailable');
}
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = DARK ? 1.0 : 0.92;
$('stage').appendChild(renderer.domElement);
const ANISO = Math.min(8, renderer.capabilities.getMaxAnisotropy());

const scene = new THREE.Scene();
scene.background = new THREE.Color(THEME.bg);
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
scene.environmentIntensity = THEME.env;
const camera = new THREE.PerspectiveCamera(32, 1, 5, 20000);
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; controls.dampingFactor = 0.12;
controls.minDistance = 90; controls.maxDistance = 3000;
controls.maxPolarAngle = Math.PI * 0.92; controls.screenSpacePanning = true;
scene.add(new THREE.HemisphereLight(THEME.hemiSky, THEME.hemiGround, THEME.hemi));
const sun = new THREE.DirectionalLight(0xffffff, THEME.sun);
sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048);
sun.shadow.bias = -0.0004; sun.shadow.normalBias = 0.6; sun.shadow.radius = 4;
sun.position.set(120, 330, 520); sun.target.position.set(0, 0, 0);
{ const sc = sun.shadow.camera; sc.left = -230; sc.right = 230; sc.top = 230; sc.bottom = -230; sc.near = 50; sc.far = 2000; sc.updateProjectionMatrix(); }
scene.add(sun, sun.target);

// ------------------------------------------------------------------ materials
const BOX = new THREE.BoxGeometry(1, 1, 1);
const PLANE = new THREE.PlaneGeometry(1, 1);
const std = (color, rough = 0.6, metal = 0.05, extra = {}) =>
  new THREE.MeshStandardMaterial(Object.assign({ color, roughness: rough, metalness: metal }, extra));
const M = {
  red: std(0xb7141b, 0.5),            // the CR30 housing is red (safety device; 440C-UM001 p. 11)
  redDark: std(0x8f1016, 0.55),
  block: std(0x2c2f33, 0.7),          // removable terminal blocks
  grey: std(0x9aa1a7, 0.55),          // Micro800 plug-in housings
  tab: std(0x4b5055, 0.65), latch: std(0x5d6369, 0.55),
  rail: std(0xc7cbcf, 0.3, 0.85), panel: std(THEME.panel, 0.5, 0.5),
  metal: std(0xb8bdc2, 0.35, 0.9), gold: std(0xd4a935, 0.3, 0.9), dark: std(0x16181a, 0.8),
};
const LED_GEO = new THREE.BoxGeometry(2.6, 1.8, 0.8);
const LED_MAT = new THREE.MeshBasicMaterial({ color: 0xffffff, toneMapped: false });
const SCREW_GEO = new THREE.CylinderGeometry(1.8, 1.8, 1.2, 24).rotateX(Math.PI / 2);
function screwTex(bump, flat) {
  const c = document.createElement('canvas'); c.width = c.height = 128;
  const g = c.getContext('2d');
  g.fillStyle = bump ? '#c8c8c8' : '#b9bec3'; g.fillRect(0, 0, 128, 128);
  g.fillStyle = bump ? '#000' : '#2a2d30';
  if (flat) g.fillRect(6, 53, 116, 22);
  else { g.fillRect(53, 20, 22, 88); g.fillRect(20, 53, 88, 22); g.beginPath(); g.arc(64, 64, 17, 0, 7); g.fill(); }
  const t = new THREE.CanvasTexture(c); t.colorSpace = bump ? THREE.NoColorSpace : THREE.SRGBColorSpace; t.anisotropy = 4; return t;
}
const SCREW_SIDE = new THREE.MeshStandardMaterial({ color: 0xb4b9be, roughness: 0.35, metalness: 0.9 });
function screwMats(type) {   // phillips (default) or flat, a Designer-only setting (docs/safety-relay-3d.md)
  const flat = String(type || '').toLowerCase() === 'flat';
  return [SCREW_SIDE, new THREE.MeshStandardMaterial({ map: screwTex(false, flat), bumpMap: screwTex(true, flat), bumpScale: 2.2, roughness: 0.4, metalness: 0.8 }), SCREW_SIDE];
}
function mesh(geo, mat, sx, sy, sz, x, y, z, parent, shadow = true) {
  const m = new THREE.Mesh(geo, mat);
  m.scale.set(sx, sy, sz); m.position.set(x, y, z);
  m.castShadow = shadow; m.receiveShadow = true;
  parent.add(m); return m;
}
const faceMats = (edge, front) => [edge, edge, edge, edge, front, edge];

// ------------------------------------------------------------------ canvas textures (procedural, no photos)
const PX = 12;
const FONT = '"Noto Sans", "Segoe UI", Arial, sans-serif';
function canvasTex(wmm, hmm, draw) {
  const c = document.createElement('canvas');
  c.width = Math.round(wmm * PX); c.height = Math.round(hmm * PX);
  const g = c.getContext('2d'); g.scale(PX, PX); draw(g, wmm, hmm);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = ANISO; return t;
}
function txt(g, s, x, y, size, color, align = 'left', weight = 700) {
  g.font = `${weight} ${size}px ${FONT}`; g.fillStyle = color; g.textAlign = align; g.textBaseline = 'middle'; g.fillText(s, x, y);
}
function rrect(g, x, y, w, h, r) {
  g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r);
  g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath();
}

// ------------------------------------------------------------------ the device model (layout, roles, live sources)
// member = key in state.v (device UDT member under IO/); null = no live tag in the device UDT
const IN_LABEL = { 0: 'LSS HLCO', 1: 'HSS HLCO' };           // FT (STELLAR)SafetyRelay: "Input 0: LSS HLCO", "Input 1: HSS HLCO"
const OUT_LABEL = { 0: 'LSS HLCO Output 0', 1: 'HSS HLCO Output 1' };
const NOT_LAB = 'Not Labelled On The FT Display';
const T_SAFE = 'Safety Input (N.C.)';
const T_SW = 'Safety Input (N.C.) Or Single-Wire Safety Input';
const T_MULTI = 'Test Output, OSSD High Side, Safety Input (N.C. / N.O.) Or Standard Diagnostic';
const T_OSSD = 'OSSD High Side (Safety Output)';
const T_OSSD2 = 'OSSD High Side Or Single-Wire Safety Output';
const pt2 = (n) => String(n).padStart(2, '0');
const OUTS = [  // the six OUT lamps (FT / 2D page): terminals 18-21, then the safety output functions SOF05 / SOF06
  { n: 0, member: 'Pt18Data', term: '18' }, { n: 1, member: 'Pt19Data', term: '19' },
  { n: 2, member: 'Pt20Data', term: '20' }, { n: 3, member: 'Pt21Data', term: '21' },
  { n: 4, member: 'SOF05', term: null }, { n: 5, member: 'SOF06', term: null }];
function mainTerms() {   // top row 00-11 (left to right), bottom row A1, A2, 12-21 (440C-UM001 Table 2 + terminal block figure)
  const t = [];
  for (let i = 0; i < 12; i++) {
    t.push({ id: pt2(i), row: 'top', col: i, label: 'Input ' + pt2(i), role: i < 10 ? T_SAFE : T_SW,
      desc: i < 10 ? (IN_LABEL[i] ? 'In ' + i + ': ' + IN_LABEL[i] : 'In ' + i + ' (' + NOT_LAB + ')') : 'Terminal ' + i + ' (No Live Tag In The Device)',
      member: i < 10 ? 'Pt' + pt2(i) + 'Data' : null });
  }
  const b = ['A1', 'A2'].concat(Array.from({ length: 10 }, (_, k) => String(12 + k)));
  b.forEach((id, col) => {
    const n = Number(id);
    const o = OUTS.find((q) => q.term === id);
    const e = { id, row: 'bottom', col, member: null };
    if (id === 'A1') Object.assign(e, { label: '+24V DC (A1)', role: 'Power Supply +24V DC (-15% / +10%)', desc: 'Control Power' });
    else if (id === 'A2') Object.assign(e, { label: '0V Common (A2)', role: 'Power Supply 0V', desc: 'Control Power Common' });
    else if (o) Object.assign(e, { label: 'Output ' + id, role: n < 20 ? T_OSSD : T_OSSD2, member: o.member,
      desc: 'Out ' + o.n + (OUT_LABEL[o.n] ? ': ' + OUT_LABEL[o.n] : ' (' + NOT_LAB + ')') });
    else Object.assign(e, { label: 'Terminal ' + id, role: T_MULTI, desc: 'Terminal ' + id + ' (No Live Tag In The Device)' });
    t.push(e);
  });
  return t;
}
const PI2_TERMS = [   // 2080-IQ4-OB4 (Micro800 plug-in, 4 in / 4 out): two columns of five (labelling approximate, see doc)
  ['I-00', 'Plugin2InPt00Data', 'Plug-In Input 0'], ['I-01', 'Plugin2InPt01Data', 'Plug-In Input 1'],
  ['I-02', 'Plugin2InPt02Data', 'Plug-In Input 2'], ['I-03', 'Plugin2InPt03Data', 'Plug-In Input 3'], ['IC', null, 'Input Common'],
  ['O-00', 'Plugin2OutPt00Data', 'Plug-In Output 0'], ['O-01', 'Plugin2OutPt01Data', 'Plug-In Output 1'],
  ['O-02', 'Plugin2OutPt02Data', 'Plug-In Output 2'], ['O-03', 'Plugin2OutPt03Data', 'Plug-In Output 3'], ['OC', null, 'Output Supply / Common']];
const PI2_DESC = { Plugin2InPt00Data: 'Reset input (FT: this lamp flashes while a reset is needed)' };

// ------------------------------------------------------------------ build
let built = false, ledMesh = null, ledColors = [], screwsMesh = null, termProxy = null, termBox = null, hlTerm = -1;
const leds = [], terms = [];
let hoverBox, selBox, hitBody;
let stScrew = 'phillips';
const WHITE = new THREE.Color(1, 1, 1), AMBER = new THREE.Color(1.0, 0.62, 0.1);

function addLed(x, y, z, id, name, fn) { leds.push({ pos: new THREE.Vector3(x, y, z), id, name, fn }); return leds.length - 1; }
const bit = (S, m) => (S.on && m && S.v && S.v[m] != null ? S.v[m] : null);

function buildDucts() {
  const RL = SCENE_W, DH = 60, DD = 70, WT = 2.4, cy0 = H / 2 + 62;
  const cssHex = (n) => '#' + n.toString(16).padStart(6, '0');
  const baseTex = canvasTex(25, DH, (g) => { g.fillStyle = cssHex(THEME.duct); g.fillRect(0, 0, 25, DH); g.fillStyle = THEME.slot; rrect(g, 9.5, 6, 6, DH - 12, 3); g.fill(); });
  const wallTex = canvasTex(25, DD, (g) => { g.fillStyle = cssHex(THEME.duct); g.fillRect(0, 0, 25, DD); g.fillStyle = THEME.slot; rrect(g, 8, 10, 9, DD - 14, 4.5); g.fill(); g.fillStyle = 'rgba(255,255,255,0.18)'; g.fillRect(0, 0, 25, 2.5); });
  baseTex.wrapS = wallTex.wrapS = THREE.RepeatWrapping; baseTex.repeat.set(RL / 25, 1); wallTex.repeat.set(RL / 25, 1);
  const mBase = std(0xffffff, 0.4, 0.02, { map: baseTex }), mWall = std(0xffffff, 0.38, 0.02, { map: wallTex });
  const mEdge = std(THEME.duct, 0.4, 0.02), mCover = std(THEME.ductCover, 0.3, 0.02);
  const wallMats = [mEdge, mEdge, mWall, mWall, mEdge, mEdge];
  const clips = [];
  const mtx = new THREE.Matrix4(), q = new THREE.Quaternion(), sc = new THREE.Vector3(), ps = new THREE.Vector3();
  const capL = RL * 0.2, capMid = [-RL / 2 + capL / 2, RL / 2 - capL / 2];
  [1, -1].forEach((sgn) => {
    const cy = sgn * cy0, cz = -9 + 1.5 + DD / 2 - 3;
    mesh(BOX, mBase, RL, DH, 2.4, 0, cy, -6.3, scene);
    [1, -1].forEach((w) => mesh(BOX, wallMats, RL, WT, DD - 2, 0, cy + w * (DH / 2 - WT / 2), cz + 1, scene));
    capMid.forEach((cx) => {
      mesh(BOX, mCover, capL, DH + 3, 1.8, cx, cy, cz + DD / 2 - 0.4, scene);
      [1, -1].forEach((w) => mesh(BOX, mCover, capL, 2, 5.5, cx, cy + w * (DH / 2 + 1.4), cz + DD / 2 - 2.9, scene));
      [1, -1].forEach((w) => mesh(BOX, mCover, 1.8, DH + 3, 5.5, cx + w * capL / 2, cy, cz + DD / 2 - 2.9, scene));
    });
    for (let x = -RL / 2 + 40; x <= RL / 2 - 20; x += 90) [1, -1].forEach((w) => clips.push([x, cy + w * (DH / 2 + 3.5), -5.2, 14, 5, 2.6]));
    [-1, 1].forEach((w) => clips.push([w * (RL / 2 - 14), cy, -5, 22, 18, 3.4]));
  });
  const cm = new THREE.InstancedMesh(BOX, std(0x8f9398, 0.5, 0.6), clips.length);
  clips.forEach((c, i) => { q.identity(); sc.set(c[3], c[4], c[5]); ps.set(c[0], c[1], c[2]); mtx.compose(ps, q, sc); cm.setMatrixAt(i, mtx); });
  cm.instanceMatrix.needsUpdate = true; cm.castShadow = cm.receiveShadow = true; scene.add(cm);
  const sm = new THREE.InstancedMesh(SCREW_GEO, screwMats(stScrew), clips.length);
  clips.forEach((c, i) => { q.identity(); sc.set(0.9, 0.9, 0.9); ps.set(c[0], c[1], c[2] + c[5] / 2 + 0.2); mtx.compose(ps, q, sc); sm.setMatrixAt(i, mtx); });
  sm.instanceMatrix.needsUpdate = true; scene.add(sm);
}

function termStripTex(w, h, row, items) {   // numbers printed on the terminal block front, screw at the middle
  return canvasTex(w, h, (g) => {
    g.fillStyle = '#2c2f33'; g.fillRect(0, 0, w, h);
    items.forEach((it) => {
      const cx = w / 2 + it.x, cy = row === 'top' ? h - 3.6 : 3.6;
      txt(g, it.id, cx, cy, 2.5, '#e9ecef', 'center', 700);
      g.fillStyle = '#16181a'; rrect(g, cx - 2.6, h / 2 - 3.2, 5.2, 6.4, 0.8); g.fill();   // screw pocket
    });
  });
}

function bandTex() {   // the red centre band: LED block legends (LED bezels), plug-in bays
  return canvasTex(W, BAND, (g) => {
    g.fillStyle = '#b7141b'; g.fillRect(0, 0, W, BAND);
    g.fillStyle = 'rgba(0,0,0,0.22)'; g.fillRect(0, 0, W, 0.7); g.fillRect(0, BAND - 0.7, W, 0.7);
    const X0 = 16, Y0 = BAND / 2, tx = (x) => X0 + x, ty = (y) => Y0 - y;   // LED block centre (texture mm)
    g.fillStyle = '#7d0d12'; rrect(g, 1.5, 1.5, 29, BAND - 3, 1.6); g.fill();
    const bez = (x, y) => { g.fillStyle = '#26282b'; rrect(g, tx(x) - 1.9, ty(y) - 1.4, 3.8, 2.8, 0.5); g.fill(); };
    txt(g, 'INPUT', tx(0), ty(26.2), 2.0, '#ffd9d9', 'center');
    for (let i = 0; i < 12; i++) { const x = -10.5 + (i % 6) * 4.2, y = i < 6 ? 22.2 : 15.2; bez(x, y); txt(g, String(i), tx(x), ty(y - 3.0), 1.9, '#fff', 'center', 600); }
    ['POWER', 'RUN', 'FAULT', 'LOCK', 'COM'].forEach((s, i) => { const y = 7.6 - i * 3.9; bez(-12, y); txt(g, s, tx(-9), ty(y), 2.0, '#fff', 'left'); });
    g.fillStyle = '#26282b'; g.beginPath(); g.arc(tx(10), ty(-2.0), 2.6, 0, 7); g.fill();
    g.strokeStyle = '#d9dde1'; g.lineWidth = 0.5; g.beginPath(); g.arc(tx(10), ty(-2.0), 2.6, 0, 7); g.stroke();
    txt(g, 'VERIFY', tx(10), ty(-6.6), 1.8, '#fff', 'center', 600);
    txt(g, 'OUTPUT', tx(0), ty(-12.4), 2.0, '#ffd9d9', 'center');
    for (let i = 0; i < 6; i++) { const x = -10.5 + i * 4.2, y = -17.4; bez(x, y); txt(g, String(i), tx(x), ty(y - 3.0), 1.9, '#fff', 'center', 600); }
    txt(g, '440C-CR30', tx(0), ty(-26.0), 2.6, '#fff', 'center');
    [-1.75, 31.75].forEach((cx) => { g.fillStyle = '#4a0a0d'; rrect(g, 50 + cx - PI_W / 2 - 0.8, 1.2, PI_W + 1.6, BAND - 2.4, 1.0); g.fill(); });
  });
}
function piEnetTex() {
  return canvasTex(PI_W, PI_H, (g, w, h) => {
    g.fillStyle = '#a3aab0'; g.fillRect(0, 0, w, h);
    g.fillStyle = '#8b9298'; g.fillRect(0, 0, w, 1.2);
    txt(g, '440C-ENET', w / 2, 5, 3.0, '#1c1f22', 'center');
    txt(g, 'EtherNet/IP', w / 2, 9.2, 2.1, '#2c3034', 'center', 600);
    ['MS', 'NS', 'LNK'].forEach((s, i) => { g.fillStyle = '#26282b'; rrect(g, 7.5, 15.4 + i * 5.2 - 1.5, 4.0, 3.0, 0.5); g.fill(); txt(g, s, 14.5, 15.4 + i * 5.2, 2.2, '#1c1f22', 'left'); });
    g.fillStyle = '#50565b'; rrect(g, 6.2, 31.0, 19.2, 15.4, 1.2); g.fill();   // RJ45 jack opening
    g.fillStyle = '#0f1113'; rrect(g, 7.6, 32.4, 16.4, 12.6, 0.8); g.fill();
    g.fillStyle = '#2a2d30'; rrect(g, 12.4, 31.4, 6.8, 2.6, 0.6); g.fill();
    g.fillStyle = '#d4a935'; for (let i = 0; i < 8; i++) g.fillRect(9.0 + i * 1.7, 38.2, 0.9, 5.6);
    txt(g, 'RJ45', w / 2, 51.5, 2.4, '#1c1f22', 'center', 600);
  });
}
function piIoTex() {
  return canvasTex(PI_W, PI_H, (g, w, h) => {
    g.fillStyle = '#a3aab0'; g.fillRect(0, 0, w, h);
    g.fillStyle = '#8b9298'; g.fillRect(0, 0, w, 1.2);
    txt(g, '2080-IQ4OB4', w / 2, 3.4, 2.7, '#1c1f22', 'center');
    txt(g, 'IN', 4.0, 8.0, 2.0, '#1c1f22', 'left'); txt(g, 'OUT', 4.0, 13.6, 2.0, '#1c1f22', 'left');
    for (let i = 0; i < 4; i++) {
      [8.0, 13.6].forEach((y) => { g.fillStyle = '#26282b'; rrect(g, 11.6 + i * 4.8 - 1.8, y - 1.3, 3.6, 2.6, 0.5); g.fill(); });
      txt(g, String(i), 11.6 + i * 4.8, 10.8, 1.8, '#1c1f22', 'center', 600);
    }
    g.fillStyle = '#6b7278'; g.fillRect(2, 17.6, w - 4, h - 19.4);
    PI2_TERMS.forEach(([id], k) => {
      const col = k < 5 ? 0 : 1, row = k % 5, cx = col ? 23.6 : 7.9, cy = 23.6 + row * 7.4;
      txt(g, id, cx, cy - 3.7, 1.9, '#f2f4f6', 'center', 700);
      g.fillStyle = '#16181a'; rrect(g, cx - 2.6, cy - 2.4, 5.2, 4.8, 0.7); g.fill();
    });
  });
}

function build(st) {
  stScrew = String((st && st.screwType) || 'phillips').toLowerCase() === 'flat' ? 'flat' : 'phillips';
  const SM = screwMats(stScrew);
  const screwPos = [];
  // back-panel, DIN rail (EN 50022 35 x 7.5 top hat), wire ducts above / below
  mesh(BOX, M.panel, SCENE_W + 60, 360, 3, 0, 0, -9, scene, false);
  const RL = SCENE_W;
  mesh(BOX, M.rail, RL, 27, 1, 0, 0, -7, scene, false);
  mesh(BOX, M.rail, RL, 1, 7.5, 0, 13, -3.75, scene, false);
  mesh(BOX, M.rail, RL, 1, 7.5, 0, -13, -3.75, scene, false);
  mesh(BOX, M.rail, RL, 4.5, 1, 0, 15.25, -0.5, scene, false);
  mesh(BOX, M.rail, RL, 4.5, 1, 0, -15.25, -0.5, scene, false);
  buildDucts();

  // housing: main body (to the recessed band) + two proud terminal blocks, mounting feet, DIN latch, side ports
  const g = new THREE.Group(); scene.add(g);
  mesh(BOX, M.red, W, H, FACE_Z, 0, 0, FACE_Z / 2, g);
  const band = new THREE.Mesh(PLANE, new THREE.MeshStandardMaterial({ map: bandTex(), roughness: 0.5, metalness: 0.02 }));
  band.scale.set(W, BAND, 1); band.position.set(0, 0, FACE_Z + 0.03); band.receiveShadow = true; g.add(band);
  const topItems = [], botItems = [];
  const mt = mainTerms();
  mt.forEach((t) => { t.x = (t.col - 5.5) * PITCH; (t.row === 'top' ? topItems : botItems).push(t); });
  const BLK_H = (H - BAND) / 2;   // 16
  [['top', topItems, 1], ['bottom', botItems, -1]].forEach(([row, items, s]) => {
    const tex = termStripTex(W - 8, BLK_H, row, items);
    mesh(BOX, faceMats(M.block, new THREE.MeshStandardMaterial({ map: tex, roughness: 0.65 })), W - 8, BLK_H, D - FACE_Z, 0, s * (BAND / 2 + BLK_H / 2), (D + FACE_Z) / 2, g);
    items.forEach((t) => mesh(BOX, M.dark, 4.6, 1.2, 4.0, t.x, s * (H / 2 - 0.4), D - 6, g, false));   // wire-entry mouths
    items.forEach((t) => { t.y = s * (BAND / 2 + BLK_H / 2); });
  });
  [-1, 1].forEach((s) => {                 // feet (hole spacing 86 x 100), DIN latch
    mesh(BOX, M.tab, 14, 9, 5, s * 43, H / 2 + 4.5, 4, g); mesh(BOX, M.tab, 14, 9, 5, s * 43, -H / 2 - 4.5, 4, g);
  });
  mesh(BOX, M.latch, 22, 6, 8, 0, -H / 2 - 3, 12, g);
  // USB Type-B and RS-232 on the left side wall (position approximate: 440C-UM001 Fig. 2 items 8 / 9)
  const side = new THREE.Group(); side.position.set(-W / 2, 0, 28); side.rotation.y = -Math.PI / 2; g.add(side);
  mesh(BOX, M.metal, 12, 10.5, 5, 0, -12, 0, side); mesh(BOX, M.dark, 8.6, 7.2, 3, 0, -12, 1.4, side, false);
  mesh(BOX, std(0x3b3f43, 0.6), 7, 1.6, 2.5, 0, -12, 1.6, side, false);
  for (let i = 0; i < 4; i++) mesh(BOX, M.gold, 1, 0.6, 2.8, -2.4 + i * 1.6, -9.9, 1.6, side, false);
  const ser = new THREE.Mesh(new THREE.CylinderGeometry(4.6, 4.6, 5, 28).rotateX(Math.PI / 2), M.metal); ser.position.set(0, 12, 0); side.add(ser);
  const serIn = new THREE.Mesh(new THREE.CylinderGeometry(3.4, 3.4, 3, 28).rotateX(Math.PI / 2), M.dark); serIn.position.set(0, 12, 1.4); side.add(serIn);
  // top / bottom vents (texture only)
  const vt = canvasTex(W, 40, (c) => { c.fillStyle = '#a3131a'; c.fillRect(0, 0, W, 40); c.fillStyle = '#5a0a0e'; for (let i = 0; i < 14; i++) c.fillRect(8 + i * 6.2, 6, 2.6, 28); });
  [1, -1].forEach((s) => {
    const p = new THREE.Mesh(PLANE, new THREE.MeshStandardMaterial({ map: vt, roughness: 0.55 }));
    p.rotation.x = -s * Math.PI / 2; p.scale.set(W - 12, 40, 1); p.position.set(0, s * (H / 2 + 0.04), 24); g.add(p);
  });

  // plug-in modules (slot 1 440C-ENET, slot 2 2080-IQ4-OB4)
  const PIX = [-1.75, 31.75], bandCz = FACE_Z + (PI_FRONT - FACE_Z) / 2;
  [piEnetTex(), piIoTex()].forEach((tex, k) => {
    mesh(BOX, faceMats(M.grey, new THREE.MeshStandardMaterial({ map: tex, roughness: 0.55 })), PI_W, PI_H, PI_FRONT - FACE_Z, PIX[k], 0, bandCz, g);
  });
  // LEDs (housing coordinates; the LED block centre is x = -34)
  const LZ = FACE_Z + 0.5, LX = -34;
  for (let i = 0; i < 12; i++) {
    const x = LX - 10.5 + (i % 6) * 4.2, y = i < 6 ? 22.2 : 15.2, m = i < 10 ? 'Pt' + pt2(i) + 'Data' : null;
    addLed(x, y, LZ, 'in' + i, 'Input ' + i, (S) => (bit(S, m) ? 'on' : 'off'));
  }
  const sx = LX - 12;
  addLed(sx, 7.6, LZ, 'power', 'Power', (S) => (S.on ? 'on' : 'off'));
  addLed(sx, 3.7, LZ, 'run', 'Run', (S) => (S.on && S.run ? 'on' : 'off'));
  addLed(sx, -0.2, LZ, 'fault', 'Fault', (S) => (S.on && S.fault ? 'fault' : 'off'));
  addLed(sx, -4.1, LZ, 'lock', 'Lock', () => 'off');
  addLed(sx, -8.0, LZ, 'com', 'Com', (S) => (S.have ? (S.on ? 'on' : 'fault') : 'off'));
  OUTS.forEach((o, i) => addLed(LX - 10.5 + i * 4.2, -17.4, LZ, 'out' + i, 'Output ' + i, (S) => (bit(S, o.member) ? 'on' : 'off')));
  const e0 = PIX[0] - PI_W / 2, i0 = PIX[1] - PI_W / 2, PZ = PI_FRONT + 0.5;
  ['MS', 'NS', 'LNK'].forEach((s, i) => addLed(e0 + 9.5, PI_H / 2 - (15.4 + i * 5.2), PZ, 'enet' + s, '440C-ENET ' + s, (S) => (S.on ? 'on' : 'off')));
  for (let i = 0; i < 4; i++) {
    addLed(i0 + 11.6 + i * 4.8, PI_H / 2 - 8.0, PZ, 'pin' + i, 'Plug-In Input ' + i, (S) => (bit(S, 'Plugin2InPt0' + i + 'Data') ? 'on' : 'off'));
    addLed(i0 + 11.6 + i * 4.8, PI_H / 2 - 13.6, PZ, 'pout' + i, 'Plug-In Output ' + i, (S) => (bit(S, 'Plugin2OutPt0' + i + 'Data') ? 'on' : 'off'));
  }
  // terminals (screw positions)
  mt.forEach((t) => {
    t.tw = 6.4; t.th = 9; t.pos = new THREE.Vector3(t.x, t.y, D + 0.3); t.where = t.row === 'top' ? 'Top Row' : 'Bottom Row';
    terms.push(t); screwPos.push(t.pos);
  });
  PI2_TERMS.forEach(([id, member, name], k) => {
    const col = k < 5 ? 0 : 1, row = k % 5;
    const t = { id, label: id, role: name + ' (2080-IQ4OB4 Plug-In 2)', desc: member ? name + (PI2_DESC[member] ? ': ' + PI2_DESC[member] : '') : name, member,
      where: 'Plug-In 2', tw: 6.4, th: 6, pos: new THREE.Vector3(i0 + (col ? 23.6 : 7.9), PI_H / 2 - (23.6 + row * 7.4), PZ - 0.3) };
    terms.push(t); screwPos.push(t.pos);
  });
  const mtx = new THREE.Matrix4();
  ledMesh = new THREE.InstancedMesh(LED_GEO, LED_MAT, leds.length);
  leds.forEach((l, i) => { mtx.makeTranslation(l.pos.x, l.pos.y, l.pos.z); ledMesh.setMatrixAt(i, mtx); ledMesh.setColorAt(i, LED.off); });
  ledColors = leds.map(() => 'off');
  ledMesh.instanceMatrix.needsUpdate = true; ledMesh.instanceColor.needsUpdate = true; scene.add(ledMesh);
  screwsMesh = new THREE.InstancedMesh(SCREW_GEO, SM, screwPos.length);
  screwPos.forEach((p, i) => { mtx.makeTranslation(p.x, p.y, p.z); screwsMesh.setMatrixAt(i, mtx); screwsMesh.setColorAt(i, WHITE); });
  screwsMesh.instanceMatrix.needsUpdate = true; screwsMesh.instanceColor.needsUpdate = true; screwsMesh.castShadow = true; scene.add(screwsMesh);
  termProxy = new THREE.InstancedMesh(BOX, new THREE.MeshBasicMaterial({ visible: false }), screwPos.length);
  const COARSE = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  const sc3 = new THREE.Vector3(), q0 = new THREE.Quaternion();
  terms.forEach((t, i) => { sc3.set(COARSE ? t.tw * 1.15 : t.tw, COARSE ? t.th * 1.1 : t.th, 6); mtx.compose(t.pos, q0, sc3); termProxy.setMatrixAt(i, mtx); });
  termProxy.instanceMatrix.needsUpdate = true; termProxy.computeBoundingSphere(); scene.add(termProxy);
  termBox = new THREE.LineSegments(new THREE.EdgesGeometry(BOX), new THREE.LineBasicMaterial({ color: 0xffb000 }));
  termBox.visible = false; scene.add(termBox);
  hitBody = new THREE.Mesh(BOX, new THREE.MeshBasicMaterial({ visible: false }));
  hitBody.scale.set(W, H, D); hitBody.position.set(0, 0, D / 2); scene.add(hitBody);
  const edges = new THREE.EdgesGeometry(BOX);
  hoverBox = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: THEME.hover }));
  selBox = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: THEME.sel }));
  [hoverBox, selBox].forEach((b) => { b.visible = false; b.scale.set(W + 1.5, H + 1.5, D + 1.5); b.position.set(0, 0, D / 2); scene.add(b); });
  resetView(true);
  built = true;
}

// ------------------------------------------------------------------ camera (hand-rolled tween), straight-on zoom
const REDUCED = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
const ease = (k) => (k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2);
let anim = null, focused = false, overview = null, histPushed = false, dirty = true;
function overviewPose() {
  const aspect = Math.max(0.3, camera.aspect || 1), th = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2);
  const dist = Math.max(125 / (th * aspect), 135 / th);
  return { t: new THREE.Vector3(0, 0, 40), p: new THREE.Vector3(dist * 0.16, dist * 0.2, 40 + dist * 0.97), near: Math.max(5, dist / 200), far: dist * 10 };
}
function flyTo(pose, ms) {
  const dur = REDUCED ? 0 : ms;
  if (dur <= 0) {
    anim = null; controls.enabled = true; camera.position.copy(pose.p); controls.target.copy(pose.t);
    camera.near = pose.near; camera.far = pose.far; camera.updateProjectionMatrix(); controls.update(); dirty = true; return;
  }
  anim = { t0: performance.now(), dur, p0: camera.position.clone(), p1: pose.p.clone(), g0: controls.target.clone(), g1: pose.t.clone(), near: pose.near, far: pose.far };
  controls.enabled = false;
  camera.near = Math.min(camera.near, pose.near); camera.far = Math.max(camera.far, pose.far); camera.updateProjectionMatrix();
}
function stepAnim(now) {
  if (!anim) return false;
  const k = Math.min(1, (now - anim.t0) / anim.dur), e = ease(k);
  camera.position.lerpVectors(anim.p0, anim.p1, e); controls.target.lerpVectors(anim.g0, anim.g1, e); camera.lookAt(controls.target);
  if (k >= 1) { camera.near = anim.near; camera.far = anim.far; camera.updateProjectionMatrix(); anim = null; controls.enabled = true; controls.update(); }
  return true;
}
function resetView(instant) { if (focused) { zoomOut(); return; } flyTo(overviewPose(), instant ? 0 : 700); }
function focusPose() {   // straight on: camera on the face normal (zero yaw / pitch); the relay sits beside the info panel
  const r = $('stage').getBoundingClientRect(), Wd = Math.max(1, r.width), Hh = Math.max(1, r.height), aspect = Wd / Hh;
  const th = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2), narrow = Wd <= 640;
  const pw = narrow ? 0 : Math.min(460, Wd - 24) + 24, freeW = narrow ? Wd : Math.max(120, Wd - pw);
  const dist = Math.max(112 / 0.82 / (2 * th), (W + 36) / (2 * th * aspect * (freeW / Wd)));
  const t = new THREE.Vector3((pw / Wd) * dist * th * aspect, narrow ? -0.5 * dist * th : 0, D);
  return { t, p: t.clone().add(new THREE.Vector3(0, 0, dist)), near: Math.max(5, dist / 200), far: Math.max(overviewPose().far, dist * 10) };
}
function zoomTo(instant) {
  if (!focused) overview = { p: camera.position.clone(), t: controls.target.clone(), near: camera.near, far: camera.far };
  focused = true; setSelected(true); flyTo(focusPose(), instant ? 0 : 800);
  try { if (!histPushed) { history.pushState({ relay3d: 1 }, ''); histPushed = true; } } catch (e) { /* sandboxed frame */ }
}
function zoomOut(fromPop) {
  unpinTerm();
  if (!focused) return;
  focused = false; setSelected(false); flyTo(overview || overviewPose(), 700);
  if (histPushed) { histPushed = false; if (!fromPop) { try { history.back(); } catch (e) { /* ignore */ } } }
}
$('reset').addEventListener('click', () => { resetView(); });
window.addEventListener('popstate', () => { if (focused) { histPushed = false; zoomOut(true); } });

function resize() {
  const r = $('stage').getBoundingClientRect(), w = Math.max(1, r.width), h = Math.max(1, r.height);
  renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); dirty = true;
}
new ResizeObserver(resize).observe($('stage'));
resize();
controls.addEventListener('change', () => { dirty = true; });
let pendingPick = false;
function frame() {
  requestAnimationFrame(frame);
  if (stepAnim(performance.now())) dirty = true; else if (controls.update()) dirty = true;
  if (pendingPick) { pendingPick = false; doHover(); }
  if (dirty && built) { dirty = false; renderer.render(scene, camera); }
}
requestAnimationFrame(frame);

// ------------------------------------------------------------------ hover / tap
const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
let mouse = null, down = null, selected = false, hovered = false, pinned = null;
const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch]));
function setRay(ev) {
  const r = renderer.domElement.getBoundingClientRect();
  ndc.set(((ev.clientX - r.left) / r.width) * 2 - 1, -((ev.clientY - r.top) / r.height) * 2 + 1); ray.setFromCamera(ndc, camera);
}
function bodyAt(ev) { setRay(ev); return ray.intersectObject(hitBody, false).length > 0; }
function terminalAt(ev) {
  if (!ev || anim || !termProxy) return null;
  setRay(ev);
  const h = ray.intersectObject(termProxy, false)[0];
  return h ? { id: h.instanceId, t: terms[h.instanceId] } : null;
}
function setTerm(t) {
  const id = t ? t.id : -1;
  if (id === hlTerm) return;
  if (hlTerm >= 0) screwsMesh.setColorAt(hlTerm, WHITE);
  if (id >= 0) { screwsMesh.setColorAt(id, AMBER); termBox.visible = true; termBox.position.copy(t.t.pos); termBox.scale.set(t.t.tw, t.t.th, 6.2); }
  else termBox.visible = false;
  screwsMesh.instanceColor.needsUpdate = true; hlTerm = id; dirty = true;
}
let S = { have: false, on: false, v: {} };
function memberState(m) {   // ON / OFF, COMM LOSS (red), No Data / No Live Tag (gray)
  if (!m) return { txt: 'No Live Tag', cls: 'gray' };
  if (!S.have) return { txt: 'No Data', cls: 'gray' };
  if (!S.on) return { txt: 'COMM LOSS', cls: 'bad' };
  const b = S.v[m];
  if (b == null) return { txt: 'No Data', cls: 'gray' };
  return { txt: b ? 'ON' : 'OFF', cls: b ? 'ok' : 'gray' };
}
function termTip(t) {
  const st = memberState(t.t.member);
  return `<b>${esc(t.t.label)}</b><div class="muted">${esc(t.t.where)} &middot; Terminal ${esc(t.t.id)}</div>` +
    `<div class="muted">${esc(t.t.role)}</div><div>${esc(t.t.desc)}</div><div class="st ${st.cls}">${st.txt}</div>`;
}
function statusLine() {
  if (!S.have) return ['No Data', 'gray'];
  if (!S.on) return ['COMM LOSS', 'bad'];
  if (S.fault) return ['FAULT', 'bad'];
  return S.run ? ['RUN', 'ok'] : ['STOP', 'gray'];
}
function bodyTip() {
  const [s, c] = statusLine();
  return `<b>${esc(DEVICE)}</b><div class="muted">440C-CR30-22BBB &middot; Guardmaster Configurable Safety Relay</div><div class="st ${c}">${s}</div>` +
    (focused ? '' : '<div class="muted">Click To Zoom</div>');
}
function doHover() {
  if (!mouse || !built) return;
  const tm = terminalAt(mouse);
  const over = !!tm || bodyAt(mouse);
  if (over !== hovered) { hovered = over; hoverBox.visible = over && !selected; dirty = true; }
  renderer.domElement.style.cursor = over ? 'pointer' : 'grab';
  if (!tm && pinned) { setTerm(pinned.t); placeTip(pinned.html(), pinned.pt); return; }
  setTerm(tm);
  if (!over) { $('tip').hidden = true; return; }
  placeTip(tm ? termTip(tm) : bodyTip(), mouse);
}
function placeTip(html, pt) {
  const tip = $('tip'); tip.innerHTML = html; tip.hidden = false;
  const r = $('stage').getBoundingClientRect(), tw = tip.offsetWidth, th = tip.offsetHeight;
  let x = pt.clientX - r.left + 16, y = pt.clientY - r.top + 16;
  if (x + tw > r.width - 8) x = pt.clientX - r.left - tw - 16;
  if (y + th > r.height - 8) y = pt.clientY - r.top - th - 16;
  tip.style.left = Math.max(8, x) + 'px'; tip.style.top = Math.max(8, y) + 'px';
}
function pinTerm(t, ev) { pinned = { id: t.id, t, pt: { clientX: ev.clientX, clientY: ev.clientY }, html: () => termTip(t) }; setTerm(t); placeTip(pinned.html(), pinned.pt); }
function unpinTerm() { if (!pinned) return; pinned = null; setTerm(null); $('tip').hidden = true; dirty = true; }
renderer.domElement.addEventListener('pointermove', (ev) => { if (ev.pointerType === 'touch') return; mouse = ev; pendingPick = true; });
renderer.domElement.addEventListener('pointerleave', (ev) => { if (ev.pointerType === 'touch') return; mouse = null; hovered = false; if (hoverBox) hoverBox.visible = false; if (!pinned) $('tip').hidden = true; dirty = true; });
renderer.domElement.addEventListener('pointerdown', (ev) => { down = [ev.clientX, ev.clientY]; });
renderer.domElement.addEventListener('pointerup', (ev) => {
  if (!down || Math.hypot(ev.clientX - down[0], ev.clientY - down[1]) > (ev.pointerType === 'touch' ? 10 : 5)) { down = null; return; }
  down = null;
  if (!built) return;
  const tm = terminalAt(ev);
  if (tm) { pinTerm(tm, ev); return; }
  if (bodyAt(ev)) { if (focused) unpinTerm(); else zoomTo(); return; }
  zoomOut();
});
function setSelected(on) {
  selected = on; selBox.visible = on; if (on) hoverBox.visible = false;
  const p = $('panel');
  if (on) { p.hidden = false; void p.offsetWidth; p.classList.add('show'); }
  else { p.classList.remove('show'); setTimeout(() => { if (!selected) p.hidden = true; }, REDUCED ? 0 : 260); }
  renderPanel(); dirty = true;
}
$('p-close').addEventListener('click', () => zoomOut());
window.addEventListener('keydown', (e) => { if (e.key === 'Escape') { if (pinned) unpinTerm(); else zoomOut(); } });

// ------------------------------------------------------------------ state -> LEDs / panel
let state = null;
function setLed(i, key) { if (ledColors[i] === key) return false; ledColors[i] = key; ledMesh.setColorAt(i, LED[key]); return true; }
function applyState() {
  const ok = !!(state && state.ok);
  S = { have: ok, on: ok && !!state.comm, v: ok ? (state.v || {}) : {}, run: ok && !!state.run, fault: ok && !!state.fault };
  if (built) {
    let ch = false;
    leds.forEach((l, i) => { ch = setLed(i, l.fn(S)) || ch; });
    if (ch) { ledMesh.instanceColor.needsUpdate = true; dirty = true; }
  }
  const chip = $('chip');
  if (!ok) { chip.textContent = 'No Data'; chip.className = 'chip chip-off'; }
  else if (!S.on) { chip.textContent = 'Comm Loss'; chip.className = 'chip chip-fault'; }
  else if (S.fault) { chip.textContent = 'Fault'; chip.className = 'chip chip-fault'; }
  else { chip.textContent = S.run ? 'Run' : 'Stop'; chip.className = 'chip ' + (S.run ? 'chip-run' : 'chip-off'); }
  const banner = $('banner');
  if (ok && !S.on) { banner.textContent = 'Communication Lost'; banner.hidden = false; }
  else if (state && !ok) { banner.textContent = state.reason || 'No Data'; banner.hidden = false; }
  else banner.hidden = true;
  $('t-dev').textContent = (state && state.device) || DEVICE;
  if (hovered) doHover();
  renderPanel();
}
function rowHtml(n, name, m, extra) {
  const s = memberState(m), dot = s.cls === 'ok' ? 'on' : s.cls === 'bad' ? 'fault' : 'off';
  return `<div class="row"><span class="n">${esc(n)}</span><i class="dot ${dot}"></i><span class="lbl" title="${esc(name)}">${esc(name)}${extra ? '<br><span class="muted">' + esc(extra) + '</span>' : ''}</span><span class="v ${s.cls}">${s.txt}</span></div>`;
}
function renderPanel() {
  if (!selected) return;
  const [st, cls] = statusLine();
  $('p-status').innerHTML = `<span class="${cls}">${esc(st)}</span>`;
  $('p-title').textContent = DEVICE;
  $('p-sub').textContent = '440C-CR30-22BBB · Guardmaster Configurable Safety Relay';
  const yn = (m) => { const s = memberState(m); return s.txt === 'ON' ? ['Yes', 'bad'] : s.txt === 'OFF' ? ['No', 'ok'] : [s.txt, s.cls]; };
  const kv = (a, b, c) => `<div class="kv"><span>${esc(a)}</span><span class="${c || ''}">${esc(b == null ? '--' : b)}</span></div>`;
  const code = (k) => (S.on && state && state.codes && state.codes[k] != null ? state.codes[k] : '--');
  let h = '<div class="sec">Status</div>';
  h += kv('Run Mode', !S.on ? '--' : S.run ? 'Run' : 'Stop', S.on && S.run ? 'ok' : 'gray');
  h += kv('Major Fault', S.on ? (S.fault ? 'Yes' : 'No') : '--', S.on && S.fault ? 'bad' : S.on ? 'ok' : 'gray');
  h += kv('Major Fault Code / Type', S.on ? code('MajorFaultCode') + ' / ' + code('MajorFaultType') : '--');
  h += kv('Minor Fault', yn('MinorFault')[0], yn('MinorFault')[1]);
  h += kv('Connection', !S.have ? 'No Data' : S.on ? 'Connected' : 'COMM LOSS', !S.have ? 'gray' : S.on ? 'ok' : 'bad');
  const r1 = yn('SOF01ResetRequired'), r2 = yn('SOF02ResetRequired');
  h += kv('SOF01 Reset Required (LSS HLCO Output 0)', r1[0], r1[1]);
  h += kv('SOF02 Reset Required (HSS HLCO Output 1)', r2[0], r2[1]);
  h += kv('Reset Alarm (PLC Bit)', S.on && state && state.resetAlm != null ? (state.resetAlm ? 'Active' : 'Clear') : '--', S.on && state && state.resetAlm ? 'bad' : '');
  h += kv('Plug-In 1', '440C-ENET'); h += kv('Plug-In 2', '2080-IQ4-OB4');
  h += '<div class="sec">Inputs (Safety Input Points 0-9)</div>';
  for (let i = 0; i < 10; i++) h += rowHtml(i, IN_LABEL[i] ? 'In ' + i + ': ' + IN_LABEL[i] : 'Input ' + i, 'Pt' + pt2(i) + 'Data', IN_LABEL[i] ? '' : NOT_LAB);
  h += '<div class="sec">Outputs (Terminals 18-21, SOF05 / SOF06)</div>';
  OUTS.forEach((o) => { h += rowHtml(o.n, OUT_LABEL[o.n] ? 'Out ' + o.n + ': ' + OUT_LABEL[o.n] : 'Out ' + o.n, o.member, (o.term ? 'Terminal ' + o.term : 'Safety Output Function') + (OUT_LABEL[o.n] ? '' : ' · ' + NOT_LAB)); });
  h += '<div class="sec">Plug-In 2 (2080-IQ4-OB4)</div>';
  for (let i = 0; i < 4; i++) h += rowHtml('I' + i, 'Plug-In Input ' + i, 'Plugin2InPt0' + i + 'Data', i === 0 ? 'Reset Input' : '');
  for (let i = 0; i < 4; i++) h += rowHtml('O' + i, 'Plug-In Output ' + i, 'Plugin2OutPt0' + i + 'Data');
  $('p-body').innerHTML = h;
}

window.__relay3d = {
  select: () => zoomTo(), out: () => zoomOut(), reset: () => resetView(true), busy: () => !!anim, focused: () => focused, ready: () => built,
  pose: () => [camera.position.toArray(), controls.target.toArray()], pinned: () => (pinned ? pinned.t.t.id : null),
  view: (p, t) => { camera.position.set(p[0], p[1], p[2]); controls.target.set(t[0], t[1], t[2]); camera.lookAt(controls.target); controls.update(); dirty = true; },
  termScreen: (id, where) => { const t = terms.find((q) => q.id === id && (!where || q.where === where)); if (!t) return null;
    const v = t.pos.clone().project(camera), r = renderer.domElement.getBoundingClientRect(); return [r.left + (v.x + 1) / 2 * r.width, r.top + (1 - v.y) / 2 * r.height]; },
  bodyScreen: () => { const v = new THREE.Vector3(30, -10, D).project(camera), r = renderer.domElement.getBoundingClientRect(); return [r.left + (v.x + 1) / 2 * r.width, r.top + (1 - v.y) / 2 * r.height]; },
  leds: () => leds.map((l, i) => [l.id, ledColors[i]]),
};

// ------------------------------------------------------------------ polling
async function poll() {
  let next = POLL_MS;
  try {
    const url = DEMO ? './lib/demo-state.json' : './state?device=' + encodeURIComponent(DEVICE) + '&plc=' + encodeURIComponent(PLC);
    const r = await fetch(url, { cache: 'no-store', credentials: 'same-origin', headers: { Accept: 'application/json' } });
    if (r.status === 401 || r.status === 403) { state = { ok: false, reason: 'Login Required' }; next = 10000; }
    else if (!r.ok) state = { ok: false, reason: 'No Data From Gateway (' + r.status + ')' };
    else { state = await r.json(); $('updated').textContent = DEMO ? 'Demo Data (Static)' : 'Updated ' + new Date().toLocaleTimeString(); }
  } catch (e) { state = { ok: false, reason: 'No Data From Gateway' }; }
  if (!built) build(state);
  applyState();
  if (DEMO) { $('demo').hidden = false; return; }
  setTimeout(poll, next);
}
poll();
