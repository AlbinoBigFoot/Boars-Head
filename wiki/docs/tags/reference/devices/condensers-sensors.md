---
title: "Condensers / Sensors (Instances)"
sidebar_label: "Condensers / Sensors"
description: "Device instances in [default]Boars_Head/GrovePort/Condensers/Sensors: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Condensers/Sensors`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Condensers &gt; Sensors**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Condensers/Sensors/udts.json`. 1 UDT instance(s): 1 x [Devices/Sensor](../udts/devices/sensor.md).

## Outside Air Temp

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp` |
| Type | [Devices/Sensor](../udts/devices/sensor.md) |
| Label | Outside Air Temp |
| Description | sensor. Live PLC \[RCP1\] (read only): AInTag=TS\_AIR, AInEU=°F. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `AInTag` | `TS_AIR` |
| `AInEU` | `°F` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `AIn` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]TS_AIR` | 174 tags |
| `AInRef` | [PLC\_Ref/P\_AIn](../udts/plc-ref/p-ain.md) | no | reference to `(empty)` | |

