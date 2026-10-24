---
title: "PLC/Modules/1769_IF8"
sidebar_label: "1769_IF8"
description: "UDT definition PLC/Modules/1769_IF8: 1769-IF8 8-Channel Analog Input (0-5 V / 4-20 mA) (read only)"
generated: true
---

:::note

:::
# UDT `PLC/Modules/1769_IF8`

1769-IF8 8-Channel Analog Input (0-5 V / 4-20 mA) (read only)

Allen-Bradley 1769-IF8 on a Logix local bus: OPC ns=1;s=\[\{DeviceName\}\]Local:\{Slot\}:I\|O\|C.&lt;member&gt;, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Modules &gt; 1769\_IF8 |
| Tag path | `[default]_types_/PLC/Modules/1769_IF8` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/Modules/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 98 (98 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `DeviceName` | String | - | own |
| `Slot` | Integer | `0` | own |
| `Description` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

66 members read OPC through the server `Ignition OPC UA Server`. Common prefix: `ns=1;s=[{DeviceName}]`. The Source column shows the part after the device.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `CatalogDescription` | String | expr `'8-Channel Analog Input (0-5 V / 4-20 mA)'` | | yes | | | | Catalog description |
| `CatalogNumber` | String | expr `'1769-IF8'` | | yes | | | | Allen-Bradley catalog number |
| `Ch0Data` | Int2 | OPC `Local:{Slot}:I.Ch0Data` | PAX\_Status | yes | | | | Channel 0 input value (counts in the configured data format) |
| `Ch0DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch0DataFormat` | PAX\_Status | yes | | | | Channel 0 configured data format code (module configuration) |
| `Ch0En` | Boolean | OPC `Local:{Slot}:C.Ch0En` | PAX\_Status | yes | | | | Channel 0 enabled (configuration) |
| `Ch0HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch0HAlarm` | PAX\_Faceplate | yes | | | | Channel 0 module high process alarm |
| `Ch0LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch0LAlarm` | PAX\_Faceplate | yes | | | | Channel 0 module low process alarm |
| `Ch0OverRange` | Boolean | OPC `Local:{Slot}:I.Ch0OverRange` | PAX\_Status | yes | | | | Channel 0 over range |
| `Ch0Range` | Int1 | OPC `Local:{Slot}:C.Ch0Range` | PAX\_Status | yes | | | | Channel 0 configured input range code (module configuration) |
| `Ch0RangeText` | String | expr `case({[.]Ch0Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 0 input range (1769-IF8 profile code) |
| `Ch0Signal` | Float4 | expr `if({[.]Ch0DataFormat} = 1, {[.]Ch0Data} / 1000.0, null)` | | yes | | | | Channel 0 signal in V or mA (Engineering Units counts / 1000) |
| `Ch0UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch0UnderRange` | PAX\_Status | yes | | | | Channel 0 under range |
| `Ch0Unit` | String | expr `case({[.]Ch0Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 0 signal unit (range code) |
| `Ch1Data` | Int2 | OPC `Local:{Slot}:I.Ch1Data` | PAX\_Status | yes | | | | Channel 1 input value (counts in the configured data format) |
| `Ch1DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch1DataFormat` | PAX\_Status | yes | | | | Channel 1 configured data format code (module configuration) |
| `Ch1En` | Boolean | OPC `Local:{Slot}:C.Ch1En` | PAX\_Status | yes | | | | Channel 1 enabled (configuration) |
| `Ch1HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch1HAlarm` | PAX\_Faceplate | yes | | | | Channel 1 module high process alarm |
| `Ch1LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch1LAlarm` | PAX\_Faceplate | yes | | | | Channel 1 module low process alarm |
| `Ch1OverRange` | Boolean | OPC `Local:{Slot}:I.Ch1OverRange` | PAX\_Status | yes | | | | Channel 1 over range |
| `Ch1Range` | Int1 | OPC `Local:{Slot}:C.Ch1Range` | PAX\_Status | yes | | | | Channel 1 configured input range code (module configuration) |
| `Ch1RangeText` | String | expr `case({[.]Ch1Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 1 input range (1769-IF8 profile code) |
| `Ch1Signal` | Float4 | expr `if({[.]Ch1DataFormat} = 1, {[.]Ch1Data} / 1000.0, null)` | | yes | | | | Channel 1 signal in V or mA (Engineering Units counts / 1000) |
| `Ch1UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch1UnderRange` | PAX\_Status | yes | | | | Channel 1 under range |
| `Ch1Unit` | String | expr `case({[.]Ch1Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 1 signal unit (range code) |
| `Ch2Data` | Int2 | OPC `Local:{Slot}:I.Ch2Data` | PAX\_Status | yes | | | | Channel 2 input value (counts in the configured data format) |
| `Ch2DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch2DataFormat` | PAX\_Status | yes | | | | Channel 2 configured data format code (module configuration) |
| `Ch2En` | Boolean | OPC `Local:{Slot}:C.Ch2En` | PAX\_Status | yes | | | | Channel 2 enabled (configuration) |
| `Ch2HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch2HAlarm` | PAX\_Faceplate | yes | | | | Channel 2 module high process alarm |
| `Ch2LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch2LAlarm` | PAX\_Faceplate | yes | | | | Channel 2 module low process alarm |
| `Ch2OverRange` | Boolean | OPC `Local:{Slot}:I.Ch2OverRange` | PAX\_Status | yes | | | | Channel 2 over range |
| `Ch2Range` | Int1 | OPC `Local:{Slot}:C.Ch2Range` | PAX\_Status | yes | | | | Channel 2 configured input range code (module configuration) |
| `Ch2RangeText` | String | expr `case({[.]Ch2Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 2 input range (1769-IF8 profile code) |
| `Ch2Signal` | Float4 | expr `if({[.]Ch2DataFormat} = 1, {[.]Ch2Data} / 1000.0, null)` | | yes | | | | Channel 2 signal in V or mA (Engineering Units counts / 1000) |
| `Ch2UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch2UnderRange` | PAX\_Status | yes | | | | Channel 2 under range |
| `Ch2Unit` | String | expr `case({[.]Ch2Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 2 signal unit (range code) |
| `Ch3Data` | Int2 | OPC `Local:{Slot}:I.Ch3Data` | PAX\_Status | yes | | | | Channel 3 input value (counts in the configured data format) |
| `Ch3DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch3DataFormat` | PAX\_Status | yes | | | | Channel 3 configured data format code (module configuration) |
| `Ch3En` | Boolean | OPC `Local:{Slot}:C.Ch3En` | PAX\_Status | yes | | | | Channel 3 enabled (configuration) |
| `Ch3HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch3HAlarm` | PAX\_Faceplate | yes | | | | Channel 3 module high process alarm |
| `Ch3LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch3LAlarm` | PAX\_Faceplate | yes | | | | Channel 3 module low process alarm |
| `Ch3OverRange` | Boolean | OPC `Local:{Slot}:I.Ch3OverRange` | PAX\_Status | yes | | | | Channel 3 over range |
| `Ch3Range` | Int1 | OPC `Local:{Slot}:C.Ch3Range` | PAX\_Status | yes | | | | Channel 3 configured input range code (module configuration) |
| `Ch3RangeText` | String | expr `case({[.]Ch3Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 3 input range (1769-IF8 profile code) |
| `Ch3Signal` | Float4 | expr `if({[.]Ch3DataFormat} = 1, {[.]Ch3Data} / 1000.0, null)` | | yes | | | | Channel 3 signal in V or mA (Engineering Units counts / 1000) |
| `Ch3UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch3UnderRange` | PAX\_Status | yes | | | | Channel 3 under range |
| `Ch3Unit` | String | expr `case({[.]Ch3Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 3 signal unit (range code) |
| `Ch4Data` | Int2 | OPC `Local:{Slot}:I.Ch4Data` | PAX\_Status | yes | | | | Channel 4 input value (counts in the configured data format) |
| `Ch4DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch4DataFormat` | PAX\_Status | yes | | | | Channel 4 configured data format code (module configuration) |
| `Ch4En` | Boolean | OPC `Local:{Slot}:C.Ch4En` | PAX\_Status | yes | | | | Channel 4 enabled (configuration) |
| `Ch4HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch4HAlarm` | PAX\_Faceplate | yes | | | | Channel 4 module high process alarm |
| `Ch4LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch4LAlarm` | PAX\_Faceplate | yes | | | | Channel 4 module low process alarm |
| `Ch4OverRange` | Boolean | OPC `Local:{Slot}:I.Ch4OverRange` | PAX\_Status | yes | | | | Channel 4 over range |
| `Ch4Range` | Int1 | OPC `Local:{Slot}:C.Ch4Range` | PAX\_Status | yes | | | | Channel 4 configured input range code (module configuration) |
| `Ch4RangeText` | String | expr `case({[.]Ch4Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 4 input range (1769-IF8 profile code) |
| `Ch4Signal` | Float4 | expr `if({[.]Ch4DataFormat} = 1, {[.]Ch4Data} / 1000.0, null)` | | yes | | | | Channel 4 signal in V or mA (Engineering Units counts / 1000) |
| `Ch4UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch4UnderRange` | PAX\_Status | yes | | | | Channel 4 under range |
| `Ch4Unit` | String | expr `case({[.]Ch4Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 4 signal unit (range code) |
| `Ch5Data` | Int2 | OPC `Local:{Slot}:I.Ch5Data` | PAX\_Status | yes | | | | Channel 5 input value (counts in the configured data format) |
| `Ch5DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch5DataFormat` | PAX\_Status | yes | | | | Channel 5 configured data format code (module configuration) |
| `Ch5En` | Boolean | OPC `Local:{Slot}:C.Ch5En` | PAX\_Status | yes | | | | Channel 5 enabled (configuration) |
| `Ch5HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch5HAlarm` | PAX\_Faceplate | yes | | | | Channel 5 module high process alarm |
| `Ch5LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch5LAlarm` | PAX\_Faceplate | yes | | | | Channel 5 module low process alarm |
| `Ch5OverRange` | Boolean | OPC `Local:{Slot}:I.Ch5OverRange` | PAX\_Status | yes | | | | Channel 5 over range |
| `Ch5Range` | Int1 | OPC `Local:{Slot}:C.Ch5Range` | PAX\_Status | yes | | | | Channel 5 configured input range code (module configuration) |
| `Ch5RangeText` | String | expr `case({[.]Ch5Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 5 input range (1769-IF8 profile code) |
| `Ch5Signal` | Float4 | expr `if({[.]Ch5DataFormat} = 1, {[.]Ch5Data} / 1000.0, null)` | | yes | | | | Channel 5 signal in V or mA (Engineering Units counts / 1000) |
| `Ch5UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch5UnderRange` | PAX\_Status | yes | | | | Channel 5 under range |
| `Ch5Unit` | String | expr `case({[.]Ch5Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 5 signal unit (range code) |
| `Ch6Data` | Int2 | OPC `Local:{Slot}:I.Ch6Data` | PAX\_Status | yes | | | | Channel 6 input value (counts in the configured data format) |
| `Ch6DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch6DataFormat` | PAX\_Status | yes | | | | Channel 6 configured data format code (module configuration) |
| `Ch6En` | Boolean | OPC `Local:{Slot}:C.Ch6En` | PAX\_Status | yes | | | | Channel 6 enabled (configuration) |
| `Ch6HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch6HAlarm` | PAX\_Faceplate | yes | | | | Channel 6 module high process alarm |
| `Ch6LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch6LAlarm` | PAX\_Faceplate | yes | | | | Channel 6 module low process alarm |
| `Ch6OverRange` | Boolean | OPC `Local:{Slot}:I.Ch6OverRange` | PAX\_Status | yes | | | | Channel 6 over range |
| `Ch6Range` | Int1 | OPC `Local:{Slot}:C.Ch6Range` | PAX\_Status | yes | | | | Channel 6 configured input range code (module configuration) |
| `Ch6RangeText` | String | expr `case({[.]Ch6Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 6 input range (1769-IF8 profile code) |
| `Ch6Signal` | Float4 | expr `if({[.]Ch6DataFormat} = 1, {[.]Ch6Data} / 1000.0, null)` | | yes | | | | Channel 6 signal in V or mA (Engineering Units counts / 1000) |
| `Ch6UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch6UnderRange` | PAX\_Status | yes | | | | Channel 6 under range |
| `Ch6Unit` | String | expr `case({[.]Ch6Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 6 signal unit (range code) |
| `Ch7Data` | Int2 | OPC `Local:{Slot}:I.Ch7Data` | PAX\_Status | yes | | | | Channel 7 input value (counts in the configured data format) |
| `Ch7DataFormat` | Int1 | OPC `Local:{Slot}:C.Ch7DataFormat` | PAX\_Status | yes | | | | Channel 7 configured data format code (module configuration) |
| `Ch7En` | Boolean | OPC `Local:{Slot}:C.Ch7En` | PAX\_Status | yes | | | | Channel 7 enabled (configuration) |
| `Ch7HAlarm` | Boolean | OPC `Local:{Slot}:I.Ch7HAlarm` | PAX\_Faceplate | yes | | | | Channel 7 module high process alarm |
| `Ch7LAlarm` | Boolean | OPC `Local:{Slot}:I.Ch7LAlarm` | PAX\_Faceplate | yes | | | | Channel 7 module low process alarm |
| `Ch7OverRange` | Boolean | OPC `Local:{Slot}:I.Ch7OverRange` | PAX\_Status | yes | | | | Channel 7 over range |
| `Ch7Range` | Int1 | OPC `Local:{Slot}:C.Ch7Range` | PAX\_Status | yes | | | | Channel 7 configured input range code (module configuration) |
| `Ch7RangeText` | String | expr `case({[.]Ch7Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V',…` (full below) | | yes | | | | Channel 7 input range (1769-IF8 profile code) |
| `Ch7Signal` | Float4 | expr `if({[.]Ch7DataFormat} = 1, {[.]Ch7Data} / 1000.0, null)` | | yes | | | | Channel 7 signal in V or mA (Engineering Units counts / 1000) |
| `Ch7UnderRange` | Boolean | OPC `Local:{Slot}:I.Ch7UnderRange` | PAX\_Status | yes | | | | Channel 7 under range |
| `Ch7Unit` | String | expr `case({[.]Ch7Range}, 0, 'V', 1, 'V', 2, 'V', 3, 'mA', 4, 'V', 5, 'mA', '')` | | yes | | | | Channel 7 signal unit (range code) |
| `CommOk` | Boolean | OPC `[Diagnostics]/Connected` | PAX\_Status | yes | | | | Logix driver connected (gates the card alarms during a comm loss) |
| `ConnectionFaulted` | Boolean | expr `coalesce({[.]CommOk}, false) && {[.]Fault} = -1` | | yes | | | | Connection fault to the card: every Fault bit set (only while the driver is connected) |
| `Fault` | Int4 | OPC `Local:{Slot}:I.Fault` | PAX\_Status | yes | | | | Module fault word (Logix Local:n:I.Fault); 0 = OK, all bits set (-1) = connection fault |
| `Faulted` | Boolean | expr `coalesce({[.]CommOk}, false) && {[.]Fault} != 0` | | yes | | | 1 | Module fault: Fault word non-zero (only while the driver is connected) |
| `ModuleType` | String | expr `'AI'` | | yes | | | | DI / DO / AI / AO / Comm |
| `PanelLabel` | String | expr `'ANALOG IN'` | | yes | | | | Front-panel legend |
| `Points` | Int4 | expr `8` | | yes | | | | Point / channel count |
| `Series` | String | expr `'A'` | | yes | | | | Catalog series |

<details>
<summary>Full expressions / references (8)</summary>

**`Ch0RangeText`** (expr)

```
case({[.]Ch0Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```

**`Ch1RangeText`** (expr)

```
case({[.]Ch1Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```

**`Ch2RangeText`** (expr)

```
case({[.]Ch2Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```

**`Ch3RangeText`** (expr)

```
case({[.]Ch3Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```

**`Ch4RangeText`** (expr)

```
case({[.]Ch4Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```

**`Ch5RangeText`** (expr)

```
case({[.]Ch5Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```

**`Ch6RangeText`** (expr)

```
case({[.]Ch6Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```

**`Ch7RangeText`** (expr)

```
case({[.]Ch7Range}, 0, '-10 to +10 V', 1, '0 to 5 V', 2, '0 to 10 V', 3, '4 to 20 mA', 4, '1 to 5 V', 5, '0 to 20 mA', 'Unknown')
```


</details>

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `Faulted` | Module Fault | High | WhenTrue | `true` | replace(try(split(\{PathToTag\}, '/')\[1, 0\], ''), 'GrovePort', 'Groveport') + ' / ' + try(split(\{PathToTag\}, '/')\[2, 0\], '') + ' / PLC / ' + try(split(\{PathToTag\}, '/')\[4, 0\], '') + ' / ' + try(split(\{PathToTag\}, '/')\[5, 0\], '') | 1769-IF8 Local:n:I.Fault != 0 (-1 = connection fault to the card). Suppressed while PLC communicati… |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Nested in: [PLC/Sites/BH\_Groveport\_RCP1](../plc-sites/bh-groveport-rcp1.md) (as `Slot01`), [PLC/Sites/BH\_Groveport\_RCP1](../plc-sites/bh-groveport-rcp1.md) (as `Slot02`), [PLC/Sites/BH\_Groveport\_RCP1](../plc-sites/bh-groveport-rcp1.md) (as `Slot03`), [PLC/Sites/BH\_Groveport\_RCP1](../plc-sites/bh-groveport-rcp1.md) (as `Slot04`)

Reached through nesting by 1 top-level instance(s).
