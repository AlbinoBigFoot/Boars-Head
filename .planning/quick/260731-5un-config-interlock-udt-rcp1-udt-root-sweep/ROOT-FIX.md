# ROOT-FIX — `260731-5un` RCP1 / Units `_Root` repair

**Date:** 2026-07-31  
**Commit message:** `fix(260731-5un): force RCP1 and device leaves onto _Root UDTs`

## What was wrong

Last night’s GSD sweep correctly put **Devices/** members on `_Root/*` / `Config/Interlock`, but **RCP1 OPC source folders** were still wrong:

1. **Bare `AtomicTag` + OPC + `dataType`** (COMP 7, HTLR-Pump 1, Main Liq SV, HSS-Pumps Pressure) — no `typeId`, no `Value` child.
2. **Fake `_Root` via `Folder` + nested `Value`/`SP` AtomicTags** (HTR) — invented the shape without `typeId: "_Root/…"`.
3. **`Interlock` as Folder of AtomicTags** instead of `Config/Interlock` with `_Root` children.
4. **Units `sourceTagPath`s** pointed at those bare leaves (e.g. `[default]RCP1/COMP 7/Alm`) instead of `…/Alm/Value`.

Agents kept doing this because the COMP 7 doc described RCP1 as “OPC AtomicTags for reference Values,” so subagents treated flat OPC leaves as the pattern — skipping the project rule that process leaves are `_Root` instances with OPC on `Value`.

## Before → after (examples)

**COMP 7 / Alm**

```json
// BEFORE
{ "name": "Alm", "tagType": "AtomicTag", "valueSource": "opc", "dataType": "Boolean", ... }

// AFTER
{
  "name": "Alm",
  "typeId": "_Root/Digital",
  "tagType": "UdtInstance",
  "tags": [{ "name": "Value", "tagType": "AtomicTag", "valueSource": "opc", ... }]
}
```

Units: `[default]RCP1/COMP 7/Alm` → `[default]RCP1/COMP 7/Alm/Value`

**HTR / HH**

```json
// BEFORE
{ "name": "HH", "tagType": "Folder", "tags": [ AtomicTag Value, AtomicTag SP ] }

// AFTER
{
  "name": "HH",
  "typeId": "_Root/Digital",
  "tagType": "UdtInstance",
  "tags": [
    { "name": "Value", "valueSource": "opc", ... },
    { "name": "SP", "typeId": "_Root/Analog", "tagType": "UdtInstance", "tags": [ OPC Value ] }
  ]
}
```

## What was fixed

| Folder | Converted |
|--------|-----------|
| `RCP1/COMP 7` | 43 Atomic → `_Root` (+ Interlock → `Config/Interlock`; Fail_Timer/PRE → `_Root/Analog`) |
| `RCP1/HTLR-Pump 1` | 38 |
| `RCP1/Main Liq SV` | 36 |
| `RCP1/HTR` | 9 Atomic + 5 Folder→`_Root` |
| `RCP1/HSS-Pumps Pressure` | 12 |
| **Total leaves** | **143** |
| Units `sourceTagPath` updates | **138** (5 HTR `…/Value` paths already correct) |

`Devices/*` typeDefs were already `_Root` / `Config/*` — no type change. Faceplate/sim paths unchanged (Devices member names/`…/Value` unchanged).

## Tooling

- Script: `_fix_rcp1_root.py` (this folder)
- Scan: POST `scan/config` after edit
