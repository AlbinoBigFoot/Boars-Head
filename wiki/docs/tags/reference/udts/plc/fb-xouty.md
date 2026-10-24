---
title: "PLC/FB_XoutY"
sidebar_label: "FB_XoutY"
description: "UDT definition PLC/FB_XoutY"
generated: true
---

:::note

:::
# UDT `PLC/FB_XoutY`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; FB\_XoutY |
| Tag path | `[default]_types_/PLC/FB_XoutY` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 22 (22 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

22 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `In1` | Boolean | OPC `{TagPrefix}.In1` | | yes | | | | |
| `In2` | Boolean | OPC `{TagPrefix}.In2` | | yes | | | | |
| `In3` | Boolean | OPC `{TagPrefix}.In3` | | yes | | | | |
| `In4` | Boolean | OPC `{TagPrefix}.In4` | | yes | | | | |
| `In5` | Boolean | OPC `{TagPrefix}.In5` | | yes | | | | |
| `In6` | Boolean | OPC `{TagPrefix}.In6` | | yes | | | | |
| `In7` | Boolean | OPC `{TagPrefix}.In7` | | yes | | | | |
| `In8` | Boolean | OPC `{TagPrefix}.In8` | | yes | | | | |
| `In9` | Boolean | OPC `{TagPrefix}.In9` | | yes | | | | |
| `In10` | Boolean | OPC `{TagPrefix}.In10` | | yes | | | | |
| `In11` | Boolean | OPC `{TagPrefix}.In11` | | yes | | | | |
| `In12` | Boolean | OPC `{TagPrefix}.In12` | | yes | | | | |
| `In13` | Boolean | OPC `{TagPrefix}.In13` | | yes | | | | |
| `In14` | Boolean | OPC `{TagPrefix}.In14` | | yes | | | | |
| `In15` | Boolean | OPC `{TagPrefix}.In15` | | yes | | | | |
| `In16` | Boolean | OPC `{TagPrefix}.In16` | | yes | | | | |
| `Out` | Boolean | OPC `{TagPrefix}.Out` | | yes | | | | |
| `OutN` | Boolean | OPC `{TagPrefix}.OutN` | | yes | | | | |
| `X` | Int2 | OPC `{TagPrefix}.X` | | yes | | | | |
| `Y` | Int2 | OPC `{TagPrefix}.Y` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
