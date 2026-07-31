# Phase — Sensor (`260731-5un`)

## Done
- Trimmed **`Devices/Sensor`** to PLC `P_AIn`-backed members only (all `_Root/*` or `Config/_Alarms`).
- Removed **`SummaryInstances`** (not PLC).
- **`Status`** Multistate states aligned to **`P_AIn.Val_Fault`**: 0=OK, 20=LO, 21=HI, 24=LOLO, 25=HIHI, 32=FAIL, 34=CFGERR.
- No `Config/Interlock` (P_AIn has no P_Intlk).
- Created **`RCP1/HSS-Pumps Pressure/`** OPC tags → PLC `SYS_PT2` (Machine Room HSS suction PT).
- Wired **`Units/Machine Room/HSS-Pumps Pressure`** `…/Value` `sourceTagPath`s to RCP1.
- Sensor Controls bindings unchanged (member names kept).
- Sim `SENSOR_PROFILES` Status values updated to Val_Fault enums; CSV regen.

## Devices/Sensor final members

| Member | typeId | PLC source |
|--------|--------|------------|
| Cmd_Reset | `_Root/Digital` | OCmd_Reset |
| Fail | `_Root/Digital` | Sts_Fail |
| Hi | `_Root/Digital` | Sts_Hi |
| HiHi | `_Root/Digital` | Sts_HiHi |
| HiHiLim | `_Root/Analog` | Val_HiHiLim |
| HiLim | `_Root/Analog` | Val_HiLim |
| Lo | `_Root/Digital` | Sts_Lo |
| LoLim | `_Root/Analog` | Val_LoLim |
| LoLo | `_Root/Digital` | Sts_LoLo |
| LoLoLim | `_Root/Analog` | Val_LoLoLim |
| Status | `_Root/Multistate` | Val_Fault |
| Value | `_Root/Analog` | Val |
| _Alarms | `Config/_Alarms` | HMI rollup |

## RCP1 path

| Layer | Path |
|-------|------|
| Ignition | `[default]RCP1/HSS-Pumps Pressure/<member>` |
| OPC item | `ns=1;s=[RCP1]SYS_PT2.<plc leaf>` |
| Units instance | `Units/Machine Room/HSS-Pumps Pressure` |

P_DIn discrete sensors not modeled on this type (P_AIn pressure transmitters only).
