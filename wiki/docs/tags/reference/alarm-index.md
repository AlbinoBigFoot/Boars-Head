---
title: "Alarm Index (Generated)"
sidebar_label: "Alarm Index"
description: "Every Ignition alarm defined on a UDT member, with priority and enable condition."
generated: true
---

:::note

:::
Every Ignition alarm configured in the tag configuration. The rule is that alarms live on UDT definition members only ([Alarms](../alarms.md)); the second table lists any alarm found on an instance or plain tag (it should be empty).

**32 alarm definitions** on UDT members: 17 High, 9 Medium, 4 Critical, 2 Low.

| UDT | Member | Alarm | Priority | Mode | Enabled | Notes |
|---|---|---|---|---|---|---|
| [Devices/LTU](udts/devices/ltu.md) | `PlcCountAlarm` | Transfer Count High | Medium | WhenTrue | `true` | NH3\_LTU\_Count\_Alarm\_Inp (count &gt;= setpoint) |
| [PLC/CR30\_Input](udts/plc/cr30-input.md) | `ConnectionFaulted` | Safety Relay Comm Loss | High | WhenTrue | `true` | CR30 SafetyRelay:I.ConnectionFaulted |
| [PLC/CR30\_Input](udts/plc/cr30-input.md) | `MajorFault` | Safety Relay Major Fault | High | WhenTrue | `true` | CR30 SafetyRelay:I.MajorFault |
| [PLC/CR30\_Input](udts/plc/cr30-input.md) | `SOF01ResetRequired` | LSS HLCO Output 0 Reset Required | Medium | WhenTrue | `true` | CR30 SafetyRelay:I.SOF01ResetRequired |
| [PLC/CR30\_Input](udts/plc/cr30-input.md) | `SOF02ResetRequired` | HSS HLCO Output 1 Reset Required | Medium | WhenTrue | `true` | CR30 SafetyRelay:I.SOF02ResetRequired |
| [PLC/P\_AIn](udts/plc/p-ain.md) | `Sts_Fail` | Input Failure | High | WhenTrue | `coalesce({[.]Cfg_HasFailAlm}, false)` | PlantPAx P\_AIn Sts\_Fail |
| [PLC/P\_AIn](udts/plc/p-ain.md) | `Sts_Hi` | High | Medium | WhenTrue | `coalesce({[.]Cfg_HasHiAlm}, false)` | PlantPAx P\_AIn Sts\_Hi |
| [PLC/P\_AIn](udts/plc/p-ain.md) | `Sts_HiHi` | High-High | High | WhenTrue | `coalesce({[.]Cfg_HasHiHiAlm}, false)` | PlantPAx P\_AIn Sts\_HiHi |
| [PLC/P\_AIn](udts/plc/p-ain.md) | `Sts_Lo` | Low | Medium | WhenTrue | `coalesce({[.]Cfg_HasLoAlm}, false)` | PlantPAx P\_AIn Sts\_Lo |
| [PLC/P\_AIn](udts/plc/p-ain.md) | `Sts_LoLo` | Low-Low | High | WhenTrue | `coalesce({[.]Cfg_HasLoLoAlm}, false)` | PlantPAx P\_AIn Sts\_LoLo |
| [PLC/P\_DIn](udts/plc/p-din.md) | `Sts` | State Alarm | High | WhenTrue | `{AlarmOnSts}` | PlantPAx P\_DIn Sts (AlarmOnSts) |
| [PLC/P\_DIn](udts/plc/p-din.md) | `Sts_TgtDisagree` | Target Disagree | Medium | WhenTrue | `coalesce({[.]Cfg_HasTgtDisagreeAlm}, false)` | PlantPAx P\_DIn Sts\_TgtDisagree |
| [PLC/P\_Motor](udts/plc/p-motor.md) | `Alm_FailToStart` | Fail To Start | High | WhenTrue | `true` | PlantPAx P\_Motor Alm\_FailToStart |
| [PLC/P\_Motor](udts/plc/p-motor.md) | `Alm_FailToStop` | Fail To Stop | High | WhenTrue | `true` | PlantPAx P\_Motor Alm\_FailToStop |
| [PLC/P\_Motor](udts/plc/p-motor.md) | `Alm_IntlkTrip` | Interlock Trip | Medium | WhenTrue | `true` | PlantPAx P\_Motor Alm\_IntlkTrip |
| [PLC/P\_Motor](udts/plc/p-motor.md) | `Alm_IOFault` | IO Fault | Critical | WhenTrue | `true` | PlantPAx P\_Motor Alm\_IOFault |
| [PLC/P\_ValveSO](udts/plc/p-valveso.md) | `Alm_FullStall` | Full Stall | High | WhenTrue | `true` | PlantPAx P\_ValveSO Alm\_FullStall |
| [PLC/P\_ValveSO](udts/plc/p-valveso.md) | `Alm_IntlkTrip` | Interlock Trip | Medium | WhenTrue | `true` | PlantPAx P\_ValveSO Alm\_IntlkTrip |
| [PLC/P\_ValveSO](udts/plc/p-valveso.md) | `Alm_IOFault` | IO Fault | High | WhenTrue | `true` | PlantPAx P\_ValveSO Alm\_IOFault |
| [PLC/P\_ValveSO](udts/plc/p-valveso.md) | `Alm_TransitStall` | Transit Stall | High | WhenTrue | `true` | PlantPAx P\_ValveSO Alm\_TransitStall |
| [PLC/Screw\_Compressor](udts/plc/screw-compressor.md) | `Alm` | Compressor Alarm | Medium | WhenTrue | `true` | Screw\_Compressor COMP\[n\].Alm |
| [PLC/Screw\_Compressor](udts/plc/screw-compressor.md) | `Comm` | Comm Error | Low | WhenTrue | `true` | Screw\_Compressor COMP\[n\].Comm |
| [PLC/Screw\_Compressor](udts/plc/screw-compressor.md) | `Cutout` | Cutout | High | WhenTrue | `true` | Screw\_Compressor COMP\[n\].Cutout |
| [PLC/Screw\_Compressor](udts/plc/screw-compressor.md) | `Failed` | Failed | Critical | WhenTrue | `true` | Screw\_Compressor COMP\[n\].Failed |
| [PLC/Controllers/CompactLogix\_5370](udts/plc-controllers/compactlogix-5370.md) | `CommLoss` | Controller Communication Lost | Critical | WhenTrue | `true` | PLC communication lost: Logix driver \[Diagnostics\]/Connected = false for 12 s (active del… |
| [PLC/Controllers/CompactLogix\_5370](udts/plc-controllers/compactlogix-5370.md) | `IOFault` | Controller I/O Fault | High | WhenTrue | `true` | CIP identity extended status 2: at least one faulted I/O connection. Suppressed while PLC… |
| [PLC/Controllers/CompactLogix\_5370](udts/plc-controllers/compactlogix-5370.md) | `MajorFault` | Controller Major Fault | Critical | WhenTrue | `true` | CIP identity Status major fault (bits 10/11 or extended status 5). Suppressed while PLC c… |
| [PLC/Controllers/CompactLogix\_5370](udts/plc-controllers/compactlogix-5370.md) | `MinorFault` | Controller Minor Fault | Low | WhenTrue | `true` | CIP identity Status minor fault (bits 8/9). Suppressed while PLC communication is lost. |
| [PLC/Controllers/CompactLogix\_5370](udts/plc-controllers/compactlogix-5370.md) | `NotRun` | Controller Not In Run Mode | High | WhenTrue | `true` | Controller connected but its extended status is not Run (6) or Run with I/O fault (2): Pr… |
| [PLC/Modules/\_Discrete16In](udts/plc-modules/discrete16in.md) | `Faulted` | Module Fault | High | WhenTrue | `true` | 1769 16-point Local:n:I.Fault != 0 (-1 = connection fault to the card). Suppressed while… |
| [PLC/Modules/\_Discrete16Out](udts/plc-modules/discrete16out.md) | `Faulted` | Module Fault | High | WhenTrue | `true` | 1769 16-point Local:n:I.Fault != 0 (-1 = connection fault to the card). Suppressed while… |
| [PLC/Modules/1769\_IF8](udts/plc-modules/type-1769-if8.md) | `Faulted` | Module Fault | High | WhenTrue | `true` | 1769-IF8 Local:n:I.Fault != 0 (-1 = connection fault to the card). Suppressed while PLC c… |

## Alarms On Instances Or Plain Tags

_None._
