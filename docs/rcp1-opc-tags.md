# RCP1 OPC UA AtomicTags (Machine Room test sources)

**Convention:** `[default]RCP1/...` holds **OPC AtomicTags only** — no `typeId`, no `_Root`,
no `UdtInstance`. Config / `_Root` UDTs stay on **Devices** and **Units**. Units
`sourceTagPath` overrides point at the OPC leaf itself (e.g. `[default]RCP1/COMP 7/Alm`),
not `…/Value` under RCP1 (except when the PLC leaf is literally named `Value`, as on Sensor).

OPC server: `Ignition OPC UA Server`  
Node id form: `ns=1;s=[RCP1]<PLC_TAG>.<member>`

No live OPC device named `RCP1` is required for the tag definitions to load; quality stays
Bad until a Logix driver exposes those node ids.

## Folders (test instances wired on `Units/Machine Room`)

| RCP1 folder | AtomicTags | OPC root | Devices type |
|-------------|------------|----------|--------------|
| `COMP 7` | 43 | `COMP[7].…` (+ `Fail_Timer.PRE`, `Interlock.…`) | Compressor |
| `HTLR-Pump 1` | 38 | `HTR_PUMPS[1].…`, `HTR_PUMPS_RUNTIME[1].…`, `HTR_PUMP1_INTLK.…` | Pump |
| `Main Liq SV` | 36 | `MAIN_LIQ_CV5.…` | Valve |
| `HTR` | 14 | `HTR.…` (bools + `*_SP` setpoints) | Tank |
| `HSS-Pumps Pressure` | 12 | `SYS_PT2.…` | Sensor |

**Total:** 143 OPC AtomicTags under `[default]RCP1/`.

Structural `Folder` nodes are used only to nest PLC-shaped paths (`Fail_Timer/PRE`,
`Interlock/*`) — children remain AtomicTags.

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

## Not wired (no invented PLC paths)

Other Machine Room instances (`COMP 1/4/5/6`, remaining pumps/valves/tanks/sensors, OPL1,
HSS-PT6, etc.) have no RCP1 OPC folders yet. Add folders only when PLC tag names are known.

## Detail

Per-device member maps: `docs/rcp1-comp7-opc-tags.md` and
`.planning/quick/260731-5un-config-interlock-udt-rcp1-udt-root-sweep/PHASE-*.md`.
