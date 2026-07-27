# BH Perspective themes

Practical guide for operators, designers, and implementers working on Boar’s Head (BH) HMI theming on Ignition **8.3.x**.

> **Status (`feature/themes`):** Four operator themes (`light-cool`, `dark-cool`, `light-warm`, `dark-warm`) are live on Standard. ChangeTheme swaps gateway CSS; Advanced Stylesheet semantic aliases ride those neutrals. Prefer this doc + the linked deep dives over any leftover hardcoded hex in views or stylesheet comments that still say status/device fills are “theme-independent.”
>
> **Verification screenshots:** Playwright captures from the BH client live under [`verify-screenshots/themes/`](../verify-screenshots/themes/) (overview + header/nav per theme; optional faceplate / Adhoc Trend / alarms).

---

## Quick start

| What | Where |
|------|--------|
| Switch theme / animations | Top-right **settings gear** → **ChangeTheme** (Light/Dark × Cool/Warm + Animations On/Off) |
| Theme session value | `session.props.theme` (default: `light` / prefer `light-cool`) |
| Animations session value | `session.props.animations` (boolean, default: `true`) |
| Gateway theme CSS | `gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/<name>/` |
| Product CSS (classes + semantic aliases) | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css` |
| Figma source | [Dev Jam](https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w/Dev) (`Q8EmmXokQsiX91aPMtLm2w`, page `Dev Jam` / `25:2`) |

After editing theme files under `gateways/*/data/config/`, rely on the **ignition-scan** config scan (or POST `/data/api/v1/scan/config`). Hard-refresh the Perspective client after a theme change.

Theme selection is **only** via the gear → ChangeTheme popup (not nested inside the login / switch-user popup).

---

## 1. Four modes

BH exposes **four** operator-facing themes. ChangeTheme is a 2×2 picker: **Light / Dark** and **Cool / Warm**.

| UI selection | `session.props.theme` | Meaning |
|--------------|----------------------|---------|
| Light + Cool | `light-cool` | Light surfaces, cool neutrals (**default**) |
| Dark + Cool | `dark-cool` | Dark surfaces, cool neutrals |
| Light + Warm | `light-warm` | Light surfaces, warm neutrals |
| Dark + Warm | `dark-warm` | Dark surfaces, warm neutrals |

**Cool = `light-cool` / `dark-cool`.** Stock Ignition `light` / `dark` bundles do **not** apply BH disk `variables.css` overrides (including `--ct-water`), so ChangeTheme writes the thin cool themes. Legacy `light` / `dark` session values are still treated as cool in UI bindings and upgraded on the next Cool/Light/Dark click. Advanced Stylesheet also defines `--ct-water` as a safety net.

Figma’s Theme property maps the same four modes (`Light` / `Dark` / `Light Warm` / `Dark Warm`) — see [theme-figma-tokens.md](./theme-figma-tokens.md).

---

## 1b. Animations master toggle

ChangeTheme also exposes **Animations** On / Off (default **On**).

| UI | Session | Effect |
|----|---------|--------|
| On | `session.props.animations = true` | Device / alarm CSS motion runs normally |
| Off | `session.props.animations = false` | Known motion classes stop (`animation: none`) |

**Wiring:**

1. Default is set in session props: `"animations": true` next to `"theme"`.
2. ChangeTheme On/Off writes `session.props.animations` (and best-effort `html.animations-off` via JS API when available).
3. Docked **Header** binds `app-header` vs `app-header animations-off` from that session prop.
4. Advanced Stylesheet gates known classes under `body:has(.psc-animations-off)` and `html.animations-off`:
   - `fan-spin`, `ct-fan-side-spin`, `ct-spray-run`, `alarm-flash`, `container-fade-in` (plus `.psc-*` forms)

Transitions used by theme chrome are **not** blanket-disabled — only the listed animation classes — so theme toggles stay smooth.

---

## 2. How `session.props.theme` loads CSS

Perspective does **not** set a `[data-theme]` attribute. Switching themes swaps the gateway stylesheet:

1. Client reads **`session.props.theme`** (string = folder name under gateway `themes/`).
2. Gateway serves that theme’s `config.json` → entrypoint (usually `index.css`).
3. Theme CSS loads **first** (`--neutral-*`, IA component chrome, accents).
4. Project **Advanced Stylesheet** loads **after** and builds BH semantic tokens on top of those variables.
5. Any CSS using `var(--neutral-*)` or semantic aliases (`--surface-page`, `--text`, …) updates automatically.

**Critical rule:** Never redefine `--neutral-10` … `--neutral-100` in `stylesheet.css`. That stomps every theme to whatever hex you wrote.

Default is set in session props:

`gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json` → `"theme": "light"`.

### Folder layout (Standard)

```text
gateways/standard/data/config/.../themes/
├── light/          # FULL base (cool light) — fonts, globals, app/, common/, palette/
├── dark/           # FULL base (cool dark)
├── light-warm/     # THIN — own variables.css + @import chrome from ../light/
├── dark-warm/      # THIN — own variables + light fonts + dark globals/palette
├── light-cool/     # THIN alias (optional; same cool neutrals as light)
└── dark-cool/      # THIN alias (optional; same cool neutrals as dark)
```

Thin themes only override neutrals (and optionally `--callToAction` / accents). They must be able to `@import` sibling `light/` and `dark/` — **do not ship warm/cool-only folders without full bases** (Edge currently has thin-only folders; sync from Standard if Edge theming matters).

Deep file patterns, `resource.json` rules, and import graphs: [ignition-theme-architecture.md](./ignition-theme-architecture.md).

---

## 3. Theme files vs Advanced Stylesheet

| Layer | Owns | Examples |
|-------|------|----------|
| **Gateway theme** `themes/<name>/` | Neutral scale + Ignition built-in chrome | `--neutral-*`, `--container*`, `--input`, `--callToAction`, fonts, `common/` / `palette/` component CSS |
| **Advanced Stylesheet** `stylesheet.css` | BH product look on top of theme vars | Semantic aliases (`--surface-*`, `--text*`, `--border*`, `--nav-*`), utility classes (`bg-page`, `bg-component`, `app-header`, `nav-*`), motion (`fan-spin`, `alarm-flash`), **fixed `--alarm-*`** |

| Do | Don’t |
|----|--------|
| Map semantics with `var(--neutral-*)` | Redefine `--neutral-*` hex in the stylesheet |
| Bind views with **simple CSS class names** | Create Designer Style Classes (`Fonts/Label`, `Colors/Header`, …) |
| Put page fills on classes (`bg-page`) | Hardcode `#D8D8D8` / `#1A2329` in `view.json` for chrome |

CSS-only rule: all Perspective styling lives in the Advanced Stylesheet; views set `props.style.classes` to those class names (Perspective prefixes them as `.psc-*`).

---

## 4. What themes (in scope)

Themes drive **ambient chrome** — anything that should feel light/dark and cool/warm:

| Surface | Expected approach |
|---------|-------------------|
| **Page / overview backgrounds** | Root class `bg-page` → `--surface-page` |
| **Header / masthead** | `app-header` or `bg-header` → `--surface-header` |
| **Nav / dock** | `nav-*` classes → `--surface-nav`, `--text-nav`, `--icon-nav`, `--border-nav` |
| **Cards / panels** | `bg-component`, `bg-container`, `container-card` |
| **Faceplates** (`01_Popups/00_Faceplates/**`) | Same card/container classes; text/icons via `--text` / `--icon` / font classes |
| **Device components** (`02_Components/01_Devices/**`) | Housing, rings, blades, strokes from neutrals / `--surface-*` / `--deviceFill-*` mapped to `var(--neutral-*)` |
| **Status chips (normal)** | `Refridgeration_STS sts-<TOKEN>` — normal states (COOLING, IDLE, OFF, …) track theme grayscale |
| **Adhoc Trend / `/trending`** | Page + toolbars + chart **background / grid / axes** theme; faceplates use `bg-container` / `container-card` |
| **Ticket Logger** | Popup / context-menu chrome via `bg-component`, cards, `--neutral-*` icons |
| **ChangeTheme gear UI** | Selection chrome already bound to `--neutral-*` expressions |

**OK to keep fixed (not “chrome”):**

- Trend **pen / series** qualitative colors (data encoding).
- Saturated **attention** accents for FAULT / DEFROST / MANUAL (ISA-101), separate from alarm-table tokens — but do not freeze *normal* device fills as cool-gray forever.

Hex tables and Figma → semantic mapping: [theme-figma-tokens.md](./theme-figma-tokens.md).

---

## 5. What never changes: alarm colors only

**Only `--alarm-*` (and consumers that paint true alarm priority) stay fixed across all four themes.**

| Token family | Behavior |
|--------------|----------|
| `--alarm-critical` / `-high` / `-medium` / `-low` (+ ack variants) | Locked hex in Advanced Stylesheet |
| Alarm Status Table row classes, DeviceAlarmIndicator priority, alarm borders/icons | Use `--alarm-*` — same hue in light, dark, warm, cool |

Do **not** treat `--sts-*` normal fills or `--deviceFill-running|stopped` as permanently theme-locked. Intended design remaps those to `var(--neutral-*)` so device chrome follows the active theme. (Some stylesheet values may still be fixed hex until implementers finish that pass.)

Verify: flip ChangeTheme through all four modes — pages, header, nav, faceplates, Ticket Logger, trending chrome, and devices should shift; **alarm table / alarm icons should not change hue**.

---

## 6. How to add a new themed surface

1. **Pick a semantic token** (or add one alias in `stylesheet.css` that points at `var(--neutral-*)` — never a mode-specific hex):

   ```css
   :root {
     --surface-my-panel: var(--neutral-20);
     --text-my-panel: var(--neutral-100);
   }
   ```

2. **Expose a utility class** in the Advanced Stylesheet:

   ```css
   .psc-bg-my-panel {
     background-color: var(--surface-my-panel);
     color: var(--text-my-panel);
   }
   ```

3. **Bind the view** with the simple class name (no Designer Style Class):

   ```json
   "style": { "classes": "bg-my-panel" }
   ```

4. **Avoid** `props.style.backgroundColor: "#…"` for anything that should follow themes.
5. **Scan** projects (and config if you touched themes) so the gateway reloads; hard-refresh the client.
6. **Smoke-test** Light/Dark × Cool/Warm via ChangeTheme.

If the surface is an IA built-in (button, table, input), prefer adjusting gateway theme variables / palette CSS rather than fighting with one-off hex in the view.

---

## 7. Scrollbars

Perspective’s browser client is **Chromium**, so Advanced Stylesheet `::-webkit-scrollbar*` rules apply. Firefox users get `scrollbar-width` / `scrollbar-color`.

| Class | Role |
|-------|------|
| `unit-overview-grid` | `/devices` Level 3 card wrap — `overflow-x: hidden`, flex `min-width: 0`, themed vertical bars |
| `unit-overview-host` | Embedded Unit Overview root / table hosts — same H-overflow clamp; vertical scroll kept |
| `themed-scroll` | Optional app-wide themed scroll chrome (`--neutral-50` thumb on `--neutral-20` track; hover uses `--accent`) |

Horizontal bars on Unit Overview tables are suppressed (`overflow-x: hidden` + zero-height horizontal webkit scrollbar). Do **not** set `overflow: hidden` on those hosts if tall tables still need vertical scrolling.

---

## 8. Related docs

| Doc | Use when |
|-----|----------|
| [theme-figma-tokens.md](./theme-figma-tokens.md) | Hex extracts per mode, Figma node index, accent notes, alarm lock table |
| [ignition-theme-architecture.md](./ignition-theme-architecture.md) | Full 8.3 folder layout, thin vs full themes, implementer checklist, Edge caveats |

---

## 9. Figma source

- **File:** [Dev Jam](https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w/Dev)  
- **fileKey:** `Q8EmmXokQsiX91aPMtLm2w`  
- **Page:** `Dev Jam` (`25:2`)  
- **Authority for device chrome:** Theme variants on Evaporator / Pump / Exhaust Fan / etc. (`Theme` = Light \| Dark \| Light Warm \| Dark Warm)  
- **Alarm samples:** Labels / Alarms frames near `89:1546` / `89:1581`

There is no separate Figma “chrome matrix” (masthead × 4, faceplate × 4, …) yet — page/faceplate/trend/Ticket Logger chrome follows the shared semantic tokens documented above and in the Figma token extract.

---

## Operator tip

Use the settings gear → ChangeTheme anytime. Cool/Warm only flips the neutral (and accent) family; Light/Dark flips surface inversion. Animations Off freezes fans / alarm blink / spray motion without changing colors. Alarms keep the same priority colors so severity stays recognizable on every mode.
