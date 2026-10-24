---
title: "Machine Room / Sequences (Instances)"
sidebar_label: "Machine Room / Sequences"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/Sequences: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/Sequences`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; Sequences**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/Sequences/udts.json`. 2 UDT instance(s): 2 x [Devices/SuctionSequence](../udts/devices/suctionsequence.md).

## HSS

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Sequences/HSS` |
| Type | [Devices/SuctionSequence](../udts/devices/suctionsequence.md) |
| Label | High Stage Suction |
| Description | suctionsequence. Live PLC \[RCP1\] (read only): SeqTag=HSS. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `SeqTag` | `HSS` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Seq` | [PLC/Comp\_Sequence](../udts/plc/comp-sequence.md) | yes | `[RCP1]HSS` | 62 tags |
| `PlcHmiEnable` | OPC atomic | yes | `ns=1;s=[RCP1]` | |

## LSS

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Sequences/LSS` |
| Type | [Devices/SuctionSequence](../udts/devices/suctionsequence.md) |
| Label | Low Stage Suction |
| Description | suctionsequence. Live PLC \[RCP1\] (read only): SeqTag=LSS, EnableTag=LSS\_HMI\_Enable. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `SeqTag` | `LSS` |
| `EnableTag` | `LSS_HMI_Enable` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Seq` | [PLC/Comp\_Sequence](../udts/plc/comp-sequence.md) | yes | `[RCP1]LSS` | 62 tags |
| `PlcHmiEnable` | OPC atomic | yes | `ns=1;s=[RCP1]LSS_HMI_Enable` | 1 tags |

