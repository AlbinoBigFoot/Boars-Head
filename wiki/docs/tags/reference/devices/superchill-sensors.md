---
title: "SuperChill / Sensors (Instances)"
sidebar_label: "SuperChill / Sensors"
description: "Device instances in [default]Boars_Head/GrovePort/SuperChill/Sensors: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/SuperChill/Sensors`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; SuperChill &gt; Sensors**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/SuperChill/Sensors/udts.json`. 1 UDT instance(s): 1 x [Devices/Sensor](../udts/devices/sensor.md).

## Underfloor Temp

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/SuperChill/Sensors/Underfloor Temp` |
| Type | [Devices/Sensor](../udts/devices/sensor.md) |
| Label | Superchill Underfloor Temp |
| Description | sensor. Live PLC \[RCP1\] (read only): AInTag=TS\_UF1, AInEU=°F. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `AInTag` | `TS_UF1` |
| `AInEU` | `°F` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `AIn` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]TS_UF1` | 174 tags |
| `AInRef` | [PLC\_Ref/P\_AIn](../udts/plc-ref/p-ain.md) | no | reference to `(empty)` | |

