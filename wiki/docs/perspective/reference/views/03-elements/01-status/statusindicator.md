---
title: "StatusIndicator"
sidebar_label: "StatusIndicator"
description: "Perspective view 03_Elements/01_Status/StatusIndicator (Element (small reusable part)): 2 components, 15 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/StatusIndicator", "StatusIndicator"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/StatusIndicator`.

| | |
|---|---|
| View path | `03_Elements/01_Status/StatusIndicator` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/StatusIndicator/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; StatusIndicator |
| Root | `ia.container.flex`, height 22, width 96 |
| Size | 2 components, 15 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T06:25:24Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Evaporators/EV-01/Status/Value"` | input |
| `outOfService` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `label` | `"Fault"` | bound (expr) |
| `metadata` | `{"longDescription": "evaporator status", "shortDescription": "statu...` | bound (tag) |
| `quality` | `"Good"` | bound (expr) |
| `states` | `[{"label": "Off", "value": 0}, {"label": "Cooling", "value": 1}, {"...` | bound (expr) |
| `value` | `3` | bound (expr) |
| `tooltip` | `""` | bound (expr) |
| `display` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1.

```text
root  ia.container.flex  [4 bindings]
  StatusLabel  ia.display.label  [4 bindings]
```

## Bindings

15 bindings: expr 10, expr-struct 2, property 2, tag 1.

<details>
<summary>All 15 bindings, grouped by component</summary>

**`(view)`**

- `custom.label`: expression, then script transform

```js
if(isNull({view.custom.states}),
	{view.custom.value},
	{view.custom.value})
```

Transform 1, script:

```python
if value is None:
    tag_path = ''
    try:
        tag_path = self.view.params.tagPath or ''
    except:
        pass
    if str(tag_path).strip() == '':
        return ''
    q = ''
    try:
        q = str(self.custom.quality or '')
    except:
        pass
    if not q.startswith('Good'):
        return 'COMM LOSS'
    return ''
try:
    v = int(value)
except:
    return ''
# Evaporator: stages inline beside DFT (DFT PD / HG / BLD / FD)
codes_evap = {
    0: 'STOP', 1: 'CLG', 2: 'DFT', 3: 'FLT', 5: 'IDLE',
    6: 'DFT PD', 7: 'DFT HG', 8: 'DFT BLD', 9: 'DFT FD'
}
codes_run = {0: 'STOP', 1: 'RUN', 2: 'FLT', 4: 'IDLE'}
stage_alias = {
    'PUMP DOWN': 'DFT PD', '1.PD': 'DFT PD', 'PD': 'DFT PD',
    'HOT GAS': 'DFT HG', '2.HG': 'DFT HG', 'HG': 'DFT HG',
    'BLEED': 'DFT BLD', '3.BLD': 'DFT BLD', 'BLD': 'DFT BLD',
    'FAN DELAY': 'DFT FD', '3.FD': 'DFT FD', 'FD': 'DFT FD'
}
states = self.custom.states
if states:
    try:
        for s in states:
            sv = s['value'] if hasattr(s, '__getitem__') else getattr(s, 'value', None)
            sl = s['label'] if hasattr(s, '__getitem__') else getattr(s, 'label', None)
            if sv is not None and int(sv) == v and sl not in (None, ''):
                key = str(sl).strip().upper()
# ... 55 more line(s): see the view.json
```


- `custom.metadata`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}.Metadata`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	'',
	{value})
```


- `custom.quality`: expression

```js
if({view.params.tagPath} = '',
	'Bad',
	qualityOf(tag({view.params.tagPath})))
```


- `custom.states`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath})),
	null,
	if(!isGood(tag({view.params.tagPath} + '.Metadata')),
		null,
		tag({view.params.tagPath} + '.Metadata')['states']))
```


- `custom.value`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath})),
	null,
	tag({view.params.tagPath}))
```


- `custom.tooltip`: expression, then script transform

```js
{view.custom.label}
```

Transform 1, script:

```python
code = str(value or '').strip().upper()
tips = {
    'CLG': 'Cooling',
    'COOLING': 'Cooling',
    'RUN': 'Running',
    'RUNNING': 'Running',
    'DFT': 'Defrost',
    'DEFROST': 'Defrost',
    'DFT PD': 'Defrost - Pump Down',
    'DFT HG': 'Defrost - Hot Gas',
    'DFT BLD': 'Defrost - Bleed',
    'DFT FD': 'Defrost - Fan Delay',
    '1.PD': 'Defrost - Pump Down',
    '2.HG': 'Defrost - Hot Gas',
    '3.BLD': 'Defrost - Bleed',
    '3.FD': 'Defrost - Fan Delay',
    'IDLE': 'Idle - Achieved Temp Setpoint',
    'STOP': 'Off - Unit disabled',
    'OFF': 'Off - Unit disabled',
    'FLT': 'Fault',
    'FAULT': 'Fault',
    'OPEN': 'Open',
    'CLOSED': 'Closed',
    'CLOSING': 'Closing',
    'OPENING': 'Opening',
    'DISABLED': 'Disabled',
    'UNK': 'Unknown',
    'OK': 'Normal',
    'COMM LOSS': 'Communication loss',
    'COMMLOSS': 'Communication loss',
    'COMM': 'Communication loss'
}
return tips.get(code, '')
```


- `custom.display`: expression

```js
if(coalesce({view.params.outOfService}, false), 'OUT OF SERVICE', if({view.params.tagPath} != '' && left(toStr(coalesce({view.custom.quality}, 'Bad')), 4) != 'Good', 'COMM LOSS', coalesce({view.custom.label}, '')))
```


**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

- `meta.tooltip.text`: property `view.custom.tooltip`

- `meta.tooltip.enabled`: expression

```js
if(coalesce({view.custom.tooltip}, '') = '',
	false,
	true)
```


**`root/StatusLabel`**

- `props.style.color`: expression, then script transform

```js
{view.custom.display}
```

Transform 1, script:

```python
s = str(value).strip().upper()
if not s:
    return 'transparent'
# Match DFT with optional stage suffix (DFT PD / DFT HG / ...)
if s == 'DFT' or s.startswith('DFT '):
    return '#EC407A'
colors = {
    'COOLING': '#1E88E5',
    'CLG': '#1E88E5',
    'RUN': '#228B22',
    'RUNNING': '#228B22',
    'ON': '#228B22',
    'OPEN': '#228B22',
    'OK': '#228B22',
    'DEFROST': '#EC407A',
    'FAULT': '#C62828',
    'ALARM': '#C62828',
    'FLT': '#C62828',
    'COMM LOSS': '#C62828',
    'COMMLOSS': '#C62828',
    'COMM': '#C62828',
    'IDLE': '#228B22',
    'STANDBY': '#228B22',
    'IDL': '#228B22',
    'OFF': '#9E9E9E',
    'STOP': '#9E9E9E',
    'STOPPED': '#9E9E9E',
    'CLOSED': '#9E9E9E',
    'UNK': '#607D8B',
    'OUT OF SERVICE': '#616161'
}
return colors.get(s, '#607D8B')
```


- `props.text`: property `view.custom.display`

- `props.style.opacity`: expression

```js
if({view.custom.display} = '',
   0,
   1)
```


- `props.style.fontSize`: expression

```js
if(coalesce({view.params.outOfService}, false), '10px', '12px')
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (8): [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](../../01-popups/00-faceplates/assets/coolingtower/controls.md), [02\_Components/01\_Devices/Compressor](../../02-components/01-devices/compressor.md), [02\_Components/01\_Devices/CoolingTower](../../02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](../../02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](../../02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Pump](../../02-components/01-devices/pump.md), [02\_Components/01\_Devices/SolenoidValve](../../02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](../../02-components/01-devices/tank.md)

## Tags And Data

- `{tagPath}.Metadata`

Member paths appended to a base path in expressions (relative):

`.Metadata`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
