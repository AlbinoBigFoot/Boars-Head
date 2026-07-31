# ROOT-FIX — corrected architecture (`260731-5un`)

**Date:** 2026-07-31  
**Commit message:** `fix(260731-5un): RCP1 OPC-only; _Root stays on Devices/Units`

## Corrected rule (user-confirmed)

| Layer | What belongs there |
|-------|--------------------|
| **`[default]RCP1/...`** | **OPC UA tags ONLY** — bare `AtomicTag` + `valueSource: opc` + `opcItemPath` + `dataType`. **No `typeId`, no `_Root`, no fake Folder+Value mimicking `_Root`.** Organizational `Folder`s are OK only to mirror PLC nesting (e.g. `Interlock/…`, `Fail_Timer/PRE`). |
| **`Devices/*` / `Units/*` plant instances** | **`_Root/*` and `Config/*` UDT instances.** Their `Value` (reference) points at the RCP1 OPC leaf. |

```
Devices/Units member (_Root/Digital|Analog|…)
  └── Value  (valueSource: reference)
        └── sourceTagPath → [default]RCP1/<device>/<leaf>   ← OPC AtomicTag
```

**Not:**
```
RCP1/<device>/<leaf> as _Root UdtInstance
  └── Value (opc)   ← WRONG — put _Root on Devices, not RCP1
```

## What went wrong in `76c05d8`

Commit `76c05d8` converted **143 RCP1 leaves TO `_Root`** and rewrote Units `sourceTagPath`s to `…/Value` under RCP1. That inverted the architecture: earlier frustration about missing `_Root` was about **device/unit tags**, not about instantiating `_Root` under RCP1.

## What this fix did

1. Restored RCP1 folders from pre-`76c05d8` (`7065981`) for COMP 7, HTLR-Pump 1, Main Liq SV, HSS-Pumps Pressure (flat OPC AtomicTags).
2. Flattened **HTR** Folder+Value/SP mimic into flat OPC AtomicTags (`HH`, `HH_SP`, …) — no nested Value folders.
3. Restored Units `sourceTagPath`s to `[default]RCP1/<device>/<leaf>` (not `…/Value`). HTR SP leaves use `…/HH_SP` etc.
4. Audited **Devices** UDT defs — process members already use `typeId: _Root/…` or `Config/…` (nested `Devices/VFD` under Evaporator is intentional composition).

## Examples

**RCP1 OPC leaf (COMP 7 / Alm):**

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

**Units sourceTagPath:**

```json
"sourceTagPath": "[default]RCP1/COMP 7/Alm"
```

(Device member remains `_Root/Digital` with reference `Value` → that path.)

## Verification

- RCP1 under `tag-definition/default/RCP1/`: **zero** `typeId` / `_Root` / `UdtInstance`
- Units: **zero** mistaken `…/Value` under RCP1 (except legitimate leaf named `HSS-Pumps Pressure/Value`)
- Devices: process leaves on `_Root/*` / `Config/*`
