# Scout Faceplate Controls / Mode / Status / KPI — research brief

**Source:** `C:\Program Files\Inductive Automation\Perspective-8-3-Scout\data\projects\ScoutMotors`  
**Date:** 2026-07-30  
**Scope:** What Scout’s unified Faceplate actually embeds for “controls,” how Operator/Maintenance modes work, Start/Stop wiring, KPI discovery, tab hiding, layout/CSS, and compressor-specific notes.  
**Read-only on Scout.** Contrast with BH target layout in `CONTEXT.md` (Mode → Status/commands → KPI).

---

## Verdict (critical for BH redesign)

**Scout’s unified Faceplate has no Controls tab and no Mode → Status → KPI section stack.**

| BH target (CONTEXT) | Scout unified Faceplate |
|---------------------|-------------------------|
| Tab: **Controls** | **Does not exist** |
| Sections: Mode → Status/commands → KPI | N/A on shell |
| Start/Stop / Auto/Manual/Remote buttons | No dedicated control strip; commands live as **writable tags on Configuration** |
| Operator / Program / Maintenance mode chips | **Not faceplate mode buttons.** Operator + Maintenance are **status icons** on plant graphics (`IconHeader`). **No “Program” mode** in Scout faceplate/legend |
| KPI discovery | No faceplate KPI browse; sparse KPI in title / PIP cards |
| Tab hide-if-empty | Yes — browse + `getConfiguration` → `tagFlags.show*` |

`_Assets/Main` is the **Trend** tab body (history chart), not Controls. Do not port Main as a Controls layout.

Closest Scout analogues for BH Controls redesign:

1. **Commands / setpoints:** `Configuration/Configuration` + `ConfigurationRow` + `03_Elements/00_Control/*`
2. **Mode indicators (read-only):** `03_Elements/01_Status/IconHeader` + Legend
3. **Light KPI:** `_Assets/Title` (Pump Starts) and PIP unit cards (hardcoded KPIs, not Faceplate)

BH’s existing `_Assets/Compressor/Controls` (Operator/Program/Maintenance chips + CP/SV Remote/Auto/Manual + FLA/SVP/DisP/Amps) is **BH-invented**, not a Scout Faceplate port.

---

## 1. Section order (Mode → Status/commands → KPI)

**On unified Faceplate: none of these sections exist.**

Shell tab order (left → right, only if visible):

1. **Trend** → `01_Popups/00_Faceplates/_Assets/Main`
2. **Configuration** → `01_Popups/00_Faceplates/Configuration/Configuration`
3. **Alarm Configuration** → `01_Popups/00_Faceplates/Alarm Configuration/AlarmConfiguration`
4. **Alarms** → `01_Popups/00_Faceplates/Alarm/Alarms`

Default tab: first available among Trend → Configuration → Alarm Configuration → Alarms (`tagFlags.defaultTab`).

### Where Scout *does* put Mode / Status / KPI (outside Controls tab)

| Concern | Where | Order / structure |
|---------|--------|-------------------|
| Operator / Maintenance / Hand / OOS / Sim | Plant device chrome via `IconHeader` | Horizontal icon row (status only) |
| System Mode / PID / unit knobs | `HotWater/UnitControl` | **Card sections** (Header + ConfigurationRows): System Mode → Pump Speed Loop → … |
| Command (CMD) + SP + OVRD | Configuration tab (browse) or HotWater PumpConfiguration allow-list | Flat **row list**, not Mode/Status/KPI |
| Pump Starts KPI | Faceplate popup **Title** bar (`_Assets/Title`) | Title text + optional “Pump Starts: N” |
| Unit KPIs | PIP/Nugget cards (`02_Components/00_Units/...`) | Hardcoded flex KPI blocks on overview cards |

**Implication for BH:** Mode → Status → KPI is a **new product layout**. Scout supplies patterns for *pieces* (icons, CMD writes, title KPI), not a ready-made Controls view to copy.

---

## 2. Operator / Program / Maintenance modes

### What Scout has

| Mode | Tag (under device `tagPath`) | UI | Writable from Faceplate? |
|------|------------------------------|----|--------------------------|
| **Operator** | `/OPER` | Icon in `IconHeader`; Legend: “Operator Mode Enabled” | No — indicator only |
| **Maintenance** | `/MAINT` | Icon in `IconHeader`; Legend: “A component has been manually disabled from the HMI” | No — indicator only |
| **Hand** | `/H` | Icon; Legend: “controlled from outside the HMI” | Indicator only |
| **Out of Service** | `/OOS` | Icon | Indicator only |
| **Simulate** | `/SIM` | Icon | Indicator only |
| **Not at setpoint** | `/MSMX` | Icon | Indicator only |
| **Stale** | `/YAI` | Icon | Indicator only |
| **Program** | — | **Not present** in IconHeader, Legend, or Faceplate | N/A |

**IconHeader binding pattern** (`03_Elements/01_Status/IconHeader`):

1. Quality gate: `qualityOf(tag(tagPath + '/OPER')) = 'Good'` (same for MAINT, H, …).
2. Display: if quality good, show icon when tag value is truthy; else hide.

Tag dictionary maps `"OPER": "Operator"` (`tags/tags.json`). These are **BACnet/UDT status bits**, not HMI role chips and not mutually exclusive mode *commands*.

### What “Operator” is *not* in Scout

- Not a Faceplate button that writes a mode.
- Not the same as session role `session.custom.Operator` (security/nav), though the name overlaps.
- Not BH’s placeholder chips (“bind later”) on Compressor Controls.

### HotWater “System Mode”

`HotWater/UnitControl` uses ConfigurationRows for tags like `STRTUP_SYS`, `STRTUP_AUTO_SYS_DLY` under a **“System Mode”** card header. That is unit-level startup/auto delay config, **not** Operator/Program/Maintenance.

### BH mapping note

CONTEXT wants Maintenance / Program / Operator as Controls section 1. Scout only documents **OPER + MAINT as status icons**. “Program” must come from BH PLC/FT conventions (or be dropped), not Scout Faceplate.

---

## 3. Start / Stop / Auto / Manual / Remote control wiring

### No Start/Stop button strip on Faceplate

Scout does **not** embed Start / Stop / Auto / Manual / Remote as labeled command buttons on the unified shell.

### How commands actually work

**Primary path — Configuration tab (browse):**

1. Recursive `system.tag.browse(tagPath)` → AtomicTags.
2. Keep tags where **Enabled**, **not readOnly**, **AlarmEvalEnabled ≠ True**.
3. FlexRepeater → `ConfigurationRow` per path.
4. `ConfigurationRow` routes by datatype:
   - Boolean / Int4 → `03_Elements/00_Control/MultiStateInput`
   - else → `03_Elements/00_Control/AnalogInput`
5. Writes: MultiStateInput → `APIModule.main.writeToTagAPIValue(tagPath, value)` (edit-pencil + dropdown). Older Boolean asset confirms via `HBT.Alerts` then `system.tag.writeBlocking`.

So a device **`CMD`** (Boolean or Int with `Metadata.states`) appears as a **config row** labeled from tag metadata shortDescription, not as “Start” / “Stop” chrome.

**HotWater PumpConfiguration allow-list** (device-specific Config, not unified browse):

```text
INCLUDE_NAMES = ('PDIT_SP', 'CMD', 'OVRD', 'SPD_MIN', 'RST_FLOW_PCT')
```

CMD is explicitly treated as a **configuration/control tag**, same row UI.

### Device graphic (not Faceplate)

`02_Components/01_Devices/Compressor` (and Pump/Fan/Valve/…):

- Command display: prefer `/CMD`, else `/SIG`
- Feedback: prefer `/STS`, else `/FB`
- Used for SVG/state coloring on the P&ID, not Faceplate buttons

### Auto / Manual / Remote

- **Not** discrete Faceplate buttons in Scout.
- Multi-state labels (if any) come from **tag `.Metadata.states`** (e.g. Boolean asset defaults `["No","Yes"]`).
- BH Compressor `CP_Mode` / `SV_Mode` → Remote(1) / Auto(2) / Manual(3) is **Quantum compressor UDT**, absent from Scout Faceplate Controls (Scout has no such view).

### RolesPermissions (documentation only)

`00_Pages/Administrative/RolesPermissions` lists capability strings like “Start/Stop”, “Mode - Auto/Manual” as **role matrix text**, not Faceplate wiring.

---

## 4. KPI discovery

| Mechanism | Used by Scout Faceplate? | Notes |
|-----------|--------------------------|--------|
| Fixed pen/KPI list by `deviceType` | **No** on unified Faceplate | Shell has **no** `deviceType` param |
| Tag browse for KPIs | **No** dedicated KPI browse | Browse is for Trend / Config / Alarm Config / Alarms |
| Hardcoded paths | Title only | `_Assets/Title`: `…/STRT_NUM` → “Pump Starts: …” when tag looks like HWP / VFD / VLV_BYP |
| PIP/Nugget fixed KPIs | Overview cards only | e.g. AHU PIP `KPIs` flex — fan speed fill bars, etc. |

**Configuration sample tags** in Designer defaults include `RT`, `STRT_NUM`, `MAN_DSBL`, `YAR_RST` — those appear **as config rows if writable**, not as a KPI section.

**Trend “KPIs”:** `_Assets/Main` discovers **history-enabled analog** leaves for the chart — operational trending, not runtime-hours KPI cards.

**BH today:** Compressor Controls hardcodes Status, FLA, SVP, DisP, Amps, Rung — fixed list under `tagPath`, not Scout browse.

---

## 5. Tab visibility / empty-tab hiding (shell)

**File:** `01_Popups/00_Faceplates/Faceplate/view.json`  
**Binding:** `custom.tagFlags` expr-struct on `tagPath` + `hiddenFrom*` params → script transform.

### Algorithm (summary)

1. Recursively enumerate leaf tags under `tagPath` (`system.tag.browse`).
2. Per leaf, `system.tag.getConfiguration(leaf, False)`:
   - **showTrend** — `historyEnabled` AND analog datatype AND not in `hiddenFromTrend`
   - **showConfiguration** — not `readOnly`, no alarms on tag, non-empty datatype, not in `hiddenFromConfiguration`
   - **showAlarmConfiguration** — has alarms, not in `hiddenFromAlarmConfiguration`
   - **showAlarms** — has alarms, not in `hiddenFromAlarms`
3. `defaultTab` = first true among Trend → Configuration → Alarm Configuration → Alarms.
4. Each tab button: `display: none` / `basis: 0px` / `grow: 0` when its flag is false.
5. Tab bar CSS class: `faceplate-buttons-{N}` where N = visible count (2–5).
6. EmbeddedView gets `hiddenTags` = the `hiddenFrom*` string for the **selected** tab.

**Params (caller overrides):**

- `tagPath`
- `hiddenFromTrend` / `hiddenFromConfiguration` / `hiddenFromAlarmConfiguration` / `hiddenFromAlarms`  
  (comma or semicolon lists; full path or provider-stripped)

**No Controls flag.** BH already added `showControls` + params — Scout pattern does not include it; BH must invent visibility rules (e.g. always show Controls, or detect CMD/OPER/KPI tags).

Utility / HotWater shells often **hardcode** tabs onStartup (`selected = 'Trend'`) without the full `tagFlags` browse (older parallel shells).

---

## 6. Visual layout (grid, cards, CSS)

### Unified Faceplate shell

- Root: **column flex** — Tabs row → Body (`classes: faceplate`).
- Tabs: flex row; each tab is `ia.input.button`; selected class `faceplate-button-selected` else `faceplate-button`.
- Body: column flex, class `faceplate`, embeds one view.
- Default size ~498×360.
- Designer style classes elsewhere: `Fonts/Label`, `Fonts/Title`, `Container/Card`, `Container/Header` (BH should map to Advanced Stylesheet equivalents).

### Stylesheet (Scout)

`com.inductiveautomation.perspective/stylesheet/stylesheet.css`:

| Class | Role |
|-------|------|
| `.psc-faceplate` | Body background `--faceplate-background` |
| `.psc-faceplate-button` | Unselected tab |
| `.psc-faceplate-button-selected` | Selected tab (taller, shadow) |
| `[class*="psc-faceplate-buttons"]` | Tab bar **CSS grid**, height 65px |
| `.psc-faceplate-buttons-2` … `-5` | `repeat(N, 1fr)` columns |

### Configuration content

- FlexRepeater column of rows; alternating `--neutral-40` / `--neutral-50`.
- No Mode/Status/KPI cards on unified Config.

### UnitControl / device-specific Config

- Column of **flex “cards”** (`Container/Card`) with header (`Container/Header Fonts/Label`) + stacked ConfigurationRows — closest Scout visual to “sections.”

### IconHeader

- Horizontal flex of small status icons (~20px), overflow visible.

---

## 7. Key file paths (ScoutMotors)

Base:  
`...\Perspective-8-3-Scout\data\projects\ScoutMotors\com.inductiveautomation.perspective\views\`

### Unified Faceplate

| Role | Path |
|------|------|
| Shell | `01_Popups/00_Faceplates/Faceplate` |
| Trend (misnamed Main) | `01_Popups/00_Faceplates/_Assets/Main` |
| Configuration (browse) | `01_Popups/00_Faceplates/Configuration/Configuration` |
| Config row | `01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow` |
| Alarm Configuration | `01_Popups/00_Faceplates/Alarm Configuration/AlarmConfiguration` |
| Alarms | `01_Popups/00_Faceplates/Alarm/Alarms` |
| Title / Pump Starts | `01_Popups/00_Faceplates/_Assets/Title` |
| Tab assets (legacy) | `01_Popups/00_Faceplates/_Assets/Tabs`, `_Assets/Tab` |

### Controls / mode / status building blocks

| Role | Path |
|------|------|
| Mode/status icons | `03_Elements/01_Status/IconHeader` |
| Icon views | `03_Elements/01_Status/Icons/{Operator,Maintenance,Hand,OutOfService,Simulate,...}` |
| Legend copy | `00_Pages/00_Docked/Legend` |
| Multi-state write UI | `03_Elements/00_Control/MultiStateInput` |
| Analog write UI | `03_Elements/00_Control/AnalogInput` |
| Boolean confirm UI (legacy) | `03_Elements/00_Control/_Assets/Boolean` |
| CSS | `...\stylesheet\stylesheet.css` (`.psc-faceplate*`) |

### Parallel / device-specific shells (still no Controls tab)

| Role | Path |
|------|------|
| Utility pumps/valves/sensors | `01_Popups/00_Faceplates/Utility/{Pumps,Valves,Sensors}` → Trend via `Utility/_Assets/Main/Main` |
| HotWater pump shell | `01_Popups/00_Faceplates/HotWater/PumpFaceplate` |
| Pump Main / Config | `HotWater/_Assets/Main/PumpMain`, `HotWater/_Assets/Configuration/PumpConfiguration` |
| Unit-level mode/PID cards | `01_Popups/00_Faceplates/HotWater/UnitControl` |
| Older Main/Config shells | `RHVAV`, `VAV`, AHU Configuration grids |

### Device graphic (CMD/STS on canvas)

`02_Components/01_Devices/Compressor` (and Pump, Fan, Valve, …) — faceplate open via `params.faceplate` + `Navigation.Faceplate.openFaceplate`.

---

## 8. Compressor-specific Faceplate controls

**Scout has no compressor-specific Faceplate Controls view.**

- Device SVG: `02_Components/01_Devices/Compressor` — same CMD/SIG + STS/FB pattern as other motors.
- Opening faceplate uses the **same unified Faceplate** (or whatever path is passed in `params.faceplate`); no `deviceType` switch.
- No Web GUI button / `webGuiUrl` in Scout Faceplates tree.
- No CP_Mode / SV_Mode / Rung / FLA faceplate Controls in Scout.

BH compressor-only Controls (`_Assets/Compressor/Controls`) and Web GUI (CONTEXT) are **net-new** relative to Scout’s Faceplate model.

---

## 9. Implications for BH redesign (`260730-m0m`)

1. **Do not expect to port a Scout Controls view** — invent Controls content; reuse Scout **shell tab-hide**, **ConfigurationRow/write**, and **IconHeader semantics** where they fit.
2. **Mode section:** Scout = read-only OPER/MAINT icons. BH Op/Prog/Maint chips need BH tag or session design; Program is not in Scout.
3. **Status/commands:** Scout puts CMD on Configuration. BH’s dedicated Start/Stop/Auto/Manual/Remote strip is new UX; wire to BH UDT commands (and/or keep CMD also on Config).
4. **KPI:** Scout does not browse KPIs on Faceplate. Prefer **deviceType fixed lists** (compressor now, pump later) or explicit params — not Scout Trend browse.
5. **Tab visibility:** Copy Scout `tagFlags` pattern; add `showControls` / `showInterlocks` with explicit rules (always-on vs tag presence).
6. **Visual:** Keep Scout tab chrome (`faceplate-button*`, `faceplate-buttons-N`); for Controls body use BH CSS (`faceplate-section`, `faceplate-mode-chip`, `faceplate-kpi-row`) + optional Scout-like **section cards** from UnitControl.
7. **Compressor Web GUI:** Scout offers no reference — BH-only param/`webGuiUrl`.

---

## Related local docs

- `.planning/quick/_scout-faceplate-trend-research.md` — Trend / `_Assets/Main` browse
- `.planning/quick/_faceplate-diag.md` — BH shell paths; notes Scout has no Controls tab
- `.planning/quick/260730-m0m-.../CONTEXT.md` — locked BH Controls/Config/Interlocks decisions
