---
title: HLCO Safety Relay (440C-CR30)
sidebar_label: 12 Safety Relay
sidebar_position: 13
description: The HLCO safety relay mapped to the module input assembly SafetyRelay:I (site library type CR30_Input) and two controller BOOLs.
sources:
  - docs/pax-mapping/12-safety-relay.md
last_verified: 2026-10-23
---

# HLCO Safety Relay (440C-CR30)

Source doc: `docs/pax-mapping/12-safety-relay.md`. Type: [Devices/SafetyRelay](../reference/udts/devices/safetyrelay.md);
instance `Machine Room/SafetyRelays/HLCO Safety Relay` ([page](../reference/devices/machine-room-safetyrelays.md)); page
`/safety-relay`.

| Part / member | PLC tag | What |
|---|---|---|
| `IO` -> [PLC/CR30_Input](../reference/udts/plc/cr30-input.md) | `SafetyRelay:I` (module-defined input assembly) | `Pt00..09Data` inputs, `Pt18..21Data` outputs, `Plugin2In/OutPt00..03Data` (2080-IQ4OB4 plug-in), `SOF01/02ResetRequired`, `SOF05`, `SOF06`, `RunMode`, `ConnectionFaulted`, `MajorFault`, `MajorFaultCode` / `Type`, `MinorFault` |
| `PlcMajorFault` | `SafetyRelay_MajorFault` (BOOL) | FT "CR30 Fault LED" |
| `PlcResetAlm` | `SafetyRelay_ResetAlm` (BOOL) | not shown on FT |

The input assembly is not a UDT in the L5K, so the project uses **site library types for module tags**:
`CR30_Input` was built from the browsed `SafetyRelay:I` members the HMI / FT use, with the library rules (read only,
`ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, PAX tag groups).

![Safety relay page, live](/img/tags/safety-relay-page.png)

<details>
<summary>Full field map (32 fields, from docs/pax-mapping/12-safety-relay.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): HLCO Safety Relay | Status |
|---|---|---|---|---|---|
| `ConnectionFaulted` | `IO/ConnectionFaulted` | `SafetyRelay:I.ConnectionFaulted` | Status | 0 | mapped |
| `MajorFault` | `PlcMajorFault` | `SafetyRelay_MajorFault` | Status (atomic) | 0 | mapped |
| `MajorFaultCode` | `IO/MajorFaultCode` | `SafetyRelay:I.MajorFaultCode` | Status | 0 | mapped |
| `MajorFaultType` | `IO/MajorFaultType` | `SafetyRelay:I.MajorFaultType` | Status | 0 | mapped |
| `Plugin2InPt00Data` | `IO/Plugin2InPt00Data` | `SafetyRelay:I.Plugin2InPt00Data` | Status | 0 | mapped |
| `Plugin2InPt01Data` | `IO/Plugin2InPt01Data` | `SafetyRelay:I.Plugin2InPt01Data` | Status | 0 | mapped |
| `Plugin2InPt02Data` | `IO/Plugin2InPt02Data` | `SafetyRelay:I.Plugin2InPt02Data` | Status | 0 | mapped |
| `Plugin2InPt03Data` | `IO/Plugin2InPt03Data` | `SafetyRelay:I.Plugin2InPt03Data` | Status | 0 | mapped |
| `Plugin2OutPt00Data` | `IO/Plugin2OutPt00Data` | `SafetyRelay:I.Plugin2OutPt00Data` | Status | 0 | mapped |
| `Plugin2OutPt01Data` | `IO/Plugin2OutPt01Data` | `SafetyRelay:I.Plugin2OutPt01Data` | Status | 0 | mapped |
| `Plugin2OutPt02Data` | `IO/Plugin2OutPt02Data` | `SafetyRelay:I.Plugin2OutPt02Data` | Status | 0 | mapped |
| `Plugin2OutPt03Data` | `IO/Plugin2OutPt03Data` | `SafetyRelay:I.Plugin2OutPt03Data` | Status | 0 | mapped |
| `Pt00Data` | `IO/Pt00Data` | `SafetyRelay:I.Pt00Data` | Status | 1 | mapped |
| `Pt01Data` | `IO/Pt01Data` | `SafetyRelay:I.Pt01Data` | Status | 1 | mapped |
| `Pt02Data` | `IO/Pt02Data` | `SafetyRelay:I.Pt02Data` | Status | 0 | mapped |
| `Pt03Data` | `IO/Pt03Data` | `SafetyRelay:I.Pt03Data` | Status | 0 | mapped |
| `Pt04Data` | `IO/Pt04Data` | `SafetyRelay:I.Pt04Data` | Status | 0 | mapped |
| `Pt05Data` | `IO/Pt05Data` | `SafetyRelay:I.Pt05Data` | Status | 0 | mapped |
| `Pt06Data` | `IO/Pt06Data` | `SafetyRelay:I.Pt06Data` | Status | 0 | mapped |
| `Pt07Data` | `IO/Pt07Data` | `SafetyRelay:I.Pt07Data` | Status | 0 | mapped |
| `Pt08Data` | `IO/Pt08Data` | `SafetyRelay:I.Pt08Data` | Status | 0 | mapped |
| `Pt09Data` | `IO/Pt09Data` | `SafetyRelay:I.Pt09Data` | Status | 0 | mapped |
| `Pt18Data` | `IO/Pt18Data` | `SafetyRelay:I.Pt18Data` | Status | 1 | mapped |
| `Pt19Data` | `IO/Pt19Data` | `SafetyRelay:I.Pt19Data` | Status | 1 | mapped |
| `Pt20Data` | `IO/Pt20Data` | `SafetyRelay:I.Pt20Data` | Status | 0 | mapped |
| `Pt21Data` | `IO/Pt21Data` | `SafetyRelay:I.Pt21Data` | Status | 0 | mapped |
| `ResetAlm` | `PlcResetAlm` | `SafetyRelay_ResetAlm` | Status (atomic) | 0 | mapped |
| `RunMode` | `IO/RunMode` | `SafetyRelay:I.RunMode` | Status | 1 | mapped |
| `SOF01ResetRequired` | `IO/SOF01ResetRequired` | `SafetyRelay:I.SOF01ResetRequired` | Status | 0 | mapped |
| `SOF02ResetRequired` | `IO/SOF02ResetRequired` | `SafetyRelay:I.SOF02ResetRequired` | Status | 0 | mapped |
| `SOF05` | `IO/SOF05` | `SafetyRelay:I.SOF05` | Status | 0 | mapped |
| `SOF06` | `IO/SOF06` | `SafetyRelay:I.SOF06` | Status | 0 | mapped |

</details>

## Alarms

On `IO` (library): **Safety Relay Major Fault** (High, the module's own `MajorFault` bit), **Safety Relay Comm Loss**
(High, `ConnectionFaulted`), **LSS HLCO Output 0 Reset Required** and **HSS HLCO Output 1 Reset Required** (Medium,
`SOF01/02ResetRequired`). FT's `SafetyRelay_MajorFault` BOOL is read as `PlcMajorFault` for the LED (no alarm).

## Live Check (2026-10-23)

`Pt00Data` / `Pt01Data` = 1 (Input 0 LSS HLCO, Input 1 HSS HLCO), `Pt18Data` / `Pt19Data` = 1 (outputs 0 / 1), all
other points 0, `RunMode` 1, `ConnectionFaulted` 0: matches the FT HLCO Safety Relay photo. The two major-fault
sources agree (both 0).
