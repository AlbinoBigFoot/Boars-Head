# Phase — Tank (`260731-5un`)

## Done
- Trimmed **`Devices/Tank`** to PLC-backed Recirculator/Accumulator/level members (all `_Root/*` + `_Alarms`).
- **Omitted `Config/Interlock`**: plant vessels (HTR/LTR/HPR) have no `P_Intlk`; interlocks live on pumps (`HTR_PUMP*_INTLK`). Removed lightweight Interlock Folder + `SummaryInstances`.
- Created **`[default]RCP1/HTR/`** OPC tags; wired **`Units/Machine Room/HTR`** `sourceTagPath`s.
- Tank faceplate `showInterlocks=false`; Controls dropped unused Mode (OPER/MAINT/PROG) section.
- Sim: removed Tank Interlock faceplate defaults; rebuilt `bh-plant-sim.csv` / `_Sim_/Tanks`.

## Devices/Tank final members

| Member | typeId | Notes |
|--------|--------|-------|
| H | `_Root/Digital` | + nested `SP` (`_Root/Analog`, %) |
| HH | `_Root/Digital` | + nested `SP` |
| L | `_Root/Digital` | + nested `SP` |
| LL | `_Root/Digital` | + nested `SP` |
| LSH | `_Root/Digital` | HLS / HLCO |
| LSL | `_Root/Digital` | LLCO |
| Level | `_Root/Analog` | %; nested `SP` = LEVEL_SP |
| Pressure | `_Root/Analog` | psig (optional PT) |
| Status | `_Root/Multistate` | 0=OK … 5=FAULT |
| _Alarms | `Config/_Alarms` | |

No bare AtomicTags / Folders / `Config/Interlock` on Tank.

## RCP1 path

`[default]RCP1/HTR/` → OPC `ns=1;s=[RCP1]HTR.*` (Level/SP, HH|H|L|LL Value+SP, Pressure, LSH, LSL, Status)
