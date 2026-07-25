# Ignition Perspective theme architecture (8.3 file-based)

Canonical guide for BH (`gateways/standard`) theme work on Ignition **8.3.x**. Themes are **gateway config resources**, not project Designer Style Classes. The project Advanced Stylesheet **consumes** theme CSS variables; it must not redefine the theme’s `--neutral-*` scale.

**Sources researched**

| Source | Path |
|--------|------|
| Scout stock themes | `C:\Program Files\Inductive Automation\Perspective-8-3-Scout\data\config\resources\core\com.inductiveautomation.perspective\themes\` |
| ScoutMotors project theme copy | `…\Perspective-8-3-Scout\data\projects\ScoutMotors\themes\` (optional override pattern; BH uses gateway themes) |
| Lightspeed Frontend | `C:\Users\dylan.jones\Documents\Cursor\Ignition QA\assets\Lightspeed-Frontend\config\resources\core\com.inductiveautomation.perspective\themes\` |
| BH Standard (active) | `gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/` |
| BH Advanced Stylesheet | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css` |
| Theme switcher | `…/views/00_Pages/00_Docked/_Assets/ChangeTheme/view.json` |
| Session default | `…/session-props/props.json` → `"theme": "light"` |

---

## 1. How Perspective loads themes

1. Client reads **`session.props.theme`** (string = folder name under gateway `themes/`).
2. Gateway serves that theme’s **`config.json` → `entrypoint`** (normally `index.css`).
3. Theme CSS (variables + Ignition component chrome) loads **first**.
4. Project **Advanced Stylesheet** loads **after** the theme.
5. There is **no** `[data-theme]` attribute. Switching themes swaps the entire theme stylesheet; CSS that uses `var(--neutral-*)` updates automatically.

**Implication:** Any `:root { --neutral-10: … }` in `stylesheet.css` **stomps every theme** to whatever hex you wrote (historically this locked BH to light-cool). Do not redefine `--neutral-*` in the Advanced Stylesheet.

After editing theme files under `gateways/*/data/config/`, rely on the **ignition-scan** config scan (or POST `/data/api/v1/scan/config`) so the gateway reloads from disk.

---

## 2. Correct file layout

### Gateway path (BH Standard)

```text
gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/
├── light/                 # FULL base (cool light) — fonts, globals, app/, common/, designer/, palette/
│   ├── config.json        # { "entrypoint": "index.css", "isPrivate": false }
│   ├── resource.json      # scope G, files[] inventory
│   ├── index.css          # @import chain
│   ├── variables.css      # --neutral-*, --callToAction*, containers, borders, …
│   ├── fonts.css
│   ├── globals.css
│   ├── app/
│   ├── common/
│   ├── designer/
│   └── palette/
├── dark/                  # FULL dark base (cool) — own variables + globals + palette; reuses light chrome
│   ├── index.css
│   ├── variables.css      # inverted --neutral-* (10=darkest surface … 100=lightest text)
│   ├── globals.css
│   └── palette/
├── light-warm/            # THIN variant — only variables + index imports from ../light/
├── dark-warm/             # THIN — variables + imports light chrome + ../dark/globals + ../dark/palette
├── light-cool/            # THIN alias of cool light (same neutrals as light; optional duplicate)
└── dark-cool/             # THIN alias of cool dark (same neutrals as dark; optional duplicate)
```

### Canonical `index.css` patterns (Scout / Lightspeed / BH)

**Full `light`**

```css
@import "./variables.css";
@import "./fonts.css";
@import "./globals.css";
@import "./app/index.css";
@import "./common/index.css";
@import "./designer/index.css";
@import "./palette/index.css";
```

**Thin `light-warm` / `light-cool`** (Lightspeed Frontend pattern)

```css
@import "./variables.css";
@import "../light/fonts.css";
@import "../light/globals.css";
@import "../light/app/index.css";
@import "../light/common/index.css";
@import "../light/designer/index.css";
@import "../light/palette/index.css";
```

**Thin `dark-warm` / `dark-cool`**

```css
@import "./variables.css";
@import "../light/fonts.css";
@import "../dark/globals.css";
@import "../light/app/index.css";
@import "../light/common/index.css";
@import "../light/designer/index.css";
@import "../light/palette/index.css";
@import "../dark/palette/index.css";
```

**Thin `variables.css`** always starts from the matching base, then overrides neutrals (and optionally accents):

```css
@import "../light/variables.css";   /* or ../dark/variables.css */

:root {
    --neutral-10: #…;
    /* … through --neutral-100 */
    /* optional: --callToAction, --accent, … */
}
```

### Theme name matrix (BH / ChangeTheme)

| `session.props.theme` | Meaning | Neutrals source |
|-----------------------|---------|-----------------|
| `light` | Light + cool (default) | `light/variables.css` (cool scale baked into BH `light`) |
| `dark` | Dark + cool | `dark/variables.css` (cool inverted) |
| `light-warm` | Light + warm | `light-warm/variables.css` |
| `dark-warm` | Dark + warm | `dark-warm/variables.css` |
| `light-cool` | Cool light **alias** (optional) | Same cool light neutrals as `light` |
| `dark-cool` | Cool dark **alias** (optional) | Same cool dark neutrals as `dark` |

**BH UX convention:** ChangeTheme treats **Cool** as writing `light` / `dark`, and **Warm** as `light-warm` / `dark-warm`. Keep `light-cool` / `dark-cool` on disk as aliases for interoperability with stock Ignition / Lightspeed exports; prefer `light` / `dark` in session scripts so Cool stays the short names.

### Required resource files (every theme folder)

| File | Role |
|------|------|
| `config.json` | `"entrypoint": "index.css"`, `"isPrivate": false` |
| `resource.json` | Gateway resource metadata (`scope: "G"`, `files` list, signatures) |
| `index.css` | Import graph |
| `variables.css` | `:root` token definitions |

Thin themes list only those four files in `resource.json`. Full `light` / `dark` list the entire chrome tree.

### Edge / incomplete gateways

Thin themes **`@import ../light/…` and `../dark/…`**. If a gateway only has `*-warm` / `*-cool` folders (as Edge currently does), cool/warm themes **break** without stock `light` + `dark` bases. Standard must keep full `light` and `dark` trees. Sync Edge from Standard when themes matter there.

---

## 3. What belongs in theme files vs Advanced Stylesheet

### Theme files (`themes/<name>/variables.css` + chrome)

| Own here | Examples |
|----------|----------|
| Neutral scale | `--neutral-10` … `--neutral-100` |
| Ignition semantic surfaces | `--containerRoot`, `--container`, `--containerNested`, `--input`, `--label`, `--border`, `--icon*` |
| Accents for built-in components | `--callToAction`, `--callToAction--hover`, `--error`, `--info`, … |
| Typography / radius / shadows used by IA components | `--font-NotoSans`, `--borderRadius`, `--boxShadow*` |
| Component palette CSS | `common/button.css`, `palette/table.css`, … (usually inherited from `light/`) |

Warm/cool variants should **only** override neutrals (+ optional `--callToAction` / `--accent`). Do not duplicate the full chrome tree.

### Advanced Stylesheet (`stylesheet.css`)

| Own here | Examples |
|----------|----------|
| Semantic **aliases** that `var()` into theme neutrals | `--surface-page`, `--surface-header`, `--text`, `--border`, `--nav-*` |
| Utility / layout classes | `.bg-page`, `.bg-header`, `.bg-component`, `.container-card`, `.font-label`, `.app-header`, `.nav-*` |
| Motion / behavior | `.fan-spin`, `.alarm-flash` |
| **Alarm tokens only** (theme-invariant hex) | `--alarm-critical`, `--alarm-high`, … and alarm table row classes |
| Status / device chrome that should **follow themes** | Prefer `--sts-*-bg/fg` and `--deviceFill-*` defined as `var(--neutral-*)` (or other theme tokens), not fixed cool-gray hex |
| Attention status that is not alarm-table chrome | Fault / defrost / manual may keep saturated accents for ISA-101 attention — but they are **not** frozen the way `--alarm-*` is; do not block theming of normal device chrome for their sake |

### Hard rules

1. **Never** redefine `--neutral-*` in `stylesheet.css`.
2. **Never** put page/component fill colors as hardcoded hex in `view.json` when a class + semantic token exists.
3. Theme CSS owns IA built-in look; Advanced Stylesheet owns BH product look **on top of** those variables.
4. Designer Style Classes remain forbidden for BH (CSS-only rule).

---

## 4. Theming components and page backgrounds

### Semantic token layer (stylesheet)

Build aliases once; they recompute when the theme’s `--neutral-*` change:

```css
:root {
  --surface-page: var(--neutral-10);
  --surface-raised: var(--neutral-20);
  --surface-component: var(--neutral-20);
  --surface-header: var(--neutral-30);
  --surface-container: var(--neutral-30);
  --text: var(--neutral-100);
  --text-secondary: var(--neutral-80);
  --border: var(--neutral-30);
  --icon: var(--neutral-90);
  /* … */
}
```

### Page / root backgrounds

- Apply **`bg-page`** (→ `.psc-bg-page` → `var(--surface-page)`) on **every page root** and primary overview root.
- Docked header: **`app-header`** (uses `--surface-header`) or **`bg-header`**.
- Cards / faceplate shells: **`bg-component`**, **`bg-container`**, **`container-card`**.
- Prefer `props.style.classes`; avoid `props.style.backgroundColor: "#D8D8D8"` / `"#ECEFF1"` (common Overview anti-pattern today).

### Device components + SVG chrome

- Housing, rings, blades, strokes, labels: drive fills/strokes from **theme neutrals** or classes that use `--surface-*` / `--text` / `--border` / `--icon`.
- Running / stopped / faulted **device fills**: map to neutrals, e.g. `--deviceFill-running: var(--neutral-10)`, `--deviceFill-stopped: var(--neutral-60)`, `--deviceFill-faulted: var(--neutral-100)` (tune for contrast per light/dark — define in stylesheet as `var(--neutral-*)`, not fixed `#fafafa`).
- Do **not** leave Figma export hex (`#D8D8D8`, `#1A2329`, …) as the only chrome colors on live views.

### Faceplates (`01_Popups/00_Faceplates/**`)

- Root / panels: `bg-component` / `bg-container` / `container-card` — **not** hardcoded `#1A2329` / `#263238` (present on several device faceplates today).
- Text / icons: `font-label`, `font-value`, `--neutral-*` or `--text` / `--icon`.
- Alarm indicators inside faceplates still use **`--alarm-*`** / alarm classes (invariant).

### Adhoc Trend faceplate + `/trending` UI

- Faceplates: `AdhocTrend`, `AdhocTrendConfig` already use `bg-container` / `container-card` — keep that pattern; strip any leftover hex backgrounds.
- Page `98_Configuration/AdhocTrend/Trend` and docked trending assets: root `bg-page` or `bg-container`; chart chrome via theme neutrals / `--surface-*`.
- Pen / series colors may stay a fixed qualitative palette (session `custom.AdhocTrend.colors`) — that is data-viz, not chrome. Chart **background, grid, axes, toolbars** must theme.

### Ticket Logger

- Popup / config views: `bg-component`, `container-card`, `font-value` (already used).
- Context-menu Ticket Logger rows: keep `bg-component font-value`; icon color `--neutral-80` (themes correctly).
- Do not introduce dark-only panel hex.

### Nav + headers

- Nav dock / tree: classes under `.psc-nav-*` already bind to `--surface-nav`, `--text-nav`, `--icon-nav`, `--border-nav`.
- Header: `.psc-app-header` → `--surface-header` + `--border`.
- Theme gear (`ChangeTheme`): already binds selection chrome to `--neutral-*` via expressions — keep using theme names in the matrix above.

### Status chips (`Refridgeration_STS` / `sts-*`)

- **Normal** states (COOLING / IDLE / OFF / UNKNOWN): prefer grayscale via **`var(--neutral-*)`** so chips track light/dark/warm/cool.
- **Attention** states (FAULT / DEFROST / MANUAL): may use saturated accents for ISA-101; optional left-border accents. These are separate from `--alarm-*` table tokens.
- Always keep a **text status code** on the control — never encode state with color alone.

---

## 5. Alarm tokens stay theme-invariant

**Only `--alarm-*` (and alarm-table / alarm-icon consumers) are required to stay fixed across themes.**

Define once on `:root` in Advanced Stylesheet:

```css
--alarm-critical / -ack
--alarm-high / -ack
--alarm-medium / -ack
--alarm-low / -ack
--alarm-row-fg-light
--alarm-row-fg-dark
```

Use for Alarm Status Table row classes, DeviceAlarmIndicator priority colors, and any true alarm chrome.

**Do not** freeze `--sts-*` or `--deviceFill-*` as permanently theme-independent unless a specific token is literally an alarm color. Prefer mapping normal status / device fills to theme neutrals so surfaces and device chrome follow the active theme.

Scout’s `overrides-light` theme shows an older pattern of pinning `--deviceFill-*` in a theme override; for BH, put themeable device fills in the stylesheet as `var(--neutral-*)` instead of a separate overrides theme.

---

## 6. Lightspeed Frontend vs BH

Lightspeed Frontend assets ship **only** the four thin folders (`light-cool`, `light-warm`, `dark-cool`, `dark-warm`) that import sibling `../light` and `../dark`. Stock Ignition on the gateway supplies the full bases.

BH Standard already mirrors the robust layout: full `light` + `dark` (with cool neutrals baked in) plus thin warm/cool aliases and warm accent overrides on warm themes. That is the correct 8.3 approach for ChangeTheme’s `light` / `dark` / `light-warm` / `dark-warm` names.

---

## 7. Implementation checklist (BH agents)

### Gateway themes

- [ ] Ensure **`light`** and **`dark`** full trees exist under Standard `…/themes/` (fonts, globals, app, common, designer, palette).
- [ ] Ensure thin **`light-warm`**, **`dark-warm`**, and optional **`light-cool`**, **`dark-cool`** with correct `@import` graphs and `variables.css` neutral overrides.
- [ ] Warm themes may set warm `--callToAction` / `--accent`; cool themes keep cool CTA.
- [ ] `config.json` + `resource.json` present for every theme; entrypoint `index.css`.
- [ ] After edits: **config scan** (ignition-scan hook).
- [ ] If Edge needs themes: copy full `light`/`dark` bases too — thin-only is broken.

### Advanced Stylesheet

- [ ] **Do not** redefine `--neutral-*`.
- [ ] Keep semantic aliases (`--surface-*`, `--text-*`, `--border*`, `--nav-*`) as `var(--neutral-*)`.
- [ ] Keep **`--alarm-*` only** as fixed hex on `:root`.
- [ ] Remap `--sts-*` normal fills and `--deviceFill-*` to `var(--neutral-*)` (or theme accents where appropriate).
- [ ] Utility classes `bg-page`, `bg-header`, `bg-component`, `bg-container`, `app-header`, `nav-*` remain the styling API for views.

### Session / switcher

- [ ] Default `session.props.theme` = `light` (or product choice).
- [ ] ChangeTheme only writes: `light`, `dark`, `light-warm`, `dark-warm` (cool = short names).
- [ ] No scripts that assume `[data-theme]`.

### Views — page backgrounds (all)

- [ ] Every `00_Pages/**` overview / summary / trending page root uses **`bg-page`** (or equivalent surface class).
- [ ] Remove hardcoded page fills (`#D8D8D8`, `#ECEFF1`, etc.).
- [ ] Devices Overview pattern (`classes: "bg-page"`) is the reference.

### Views — nav + headers

- [ ] Header dock keeps `app-header` (or `bg-header`); no fixed hex bar.
- [ ] Navigation / TempNav keep `nav-*` classes; icons/text via theme tokens.

### Views — faceplates (`01_Popups/00_Faceplates/**`)

- [ ] Replace `#1A2329` / `#263238` (and similar) with `bg-component` / `bg-container` / `container-card`.
- [ ] AdhocTrend + AdhocTrendConfig stay on card/container classes; verify no hex panels.
- [ ] Alert / Menu faceplates use theme surfaces; alarm severity still `--alarm-*`.

### Views — Adhoc Trend + `/trending`

- [ ] Trend page root + toolbars themed; chart plot background follows surface tokens.
- [ ] Docked trending assets themed; config faceplate themed.
- [ ] Series pen colors may remain fixed qualitative palette.

### Views — Ticket Logger

- [ ] Ticket Logger view + context-menu chrome use `bg-component` / cards / `--neutral-*` icons.
- [ ] No dark-only hardcoded shells.

### Views — device components

- [ ] `02_Components/01_Devices/**` chrome uses theme neutrals / classes; SVG fills follow `--deviceFill-*` or neutral vars.
- [ ] Status chips use `Refridgeration_STS sts-<TOKEN>` with themeable normal colors.
- [ ] Alarm indicators continue to use invariant `--alarm-*`.

### Verification

- [ ] Flip ChangeTheme through **light → dark → light-warm → dark-warm**; confirm page, header, nav, faceplates, ticket logger, trending, and device chrome all shift.
- [ ] Confirm alarm table / alarm icons **do not** change hue across themes.
- [ ] Confirm no stylesheet `:root` block reintroduces `--neutral-*` hex.
- [ ] Scan projects + config after disk edits; hard-refresh Perspective client.

---

## 8. Quick reference — key rules

1. Theme folder name = `session.props.theme`.
2. Theme CSS loads **before** Advanced Stylesheet — never stomp `--neutral-*` in the stylesheet.
3. Thin warm/cool themes = `variables.css` override + `@import` from `light`/`dark` chrome.
4. BH session names: `light` / `dark` / `light-warm` / `dark-warm` (+ cool aliases on disk).
5. Style views with **classes** (`bg-page`, `bg-header`, `bg-component`, `app-header`, `nav-*`) backed by semantic tokens.
6. **Only `--alarm-*` are theme-invariant**; theme surfaces, text, borders, icons, device chrome, and normal status fills.
7. Faceplates, Adhoc Trend / trending, Ticket Logger, devices, nav, headers, and **all page backgrounds** are in scope for theming.
8. No Designer Style Classes; edit on disk + ignition-scan.
