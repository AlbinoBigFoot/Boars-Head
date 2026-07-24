# BH Evaporator HMI — Component Guide

Onboarding guide for the Boars Head (BH) Ignition Perspective evaporator demo. Read this if you are new to the project and need to understand pages, embedded views, tags, CSS, and scripts.

| | |
|---|---|
| **Gateway / project** | Docker Standard gateway · Ignition **8.1.43** · project **BH** |
| **Perspective root** | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/` |
| **Scripts** | `gateways/standard/data/projects/BH/ignition/script-python/shared/` |
| **Demo tags** | Import `taginstances.json` under `[default]Evaporators` |
| **Alarm UDT / Flash** | Import `tags-alarms.json` at provider root (`_Config`, `Config/_Alarms`) |

Designer tip: after editing files on disk, **Update Project** (or restart the gateway if icons/CSS do not pick up).

---

## Mental model

```
Page: Evaporators/Overview  (URLs: /  and  /evaporators)
  │
  └─ Embedded device view  (Evaporator | EvaporatorDual | EvaporatorTriple)
       params: tagPath, faceplate
       │
       ├─ DeviceAlarmIndicator     ← _Alarms/_Active, _Unack, _ActiveHighPriority
       ├─ Label + faceplate icon   ← metadata / material/fullscreen
       ├─ SVG fan graphic(s)       ← Fan N/CMD/Value + CSS class fan-spin
       ├─ AnalogValue              ← Temp/Value
       ├─ StatusIndicator          ← Status/Value (+ states metadata)
       └─ onClick                  → popup Faceplates/Evaporator (same tagPath)
```

Everything is **tag-path driven**. Pass a device UDT path like `[default]Evaporators/EV-02` into `tagPath`; children resolve nested tags relative to that path.

---

## Pages

| View path | Page URL | Role |
|-----------|----------|------|
| `00_Pages/Evaporators/Overview` | `/` and `/evaporators` | Flex demo: status matrix + alarming matrix of device graphics |
| `00_Pages/Unit/Overview` | *(not mapped in page-config)* | Table overview; cells are view paths + live tag paths |
| `00_Pages/NoViewPath` | — | Stub |
| `01_Popups/00_Faceplates/Evaporator` | *(popup, not a page)* | Faceplate opened from a device click |

Page config lives at:

`com.inductiveautomation.perspective/page-config/config.json`

### Overview page layout

`Evaporators/Overview` is a column flex container (light gray background, black labels).

1. **Title / subtitle**
2. **Column headers** — 1 Fan · 2 Fan · 3 Fan
3. **Status rows** — Off, Cooling, Defrost, Fault, Manual, Idle  
   Each row embeds one single-, dual-, and triple-fan device bound to the EV tags below.
4. **Alarming section** — Critical / High / Medium / Low rows (same 1/2/3-fan columns)
5. **Legend**

Every device instance passes:

```text
tagPath  = [default]Evaporators/EV-##
faceplate = "Evaporator"
```

---

## Device components (embedded views)

Path: `views/02_Components/01_Devices/`

| View | Fans | Typical size |
|------|------|--------------|
| `Evaporator` | 1 (`Fan 1`) | ~96 × 167 |
| `EvaporatorDual` | 2 | ~120 × 176 |
| `EvaporatorTriple` | 3 | ~168 × 176 |

### Params

| Param | Type | Meaning |
|-------|------|---------|
| `tagPath` | string | Root of a `Devices/Evaporator` UDT instance |
| `faceplate` | string or null | Faceplate view name under `01_Popups/00_Faceplates/`. If null/empty, click does nothing and the fullscreen icon is hidden (opacity 0). |

### What they embed / contain

Top → bottom:

| Piece | Type | Behavior |
|-------|------|----------|
| `DeviceAlarmIndicator` | Embedded view | Alarm badge (left of label) |
| Device name label | `ia.display.label` | `tagPath` metadata `shortDescription`, else last path segment |
| Faceplate affordance | `ia.display.icon` `material/fullscreen` | Right side; only meaningful when `faceplate` is set |
| Fan SVG(s) | Drawing / icon group | Spin when that fan’s `CMD/Value` is true |
| `AnalogValue` | Embedded view | Temperature |
| `StatusIndicator` | Embedded view | CLG / STOP / DFT / … |

### Key bindings (pattern)

| Concern | Binding |
|---------|---------|
| Status | `{tagPath}/Status/Value` → StatusIndicator |
| Temp | `{tagPath}/Temp/Value` → AnalogValue |
| Fan running | `{tagPath}/Fan N/CMD/Value` (Boolean) |
| Fan spin CSS | Script transform on blades: return `'fan-spin'` if CMD is true, else `''` |
| Alarm | DeviceAlarmIndicator `params.tagPath` = device `tagPath` |
| Click | `system.perspective.openPopup(...)` → `01_Popups/00_Faceplates/{faceplate}` with `{ tagPath }`, popup id like `ev-fp-{tagPath}` |

Cooling (**CLG**) is a **status**, not “running.” Running is communicated only by **spinning fans** (CMD on).

---

## Element views

Path: `views/03_Elements/`

### StatusIndicator — `01_Status/StatusIndicator`

- **Param:** `tagPath` → full path to `.../Status/Value`
- Reads the value and optional `.Metadata.states`
- Maps demo integers to codes and colors (inline style, not the STS CSS classes):

| Value | Code | Color (approx) |
|------:|------|----------------|
| 0 | STOP | gray |
| 1 | CLG | cyan `#039BE5` |
| 2 | DFT | amber |
| 3 | FLT | red |
| 4 | MAN | magenta |
| 5 | IDLE | gray |

**Important:** status `1` is **CLG** (cooling), not green RUN. Fan spin is separate.

### AnalogValue — `01_Status/AnalogValue`

- **Params:** `tagPath`, spacing helpers (`center` / `data` / `engUnit`)
- Embeds `_Assets/Numeric`, which formats `tag(tagPath)`, engineering unit, and format string from tag properties

### DeviceAlarmIndicator — `01_Status/NotificationIcons/DeviceAlarmIndicator`

Used on the **graphic** Overview devices.

| Binding | Tag |
|---------|-----|
| Show/hide | `{tagPath}/_Alarms/_Active` |
| Blink CSS | `alarm-flash` when `_Active && _Unack` |
| Icon path | `_ActiveHighPriority` → `equipment/alarm_*` |

Priority convention on these memory tags:

| Priority | Icon path |
|---------:|-----------|
| 1 | `equipment/alarm_critical` |
| 2 | `equipment/alarm_high` |
| 3 | `equipment/alarm_medium` |
| 4 | `equipment/alarm_low` |
| 10 | none / unused |

Blink is **CSS** (see below). Does **not** require `_Config/Flash` for Overview badges.

### DeviceLabelAlarmIndicator — `03_Table/DeviceLabelAlarmIndicator`

Used in the **table** Overview (device name column).

| Binding | Tag |
|---------|-----|
| Icon visibility | `{value}/_Alarms/_Flash` |
| Icon view path | `{value}/_Alarms/_Icon` |
| Label text | metadata / tag name |

Here blink is **tag-driven** via `_Flash` (which uses `_Config/Flash` when unacked).

### Other notification helpers

| View | Role |
|------|------|
| `NotificationIcons/Alarms/Critical\|High\|Medium\|Low` | Thin wrappers around `equipment/alarm_*` icons |
| `NotificationIcons/Blank` | Empty / transparent placeholder |
| `NotificationIcons/ElementAlarmIndicator` | Per-tag Ignition alarm props (`.../Value/Alarms.*`) + `[default]_Config/Flash` |
| `NotificationIcons/TableAlarmIndicator` | Table cell helper bound to `_Flash` / `_Icon` |
| `NotificationIcons/CommLoss` | Comm-loss indicator |

**Priority caveat:** Ignition’s native alarm priority numbering (often 4=Critical … 1=Low) is **opposite** of this project’s `_ActiveHighPriority` memory convention (1=Critical … 4=Low). Do not mix the two without converting.

### Table cell views

Under `03_Elements/03_Table/`: `Boolean`, `Numeric`, `String` — used by the Unit/Overview table for live values from tag paths stored in the Overview document.

---

## CSS (Advanced Stylesheet) — the only styling system

**File:** `com.inductiveautomation.perspective/stylesheet/stylesheet.css`

**Rule:** All look-and-feel lives in this CSS file unless you are explicitly told otherwise. Do **not** create Designer Style Classes under Styles → Colors / Container / Fonts.

Perspective prefixes advanced stylesheet classes with `psc-`. When a binding sets `style.classes` to `fan-spin`, the rule that applies is `.psc-fan-spin`.

| Class (as set in bindings) | Effect | When applied |
|----------------------------|--------|--------------|
| `fan-spin` | Counter-clockwise rotate, 1.25s linear infinite | Fan blades when `Fan N/CMD/Value` is true |
| `alarm-flash` | Opacity blink, 1s steps | DeviceAlarmIndicator when active **and** unacked |
| `Refridgeration_STS` + `sts-COOLING` / `sts-IDLE` / … | ISA-101-ish status chip palette | Prefer when wiring StatusIndicator |
| `font-label` / `font-value` / `font-title` / `font-livedata` / … | Typography | Labels, values, live data, buttons |
| `bg-header` / `bg-component` / `bg-container` / … | Background colors | Headers, cards, surfaces |
| `container-card` / `container-button` / … | Borders, shadows, hover | Cards, buttons, chrome |

Former Designer Style Classes (`Fonts/Label`, `Colors/Header`, `Container/Card`, …) were migrated into these CSS names; the Style Class folders were removed.

---

## Scripts (project library `shared`)

Path: `ignition/script-python/shared/`

| Module | Purpose |
|--------|---------|
| `shared.Alarms` | `rebuild(...)` — rebuilds expression-driven members under a `Config/_Alarms` instance from browsed alarm sources. Hooked from UDT `Rebuild` valueChanged. Demo currently relies more on **memory** overrides than a full live rebuild. |
| `shared.Overview` | `rebuildOverview` / `rebuildFromRebuildTag` — builds the table document `{columns, data}` into `.../Overview/Instances/Value` by discovering evaporator UDT instances. Device Name column points at `DeviceLabelAlarmIndicator`. |
| `shared.Utilities` | Helpers such as `getLabelValue` for multistate boolean table cells |

Trigger pattern for Overview rebuild: write `True` to the Overview UDT’s `Rebuild` tag (see `tags.json` / imported Overview instance); the valueChanged script calls `shared.Overview.rebuildFromRebuildTag` and clears the flag.

---

## Tags

### Import files (repo root)

| File | Import target | Contents |
|------|---------------|----------|
| `tags-alarms.json` | Provider **root** | `_Config` (Flash, Icons, Colors) + UDT type `Config/_Alarms` |
| `taginstances.json` | Folder `Evaporators` (or import so paths are `[default]Evaporators/EV-*`) | Demo evaporators + Overview instance |
| `tags.json` | As needed | Overview UDT definition (`Rebuild`, `Instances`, …) |

### Evaporator instance shape

```text
[default]Evaporators/EV-XX/          typeId: Devices/Evaporator
  Status/Value                       Int4 + metadata.states (0–5)
  Temp/Value                         Float + eng unit
  Pressure/Value                     Float + eng unit
  Fan 1|2|3/
    CMD/Value                        Boolean  ← fan-spin
    SPD_FBK/Value                    Float
    Fault/Value                      Boolean
  _Alarms/                           typeId: Config/_Alarms
    _Active                          Boolean (memory in demo)
    _Unack                           Boolean (memory in demo)
    _ActiveHighPriority              Int4 1–4 or 10
    _UnackHighPriority               Int4
    _Flash                           expr (see below)
    _Icon, _Color, counts            expr (UDT defaults)
```

### Alarm / flash semantics

| Tag | Role |
|-----|------|
| `_Active` | Any active alarm → badge visible |
| `_Unack` | Unacknowledged → should blink; `false` while still active = **acked** → solid |
| `_ActiveHighPriority` | Which icon (1 Crit … 4 Low) |
| `_Config/Flash` | 1 Hz clock: `getSecond(now()) % 2 = 0` |
| `_Flash` | `if(_Active, if(_Unack, {_Config/Flash}, True), False)` |

**Two blink mechanisms:**

1. **Overview device badge** — CSS `alarm-flash` when `_Active && _Unack` (no Flash tag required for this path).
2. **Table label icon** — visibility bound to `_Flash`, which needs `_Config/Flash` when unacked.

To **ack** in the demo: set `_Alarms/_Unack` to `false` (leave `_Active` true) → icon stays on, stops flashing.

### Demo EV matrix

Status rows on the Overview page:

| Row | 1-fan | 2-fan | 3-fan | Status | Fans CMD on |
|-----|-------|-------|-------|--------|-------------|
| Off | EV-01 | EV-08 | EV-15 | 0 STOP | — |
| Cooling | EV-02 | EV-09 | EV-16 | 1 CLG | 1 / 1–2 / 1–3 |
| Defrost | EV-03 | EV-10 | EV-17 | 2 DFT | — |
| Fault | EV-04 | EV-11 | EV-18 | 3 FLT | — (+ Critical unack) |
| Manual | EV-05 | EV-12 | EV-19 | 4 MAN | — |
| Idle | EV-06 | EV-13 | EV-20 | 5 IDLE | — |

Alarming rows (Idle status, Active + Unack, priority by row):

| Priority | 1-fan | 2-fan | 3-fan |
|----------|-------|-------|-------|
| Critical (1) | EV-22 | EV-26 | EV-30 |
| High (2) | EV-23 | EV-27 | EV-31 |
| Medium (3) | EV-24 | EV-28 | EV-32 |
| Low (4) | EV-25 | EV-29 | EV-33 |

Gaps at EV-07 / EV-14 / EV-21 are intentional (old “cooling + fans” row removed).

Table Overview document currently samples Cooling demos **EV-02, EV-09, EV-16**. A full rebuild can rediscover instances under the folder.

---

## Icons

Custom Perspective icon library (gateway module data, **not** inside the BH project folder):

`gateways/standard/data/modules/com.inductiveautomation.perspective/icons/equipment.svg`

Also registered in `icons.digest.json` (SHA). After changing SVG files, restart the gateway so 8.1 picks them up.

| Library path | Use |
|--------------|-----|
| `equipment/alarm_critical` | Red square + C |
| `equipment/alarm_high` | Orange triangle + H |
| `equipment/alarm_medium` | Yellow inverted triangle + M |
| `equipment/alarm_low` | Purple diamond + L |

`_Config/Icons/Alarms/*` store **view paths** (e.g. `03_Elements/.../Alarms/Critical`) for table cells; those views in turn reference the `equipment/*` icons. `_Config/Colors/Alarms/*` hold matching hex colors.

---

## Embedded views — how Perspective nests them

Ignition Perspective “Embedded View” components (`ia.display.view`) load another view by **path** and pass **params**.

Examples in this project:

| Parent | Child path | Params passed |
|--------|------------|---------------|
| Overview page | `02_Components/01_Devices/Evaporator` (etc.) | `tagPath`, `faceplate` |
| Device | `03_Elements/.../DeviceAlarmIndicator` | `tagPath` |
| Device | `03_Elements/01_Status/AnalogValue` | `tagPath` → Temp |
| Device | `03_Elements/01_Status/StatusIndicator` | `tagPath` → Status/Value |
| AnalogValue | `03_Elements/01_Status/_Assets/Numeric` | formatting inputs |
| DeviceLabelAlarmIndicator | `03_Elements/.../Alarms/{priority}` or Blank | via `_Icon` string |

Changing a child view updates every parent that embeds it — that is why StatusIndicator and DeviceAlarmIndicator are shared elements.

---

## Faceplate popup

- View: `01_Popups/00_Faceplates/Evaporator`
- Opened only when device `faceplate` param is non-empty
- Receives the same `tagPath` so faceplate controls bind to the same UDT instance
- Overview always passes `faceplate: "Evaporator"`

---

## Quick troubleshooting

| Symptom | Check |
|---------|--------|
| No CLG / wrong green “RUN” | StatusIndicator mapping; status value should be `1` for cooling |
| Fans not spinning | `Fan N/CMD/Value` true? Advanced stylesheet loaded? Class name `fan-spin`? |
| Alarm badge missing | `_Alarms/_Active` memory true? Priority 1–4? Equipment icons registered + gateway restarted? |
| Badge solid, never blinks | `_Unack` must be true for CSS flash; for table icons, `_Flash` / `_Config/Flash` |
| Badge gone after “flash fix” | Do not bind visibility to Flash alone on DeviceAlarmIndicator — visibility is `_Active` |
| Table Overview empty | `Evaporators/Overview/Instances/Value`; try Overview `Rebuild` |
| Edits not visible | Update Project; for icons/CSS, gateway restart may be required |

---

## Related repo docs

| Doc | Topic |
|-----|--------|
| `README.md` | Docker stack, ports, planning |
| `docs/udt-evaporator-isa95.md` | UDT / ISA-95 notes |
| `docs/central-alarming.md` | Alarm Status Table, `/alarms`, unack vs ack colors |
| `.planning/*` | Project planning (GSD) |
