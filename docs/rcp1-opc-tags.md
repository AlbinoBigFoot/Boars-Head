# RCP1 OPC UA AtomicTags (Machine Room test sources)

**Convention:** `[default]RCP1/...` holds **OPC AtomicTags only** — no `typeId`, no `_Root`,
no `UdtInstance`. Config / `_Root` UDTs stay on **Devices** and **Units**. Units
`sourceTagPath` overrides point at the OPC leaf itself (e.g. `[default]RCP1/COMP 7/Alm`),
not `…/Value` under RCP1 (except when the PLC leaf is literally named `Value`, as on Sensor).

OPC server: `Ignition OPC UA Server`  
Node id form: `ns=1;s=[RCP1]<PLC_TAG>.<member>`

No live OPC device named `RCP1` is required for the tag definitions to load; quality stays
Bad until a Logix driver exposes those node ids.

## Tag tree path

| Layer | Path |
|-------|------|
| Perspective Overview | `view.params.tagPath` = `[default]Plant/Machine Room/Overview` |
| Plant instance | `Plant/Machine Room/Overview` → `typeId: Units/Machine Room` |
| Units UDT | `tag-type-definition/default/Units` → `Machine Room` |
| OPC sources | `[default]RCP1/<same display name as Unit>/` |

## Folders (wired on `Units/Machine Room`)

| RCP1 folder | AtomicTags | OPC root | Devices type |
|-------------|------------|----------|--------------|
| `COMP 1` | 43 | `COMP[1].…` (+ `Fail_Timer.PRE`, `Interlock.…`) | Compressor |
| `COMP 4` | 43 | `COMP[4].…` | Compressor |
| `COMP 5` | 43 | `COMP[5].…` | Compressor |
| `COMP 6` | 43 | `COMP[6].…` | Compressor |
| `COMP 7` | 43 | `COMP[7].…` | Compressor |
| `HTLR-Pump 1` | 38 | `HTR_PUMPS[1].…`, `HTR_PUMPS_RUNTIME[1].…`, `HTR_PUMP1_INTLK.…` | Pump |
| `HTLR-Pump 2` | 38 | `HTR_PUMPS[2].…`, `HTR_PUMPS_RUNTIME[2].…`, `HTR_PUMP2_INTLK.…` | Pump |
| `LTLR-Pump 1` | 38 | `LTR_PUMPS[1].…`, `LTR_PUMPS_RUNTIME[1].…`, `LTR_PUMP1_INTLK.…` | Pump |
| `LTLR-Pump 2` | 38 | `LTR_PUMPS[2].…`, `LTR_PUMPS_RUNTIME[2].…`, `LTR_PUMP2_INTLK.…` | Pump |
| `Main Liq SV` | 36 | `MAIN_LIQ_CV5.…` | Valve |
| `HTR` | 14 | `HTR.…` (bools + `*_SP` setpoints) | Tank |
| `LTR` | 14 | `LTR.…` (mirror HTR vessel shape) | Tank |
| `HPR` | 14 | `HPR.…` (mirror HTR vessel shape) | Tank |
| `HSS-Pumps Pressure` | 12 | `SYS_PT2.…` (HSS suction) | Sensor |
| `HSL-Pumps Pressure` | 12 | `SYS_PT5.…` (HTRS / high-stage recirculator PT) | Sensor |
| `LSL-Pumps Pressure` | 12 | `SYS_PT4.…` (LTRL / low-stage recirculator PT) | Sensor |
| `LSS-Pumps Pressure` | 12 | `SYS_PT1.…` (LSS suction) | Sensor |
| `BR EF` | 5 | `BR_EEF17.…` + `BR_EEF17_FailToStart` (P_DIn sail switch) | ExhaustFan |
| `MR EF` | 5 | `MR_EEF15.…` + `MR_EEF15_FailToStart` (P_DIn sail switch) | ExhaustFan |

**Total:** 503 OPC AtomicTags under `[default]RCP1/` (+ 1 Memory control
`[default]RCP1/Simulate`).

Structural `Folder` nodes are used only to nest PLC-shaped paths (`Fail_Timer/PRE`,
`Interlock/*`) — children remain AtomicTags.

## Simulate mode

Boolean `[default]RCP1/Simulate` flips those 503 leaves between OPC and Memory for
demo. See **`docs/rcp1-simulate.md`** (tagChange script, path stash, header toggle).

## Units/Machine Room device list

| Unit name | typeId | sourceTagPaths | Notes |
|-----------|--------|----------------|-------|
| COMP 1 | Devices/Compressor | 43 | |
| COMP 4 | Devices/Compressor | 43 | |
| COMP 5 | Devices/Compressor | 43 | |
| COMP 6 | Devices/Compressor | 43 | |
| COMP 7 | Devices/Compressor | 43 | |
| HTLR-Pump 1 | Devices/Pump | 38 | AutoEN / Min_Runtime_Set not wired (no P_Motor leaf) |
| HTLR-Pump 2 | Devices/Pump | 38 | |
| LTLR-Pump 1 | Devices/Pump | 38 | |
| LTLR-Pump 2 | Devices/Pump | 38 | |
| Main Liq SV | Devices/Valve | 36 | |
| HTR | Devices/Tank | 14 | |
| LTR | Devices/Tank | 14 | |
| HPR | Devices/Tank | 14 | |
| HSS-Pumps Pressure | Devices/Sensor | 12 | |
| HSL-Pumps Pressure | Devices/Sensor | 12 | |
| LSL-Pumps Pressure | Devices/Sensor | 12 | |
| LSS-Pumps Pressure | Devices/Sensor | 12 | |
| BR EF | Devices/ExhaustFan | 5 | Partial — see below |
| MR EF | Devices/ExhaustFan | 5 | Partial — see below |
| _Alarms | Config/_Alarms | 0 | HMI rollup; not OPC |

## Example leaf

```json
{
  "name": "Alm",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[RCP1]COMP[7].Alm",
  "dataType": "Boolean"
}
```

## Unmapped / partial / Overview-only leftovers

| Item | Why |
|------|-----|
| **BR EF / MR EF** (partial) | FT `(STELLAR)MachineRoom` binds sail-switch `P_DIn` tags `BR_EEF17` / `MR_EEF15` (+ `*_FailToStart` BOOLs), not full `P_Motor`. Wired: `Started`, `Failed`, `Alm`, `Cmd_Reset`, `Status`. Unwired ExhaustFan members (`Cmd_Start/Stop`, `Interlock`, `RuntimeHours`, `OPER/MAINT/PROG`, …) have no matching PLC leaves on those tags. Full motors `MR_EEF1` / `MR_EEF2` exist in L5K but are not the overview icons. |
| **OPL1** (Overview view) | Two valve embeds hardcode `[default]Valves/MAIN-LIQ-SV` — not under `Plant/Machine Room/Overview`. Discrete PLC `HTR_OPL` / `LTR_OPL` (`P_DIn`) are not Units members. |
| **HSS-PT6** (Overview view) | Hardcoded `[default]Sensors/HSS-PT` — outside Machine Room Units tree. |
| **SYS_PT3** (HSD discharge) | Shown as caption on FT MachineRoom; not a Units/Machine Room Sensor instance. |
| **Pump AutoEN / Min_Runtime_Set** | Locked Devices members with no `P_Motor` leaf — intentionally unwired (same as HTLR-Pump 1). |

## Evidence

- L5K: `COMP[]`, `HTR_PUMPS[]` / `LTR_PUMPS[]` + runtime + `*_INTLK`, `SYS_PT1–5`, `MAIN_LIQ_CV5`, `BR_EEF17`, `MR_EEF15`
- FT: `docs/ft-display-tags/batch5.jsonl` + `Displays/(STELLAR)MachineRoom.xml`
- Prior patterns: `docs/rcp1-comp7-opc-tags.md`, phase notes under `.planning/quick/260731-5un-…/`

## Detail

Per-device member maps: `docs/rcp1-comp7-opc-tags.md` and
`.planning/quick/260731-5un-config-interlock-udt-rcp1-udt-root-sweep/PHASE-*.md`.
