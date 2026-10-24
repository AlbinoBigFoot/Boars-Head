---
title: Daily Rounds Fill From Live
sidebar_position: 4
description: How the Daily Rounds Log's Fill From Live Values button maps form fields to tags, what it leaves blank and how to change the mapping.
sources:
  - docs/operations-forms.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py
last_verified: 2026-10-24
---

# Daily Rounds Fill From Live

## What it does

On the **Daily Rounds Log**, **Fill From Live Values** reads the current plant values and pre-fills the matching
form fields, so the operator only checks and corrects them during the round. It is a convenience: **every field
stays editable**, nothing is submitted, and only readings with **Good** quality are filled. Fields the plant does
not measure stay blank for the operator.

User decision: rounds are field-verified readings, so the live values are a starting point, not the record.

![Daily Rounds after Fill From Live Values, dark theme](/img/features/operations-forms/daily-dark-1920-fill-live.png)

## How it works

`shared.Forms.liveValues(session)` (needs `Forms/Use`) does **one** `system.tag.readBlocking` of about 133 paths
and returns `{field: value}` for the Good ones. Paths of PLC-mapped devices are first translated with
`shared.Pax.livePath` (their values moved into nested PlantPAx members). The mapping is a table inside the
`shared.Forms` script module.

Base path: `[default]Boars_Head/GrovePort/`.

| Form field | Tag (relative to the base) |
|---|---|
| COMP 1/4/5/6/7 Suction, Discharge, FLA %, Hours, Slide Valve % | `Machine Room/Compressors/COMP n/{SucP, DisP, FLA, TotalRuntime, SVP}/Value` |
| HTR / LTR / HPR Level, PSI | `Machine Room/Tanks/{HTR,LTR,HPR}/{Level,Pressure}/Value` |
| CSV Level, PSI | `Condensers/Tanks/CSV/{Level,Pressure}/Value` |
| HTR / LTR Pump (lead pump 1 / 2) | `.../Tanks/{HTR,LTR}/Cfg_LeadPump/Value` |
| HTR / LTR Pump Hours | `Machine Room/Pumps/{HTLR,LTLR}-Pump <lead>/Val_TotRunHrs/Value` |
| CSV Pump #1-3 Status | `Condensers/Pumps/Sump Pump n`: `.Enabled` false = "Out of Service", else `Sts_Running` = Running / Idle |
| CSV Pump #1-3 Hours | `Condensers/Pumps/Sump Pump n/Val_TotRunHrs/Value` |
| Condenser 1 / 2 Fan A / B status and hours | `Condensers/Condensers/EC-1A` / `EC-1B`, `Fan 1` / `Fan 2`: `Sts_Running`, `Val_TotRunHrs` (assumed: unit 1 = EC-1A, Fan A = Fan 1) |
| Evaporator A1 ... G5 Temp | `<Area>/Utility/CG-xx/Temp/Value` (A Freezer, B SuperChill, C Club, D Palletizing, E East PH, F West PH, G Dock) |
| Evaporator Status | `CG-xx.Enabled` false = "Out of Service"; `Status/Value` 1 Cool, 2 / 6-9 Defrost, 5 Idle; 0 STOP, 3 FLT, 4 MAN = blank |
| Outside Ambient Temp | `Condensers/Sensors/Outside Air Temp/Value/Value` |

Never filled (no tag, or deliberately manual): compressor Ratio and Oil Level, the purger, Filter ΔP, Retention
Ponds, conductivity, evaporator **Suction PSIG** (a manual gauge reading by design), evaporator Unit Hours and Coil
Condition, the therm readings T1-T11 and Control Room Temp, HPR / CSV pump.

Result on 2026-10-10: 109 of 182 fields mapped, 108 filled (CSV pressure had no value). On 2026-10-23 a check
filled 84 fields (with the plant on the PLC tags, some values were not Good).

## How To Change It

1. Project Browser > Scripting > Project Library > `shared` > `Forms`. Find the live-value mapping table used by
   `liveValues` (field key -> tag path or rule) and edit the entry.
2. Fields on PLC-mapped devices resolve through `shared.Pax.livePath`; use the same path style as the neighbouring
   entries.
3. Save the project, then test: open Daily Rounds, click Fill From Live Values, compare with the device faceplates.
   The form's fields themselves match the Excel workbook and are never added or removed.

## Known limitations

- The condenser unit / fan assignment is an assumption (EC-1A = unit 1, Fan 1 = Fan A); confirm with the site.
- Values that are not Good stay blank; the info banner after the fill does not list which fields were skipped.
