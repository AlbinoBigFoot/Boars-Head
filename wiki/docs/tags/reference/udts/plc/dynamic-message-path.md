---
title: "PLC/Dynamic_Message_Path"
sidebar_label: "Dynamic_Message_Path"
description: "UDT definition PLC/Dynamic_Message_Path"
generated: true
---

:::note

:::
# UDT `PLC/Dynamic_Message_Path`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Dynamic\_Message\_Path |
| Tag path | `[default]_types_/PLC/Dynamic_Message_Path` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 6 (6 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

6 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `CS_Path` | String | OPC `{TagPrefix}.CS_Path` | | yes | | | | |
| `HEX_Path` | String | OPC `{TagPrefix}.HEX_Path` | | yes | | | | |
| `IP1` | String | OPC `{TagPrefix}.IP1` | | yes | | | | |
| `IP2` | String | OPC `{TagPrefix}.IP2` | | yes | | | | |
| `IP3` | String | OPC `{TagPrefix}.IP3` | | yes | | | | |
| `IP4` | String | OPC `{TagPrefix}.IP4` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
