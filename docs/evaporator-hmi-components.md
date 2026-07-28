# BH Evaporator HMI — Component Guide

Onboarding guide for the Boars Head (BH) Ignition Perspective evaporator demo. Read this if you are new to the project and need to understand pages, embedded views, tags, CSS, and scripts.

| | |
|---|---|
| **Gateway / project** | Docker Standard gateway · Ignition **8.1.43** · project **BH** |
| **Perspective root** | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/` |
| **Scripts** | `gateways/standard/data/projects/BH/ignition/script-python/shared/` |
| **Demo tags** | Import `taginstances.json` under `[default]Evaporators` |
| **Compressor tags** | Import `taginstances-compressors.json` under `[default]Compressors` |
| **Exhaust Fan tags** | Import `taginstances-exhaust-fans.json` under `[default]ExhaustFans` |
| **Cooling Tower tags** | Import `taginstances-cooling-towers.json` under `[default]CoolingTowers` |
| **Alarm UDT / Flash** | Import `tags-alarms.json` at provider root (`_Config`, `Config/_Alarms`) |

Designer tip: after editing files on disk, **Update Project** (or restart the gateway if icons/CSS do not pick up).

---

## Mental model

```
Page: Evaporators/Overview  (URLs: /  and  /evaporators)
  │
  └─ Embedded device view  (Evaporator — single fan)
       params: tagPath, faceplate
       │
       ├─ IconHeader               ← former alarm-icon slot (symbols TBD)
       ├─ Label + faceplate icon   ← metadata / material/fullscreen
       ├─ Graphic + AlarmHeader    ← overlay badge + priority border
       ├─ AnalogValue              ← Temp/Value
       ├─ StatusIndicator          ← Status/Value (+ states metadata)
       └─ onClick                  → popup Faceplates/Evaporator (same tagPath)
```

Everything is **tag-path driven**. Pass a device UDT path like `[default]Evaporators/EV-02` into `tagPath`; children resolve nested tags relative to that path.

---

## Pages

| View path | Page URL | Role |
|-----------|----------|------|
| `00_Pages/Evaporators/Overview` | `/` and `/evaporators` | 4×4 grid of 16 single-fan evaporators (`EV-01`…`EV-16`) |
| `00_Pages/Compressors/Overview` | `/compressors` | COMP-01..03 NH3 compressor devices (Figma layout) |
| `00_Pages/ExhaustFans/Overview` | `/exhaust-fans` | EFAN-01..03 radiator-style exhaust fans (impeller spins on Run) |
| `01_Popups/00_Faceplates/ExhaustFan` | *(popup, not a page)* | Exhaust Fan faceplate (status + analog) |
| `00_Pages/CoolingTowers/Overview` | `/cooling-towers` | CT-01..03 BH-style towers (Hoffman silhouette) |
| `01_Popups/00_Faceplates/CoolingTower` | *(popup, not a page)* | Cooling Tower faceplate (status + analog) |
| `00_Pages/Unit/Overview` | *(not mapped in page-config)* | Table overview; cells are view paths + live tag paths |
| `00_Pages/NoViewPath` | — | Stub |
| `01_Popups/00_Faceplates/Evaporator` | *(popup, not a page)* | Faceplate opened from a device click |
| `01_Popups/00_Faceplates/Compressor` | *(popup, not a page)* | Compressor faceplate (status + analog) |

Page config lives at:

`com.inductiveautomation.perspective/page-config/config.json`

### Overview page layout

`Evaporators/Overview` is a column flex container (light gray background, black labels), matching Compressors / Cooling Towers:

1. **Title / subtitle** — 16 single-fan plant overview
2. **Four rows × four embeds** — `EV-01`…`EV-16`, all `02_Components/01_Devices/Evaporator`

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
| `Evaporator` | 1 (`Fan 1`) | ~96 × 176 |
| `EvaporatorDual` | 2 | ~120 × 176 (available; not on Overview) |
| `EvaporatorTriple` | 3 | ~168 × 176 (available; not on Overview) |

### Params

| Param | Type | Meaning |
|-------|------|---------|
| `tagPath` | string | Root of a `Devices/Evaporator` UDT instance |
| `faceplate` | string or null | Faceplate view name under `01_Popups/00_Faceplates/`. If null/empty, click does nothing and the fullscreen icon is hidden (opacity 0). |

### What they embed / contain

Top → bottom:

| Piece | Type | Behavior |
|-------|------|----------|
| `IconHeader` | Embedded view | Left of label (Scout-style header slot; symbols TBD) |
| Device name label | `ia.display.label` | `tagPath` metadata `shortDescription`, else last path segment |
| Faceplate affordance | `ia.display.icon` `material/fullscreen` | Right side; only meaningful when `faceplate` is set |
| Fan SVG(s) | Drawing / icon group | Spin when that fan’s `CMD/Value` is true |
| `AlarmHeader` | Embedded view | Alarm badge overlays Graphic (top-left) + priority border |
| `AnalogValue` | Embedded view | Temperature |
| `StatusIndicator` | Embedded view | COOL / OFF / DEF (+ stage under) / Operator + tooltips |

### Key bindings (pattern)

| Concern | Binding |
|---------|---------|
| Status | `{tagPath}/Status/Value` → StatusIndicator |
| Temp | `{tagPath}/Temp/Value` → AnalogValue |
| Fan running | `{tagPath}/Fan N/CMD/Value` (Boolean) |
| Fan spin CSS | Script transform on blades: return `'fan-spin'` if CMD is true, else `''` |
| Alarm overlay | AlarmHeader `params.tagPath` = device `tagPath`; Graphic classes `alarm-border alarm-priority-*` |
| Icon header | IconHeader `params.tagPath` = device `tagPath` (slot only until symbol ticket) |
| Click | `system.perspective.openPopup(...)` → `01_Popups/00_Faceplates/{faceplate}` with `{ tagPath }`, popup id like `ev-fp-{tagPath}` |

Cooling (**COOL**) is a **status**, not “running.” Running is communicated only by **spinning fans** (CMD on).

---

## Element views

Path: `views/03_Elements/`

### StatusIndicator — `01_Status/StatusIndicator`

- **Param:** `tagPath` → full path to `.../Status/Value`
- Reads the value and optional `.Metadata.states`
- Maps demo integers to codes and colors (inline style, not the STS CSS classes):

| Value | Code | Color (approx) |
|------:|------|----------------|
| 0 | OFF | gray `#9E9E9E` |
| 1 | COOL | blue `#1E88E5` |
| 2 | DEF | pink `#EC407A` |
| 3 | FLT | red `#C62828` |
| 4 | Operator | amber `#FF8F00` |
| 5 | IDLE | green `#228B22` |
| 6 | 1.PD | pink `#EC407A` |
| 7 | 2.HG | pink `#EC407A` |
| 8 | 3.BLD | pink `#EC407A` |
| 9 | 3.FD | pink `#EC407A` |

**Important:** status `1` is **COOL** (cooling), not green RUN. Fan spin is separate. Enum value `4` (Manual) displays as **Operator**. Defrost steps show **DEF** on the primary line with the stage code (`1.PD` / `2.HG` / `3.BLD` / `3.FD`) under it. Tooltips use the parenthetical descriptions from the ticket (Cooling, Pump Down, Achieved Temp Setpoint, …).

### AlarmHeader — `01_Status/AlarmHeader`

Scout-style overlay alarm badge (same tag bindings as the former label-row `DeviceAlarmIndicator`). Sits on the device Graphic with CSS `alarm-header` + priority-colored `alarm-border`.

### IconHeader — `01_Status/IconHeader`

Occupies the former alarm-icon slot beside the device label. `custom.icons.{fault,operator,disabled,oos}` stubs are ready; Figma/Ignition symbols land in a follow-up ticket.

### AnalogValue — `01_Status/AnalogValue`

- **Params:** `tagPath` (…`/Temp/Value`), optional `spTagPath`, spacing helpers (`center` / `data` / `engUnit`)
- If `spTagPath` is empty, derives sibling `…/Temp/SP` from `tagPath` ending in `/Value`
- Embeds `_Assets/Numeric`; value text turns theme-invariant red when `Value > SP`
- **SP lives only on device `Temp/SP`** (member name literally `SP`, sibling of `Temp/Value`). Do **not** also add `SP` on `_Root/Analog` — Ignition renames the device member to `SP_duplicate_1` and AnalogValue’s `…/Value` → `…/SP` derivation breaks.
- Defaults: Evap **35°F**, CT **85°F**, Pump **50 gpm**, ExhaustFan **1000 cfm**, Compressor **25 psi**
- Over-SP demos: **EV-02** (40), **CT-01** (90), **PMP-01** (60), **EFAN-01** (1200), **COMP-01** (35)

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
| `device-comm-loss` | SVG fills → `--deviceFill-commLoss` (theme-invariant red) | Device `Graphic` when `Status/Value` quality ≠ Good |
| `Refridgeration_STS` + `sts-COOLING` / `sts-IDLE` / `sts-COMMLOSS` / … | ISA-101-ish status chip palette | Prefer when wiring StatusIndicator |
| `font-label` / `font-value` / `font-title` / `font-livedata` / … | Typography | Labels, values, live data, buttons |
| `bg-header` / `bg-component` / `bg-container` / … | Background colors | Headers, cards, surfaces |
| `container-card` / `container-button` / … | Borders, shadows, hover | Cards, buttons, chrome |

Former Designer Style Classes (`Fonts/Label`, `Colors/Header`, `Container/Card`, …) were migrated into these CSS names; the Style Class folders were removed.

### Comm Loss (quality-driven)

**Signal:** `qualityOf(tag({tagPath} + '/Status/Value')) != 'Good'` (empty `tagPath` → not Comm Loss on graphics; StatusIndicator shows blank).

No dedicated `CommFail` PLC bit required — Ignition tag quality covers OPC disconnect / Bad / Uncertain. Optional future: AND a CommFail bit if plant tags add one.

**Priority:** Comm Loss (Bad quality) wins over any Status enum. Manual is not shown as a status code.

**UI:** StatusIndicator text = `Comm Loss` (red); device Graphic class `device-comm-loss` fills the component red via `--deviceFill-commLoss` / `sts-COMMLOSS`. Device bodies are otherwise grayscale — status colors apply to StatusIndicator text only.

**Demo (single instance only):** `[default]Evaporators/EV-01/Status/Value` has `"enabled": false` in `tag-definition/default/Evaporators/udts.json`. That forces Bad quality on **EV-01 only**. Do **not** put `enabled: false` on the Evaporator UDT type (that broke every EV previously). To restore: set `enabled: true` (or remove the key) on that one leaf, then POST scan/config.

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
| `taginstances-compressors.json` | Folder `Compressors` → `[default]Compressors/COMP-*` | Demo compressors (Run / Off / Fault) |
| `taginstances-exhaust-fans.json` | Folder `ExhaustFans` → `[default]ExhaustFans/EFAN-*` | Demo exhaust fans (Run spins impeller) |
| `taginstances-cooling-towers.json` | Folder `CoolingTowers` → `[default]CoolingTowers/CT-*` | Demo cooling towers |
| `tags.json` | As needed | Overview UDT definition (`Rebuild`, `Instances`, …) |

### Evaporator instance shape

```text
[default]Evaporators/EV-XX/          typeId: Devices/Evaporator
  Status/Value                       Int4 + metadata.states (0–5)
  Temp/Value                         Float + eng unit
  Pressure/Value                     Float + eng unit
  Fan 1/                             (plant Overview set is single-fan only)
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

### Plant EV set (Overview + sim)

Gateway tags and plant sim are slimmed to **16 single-fan** instances `EV-01`…`EV-16` (Fan 1 only; no Fan 2/3). Legacy `EV-17`–`EV-33` and `EV-001`–`EV-003` placeholders were removed.

**Status enum (Evaporator):** `0` Off(OFF) · `1` Cooling(COOL) · `2` Defrost(DEF) · `3` Fault(FLT) · `4` Manual(Operator) · `5` Idle · `6` Pump Down(1.PD) · `7` Hot Gas(2.HG) · `8` Bleed(3.BLD) · `9` Fan Delay(3.FD). Comm Loss = Bad quality on `Status/Value`, not an enum int.

| EV | Demo | Status int | Fan CMD | Notes |
|----|------|------------|---------|-------|
| 01 | Comm Loss | *(ignored)* | false | `Status/Value` `enabled: false` |
| 02 | Cooling + over-SP | 1 | true | Temp **40** fixed; SP **35** → AnalogValue red |
| 03 / 08 / 13 | Idle | 5 | false | Temp under SP |
| 04 | Defrost | 2 | false | DEF |
| 05 | Off | 0 | false | |
| 06 / 11 / 16 | Fault | 3 | false | Fault true |
| 07 | Cooling | 1 | true | Temp under SP (contrast vs EV-02) |
| 09 | Pump Down | 6 | false | 1.PD |
| 10 | Bleed | 8 | false | 3.BLD |
| 12 | Operator | 4 | false | Manual / Operator |
| 14 | Hot Gas | 7 | false | 2.HG |
| 15 | Fan Delay | 9 | false | 3.FD |

**Non-EV Overview (CT / Pump / Fan / Comp):** four instances each — `*-01` Run(`1`) · `*-02` Idle(`4`) · `*-03` Fault(`2`) · `*-04` Off(`0`). Enum: `0` Off(OFF) · `1` Run · `2` Fault(FLT) · `3` Manual(Operator) · `4` Idle. Over-SP AnalogValue red on **CT-01** (90>85), **PMP-01** (60>50), **EFAN-01** (1200>1000), **COMP-01** (35>25).

Sim profiles live in `sim/build_plant_sim.py` → `sim/bh-plant-sim.csv` and gateway `opcua/device/Sim/instructions.csv`. Rebuild: `python sim/build_plant_sim.py` then POST scan/config (or restart Sim device) so OPC picks up the CSV.

**Note:** Adhoc Trend’s saved tag tree may still list old `EV-001` / `EV-17+` paths until refreshed in Designer; live Overview / tags use `EV-01`…`EV-16` only.

---

## Icons

Custom Perspective icon library (gateway module data, **not** inside the BH project folder):

`gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/icons/equipment/equipment.svg`

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
| No COOL / wrong green “RUN” | StatusIndicator mapping; status value should be `1` for cooling |
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
