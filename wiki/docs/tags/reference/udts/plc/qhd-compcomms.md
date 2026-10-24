---
title: "PLC/QHD_CompComms"
sidebar_label: "QHD_CompComms"
description: "UDT definition PLC/QHD_CompComms"
generated: true
---

:::note

:::
# UDT `PLC/QHD_CompComms`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; QHD\_CompComms |
| Tag path | `[default]_types_/PLC/QHD_CompComms` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 361 (358 atomic, 0 nested UDT, 3 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `(text, 64 chars)` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

358 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `CommArrayHP1/` | Folder | | | | | | | |
| `CommArrayHP1/108` | Int2 | OPC `{TagPrefix}.CommArrayHP1[108]` | | yes | | | | temporary data array |
| `CommArrayHP1/29` | Int2 | OPC `{TagPrefix}.CommArrayHP1[29]` | | yes | | | | temporary data array |
| `CommArrayHP1/8` | Int2 | OPC `{TagPrefix}.CommArrayHP1[8]` | | yes | | | | temporary data array |
| `CommArrayHP1/110` | Int2 | OPC `{TagPrefix}.CommArrayHP1[110]` | | yes | | | | temporary data array |
| `CommArrayHP1/56` | Int2 | OPC `{TagPrefix}.CommArrayHP1[56]` | | yes | | | | temporary data array |
| `CommArrayHP1/35` | Int2 | OPC `{TagPrefix}.CommArrayHP1[35]` | | yes | | | | temporary data array |
| `CommArrayHP1/34` | Int2 | OPC `{TagPrefix}.CommArrayHP1[34]` | | yes | | | | temporary data array |
| `CommArrayHP1/104` | Int2 | OPC `{TagPrefix}.CommArrayHP1[104]` | | yes | | | | temporary data array |
| `CommArrayHP1/39` | Int2 | OPC `{TagPrefix}.CommArrayHP1[39]` | | yes | | | | temporary data array |
| `CommArrayHP1/51` | Int2 | OPC `{TagPrefix}.CommArrayHP1[51]` | | yes | | | | temporary data array |
| `CommArrayHP1/13` | Int2 | OPC `{TagPrefix}.CommArrayHP1[13]` | | yes | | | | temporary data array |
| `CommArrayHP1/73` | Int2 | OPC `{TagPrefix}.CommArrayHP1[73]` | | yes | | | | temporary data array |
| `CommArrayHP1/4` | Int2 | OPC `{TagPrefix}.CommArrayHP1[4]` | | yes | | | | temporary data array |
| `CommArrayHP1/75` | Int2 | OPC `{TagPrefix}.CommArrayHP1[75]` | | yes | | | | temporary data array |
| `CommArrayHP1/19` | Int2 | OPC `{TagPrefix}.CommArrayHP1[19]` | | yes | | | | temporary data array |
| `CommArrayHP1/98` | Int2 | OPC `{TagPrefix}.CommArrayHP1[98]` | | yes | | | | temporary data array |
| `CommArrayHP1/22` | Int2 | OPC `{TagPrefix}.CommArrayHP1[22]` | | yes | | | | temporary data array |
| `CommArrayHP1/1` | Int2 | OPC `{TagPrefix}.CommArrayHP1[1]` | | yes | | | | temporary data array |
| `CommArrayHP1/62` | Int2 | OPC `{TagPrefix}.CommArrayHP1[62]` | | yes | | | | temporary data array |
| `CommArrayHP1/6` | Int2 | OPC `{TagPrefix}.CommArrayHP1[6]` | | yes | | | | temporary data array |
| `CommArrayHP1/66` | Int2 | OPC `{TagPrefix}.CommArrayHP1[66]` | | yes | | | | temporary data array |
| `CommArrayHP1/63` | Int2 | OPC `{TagPrefix}.CommArrayHP1[63]` | | yes | | | | temporary data array |
| `CommArrayHP1/9` | Int2 | OPC `{TagPrefix}.CommArrayHP1[9]` | | yes | | | | temporary data array |
| `CommArrayHP1/47` | Int2 | OPC `{TagPrefix}.CommArrayHP1[47]` | | yes | | | | temporary data array |
| `CommArrayHP1/100` | Int2 | OPC `{TagPrefix}.CommArrayHP1[100]` | | yes | | | | temporary data array |
| `CommArrayHP1/91` | Int2 | OPC `{TagPrefix}.CommArrayHP1[91]` | | yes | | | | temporary data array |
| `CommArrayHP1/5` | Int2 | OPC `{TagPrefix}.CommArrayHP1[5]` | | yes | | | | temporary data array |
| `CommArrayHP1/17` | Int2 | OPC `{TagPrefix}.CommArrayHP1[17]` | | yes | | | | temporary data array |
| `CommArrayHP1/102` | Int2 | OPC `{TagPrefix}.CommArrayHP1[102]` | | yes | | | | temporary data array |
| `CommArrayHP1/86` | Int2 | OPC `{TagPrefix}.CommArrayHP1[86]` | | yes | | | | temporary data array |
| `CommArrayHP1/42` | Int2 | OPC `{TagPrefix}.CommArrayHP1[42]` | | yes | | | | temporary data array |
| `CommArrayHP1/38` | Int2 | OPC `{TagPrefix}.CommArrayHP1[38]` | | yes | | | | temporary data array |
| `CommArrayHP1/60` | Int2 | OPC `{TagPrefix}.CommArrayHP1[60]` | | yes | | | | temporary data array |
| `CommArrayHP1/64` | Int2 | OPC `{TagPrefix}.CommArrayHP1[64]` | | yes | | | | temporary data array |
| `CommArrayHP1/52` | Int2 | OPC `{TagPrefix}.CommArrayHP1[52]` | | yes | | | | temporary data array |
| `CommArrayHP1/21` | Int2 | OPC `{TagPrefix}.CommArrayHP1[21]` | | yes | | | | temporary data array |
| `CommArrayHP1/30` | Int2 | OPC `{TagPrefix}.CommArrayHP1[30]` | | yes | | | | temporary data array |
| `CommArrayHP1/111` | Int2 | OPC `{TagPrefix}.CommArrayHP1[111]` | | yes | | | | temporary data array |
| `CommArrayHP1/46` | Int2 | OPC `{TagPrefix}.CommArrayHP1[46]` | | yes | | | | temporary data array |
| `CommArrayHP1/10` | Int2 | OPC `{TagPrefix}.CommArrayHP1[10]` | | yes | | | | temporary data array |
| `CommArrayHP1/79` | Int2 | OPC `{TagPrefix}.CommArrayHP1[79]` | | yes | | | | temporary data array |
| `CommArrayHP1/54` | Int2 | OPC `{TagPrefix}.CommArrayHP1[54]` | | yes | | | | temporary data array |
| `CommArrayHP1/28` | Int2 | OPC `{TagPrefix}.CommArrayHP1[28]` | | yes | | | | temporary data array |
| `CommArrayHP1/94` | Int2 | OPC `{TagPrefix}.CommArrayHP1[94]` | | yes | | | | temporary data array |
| `CommArrayHP1/103` | Int2 | OPC `{TagPrefix}.CommArrayHP1[103]` | | yes | | | | temporary data array |
| `CommArrayHP1/74` | Int2 | OPC `{TagPrefix}.CommArrayHP1[74]` | | yes | | | | temporary data array |
| `CommArrayHP1/99` | Int2 | OPC `{TagPrefix}.CommArrayHP1[99]` | | yes | | | | temporary data array |
| `CommArrayHP1/14` | Int2 | OPC `{TagPrefix}.CommArrayHP1[14]` | | yes | | | | temporary data array |
| `CommArrayHP1/67` | Int2 | OPC `{TagPrefix}.CommArrayHP1[67]` | | yes | | | | temporary data array |
| `CommArrayHP1/106` | Int2 | OPC `{TagPrefix}.CommArrayHP1[106]` | | yes | | | | temporary data array |
| `CommArrayHP1/53` | Int2 | OPC `{TagPrefix}.CommArrayHP1[53]` | | yes | | | | temporary data array |
| `CommArrayHP1/48` | Int2 | OPC `{TagPrefix}.CommArrayHP1[48]` | | yes | | | | temporary data array |
| `CommArrayHP1/15` | Int2 | OPC `{TagPrefix}.CommArrayHP1[15]` | | yes | | | | temporary data array |
| `CommArrayHP1/112` | Int2 | OPC `{TagPrefix}.CommArrayHP1[112]` | | yes | | | | temporary data array |
| `CommArrayHP1/31` | Int2 | OPC `{TagPrefix}.CommArrayHP1[31]` | | yes | | | | temporary data array |
| `CommArrayHP1/32` | Int2 | OPC `{TagPrefix}.CommArrayHP1[32]` | | yes | | | | temporary data array |
| `CommArrayHP1/24` | Int2 | OPC `{TagPrefix}.CommArrayHP1[24]` | | yes | | | | temporary data array |
| `CommArrayHP1/78` | Int2 | OPC `{TagPrefix}.CommArrayHP1[78]` | | yes | | | | temporary data array |
| `CommArrayHP1/83` | Int2 | OPC `{TagPrefix}.CommArrayHP1[83]` | | yes | | | | temporary data array |
| `CommArrayHP1/85` | Int2 | OPC `{TagPrefix}.CommArrayHP1[85]` | | yes | | | | temporary data array |
| `CommArrayHP1/37` | Int2 | OPC `{TagPrefix}.CommArrayHP1[37]` | | yes | | | | temporary data array |
| `CommArrayHP1/92` | Int2 | OPC `{TagPrefix}.CommArrayHP1[92]` | | yes | | | | temporary data array |
| `CommArrayHP1/107` | Int2 | OPC `{TagPrefix}.CommArrayHP1[107]` | | yes | | | | temporary data array |
| `CommArrayHP1/97` | Int2 | OPC `{TagPrefix}.CommArrayHP1[97]` | | yes | | | | temporary data array |
| `CommArrayHP1/11` | Int2 | OPC `{TagPrefix}.CommArrayHP1[11]` | | yes | | | | temporary data array |
| `CommArrayHP1/16` | Int2 | OPC `{TagPrefix}.CommArrayHP1[16]` | | yes | | | | temporary data array |
| `CommArrayHP1/84` | Int2 | OPC `{TagPrefix}.CommArrayHP1[84]` | | yes | | | | temporary data array |
| `CommArrayHP1/41` | Int2 | OPC `{TagPrefix}.CommArrayHP1[41]` | | yes | | | | temporary data array |
| `CommArrayHP1/114` | Int2 | OPC `{TagPrefix}.CommArrayHP1[114]` | | yes | | | | temporary data array |
| `CommArrayHP1/113` | Int2 | OPC `{TagPrefix}.CommArrayHP1[113]` | | yes | | | | temporary data array |
| `CommArrayHP1/81` | Int2 | OPC `{TagPrefix}.CommArrayHP1[81]` | | yes | | | | temporary data array |
| `CommArrayHP1/40` | Int2 | OPC `{TagPrefix}.CommArrayHP1[40]` | | yes | | | | temporary data array |
| `CommArrayHP1/71` | Int2 | OPC `{TagPrefix}.CommArrayHP1[71]` | | yes | | | | temporary data array |
| `CommArrayHP1/45` | Int2 | OPC `{TagPrefix}.CommArrayHP1[45]` | | yes | | | | temporary data array |
| `CommArrayHP1/49` | Int2 | OPC `{TagPrefix}.CommArrayHP1[49]` | | yes | | | | temporary data array |
| `CommArrayHP1/12` | Int2 | OPC `{TagPrefix}.CommArrayHP1[12]` | | yes | | | | temporary data array |
| `CommArrayHP1/7` | Int2 | OPC `{TagPrefix}.CommArrayHP1[7]` | | yes | | | | temporary data array |
| `CommArrayHP1/68` | Int2 | OPC `{TagPrefix}.CommArrayHP1[68]` | | yes | | | | temporary data array |
| `CommArrayHP1/18` | Int2 | OPC `{TagPrefix}.CommArrayHP1[18]` | | yes | | | | temporary data array |
| `CommArrayHP1/26` | Int2 | OPC `{TagPrefix}.CommArrayHP1[26]` | | yes | | | | temporary data array |
| `CommArrayHP1/76` | Int2 | OPC `{TagPrefix}.CommArrayHP1[76]` | | yes | | | | temporary data array |
| `CommArrayHP1/95` | Int2 | OPC `{TagPrefix}.CommArrayHP1[95]` | | yes | | | | temporary data array |
| `CommArrayHP1/23` | Int2 | OPC `{TagPrefix}.CommArrayHP1[23]` | | yes | | | | temporary data array |
| `CommArrayHP1/65` | Int2 | OPC `{TagPrefix}.CommArrayHP1[65]` | | yes | | | | temporary data array |
| `CommArrayHP1/116` | Int2 | OPC `{TagPrefix}.CommArrayHP1[116]` | | yes | | | | temporary data array |
| `CommArrayHP1/72` | Int2 | OPC `{TagPrefix}.CommArrayHP1[72]` | | yes | | | | temporary data array |
| `CommArrayHP1/3` | Int2 | OPC `{TagPrefix}.CommArrayHP1[3]` | | yes | | | | temporary data array |
| `CommArrayHP1/36` | Int2 | OPC `{TagPrefix}.CommArrayHP1[36]` | | yes | | | | temporary data array |
| `CommArrayHP1/50` | Int2 | OPC `{TagPrefix}.CommArrayHP1[50]` | | yes | | | | temporary data array |
| `CommArrayHP1/58` | Int2 | OPC `{TagPrefix}.CommArrayHP1[58]` | | yes | | | | temporary data array |
| `CommArrayHP1/20` | Int2 | OPC `{TagPrefix}.CommArrayHP1[20]` | | yes | | | | temporary data array |
| `CommArrayHP1/33` | Int2 | OPC `{TagPrefix}.CommArrayHP1[33]` | | yes | | | | temporary data array |
| `CommArrayHP1/87` | Int2 | OPC `{TagPrefix}.CommArrayHP1[87]` | | yes | | | | temporary data array |
| `CommArrayHP1/2` | Int2 | OPC `{TagPrefix}.CommArrayHP1[2]` | | yes | | | | temporary data array |
| `CommArrayHP1/96` | Int2 | OPC `{TagPrefix}.CommArrayHP1[96]` | | yes | | | | temporary data array |
| `CommArrayHP1/69` | Int2 | OPC `{TagPrefix}.CommArrayHP1[69]` | | yes | | | | temporary data array |
| `CommArrayHP1/77` | Int2 | OPC `{TagPrefix}.CommArrayHP1[77]` | | yes | | | | temporary data array |
| `CommArrayHP1/109` | Int2 | OPC `{TagPrefix}.CommArrayHP1[109]` | | yes | | | | temporary data array |
| `CommArrayHP1/70` | Int2 | OPC `{TagPrefix}.CommArrayHP1[70]` | | yes | | | | temporary data array |
| `CommArrayHP1/89` | Int2 | OPC `{TagPrefix}.CommArrayHP1[89]` | | yes | | | | temporary data array |
| `CommArrayHP1/101` | Int2 | OPC `{TagPrefix}.CommArrayHP1[101]` | | yes | | | | temporary data array |
| `CommArrayHP1/27` | Int2 | OPC `{TagPrefix}.CommArrayHP1[27]` | | yes | | | | temporary data array |
| `CommArrayHP1/44` | Int2 | OPC `{TagPrefix}.CommArrayHP1[44]` | | yes | | | | temporary data array |
| `CommArrayHP1/88` | Int2 | OPC `{TagPrefix}.CommArrayHP1[88]` | | yes | | | | temporary data array |
| `CommArrayHP1/105` | Int2 | OPC `{TagPrefix}.CommArrayHP1[105]` | | yes | | | | temporary data array |
| `CommArrayHP1/0` | Int2 | OPC `{TagPrefix}.CommArrayHP1[0]` | | yes | | | | temporary data array |
| `CommArrayHP1/43` | Int2 | OPC `{TagPrefix}.CommArrayHP1[43]` | | yes | | | | temporary data array |
| `CommArrayHP1/115` | Int2 | OPC `{TagPrefix}.CommArrayHP1[115]` | | yes | | | | temporary data array |
| `CommArrayHP1/57` | Int2 | OPC `{TagPrefix}.CommArrayHP1[57]` | | yes | | | | temporary data array |
| `CommArrayHP1/61` | Int2 | OPC `{TagPrefix}.CommArrayHP1[61]` | | yes | | | | temporary data array |
| `CommArrayHP1/90` | Int2 | OPC `{TagPrefix}.CommArrayHP1[90]` | | yes | | | | temporary data array |
| `CommArrayHP1/25` | Int2 | OPC `{TagPrefix}.CommArrayHP1[25]` | | yes | | | | temporary data array |
| `CommArrayHP1/93` | Int2 | OPC `{TagPrefix}.CommArrayHP1[93]` | | yes | | | | temporary data array |
| `CommArrayHP1/82` | Int2 | OPC `{TagPrefix}.CommArrayHP1[82]` | | yes | | | | temporary data array |
| `CommArrayHP1/80` | Int2 | OPC `{TagPrefix}.CommArrayHP1[80]` | | yes | | | | temporary data array |
| `CommArrayHP1/59` | Int2 | OPC `{TagPrefix}.CommArrayHP1[59]` | | yes | | | | temporary data array |
| `CommArrayHP1/55` | Int2 | OPC `{TagPrefix}.CommArrayHP1[55]` | | yes | | | | temporary data array |
| `CommArrayHP2/` | Folder | | | | | | | |
| `CommArrayHP2/28` | Int2 | OPC `{TagPrefix}.CommArrayHP2[28]` | | yes | | | | temporary data array |
| `CommArrayHP2/84` | Int2 | OPC `{TagPrefix}.CommArrayHP2[84]` | | yes | | | | temporary data array |
| `CommArrayHP2/50` | Int2 | OPC `{TagPrefix}.CommArrayHP2[50]` | | yes | | | | temporary data array |
| `CommArrayHP2/58` | Int2 | OPC `{TagPrefix}.CommArrayHP2[58]` | | yes | | | | temporary data array |
| `CommArrayHP2/29` | Int2 | OPC `{TagPrefix}.CommArrayHP2[29]` | | yes | | | | temporary data array |
| `CommArrayHP2/69` | Int2 | OPC `{TagPrefix}.CommArrayHP2[69]` | | yes | | | | temporary data array |
| `CommArrayHP2/73` | Int2 | OPC `{TagPrefix}.CommArrayHP2[73]` | | yes | | | | temporary data array |
| `CommArrayHP2/3` | Int2 | OPC `{TagPrefix}.CommArrayHP2[3]` | | yes | | | | temporary data array |
| `CommArrayHP2/115` | Int2 | OPC `{TagPrefix}.CommArrayHP2[115]` | | yes | | | | temporary data array |
| `CommArrayHP2/65` | Int2 | OPC `{TagPrefix}.CommArrayHP2[65]` | | yes | | | | temporary data array |
| `CommArrayHP2/82` | Int2 | OPC `{TagPrefix}.CommArrayHP2[82]` | | yes | | | | temporary data array |
| `CommArrayHP2/56` | Int2 | OPC `{TagPrefix}.CommArrayHP2[56]` | | yes | | | | temporary data array |
| `CommArrayHP2/15` | Int2 | OPC `{TagPrefix}.CommArrayHP2[15]` | | yes | | | | temporary data array |
| `CommArrayHP2/6` | Int2 | OPC `{TagPrefix}.CommArrayHP2[6]` | | yes | | | | temporary data array |
| `CommArrayHP2/26` | Int2 | OPC `{TagPrefix}.CommArrayHP2[26]` | | yes | | | | temporary data array |
| `CommArrayHP2/68` | Int2 | OPC `{TagPrefix}.CommArrayHP2[68]` | | yes | | | | temporary data array |
| `CommArrayHP2/22` | Int2 | OPC `{TagPrefix}.CommArrayHP2[22]` | | yes | | | | temporary data array |
| `CommArrayHP2/54` | Int2 | OPC `{TagPrefix}.CommArrayHP2[54]` | | yes | | | | temporary data array |
| `CommArrayHP2/91` | Int2 | OPC `{TagPrefix}.CommArrayHP2[91]` | | yes | | | | temporary data array |
| `CommArrayHP2/25` | Int2 | OPC `{TagPrefix}.CommArrayHP2[25]` | | yes | | | | temporary data array |
| `CommArrayHP2/64` | Int2 | OPC `{TagPrefix}.CommArrayHP2[64]` | | yes | | | | temporary data array |
| `CommArrayHP2/13` | Int2 | OPC `{TagPrefix}.CommArrayHP2[13]` | | yes | | | | temporary data array |
| `CommArrayHP2/46` | Int2 | OPC `{TagPrefix}.CommArrayHP2[46]` | | yes | | | | temporary data array |
| `CommArrayHP2/5` | Int2 | OPC `{TagPrefix}.CommArrayHP2[5]` | | yes | | | | temporary data array |
| `CommArrayHP2/104` | Int2 | OPC `{TagPrefix}.CommArrayHP2[104]` | | yes | | | | temporary data array |
| `CommArrayHP2/111` | Int2 | OPC `{TagPrefix}.CommArrayHP2[111]` | | yes | | | | temporary data array |
| `CommArrayHP2/88` | Int2 | OPC `{TagPrefix}.CommArrayHP2[88]` | | yes | | | | temporary data array |
| `CommArrayHP2/40` | Int2 | OPC `{TagPrefix}.CommArrayHP2[40]` | | yes | | | | temporary data array |
| `CommArrayHP2/37` | Int2 | OPC `{TagPrefix}.CommArrayHP2[37]` | | yes | | | | temporary data array |
| `CommArrayHP2/85` | Int2 | OPC `{TagPrefix}.CommArrayHP2[85]` | | yes | | | | temporary data array |
| `CommArrayHP2/9` | Int2 | OPC `{TagPrefix}.CommArrayHP2[9]` | | yes | | | | temporary data array |
| `CommArrayHP2/110` | Int2 | OPC `{TagPrefix}.CommArrayHP2[110]` | | yes | | | | temporary data array |
| `CommArrayHP2/42` | Int2 | OPC `{TagPrefix}.CommArrayHP2[42]` | | yes | | | | temporary data array |
| `CommArrayHP2/57` | Int2 | OPC `{TagPrefix}.CommArrayHP2[57]` | | yes | | | | temporary data array |
| `CommArrayHP2/55` | Int2 | OPC `{TagPrefix}.CommArrayHP2[55]` | | yes | | | | temporary data array |
| `CommArrayHP2/71` | Int2 | OPC `{TagPrefix}.CommArrayHP2[71]` | | yes | | | | temporary data array |
| `CommArrayHP2/92` | Int2 | OPC `{TagPrefix}.CommArrayHP2[92]` | | yes | | | | temporary data array |
| `CommArrayHP2/97` | Int2 | OPC `{TagPrefix}.CommArrayHP2[97]` | | yes | | | | temporary data array |
| `CommArrayHP2/99` | Int2 | OPC `{TagPrefix}.CommArrayHP2[99]` | | yes | | | | temporary data array |
| `CommArrayHP2/49` | Int2 | OPC `{TagPrefix}.CommArrayHP2[49]` | | yes | | | | temporary data array |
| `CommArrayHP2/87` | Int2 | OPC `{TagPrefix}.CommArrayHP2[87]` | | yes | | | | temporary data array |
| `CommArrayHP2/4` | Int2 | OPC `{TagPrefix}.CommArrayHP2[4]` | | yes | | | | temporary data array |
| `CommArrayHP2/81` | Int2 | OPC `{TagPrefix}.CommArrayHP2[81]` | | yes | | | | temporary data array |
| `CommArrayHP2/109` | Int2 | OPC `{TagPrefix}.CommArrayHP2[109]` | | yes | | | | temporary data array |
| `CommArrayHP2/66` | Int2 | OPC `{TagPrefix}.CommArrayHP2[66]` | | yes | | | | temporary data array |
| `CommArrayHP2/80` | Int2 | OPC `{TagPrefix}.CommArrayHP2[80]` | | yes | | | | temporary data array |
| `CommArrayHP2/83` | Int2 | OPC `{TagPrefix}.CommArrayHP2[83]` | | yes | | | | temporary data array |
| `CommArrayHP2/62` | Int2 | OPC `{TagPrefix}.CommArrayHP2[62]` | | yes | | | | temporary data array |
| `CommArrayHP2/8` | Int2 | OPC `{TagPrefix}.CommArrayHP2[8]` | | yes | | | | temporary data array |
| `CommArrayHP2/0` | Int2 | OPC `{TagPrefix}.CommArrayHP2[0]` | | yes | | | | temporary data array |
| `CommArrayHP2/76` | Int2 | OPC `{TagPrefix}.CommArrayHP2[76]` | | yes | | | | temporary data array |
| `CommArrayHP2/79` | Int2 | OPC `{TagPrefix}.CommArrayHP2[79]` | | yes | | | | temporary data array |
| `CommArrayHP2/18` | Int2 | OPC `{TagPrefix}.CommArrayHP2[18]` | | yes | | | | temporary data array |
| `CommArrayHP2/63` | Int2 | OPC `{TagPrefix}.CommArrayHP2[63]` | | yes | | | | temporary data array |
| `CommArrayHP2/105` | Int2 | OPC `{TagPrefix}.CommArrayHP2[105]` | | yes | | | | temporary data array |
| `CommArrayHP2/19` | Int2 | OPC `{TagPrefix}.CommArrayHP2[19]` | | yes | | | | temporary data array |
| `CommArrayHP2/106` | Int2 | OPC `{TagPrefix}.CommArrayHP2[106]` | | yes | | | | temporary data array |
| `CommArrayHP2/108` | Int2 | OPC `{TagPrefix}.CommArrayHP2[108]` | | yes | | | | temporary data array |
| `CommArrayHP2/39` | Int2 | OPC `{TagPrefix}.CommArrayHP2[39]` | | yes | | | | temporary data array |
| `CommArrayHP2/36` | Int2 | OPC `{TagPrefix}.CommArrayHP2[36]` | | yes | | | | temporary data array |
| `CommArrayHP2/21` | Int2 | OPC `{TagPrefix}.CommArrayHP2[21]` | | yes | | | | temporary data array |
| `CommArrayHP2/103` | Int2 | OPC `{TagPrefix}.CommArrayHP2[103]` | | yes | | | | temporary data array |
| `CommArrayHP2/33` | Int2 | OPC `{TagPrefix}.CommArrayHP2[33]` | | yes | | | | temporary data array |
| `CommArrayHP2/32` | Int2 | OPC `{TagPrefix}.CommArrayHP2[32]` | | yes | | | | temporary data array |
| `CommArrayHP2/48` | Int2 | OPC `{TagPrefix}.CommArrayHP2[48]` | | yes | | | | temporary data array |
| `CommArrayHP2/78` | Int2 | OPC `{TagPrefix}.CommArrayHP2[78]` | | yes | | | | temporary data array |
| `CommArrayHP2/60` | Int2 | OPC `{TagPrefix}.CommArrayHP2[60]` | | yes | | | | temporary data array |
| `CommArrayHP2/38` | Int2 | OPC `{TagPrefix}.CommArrayHP2[38]` | | yes | | | | temporary data array |
| `CommArrayHP2/44` | Int2 | OPC `{TagPrefix}.CommArrayHP2[44]` | | yes | | | | temporary data array |
| `CommArrayHP2/51` | Int2 | OPC `{TagPrefix}.CommArrayHP2[51]` | | yes | | | | temporary data array |
| `CommArrayHP2/24` | Int2 | OPC `{TagPrefix}.CommArrayHP2[24]` | | yes | | | | temporary data array |
| `CommArrayHP2/98` | Int2 | OPC `{TagPrefix}.CommArrayHP2[98]` | | yes | | | | temporary data array |
| `CommArrayHP2/67` | Int2 | OPC `{TagPrefix}.CommArrayHP2[67]` | | yes | | | | temporary data array |
| `CommArrayHP2/90` | Int2 | OPC `{TagPrefix}.CommArrayHP2[90]` | | yes | | | | temporary data array |
| `CommArrayHP2/102` | Int2 | OPC `{TagPrefix}.CommArrayHP2[102]` | | yes | | | | temporary data array |
| `CommArrayHP2/47` | Int2 | OPC `{TagPrefix}.CommArrayHP2[47]` | | yes | | | | temporary data array |
| `CommArrayHP2/52` | Int2 | OPC `{TagPrefix}.CommArrayHP2[52]` | | yes | | | | temporary data array |
| `CommArrayHP2/31` | Int2 | OPC `{TagPrefix}.CommArrayHP2[31]` | | yes | | | | temporary data array |
| `CommArrayHP2/89` | Int2 | OPC `{TagPrefix}.CommArrayHP2[89]` | | yes | | | | temporary data array |
| `CommArrayHP2/16` | Int2 | OPC `{TagPrefix}.CommArrayHP2[16]` | | yes | | | | temporary data array |
| `CommArrayHP2/34` | Int2 | OPC `{TagPrefix}.CommArrayHP2[34]` | | yes | | | | temporary data array |
| `CommArrayHP2/70` | Int2 | OPC `{TagPrefix}.CommArrayHP2[70]` | | yes | | | | temporary data array |
| `CommArrayHP2/61` | Int2 | OPC `{TagPrefix}.CommArrayHP2[61]` | | yes | | | | temporary data array |
| `CommArrayHP2/93` | Int2 | OPC `{TagPrefix}.CommArrayHP2[93]` | | yes | | | | temporary data array |
| `CommArrayHP2/35` | Int2 | OPC `{TagPrefix}.CommArrayHP2[35]` | | yes | | | | temporary data array |
| `CommArrayHP2/45` | Int2 | OPC `{TagPrefix}.CommArrayHP2[45]` | | yes | | | | temporary data array |
| `CommArrayHP2/75` | Int2 | OPC `{TagPrefix}.CommArrayHP2[75]` | | yes | | | | temporary data array |
| `CommArrayHP2/10` | Int2 | OPC `{TagPrefix}.CommArrayHP2[10]` | | yes | | | | temporary data array |
| `CommArrayHP2/12` | Int2 | OPC `{TagPrefix}.CommArrayHP2[12]` | | yes | | | | temporary data array |
| `CommArrayHP2/114` | Int2 | OPC `{TagPrefix}.CommArrayHP2[114]` | | yes | | | | temporary data array |
| `CommArrayHP2/112` | Int2 | OPC `{TagPrefix}.CommArrayHP2[112]` | | yes | | | | temporary data array |
| `CommArrayHP2/72` | Int2 | OPC `{TagPrefix}.CommArrayHP2[72]` | | yes | | | | temporary data array |
| `CommArrayHP2/27` | Int2 | OPC `{TagPrefix}.CommArrayHP2[27]` | | yes | | | | temporary data array |
| `CommArrayHP2/53` | Int2 | OPC `{TagPrefix}.CommArrayHP2[53]` | | yes | | | | temporary data array |
| `CommArrayHP2/14` | Int2 | OPC `{TagPrefix}.CommArrayHP2[14]` | | yes | | | | temporary data array |
| `CommArrayHP2/30` | Int2 | OPC `{TagPrefix}.CommArrayHP2[30]` | | yes | | | | temporary data array |
| `CommArrayHP2/94` | Int2 | OPC `{TagPrefix}.CommArrayHP2[94]` | | yes | | | | temporary data array |
| `CommArrayHP2/100` | Int2 | OPC `{TagPrefix}.CommArrayHP2[100]` | | yes | | | | temporary data array |
| `CommArrayHP2/101` | Int2 | OPC `{TagPrefix}.CommArrayHP2[101]` | | yes | | | | temporary data array |
| `CommArrayHP2/59` | Int2 | OPC `{TagPrefix}.CommArrayHP2[59]` | | yes | | | | temporary data array |
| `CommArrayHP2/113` | Int2 | OPC `{TagPrefix}.CommArrayHP2[113]` | | yes | | | | temporary data array |
| `CommArrayHP2/43` | Int2 | OPC `{TagPrefix}.CommArrayHP2[43]` | | yes | | | | temporary data array |
| `CommArrayHP2/74` | Int2 | OPC `{TagPrefix}.CommArrayHP2[74]` | | yes | | | | temporary data array |
| `CommArrayHP2/2` | Int2 | OPC `{TagPrefix}.CommArrayHP2[2]` | | yes | | | | temporary data array |
| `CommArrayHP2/17` | Int2 | OPC `{TagPrefix}.CommArrayHP2[17]` | | yes | | | | temporary data array |
| `CommArrayHP2/11` | Int2 | OPC `{TagPrefix}.CommArrayHP2[11]` | | yes | | | | temporary data array |
| `CommArrayHP2/116` | Int2 | OPC `{TagPrefix}.CommArrayHP2[116]` | | yes | | | | temporary data array |
| `CommArrayHP2/20` | Int2 | OPC `{TagPrefix}.CommArrayHP2[20]` | | yes | | | | temporary data array |
| `CommArrayHP2/77` | Int2 | OPC `{TagPrefix}.CommArrayHP2[77]` | | yes | | | | temporary data array |
| `CommArrayHP2/23` | Int2 | OPC `{TagPrefix}.CommArrayHP2[23]` | | yes | | | | temporary data array |
| `CommArrayHP2/1` | Int2 | OPC `{TagPrefix}.CommArrayHP2[1]` | | yes | | | | temporary data array |
| `CommArrayHP2/86` | Int2 | OPC `{TagPrefix}.CommArrayHP2[86]` | | yes | | | | temporary data array |
| `CommArrayHP2/7` | Int2 | OPC `{TagPrefix}.CommArrayHP2[7]` | | yes | | | | temporary data array |
| `CommArrayHP2/107` | Int2 | OPC `{TagPrefix}.CommArrayHP2[107]` | | yes | | | | temporary data array |
| `CommArrayHP2/95` | Int2 | OPC `{TagPrefix}.CommArrayHP2[95]` | | yes | | | | temporary data array |
| `CommArrayHP2/41` | Int2 | OPC `{TagPrefix}.CommArrayHP2[41]` | | yes | | | | temporary data array |
| `CommArrayHP2/96` | Int2 | OPC `{TagPrefix}.CommArrayHP2[96]` | | yes | | | | temporary data array |
| `CommArrayHP3/` | Folder | | | | | | | |
| `CommArrayHP3/109` | Int2 | OPC `{TagPrefix}.CommArrayHP3[109]` | | yes | | | | temporary data array |
| `CommArrayHP3/82` | Int2 | OPC `{TagPrefix}.CommArrayHP3[82]` | | yes | | | | temporary data array |
| `CommArrayHP3/8` | Int2 | OPC `{TagPrefix}.CommArrayHP3[8]` | | yes | | | | temporary data array |
| `CommArrayHP3/73` | Int2 | OPC `{TagPrefix}.CommArrayHP3[73]` | | yes | | | | temporary data array |
| `CommArrayHP3/66` | Int2 | OPC `{TagPrefix}.CommArrayHP3[66]` | | yes | | | | temporary data array |
| `CommArrayHP3/27` | Int2 | OPC `{TagPrefix}.CommArrayHP3[27]` | | yes | | | | temporary data array |
| `CommArrayHP3/50` | Int2 | OPC `{TagPrefix}.CommArrayHP3[50]` | | yes | | | | temporary data array |
| `CommArrayHP3/16` | Int2 | OPC `{TagPrefix}.CommArrayHP3[16]` | | yes | | | | temporary data array |
| `CommArrayHP3/107` | Int2 | OPC `{TagPrefix}.CommArrayHP3[107]` | | yes | | | | temporary data array |
| `CommArrayHP3/5` | Int2 | OPC `{TagPrefix}.CommArrayHP3[5]` | | yes | | | | temporary data array |
| `CommArrayHP3/25` | Int2 | OPC `{TagPrefix}.CommArrayHP3[25]` | | yes | | | | temporary data array |
| `CommArrayHP3/71` | Int2 | OPC `{TagPrefix}.CommArrayHP3[71]` | | yes | | | | temporary data array |
| `CommArrayHP3/75` | Int2 | OPC `{TagPrefix}.CommArrayHP3[75]` | | yes | | | | temporary data array |
| `CommArrayHP3/83` | Int2 | OPC `{TagPrefix}.CommArrayHP3[83]` | | yes | | | | temporary data array |
| `CommArrayHP3/102` | Int2 | OPC `{TagPrefix}.CommArrayHP3[102]` | | yes | | | | temporary data array |
| `CommArrayHP3/62` | Int2 | OPC `{TagPrefix}.CommArrayHP3[62]` | | yes | | | | temporary data array |
| `CommArrayHP3/77` | Int2 | OPC `{TagPrefix}.CommArrayHP3[77]` | | yes | | | | temporary data array |
| `CommArrayHP3/76` | Int2 | OPC `{TagPrefix}.CommArrayHP3[76]` | | yes | | | | temporary data array |
| `CommArrayHP3/31` | Int2 | OPC `{TagPrefix}.CommArrayHP3[31]` | | yes | | | | temporary data array |
| `CommArrayHP3/56` | Int2 | OPC `{TagPrefix}.CommArrayHP3[56]` | | yes | | | | temporary data array |
| `CommArrayHP3/45` | Int2 | OPC `{TagPrefix}.CommArrayHP3[45]` | | yes | | | | temporary data array |
| `CommArrayHP3/92` | Int2 | OPC `{TagPrefix}.CommArrayHP3[92]` | | yes | | | | temporary data array |
| `CommArrayHP3/67` | Int2 | OPC `{TagPrefix}.CommArrayHP3[67]` | | yes | | | | temporary data array |
| `CommArrayHP3/22` | Int2 | OPC `{TagPrefix}.CommArrayHP3[22]` | | yes | | | | temporary data array |
| `CommArrayHP3/70` | Int2 | OPC `{TagPrefix}.CommArrayHP3[70]` | | yes | | | | temporary data array |
| `CommArrayHP3/0` | Int2 | OPC `{TagPrefix}.CommArrayHP3[0]` | | yes | | | | temporary data array |
| `CommArrayHP3/2` | Int2 | OPC `{TagPrefix}.CommArrayHP3[2]` | | yes | | | | temporary data array |
| `CommArrayHP3/57` | Int2 | OPC `{TagPrefix}.CommArrayHP3[57]` | | yes | | | | temporary data array |
| `CommArrayHP3/94` | Int2 | OPC `{TagPrefix}.CommArrayHP3[94]` | | yes | | | | temporary data array |
| `CommArrayHP3/72` | Int2 | OPC `{TagPrefix}.CommArrayHP3[72]` | | yes | | | | temporary data array |
| `CommArrayHP3/88` | Int2 | OPC `{TagPrefix}.CommArrayHP3[88]` | | yes | | | | temporary data array |
| `CommArrayHP3/26` | Int2 | OPC `{TagPrefix}.CommArrayHP3[26]` | | yes | | | | temporary data array |
| `CommArrayHP3/105` | Int2 | OPC `{TagPrefix}.CommArrayHP3[105]` | | yes | | | | temporary data array |
| `CommArrayHP3/61` | Int2 | OPC `{TagPrefix}.CommArrayHP3[61]` | | yes | | | | temporary data array |
| `CommArrayHP3/53` | Int2 | OPC `{TagPrefix}.CommArrayHP3[53]` | | yes | | | | temporary data array |
| `CommArrayHP3/38` | Int2 | OPC `{TagPrefix}.CommArrayHP3[38]` | | yes | | | | temporary data array |
| `CommArrayHP3/96` | Int2 | OPC `{TagPrefix}.CommArrayHP3[96]` | | yes | | | | temporary data array |
| `CommArrayHP3/108` | Int2 | OPC `{TagPrefix}.CommArrayHP3[108]` | | yes | | | | temporary data array |
| `CommArrayHP3/104` | Int2 | OPC `{TagPrefix}.CommArrayHP3[104]` | | yes | | | | temporary data array |
| `CommArrayHP3/28` | Int2 | OPC `{TagPrefix}.CommArrayHP3[28]` | | yes | | | | temporary data array |
| `CommArrayHP3/99` | Int2 | OPC `{TagPrefix}.CommArrayHP3[99]` | | yes | | | | temporary data array |
| `CommArrayHP3/44` | Int2 | OPC `{TagPrefix}.CommArrayHP3[44]` | | yes | | | | temporary data array |
| `CommArrayHP3/20` | Int2 | OPC `{TagPrefix}.CommArrayHP3[20]` | | yes | | | | temporary data array |
| `CommArrayHP3/78` | Int2 | OPC `{TagPrefix}.CommArrayHP3[78]` | | yes | | | | temporary data array |
| `CommArrayHP3/4` | Int2 | OPC `{TagPrefix}.CommArrayHP3[4]` | | yes | | | | temporary data array |
| `CommArrayHP3/58` | Int2 | OPC `{TagPrefix}.CommArrayHP3[58]` | | yes | | | | temporary data array |
| `CommArrayHP3/64` | Int2 | OPC `{TagPrefix}.CommArrayHP3[64]` | | yes | | | | temporary data array |
| `CommArrayHP3/30` | Int2 | OPC `{TagPrefix}.CommArrayHP3[30]` | | yes | | | | temporary data array |
| `CommArrayHP3/33` | Int2 | OPC `{TagPrefix}.CommArrayHP3[33]` | | yes | | | | temporary data array |
| `CommArrayHP3/48` | Int2 | OPC `{TagPrefix}.CommArrayHP3[48]` | | yes | | | | temporary data array |
| `CommArrayHP3/7` | Int2 | OPC `{TagPrefix}.CommArrayHP3[7]` | | yes | | | | temporary data array |
| `CommArrayHP3/41` | Int2 | OPC `{TagPrefix}.CommArrayHP3[41]` | | yes | | | | temporary data array |
| `CommArrayHP3/47` | Int2 | OPC `{TagPrefix}.CommArrayHP3[47]` | | yes | | | | temporary data array |
| `CommArrayHP3/9` | Int2 | OPC `{TagPrefix}.CommArrayHP3[9]` | | yes | | | | temporary data array |
| `CommArrayHP3/93` | Int2 | OPC `{TagPrefix}.CommArrayHP3[93]` | | yes | | | | temporary data array |
| `CommArrayHP3/55` | Int2 | OPC `{TagPrefix}.CommArrayHP3[55]` | | yes | | | | temporary data array |
| `CommArrayHP3/23` | Int2 | OPC `{TagPrefix}.CommArrayHP3[23]` | | yes | | | | temporary data array |
| `CommArrayHP3/101` | Int2 | OPC `{TagPrefix}.CommArrayHP3[101]` | | yes | | | | temporary data array |
| `CommArrayHP3/110` | Int2 | OPC `{TagPrefix}.CommArrayHP3[110]` | | yes | | | | temporary data array |
| `CommArrayHP3/24` | Int2 | OPC `{TagPrefix}.CommArrayHP3[24]` | | yes | | | | temporary data array |
| `CommArrayHP3/84` | Int2 | OPC `{TagPrefix}.CommArrayHP3[84]` | | yes | | | | temporary data array |
| `CommArrayHP3/54` | Int2 | OPC `{TagPrefix}.CommArrayHP3[54]` | | yes | | | | temporary data array |
| `CommArrayHP3/13` | Int2 | OPC `{TagPrefix}.CommArrayHP3[13]` | | yes | | | | temporary data array |
| `CommArrayHP3/91` | Int2 | OPC `{TagPrefix}.CommArrayHP3[91]` | | yes | | | | temporary data array |
| `CommArrayHP3/40` | Int2 | OPC `{TagPrefix}.CommArrayHP3[40]` | | yes | | | | temporary data array |
| `CommArrayHP3/46` | Int2 | OPC `{TagPrefix}.CommArrayHP3[46]` | | yes | | | | temporary data array |
| `CommArrayHP3/52` | Int2 | OPC `{TagPrefix}.CommArrayHP3[52]` | | yes | | | | temporary data array |
| `CommArrayHP3/36` | Int2 | OPC `{TagPrefix}.CommArrayHP3[36]` | | yes | | | | temporary data array |
| `CommArrayHP3/21` | Int2 | OPC `{TagPrefix}.CommArrayHP3[21]` | | yes | | | | temporary data array |
| `CommArrayHP3/60` | Int2 | OPC `{TagPrefix}.CommArrayHP3[60]` | | yes | | | | temporary data array |
| `CommArrayHP3/37` | Int2 | OPC `{TagPrefix}.CommArrayHP3[37]` | | yes | | | | temporary data array |
| `CommArrayHP3/115` | Int2 | OPC `{TagPrefix}.CommArrayHP3[115]` | | yes | | | | temporary data array |
| `CommArrayHP3/10` | Int2 | OPC `{TagPrefix}.CommArrayHP3[10]` | | yes | | | | temporary data array |
| `CommArrayHP3/113` | Int2 | OPC `{TagPrefix}.CommArrayHP3[113]` | | yes | | | | temporary data array |
| `CommArrayHP3/103` | Int2 | OPC `{TagPrefix}.CommArrayHP3[103]` | | yes | | | | temporary data array |
| `CommArrayHP3/68` | Int2 | OPC `{TagPrefix}.CommArrayHP3[68]` | | yes | | | | temporary data array |
| `CommArrayHP3/116` | Int2 | OPC `{TagPrefix}.CommArrayHP3[116]` | | yes | | | | temporary data array |
| `CommArrayHP3/74` | Int2 | OPC `{TagPrefix}.CommArrayHP3[74]` | | yes | | | | temporary data array |
| `CommArrayHP3/35` | Int2 | OPC `{TagPrefix}.CommArrayHP3[35]` | | yes | | | | temporary data array |
| `CommArrayHP3/29` | Int2 | OPC `{TagPrefix}.CommArrayHP3[29]` | | yes | | | | temporary data array |
| `CommArrayHP3/12` | Int2 | OPC `{TagPrefix}.CommArrayHP3[12]` | | yes | | | | temporary data array |
| `CommArrayHP3/90` | Int2 | OPC `{TagPrefix}.CommArrayHP3[90]` | | yes | | | | temporary data array |
| `CommArrayHP3/11` | Int2 | OPC `{TagPrefix}.CommArrayHP3[11]` | | yes | | | | temporary data array |
| `CommArrayHP3/63` | Int2 | OPC `{TagPrefix}.CommArrayHP3[63]` | | yes | | | | temporary data array |
| `CommArrayHP3/17` | Int2 | OPC `{TagPrefix}.CommArrayHP3[17]` | | yes | | | | temporary data array |
| `CommArrayHP3/95` | Int2 | OPC `{TagPrefix}.CommArrayHP3[95]` | | yes | | | | temporary data array |
| `CommArrayHP3/97` | Int2 | OPC `{TagPrefix}.CommArrayHP3[97]` | | yes | | | | temporary data array |
| `CommArrayHP3/111` | Int2 | OPC `{TagPrefix}.CommArrayHP3[111]` | | yes | | | | temporary data array |
| `CommArrayHP3/18` | Int2 | OPC `{TagPrefix}.CommArrayHP3[18]` | | yes | | | | temporary data array |
| `CommArrayHP3/65` | Int2 | OPC `{TagPrefix}.CommArrayHP3[65]` | | yes | | | | temporary data array |
| `CommArrayHP3/89` | Int2 | OPC `{TagPrefix}.CommArrayHP3[89]` | | yes | | | | temporary data array |
| `CommArrayHP3/69` | Int2 | OPC `{TagPrefix}.CommArrayHP3[69]` | | yes | | | | temporary data array |
| `CommArrayHP3/81` | Int2 | OPC `{TagPrefix}.CommArrayHP3[81]` | | yes | | | | temporary data array |
| `CommArrayHP3/15` | Int2 | OPC `{TagPrefix}.CommArrayHP3[15]` | | yes | | | | temporary data array |
| `CommArrayHP3/42` | Int2 | OPC `{TagPrefix}.CommArrayHP3[42]` | | yes | | | | temporary data array |
| `CommArrayHP3/80` | Int2 | OPC `{TagPrefix}.CommArrayHP3[80]` | | yes | | | | temporary data array |
| `CommArrayHP3/39` | Int2 | OPC `{TagPrefix}.CommArrayHP3[39]` | | yes | | | | temporary data array |
| `CommArrayHP3/19` | Int2 | OPC `{TagPrefix}.CommArrayHP3[19]` | | yes | | | | temporary data array |
| `CommArrayHP3/3` | Int2 | OPC `{TagPrefix}.CommArrayHP3[3]` | | yes | | | | temporary data array |
| `CommArrayHP3/6` | Int2 | OPC `{TagPrefix}.CommArrayHP3[6]` | | yes | | | | temporary data array |
| `CommArrayHP3/49` | Int2 | OPC `{TagPrefix}.CommArrayHP3[49]` | | yes | | | | temporary data array |
| `CommArrayHP3/32` | Int2 | OPC `{TagPrefix}.CommArrayHP3[32]` | | yes | | | | temporary data array |
| `CommArrayHP3/79` | Int2 | OPC `{TagPrefix}.CommArrayHP3[79]` | | yes | | | | temporary data array |
| `CommArrayHP3/106` | Int2 | OPC `{TagPrefix}.CommArrayHP3[106]` | | yes | | | | temporary data array |
| `CommArrayHP3/112` | Int2 | OPC `{TagPrefix}.CommArrayHP3[112]` | | yes | | | | temporary data array |
| `CommArrayHP3/100` | Int2 | OPC `{TagPrefix}.CommArrayHP3[100]` | | yes | | | | temporary data array |
| `CommArrayHP3/14` | Int2 | OPC `{TagPrefix}.CommArrayHP3[14]` | | yes | | | | temporary data array |
| `CommArrayHP3/34` | Int2 | OPC `{TagPrefix}.CommArrayHP3[34]` | | yes | | | | temporary data array |
| `CommArrayHP3/98` | Int2 | OPC `{TagPrefix}.CommArrayHP3[98]` | | yes | | | | temporary data array |
| `CommArrayHP3/87` | Int2 | OPC `{TagPrefix}.CommArrayHP3[87]` | | yes | | | | temporary data array |
| `CommArrayHP3/1` | Int2 | OPC `{TagPrefix}.CommArrayHP3[1]` | | yes | | | | temporary data array |
| `CommArrayHP3/85` | Int2 | OPC `{TagPrefix}.CommArrayHP3[85]` | | yes | | | | temporary data array |
| `CommArrayHP3/43` | Int2 | OPC `{TagPrefix}.CommArrayHP3[43]` | | yes | | | | temporary data array |
| `CommArrayHP3/86` | Int2 | OPC `{TagPrefix}.CommArrayHP3[86]` | | yes | | | | temporary data array |
| `CommArrayHP3/59` | Int2 | OPC `{TagPrefix}.CommArrayHP3[59]` | | yes | | | | temporary data array |
| `CommArrayHP3/114` | Int2 | OPC `{TagPrefix}.CommArrayHP3[114]` | | yes | | | | temporary data array |
| `CommArrayHP3/51` | Int2 | OPC `{TagPrefix}.CommArrayHP3[51]` | | yes | | | | temporary data array |
| `EthernetSlot` | Int4 | OPC `{TagPrefix}.EthernetSlot` | | yes | | | | Slot containing the Ethernet Card |
| `FastUpdateRate_Actual` | Int4 | OPC `{TagPrefix}.FastUpdateRate_Actual` | | yes | | | | Measured refresh rate (ms) |
| `FastUpdateRate_Set` | Int4 | OPC `{TagPrefix}.FastUpdateRate_Set` | | yes | | | | Target refresh rate for $'important$' values. (ms) |
| `IntegratedNIC` | Boolean | OPC `{TagPrefix}.IntegratedNIC` | | yes | | | | true if ethernet is integrated into processor (L8, compactlogix) |
| `NumberOfCompressors` | Int4 | OPC `{TagPrefix}.NumberOfCompressors` | | yes | | | | Number of Compressors to Scan |
| `WriteData` | Int2 | OPC `{TagPrefix}.WriteData` | | yes | | | | integer to write |
| `ZZZZZZZZZZQHD_CompCo0` | Int1 | OPC `{TagPrefix}.ZZZZZZZZZZQHD_CompCo0` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
