---
title: "Freezer / Sensors (Instances)"
sidebar_label: "Freezer / Sensors"
description: "Device instances in [default]Boars_Head/GrovePort/Freezer/Sensors: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Freezer/Sensors`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Freezer &gt; Sensors**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Freezer/Sensors/udts.json`. 1 UDT instance(s): 1 x [Devices/Sensor](../udts/devices/sensor.md).

## Underfloor Temp

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp` |
| Type | [Devices/Sensor](../udts/devices/sensor.md) |
| Label | Freezer Underfloor Temp |
| Description | sensor. Live PLC \[RCP1\] (read only): AInTag=TS\_UF2, AInEU=°F. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `AInTag` | `TS_UF2` |
| `AInEU` | `°F` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `AIn` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]TS_UF2` | 174 tags |
| `AInRef` | [PLC\_Ref/P\_AIn](../udts/plc-ref/p-ain.md) | no | reference to `(empty)` | |

