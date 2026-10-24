---
title: "Units/AHU"
sidebar_label: "AHU"
description: "UDT definition Units/AHU: ahu"
generated: true
---

:::note

:::
# UDT `Units/AHU`

ahu

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; Units &gt; AHU |
| Tag path | `[default]_types_/Units/AHU` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Units/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 4 (0 atomic, 4 nested UDT, 0 folders) |
| Status | no instances |

## Parameters

_No parameters._

## Structure

```mermaid
flowchart LR
  n0["Units/AHU"]
  style n0 stroke-width:3px
  n0 -- "Status" --> n1["_Root/Multistate"]
  n0 -- "SummaryInstances" --> n2["_Root/Expression"]
  n0 -- "Temp" --> n3["_Root/Analog"]
  n0 -- "_Alarms" --> n4["Config/_Alarms"]
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Status` | UDT | nested [\_Root/Multistate](../root/multistate.md) | | | | | | |
| `SummaryInstances` | UDT | nested [\_Root/Expression](../root/expression.md) | | | | | | |
| `Temp` | UDT | nested [\_Root/Analog](../root/analog.md) | | | | | | |
| `_Alarms` | UDT | nested [Config/\_Alarms](../config/alarms.md) | | | | | | |

## Nested UDTs

| Member | Type | Parameter bindings | Default state |
|---|---|---|---|
| `Status` | [\_Root/Multistate](../root/multistate.md) | - | enabled |
| `SummaryInstances` | [\_Root/Expression](../root/expression.md) | - | enabled |
| `Temp` | [\_Root/Analog](../root/analog.md) | - | enabled |
| `_Alarms` | [Config/\_Alarms](../config/alarms.md) | - | enabled |

`disabled` parts subscribe nothing until an instance enables them (instance override `enabled: true`). See the device instance pages for which instances enable which part.

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT.
