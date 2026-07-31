# RESEARCH — BH Faceplate current state (redesign baseline)

**Quick id:** `260730-m0m`  
**Date:** 2026-07-30  
**Scope:** Unified Faceplate shell + Compressor Controls/Configuration + AlarmConfiguration + open params + Devices/Compressor UDT  
**Out of scope here:** Scout parity deep-dive (separate research); Trend/Alarms redesign (chrome only)

---

## 1. What exists

### 1.1 Shell — `01_Popups/00_Faceplates/Faceplate`

Shared tabbed popup (Scout-style). Default size **560×640**.

| Area | Behavior |
|------|----------|
| Header | Title from `tagPath.Metadata.shortDescription` (fallback: leaf of `tagPath`); **Web GUI** button; **Close** |
| Tabs | Controls · Configuration · Trend · Alarm Configuration · Alarms |
| Body | Single embedded view; path from `custom.selected` + `params.deviceType` |

**Params (all input):**

| Param | Default | Role |
|-------|---------|------|
| `tagPath` | `""` | Device root |
| `deviceType` | `"Compressor"` | Selects Controls/Config embed path |
| `webGuiUrl` | `""` | External GUI URL |
| `hiddenFromTrend` | `""` | Passed to Trend / AlarmConfiguration as `hiddenTags` |
| `showControls` | `true` | Tab visibility |
| `showConfiguration` | `true` | Tab visibility |
| `showTrend` | `true` | Tab visibility |
| `showAlarmConfiguration` | `true` | Tab visibility |
| `showAlarms` | `true` | Tab visibility |

**Not present:** `showInterlocks` / Interlocks tab (CONTEXT wants this; BH does not have it yet).

**Embed path map today** (`props.path` expression):

| Selected | Path |
|----------|------|
| Controls | `…/_Assets/Compressor/Controls` (any `deviceType`; only Compressor case, same fallback) |
| Configuration | `…/_Assets/Compressor/Configuration` (same) |
| Trend | `…/_Assets/Trend` |
| Alarm Configuration | `…/_Assets/AlarmConfiguration` |
| Alarms | `…/_Assets/Alarms` |

Ticket Logger context menu + `ticketLog` handler are present on shell and child assets.

### 1.2 Thin wrappers / openers

| Path | Role |
|------|------|
| `01_Popups/00_Faceplates/Compressor` | Thin embed of Faceplate; forwards `tagPath` + `webGuiUrl`; hardcodes all `show*` = true |
| `02_Components/01_Devices/Compressor` | Device graphic; on click opens Faceplate when `faceplate` ∈ `{Compressor, Faceplate}` with all `show*` true + `webGuiUrl` from param |
| `shared.Alerts.showFaceplate(...)` | Builds same params → `Navigation.Faceplate.openFaceplate` → view `…/Faceplate`, popup id `comp-fp-{tagPath\|title}` |
| `Navigation.Faceplate.openFaceplate` | Generic `openPopup`; merges params; geometry 560×640 default |

Legacy per-device faceplates (Pump, Evaporator, …) still exist under `01_Popups/00_Faceplates/` and are used from nav / Unit Overview; **Compressor path has moved to the unified shell**.

### 1.3 Controls — `_Assets/Compressor/Controls`

**Implemented (live tag reads):**

- **CP_Mode / SV_Mode** — labels Remote/Auto/Manual (1/2/3); CSS `comp-mode` + `comp-mode-{remote\|auto\|manual}` (saturated colors — ISA-101 tension)
- **Status** — embed `03_Elements/01_Status/StatusIndicator` → `{tagPath}/Status/Value`
- **KPIs** — FLA, SVP, DisP, Amps via `AnalogValue` (status path); **Rung** as text Off/Running/AntiRec/Starting

**Stub / placeholder:**

- **HMI role chips** Operator / Program / Maintenance — static labels, class `faceplate-mode-chip` only (never `faceplate-mode-active`)
- Explicit copy: *"HMI role modes (bind later) · Device CP/SV = Remote/Auto/Manual"*
- **No** start/stop / auto / manual / remote **command buttons**
- **No** runtime hours / motor starts / max run time KPIs
- **No** Web GUI control in this tab (Web GUI lives in shell header only)

### 1.4 Configuration — `_Assets/Compressor/Configuration`

**Implemented:**

- Writable SPs: `FLA/SP`, `SVP/SP`, `DisP/SP` via `03_Elements/00_Control/AnalogValue` (`setpoint: true`, gated by `!session.custom.ReadOnly`)

**Stub:**

- Dashed note (`faceplate-stub`): *"Additional UDT writables can be added here. CP_Mode / SV_Mode are shown on Controls (read-only Quantum modes)."*
- No enable/disable, no device config fields, no interlock permissive/bypass UI

### 1.5 Alarm Configuration — `_Assets/AlarmConfiguration` + `AlarmConfigurationRow`

**Real implementation** (not a stub):

- Recursive browse under `tagPath`; collect tags with configured alarms; filter noise (`_Alarms`, `SummaryInstances`) + `hiddenTags`
- FlexRepeater → row view: Priority dropdown, digital Trigger, analog SetpointA; writes via `system.tag.writeBlocking` when not ReadOnly
- Empty state uses `faceplate-stub` copy when zero alarms

### 1.6 Trend / Alarms tabs

| Tab | State |
|-----|--------|
| Trend | Functional history chart (browse historized analogs, time dropdown) — treat as recently fixed; redesign = visibility + chrome |
| Alarms | `AlarmStatusTable` filtered to device tag source — same |

### 1.7 Stylesheet — faceplate-* (Advanced Stylesheet)

Under `stylesheet.css` (~2732+):

| Class | Purpose |
|-------|---------|
| `faceplate` | Shell card chrome |
| `faceplate-header` / `faceplate-title` | Header |
| `faceplate-button` / `faceplate-button-selected` / `faceplate-tab-text` | Tab chrome (monospace 11px; selected taller + no bottom border) |
| `faceplate-buttons-1`…`5` | CSS grid column count from `visibleTabCount` |
| `faceplate-body` | Body surface |
| `faceplate-kpi-row` / `faceplate-kpi-label` | KPI layout |
| `faceplate-mode-chip` / `faceplate-mode-active` | Role chips (**active unused in views**) |
| `faceplate-section` / `faceplate-section-title` | Section headers |
| `faceplate-stub` | Dashed muted placeholder box |
| `faceplate-alarm-*` | Alarm config list/row/fields |

Related (not `faceplate-*`): `comp-mode*` uses saturated `--comp-mode-auto/manual/remote` — conflicts with HP/ISA-101 grayscale-for-normal guidance.

Adhoc-trend faceplate classes are separate product chrome; out of this redesign’s Controls/Config focus.

---

## 2. What’s stub / missing vs CONTEXT locked decisions

| CONTEXT target | BH today |
|----------------|----------|
| Controls: Mode Op/Prog/Maint + associated controls | Static chips; no binding; no commands |
| Controls: Status + start/stop, auto, manual, remote buttons | Status indicator only; no command buttons |
| Controls: KPIs runtime / starts / max run | Process KPIs only (FLA/SVP/DisP/Amps/Rung) |
| Compressors: Web GUI button | Shell header only; see §4 — effectively always hidden |
| Config: edit SPs, enable/disable, device-specific | SPs only (3 tags) |
| Config: interlock permissives/bypasses (Scout) | Absent |
| Tab: Interlocks when applicable | **No tab, no param, no asset view** |
| Hide tab if empty | Caller `show*` flags only — no data-driven empty detection |
| Professional modern look | Scaffold CSS exists; layout still sparse/stub-heavy |

---

## 3. Tab show logic today

### 3.1 Mechanism

1. Caller passes booleans (`showControls`, …).
2. Shell `custom.visibleTabCount` = sum of true flags (0–5).
3. Tabs container class = `faceplate-buttons-{N}` for equal-width grid.
4. Each tab button: `display: flex|none`, `grow` 1|0, `basis` px|0 from its `show*` flag.
5. `custom.selected` defaults to **`"Controls"`**; click sets to button `meta.name`.
6. Body embed switches on `selected` string.

### 3.2 Call sites — always all true

Every production opener hardcodes all five tabs on:

- `shared.Alerts.showFaceplate` defaults all `True`
- Device Compressor click script: all `True`
- Thin `Compressor` faceplate wrapper: all `true` in static params

**No call site** today sets a subset or derives flags from tag presence.

### 3.3 Gaps vs “hide if empty”

- No browse/exists checks before showing Configuration / Alarm Configuration / Trend / Alarms.
- No Interlocks flag at all.
- If Controls is hidden but `selected` stays `"Controls"`, body still resolves Controls embed (no auto-select first visible tab).
- `deviceType` switch is a no-op for non-Compressor (same paths) — Pump/etc. cannot yet get device-specific Controls/Config without new assets + case arms.
- Docstring in `showFaceplate` mentions paths `…/Compressor/{Controls,Configuration}` but real embeds are under `_Assets/Compressor/…`.

---

## 4. Web GUI button state

| Layer | Behavior |
|-------|----------|
| Faceplate header | `meta.visible` when `len(coalesce(webGuiUrl,'')) > 0` |
| onAction | `system.perspective.openURL(url)` |
| Param plumbing | Device graphic → Faceplate; thin Compressor wrapper → Faceplate; `showFaceplate(webGuiUrl=…)` |
| Page embeds | Machine Room / Compressors Overview & Graphic pass **only** `tagPath` + `faceplate` — **never `webGuiUrl`** |

**Verdict:** Plumbing is complete; **button is always hidden in current HMI pages** because URLs are never supplied. Redesign should decide: hardcode per-comp URLs on page embeds, Metadata/UDT field, or `_Config` map — and optionally move the CTA into Controls (CONTEXT) while keeping or dropping header button.

---

## 5. Devices/Compressor UDT — mode / status / KPI / interlock

Source: `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json` (`Devices/Compressor`).

### 5.1 Present and used by Controls/Config

| Member | Shape | UI use |
|--------|--------|--------|
| `Status` | Multistate 0–4 Off/Run/Fault/Manual/Idle | StatusIndicator |
| `FLA` | Analog Value (+ SP) | KPI + Config SP |
| `SVP` | Analog Value (+ SP) | KPI + Config SP |
| `DisP` | Analog Value (+ SP) | KPI + Config SP |
| `Amps` | Analog Value (**no SP**) | KPI only |
| `CP_Mode` | Multistate 1/2/3 Remote/Auto/Manual | Controls read-only |
| `SV_Mode` | same | Controls read-only |
| `Rung` | Multistate 0–3 | Controls text |

### 5.2 Present on UDT but unused by faceplate tabs

| Member | Notes |
|--------|--------|
| `Color` | Graphic state (Off/Running/AntiRec/Cutout/CommError) |
| `Alm`, `Cutout`, `Failed`, `Started`, `Comm` | Digitals (+ alarms on several) |
| `SummaryInstances` | Overview layout metadata + `tagsForDeviceDetails` |
| `_Alarms` | Config/_Alarms instance (AlarmConfiguration browse skips `_Alarms` folder name as noise) |

**No root `Metadata` document** on Devices/Compressor — Faceplate title binding to `{tagPath}.Metadata` will typically miss; title falls back to tag leaf (`COMP-01`, etc.).

### 5.3 Missing vs redesign / PLC

| Need | Devices/Compressor | PLC `Screw_Compressor` |
|------|--------------------|-------------------------|
| Interlocks | **Absent** | `Interlock` → `PLC/P_Intlk` (Cfg_Bypassable, Inp_Intlk##, Sts_*, OCmd_BypassAll, …) |
| Op / Prog / Maint HMI role | **Absent** | Not mirrored on HMI UDT (Scout-style; may be session/security, not PLC) |
| Start/stop / mode commands | **Absent** | Exists on PLC AOI family (not exposed on Devices/Compressor) |
| Runtime hours / starts / max run | **Absent** | Partially on other PLC types; not on HMI Compressor UDT |
| `webGuiUrl` | **Absent** (Perspective param only) | N/A |

**Implication:** Interlocks tab and richer Controls/Config require either (a) HMI UDT expansion + tag bindings from PLC, or (b) faceplate reading PLC path alongside Devices path — both are open design choices (CONTEXT assumptions).

---

## 6. Visual debt (redesign chrome checklist)

1. **Stub aesthetics dominate Controls/Config** — dashed `faceplate-stub`, hint text, inert chips; reads as WIP not operator HMI.
2. **Mode chips never activate** — `faceplate-mode-active` unused; no selected-state storytelling.
3. **Saturated CP/SV mode colors** (`comp-mode-*`) vs ISA-101 / HP HMI grayscale-for-normal + text status code.
4. **Tab bar density** — five equal columns + long label “Alarm Configuration” at 11px monospace; wrapping/`white-space: normal` looks busy at 560px.
5. **Header vs Controls CTA** — Web GUI in header (when URL set) vs CONTEXT placing it under Controls; Close + optional Web GUI + title crowding.
6. **Duplicate chrome classes** — shell uses `bg-component container-card … faceplate` plus section classes; adhoc-trend has a parallel polished card language — device faceplate feels thinner.
7. **KPI rows** — fixed 56px labels + embedded AnalogValue height hacks; uneven vs StatusIndicator block.
8. **No Interlocks visual system** yet (no row/status/bypass classes).
9. **Selected-tab / empty-tab edge cases** can show blank or wrong embed when flags change without resetting `selected`.

---

## 7. File index (absolute)

| Artifact | Path |
|----------|------|
| Shell | `C:\Users\dylan.jones\Documents\Bors\gateways\standard\data\projects\BH\com.inductiveautomation.perspective\views\01_Popups\00_Faceplates\Faceplate\view.json` |
| Controls | `…\01_Popups\00_Faceplates\_Assets\Compressor\Controls\view.json` |
| Configuration | `…\01_Popups\00_Faceplates\_Assets\Compressor\Configuration\view.json` |
| AlarmConfiguration | `…\01_Popups\00_Faceplates\_Assets\AlarmConfiguration\view.json` |
| AlarmConfigurationRow | `…\01_Popups\00_Faceplates\_Assets\AlarmConfigurationRow\view.json` |
| Styles | `…\BH\com.inductiveautomation.perspective\stylesheet\stylesheet.css` (`.psc-faceplate-*`) |
| showFaceplate | `…\BH\ignition\script-python\shared\Alerts\code.py` |
| openFaceplate | `…\BH\ignition\script-python\Navigation\Faceplate\code.py` |
| Device open | `…\02_Components\01_Devices\Compressor\view.json` |
| Devices UDT | `…\tag-type-definition\default\Devices\udts.json` (`Compressor`) |
| PLC interlock | `…\tag-type-definition\default\PLC\udts.json` (`Screw_Compressor.Interlock` → `P_Intlk`) |
| Locked decisions | `C:\Users\dylan.jones\Documents\Bors\.planning\quick\260730-m0m-faceplate-controls-config-interlocks-red\CONTEXT.md` |

---

## 8. Redesign planning takeaways

1. **Shell + flags are ready scaffolding**; content tabs for Controls/Config are mostly placeholders; Alarm Configuration / Trend / Alarms are the mature tabs.
2. **Interlocks are a greenfield BH UI** with PLC data available only under `PLC/Screw_Compressor`, not Devices HMI UDT — plan tag exposure before tab UI.
3. **Tab visibility is caller-driven, not data-driven** — implementing “hide if empty” needs new policy (static per deviceType, or runtime browse).
4. **Web GUI is wired but unused** — unblock by supplying URLs at page/device param layer (or UDT/config), and align button placement with CONTEXT (Controls section).
5. **Op/Prog/Maint vs CP/SV** must be decided: session role UI vs new tags; today only Quantum CP/SV modes are real.
6. **Visual pass** should lean on existing `faceplate-*` tokens, drop stub chrome as sections ship, and reconcile `comp-mode` saturation with HP HMI color rules.
