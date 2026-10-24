---
title: "Device Instances (Generated)"
sidebar_label: "All Device Instances"
description: "Every UDT instance under [default]Boars_Head with its type, parameters and page."
generated: true
---

:::note

:::
Every UDT instance in the device tree `[default]Boars_Head/<Site>/<Area>/<Type>/<Device>`. Each page lists the instance parameters and the PLC object every nested part reads once the parameters are substituted (`[DeviceName]TagPrefix`). The **In `_RCP1_` mirror** column counts the tags of that object in the pruned browse mirror `[default]_RCP1_` (evidence that the object exists in the controller; empty when the mirror is not on this machine).

How the values get there: [PAX Mapping](../../pax-mapping/index.md).

| Instance | Type | Folder | Parameters |
|---|---|---|---|
| `AD03` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Club/Detectors](club-detectors.md) | DInTag=AD\[3\] |
| `CG-C1` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Club/Utility](club-utility.md) | CGTag=CG\[5\], ZATTag=CG\_ZAT\[5\], IntlkTag=CG\_Interlock\[5\], FansTag=CG\_Fans\[5\], FansRunTimeTag=CG\_Fans\_Runtime\[5\], LiquidS… |
| `Fan 1` | [Devices/Pump](../udts/devices/pump.md) | [Condensers/Condensers/EC-1A](condensers-condensers-ec-1a.md) | MotorTag=CD1A\_FAN1, IntlkTag=EC1\_INTLK, RunTimeTag=CD1A\_FAN1\_Runtime |
| `Fan 2` | [Devices/Pump](../udts/devices/pump.md) | [Condensers/Condensers/EC-1A](condensers-condensers-ec-1a.md) | MotorTag=CD1A\_FAN2, IntlkTag=EC1\_INTLK, RunTimeTag=CD1A\_FAN2\_Runtime |
| `Fan 1` | [Devices/Pump](../udts/devices/pump.md) | [Condensers/Condensers/EC-1B](condensers-condensers-ec-1b.md) | MotorTag=CD1B\_FAN1, IntlkTag=EC1\_INTLK, RunTimeTag=CD1B\_FAN1\_Runtime |
| `Fan 2` | [Devices/Pump](../udts/devices/pump.md) | [Condensers/Condensers/EC-1B](condensers-condensers-ec-1b.md) | MotorTag=CD1B\_FAN2, IntlkTag=EC1\_INTLK, RunTimeTag=CD1B\_FAN2\_Runtime |
| `RS-LVL-OL2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Condensers/LevelSwitches](condensers-levelswitches.md) | DInTag=RS\_LVL\_OL2 |
| `RS-LVL-OL3` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Condensers/LevelSwitches](condensers-levelswitches.md) | DInTag=RS\_LVL\_OL3 |
| `RS-LLCO2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Condensers/LevelSwitches](condensers-levelswitches.md) | DInTag=RS\_LLCO2 |
| `Sump Pump 1` | [Devices/Pump](../udts/devices/pump.md) | [Condensers/Pumps](condensers-pumps.md) | MotorTag=CD1\_P1, IntlkTag=EC1\_INTLK, RunTimeTag=CD1\_P1\_Runtime |
| `Sump Pump 2` | [Devices/Pump](../udts/devices/pump.md) | [Condensers/Pumps](condensers-pumps.md) | MotorTag=CD1\_P2, IntlkTag=EC1\_INTLK, RunTimeTag=CD1\_P2\_Runtime |
| `Sump Pump 3` | [Devices/Pump](../udts/devices/pump.md) | [Condensers/Pumps](condensers-pumps.md) | MotorTag=CD1\_P3, IntlkTag=EC1\_INTLK, RunTimeTag=CD1\_P3\_Runtime |
| `Outside Air Temp` | [Devices/Sensor](../udts/devices/sensor.md) | [Condensers/Sensors](condensers-sensors.md) | AInTag=TS\_AIR, AInEU=°F |
| `HSD` | [Devices/DischargeSequence](../udts/devices/dischargesequence.md) | [Condensers/Sequences](condensers-sequences.md) | SeqrTag=HSD\_Seqr, Seq1Tag=HSD\_Sequence\[1\], Seq2Tag=HSD\_Sequence\[2\], Seq3Tag=HSD\_Sequence\[3\], Seq4Tag=HSD\_Sequence\[4\], S… |
| `CSV` | [Devices/Tank](../udts/devices/tank.md) | [Condensers/Tanks](condensers-tanks.md) | LevelTag=LT\_CSV, LevelEU=In" |
| `Main HG CV6` | [Devices/Valve](../udts/devices/valve.md) | [Condensers/Valves](condensers-valves.md) | ValveTag=MAIN\_HG\_CV6 |
| `Main MW CV25` | [Devices/Valve](../udts/devices/valve.md) | [Condensers/Valves](condensers-valves.md) | ValveTag=RS\_MW\_CV25, IntlkTag=EC1\_INTLK |
| `Backup MW CV26` | [Devices/Valve](../udts/devices/valve.md) | [Condensers/Valves](condensers-valves.md) | ValveTag=RS\_BACKUP\_MW\_CV26, IntlkTag=EC1\_INTLK |
| `FD05` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Dock/Detectors](dock-detectors.md) | DInTag=FD\[5\] |
| `AD08` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Dock/Detectors](dock-detectors.md) | DInTag=AD\[8\] |
| `AD07` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Dock/Detectors](dock-detectors.md) | DInTag=AD\[7\] |
| `CG-G5` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Dock/Utility](dock-utility.md) | CGTag=CG\[19\], ZATTag=CG\_ZAT\[19\], IntlkTag=CG\_Interlock\[19\], FansTag=CG\_Fans\[19\], FansRunTimeTag=CG\_Fans\_Runtime\[19\], Li… |
| `CG-G3` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Dock/Utility](dock-utility.md) | CGTag=CG\[17\], ZATTag=CG\_ZAT\[17\], IntlkTag=CG\_Interlock\[17\], FansTag=CG\_Fans\[17\], FansRunTimeTag=CG\_Fans\_Runtime\[17\], Li… |
| `CG-G2` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Dock/Utility](dock-utility.md) | CGTag=CG\[16\], ZATTag=CG\_ZAT\[16\], IntlkTag=CG\_Interlock\[16\], FansTag=CG\_Fans\[16\], FansRunTimeTag=CG\_Fans\_Runtime\[16\], Li… |
| `CG-G1` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Dock/Utility](dock-utility.md) | CGTag=CG\[15\], ZATTag=CG\_ZAT\[15\], IntlkTag=CG\_Interlock\[15\], FansTag=CG\_Fans\[15\], FansRunTimeTag=CG\_Fans\_Runtime\[15\], Li… |
| `CG-G4` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Dock/Utility](dock-utility.md) | CGTag=CG\[18\], ZATTag=CG\_ZAT\[18\], IntlkTag=CG\_Interlock\[18\], FansTag=CG\_Fans\[18\], FansRunTimeTag=CG\_Fans\_Runtime\[18\], Li… |
| `AD05` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [East PH/Detectors](east-ph-detectors.md) | DInTag=AD\[5\] |
| `FD04` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [East PH/Detectors](east-ph-detectors.md) | DInTag=FD\[4\] |
| `CG-E2` | [Devices/Evaporator](../udts/devices/evaporator.md) | [East PH/Utility](east-ph-utility.md) | CGTag=CG\[8\], ZATTag=CG\_ZAT\[8\], IntlkTag=CG\_Interlock\[8\], FansTag=CG\_Fans\[8\], FansRunTimeTag=CG\_Fans\_Runtime\[8\], LiquidS… |
| `CG-E4` | [Devices/Evaporator](../udts/devices/evaporator.md) | [East PH/Utility](east-ph-utility.md) | CGTag=CG\[10\], ZATTag=CG\_ZAT\[10\], IntlkTag=CG\_Interlock\[10\], FansTag=CG\_Fans\[10\], FansRunTimeTag=CG\_Fans\_Runtime\[10\], Li… |
| `CG-E1` | [Devices/Evaporator](../udts/devices/evaporator.md) | [East PH/Utility](east-ph-utility.md) | CGTag=CG\[7\], ZATTag=CG\_ZAT\[7\], IntlkTag=CG\_Interlock\[7\], FansTag=CG\_Fans\[7\], FansRunTimeTag=CG\_Fans\_Runtime\[7\], LiquidS… |
| `CG-E3` | [Devices/Evaporator](../udts/devices/evaporator.md) | [East PH/Utility](east-ph-utility.md) | CGTag=CG\[9\], ZATTag=CG\_ZAT\[9\], IntlkTag=CG\_Interlock\[9\], FansTag=CG\_Fans\[9\], FansRunTimeTag=CG\_Fans\_Runtime\[9\], LiquidS… |
| `FD01` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Freezer/Detectors](freezer-detectors.md) | DInTag=FD\[1\] |
| `AD01` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Freezer/Detectors](freezer-detectors.md) | DInTag=AD\[1\] |
| `Underfloor Temp` | [Devices/Sensor](../udts/devices/sensor.md) | [Freezer/Sensors](freezer-sensors.md) | AInTag=TS\_UF2, AInEU=°F |
| `CG-A2` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Freezer/Utility](freezer-utility.md) | CGTag=CG\[2\], ZATTag=CG\_ZAT\[2\], IntlkTag=CG\_Interlock\[2\], FansTag=CG\_Fans\[2\], FansRunTimeTag=CG\_Fans\_Runtime\[2\], LiquidS… |
| `CG-A1` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Freezer/Utility](freezer-utility.md) | CGTag=CG\[1\], ZATTag=CG\_ZAT\[1\], IntlkTag=CG\_Interlock\[1\], FansTag=CG\_Fans\[1\], FansRunTimeTag=CG\_Fans\_Runtime\[1\], LiquidS… |
| `COMP 6` | [Devices/Compressor](../udts/devices/compressor.md) | [Machine Room/Compressors](machine-room-compressors.md) | CompTag=COMP\[6\], IntlkTag=COMP\[6\].Interlock |
| `COMP 1` | [Devices/Compressor](../udts/devices/compressor.md) | [Machine Room/Compressors](machine-room-compressors.md) | CompTag=COMP\[1\], IntlkTag=COMP\[1\].Interlock |
| `COMP 5` | [Devices/Compressor](../udts/devices/compressor.md) | [Machine Room/Compressors](machine-room-compressors.md) | CompTag=COMP\[5\], IntlkTag=COMP\[5\].Interlock |
| `COMP 4` | [Devices/Compressor](../udts/devices/compressor.md) | [Machine Room/Compressors](machine-room-compressors.md) | CompTag=COMP\[4\], IntlkTag=COMP\[4\].Interlock |
| `Overview` | [Overview/Compressor Overview](../udts/overview/compressor-overview.md) | [Machine Room/Compressors](machine-room-compressors.md) | |
| `COMP 7` | [Devices/Compressor](../udts/devices/compressor.md) | [Machine Room/Compressors](machine-room-compressors.md) | CompTag=COMP\[7\], IntlkTag=COMP\[7\].Interlock |
| `VL-AD` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/Detectors](machine-room-detectors.md) | DInTag=AD\_VL |
| `MR-AD1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/Detectors](machine-room-detectors.md) | DInTag=AD\_MR1 |
| `MASTER-AD1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/Detectors](machine-room-detectors.md) | DInTag=MASTER\_AD1 |
| `FIRE` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `MR AD` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `RDISKS` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `VL AD` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `Alarm Light` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `Alarm Circuit` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `Alarm Reset` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `Alarm Silence` | [\_Root/Digital](../udts/root/digital.md) | [Machine Room/Digitals](machine-room-digitals.md) | |
| `BR EF` | [Devices/ExhaustFan](../udts/devices/exhaustfan.md) | [Machine Room/ExhaustFans](machine-room-exhaustfans.md) | FanTag=BR\_EEF17, FailTag=BR\_EEF17\_FailToStart |
| `MR EF` | [Devices/ExhaustFan](../udts/devices/exhaustfan.md) | [Machine Room/ExhaustFans](machine-room-exhaustfans.md) | FanTag=MR\_EEF15, FailTag=MR\_EEF15\_FailToStart |
| `Overview` | [Overview/Exhaust Fan Overview](../udts/overview/exhaust-fan-overview.md) | [Machine Room/ExhaustFans](machine-room-exhaustfans.md) | |
| `NH3 LTU` | [Devices/LTU](../udts/devices/ltu.md) | [Machine Room/LTU](machine-room-ltu.md) | InputTag=NH3\_LTU, CountTag=NH3\_LTU\_HMI\_Count, CountAlarmTag=NH3\_LTU\_Count\_Alarm\_Inp, CountAlarmSPTag=NH3\_LTU\_Count\_Alar… |
| `RCP1` | [PLC/Sites/BH\_Groveport\_RCP1](../udts/plc-sites/bh-groveport-rcp1.md) | [Machine Room/PLC](machine-room-plc.md) | Description=Refrigeration Control Panel 1 PLC, DeviceName=RCP1 |
| `HTLR-Pump 2` | [Devices/Pump](../udts/devices/pump.md) | [Machine Room/Pumps](machine-room-pumps.md) | MotorTag=HTR\_PUMPS\[2\], IntlkTag=HTR\_PUMP2\_INTLK, RunTimeTag=HTR\_PUMPS\_RUNTIME\[2\] |
| `LTLR-Pump 2` | [Devices/Pump](../udts/devices/pump.md) | [Machine Room/Pumps](machine-room-pumps.md) | MotorTag=LTR\_PUMPS\[2\], IntlkTag=LTR\_PUMP2\_INTLK, RunTimeTag=LTR\_PUMPS\_RUNTIME\[2\] |
| `LTLR-Pump 1` | [Devices/Pump](../udts/devices/pump.md) | [Machine Room/Pumps](machine-room-pumps.md) | MotorTag=LTR\_PUMPS\[1\], IntlkTag=LTR\_PUMP1\_INTLK, RunTimeTag=LTR\_PUMPS\_RUNTIME\[1\] |
| `HTLR-Pump 1` | [Devices/Pump](../udts/devices/pump.md) | [Machine Room/Pumps](machine-room-pumps.md) | MotorTag=HTR\_PUMPS\[1\], IntlkTag=HTR\_PUMP1\_INTLK, RunTimeTag=HTR\_PUMPS\_RUNTIME\[1\] |
| `Overview` | [Overview/Pump Overview](../udts/overview/pump-overview.md) | [Machine Room/Pumps](machine-room-pumps.md) | |
| `PS01 EC1A-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[1\] |
| `PS02 EC1A-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[2\] |
| `PS03 EC1B-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[3\] |
| `PS04 EC1B-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[4\] |
| `PS05 COMP-1-SEPR-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[5\] |
| `PS06 COMP-1-SEPR-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[6\] |
| `PS07 COMP-1-TSYPHON` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[7\] |
| `PS08 COMP-2-SEPR-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[8\] |
| `PS09 COMP-2-SEPR-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[9\] |
| `PS10 COMP-2-TSYPHON` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[10\] |
| `PS14 COMP-4-SEPR-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[14\] |
| `PS15 COMP-4-SEPR-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[15\] |
| `PS16 COMP-4-TSYPHON` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[16\] |
| `PS17 COMP-5-SEPR-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[17\] |
| `PS18 COMP-5-SEPR-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[18\] |
| `PS19 COMP-5-TSYPHON` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[19\] |
| `PS20 COMP-6-SEPR-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[20\] |
| `PS21 COMP-6-SEPR-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[21\] |
| `PS22 COMP-6-TSYPHON` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[22\] |
| `PS23 COMP-7-SEPR-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[23\] |
| `PS24 COMP-7-SEPR-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[24\] |
| `PS25 COMP-7-TSYPHON` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[25\] |
| `PS26 TSYPON-VESSEL-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[26\] |
| `PS27 TSYPON-VESSEL-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[27\] |
| `PS28 LTR-VESSEL-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[28\] |
| `PS29 LTR-VESSEL-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[29\] |
| `PS30 LTR-OIL POT` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[30\] |
| `PS31 HTR-VESSEL-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[31\] |
| `PS32 HTR-VESSEL-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[32\] |
| `PS33 HTR-VESSEL-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[33\] |
| `PS34 HTR-OIL POT` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[34\] |
| `PS35 PURGER` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[35\] |
| `PS36 HPR-1` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[36\] |
| `PS37 HPR-2` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Machine Room/RuptureDisks](machine-room-rupturedisks.md) | DInTag=PS\[37\] |
| `HLCO Safety Relay` | [Devices/SafetyRelay](../udts/devices/safetyrelay.md) | [Machine Room/SafetyRelays](machine-room-safetyrelays.md) | ModuleTag=SafetyRelay:I, MajorFaultTag=SafetyRelay\_MajorFault, ResetAlmTag=SafetyRelay\_ResetAlm |
| `LSS-Pumps Pressure` | [Devices/Sensor](../udts/devices/sensor.md) | [Machine Room/Sensors](machine-room-sensors.md) | AInTag=SYS\_PT1, AInEU=PSIG |
| `HSD-Discharge Pressure` | [Devices/Sensor](../udts/devices/sensor.md) | [Machine Room/Sensors](machine-room-sensors.md) | AInTag=SYS\_PT3, AInEU=PSIG |
| `LSL-Pumps Pressure` | [Devices/Sensor](../udts/devices/sensor.md) | [Machine Room/Sensors](machine-room-sensors.md) | AInTag=SYS\_PT4, AInEU=PSIG |
| `HSL-Pumps Pressure` | [Devices/Sensor](../udts/devices/sensor.md) | [Machine Room/Sensors](machine-room-sensors.md) | AInTag=SYS\_PT5, AInEU=PSIG |
| `Overview` | [Overview/Sensor Overview](../udts/overview/sensor-overview.md) | [Machine Room/Sensors](machine-room-sensors.md) | |
| `HSS-Pumps Pressure` | [Devices/Sensor](../udts/devices/sensor.md) | [Machine Room/Sensors](machine-room-sensors.md) | AInTag=SYS\_PT2, AInEU=PSIG |
| `Condenser Sump Level` | [Devices/Sensor](../udts/devices/sensor.md) | [Machine Room/Sensors](machine-room-sensors.md) | AInSource=\[default\]Boars\_Head/GrovePort/Condensers/Tanks/CSV/LvlAIn, AInEU=In" |
| `HSS` | [Devices/SuctionSequence](../udts/devices/suctionsequence.md) | [Machine Room/Sequences](machine-room-sequences.md) | SeqTag=HSS |
| `LSS` | [Devices/SuctionSequence](../udts/devices/suctionsequence.md) | [Machine Room/Sequences](machine-room-sequences.md) | SeqTag=LSS, EnableTag=LSS\_HMI\_Enable |
| `HTR` | [Devices/Tank](../udts/devices/tank.md) | [Machine Room/Tanks](machine-room-tanks.md) | LevelTag=HT\_LVL, PressSource=\[default\]Boars\_Head/GrovePort/Machine Room/Sensors/HSS-Pumps Pressure/AIn, HLCOTag=HTR\_HLC… |
| `LTR` | [Devices/Tank](../udts/devices/tank.md) | [Machine Room/Tanks](machine-room-tanks.md) | LevelTag=LT\_LVL, PressSource=\[default\]Boars\_Head/GrovePort/Machine Room/Sensors/LSS-Pumps Pressure/AIn, HLCOTag=LTR\_HLC… |
| `Overview` | [Overview/Tank Overview](../udts/overview/tank-overview.md) | [Machine Room/Tanks](machine-room-tanks.md) | |
| `HPR` | [Devices/Tank](../udts/devices/tank.md) | [Machine Room/Tanks](machine-room-tanks.md) | LevelTag=LT\_HPR, LoLoTag=HPR\_LOLO, LevelEU=% |
| `Main Liq SV` | [Devices/Valve](../udts/devices/valve.md) | [Machine Room/Valves](machine-room-valves.md) | ValveTag=MAIN\_LIQ\_CV5 |
| `Overview` | [Overview/Valve Overview](../udts/overview/valve-overview.md) | [Machine Room/Valves](machine-room-valves.md) | |
| `AD04` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [Palletizing/Detectors](palletizing-detectors.md) | DInTag=AD\[4\] |
| `CG-D1` | [Devices/Evaporator](../udts/devices/evaporator.md) | [Palletizing/Utility](palletizing-utility.md) | CGTag=CG\[6\], ZATTag=CG\_ZAT\[6\], IntlkTag=CG\_Interlock\[6\], FansTag=CG\_Fans\[6\], FansRunTimeTag=CG\_Fans\_Runtime\[6\], LiquidS… |
| `AD02` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [SuperChill/Detectors](superchill-detectors.md) | DInTag=AD\[2\] |
| `Underfloor Temp` | [Devices/Sensor](../udts/devices/sensor.md) | [SuperChill/Sensors](superchill-sensors.md) | AInTag=TS\_UF1, AInEU=°F |
| `CG-B2` | [Devices/Evaporator](../udts/devices/evaporator.md) | [SuperChill/Utility](superchill-utility.md) | CGTag=CG\[4\], ZATTag=CG\_ZAT\[4\], IntlkTag=CG\_Interlock\[4\], FansTag=CG\_Fans\[4\], FansRunTimeTag=CG\_Fans\_Runtime\[4\], LiquidS… |
| `CG-B1` | [Devices/Evaporator](../udts/devices/evaporator.md) | [SuperChill/Utility](superchill-utility.md) | CGTag=CG\[3\], ZATTag=CG\_ZAT\[3\], IntlkTag=CG\_Interlock\[3\], FansTag=CG\_Fans\[3\], FansRunTimeTag=CG\_Fans\_Runtime\[3\], LiquidS… |
| `FD03` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [West PH/Detectors](west-ph-detectors.md) | DInTag=FD\[3\] |
| `AD06` | [Devices/DiscreteInput](../udts/devices/discreteinput.md) | [West PH/Detectors](west-ph-detectors.md) | DInTag=AD\[6\] |
| `CG-F2` | [Devices/Evaporator](../udts/devices/evaporator.md) | [West PH/Utility](west-ph-utility.md) | CGTag=CG\[12\], ZATTag=CG\_ZAT\[12\], IntlkTag=CG\_Interlock\[12\], FansTag=CG\_Fans\[12\], FansRunTimeTag=CG\_Fans\_Runtime\[12\], Li… |
| `CG-F4` | [Devices/Evaporator](../udts/devices/evaporator.md) | [West PH/Utility](west-ph-utility.md) | CGTag=CG\[14\], ZATTag=CG\_ZAT\[14\], IntlkTag=CG\_Interlock\[14\], FansTag=CG\_Fans\[14\], FansRunTimeTag=CG\_Fans\_Runtime\[14\], Li… |
| `CG-F1` | [Devices/Evaporator](../udts/devices/evaporator.md) | [West PH/Utility](west-ph-utility.md) | CGTag=CG\[11\], ZATTag=CG\_ZAT\[11\], IntlkTag=CG\_Interlock\[11\], FansTag=CG\_Fans\[11\], FansRunTimeTag=CG\_Fans\_Runtime\[11\], Li… |
| `CG-F3` | [Devices/Evaporator](../udts/devices/evaporator.md) | [West PH/Utility](west-ph-utility.md) | CGTag=CG\[13\], ZATTag=CG\_ZAT\[13\], IntlkTag=CG\_Interlock\[13\], FansTag=CG\_Fans\[13\], FansRunTimeTag=CG\_Fans\_Runtime\[13\], Li… |
