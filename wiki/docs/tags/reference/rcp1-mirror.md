---
title: "_RCP1_ Mirror (Generated)"
sidebar_label: "_RCP1_ Mirror"
description: "Counts and objects of the pruned, read-only browse mirror [default]_RCP1_ of the RCP1 PLC."
generated: true
---

:::note

:::
`[default]_RCP1_` is a browse of the production controller `[RCP1]`, pruned to the PlantPAx members the HMI and FactoryTalk use, with every tag `readOnly`. The HMI reads the PLC through the device UDTs, not through this folder (exceptions: the SAFETYS `Digitals` references). It is git-ignored, so it exists only on this gateway. Background: [PAX Mapping](../pax-mapping/index.md), [PLC Write Lock](../plc-write-lock.md).

| Check | Result |
|---|---|
| Atomic tags | 35056 |
| Read only | 35056 of 35056 |
| Tags carrying a `value` key (must be 0) | 0 |
| Distinct OPC items | 35056 |

### By top folder

| Top folder | Tags |
|---|---|
| `Controller:Global` | 34627 |
| `Program:CompSeq_LSS` | 262 |
| `Program:Quantum_ENET_Comms` | 139 |
| `_Diagnostics_` | 25 |
| `Program:RCP_Alarm_Circuit` | 2 |
| `Program:System_Clock_Timers` | 1 |

### By tag group

| Tag group | Tags |
|---|---|
| `RCP1_Status` | 17947 |
| `RCP1_Faceplate` | 17109 |

### By data type

| Data type | Tags |
|---|---|
| `Boolean` | 25717 |
| `String` | 2716 |
| `Float4` | 1916 |
| `Int1` | 1838 |
| `Int4` | 1469 |
| `Int2` | 1384 |
| `Float8` | 10 |
| `Int8` | 6 |

### By value source

| Value source | Tags |
|---|---|
| `opc` | 35056 |

## Objects

One row per controller object (array or single tag) in the mirror, with the device instances whose parts read it.

| Folder | Object | Tags | Read by device instances |
|---|---|---|---|
| `Controller:Global` | `AD` | 416 | Club/Detectors/AD03, Dock/Detectors/AD07, Dock/Detectors/AD08, East PH/Detectors/AD05, Freezer/Detectors/AD01, Palletizing/Detectors/AD04 +2 |
| `Controller:Global` | `AD_MR1` | 52 | Machine Room/Detectors/MR-AD1 |
| `Controller:Global` | `AD_VL` | 52 | Machine Room/Detectors/VL-AD |
| `Controller:Global` | `ALARM` | 12 | Machine Room/Digitals/Alarm Reset, Machine Room/Digitals/Alarm Silence |
| `Controller:Global` | `Alarm_Circuit` | 139 | Machine Room/Digitals/Alarm Circuit |
| `Controller:Global` | `Alarm_Light` | 139 | Machine Room/Digitals/Alarm Light |
| `Controller:Global` | `Alarm_Reset_DO` | 139 | |
| `Controller:Global` | `Alarm_Reset_Relay` | 139 | |
| `Controller:Global` | `BR_EEF17` | 52 | Machine Room/ExhaustFans/BR EF |
| `Controller:Global` | `BR_EEF17_FailToStart` | 1 | Machine Room/ExhaustFans/BR EF |
| `Controller:Global` | `CD1A_FAN1` | 108 | Condensers/Condensers/EC-1A/Fan 1 |
| `Controller:Global` | `CD1A_FAN1_Runtime` | 11 | Condensers/Condensers/EC-1A/Fan 1 |
| `Controller:Global` | `CD1A_FAN2` | 108 | Condensers/Condensers/EC-1A/Fan 2 |
| `Controller:Global` | `CD1A_FAN2_Runtime` | 11 | Condensers/Condensers/EC-1A/Fan 2 |
| `Controller:Global` | `CD1B_FAN1` | 108 | Condensers/Condensers/EC-1B/Fan 1 |
| `Controller:Global` | `CD1B_FAN1_Runtime` | 11 | Condensers/Condensers/EC-1B/Fan 1 |
| `Controller:Global` | `CD1B_FAN2` | 108 | Condensers/Condensers/EC-1B/Fan 2 |
| `Controller:Global` | `CD1B_FAN2_Runtime` | 11 | Condensers/Condensers/EC-1B/Fan 2 |
| `Controller:Global` | `CD1_P1` | 108 | Condensers/Pumps/Sump Pump 1 |
| `Controller:Global` | `CD1_P1_Runtime` | 11 | Condensers/Pumps/Sump Pump 1 |
| `Controller:Global` | `CD1_P2` | 108 | Condensers/Pumps/Sump Pump 2 |
| `Controller:Global` | `CD1_P2_Runtime` | 11 | Condensers/Pumps/Sump Pump 2 |
| `Controller:Global` | `CD1_P3` | 108 | Condensers/Pumps/Sump Pump 3 |
| `Controller:Global` | `CD1_P3_Runtime` | 11 | Condensers/Pumps/Sump Pump 3 |
| `Controller:Global` | `CD_SUMP_OPL1H_SET` | 1 | Condensers/Sequences/HSD |
| `Controller:Global` | `CD_SUMP_OPL1L_SET` | 1 | Condensers/Sequences/HSD |
| `Controller:Global` | `CD_SUMP_OPLH_SET` | 1 | Condensers/Sequences/HSD |
| `Controller:Global` | `CD_SUMP_OPLL_SET` | 1 | Condensers/Sequences/HSD |
| `Controller:Global` | `CG` | 2052 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `CG_Bleed_SV` | 1963 | Dock/Utility/CG-G1, East PH/Utility/CG-E1, East PH/Utility/CG-E2, East PH/Utility/CG-E3, East PH/Utility/CG-E4, Freezer/Utility/CG-A1 +7 |
| `Controller:Global` | `CG_Fans` | 2052 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `CG_Fans_Runtime` | 209 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `CG_HotGas_SV` | 2869 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `CG_Interlock` | 589 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `CG_Liquid_SV` | 2869 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `CG_Suction_SV` | 2869 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `CG_ZAT` | 3306 | Club/Utility/CG-C1, Dock/Utility/CG-G1, Dock/Utility/CG-G2, Dock/Utility/CG-G3, Dock/Utility/CG-G4, Dock/Utility/CG-G5 +13 |
| `Controller:Global` | `COMP` | 5340 | Machine Room/Compressors/COMP 1, Machine Room/Compressors/COMP 4, Machine Room/Compressors/COMP 5, Machine Room/Compressors/COMP 6, Machine Room/Compressors/COMP 7 |
| `Controller:Global` | `Cmd_FirstNoDelay` | 1 | Condensers/Sequences/HSD |
| `Controller:Global` | `Enable_Comp_Alm` | 1 | |
| `Controller:Global` | `Enable_Fire_Alm` | 1 | |
| `Controller:Global` | `Enable_NH3_Alm` | 1 | |
| `Controller:Global` | `Enable_PS_Alm` | 1 | |
| `Controller:Global` | `Enable_Temp_Alm` | 1 | |
| `Controller:Global` | `FD` | 208 | Dock/Detectors/FD05, East PH/Detectors/FD04, Freezer/Detectors/FD01, West PH/Detectors/FD03 |
| `Controller:Global` | `HMI_ESTOP` | 1 | |
| `Controller:Global` | `HMI_Ltu_Clear` | 1 | Machine Room/LTU/NH3 LTU |
| `Controller:Global` | `HPR_LOLO` | 52 | Machine Room/Tanks/HPR |
| `Controller:Global` | `HSD_Fixed_SP` | 1 | Condensers/Sequences/HSD |
| `Controller:Global` | `HSD_PIDE` | 262 | |
| `Controller:Global` | `HSD_Seqr` | 51 | Condensers/Sequences/HSD |
| `Controller:Global` | `HSD_Sequence` | 7 | Condensers/Sequences/HSD |
| `Controller:Global` | `HSS` | 62 | Machine Room/Sequences/HSS |
| `Controller:Global` | `HSS_LU_PIDE` | 262 | |
| `Controller:Global` | `HTPS_SET` | 1 | Machine Room/Tanks/HTR |
| `Controller:Global` | `HTRL_PUMPS_SEQ` | 35 | Machine Room/Tanks/HTR |
| `Controller:Global` | `HTR_HIHI` | 52 | Machine Room/Tanks/HTR |
| `Controller:Global` | `HTR_HLCO` | 52 | Machine Room/Tanks/HTR |
| `Controller:Global` | `HTR_LOLO` | 52 | Machine Room/Tanks/HTR |
| `Controller:Global` | `HTR_OPL` | 52 | Machine Room/Tanks/HTR |
| `Controller:Global` | `HTR_PUMP1_INTLK` | 31 | Machine Room/Pumps/HTLR-Pump 1 |
| `Controller:Global` | `HTR_PUMP2_INTLK` | 31 | Machine Room/Pumps/HTLR-Pump 2 |
| `Controller:Global` | `HTR_PUMPS` | 216 | Machine Room/Pumps/HTLR-Pump 1, Machine Room/Pumps/HTLR-Pump 2 |
| `Controller:Global` | `HTR_PUMPS_ALM` | 104 | Machine Room/Tanks/HTR |
| `Controller:Global` | `HTR_PUMPS_RUNTIME` | 22 | Machine Room/Pumps/HTLR-Pump 1, Machine Room/Pumps/HTLR-Pump 2 |
| `Controller:Global` | `HT_LVL` | 174 | Machine Room/Tanks/HTR |
| `Controller:Global` | `KW_PULSE` | 52 | |
| `Controller:Global` | `LSS` | 62 | Machine Room/Sequences/LSS |
| `Controller:Global` | `LSS_HMI_Enable` | 1 | Machine Room/Sequences/LSS |
| `Controller:Global` | `LSS_LU_PIDE` | 262 | |
| `Controller:Global` | `LTPS_SET` | 1 | Machine Room/Tanks/LTR |
| `Controller:Global` | `LTR1_LSHH` | 52 | |
| `Controller:Global` | `LTRL_PUMPS_SEQ` | 35 | Machine Room/Tanks/LTR |
| `Controller:Global` | `LTR_HIHI` | 52 | Machine Room/Tanks/LTR |
| `Controller:Global` | `LTR_HLCO` | 52 | Machine Room/Tanks/LTR |
| `Controller:Global` | `LTR_LOLO` | 52 | Machine Room/Tanks/LTR |
| `Controller:Global` | `LTR_OPL` | 52 | Machine Room/Tanks/LTR |
| `Controller:Global` | `LTR_PUMP1_INTLK` | 31 | Machine Room/Pumps/LTLR-Pump 1 |
| `Controller:Global` | `LTR_PUMP2_INTLK` | 31 | Machine Room/Pumps/LTLR-Pump 2 |
| `Controller:Global` | `LTR_PUMPS` | 216 | Machine Room/Pumps/LTLR-Pump 1, Machine Room/Pumps/LTLR-Pump 2 |
| `Controller:Global` | `LTR_PUMPS_ALM` | 104 | Machine Room/Tanks/LTR |
| `Controller:Global` | `LTR_PUMPS_RUNTIME` | 22 | Machine Room/Pumps/LTLR-Pump 1, Machine Room/Pumps/LTLR-Pump 2 |
| `Controller:Global` | `LT_CSV` | 174 | Condensers/Tanks/CSV |
| `Controller:Global` | `LT_HPR` | 174 | Machine Room/Tanks/HPR |
| `Controller:Global` | `LT_LVL` | 174 | Machine Room/Tanks/LTR |
| `Controller:Global` | `Local:10:I` | 2 | |
| `Controller:Global` | `Local:11:I` | 2 | |
| `Controller:Global` | `Local:12:I` | 2 | |
| `Controller:Global` | `Local:12:O` | 1 | |
| `Controller:Global` | `Local:13:I` | 2 | |
| `Controller:Global` | `Local:13:O` | 1 | |
| `Controller:Global` | `Local:14:I` | 2 | |
| `Controller:Global` | `Local:14:O` | 1 | |
| `Controller:Global` | `Local:15:I` | 2 | |
| `Controller:Global` | `Local:15:O` | 1 | |
| `Controller:Global` | `Local:16:I` | 2 | |
| `Controller:Global` | `Local:16:O` | 1 | |
| `Controller:Global` | `Local:17:I` | 2 | |
| `Controller:Global` | `Local:17:O` | 1 | |
| `Controller:Global` | `Local:18:I` | 2 | |
| `Controller:Global` | `Local:18:O` | 1 | |
| `Controller:Global` | `Local:19:I` | 2 | |
| `Controller:Global` | `Local:19:O` | 1 | |
| `Controller:Global` | `Local:1:I` | 56 | |
| `Controller:Global` | `Local:1:O` | 17 | |
| `Controller:Global` | `Local:2:I` | 56 | |
| `Controller:Global` | `Local:2:O` | 17 | |
| `Controller:Global` | `Local:3:I` | 56 | |
| `Controller:Global` | `Local:3:O` | 17 | |
| `Controller:Global` | `Local:4:I` | 56 | |
| `Controller:Global` | `Local:4:O` | 17 | |
| `Controller:Global` | `Local:5:I` | 2 | |
| `Controller:Global` | `Local:6:I` | 2 | |
| `Controller:Global` | `Local:7:I` | 2 | |
| `Controller:Global` | `Local:8:I` | 2 | |
| `Controller:Global` | `Local:9:I` | 2 | |
| `Controller:Global` | `MAIN_HG_CV6` | 151 | Condensers/Valves/Main HG CV6 |
| `Controller:Global` | `MAIN_LIQ_CV5` | 151 | Machine Room/Valves/Main Liq SV |
| `Controller:Global` | `MASTER_AD1` | 52 | Machine Room/Detectors/MASTER-AD1 |
| `Controller:Global` | `MR_ALM_ES1` | 52 | |
| `Controller:Global` | `MR_ALM_RST1` | 52 | |
| `Controller:Global` | `MR_ALM_SIL1` | 52 | |
| `Controller:Global` | `MR_ALM_VS1` | 52 | |
| `Controller:Global` | `MR_EEF1` | 108 | |
| `Controller:Global` | `MR_EEF15` | 52 | Machine Room/ExhaustFans/MR EF |
| `Controller:Global` | `MR_EEF15_FailToStart` | 1 | Machine Room/ExhaustFans/MR EF |
| `Controller:Global` | `MR_EEF2` | 108 | |
| `Controller:Global` | `NH3_LTU` | 52 | Machine Room/LTU/NH3 LTU |
| `Controller:Global` | `NH3_LTU_Count_Alarm_Inp` | 1 | Machine Room/LTU/NH3 LTU |
| `Controller:Global` | `NH3_LTU_Count_Alarm_SP` | 1 | Machine Room/LTU/NH3 LTU |
| `Controller:Global` | `NH3_LTU_HMI_Count` | 1 | Machine Room/LTU/NH3 LTU |
| `Controller:Global` | `PS` | 1768 | Machine Room/RuptureDisks/PS01 EC1A-1, Machine Room/RuptureDisks/PS02 EC1A-2, Machine Room/RuptureDisks/PS03 EC1B-1, Machine Room/RuptureDisks/PS04 EC1B-2, Machine Room/RuptureDisks/PS05 COMP-1-SEPR-1, Machine Room/RuptureDisks/PS06 COMP-1-SEPR-2 +28 |
| `Controller:Global` | `RCP_ALM_ES1` | 52 | |
| `Controller:Global` | `RCP_MCR` | 139 | |
| `Controller:Global` | `RS_BACKUP_MW_CV26` | 151 | Condensers/Valves/Backup MW CV26 |
| `Controller:Global` | `RS_LLCO2` | 52 | Condensers/LevelSwitches/RS-LLCO2 |
| `Controller:Global` | `RS_LVL_OL2` | 52 | Condensers/LevelSwitches/RS-LVL-OL2 |
| `Controller:Global` | `RS_LVL_OL3` | 52 | Condensers/LevelSwitches/RS-LVL-OL3 |
| `Controller:Global` | `RS_MW_CV25` | 151 | Condensers/Valves/Main MW CV25 |
| `Controller:Global` | `SYS_PT1` | 174 | Machine Room/Sensors/LSS-Pumps Pressure |
| `Controller:Global` | `SYS_PT2` | 174 | Machine Room/Sensors/HSS-Pumps Pressure |
| `Controller:Global` | `SYS_PT3` | 174 | Machine Room/Sensors/HSD-Discharge Pressure |
| `Controller:Global` | `SYS_PT4` | 174 | Machine Room/Sensors/LSL-Pumps Pressure |
| `Controller:Global` | `SYS_PT5` | 174 | Machine Room/Sensors/HSL-Pumps Pressure |
| `Controller:Global` | `SafetyRelay:I` | 146 | Machine Room/SafetyRelays/HLCO Safety Relay |
| `Controller:Global` | `SafetyRelay:O` | 18 | |
| `Controller:Global` | `SafetyRelay_MajorFault` | 1 | Machine Room/SafetyRelays/HLCO Safety Relay |
| `Controller:Global` | `SafetyRelay_ResetAlm` | 1 | Machine Room/SafetyRelays/HLCO Safety Relay |
| `Controller:Global` | `Set_Time` | 1 | |
| `Controller:Global` | `TS_AIR` | 174 | Condensers/Sensors/Outside Air Temp |
| `Controller:Global` | `TS_UF1` | 174 | SuperChill/Sensors/Underfloor Temp |
| `Controller:Global` | `TS_UF2` | 174 | Freezer/Sensors/Underfloor Temp |
| `Controller:Global` | `Time_New` | 5 | |
| `Program:CompSeq_LSS` | `Program:CompSeq_LSS` | 262 | |
| `Program:Quantum_ENET_Comms` | `Program:Quantum_ENET_Comms` | 139 | |
| `Program:RCP_Alarm_Circuit` | `Program:RCP_Alarm_Circuit` | 2 | Machine Room/Digitals/FIRE, Machine Room/Digitals/RDISKS |
| `Program:System_Clock_Timers` | `Program:System_Clock_Timers` | 1 | |
| `_Diagnostics_` | `_Diagnostics_` | 25 | |
