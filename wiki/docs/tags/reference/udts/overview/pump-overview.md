---
title: "Overview/Pump Overview"
sidebar_label: "Pump Overview"
description: "UDT definition Overview/Pump Overview: pump overview"
generated: true
---

:::note

:::
# UDT `Overview/Pump Overview`

pump overview

pump overview instances table

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; Overview &gt; Pump Overview |
| Tag path | `[default]_types_/Overview/Pump Overview` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Overview/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 4 (1 atomic, 3 nested UDT, 0 folders) |
| Status | in use |

## Parameters

_No parameters._

## Structure

```mermaid
flowchart LR
  n0["Overview/Pump Overview"]
  style n0 stroke-width:3px
  n0 -- "DeviceCount" --> n1["_Root/Expression"]
  n0 -- "ActiveAlarmCount" --> n2["_Root/Expression"]
  n0 -- "Instances" --> n3["_Root/Document"]
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `DeviceCount` | UDT | nested [\_Root/Expression](../root/expression.md) | | | | | | |
| `ActiveAlarmCount` | UDT | nested [\_Root/Expression](../root/expression.md) | | | | | | |
| `Instances` | UDT | nested [\_Root/Document](../root/document.md) | | | | | | overview table columns + data (Lightspeed pattern) |
| `Rebuild` | Boolean | memory = `False` | | | | | | |

## Nested UDTs

| Member | Type | Parameter bindings | Default state |
|---|---|---|---|
| `DeviceCount` | [\_Root/Expression](../root/expression.md) | - | enabled |
| `ActiveAlarmCount` | [\_Root/Expression](../root/expression.md) | `exprFunction = sum; exprTargetPath = /_Alarms/_Active` | enabled |
| `Instances` | [\_Root/Document](../root/document.md) | - | enabled |

`disabled` parts subscribe nothing until an instance enables them (instance override `enabled: true`). See the device instance pages for which instances enable which part.

## Alarms

_No alarms defined on this type._

## Used By

1 direct instance(s):

| Instance | Instance page |
|---|---|
| `[default]Boars_Head/GrovePort/Machine Room/Pumps/Overview` | [Machine Room/Pumps](../../devices/machine-room-pumps.md) |
