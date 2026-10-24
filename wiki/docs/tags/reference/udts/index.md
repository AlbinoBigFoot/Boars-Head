---
title: "UDT Definitions (Generated)"
sidebar_label: "All UDT Definitions"
description: "Every UDT definition in the default tag provider, grouped by folder, with member, alarm, history and instance counts."
generated: true
---

:::note

:::
Every UDT (User Defined Type) definition in the `default` tag provider. In the Designer they are under **Tag Browser > default > Data Types**; on disk under `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/<folder>/udts.json`.

The hand-written guides explain the design: see [UDTs](../../udts/index.md).

## Config
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [Config/\_Alarms](config/alarms.md) | | 12 | 0 | 0 | 0 | 0 | in use |
| [Config/Interlock](config/interlock.md) | P\_Intlk HMI mirror | 0 | 47 | 0 | 0 | 0 | no instances |
| [Config/Integration](config/integration.md) | One API endpoint / connection (\_Config/Integrations/&lt;Name&gt;). shared.Integrations reads an… | 10 | 0 | 0 | 0 | 1 | in use |

## Devices
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [Devices/Valve](devices/valve.md) | valve | 1 | 5 | 0 | 0 | 4 | in use |
| [Devices/Compressor](devices/compressor.md) | compressor | 1 | 4 | 0 | 0 | 5 | in use |
| [Devices/CoolingTower](devices/coolingtower.md) | cooling tower | 0 | 18 | 0 | 0 | 0 | no instances |
| [Devices/Pump](devices/pump.md) | pump | 1 | 4 | 0 | 0 | 11 | in use |
| [Devices/ExhaustFan](devices/exhaustfan.md) | exhaust fan | 1 | 2 | 0 | 0 | 2 | in use |
| [Devices/Tank](devices/tank.md) | tank / vessel | 2 | 16 | 0 | 0 | 4 | in use |
| [Devices/VFD](devices/vfd.md) | vfd | 0 | 4 | 0 | 0 | 0 | no instances |
| [Devices/DiscreteInput](devices/discreteinput.md) | discrete input | 0 | 1 | 0 | 0 | 52 | in use |
| [Devices/Sensor](devices/sensor.md) | sensor | 0 | 3 | 0 | 0 | 9 | in use |
| [Devices/Evaporator](devices/evaporator.md) | Evaporator (CG\_RL\_Evap HMI mirror) | 2 | 11 | 0 | 0 | 19 | in use |
| [Devices/LTU](devices/ltu.md) | liquid transfer unit | 4 | 8 | 1 | 0 | 1 | in use |
| [Devices/SuctionSequence](devices/suctionsequence.md) | suction sequence | 1 | 6 | 0 | 0 | 2 | in use |
| [Devices/SafetyRelay](devices/safetyrelay.md) | safety relay | 2 | 2 | 0 | 0 | 1 | in use |
| [Devices/DischargeSequence](devices/dischargesequence.md) | discharge sequence | 13 | 5 | 0 | 0 | 1 | in use |

## Overview
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [Overview/Pump Overview](overview/pump-overview.md) | pump overview | 1 | 3 | 0 | 0 | 1 | in use |
| [Overview/Compressor Overview](overview/compressor-overview.md) | compressor overview | 1 | 3 | 0 | 0 | 1 | in use |
| [Overview/Exhaust Fan Overview](overview/exhaust-fan-overview.md) | exhaust fan overview | 1 | 3 | 0 | 0 | 1 | in use |
| [Overview/Evaporator Overview](overview/evaporator-overview.md) | evaporator overview | 1 | 3 | 0 | 0 | 0 | no instances |
| [Overview/Cooling Tower Overview](overview/cooling-tower-overview.md) | cooling tower overview | 1 | 3 | 0 | 0 | 0 | no instances |
| [Overview/Tank Overview](overview/tank-overview.md) | tank overview | 1 | 3 | 0 | 0 | 1 | in use |
| [Overview/Valve Overview](overview/valve-overview.md) | valve overview | 1 | 3 | 0 | 0 | 1 | in use |
| [Overview/Sensor Overview](overview/sensor-overview.md) | sensor overview | 1 | 3 | 0 | 0 | 1 | in use |

## PLC
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [PLC/TIMER](plc/timer.md) | | 5 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/MESSAGE](plc/message.md) | | 29 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Command\_Word](plc/command-word.md) | | 2 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/COUNTER](plc/counter.md) | | 7 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/CG\_RL\_Evap](plc/cg-rl-evap.md) | Controller CG\_RL\_Evap (read only) | 68 | 0 | 0 | 10 | 0 | in use |
| [PLC/Control\_Group\_DIO](plc/control-group-dio.md) | | 47 | 5 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FB\_XoutY](plc/fb-xouty.md) | | 22 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/HL\_LIMIT](plc/hl-limit.md) | | 0 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Accumulator](plc/accumulator.md) | | 1 | 4 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/RATE\_LIMITER](plc/rate-limiter.md) | | 0 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FBD\_COMPARE](plc/fbd-compare.md) | | 0 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/CR30\_Input](plc/cr30-input.md) | Controller CR30\_Input (read only) | 32 | 0 | 4 | 0 | 0 | in use |
| [PLC/QHD\_CompData](plc/qhd-compdata.md) | | 6 | 2 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FBD\_TIMER](plc/fbd-timer.md) | | 0 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FBD\_BOOLEAN\_NOT](plc/fbd-boolean-not.md) | | 0 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_AIn](plc/p-ain.md) | PlantPAx P\_AIn (read only) | 179 | 0 | 5 | 7 | 0 | in use |
| [PLC/R717\_P2T](plc/r717-p2t.md) | | 6 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_DIn](plc/p-din.md) | PlantPAx P\_DIn (read only) | 53 | 0 | 2 | 2 | 0 | in use |
| [PLC/MSG\_CSPath2Hex](plc/msg-cspath2hex.md) | | 4 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FB\_AlgSolCtrl](plc/fb-algsolctrl.md) | | 9 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_DescList](plc/p-desclist.md) | | 2 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_Intlk](plc/p-intlk.md) | PlantPAx P\_Intlk (read only) | 50 | 0 | 0 | 0 | 0 | in use |
| [PLC/P\_PIDE\_only](plc/p-pide-only.md) | | 2 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Ethernet\_Message\_Config](plc/ethernet-message-config.md) | | 0 | 4 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/udtFaultRecord](plc/udtfaultrecord.md) | | 12 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_Mode](plc/p-mode.md) | | 32 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Comp\_Sequence](plc/comp-sequence.md) | Controller Comp\_Sequence (read only) | 44 | 0 | 0 | 10 | 0 | in use |
| [PLC/FB\_2SpUpDownSeqr](plc/fb-2spupdownseqr.md) | Controller FB\_2SpUpDownSeqr (read only) | 23 | 0 | 0 | 2 | 0 | in use |
| [PLC/QHD\_CompWrite](plc/qhd-compwrite.md) | | 16 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Alarm\_System](plc/alarm-system.md) | | 14 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FBD\_BOOLEAN\_AND](plc/fbd-boolean-and.md) | | 0 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_Gate](plc/p-gate.md) | | 12 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_DOut](plc/p-dout.md) | | 173 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_RunTime](plc/p-runtime.md) | PlantPAx P\_RunTime (read only) | 11 | 0 | 0 | 3 | 0 | in use |
| [PLC/CONTROL](plc/control.md) | | 10 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Recirculator](plc/recirculator.md) | | 15 | 9 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_Motor](plc/p-motor.md) | PlantPAx P\_Motor (read only) | 109 | 0 | 4 | 3 | 0 | in use |
| [PLC/QHD\_CompComms](plc/qhd-compcomms.md) | | 358 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_ValveSO](plc/p-valveso.md) | PlantPAx P\_ValveSO (read only) | 151 | 0 | 4 | 4 | 0 | in use |
| [PLC/QHD\_CompRead](plc/qhd-compread.md) | | 23 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/MakeUp\_Water](plc/makeup-water.md) | | 11 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FBD\_BOOLEAN\_OR](plc/fbd-boolean-or.md) | | 0 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FB\_SeqToRun](plc/fb-seqtorun.md) | | 10 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_Alarm](plc/p-alarm.md) | | 46 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Controller\_Device](plc/controller-device.md) | | 44 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FB\_DuplexAlternator](plc/fb-duplexalternator.md) | | 17 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/P\_PIDE](plc/p-pide.md) | | 311 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Screw\_Compressor](plc/screw-compressor.md) | Controller Screw\_Compressor (read only) | 63 | 0 | 4 | 21 | 0 | in use |
| [PLC/Liquid\_Transfer\_Unit](plc/liquid-transfer-unit.md) | | 4 | 3 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/DateTime\_Type](plc/datetime-type.md) | | 7 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/Dynamic\_Message\_Path](plc/dynamic-message-path.md) | | 6 | 0 | 0 | 0 | 0 | unused (raw L5K import) |
| [PLC/FB\_DayOfWeek](plc/fb-dayofweek.md) | | 3 | 0 | 0 | 0 | 0 | unused (raw L5K import) |

## PLC/Controllers
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [PLC/Controllers/CompactLogix\_5370](plc-controllers/compactlogix-5370.md) | CompactLogix 5370 L3 controller base (read only) | 21 | 0 | 5 | 0 | 0 | in use |

## PLC/Modules
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [PLC/Modules/\_Discrete16In](plc-modules/discrete16in.md) | 1769 16-point discrete input base (read only) | 7 | 0 | 1 | 0 | 0 | in use |
| [PLC/Modules/\_Discrete16Out](plc-modules/discrete16out.md) | 1769 16-point discrete output base (read only) | 8 | 0 | 1 | 0 | 0 | in use |
| [PLC/Modules/1769\_IA16](plc-modules/type-1769-ia16.md) | 1769-IA16 16-Point 120V AC Input (read only) | 4 | 0 | 0 | 0 | 0 | in use |
| [PLC/Modules/1769\_IF8](plc-modules/type-1769-if8.md) | 1769-IF8 8-Channel Analog Input (0-5 V / 4-20 mA) (read only) | 98 | 0 | 1 | 0 | 0 | in use |
| [PLC/Modules/1769\_IQ16](plc-modules/type-1769-iq16.md) | 1769-IQ16 16-Point 24V DC Sink / Source Input (read only) | 4 | 0 | 0 | 0 | 0 | in use |
| [PLC/Modules/1769\_OA16](plc-modules/type-1769-oa16.md) | 1769-OA16 16-Point 120/240V AC Triac Output (read only) | 4 | 0 | 0 | 0 | 0 | in use |
| [PLC/Modules/1769\_OW16](plc-modules/type-1769-ow16.md) | 1769-OW16 16-Point AC/DC Relay Output (read only) | 4 | 0 | 0 | 0 | 0 | in use |

## PLC/Sites
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [PLC/Sites/BH\_Groveport\_RCP1](plc-sites/bh-groveport-rcp1.md) | Groveport RCP1 PLC (CompactLogix 5370, 19 local 1769 cards, read only) | 9 | 19 | 0 | 0 | 1 | in use |

## PLC\_Ref
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [PLC\_Ref/P\_AIn](plc-ref/p-ain.md) | PlantPAx P\_AIn reference (read only) | 179 | 0 | 0 | 0 | 0 | in use |

## Units
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [Units/AHU](units/ahu.md) | ahu | 0 | 4 | 0 | 0 | 0 | no instances |

## \_PlcWriteLockTest
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [\_PlcWriteLockTest/TestCard](plcwritelocktest/testcard.md) | PLC write lock test UDT: memory members whose readOnly the TEST boolean drives at the def… | 3 | 0 | 0 | 0 | 1 | in use |

## \_Root
| UDT | Description | Atomic | Nested UDTs | Alarms | Historized | Direct instances | Status |
|---|---|---|---|---|---|---|---|
| [\_Root/Multistate](root/multistate.md) | multistate | 1 | 0 | 0 | 1 | 0 | no instances |
| [\_Root/Digital](root/digital.md) | digital | 1 | 0 | 0 | 1 | 8 | in use |
| [\_Root/Document](root/document.md) | analog | 1 | 0 | 0 | 0 | 0 | in use |
| [\_Root/Expression](root/expression.md) | | 2 | 0 | 0 | 0 | 0 | in use |
| [\_Root/Analog](root/analog.md) | analog | 1 | 0 | 0 | 1 | 0 | in use |
| [\_Root/String](root/string.md) | string | 1 | 0 | 0 | 1 | 0 | in use |
