---
title: "Condensers / Sequences (Instances)"
sidebar_label: "Condensers / Sequences"
description: "Device instances in [default]Boars_Head/GrovePort/Condensers/Sequences: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Condensers/Sequences`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Condensers &gt; Sequences**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Condensers/Sequences/udts.json`. 1 UDT instance(s): 1 x [Devices/DischargeSequence](../udts/devices/dischargesequence.md).

## HSD

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Sequences/HSD` |
| Type | [Devices/DischargeSequence](../udts/devices/dischargesequence.md) |
| Label | High Stage Discharge |
| Description | dischargesequence. Live PLC \[RCP1\] (read only): SeqrTag=HSD\_Seqr, Seq1Tag=HSD\_Sequence\[1\], Seq2Tag=HSD\_Sequence\[2\], Seq3Tag=HSD\_Sequence\[3\], Seq4Tag=HSD\_Sequence\[4\], Seq5Tag=HSD\_Sequence\[5\], Seq6Tag=HSD\_Sequence\[6\], Seq7Tag=HSD\_Sequence\[7\], FixedSPTag=HSD\_Fixed\_SP, FirstNoDelayTag=Cmd\_FirstNoDelay, MainOpenTag=CD\_SUMP\_OPLL\_SET, MainCloseTag=CD\_SUMP\_OPLH\_SET, BackupOpenTag=CD\_SUMP\_OPL1L\_SET, Backu… |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `SeqrTag` | `HSD_Seqr` |
| `Seq1Tag` | `HSD_Sequence[1]` |
| `Seq2Tag` | `HSD_Sequence[2]` |
| `Seq3Tag` | `HSD_Sequence[3]` |
| `Seq4Tag` | `HSD_Sequence[4]` |
| `Seq5Tag` | `HSD_Sequence[5]` |
| `Seq6Tag` | `HSD_Sequence[6]` |
| `Seq7Tag` | `HSD_Sequence[7]` |
| `FixedSPTag` | `HSD_Fixed_SP` |
| `FirstNoDelayTag` | `Cmd_FirstNoDelay` |
| `MainOpenTag` | `CD_SUMP_OPLL_SET` |
| `MainCloseTag` | `CD_SUMP_OPLH_SET` |
| `BackupOpenTag` | `CD_SUMP_OPL1L_SET` |
| `BackupCloseTag` | `CD_SUMP_OPL1H_SET` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Seqr` | [PLC/FB\_2SpUpDownSeqr](../udts/plc/fb-2spupdownseqr.md) | yes | `[RCP1]HSD_Seqr` | 51 tags |
| `PlcSequence1` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Sequence[1]` | 1 tags |
| `PlcSequence2` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Sequence[2]` | 1 tags |
| `PlcSequence3` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Sequence[3]` | 1 tags |
| `PlcSequence4` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Sequence[4]` | 1 tags |
| `PlcSequence5` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Sequence[5]` | 1 tags |
| `PlcSequence6` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Sequence[6]` | 1 tags |
| `PlcSequence7` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Sequence[7]` | 1 tags |
| `PlcFixedSP` | OPC atomic | yes | `ns=1;s=[RCP1]HSD_Fixed_SP` | 1 tags |
| `PlcFirstNoDelay` | OPC atomic | yes | `ns=1;s=[RCP1]Cmd_FirstNoDelay` | 1 tags |
| `PlcMainOpenSP` | OPC atomic | yes | `ns=1;s=[RCP1]CD_SUMP_OPLL_SET` | 1 tags |
| `PlcMainCloseSP` | OPC atomic | yes | `ns=1;s=[RCP1]CD_SUMP_OPLH_SET` | 1 tags |
| `PlcBackupOpenSP` | OPC atomic | yes | `ns=1;s=[RCP1]CD_SUMP_OPL1L_SET` | 1 tags |
| `PlcBackupCloseSP` | OPC atomic | yes | `ns=1;s=[RCP1]CD_SUMP_OPL1H_SET` | 1 tags |

