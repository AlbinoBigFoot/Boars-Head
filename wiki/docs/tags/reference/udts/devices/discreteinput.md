---
title: "Devices/DiscreteInput"
sidebar_label: "DiscreteInput"
description: "UDT definition Devices/DiscreteInput: discrete input"
generated: true
---

:::note

:::
# UDT `Devices/DiscreteInput`

discrete input

PlantPAx P\_DIn discrete input (FT (RA-BAS) P\_DIn-Faceplate)

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; Devices &gt; DiscreteInput |
| Tag path | `[default]_types_/Devices/DiscreteInput` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 1 (0 atomic, 1 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `PlcDevice` | String | - | own |
| `DInTag` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## Structure

```mermaid
flowchart LR
  n0["Devices/DiscreteInput"]
  style n0 stroke-width:3px
  n0 -- "DIn" --> n1["PLC/P_DIn"]
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `DIn` | UDT | nested [PLC/P\_DIn](../plc/p-din.md) | | | | | | Live PLC object \[\{PlcDevice\}\]\{DInTag\} (PLC/P\_DIn); enabled on mapped instances only |

## Nested UDTs

| Member | Type | Parameter bindings | Default state |
|---|---|---|---|
| `DIn` | [PLC/P\_DIn](../plc/p-din.md) | `DeviceName = {PlcDevice}; TagPrefix = {DInTag}` | disabled |

`disabled` parts subscribe nothing until an instance enables them (instance override `enabled: true`). See the device instance pages for which instances enable which part.

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/LTU](ltu.md) (as `Input`)

52 direct instances.

<details>
<summary>Show the 52 instances</summary>

| Instance | Instance page |
|---|---|
| `[default]Boars_Head/GrovePort/Club/Detectors/AD03` | [Club/Detectors](../../devices/club-detectors.md) |
| `[default]Boars_Head/GrovePort/Condensers/LevelSwitches/RS-LVL-OL2` | [Condensers/LevelSwitches](../../devices/condensers-levelswitches.md) |
| `[default]Boars_Head/GrovePort/Condensers/LevelSwitches/RS-LVL-OL3` | [Condensers/LevelSwitches](../../devices/condensers-levelswitches.md) |
| `[default]Boars_Head/GrovePort/Condensers/LevelSwitches/RS-LLCO2` | [Condensers/LevelSwitches](../../devices/condensers-levelswitches.md) |
| `[default]Boars_Head/GrovePort/Dock/Detectors/FD05` | [Dock/Detectors](../../devices/dock-detectors.md) |
| `[default]Boars_Head/GrovePort/Dock/Detectors/AD08` | [Dock/Detectors](../../devices/dock-detectors.md) |
| `[default]Boars_Head/GrovePort/Dock/Detectors/AD07` | [Dock/Detectors](../../devices/dock-detectors.md) |
| `[default]Boars_Head/GrovePort/East PH/Detectors/AD05` | [East PH/Detectors](../../devices/east-ph-detectors.md) |
| `[default]Boars_Head/GrovePort/East PH/Detectors/FD04` | [East PH/Detectors](../../devices/east-ph-detectors.md) |
| `[default]Boars_Head/GrovePort/Freezer/Detectors/FD01` | [Freezer/Detectors](../../devices/freezer-detectors.md) |
| `[default]Boars_Head/GrovePort/Freezer/Detectors/AD01` | [Freezer/Detectors](../../devices/freezer-detectors.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Detectors/VL-AD` | [Machine Room/Detectors](../../devices/machine-room-detectors.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Detectors/MR-AD1` | [Machine Room/Detectors](../../devices/machine-room-detectors.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Detectors/MASTER-AD1` | [Machine Room/Detectors](../../devices/machine-room-detectors.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS01 EC1A-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS02 EC1A-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS03 EC1B-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS04 EC1B-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS05 COMP-1-SEPR-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS06 COMP-1-SEPR-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS07 COMP-1-TSYPHON` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS08 COMP-2-SEPR-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS09 COMP-2-SEPR-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS10 COMP-2-TSYPHON` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS14 COMP-4-SEPR-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS15 COMP-4-SEPR-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS16 COMP-4-TSYPHON` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS17 COMP-5-SEPR-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS18 COMP-5-SEPR-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS19 COMP-5-TSYPHON` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS20 COMP-6-SEPR-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS21 COMP-6-SEPR-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS22 COMP-6-TSYPHON` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS23 COMP-7-SEPR-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS24 COMP-7-SEPR-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS25 COMP-7-TSYPHON` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS26 TSYPON-VESSEL-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS27 TSYPON-VESSEL-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS28 LTR-VESSEL-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS29 LTR-VESSEL-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS30 LTR-OIL POT` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS31 HTR-VESSEL-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS32 HTR-VESSEL-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS33 HTR-VESSEL-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS34 HTR-OIL POT` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS35 PURGER` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS36 HPR-1` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/PS37 HPR-2` | [Machine Room/RuptureDisks](../../devices/machine-room-rupturedisks.md) |
| `[default]Boars_Head/GrovePort/Palletizing/Detectors/AD04` | [Palletizing/Detectors](../../devices/palletizing-detectors.md) |
| `[default]Boars_Head/GrovePort/SuperChill/Detectors/AD02` | [SuperChill/Detectors](../../devices/superchill-detectors.md) |
| `[default]Boars_Head/GrovePort/West PH/Detectors/FD03` | [West PH/Detectors](../../devices/west-ph-detectors.md) |
| `[default]Boars_Head/GrovePort/West PH/Detectors/AD06` | [West PH/Detectors](../../devices/west-ph-detectors.md) |

</details>
