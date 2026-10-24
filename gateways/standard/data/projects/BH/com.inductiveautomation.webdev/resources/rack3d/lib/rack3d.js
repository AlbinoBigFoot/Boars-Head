// PLC Rack 3D (CompactLogix 5370 L3 + 1769 Compact I/O), read only.
// Source: .cursor/tasks/plc-rack-3d/src/rack3d.js -> copied by build.py into the WebDev resource rack3d/lib.
// docs/plc-rack-3d.md. Units: millimetres (1 scene unit = 1 mm). Dimensions from Rockwell publications
// 1769-UM021 (L3 system dimensions), 1769-IN006/IN007/IN061/IN062/IN067 (I/O modules), 1769-IN015 (1769-ECR).
// Nothing here writes anything: it polls GET state every 2 s and only recolours LED instances / redraws labels.
import * as THREE from 'three';
import { OrbitControls } from './OrbitControls.js';
import { RoomEnvironment } from './RoomEnvironment.js';

const qs = new URLSearchParams(location.search);
const PLC = /^[A-Za-z0-9_-]{1,40}$/.test(qs.get('plc') || '') ? qs.get('plc') : 'RCP1';
const DARK = document.documentElement.getAttribute('data-theme') === 'dark';
const DEMO = qs.get('demo') === '1';
const POLL_MS = 2000;
const $ = (id) => document.getElementById(id);

// ------------------------------------------------------------------ real dimensions (mm)
const H = 118;                 // module body height (all 1769 + L3), 132 / 138 incl. mounting tabs
const D_IO = 87;               // 1769 I/O depth
const D_CTRL = 105;            // 1769-L3x depth (1769-UM021 system dimensions)
const W_CTRL = 55;             // 1769-L36ERM controller (1769-UM021 system dimensions)
const W_PS = 70, D_PS = 87;    // 1769 expansion power supply: the L3 has NO embedded supply (1769-UM021 p. 59/63:
                               // each bank needs its own 1769 power supply, within 4 slots of the controller)
const W_ECR = 18, D_ECR = 85;  // 1769-ECR right end cap (1769-IN015)
const WIDTH = { '1769-IF8': 52.5, '1769-OA16': 52.5, '1769-OW16': 52.5, '1769-IA16': 35, '1769-IQ16': 35 };
const PANEL_TXT = { '1769-IF8': 'ANALOG IN', '1769-IA16': '120V AC IN', '1769-IQ16': '24V DC IN',
  '1769-OA16': 'AC OUT', '1769-OW16': 'RELAY OUT' };

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
  throw new Error('rack3d: WebGL unavailable');   // stops the module; the message above stays
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
controls.enableDamping = true;
controls.dampingFactor = 0.12;
controls.minDistance = 120;
controls.maxDistance = 4000;
controls.maxPolarAngle = Math.PI * 0.92;
controls.screenSpacePanning = true;

scene.add(new THREE.HemisphereLight(THEME.hemiSky, THEME.hemiGround, THEME.hemi));
const sun = new THREE.DirectionalLight(0xffffff, THEME.sun);
sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048);
sun.shadow.bias = -0.0004;
sun.shadow.normalBias = 0.6;
sun.shadow.radius = 4;
scene.add(sun, sun.target);

// ------------------------------------------------------------------ shared geometry + materials
const BOX = new THREE.BoxGeometry(1, 1, 1);
const PLANE = new THREE.PlaneGeometry(1, 1);
const std = (color, rough = 0.6, metal = 0.05, extra = {}) =>
  new THREE.MeshStandardMaterial(Object.assign({ color, roughness: rough, metalness: metal }, extra));
const M = {
  body: std(0x3a3e42, 0.62),          // charcoal housing
  bodyDark: std(0x2a2d30, 0.7),
  door: std(0x8e959b, 0.5),           // light-gray hinged door (edges)
  tab: std(0x4b5055, 0.65),
  latch: std(0x5d6369, 0.55),
  lever: std(0x6f757b, 0.45),
  rtb: std(0x24272a, 0.75),
  screw: std(0xc0c4c8, 0.32, 0.9),
  rail: std(0xc7cbcf, 0.3, 0.85),
  port: std(0x16181a, 0.8),
  key: std(0x9aa0a6, 0.35, 0.7),
  panel: std(THEME.panel, 0.5, 0.5),   // galvanized sub-panel
};
const LED_GEO = new THREE.BoxGeometry(1.9, 1.15, 0.7);
const LED_MAT = new THREE.MeshBasicMaterial({ color: 0xffffff, toneMapped: false });
const SCREW_GEO = new THREE.CylinderGeometry(1.75, 1.75, 1.2, 24).rotateX(Math.PI / 2);
// terminal screw head: Phillips (default) or flat / slotted, a Designer-only setting per PLC (screwType in
// [default]_Config/PLCs/List, read through rack3d/state); colour map + bump map from one drawing, the instanced mesh
// takes the materials once at build time (nothing per frame)
function screwTex(bump, flat) {
  const c = document.createElement('canvas'); c.width = c.height = 128;
  const g = c.getContext('2d');
  g.fillStyle = bump ? '#c8c8c8' : '#b9bec3'; g.fillRect(0, 0, 128, 128);
  g.fillStyle = bump ? '#000' : '#2a2d30';
  if (flat) g.fillRect(6, 53, 116, 22);                          // single slot across the head
  else { g.fillRect(53, 20, 22, 88); g.fillRect(20, 53, 88, 22); g.beginPath(); g.arc(64, 64, 17, 0, 7); g.fill(); }   // Phillips cross
  const t = new THREE.CanvasTexture(c); t.colorSpace = bump ? THREE.NoColorSpace : THREE.SRGBColorSpace;
  t.anisotropy = 4; return t;
}
const SCREW_SIDE = new THREE.MeshStandardMaterial({ color: 0xb4b9be, roughness: 0.35, metalness: 0.9 });
let SCREW_MATS = null, SCREW_TYPE = 'phillips';
function setScrewType(t) {
  SCREW_TYPE = String(t || '').toLowerCase() === 'flat' ? 'flat' : 'phillips';
  const flat = SCREW_TYPE === 'flat';
  SCREW_MATS = [SCREW_SIDE, new THREE.MeshStandardMaterial({ map: screwTex(false, flat), bumpMap: screwTex(true, flat), bumpScale: 2.2, roughness: 0.4, metalness: 0.8 }), SCREW_SIDE];
}
setScrewType('phillips');
const M2 = { shell: new THREE.MeshStandardMaterial({ color: 0xb8bdc2, roughness: 0.35, metalness: 0.9 }),
  gold: new THREE.MeshStandardMaterial({ color: 0xd4a935, roughness: 0.3, metalness: 0.9 }),
  tongue: new THREE.MeshStandardMaterial({ color: 0x3b3f43, roughness: 0.6 }) };
const KEY_MAT_LIVE = new THREE.MeshStandardMaterial({ color: 0xc9a54a, roughness: 0.35, metalness: 0.85 });
const KEY_MAT_OFF = new THREE.MeshStandardMaterial({ color: 0x6f7479, roughness: 0.5, metalness: 0.5 });
const KEY_ANG = 0.68;   // RUN = up-left, REM = up, PROG = up-right (legend positions on the face)

function mesh(geo, mat, sx, sy, sz, x, y, z, parent, shadow = true) {
  const m = new THREE.Mesh(geo, mat);
  m.scale.set(sx, sy, sz);
  m.position.set(x, y, z);
  m.castShadow = shadow;
  m.receiveShadow = true;
  parent.add(m);
  return m;
}
// box with a texture only on its front (+z) face; BoxGeometry groups: +x, -x, +y, -y, +z, -z
function faceMats(edge, front) { return [edge, edge, edge, edge, front, edge]; }

// ------------------------------------------------------------------ canvas textures (procedural, no photos)
const PX = 10;   // texture pixels per mm
const FONT = '"Noto Sans", "Segoe UI", Arial, sans-serif';
function canvasTex(wmm, hmm, draw) {
  const c = document.createElement('canvas');
  c.width = Math.round(wmm * PX); c.height = Math.round(hmm * PX);
  const g = c.getContext('2d');
  g.scale(PX, PX);
  draw(g, wmm, hmm);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = ANISO;
  t.userData = { canvas: c, g, wmm, hmm, draw };
  return t;
}
function redraw(t, draw) {
  const { canvas, g, wmm, hmm } = t.userData;
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.clearRect(0, 0, canvas.width, canvas.height);
  g.scale(PX, PX);
  draw(g, wmm, hmm);
  t.needsUpdate = true;
}
function txt(g, s, x, y, size, color, align = 'left', weight = 600) {
  g.font = `${weight} ${size}px ${FONT}`;
  g.fillStyle = color; g.textAlign = align; g.textBaseline = 'middle';
  g.fillText(s, x, y);
}
function rrect(g, x, y, w, h, r) {
  g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r);
  g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath();
}
function fit(g, s, maxW, size) {
  g.font = `700 ${size}px ${FONT}`;
  while (size > 1.6 && g.measureText(s).width > maxW) { size -= 0.2; g.font = `700 ${size}px ${FONT}`; }
  return size;
}

// LED window layout (fractions of the window): label column + OK, then a 4 x 4 grid numbered 0-15 like the
// 1769 16-point indicator block (1769-IN006 / IN007 item 3). IF8 has only the module status LED (IN067 item 3).
const GRID_U0 = 0.25, GRID_DU = 0.1875, GRID_V = [0.18, 0.39, 0.61, 0.82];
const winCache = {};
function windowTex(kind, ww, wh) {
  const key = kind + ww;
  if (winCache[key]) return winCache[key];
  winCache[key] = canvasTex(ww, wh, (g) => {
    g.fillStyle = '#0d0f10'; g.fillRect(0, 0, ww, wh);
    g.strokeStyle = '#3c4146'; g.lineWidth = 0.35; g.strokeRect(0.2, 0.2, ww - 0.4, wh - 0.4);
    if (kind === 'AI') {
      txt(g, 'OK', ww * 0.11 + 2.0, wh * 0.5, 2.0, '#d9dde1', 'left');
      txt(g, 'ANALOG', ww * 0.6, wh * 0.5, 2.0, '#9aa1a8', 'center', 700);
      return;
    }
    txt(g, kind === 'DI' ? 'IN' : 'OUT', ww * 0.12, wh * 0.26, 2.0, '#d9dde1', 'center', 700);
    txt(g, 'OK', ww * 0.12, wh * 0.56, 1.7, '#d9dde1', 'center');
    for (let p = 0; p < 16; p++) {
      const u = GRID_U0 + (p % 4) * GRID_DU, v = GRID_V[Math.floor(p / 4)];
      txt(g, String(p), (u + 0.075) * ww, v * wh, 1.75, '#c9ced3', 'left', 600);
    }
  });
  return winCache[key];
}
function ledLocal(kind, ww, wh, p) {   // window-local (centre origin, +y up) LED position; p = -1 -> OK LED
  let u, v;
  if (p < 0) { u = kind === 'AI' ? 0.11 : 0.12; v = kind === 'AI' ? 0.5 : 0.8; }
  else { u = GRID_U0 + (p % 4) * GRID_DU + 0.035; v = GRID_V[Math.floor(p / 4)]; }
  return [(u - 0.5) * ww, (0.5 - v) * wh];
}

let ventTex = null;
function vents(w, d) {
  if (!ventTex) {
    ventTex = canvasTex(10, 10, (g) => {
      g.fillStyle = '#3a3e42'; g.fillRect(0, 0, 10, 10);
      g.fillStyle = '#141618'; g.fillRect(1.5, 2, 7, 1.6); g.fillRect(1.5, 6.4, 7, 1.6);
    });
    ventTex.wrapS = ventTex.wrapT = THREE.RepeatWrapping;
  }
  const t = ventTex.clone(); t.needsUpdate = true; t.repeat.set(Math.max(1, Math.round(w / 9)), Math.round(d / 9));
  return std(0xffffff, 0.7, 0.05, { map: t });
}
const ventMats = {};
function ventMat(w, d) { const k = w + 'x' + d; return ventMats[k] || (ventMats[k] = vents(w, d)); }

// door (front of the write-on label): module name, catalog, panel legend; IF8 adds live channel values
function drawDoor(g, w, h, card, values) {
  g.fillStyle = '#8f969c'; g.fillRect(0, 0, w, h);
  const gr = g.createLinearGradient(0, 0, w, 0);
  gr.addColorStop(0, 'rgba(255,255,255,0.10)'); gr.addColorStop(1, 'rgba(0,0,0,0.10)');
  g.fillStyle = gr; g.fillRect(0, 0, w, h);
  g.strokeStyle = '#6c7378'; g.lineWidth = 0.4; rrect(g, 0.6, 0.6, w - 1.2, h - 1.2, 1.2); g.stroke();
  // finger grip at the right edge (doors hinge on the left)
  g.fillStyle = '#737a80'; g.fillRect(w - 2.4, h * 0.42, 1.2, h * 0.16);
  // write-on label (user ID tag)
  const lx = 2.2, ly = 3, lw = w - 5.6, lh = h - 14;
  g.fillStyle = '#dedcd3'; g.fillRect(lx, ly, lw, lh);
  g.strokeStyle = '#c9c5b8'; g.lineWidth = 0.25;
  for (let y = ly + 12; y < ly + lh - 1; y += 4.2) { g.beginPath(); g.moveTo(lx + 1, y); g.lineTo(lx + lw - 1, y); g.stroke(); }
  const size = fit(g, card.name, lw - 2, 4.2);
  txt(g, card.name, lx + lw / 2, ly + 5, size, '#15181a', 'center', 700);
  txt(g, 'Slot ' + String(card.slot).padStart(2, '0'), lx + lw / 2, ly + 9.4, 2.4, '#4d5358', 'center', 600);
  if (values) {
    for (let i = 0; i < 8; i++) {
      const y = ly + 12 + 2.1 + i * 4.2 * 1.75;
      if (y > ly + lh - 2) break;
      txt(g, 'Ch' + i, lx + 1.2, y, 2.3, '#4d5358', 'left', 600);
      txt(g, values[i] || '--', lx + lw - 1.2, y, 2.6, values[i] ? '#15181a' : '#8a9096', 'right', 700);
    }
  }
  txt(g, PANEL_TXT[card.catalog] || '', w / 2, h - 8, 2.2, '#22272a', 'center', 700);
  txt(g, card.catalog, w / 2, h - 4.2, 2.6, '#15181a', 'center', 700);
}

// inside of the door: terminal identification label (1769-RTBN18, 18 terminals in two staggered columns)
// Terminal layout of the 1769-RTBN18 (9 rows x 2 columns, col 0 = left, col 1 = right) from the door-label drawings of
// 1769-IN006 (IA16), IN007 (IQ16), IN061 (OA16), IN062 (OW16): inputs have the even points in the right column and the
// odd ones on the left (IN 0 over IN 1 ... IN 14 / IN 15, then COM / COM); outputs have Out 0 | VAC 1, Out 2 | Out 1,
// ... VAC 2 | Out 7 ... Out 14 | Out 15. IF8 (IN067): two RTBs / 36 terminals as printed on its door (see ifInfo).
const ROLE = { 'AC COM': 'COM / AC Common', 'DC COM': 'COM / DC Common', 'VAC 1': 'VAC 1 / AC Output Supply',
  'VAC 2': 'VAC 2 / AC Output Supply', 'VAC-VDC 1': 'VAC-VDC 1 / Output Supply (AC Or DC)',
  'VAC-VDC 2': 'VAC-VDC 2 / Output Supply (AC Or DC)', 'ANLG COM': 'ANLG COM / Analog Common' };
// 1769-IF8 (IN067 p. 2 door label + p. 10 wiring): columns A (0) / B (1) = left RTB, channels 0-3; C (2) / D (3) = right RTB,
// channels 4-7. A / C: V/I in n-, ANLG Com, V/I in n+1- ... NC; B / D: V in n+, I in n+, V in n+1+ ... NC.
function ifInfo(row, col) {
  const base = col < 2 ? 0 : 4, minus = col === 0 || col === 2;
  if (row === 8) return { label: 'NC', pt: null, role: 'No Connection (Do Not Use As A Connection Point)', sig: 'NC' };
  if (minus) {
    if (row % 2) return { label: 'ANLG Com', pt: null, role: 'ANLG COM / Analog Common (Connected Across All Channels, Not To Earth Ground)', sig: 'COM' };
    const n = base + row / 2;
    return { label: 'V/I in ' + n + '-', pt: n, role: 'Channel ' + n + ' Return (V/I In -)', sig: 'MINUS' };
  }
  const n = base + (row >> 1);
  return row % 2 ? { label: 'I in ' + n + '+', pt: n, role: 'Channel ' + n + ' Current Input (I In +)', sig: 'I' }
                 : { label: 'V in ' + n + '+', pt: n, role: 'Channel ' + n + ' Voltage Input (V In +)', sig: 'V' };
}
function termInfo(cat, row, col) {
  const out = (cat === '1769-OA16' || cat === '1769-OW16');
  if (cat === '1769-IF8') {   // 1769-IN067 door label: two RTBs, four columns x 9 rows (36 terminals), see ifInfo()
    return ifInfo(row, col);
  }
  if (!out) {
    if (row === 8) { const l = cat === '1769-IQ16' ? 'DC COM' : 'AC COM'; return { label: l, pt: null, role: ROLE[l] }; }
    const n = row * 2 + (col ? 0 : 1);
    return { label: 'IN ' + n, pt: n, role: null };
  }
  const v = cat === '1769-OW16' ? 'VAC-VDC ' : 'VAC ';
  if (row === 0) return col ? { label: v + '1', pt: null, role: ROLE[v + '1'] } : { label: 'OUT 0', pt: 0, role: null };
  if (row === 4) return col ? { label: 'OUT 7', pt: 7, role: null } : { label: v + '2', pt: null, role: ROLE[v + '2'] };
  const n = row < 4 ? (col ? 2 * row - 1 : 2 * row) : (col ? 2 * row - 1 : 2 * row - 2);
  return { label: 'OUT ' + n, pt: n, role: null };
}
const termCache = {};
function termMat(catalog, w, h) {
  const key = catalog + w;
  if (termCache[key]) return termCache[key];
  const tex = canvasTex(w, h, (g) => {
    g.fillStyle = '#8f969c'; g.fillRect(0, 0, w, h);
    g.fillStyle = '#e9e7df'; g.fillRect(2, 3, w - 4, h - 6);
    g.strokeStyle = '#9b978b'; g.lineWidth = 0.25;
    const rows = 9, rh = (h - 10) / rows;
    for (let r = 0; r <= rows; r++) { g.beginPath(); g.moveTo(3, 5 + r * rh); g.lineTo(w - 3, 5 + r * rh); g.stroke(); }
    g.beginPath(); g.moveTo(w / 2, 5); g.lineTo(w / 2, h - 5); g.stroke();
    if (catalog === '1769-IF8') for (const f of [0.25, 0.75]) { g.beginPath(); g.moveTo(w * f, 5); g.lineTo(w * f, h - 5); g.stroke(); }
    if (catalog === '1769-IF8') {   // four label columns (two RTBs), as printed on the real door
      for (let i = 0; i < 36; i++) {
        const col = i % 4, r = i >> 2;
        txt(g, termInfo(catalog, r, col).label, w * (0.125 + 0.25 * col), 5 + r * rh + rh / 2, Math.min(1.9, w / 17), '#15181a', 'center', 600);
      }
    } else for (let i = 0; i < 18; i++) {
      const col = i % 2, r = i >> 1;
      txt(g, termInfo(catalog, r, col).label, col ? w * 0.75 : w * 0.25, 5 + r * rh + rh / 2, Math.min(2.4, w / 13), '#15181a', 'center', 600);
    }
    txt(g, catalog, w / 2, h - 2.2, 1.8, '#15181a', 'center', 700);
  });
  tex.flipY = true;
  return (termCache[key] = new THREE.MeshStandardMaterial({ map: tex, roughness: 0.6 }));
}

// L36ERM controller section face (55 x 118): label strip, status LED block (RUN/FORCE/I/O/OK | NS/LINK 1/LINK 2/SD,
// 1769-UM021 status indicators), SD card + mode switch door, USB, EtherNet/IP port legend (ports are underneath)
const CTRL_LED = { RUN: [19.2, 15], FORCE: [19.2, 21], IO: [19.2, 27], OK: [19.2, 33],
  NS: [33.6, 15], LINK1: [33.6, 21], LINK2: [33.6, 27], SD: [33.6, 33] };
function drawCtrl(g, w, h, name, proj) {
  g.fillStyle = '#41464b'; g.fillRect(0, 0, w, h);
  g.fillStyle = '#9ba1a7'; g.fillRect(0, 0, w, 8.5);                         // top legend strip
  txt(g, 'CompactLogix', 2, 4.3, 3.0, '#15181a', 'left', 700);
  txt(g, 'L36ERM', w - 2, 4.3, 3.0, '#15181a', 'right', 700);
  g.fillStyle = '#0e1011'; rrect(g, 3, 10.5, w - 6, 26, 1); g.fill();       // LED window
  const L = [['RUN', 'RUN'], ['FORCE', 'FORCE'], ['I/O', 'IO'], ['OK', 'OK']];
  const R = [['NS', 'NS'], ['LINK 1', 'LINK1'], ['LINK 2', 'LINK2'], ['SD', 'SD']];
  L.forEach(([s, k]) => txt(g, s, CTRL_LED[k][0] - 2.4, CTRL_LED[k][1], 2.3, '#d9dde1', 'right'));
  R.forEach(([s, k]) => txt(g, s, CTRL_LED[k][0] + 2.4, CTRL_LED[k][1], 2.3, '#d9dde1', 'left'));
  g.strokeStyle = '#2a2e31'; g.lineWidth = 0.5;
  g.beginPath(); g.moveTo(0, 39.5); g.lineTo(w, 39.5); g.moveTo(0, 66); g.lineTo(w, 66); g.stroke();
  // SD / mode switch door area
  txt(g, 'RUN', 6.5, 44, 1.9, '#d9dde1', 'center'); txt(g, 'REM', 13, 43, 1.9, '#d9dde1', 'center');
  txt(g, 'PROG', 19.8, 44, 1.9, '#d9dde1', 'center');
  g.strokeStyle = '#7d848a'; g.lineWidth = 0.35; rrect(g, 29, 42.5, 21, 20, 1); g.stroke();
  txt(g, 'SD', 39.5, 47, 2.4, '#d9dde1', 'center', 700);
  g.fillStyle = '#1b1e20'; g.fillRect(31.5, 55, 16, 2.2);
  // USB + MAC label + EtherNet/IP legend
  txt(g, 'USB', 11, 72, 2.0, '#d9dde1', 'center');
  g.fillStyle = '#c9ccce'; g.fillRect(6, 90, w - 12, proj ? 9 : 6);
  txt(g, name || 'PLC', w / 2, 93.4, 3.4, '#15181a', 'center', 700);
  if (proj) txt(g, proj, w / 2, 97.3, 1.7, '#3b4147', 'center', 600);
  txt(g, 'EtherNet/IP', 4, 106, 2.6, '#d9dde1', 'left', 700);
  txt(g, '1 (Front)', w - 3, 104.5, 1.9, '#c9ced3', 'right'); txt(g, '2 (Rear)', w - 3, 108, 1.9, '#c9ced3', 'right');
  txt(g, '1769-L36ERM', w / 2, 114, 2.4, '#c9ced3', 'center', 700);
}
// embedded 24V DC power supply section face (70 x 118): DC PWR lamp, legend, terminal door, 3 input terminals
const PS_LED = [55, 14];
const PS_TERM = [[14, 106], [35, 106], [56, 106]];
function drawPs(g, w, h) {
  g.fillStyle = '#41464b'; g.fillRect(0, 0, w, h);
  g.fillStyle = '#9ba1a7'; g.fillRect(0, 0, w, 8.5);
  txt(g, 'Compact I/O Power Supply', 3, 4.3, 2.8, '#15181a', 'left', 700);
  g.fillStyle = '#0e1011'; rrect(g, 44, 10.5, 22, 7, 1); g.fill();
  txt(g, 'POWER', PS_LED[0] - 2.4, PS_LED[1], 2.2, '#d9dde1', 'right');
  txt(g, '1769 PSU', 4, 24, 5, '#e6e9ec', 'left', 700);
  txt(g, 'Catalog Not In L5X', 4, 30, 2.4, '#c9ced3', 'left');
  g.strokeStyle = '#2a2e31'; g.lineWidth = 0.5;
  g.beginPath(); g.moveTo(0, 35); g.lineTo(w, 35); g.stroke();
  g.strokeStyle = '#7d848a'; g.lineWidth = 0.4; rrect(g, 3, 38, w - 6, 50, 1.5); g.stroke();     // terminal door
  g.fillStyle = '#737a80'; g.fillRect(w - 6, 58, 1.2, 10);
  txt(g, 'Do Not Remove Under Power', w / 2, 82, 2.0, '#c9ced3', 'center');
  g.fillStyle = '#1d2023'; rrect(g, 4, 92, w - 8, 22, 1); g.fill();                       // terminal strip
  ['L1 / +', 'L2 / -', 'GND'].forEach((s, i) => txt(g, s, PS_TERM[i][0], 96.5, 2.1, '#d9dde1', 'center'));
}

// ------------------------------------------------------------------ shared port / key geometry (built once)
function polyShape(pts) { const sh = new THREE.Shape(); pts.forEach(([x, y], i) => (i ? sh.lineTo(x, y) : sh.moveTo(x, y))); sh.closePath(); return sh; }
function ringGeo(outer, hole, depth) {
  const sh = polyShape(outer); sh.holes.push(polyShape(hole));
  return new THREE.ExtrudeGeometry(sh, { depth, bevelEnabled: false });
}
const USB_OUT = [[-4.2, -3.9], [4.2, -3.9], [4.2, 2.0], [2.3, 3.9], [-2.3, 3.9], [-4.2, 2.0]];
const USB_IN = [[-3.6, -3.3], [3.6, -3.3], [3.6, 1.75], [2.05, 3.3], [-2.05, 3.3], [-3.6, 1.75]];
const USB_RING = ringGeo(USB_OUT, USB_IN, 1.5);
const USB_CAV = new THREE.ShapeGeometry(polyShape(USB_IN));
const RJ_OUT = [[-8.6, -7.6], [8.6, -7.6], [8.6, 9.0], [-8.6, 9.0]];
const RJ_IN = [[-7.7, -6.7], [7.7, -6.7], [7.7, 6.7], [3.3, 6.7], [3.3, 8.2], [-3.3, 8.2], [-3.3, 6.7], [-7.7, 6.7]];   // jack + latch notch
// extrude / shape in XY, then rotate so the opening faces down (-y): shape y -> world z, extrusion -> -y
const RJ_RING = ringGeo(RJ_OUT, RJ_IN, 0.9).rotateX(Math.PI / 2);
const RJ_CAV = new THREE.ShapeGeometry(polyShape(RJ_IN)).rotateX(Math.PI / 2);
const KEY_BEZEL = new THREE.CylinderGeometry(4.6, 4.6, 1.2, 32).rotateX(Math.PI / 2);
const KEY_GEO = (() => {   // key blade, pointing up (+y) in its rest pose; rotation.z turns it
  const sh = new THREE.Shape();
  sh.moveTo(-1.5, -3.6); sh.lineTo(1.5, -3.6); sh.lineTo(1.5, 3.0); sh.absarc(0, 3.0, 1.5, 0, Math.PI, false); sh.lineTo(-1.5, -3.6);
  const h = new THREE.Path(); h.absarc(0, 0, 0.8, 0, Math.PI * 2, true); sh.holes.push(h);
  return new THREE.ExtrudeGeometry(sh, { depth: 1.2, bevelEnabled: true, bevelThickness: 0.2, bevelSize: 0.2, bevelSegments: 1 });
})();

// ------------------------------------------------------------------ rack build (once)
const hit = [];          // raycast targets (userData.card)
const cards = [];        // {kind, slot, member, name, catalog, type, w, d, x, group, pivot, ledIdx[], okIdx, doorTex}
let ledMesh = null, ledColors = [];
let screwsMesh = null, screwMeta = [], screwXYZ = [], termProxy = null, termBox = null, hlTerm = -1;
const WHITE = new THREE.Color(1, 1, 1), AMBER = new THREE.Color(1.0, 0.62, 0.1);
let rackW = 0, built = false;
const doorGeo = BOX;

// Panduit-style slotted wiring duct: U-channel (base + two slotted finger walls), snap-on cover segments with a lip at
// both ends (open in the middle), mounting clips + screws, soft contact shadows.
// Shared geometry (BOX), instanced clips / screws, drawn once; nothing is allocated per frame.
function rrectPath(g, x, y, w, h, r) {
  g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r);
  g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath();
}
function buildDucts() {
  const RL = rackW + 120, DH = 60, DD = 70, WT = 2.4;
  const cssHex = (n) => '#' + n.toString(16).padStart(6, '0');
  const baseTex = canvasTex(25, DH, (g) => {                      // base: mounting slot
    g.fillStyle = cssHex(THEME.duct); g.fillRect(0, 0, 25, DH);
    g.fillStyle = THEME.slot; rrectPath(g, 9.5, 6, 6, DH - 12, 3); g.fill();
  });
  const wallTex = canvasTex(25, DD, (g) => {                      // side walls: evenly spaced finger slots, rounded ends
    g.fillStyle = cssHex(THEME.duct); g.fillRect(0, 0, 25, DD);
    g.fillStyle = THEME.slot; rrectPath(g, 8, 10, 9, DD - 14, 4.5); g.fill();
    g.fillStyle = 'rgba(255,255,255,0.18)'; g.fillRect(0, 0, 25, 2.5);
  });
  baseTex.wrapS = wallTex.wrapS = THREE.RepeatWrapping;
  baseTex.repeat.set(RL / 25, 1); wallTex.repeat.set(RL / 25, 1);
  const mBase = std(0xffffff, 0.4, 0.02, { map: baseTex });
  const mWall = std(0xffffff, 0.38, 0.02, { map: wallTex });
  const mEdge = std(THEME.duct, 0.4, 0.02);
  const mCover = std(THEME.ductCover, 0.3, 0.02);
  const wallMats = [mEdge, mEdge, mWall, mWall, mEdge, mEdge];     // +y / -y faces slotted
  const clips = [];
  const mtx = new THREE.Matrix4(), q = new THREE.Quaternion(), sc = new THREE.Vector3(), ps = new THREE.Vector3();
  const shadowTex = canvasTex(8, 64, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h);
    gr.addColorStop(0, 'rgba(0,0,0,0)'); gr.addColorStop(0.33, 'rgba(0,0,0,0.5)'); gr.addColorStop(0.67, 'rgba(0,0,0,0.5)'); gr.addColorStop(1, 'rgba(0,0,0,0)');
    g.fillStyle = gr; g.fillRect(0, 0, w, h);
  });
  const shadowMat = new THREE.MeshBasicMaterial({ map: shadowTex, transparent: true, opacity: DARK ? 0.55 : 0.32, depthWrite: false, toneMapped: false });
  const capL = RL * 0.2, capMid = [-RL / 2 + capL / 2, RL / 2 - capL / 2];
  [1, -1].forEach((sgn) => {
    const cy = sgn * (H / 2 + 85), cz = -9 + 1.5 + DD / 2 - 3, x0 = rackW / 2;
    // soft contact shadow on the sub-panel around the duct (ambient-occlusion feel)
    const sh = new THREE.Mesh(PLANE, shadowMat); sh.scale.set(RL + 40, DH + 56, 1); sh.position.set(x0, cy - sgn * 4, -7.2); sh.renderOrder = 1; scene.add(sh);
    mesh(BOX, mBase, RL, DH, 2.4, x0, cy, -6.3, scene);                                       // base
    [1, -1].forEach((w) => mesh(BOX, wallMats, RL, WT, DD - 2, x0, cy + w * (DH / 2 - WT / 2), cz + 1, scene));   // finger walls
    capMid.forEach((cx) => {                                                                 // snap-on cover segments
      mesh(BOX, mCover, capL, DH + 3, 1.8, x0 + cx, cy, cz + DD / 2 - 0.4, scene);
      [1, -1].forEach((w) => mesh(BOX, mCover, capL, 2, 5.5, x0 + cx, cy + w * (DH / 2 + 1.4), cz + DD / 2 - 2.9, scene));  // lip edges
      [1, -1].forEach((w) => mesh(BOX, mCover, 1.8, DH + 3, 5.5, x0 + cx + w * capL / 2, cy, cz + DD / 2 - 2.9, scene));   // end walls
    });
    // mounting clips (panel tabs) + screws along both edges, and a DIN-rail clip at each end
    const step = 105;
    for (let x = -RL / 2 + 50; x <= RL / 2 - 30; x += step) {
      [1, -1].forEach((w) => clips.push([x0 + x, cy + w * (DH / 2 + 3.5), -5.2, 14, 5, 2.6]));
    }
    [-1, 1].forEach((w) => clips.push([x0 + w * (RL / 2 - 14), cy, -5, 22, 18, 3.4]));
  });
  const cm = new THREE.InstancedMesh(BOX, std(0x8f9398, 0.5, 0.6), clips.length);
  clips.forEach((c, i) => { q.identity(); sc.set(c[3], c[4], c[5]); ps.set(c[0], c[1], c[2]); mtx.compose(ps, q, sc); cm.setMatrixAt(i, mtx); });
  cm.instanceMatrix.needsUpdate = true; cm.castShadow = cm.receiveShadow = true; scene.add(cm);
  const sm = new THREE.InstancedMesh(SCREW_GEO, SCREW_MATS, clips.length);
  clips.forEach((c, i) => { q.identity(); sc.set(0.9, 0.9, 0.9); ps.set(c[0], c[1], c[2] + c[5] / 2 + 0.2); mtx.compose(ps, q, sc); sm.setMatrixAt(i, mtx); });
  sm.instanceMatrix.needsUpdate = true; scene.add(sm);
}

function build(st) {
  setScrewType(st && st.screwType);
  const items = [{ kind: 'controller', member: 'Controller', name: st.plc || PLC, projName: (st.controller || {}).name || '',
    catalog: (st.controller || {}).catalog || '1769-L36ERM', w: W_CTRL, d: D_CTRL },
    { kind: 'power', member: 'PowerSupply', name: 'Bank Power Supply', catalog: '1769 Power Supply', w: W_PS, d: D_PS }];
  (st.slots || []).forEach((s) => items.push({ kind: 'card', slot: s.slot, member: s.member, name: s.name,
    catalog: s.catalog, type: s.type, description: s.description, w: WIDTH[s.catalog] || 35, d: D_IO }));
  items.push({ kind: 'endcap', member: 'EndCap', name: 'Right End Cap', catalog: '1769-ECR', w: W_ECR, d: D_ECR });

  let x = 0;
  const ledPos = [];   // world positions
  const screwPos = [];
  items.forEach((it) => { it.x = x; x += it.w; });
  rackW = x;

  // back-panel, DIN rail (EN 50022 35 x 7.5 top hat), wire ducts above / below
  const PW = rackW + 220;
  const back = mesh(BOX, M.panel, PW, 520, 3, rackW / 2, 0, -9, scene, false);
  back.receiveShadow = true;
  const RL = rackW + 120;
  mesh(BOX, M.rail, RL, 27, 1, rackW / 2, 0, -7, scene, false);
  mesh(BOX, M.rail, RL, 1, 7.5, rackW / 2, 13, -3.75, scene, false);
  mesh(BOX, M.rail, RL, 1, 7.5, rackW / 2, -13, -3.75, scene, false);
  mesh(BOX, M.rail, RL, 4.5, 1, rackW / 2, 15.25, -0.5, scene, false);
  mesh(BOX, M.rail, RL, 4.5, 1, rackW / 2, -15.25, -0.5, scene, false);

  items.forEach((it) => {
    const g = new THREE.Group();
    g.position.x = it.x + it.w / 2;
    scene.add(g);
    const card = Object.assign({}, it, { group: g, ledIdx: [], okIdx: -1, ctrlIdx: {} });
    cards.push(card);
    const w = it.w, d = it.d;
    // panel mounting tabs (132 mm overall) and DIN latches
    if (it.kind !== 'endcap') {
      mesh(BOX, M.tab, Math.min(14, w * 0.4), 7, 5, -w * 0.18, H / 2 + 3.5, 4, g);
      mesh(BOX, M.tab, Math.min(14, w * 0.4), 7, 5, -w * 0.18, -H / 2 - 3.5, 4, g);
      mesh(BOX, M.latch, 9, 5, 7, w * 0.22, -H / 2 - 2.5, 13, g);
      mesh(BOX, M.latch, 9, 3, 7, w * 0.22, H / 2 + 1.5, 13, g);
    }
    if (it.kind === 'card') buildCard(card, g, ledPos, screwPos);
    else if (it.kind === 'controller') buildController(card, g, ledPos, screwPos);
    else if (it.kind === 'power') buildPower(card, g, ledPos, screwPos);
    else buildEndCap(card, g);
    // dim veil (focus mode): a translucent box in the background colour; only its opacity is animated
    card.veilMat = new THREE.MeshBasicMaterial({ color: THEME.bg, transparent: true, opacity: 0, depthWrite: false, toneMapped: false });
    const veil = new THREE.Mesh(BOX, card.veilMat);
    veil.scale.set(w + 0.8, H + 16, d + 1.5); veil.position.set(0, 0, d / 2 + 0.2); veil.renderOrder = 2; veil.visible = false;
    g.add(veil); card.veil = veil;
  });

  buildDucts();

  // instanced LEDs (all cards + controller) and terminal screws
  ledMesh = new THREE.InstancedMesh(LED_GEO, LED_MAT, ledPos.length);
  const mtx = new THREE.Matrix4();
  ledPos.forEach((p, i) => { mtx.makeTranslation(p.x, p.y, p.z); ledMesh.setMatrixAt(i, mtx); ledMesh.setColorAt(i, LED.off); });
  ledColors = ledPos.map(() => 'off');
  ledMesh.instanceMatrix.needsUpdate = true; ledMesh.instanceColor.needsUpdate = true;
  scene.add(ledMesh);
  const screws = new THREE.InstancedMesh(SCREW_GEO, SCREW_MATS, screwPos.length);
  screwPos.forEach((p, i) => { mtx.makeTranslation(p.x, p.y, p.z); screws.setMatrixAt(i, mtx); screws.setColorAt(i, WHITE); });
  screws.instanceMatrix.needsUpdate = true; screws.instanceColor.needsUpdate = true;
  screws.castShadow = true;
  scene.add(screws);
  screwsMesh = screws; screwMeta = screwPos.map((q) => q.meta || null); screwXYZ = screwPos;
  // invisible, larger hit boxes (one instanced mesh) for terminal hover
  termProxy = new THREE.InstancedMesh(BOX, new THREE.MeshBasicMaterial({ visible: false }), screwPos.length);
  const sc3 = new THREE.Vector3(), q0 = new THREE.Quaternion();
  const COARSE = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);   // touch: bigger hit areas
  screwPos.forEach((p, i) => { const tw = p.meta ? p.meta.tw : 4; sc3.set(COARSE ? tw * 1.15 : tw, COARSE ? 9.2 : 8.4, 6); mtx.compose(p, q0, sc3); termProxy.setMatrixAt(i, mtx); });
  termProxy.instanceMatrix.needsUpdate = true; termProxy.computeBoundingSphere();
  scene.add(termProxy);
  termBox = new THREE.LineSegments(new THREE.EdgesGeometry(BOX), new THREE.LineBasicMaterial({ color: 0xffb000 }));
  termBox.visible = false; scene.add(termBox);

  // hover / selection outlines (one shared edge geometry, scaled to the card)
  const edges = new THREE.EdgesGeometry(BOX);
  hoverBox = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: THEME.hover }));
  selBox = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: THEME.sel }));
  hoverBox.visible = selBox.visible = false;
  scene.add(hoverBox, selBox);

  // shadow camera covers the bank
  sun.position.set(rackW * 0.35, 520, 900);
  sun.target.position.set(rackW / 2, 0, 0);
  const sc = sun.shadow.camera;
  sc.left = -rackW * 0.75; sc.right = rackW * 0.75; sc.top = 380; sc.bottom = -380; sc.near = 50; sc.far = 3000;
  sc.updateProjectionMatrix();
  resetView(true);
  built = true;
}

function worldOf(g, x, y, z) { return new THREE.Vector3(g.position.x + x, y, z); }

function buildCard(card, g, ledPos, screwPos) {
  const w = card.w, d = card.d, F = d;   // front plane at z = d
  const kind = card.type === 'AI' ? 'AI' : card.type === 'DO' ? 'DO' : 'DI';
  const b = mesh(BOX, M.body, w - 0.5, H, d - 6, 0, 0, (d - 6) / 2, g);
  b.userData.card = card; hit.push(b);
  mesh(PLANE, ventMat(w - 6, d - 24), w - 6, d - 24, 1, 0, H / 2 + 0.02, (d - 6) / 2 + 2, g, false).rotation.x = -Math.PI / 2;
  // upper front block with the LED window, lower lip
  const top = mesh(BOX, M.body, w - 0.5, 22, 6, 0, H / 2 - 11, F - 3, g);
  top.userData.card = card; hit.push(top);
  mesh(BOX, M.body, w - 0.5, 4, 6, 0, -H / 2 + 2, F - 3, g).userData.card = card;
  const ww = w - 7, wh = 15, wy = H / 2 - 11.5;
  const win = new THREE.Mesh(PLANE, new THREE.MeshStandardMaterial({ map: windowTex(kind, ww, wh), roughness: 0.25, metalness: 0 }));
  win.scale.set(ww, wh, 1); win.position.set(0, wy, F + 0.05); g.add(win);
  const okP = ledLocal(kind, ww, wh, -1);
  card.okIdx = ledPos.length; ledPos.push(worldOf(g, okP[0], wy + okP[1], F + 0.3));
  if (kind !== 'AI') {
    for (let p = 0; p < 16; p++) {
      const lp = ledLocal(kind, ww, wh, p);
      card.ledIdx.push(ledPos.length); ledPos.push(worldOf(g, lp[0], wy + lp[1], F + 0.3));
    }
  }
  // removable terminal block (18 screws, 1769-RTBN18) behind the door
  const rtbH = 88, rtbY = -H / 2 + 4 + rtbH / 2 + 0.5;
  if (card.catalog === '1769-IF8') {   // two RTBs side by side, four staggered screw columns of 9 (36 terminals)
    const bw = (w - 8) / 2;
    mesh(BOX, M.rtb, bw, rtbH, 4, -(bw / 2 + 0.5), rtbY, F - 8, g);
    mesh(BOX, M.rtb, bw, rtbH, 4, bw / 2 + 0.5, rtbY, F - 8, g);
    for (let i = 0; i < 36; i++) {
      const col = i % 4, row = i >> 2;
      const sp = worldOf(g, (col - 1.5) * 0.235 * w, rtbY + rtbH / 2 - 6 - row * 9.5 - (col % 2 ? 0 : 4.7), F - 5.4);
      sp.meta = { card, row, col, i, tw: w * 0.2 }; screwPos.push(sp);
    }
  } else {
    mesh(BOX, M.rtb, w - 6, rtbH, 4, 0, rtbY, F - 8, g);
    for (let i = 0; i < 18; i++) {
      const col = i % 2, row = Math.floor(i / 2);
      const sp = worldOf(g, (col ? 0.14 : -0.14) * w + (kind === 'AI' ? 0 : -2), rtbY + rtbH / 2 - 6 - row * 9.5 - col * 4.7, F - 5.4);
      sp.meta = { card, row, col, i, tw: (w - 6) * 0.42 }; screwPos.push(sp);
    }
  }
  // bus lever on the top face (front left)
  mesh(BOX, M.lever, 5, 3, 10, -w / 2 + 5, H / 2 + 1.5, F - 16, g);
  // hinged door (hinge on the left edge): front face = write-on label texture
  const pivot = new THREE.Group();
  pivot.position.set(-w / 2 + 0.6, rtbY, F - 1.6);
  g.add(pivot);
  const dw = w - 1.4;
  card.doorTex = canvasTex(dw, rtbH, (gg, a, bb) => drawDoor(gg, a, bb, card, kind === 'AI' ? [] : null));
  const dm = faceMats(M.door, new THREE.MeshStandardMaterial({ map: card.doorTex, roughness: 0.55 }));
  dm[5] = termMat(card.catalog, dw, rtbH);   // back of the door (-z): terminal identification label
  const door = new THREE.Mesh(doorGeo, dm);
  door.scale.set(dw, rtbH, 2.4); door.position.set(dw / 2, 0, 0);
  door.castShadow = true; door.receiveShadow = true;
  door.userData.card = card; hit.push(door);
  pivot.add(door);
  card.pivot = pivot; card.doorTarget = 0;
}

function buildController(card, g, ledPos, screwPos) {
  const w = card.w, d = card.d, F = d;
  const b = mesh(BOX, M.body, w - 0.5, H, d - 4, 0, 0, (d - 4) / 2, g);
  b.userData.card = card; hit.push(b);
  mesh(PLANE, ventMat(W_CTRL - 8, d - 30), W_CTRL - 8, d - 30, 1, 0, H / 2 + 0.02, d / 2, g, false).rotation.x = -Math.PI / 2;
  card.ctrlTex = canvasTex(W_CTRL, H, (gg, a, bb) => drawCtrl(gg, a, bb, card.name, card.projName));
  const cx = 0;
  const cf = new THREE.Mesh(BOX, faceMats(M.bodyDark, new THREE.MeshStandardMaterial({ map: card.ctrlTex, roughness: 0.5 })));
  cf.scale.set(W_CTRL - 0.6, H, 4); cf.position.set(cx, 0, F - 2); cf.castShadow = cf.receiveShadow = true;
  cf.userData.card = card; hit.push(cf); g.add(cf);
  const at = (x0, xmm, ymm) => [x0 - W_CTRL / 2 + xmm, H / 2 - ymm];
  Object.keys(CTRL_LED).forEach((k) => {
    const [lx, ly] = at(cx, CTRL_LED[k][0], CTRL_LED[k][1]);
    card.ctrlIdx[k] = ledPos.length; ledPos.push(worldOf(g, lx, ly, F + 0.3));
  });
  // 3-position mode keyswitch (RUN / REM / PROG): the blade is a pivot that turns to the live position
  const [kx, ky] = at(cx, 13, 52);
  const bezel = new THREE.Mesh(KEY_BEZEL, M.key); bezel.position.set(kx, ky, F + 0.6); bezel.castShadow = true; g.add(bezel);
  const keyPivot = new THREE.Group(); keyPivot.position.set(kx, ky, F + 1.7); g.add(keyPivot);
  const blade = new THREE.Mesh(KEY_GEO, KEY_MAT_OFF); blade.castShadow = true; keyPivot.add(blade);
  card.keyPivot = keyPivot; card.keyBlade = blade; card.keyTarget = 0; card.keyLast = null;
  const [sx, sy] = at(cx, 39.5, 52.5);
  mesh(BOX, M.bodyDark, 20, 19, 0.8, sx, sy, F + 0.4, g, false);
  // USB 2.0 Type-B receptacle (UM021: "USB port that uses a Type B receptacle", 12 Mbps): chamfered metal shell,
  // dark recess, tongue with 4 contacts
  const [ux, uy] = at(cx, 11, 79.5);
  const usb = new THREE.Group(); usb.position.set(ux, uy, F); g.add(usb);
  const ring = new THREE.Mesh(USB_RING, M2.shell); ring.position.z = 0; usb.add(ring);
  const cav = new THREE.Mesh(USB_CAV, M.port); cav.position.z = 0.1; usb.add(cav);
  const tg = new THREE.Mesh(BOX, M2.tongue); tg.scale.set(6.0, 1.1, 1.2); tg.position.set(0, -1.1, 0.7); usb.add(tg);
  for (let i = 0; i < 4; i++) { const ct = new THREE.Mesh(BOX, M2.gold); ct.scale.set(0.8, 0.3, 1.0); ct.position.set(-2.1 + i * 1.4, -0.45, 0.75); usb.add(ct); }
  // two RJ45 jacks on the bottom (UM021: "The ports are on the bottom of the controller", Port 1 front, Port 2 rear)
  [F - 17, F - 42].forEach((z0, n) => {
    const r = new THREE.Mesh(RJ_RING, M2.shell); r.position.set(cx - 4, -H / 2, z0); g.add(r);
    const c = new THREE.Mesh(RJ_CAV, M.port); c.position.set(cx - 4, -H / 2 - 0.02, z0); g.add(c);
    for (let i = 0; i < 8; i++) {                                           // 8 contacts on the wall opposite the latch notch
      const ct = new THREE.Mesh(BOX, M2.gold); ct.scale.set(0.7, 0.5, 3.2);
      ct.position.set(cx - 4 - 5.4 + i * 1.54, -H / 2 - 0.3, z0 - 5.2); g.add(ct);
    }
    const lt = new THREE.Mesh(BOX, M2.tongue); lt.scale.set(6.2, 0.6, 1.6); lt.position.set(cx - 4, -H / 2 - 0.35, z0 + 7.1); g.add(lt);   // plastic latch key
  });
}

function buildPower(card, g, ledPos, screwPos) {
  // 1769 expansion power supply (70 mm, 1769-UM021 p. 68): catalog not in the L5X, confirm on the panel (R4)
  const w = card.w, d = card.d, F = d;
  const b = mesh(BOX, M.body, w - 0.5, H, d - 4, 0, 0, (d - 4) / 2, g);
  b.userData.card = card; hit.push(b);
  mesh(PLANE, ventMat(w - 10, d - 24), w - 10, d - 24, 1, 0, H / 2 + 0.02, d / 2, g, false).rotation.x = -Math.PI / 2;
  const pf = new THREE.Mesh(BOX, faceMats(M.bodyDark, new THREE.MeshStandardMaterial({ map: canvasTex(W_PS, H, drawPs), roughness: 0.5 })));
  pf.scale.set(w - 0.6, H, 4); pf.position.set(0, 0, F - 2); pf.castShadow = pf.receiveShadow = true;
  pf.userData.card = card; hit.push(pf); g.add(pf);
  const at = (xmm, ymm) => [-W_PS / 2 + xmm, H / 2 - ymm];
  const [plx, ply] = at(PS_LED[0], PS_LED[1]);
  card.pwrIdx = ledPos.length; ledPos.push(worldOf(g, plx, ply, F + 0.3));
  PS_TERM.forEach(([tx, ty]) => { const [sx, sy] = at(tx, ty); screwPos.push(worldOf(g, sx, sy, F + 0.2)); });
  mesh(BOX, M.lever, 5, 3, 10, -w / 2 + 5, H / 2 + 1.5, F - 16, g);
}

function buildEndCap(card, g) {
  // 1769-ECR: 18 mm visible front, rounded top, hooks behind the last module (32 mm incl. tongue), 85 mm deep
  const s = new THREE.Shape();
  const w = W_ECR;
  s.moveTo(-w / 2, -H / 2); s.lineTo(w / 2 - 3, -H / 2); s.quadraticCurveTo(w / 2, -H / 2, w / 2, -H / 2 + 4);
  s.lineTo(w / 2, H / 2 - 9); s.quadraticCurveTo(w / 2, H / 2, w / 2 - 7, H / 2); s.lineTo(-w / 2, H / 2); s.lineTo(-w / 2, -H / 2);
  const geo = new THREE.ExtrudeGeometry(s, { depth: D_ECR - 4, bevelEnabled: true, bevelThickness: 2, bevelSize: 0.8, bevelSegments: 2 });
  const m = new THREE.Mesh(geo, M.body);
  m.position.set(0, 0, 1); m.castShadow = m.receiveShadow = true; m.userData.card = card; hit.push(m); g.add(m);
  mesh(BOX, M.lever, 5, 4, 9, -2, H / 2 + 1.5, D_ECR - 14, g);
  mesh(BOX, M.tab, 8, 6, 5, -2, -H / 2 - 3, 4, g);
}

// ------------------------------------------------------------------ camera
const REDUCED = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
const ease = (k) => (k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2);   // ease-in-out cubic
let anim = null;            // hand-rolled camera tween (no library)
let focused = null;         // zoomed module (card) or null
let overview = null;        // camera pose saved when the first zoom starts
let histPushed = false;
function overviewPose() {
  const aspect = Math.max(0.3, camera.aspect || 1);
  const fov = THREE.MathUtils.degToRad(camera.fov);
  const span = rackW + 30;
  const dist = Math.max((span / 2) / (Math.tan(fov / 2) * aspect), (420 / 2) / Math.tan(fov / 2)) * 1.05;
  return { t: new THREE.Vector3(rackW / 2, 0, 45), p: new THREE.Vector3(rackW / 2 + dist * 0.16, dist * 0.2, 45 + dist * 0.97),
    near: Math.max(5, dist / 200), far: dist * 10 };
}
function flyTo(pose, ms) {
  const dur = REDUCED ? 0 : ms;
  if (dur <= 0) {
    anim = null; controls.enabled = true;
    camera.position.copy(pose.p); controls.target.copy(pose.t);
    camera.near = pose.near; camera.far = pose.far; camera.updateProjectionMatrix(); controls.update(); dirty = true;
    return;
  }
  anim = { t0: performance.now(), dur, p0: camera.position.clone(), p1: pose.p.clone(), g0: controls.target.clone(), g1: pose.t.clone(),
    near: pose.near, far: pose.far };
  controls.enabled = false;
  camera.near = Math.min(camera.near, pose.near); camera.far = Math.max(camera.far, pose.far); camera.updateProjectionMatrix();
}
function stepAnim(now) {
  if (!anim) return false;
  const k = Math.min(1, (now - anim.t0) / anim.dur), e = ease(k);
  camera.position.lerpVectors(anim.p0, anim.p1, e);
  controls.target.lerpVectors(anim.g0, anim.g1, e);
  camera.lookAt(controls.target);
  if (k >= 1) {
    camera.near = anim.near; camera.far = anim.far; camera.updateProjectionMatrix();
    anim = null; controls.enabled = true; controls.update();
  }
  return true;
}
function resetView(instant) {
  if (focused) { zoomOut(); return; }
  flyTo(overviewPose(), instant ? 0 : 700);
}
function panelWide(c) { return !!c && c.kind === 'card' && c.type !== 'AI' && $('stage').getBoundingClientRect().width >= 1000; }
function focusPose(c) {   // front of the module (straight on, whole front incl. open door) at a comfortable distance, shifted so it sits beside the info panel
  const r = $('stage').getBoundingClientRect();
  const W = Math.max(1, r.width), Hh = Math.max(1, r.height), aspect = W / Hh;
  const th = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2);
  const narrow = W <= 640;
  const pw = narrow ? 0 : (panelWide(c) ? Math.min(660, W - 24) : Math.min(440, W - 24)) + 24;
  const freeW = narrow ? W : Math.max(120, W - pw);
  const dist = Math.max(150 / 0.80 / (2 * th), (c.w * 2.2 + 40) / (2 * th * aspect * (freeW / W)));
  const cx = c.x + c.w / 2, tz = c.d * 0.7;
  const t = new THREE.Vector3(cx + (pw / W) * dist * th * aspect, narrow ? -0.5 * dist * th : 0, tz);
  const dir = new THREE.Vector3(0, 0, 1);   // straight on: camera on the face normal, zero yaw / pitch, vertical edges vertical
  return { t, p: t.clone().addScaledVector(dir, dist), near: Math.max(5, dist / 200), far: Math.max(overviewPose().far, dist * 10) };
}
function zoomTo(c, instant) {
  if (!c) return;
  if (c !== focused) unpinTerm();
  if (!focused) overview = { p: camera.position.clone(), t: controls.target.clone(), near: camera.near, far: camera.far };
  focused = c;
  setSelected(c);
  flyTo(focusPose(c), instant ? 0 : 800);
  try {
    if (!histPushed) { history.pushState({ rack3d: 1 }, ''); histPushed = true; }
  } catch (e) { /* sandboxed frame: no history */ }
}
function zoomOut(fromPop) {
  unpinTerm();
  if (!focused) return;
  focused = null;
  setSelected(null);
  flyTo(overview || overviewPose(), 700);
  if (histPushed) {
    histPushed = false;
    if (!fromPop) { try { history.back(); } catch (e) { /* ignore */ } }
  }
}
$('reset').addEventListener('click', () => { resetView(); });
window.addEventListener('popstate', () => { if (focused) { histPushed = false; zoomOut(true); } });

// ------------------------------------------------------------------ render loop (on demand)
let dirty = true, hoverBox, selBox, hovered = null, selected = null;
function resize() {
  const r = $('stage').getBoundingClientRect();
  const w = Math.max(1, r.width), h = Math.max(1, r.height);
  renderer.setSize(w, h, false);
  camera.aspect = w / h; camera.updateProjectionMatrix();
  dirty = true;
}
new ResizeObserver(resize).observe($('stage'));
resize();
controls.addEventListener('change', () => { dirty = true; });

function frame() {
  requestAnimationFrame(frame);
  if (stepAnim(performance.now())) dirty = true;
  else if (controls.update()) dirty = true;
  for (const c of cards) {
    if (c.pivot) {
      const a = c.pivot.rotation.y, t = c.doorTarget;
      if (Math.abs(a - t) > 0.002) { c.pivot.rotation.y = REDUCED ? t : a + (t - a) * 0.18; dirty = true; }
    }
    if (c.keyPivot) {
      const r = c.keyPivot.rotation.z, t = c.keyTarget || 0;
      if (Math.abs(r - t) > 0.002) { c.keyPivot.rotation.z = REDUCED ? t : r + (t - r) * 0.12; dirty = true; }
    }
    if (c.veilMat) {
      const want = focused && c !== focused ? 0.62 : 0, o = c.veilMat.opacity;
      if (Math.abs(o - want) > 0.004) { c.veilMat.opacity = REDUCED ? want : o + (want - o) * 0.14; dirty = true; }
      else if (o !== want) { c.veilMat.opacity = want; dirty = true; }
      c.veil.visible = c.veilMat.opacity > 0.01;
    }
  }
  if (pendingPick) { pendingPick = false; doHover(); }
  if (dirty && built) { dirty = false; renderer.render(scene, camera); }
}
requestAnimationFrame(frame);

// ------------------------------------------------------------------ hover / click
const ray = new THREE.Raycaster();
const ndc = new THREE.Vector2();
let mouse = null, pendingPick = false, down = null;
function pick(ev) {
  const r = renderer.domElement.getBoundingClientRect();
  ndc.set(((ev.clientX - r.left) / r.width) * 2 - 1, -((ev.clientY - r.top) / r.height) * 2 + 1);
  ray.setFromCamera(ndc, camera);
  const h = ray.intersectObjects(hit, false)[0];
  return h ? h.object.userData.card : null;
}
function outline(box, c) {
  if (!c) { box.visible = false; return; }
  box.visible = true;
  box.scale.set(c.w + 1.2, H + 1.5, c.d + 1.5);
  box.position.set(c.x + c.w / 2, 0, (c.d + 1.5) / 2 - 0.5);
}
function terminalAt(ev) {   // only when the focused module's door is open (zoomed in)
  if (!ev || !focused || anim || !focused.pivot || focused.pivot.rotation.y > -1.2 || !termProxy) return null;
  const r = renderer.domElement.getBoundingClientRect();
  ndc.set(((ev.clientX - r.left) / r.width) * 2 - 1, -((ev.clientY - r.top) / r.height) * 2 + 1);
  ray.setFromCamera(ndc, camera);
  const hits = ray.intersectObject(termProxy, false);
  for (const h of hits) { const m = screwMeta[h.instanceId]; if (m && m.card === focused) return { id: h.instanceId, m }; }
  return null;
}
function setTerm(t) {
  const id = t ? t.id : -1;
  if (id === hlTerm) return;
  if (hlTerm >= 0) screwsMesh.setColorAt(hlTerm, WHITE);
  if (id >= 0) {
    screwsMesh.setColorAt(id, AMBER);
    termBox.visible = true; termBox.position.copy(screwXYZ[id]); termBox.scale.set(t.m.tw, 8.4, 6.2);
  } else termBox.visible = false;
  screwsMesh.instanceColor.needsUpdate = true; hlTerm = id; dirty = true;
}
function termTip(t) {
  const c = t.m.card, info = termInfo(c.catalog, t.m.row, t.m.col);
  const head = `<b>${esc(info.label)}</b><div class="muted">Terminal ${t.m.i} &middot; Slot ${pad(c.slot)} ${esc(c.catalog)}</div>` +
    (info.sig && info.pt != null ? `<div class="muted">${esc(info.role)}</div>` : '');
  if (info.pt == null) return head + `<div class="st">${esc(info.role || '')}</div>`;
  const names = labels[String(c.slot)] || {}, s = slotOf(c), good = comm() && s && s.ok;
  const lbl = `<div>${esc(names[String(info.pt)] || 'Not Documented')}</div>`;
  if (!comm()) return head + lbl + '<div class="st gray">COMM LOSS</div>';
  if (!good) return head + lbl + '<div class="st gray">No Data</div>';
  if (c.type === 'AI') {
    const ch = (s.channels || [])[info.pt] || {};
    return head + lbl + `<div class="st ${ch.over || ch.under ? 'bad' : 'ok'}">${esc(fmt(ch.v, ch.unit))}${ch.over ? ' (Over Range)' : ch.under ? ' (Under Range)' : ''}</div>`;
  }
  const bits = pointBits(c, s), b = bits ? bits[info.pt] : null;
  return head + lbl + `<div class="st ${b ? 'ok' : 'gray'}">${b == null ? '--' : b ? 'ON' : 'OFF'}</div>`;
}
function doHover() {
  if (!mouse || !built) return;
  let c = pick(mouse);
  if (focused && c !== focused) c = null;   // zoomed: tooltip / outline only for the focused module
  if (anim) c = null;
  if (c !== hovered) { hovered = c; outline(hoverBox, c && c !== selected ? c : null); dirty = true; }
  renderer.domElement.style.cursor = (c || pick(mouse)) ? 'pointer' : 'grab';
  const tip = $('tip');
  const tm = terminalAt(mouse);
  if (!tm && pinned) { setTerm(pinned.t); placeTip(pinned.html(), pinned.pt); return; }   // a pinned tap tooltip stays until dismissed
  setTerm(tm);
  if (!c && !tm) { tip.hidden = true; return; }
  placeTip(tm ? termTip(tm) : tipHtml(c), mouse);
}
function placeTip(html, pt) {
  const tip = $('tip');
  tip.innerHTML = html;
  tip.hidden = false;
  const r = $('stage').getBoundingClientRect();
  const tw = tip.offsetWidth, th = tip.offsetHeight;
  let x = pt.clientX - r.left + 16, y = pt.clientY - r.top + 16;
  if (x + tw > r.width - 8) x = pt.clientX - r.left - tw - 16;
  if (y + th > r.height - 8) y = pt.clientY - r.top - th - 16;
  tip.style.left = Math.max(8, x) + 'px'; tip.style.top = Math.max(8, y) + 'px';
}
// Tap / click a terminal pins its tooltip (touch has no hover): it moves on the next terminal tap and is dismissed by a tap
// on empty module space, Escape or zooming out. The terminal stays highlighted while pinned.
let pinned = null;
function pinTerm(t, ev) {
  pinned = { id: t.id, t, pt: { clientX: ev.clientX, clientY: ev.clientY }, html: () => termTip(t) };
  setTerm(t); placeTip(pinned.html(), pinned.pt);
}
function unpinTerm() {
  if (!pinned) return;
  pinned = null; setTerm(null); $('tip').hidden = true; dirty = true;
}
renderer.domElement.addEventListener('pointermove', (ev) => { if (ev.pointerType === 'touch') return; mouse = ev; pendingPick = true; });
renderer.domElement.addEventListener('pointerleave', (ev) => {
  if (ev.pointerType === 'touch') return;
  mouse = null; hovered = null; outline(hoverBox, null); if (!pinned) $('tip').hidden = true; dirty = true;
});
renderer.domElement.addEventListener('pointerdown', (ev) => { down = [ev.clientX, ev.clientY]; });
renderer.domElement.addEventListener('pointerup', (ev) => {
  if (!down || Math.hypot(ev.clientX - down[0], ev.clientY - down[1]) > (ev.pointerType === 'touch' ? 10 : 5)) { down = null; return; }
  down = null;
  const tm = terminalAt(ev);
  if (tm) { pinTerm(tm, ev); return; }
  const c = pick(ev);
  if (c && c === focused) { unpinTerm(); return; }      // empty space on the open module: close the pinned tip
  if (c) { zoomTo(c); return; }
  zoomOut();
});
function setSelected(c) {
  if (selected && selected.pivot) selected.doorTarget = 0;
  selected = c;
  outline(selBox, c);
  if (c && c === hovered) outline(hoverBox, null);
  if (c && c.pivot) c.doorTarget = -1.85;   // open the door: shows the terminal block
  showPanel(c);
  renderPanel();
  dirty = true;
}
let hideTimer = 0;
function showPanel(c) {
  const p = $('panel');
  clearTimeout(hideTimer);
  if (c) {
    p.classList.toggle('wide', panelWide(c));
    if (p.hidden) { p.hidden = false; void p.offsetWidth; }
    p.classList.add('show');
  } else {
    p.classList.remove('show');
    hideTimer = setTimeout(() => { if (!selected) p.hidden = true; }, REDUCED ? 0 : 260);
  }
}
$('p-close').addEventListener('click', () => zoomOut());
// test / support hook (read only): frame or select a module by member name, e.g. __rack3d.focus('Slot05')
window.__rack3d = {
  focus: (m) => zoomTo(cards.find((c) => c.member === m)),
  select: (m) => { const c = cards.find((k) => k.member === m); if (c) zoomTo(c); else zoomOut(); },
  out: () => zoomOut(),
  reset: () => resetView(true),
  busy: () => !!anim,
  focused: () => (focused ? focused.member : null),
  screenOf: (m) => { const c = cards.find((k) => k.member === m); if (!c) return null;
    const v = new THREE.Vector3(c.x + c.w / 2, 10, c.d).project(camera); const r = renderer.domElement.getBoundingClientRect();
    return [r.left + (v.x + 1) / 2 * r.width, r.top + (1 - v.y) / 2 * r.height]; },
  ready: () => built,
  view: (p, t) => { camera.position.set(p[0], p[1], p[2]); controls.target.set(t[0], t[1], t[2]); camera.lookAt(controls.target); controls.update(); dirty = true; },
  termScreen: (m, row, col) => { const q = screwXYZ.find((v) => v.meta && v.meta.card.member === m && v.meta.row === row && v.meta.col === col);
    if (!q) return null; const v = q.clone().project(camera); const r = renderer.domElement.getBoundingClientRect();
    return [r.left + (v.x + 1) / 2 * r.width, r.top + (1 - v.y) / 2 * r.height]; },
  ctrlPos: () => { const c = cards.find((k) => k.kind === 'controller'); return [c.x, c.w, c.d]; },
  pose: () => [camera.position.toArray(), controls.target.toArray()],
  pinned: () => (pinned ? pinned.t.m.i : null),
  keyAngle: () => { const c = cards.find((k) => k.kind === 'controller'); return c.keyPivot.rotation.z; },
};
window.addEventListener('keydown', (e) => { if (e.key === 'Escape') { if (pinned) unpinTerm(); else zoomOut(); } });

// ------------------------------------------------------------------ state -> LEDs / labels / panel
let state = null, labels = {}, chans = {};
const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch]));
const pad = (n) => String(n).padStart(2, '0');
function keyAngle(v) {
  const t = String(v == null ? '' : v).toLowerCase();
  if (/rem/.test(t)) return 0;
  if (/prog/.test(t)) return -KEY_ANG;
  if (/run/.test(t)) return KEY_ANG;
  return null;
}
function keyName(a) { return a == null ? null : a > 0.3 ? 'RUN' : a < -0.3 ? 'PROG' : 'REM'; }
function slotOf(c) { return state && state.slots ? state.slots.find((s) => s.slot === c.slot) : null; }
function comm() { return !!(state && state.ok && state.comm); }
function cardStatus(c) {
  if (c.kind === 'endcap') return ['Passive', 'gray'];
  if (!comm()) return ['Comm Loss', 'gray'];
  if (c.kind === 'power') return ['Implied On', 'ok'];
  if (c.kind === 'controller') {
    const k = state.controller || {};
    if (k.majorFault) return ['Major Fault', 'bad'];
    if (k.ioFault) return ['I/O Fault', 'bad'];
    return [k.mode || 'Unknown', k.run ? 'ok' : 'gray'];
  }
  const s = slotOf(c);
  if (!s || s.ok == null) return ['No Data', 'gray'];
  return s.ok ? ['OK', 'ok'] : ['Fault' + (s.fault != null ? ' (' + s.fault + ')' : ''), 'bad'];
}
function pointBits(c, s) {
  if (!s) return null;
  if (c.type === 'DO') return s.readBack || s.data;
  return s.data;
}
function fmt(v, unit) {
  if (v == null || isNaN(v)) return '--';
  return (Math.abs(v) >= 100 ? v.toFixed(1) : v.toFixed(2)) + (unit ? ' ' + unit : '');
}
function tipHtml(c) {
  const [st, cls] = cardStatus(c);
  if (c.kind === 'endcap') return '<b>Right End Cap</b><div class="muted">1769-ECR &middot; Bus Terminator</div>';
  if (c.kind === 'power') return '<b>Bank Power Supply</b><div class="muted">1769 Expansion Power Supply &middot; Catalog Not In L5X</div>' +
    `<div class="st ${comm() ? 'ok' : 'gray'}">${comm() ? 'Implied On (Controller Communicating)' : 'Comm Loss'}</div>`;
  if (c.kind === 'controller') {
    return `<b>Controller &middot; ${esc(c.name)}</b><div class="muted">${esc(c.catalog)} &middot; CompactLogix 5370 L3</div>` +
      `<div class="st ${cls}">${esc(st)}</div>`;
  }
  return `<b>Slot ${pad(c.slot)} &middot; ${esc(c.name)}</b><div class="muted">${esc(c.catalog)} &middot; ${esc(c.description || '')}</div>` +
    `<div class="st ${cls}">${esc(st)}</div>`;
}
function setLed(i, key) {
  if (i < 0 || ledColors[i] === key) return false;
  ledColors[i] = key; ledMesh.setColorAt(i, LED[key]); return true;
}
function applyState() {
  if (!built) return;
  const on = comm();
  let changed = false;
  for (const c of cards) {
    if (c.kind === 'card') {
      const s = slotOf(c);
      const okKey = !on || !s || s.ok == null ? 'off' : s.ok ? 'on' : 'fault';
      changed = setLed(c.okIdx, okKey) || changed;
      const bits = on && s && s.ok ? pointBits(c, s) : null;
      c.ledIdx.forEach((li, p) => { changed = setLed(li, bits && bits[p] ? 'on' : 'off') || changed; });
      if (c.type === 'AI') {
        const vals = (s && s.channels || []).map((ch) => (on && s.ok && ch && ch.v != null ? fmt(ch.v, ch.unit) : ''));
        const key = vals.join('|');
        if (key !== c.doorKey) { c.doorKey = key; redraw(c.doorTex, (g, a, b) => drawDoor(g, a, b, c, vals)); changed = true; }
      }
    } else if (c.kind === 'power') {
      changed = setLed(c.pwrIdx, on ? 'on' : 'off') || changed;          // no tag: implied while the controller talks
    } else if (c.kind === 'controller') {
      const k = (state && state.controller) || {};
      const I = c.ctrlIdx;
      changed = setLed(I.RUN, on && k.run ? 'on' : 'off') || changed;
      changed = setLed(I.FORCE, 'off') || changed;                                  // no source tag (R6)
      changed = setLed(I.IO, !on ? 'off' : k.ioFault ? 'fault' : 'on') || changed;
      changed = setLed(I.OK, !on ? 'off' : k.majorFault ? 'fault' : 'on') || changed;
      changed = setLed(I.NS, on ? 'on' : 'off') || changed;
      changed = setLed(I.LINK1, on ? 'on' : 'off') || changed;
      changed = setLed(I.LINK2, 'off') || changed;                                  // no source tag
      changed = setLed(I.SD, 'off') || changed;                                     // no source tag
      const ang = on ? keyAngle(k.keySwitch) : null;
      if (ang != null) c.keyLast = ang;
      c.keyLive = ang != null;
      c.keyTarget = c.keyLast != null ? c.keyLast : 0;                              // not live: last known position, gray
      const mat = c.keyLive ? KEY_MAT_LIVE : KEY_MAT_OFF;
      if (c.keyBlade.material !== mat) { c.keyBlade.material = mat; changed = true; }
    }
  }
  if (changed) { ledMesh.instanceColor.needsUpdate = true; dirty = true; }
  // header chip, banner, footer
  const k = (state && state.controller) || {};
  const chip = $('chip');
  if (!state || !state.ok) { chip.textContent = 'No Data'; chip.className = 'chip chip-off'; }
  else if (!state.comm) { chip.textContent = 'Comm Loss'; chip.className = 'chip chip-fault'; }
  else if (k.majorFault) { chip.textContent = 'Major Fault'; chip.className = 'chip chip-fault'; }
  else { chip.textContent = k.mode || 'Unknown'; chip.className = 'chip ' + (k.run ? 'chip-run' : 'chip-off'); }
  const banner = $('banner');
  if (state && state.ok && !state.comm) { banner.textContent = 'Communication Lost'; banner.hidden = false; }
  else if (state && !state.ok) { banner.textContent = state.reason || 'No Data'; banner.hidden = false; }
  else banner.hidden = true;
  $('t-plc').textContent = (state && state.plc) || PLC;
  $('t-ctrl').textContent = k.catalog || '1769-L36ERM';
  if (hovered) doHover();
  renderPanel();
}
function renderPanel() {
  const c = selected;
  if (!c) return;
  const [st, cls] = cardStatus(c);
  const on = comm();
  $('p-status').innerHTML = `<span class="${cls}">${esc(st)}</span>`;
  if (c.kind === 'power') {
    $('p-title').textContent = 'Bank Power Supply';
    $('p-sub').textContent = '1769 Expansion Power Supply (Not In The L5X)';
    const rows = [['Catalog', 'Not In L5X (Confirm On The Panel: 1769-PA2 / PB2 / PA4 / PB4)'], ['Status Tag', 'None (No PLC Source)'],
      ['Power', comm() ? 'Implied On' : '--'], ['Rule', 'Controller Within 4 Slots (1769-UM021)']];
    $('p-body').innerHTML = rows.map(([a, b]) => `<div class="kv"><span>${esc(a)}</span><span>${esc(b)}</span></div>`).join('');
    return;
  }
  if (c.kind === 'controller') {
    const k = (state && state.controller) || {};
    $('p-title').textContent = 'Controller · ' + c.name;
    $('p-sub').textContent = (k.catalog || c.catalog) + ' · CompactLogix 5370 L3';
    const yn = (b) => (!on || b == null ? '--' : b ? 'Yes' : 'No');
    const kn = keyName(c.keyLast);
    const rows = [['Mode', on ? k.mode : '--'], ['Mode Switch', kn ? kn + (c.keyLive ? '' : ' (Last Known, Not Live)') : '--'], ['Project Name', k.name || c.projName || '--'], ['Driver', on ? 'Connected' : 'Disconnected'],
      ['Major Fault', yn(k.majorFault)], ['Minor Fault', yn(k.minorFault)], ['I/O Fault', yn(k.ioFault)],
      ['Last Major Fault Code', k.faultCode == null ? '--' : k.faultCode], ['Firmware', k.firmware || '--'],
      ['Modules Faulted', k.modulesFaulted == null || !on ? '--' : k.modulesFaulted + ' / ' + (k.moduleCount || cards.filter((x) => x.kind === 'card').length)],
      ['FORCE / SD / LINK 2 Lamps', 'No Source Tag']];
    $('p-body').innerHTML = rows.map(([a, b]) => `<div class="kv"><span>${esc(a)}</span><span>${esc(b == null ? '--' : b)}</span></div>`).join('');
    return;
  }
  if (c.kind === 'endcap') {
    $('p-title').textContent = 'Right End Cap';
    $('p-sub').textContent = '1769-ECR \u00b7 Bus Terminator';
    $('p-body').innerHTML = [['Catalog', '1769-ECR'], ['Function', 'Terminates The Compact I/O Bus'], ['Status Tag', 'None (Passive)']]
      .map(([a, b]) => `<div class="kv"><span>${esc(a)}</span><span>${esc(b)}</span></div>`).join('');
    return;
  }
  const s = slotOf(c);
  $('p-title').textContent = 'Slot ' + pad(c.slot) + ' · ' + c.name;
  $('p-sub').textContent = c.catalog + ' · ' + (c.description || '');
  const names = labels[String(c.slot)] || {};
  const good = on && s && s.ok;
  let html = '';
  if (c.type === 'AI') {
    const cfg = chans[String(c.slot)] || {};
    for (let i = 0; i < 8; i++) {
      const ch = (s && s.channels || [])[i] || {};
      const flag = !good ? 'gray' : ch.over || ch.under ? 'bad' : 'ok';
      const dot = !good ? 'off' : ch.over || ch.under ? 'fault' : 'on';
      const rng = good ? (ch.over ? 'Over Range' : ch.under ? 'Under Range' : '') : '';
      const sig = (cfg[String(i)] || {}).signal || '';
      html += `<div class="row" title="${esc(names[String(i)] || '')}"><span class="n">Ch${i}</span><i class="dot ${dot}"></i>` +
        `<span class="lbl">${esc(names[String(i)] || 'Not Documented')}<br><span class="muted">${esc([sig, rng].filter(Boolean).join(' · '))}</span></span>` +
        `<span class="v ${flag}">${good ? esc(fmt(ch.v, ch.unit)) : '--'}</span></div>`;
    }
  } else {
    const bits = good ? pointBits(c, s) : null;
    for (let p = 0; p < 16; p++) {
      const b = bits ? bits[p] : null;
      let v = b == null ? '--' : b ? 'ON' : 'OFF';
      if (c.type === 'DO' && good && s.data && s.readBack && s.data[p] !== s.readBack[p]) v += ' (Cmd ' + (s.data[p] ? 'ON' : 'OFF') + ')';
      html += `<div class="row" title="${esc(names[String(p)] || '')}"><span class="n">${p}</span><i class="dot ${b == null ? 'off' : b ? 'on' : 'off'}"></i>` +
        `<span class="lbl">${esc(names[String(p)] || 'Not Documented')}</span><span class="v ${b ? 'ok' : 'gray'}">${esc(v)}</span></div>`;
    }
  }
  $('p-body').innerHTML = html;
}

// ------------------------------------------------------------------ polling
let first = true;
async function poll() {
  let next = POLL_MS;
  try {
    const url = DEMO ? './lib/demo-state.json' : './state?plc=' + encodeURIComponent(PLC) + (first ? '&labels=1' : '');
    const r = await fetch(url, { cache: 'no-store', credentials: 'same-origin', headers: { Accept: 'application/json' } });
    if (r.status === 401 || r.status === 403) {
      state = { ok: false, reason: 'Login Required' }; next = 10000;
    } else if (!r.ok) {
      state = { ok: false, reason: 'No Data From Gateway (' + r.status + ')' };
    } else {
      const st = await r.json();
      if (st.labels) { labels = st.labels; chans = st.channelsCfg || {}; first = false; }
      state = st;
      if (!built && st.ok !== false && st.slots) build(st);
      $('updated').textContent = DEMO ? 'Demo Data (Static)' : 'Updated ' + new Date().toLocaleTimeString();
    }
  } catch (e) {
    state = { ok: false, reason: 'No Data From Gateway' };
  }
  applyState();
  if (DEMO) { $('demo').hidden = false; return; }   // static sample: no polling
  setTimeout(poll, next);
}
poll();
