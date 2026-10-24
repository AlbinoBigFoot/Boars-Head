---
title: Screw Compressors (COMP 1 / 4 / 5 / 6 / 7)
sidebar_label: 05 Compressors
sidebar_position: 6
description: The five Machine Room screw compressors mapped to the site UDT Screw_Compressor (COMP[n], Frick Quantum data) and the P_Intlk inside it.
sources:
  - docs/pax-mapping/05-compressors.md
last_verified: 2026-10-23
---

# Screw Compressors

Source doc: `docs/pax-mapping/05-compressors.md`. Type: [Devices/Compressor](../reference/udts/devices/compressor.md);
instances: [Machine Room / Compressors](../reference/devices/machine-room-compressors.md).

The compressors are **not a PlantPAx object**. Each is the site UDT `Screw_Compressor` (`COMP[n]`), the Frick Quantum
panel data the PLC reads over Ethernet (the `QHD_*` routines), with a standard **P_Intlk** inside it
(`COMP[n].Interlock`). So the device nests two parts: `Comp` -> [PLC/Screw_Compressor](../reference/udts/plc/screw-compressor.md)
and `Intlk` -> [PLC/P_Intlk](../reference/udts/plc/p-intlk.md) (the same interlock type the pumps use).

## Devices And PLC Objects

| HMI device | `Comp` | `Intlk` | FT label |
|---|---|---|---|
| `Machine Room/Compressors/COMP 1` | `COMP[1]` | `COMP[1].Interlock` | COMP #1 |
| `Machine Room/Compressors/COMP 4` | `COMP[4]` | `COMP[4].Interlock` | COMP #4 |
| `Machine Room/Compressors/COMP 5` | `COMP[5]` | `COMP[5].Interlock` | COMP #5 |
| `Machine Room/Compressors/COMP 6` | `COMP[6]` | `COMP[6].Interlock` | COMP #6 |
| `Machine Room/Compressors/COMP 7` | `COMP[7]` | `COMP[7].Interlock` | COMP #7 |

`COMP` is `[8]` in the PLC; indexes 0, 2 and 3 are used in no routine (L5X) and have no FT display: not mapped.

![Compressor faceplate, live](/img/tags/compressor-faceplate-live.png)

## What The HMI Shows

| On the HMI | Member it reads | PLC tag (COMP 1) |
|---|---|---|
| Machine Room tile: CP mode, SV mode, FLA, SVP, run color | `Comp/CP_Mode`, `SV_Mode` (Remote / Auto / Manual), `FLA`, `SVP`, `Rung`, `Color` | `COMP[1].CP_Mode` ... |
| Status: Started, Start / Stop request, Failed, Cutout, Alarm, Comm | `Comp/Started`, `Start_Req`, `Stop_Req`, `Failed`, `Cutout`, `Alm`, `Comm` | `COMP[1].Failed` ... |
| Auto enable | `Comp/AutoEN` (a real PLC member here) | `COMP[1].AutoEN` |
| Operating values: Amps, discharge / suction / oil pressure and temperature | `Comp/Amps`, `DisP`, `DisT`, `SucP`, `SucT`, `OilP`, `OilT` | |
| Total runtime | `Comp/TotalRuntime` | |
| Configuration: minimum runtime, fail timer | `Comp/Min_Runtime_Set`, `Comp/Fail_Timer/PRE` (Leased) | `COMP[1].Fail_Timer.PRE` |
| Interlocks tab (9 named conditions with first out) | `Intlk/*` | `COMP[1].Interlock.Cfg_CondTxt[n]` ... |
| Web GUI link to the Frick panel | `Cfg_WebGuiUrl` (HMI-owned) | - |
| Trend default pens | `Comp/SucP, SucT, DisP, DisT, OilP, OilT, SVP, Rung` (FT Comp Trend) | |

<details>
<summary>Full field map (72 fields, from docs/pax-mapping/05-compressors.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): COMP 1 / COMP 4 / COMP 5 / COMP 6 / COMP 7 | Status |
|---|---|---|---|---|---|
| `Alm` | `Comp/Alm` | `COMP[1].Alm` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Amps` | `Comp/Amps` | `COMP[1].Amps` | Status | 0 / 83.1 / 0 / 0 / 0 | mapped |
| `AutoEN` | `Comp/AutoEN` | `COMP[1].AutoEN` | Status | 1 / 1 / 1 / 0 / 0 | mapped |
| `CP_Mode` | `Comp/CP_Mode` | `COMP[1].CP_Mode` | Status | 3 / 3 / 3 / 3 / 3 | mapped |
| `Cfg_WebGuiUrl` | - | - | - | - / - / - / - / - | site-only |
| `Color` | `Comp/Color` | `COMP[1].Color` | Status | 0 / 1 / 0 / 0 / 0 | mapped |
| `Comm` | `Comp/Comm` | `COMP[1].Comm` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Cutout` | `Comp/Cutout` | `COMP[1].Cutout` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `DisP` | `Comp/DisP` | `COMP[1].DisP` | Status | 33.9 / 130.5 / 35.7 / 33.3 / 34.1 | mapped |
| `DisT` | `Comp/DisT` | `COMP[1].DisT` | Status | 89.24 / 149 / 96.98 / 82.76 / 93.38 | mapped |
| `FLA` | `Comp/FLA` | `COMP[1].FLA` | Status | 0 / 35.9 / 0 / 0 / 0 | mapped |
| `Fail_Timer_PRE` | `Comp/Fail_Timer/PRE` | `COMP[1].Fail_Timer.PRE` | Faceplate | 300000 / 60000 / 60000 / 60000 / 60000 | mapped |
| `Failed` | `Comp/Failed` | `COMP[1].Failed` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Cfg_Bypassable` | `Intlk/Cfg_Bypassable` | `COMP[1].Interlock.Cfg_Bypassable` | Faceplate | 248 / 248 / 248 / 248 / 248 | mapped |
| `Interlock/Cfg_CondTxt00` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_0_` | `COMP[1].Interlock.Cfg_CondTxt[0]` | Faceplate | "Master Relay On" / "Master Relay On" / "Master Relay On" / "Master Relay On" / "Master Relay On" | mapped |
| `Interlock/Cfg_CondTxt01` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_1_` | `COMP[1].Interlock.Cfg_CondTxt[1]` | Faceplate | "HTR-HLCO Alarm" / "HTR-HLCO Alarm" / "HTR-HLCO Alarm" / "HTR-HLCO Alarm" / "HTR-HLCO Alarm" | mapped |
| `Interlock/Cfg_CondTxt02` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_2_` | `COMP[1].Interlock.Cfg_CondTxt[2]` | Faceplate | "Power Up Time" / "Power Up Time" / "Power Up Time" / "Power Up Time" / "Power Up Time" | mapped |
| `Interlock/Cfg_CondTxt03` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_3_` | `COMP[1].Interlock.Cfg_CondTxt[3]` | Faceplate | "COMP Shutdown Alarm" / "COMP Shutdown Alarm" / "COMP Shutdown Alarm" / "COMP Shutdown Alarm" / "COMP Shutdown Alarm" | mapped |
| `Interlock/Cfg_CondTxt04` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_4_` | `COMP[1].Interlock.Cfg_CondTxt[4]` | Faceplate | "COMP Comm Error" / "COMP Comm Error" / "COMP Comm Error" / "COMP Comm Error" / "COMP Comm Error" | mapped |
| `Interlock/Cfg_CondTxt05` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_5_` | `COMP[1].Interlock.Cfg_CondTxt[5]` | Faceplate | "COMP Failed" / "COMP Failed" / "COMP Failed" / "COMP Failed" / "COMP Failed" | mapped |
| `Interlock/Cfg_CondTxt06` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_6_` | `COMP[1].Interlock.Cfg_CondTxt[6]` | Faceplate | "LTR-HLCO Alarm" / "LTR-HLCO Alarm" / "LTR-HLCO Alarm" / "LTR-HLCO Alarm" / "LTR-HLCO Alarm" | mapped |
| `Interlock/Cfg_CondTxt07` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_7_` | `COMP[1].Interlock.Cfg_CondTxt[7]` | Faceplate | "COMP Anti Recycle" / "COMP Anti Recycle" / "COMP Anti Recycle" / "COMP Anti Recycle" / "COMP Anti Recycle" | mapped |
| `Interlock/Cfg_CondTxt08` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_8_` | `COMP[1].Interlock.Cfg_CondTxt[8]` | Faceplate | "COMP In Remote" / "COMP In Remote" / "COMP In Remote" / "COMP In Remote" / "COMP In Remote" | mapped |
| `Interlock/Cfg_CondTxt09` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_9_` | `COMP[1].Interlock.Cfg_CondTxt[9]` | Faceplate | "" / "" / "" / "" / "" | mapped |
| `Interlock/Cfg_CondTxt10` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_10_` | `COMP[1].Interlock.Cfg_CondTxt[10]` | Faceplate | "" / "" / "" / "" / "" | mapped |
| `Interlock/Cfg_CondTxt11` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_11_` | `COMP[1].Interlock.Cfg_CondTxt[11]` | Faceplate | "" / "" / "" / "" / "" | mapped |
| `Interlock/Cfg_CondTxt12` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_12_` | `COMP[1].Interlock.Cfg_CondTxt[12]` | Faceplate | "" / "" / "" / "" / "" | mapped |
| `Interlock/Cfg_CondTxt13` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_13_` | `COMP[1].Interlock.Cfg_CondTxt[13]` | Faceplate | "" / "" / "" / "" / "" | mapped |
| `Interlock/Cfg_CondTxt14` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_14_` | `COMP[1].Interlock.Cfg_CondTxt[14]` | Faceplate | "" / "" / "" / "" / "" | mapped |
| `Interlock/Cfg_CondTxt15` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_15_` | `COMP[1].Interlock.Cfg_CondTxt[15]` | Faceplate | "" / "" / "" / "" / "" | mapped |
| `Interlock/MSet_Bypass00` | `Intlk/MSet_Bypass00` | `COMP[1].Interlock.MSet_Bypass00` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass01` | `Intlk/MSet_Bypass01` | `COMP[1].Interlock.MSet_Bypass01` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass02` | `Intlk/MSet_Bypass02` | `COMP[1].Interlock.MSet_Bypass02` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass03` | `Intlk/MSet_Bypass03` | `COMP[1].Interlock.MSet_Bypass03` | Faceplate | 1 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass04` | `Intlk/MSet_Bypass04` | `COMP[1].Interlock.MSet_Bypass04` | Faceplate | 1 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass05` | `Intlk/MSet_Bypass05` | `COMP[1].Interlock.MSet_Bypass05` | Faceplate | 1 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass06` | `Intlk/MSet_Bypass06` | `COMP[1].Interlock.MSet_Bypass06` | Faceplate | 1 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass07` | `Intlk/MSet_Bypass07` | `COMP[1].Interlock.MSet_Bypass07` | Faceplate | 1 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass08` | `Intlk/MSet_Bypass08` | `COMP[1].Interlock.MSet_Bypass08` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass09` | `Intlk/MSet_Bypass09` | `COMP[1].Interlock.MSet_Bypass09` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass10` | `Intlk/MSet_Bypass10` | `COMP[1].Interlock.MSet_Bypass10` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass11` | `Intlk/MSet_Bypass11` | `COMP[1].Interlock.MSet_Bypass11` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass12` | `Intlk/MSet_Bypass12` | `COMP[1].Interlock.MSet_Bypass12` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass13` | `Intlk/MSet_Bypass13` | `COMP[1].Interlock.MSet_Bypass13` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass14` | `Intlk/MSet_Bypass14` | `COMP[1].Interlock.MSet_Bypass14` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/MSet_Bypass15` | `Intlk/MSet_Bypass15` | `COMP[1].Interlock.MSet_Bypass15` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/OCmd_Reset` | `Intlk/OCmd_Reset` | `COMP[1].Interlock.OCmd_Reset` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Rdy_Reset` | `Intlk/Rdy_Reset` | `COMP[1].Interlock.Rdy_Reset` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Sts_BypActive` | `Intlk/Sts_BypActive` | `COMP[1].Interlock.Sts_BypActive` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Sts_FirstOut` | `Intlk/Sts_FirstOut` | `COMP[1].Interlock.Sts_FirstOut` | Status | 256 / 256 / 32 / 256 / 256 | mapped |
| `Interlock/Sts_Intlk` | `Intlk/Sts_Intlk` | `COMP[1].Interlock.Sts_Intlk` | Status | 256 / 256 / 256 / 256 / 256 | mapped |
| `Interlock/Sts_IntlkOK` | `Intlk/Sts_IntlkOK` | `COMP[1].Interlock.Sts_IntlkOK` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Sts_NBIntlkOK` | `Intlk/Sts_NBIntlkOK` | `COMP[1].Interlock.Sts_NBIntlkOK` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Cfg_OKState` | `Intlk/Cfg_OKState` | `COMP[1].Interlock.Cfg_OKState` | Faceplate | 511 / 511 / 511 / 511 / 511 | mapped |
| `Interlock/Cfg_Latched` | `Intlk/Cfg_Latched` | `COMP[1].Interlock.Cfg_Latched` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Cfg_HasNav` | `Intlk/Cfg_HasNav` | `COMP[1].Interlock.Cfg_HasNav` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `Interlock/Cfg_Desc` | `Intlk/Cfg_Desc` | `COMP[1].Interlock.Cfg_Desc` | Faceplate | "Interlocks with First Out" / "Interlocks with First Out" / "Interlocks with First Out" / "Interlocks with First Out" / "Interlocks with First Out" | mapped |
| `Interlock/Cfg_Label` | `Intlk/Cfg_Label` | `COMP[1].Interlock.Cfg_Label` | Faceplate | "Interlocks" / "Interlocks" / "Interlocks" / "Interlocks" / "Interlocks" | mapped |
| `Interlock/Cfg_Tag` | `Intlk/Cfg_Tag` | `COMP[1].Interlock.Cfg_Tag` | Faceplate | "COMP #1" / "COMP #4" / "COMP #5" / "COMP #6" / "COMP #7" | mapped |
| `Interlock/Cfg_PCmdClear` | `Intlk/Cfg_PCmdClear` | `COMP[1].Interlock.Cfg_PCmdClear` | Faceplate | 1 / 1 / 1 / 1 / 1 | mapped |
| `Min_Runtime_Set` | `Comp/Min_Runtime_Set` | `COMP[1].Min_Runtime_Set` | Faceplate | 0 / 0 / 0 / 0 / 0 | mapped |
| `OilP` | `Comp/OilP` | `COMP[1].OilP` | Status | 33.9 / 116.4 / 33 / 34.7 / 34.1 | mapped |
| `OilT` | `Comp/OilT` | `COMP[1].OilT` | Status | 70.7 / 124.7 / 81.32 / 78.62 / 75.38 | mapped |
| `Rung` | `Comp/Rung` | `COMP[1].Rung` | Status | 0 / 1 / 0 / 0 / 0 | mapped |
| `SVP` | `Comp/SVP` | `COMP[1].SVP` | Status | 0.9 / 0 / 0 / 0 / 0 | mapped |
| `SV_Mode` | `Comp/SV_Mode` | `COMP[1].SV_Mode` | Status | 2 / 2 / 2 / 2 / 2 | mapped |
| `Start_Req` | `Comp/Start_Req` | `COMP[1].Start_Req` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Started` | `Comp/Started` | `COMP[1].Started` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `Stop_Req` | `Comp/Stop_Req` | `COMP[1].Stop_Req` | Status | 0 / 0 / 0 / 0 / 0 | mapped |
| `SucP` | `Comp/SucP` | `COMP[1].SucP` | Status | 33.8 / 34.7 / 33.8 / 34.1 / 33.9 | mapped |
| `SucT` | `Comp/SucT` | `COMP[1].SucT` | Status | 80.42 / 25.52 / 386.6 / 73.22 / 73.22 | mapped |
| `TotalRuntime` | `Comp/TotalRuntime` | `COMP[1].TotalRuntime` | Status | 4.462e+04 / 5.575e+04 / 4.982e+04 / 1.15e+04 / 9644 | mapped |

</details>

## Decisions And Evidence

1. **Interlock list kept.** FT has a real P_Intlk per compressor with named conditions and first out (photo "COMP #7 -
   Interlocks with First Out": Master Relay On, HTR-HLCO Alarm, Power Up Time, COMP Shutdown Alarm, COMP Comm Error,
   COMP Failed, LTR-HLCO Alarm, COMP Anti Recycle, COMP In Remote), so the Interlocks tab reads `Intlk/*`.
2. **Library scope.** `Screw_Compressor` keeps its 61 top-level members (no `ZZZZ*` padding) plus `Fail_Timer.PRE` /
   `.ACC`. Left out (no HMI or FT use): `AuxIntlk` (P_DOut), `Input_Data` (raw QHD data), the `Alarm` / `Commerr` /
   `Shutdown` P_Alarm blocks and the permissive timers.
3. **`AutoEN` / `Min_Runtime_Set` are PLC members on compressors** (on pumps they were HMI-only and were removed).
4. **Labels stay "COMP n"** in tag paths and HMI labels; FT prints "COMP #n". The PLC's own
   `COMP[n].Interlock.Cfg_Tag` = "COMP #n" supports a label-only rename if wanted.
5. **Tile SP coloring** against the old flat FLA / SVP setpoint sub-tags (no PLC source) was removed in the cleanup.

## Alarms

On `Comp` (library `PAX_ALARMS["Screw_Compressor"]`, same names / priorities as before): **Failed** (Critical),
**Cutout** (High), **Compressor Alarm** on `Alm` (Medium), **Comm Error** on `Comm` (Low). The P_Alarm blocks in the
PLC exist but are unconfigured (default "Alarm Condition", severity 750), so the top-level bits stay the alarm source.

## Live Check (2026-10-23)

COMP 4 running (82.7 A, 35.8 FLA, DisP 135 psig, `Color` 1); COMP 1 / 5 / 6 / 7 stopped. `CP_Mode` 3 / `SV_Mode` 2 on
all five; `AutoEN` 1 on 1 / 4 / 5, 0 on 6 / 7. `Comm` 0 on all five while communicating (consistent with
1 = comm error). `KW` reads 4.5e-38 (an uninitialised REAL): not shown.

## Open Items

- Label "COMP #n" rename (label only): awaiting a decision.
- Unbound members worth adding to Controls later: `AntiR_Remaining` (anti-recycle), `Alarm_String`, `Cutout_String`,
  `RPM`, `SepT`, `AuxT`, `VI`, `In_Sequence` (FT does not show them).
