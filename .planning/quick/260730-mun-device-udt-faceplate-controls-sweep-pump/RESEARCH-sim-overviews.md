# RESEARCH — Demo tags, Overview pages, faceplate open wiring

**Quick id:** `260730-mun`  
**Date:** 2026-07-30  
**Workspace:** `C:\Users\dylan.jones\Documents\Bors`  
**Sources:** `sim/bh-plant-sim.csv`, `sim/build_plant_sim.py`, `tag-definition/default/{Compressors,Pumps,Valves,Tanks,Sensors,ExhaustFans,Evaporators,CoolingTowers}`, `00_Pages/*/Overview`, `02_Components/01_Devices/*`, `01_Popups/00_Faceplates/*`, `tag-type-definition/default/{Devices,PLC}`, `docs/ft-display-tags/*`  
**Companion:** `RESEARCH-faceplate-controls-ext.md` (shell / Controls extension)

---

## Verdict

All eight device families have Overview pages + page-config routes. **Compressors** are the only family with Controls-grade UDT leaves, sim coverage (~68 leaves/device including Interlock), and unified Faceplate open (`deviceType='Compressor'`). **Pumps / ExhaustFans / CoolingTowers / Evaporators** have working Overview walls and sim Status(+Temp) demos, but open **legacy** faceplates (`tagPath` only) and lack Controls/Config/Interlock leaves. **Valves / Sensors** Overviews are **broken vs live tags** (point at SV-*/SNS-* that do not exist). **Valves / Tanks / Sensors** are **absent from plant sim** (`build_plant_sim.FOLDERS` omits them). Devices UDTs for non-Compressor types are too lean for a Controls tab demo without expansion.

---

## 1. Tag instances per folder

Top-level `UdtInstance` names from `tag-definition/default/<Folder>/udts.json` (excluding nested member instances). `Overview` rows are Overview UDT helpers, not devices.

| Folder | Device instances | typeId | Notes |
|--------|------------------|--------|-------|
| **Compressors** | COMP-01…COMP-05 | `Devices/Compressor` | + `Overview` (`Overview/Compressor Overview`) |
| **Pumps** | PMP-01…PMP-04 | `Devices/Pump` | + `Overview` |
| **ExhaustFans** | EFAN-01…EFAN-04 | `Devices/ExhaustFan` | + `Overview` |
| **CoolingTowers** | CT-01…CT-04 | `Devices/CoolingTower` | + `Overview` |
| **Evaporators** | EV-01…EV-17 | `Devices/Evaporator` | + `Overview`; **EV-17** not on Overview wall |
| **Valves** | HPRL-ISO, LTR-SV, MAIN-LIQ-SV, HTR-SV | `Devices/Valve` | Plant names; **no SV-*/SV3-*** |
| **Tanks** | LTR, HPR, HTR, LTR-01…LTR-04 | `Devices/Tank` | Plant vessels + LTR wall demos |
| **Sensors** | LSS-PT, HSS-PT, HPR-PT, OIL-TT | `Devices/Sensor` | Plant transmitters; **no SNS-*** |

`Devices` UDT types present: Pump, Compressor, VFD, Evaporator, ExhaustFan, CoolingTower, Tank, Valve, Sensor.  
`PLC` types relevant to Controls sweep: `P_Motor`, `P_ValveSO`, `P_AIn`, `P_DIn`, `P_DOut`, `P_Mode`, `P_Intlk`, `P_Alarm`, `P_RunTime`, `Screw_Compressor`, `CG_RL_Evap`, `Recirculator`, etc. (see `_focused_udt_extract.md` / `_curated_members.md`).

---

## 2. Overview pages — existence vs content

| Family | Overview view | page-config | Graphic | Wall tagPaths | Match live instances? |
|--------|---------------|-------------|---------|---------------|------------------------|
| Compressors | ✅ | ✅ `/…` Compressors | ✅ | COMP-01…05 | ✅ |
| Pumps | ✅ | ✅ | ✅ | PMP-01…04 | ✅ |
| ExhaustFans | ✅ | ✅ | ✅ | EFAN-01…04 | ✅ |
| CoolingTowers | ✅ | ✅ | ✅ | CT-01…04 | ✅ |
| Evaporators | ✅ | ✅ | ✅ | EV-01…16 | ⚠️ EV-17 tagged+sim’d, not on wall |
| Valves | ✅ | ✅ | ❌ | SV-01…03, SV3-01…03 | ❌ **no such tags** |
| Tanks | ✅ | ✅ | ❌ | LTR-01…04 | ✅ wall only; plant HTR/HPR/LTR on Machine Room |
| Sensors | ✅ | ✅ | ❌ | SNS-01…04 | ❌ **no such tags** |

**“Missing Overviews” clarification:** no family lacks an Overview *file*. Gaps are (a) **wrong/demo-only tagPaths** (Valves, Sensors), (b) **no Graphic** for Valves/Tanks/Sensors, (c) **plant instances not mirrored** on Valves/Sensors walls, (d) EV-17 omitted from Evaporators wall.

Machine Room Overview embeds plant mix: Tanks HTR/HPR/LTR, Pumps PMP-01/02, Compressors COMP-01…05, Valves MAIN-LIQ-SV, Sensors HSS-PT — useful for plant tags, not a device-family status wall.

---

## 3. Faceplate open wiring (`faceplate` → `deviceType`)

### 3.1 Overview → device graphic

Every family Overview embeds `02_Components/01_Devices/<Component>` with params:

| Overview | `path` | `params.faceplate` | `params.tagPath` |
|----------|--------|--------------------|------------------|
| Compressors | `…/Compressor` | `Compressor` | `[default]Compressors/COMP-##` |
| Pumps | `…/Pump` | `Pump` | `…/PMP-##` |
| ExhaustFans | `…/ExhaustFan` | `ExhaustFan` | `…/EFAN-##` |
| CoolingTowers | `…/CoolingTower` | `CoolingTower` | `…/CT-##` |
| Evaporators | `…/Evaporator` | `Evaporator` | `…/EV-##` |
| Valves | `…/SolenoidValve` / `SolenoidValve3Way` | same | **SV-*/SV3-*** (broken) |
| Tanks | `…/Tank` | `Tank` | `…/LTR-##` |
| Sensors | `…/Sensor` | `Sensor` | **SNS-*** (broken) |

Overviews do **not** pass `deviceType`; that is resolved (or not) inside the device component click handler.

### 3.2 Device component click → popup

| Component | Open path | Passes `deviceType`? |
|-----------|-----------|----------------------|
| **Compressor** | Unified: `01_Popups/00_Faceplates/Faceplate` via `Navigation.Faceplate.openFaceplate(…, params={tagPath, deviceType:'Compressor', webGuiUrl, show*})` when `faceplate in ('Compressor','Faceplate')` | ✅ |
| Pump, ExhaustFan, CoolingTower, Evaporator(+Dual/Triple), Tank, Sensor, SolenoidValve, SolenoidValve3Way | **Legacy:** `system.perspective.openPopup` → `01_Popups/00_Faceplates/<faceplate>` with `{tagPath}` only | ❌ |

Unit Overview table has a small faceplate map (Evaporators/CoolingTowers/Compressors/Pumps/ExhaustFans → legacy Faceplate views); Valves/Tanks/Sensors absent from that map.

### 3.3 Unified shell Controls gate

`Faceplate` `tagFlags` / Controls embed:

- `hasControlsAsset = deviceType in ('Compressor', '')`
- Controls body path: `case(deviceType, "Compressor" → _Assets/Compressor/Controls, default → same)`
- Web GUI header: `deviceType = 'Compressor' && webGuiUrl nonempty`

Legacy popups (`Pump`, `Evaporator`, …) are simple Status/Temp cards — **no Controls tab**.

**Sweep implication:** migrate non-Compressor openers to unified Faceplate + `deviceType`, add `_Assets/{Device}/Controls`, expand `hasControlsAsset` + `case()`.

---

## 4. Sim coverage (`sim/bh-plant-sim.csv` + `build_plant_sim.py`)

### 4.1 Builder scope

```text
FOLDERS = ["Evaporators", "Compressors", "Pumps", "ExhaustFans", "CoolingTowers"]
```

**Not simulated:** Valves, Tanks, Sensors (and any future VFD instances).

OPC wiring: Value leaves under those folders → `[default]_Sim_/<BrowsePath>`.

### 4.2 CSV leaf counts (per device)

| Family | Devices in CSV | Leaves / device | Content |
|--------|----------------|-----------------|---------|
| Compressors | COMP-01…05 | **68** | Status wall + DisP/Amps/FLA/SVP/modes/bools + **full Controls/Config/Interlock** faceplate defaults |
| Evaporators | EV-01…17 | **6** | Status, Temp, Pressure, Fan 1 CMD/Fault/SPD_FBK (profiles keyed by leaf parent) |
| CoolingTowers | CT-01…04 | **3** | Status, Temp, SPD_FBK |
| Pumps | PMP-01…04 | **2** | Status, Temp |
| ExhaustFans | EFAN-01…04 | **2** | Status, Temp |
| Valves / Tanks / Sensors | — | **0** | not in CSV |

### 4.3 Status-wall demo profiles (intentional)

| Family | Demo intent (from builder comments) |
|--------|-------------------------------------|
| Evaporators | Comm Loss EV-01 (tag `enabled=false`); Cooling+over-SP EV-02; Idle/Off/Fault; Defrost stages 6–9 on EV-04/09/14/16 |
| CT / PMP / EFAN | Run / Idle / Fault / Off; over-SP red on *-01 |
| Compressors | Run/Idle/Fault/Off/Manual; FLA/SVP over-SP; CP/SV modes; Interlock text on COMP-01 |

### 4.4 Sim gaps vs Controls sweep

| Gap | Impact |
|-----|--------|
| No Valves/Tanks/Sensors in FOLDERS | Cannot demo Controls/Interlocks on those Overviews without extending builder + UDT leaves |
| Pump/EFAN/CT only Status(+Temp[/SPD]) | Even after unified Faceplate, Interlocks/Config tabs stay empty until UDT + sim leaves exist |
| Evaporator sim has no Cmd_*/OPER/Interlock | Same |
| Only Compressor has `COMP_FACEPLATE_DEFAULTS` | Pattern to copy for other types once Devices UDT expanded |
| Overview Valves/Sensors tagPaths ≠ instances | Fix tagPaths (or create demo SV/SNS UDTs) before sim wiring helps |

---

## 5. Devices UDT lean-ness (why Controls can’t light up yet)

Shallow members of `tag-type-definition/default/Devices/udts.json`:

| Devices type | Process / status | Controls-grade leaves today |
|--------------|------------------|-----------------------------|
| **Compressor** | Status, DisP, Amps, FLA, SVP, CP/SV Mode, Rung, Color, Alm… | OPER/MAINT/PROG, Cmd_*, RuntimeHours, MotorStarts, timers, **Interlock/** folder |
| Pump | Status, Temp | ❌ none |
| ExhaustFan | Status, Temp | ❌ none |
| CoolingTower | Status, Temp, SPD_FBK | ❌ none |
| Evaporator | Fans, Pressure, Status, Temp | ❌ none (fan CMD/Fault only) |
| Valve | Status, Temp | ❌ none |
| Tank | Status, Level, LSH/LSL, HH/H/L/LL | ❌ none |
| Sensor | Value, Status | ❌ none |

PLC `P_Motor` / `P_ValveSO` / `P_AIn` / `P_Intlk` remain the catalog for expanding Devices UDTs (see curated research).

---

## 6. Other CSV / FT display sources

| Path | Role for this sweep |
|------|---------------------|
| `sim/bh-plant-sim.csv` | **Only** plant Programmable Device Simulator CSV |
| `gateways/.../opcua/device/Sim/instructions.csv` | Simulator device instructions (generated/wiring), not FT tags |
| `Displays/*.xml` | FT ViewME displays — **no `.csv` under Displays/** |
| `docs/ft-display-tags/FT_Display_Tag_Map.xlsx` + `batch1–5.jsonl` | Parsed FT faceplate tag map (RA-BAS `P_Motor`, `P_ValveSO`, … → BH component hints). Use for Controls leaf selection; **not** wired into BH sim |

---

## 7. Gap matrix (action-oriented)

| Type | Instances OK | Overview wall | Unified open + `deviceType` | Controls asset | Sim Controls leaves |
|------|--------------|---------------|-----------------------------|----------------|---------------------|
| Compressor | ✅ 5 | ✅ | ✅ | ✅ `_Assets/Compressor/Controls` | ✅ |
| Pump | ✅ 4 | ✅ | ❌ legacy | ❌ | ❌ (2 leaves) |
| ExhaustFan | ✅ 4 | ✅ | ❌ | ❌ | ❌ |
| CoolingTower | ✅ 4 | ✅ | ❌ | ❌ | ❌ |
| Evaporator | ✅ 17 | ⚠️ 16 of 17 | ❌ | ❌ | ❌ (status only) |
| Valve | ✅ 4 plant | ❌ wrong SV-* | ❌ (+ wrong paths) | ❌ | ❌ not in sim |
| Tank | ✅ 7 | ✅ LTR wall | ❌ | ❌ | ❌ not in sim |
| Sensor | ✅ 4 plant | ❌ wrong SNS-* | ❌ | ❌ | ❌ not in sim |

---

## 8. Recommended order for mun sweep (Overviews + sim angle)

1. **Fix Valves / Sensors Overview tagPaths** to real instances (or add dedicated demo UDTs SV-/SNS- if orientation wall must stay).
2. **Expand Devices UDTs** (Pump first per quick id) with Controls/Interlock leaves aligned to PLC/FT research; keep `_Root` metadata/engUnits.
3. **Extend `build_plant_sim.FOLDERS` + profiles** for Valves/Tanks/Sensors and Controls leaves on Pump/EFAN/CT/EV; regenerate CSV + `_Sim_` wiring.
4. **Migrate device openers** to `Faceplate` + `deviceType`; add `_Assets/{Device}/Controls`; widen `hasControlsAsset`.
5. Optionally add EV-17 to Evaporators Overview; plant Valves/Sensors tiles or Machine Room-only docs.
6. Pushover: Controls tab screenshots per deviceType once (2)–(4) land.

---

## 9. File index (quick)

| Artifact | Path |
|----------|------|
| Sim CSV | `sim/bh-plant-sim.csv` |
| Sim builder | `sim/build_plant_sim.py` |
| Tag instances | `gateways/standard/data/config/resources/core/ignition/tag-definition/default/<Folder>/udts.json` |
| Devices / PLC types | `…/tag-type-definition/default/{Devices,PLC}/udts.json` |
| Overviews | `…/projects/BH/…/views/00_Pages/{Family}/Overview/view.json` |
| Device graphics | `…/views/02_Components/01_Devices/<Name>/view.json` |
| Unified shell | `…/views/01_Popups/00_Faceplates/Faceplate/view.json` |
| Compressor Controls | `…/00_Faceplates/_Assets/Compressor/Controls/view.json` |
| FT tag map | `docs/ft-display-tags/` |
