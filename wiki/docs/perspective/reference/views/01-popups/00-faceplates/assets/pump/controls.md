---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Pump/Controls (Asset (embedded piece)): 75 components, 79 bindings, 7 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Pump/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Pump/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Pump/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Pump/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Pump &gt; Controls |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 75 components, 79 bindings, 7 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:19:43Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

<details>
<summary>31 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `qg0` | `null` | bound (expr) |
| `qg1` | `null` | bound (expr) |
| `qg2` | `null` | bound (expr) |
| `qg3` | `null` | bound (expr) |
| `qg4` | `null` | bound (expr) |
| `qg5` | `null` | bound (expr) |
| `qg6` | `null` | bound (expr) |
| `qg7` | `null` | bound (expr) |
| `qg8` | `null` | bound (expr) |
| `qg9` | `null` | bound (expr) |
| `qg10` | `null` | bound (expr) |
| `qg11` | `null` | bound (expr) |
| `qg12` | `null` | bound (expr) |
| `qg13` | `null` | bound (expr) |
| `qg14` | `null` | bound (expr) |
| `qg15` | `null` | bound (expr) |
| `qg16` | `null` | bound (expr) |
| `qg17` | `null` | bound (expr) |
| `qg18` | `null` | bound (expr) |
| `qg19` | `null` | bound (expr) |
| `qg20` | `null` | bound (expr) |
| `qg21` | `null` | bound (expr) |
| `qg22` | `null` | bound (expr) |
| `qg23` | `null` | bound (expr) |
| `qg24` | `null` | bound (expr) |
| `qg25` | `null` | bound (expr) |
| `qg26` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |

</details>

## Component Tree

Component types: ia.display.label x43, ia.container.flex x28, ia.input.button x3, ia.display.view x1.

<details>
<summary>Component tree (75 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Modes  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Modes]
  StatusSection  ia.container.flex
    StatusTitle  ia.display.label
    StatusBanner  ia.display.label  [2 bindings; 1 event]
    PiChips  ia.container.flex
      Perm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Intlk  ia.container.flex  [1 event]
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Bypass  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
    CmdRow  ia.container.flex
      BtnStart  ia.input.button  [4 bindings; 1 event]
      BtnStop  ia.input.button  [4 bindings; 1 event]
      BtnReset  ia.input.button  [3 bindings; 1 event]
  FaultsSection  ia.container.flex  [1 binding]
    FaultsTitle  ia.display.label
    FaultChips  ia.container.flex
      FailToStartAlm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      FailToStopAlm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      IOFaultAlm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      IntlkTripAlm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      FailToStartSts  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      IOFaultSts  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
  KpiSection  ia.container.flex
    KpiTitle  ia.display.label
    Runtime  ia.container.flex
      RuntimeLbl  ia.display.label
      RuntimeVal  ia.display.label  [2 bindings; 1 event]
    Starts  ia.container.flex
      StartsLbl  ia.display.label
      StartsVal  ia.display.label  [2 bindings; 1 event]
    FailTimer  ia.container.flex
      FailTimerLbl  ia.display.label
      FailTimerVal  ia.display.label  [2 bindings]
  NotReadySection  ia.container.flex
    Title  ia.display.label
    Rows  ia.container.flex
      NrdyDisabled  ia.container.flex
        Dot  ia.display.label  [1 binding]
        Label  ia.display.label
      NrdyCfgErr  ia.container.flex
        Dot  ia.display.label  [1 binding]
        Label  ia.display.label
      NrdyIntlk  ia.container.flex
        Dot  ia.display.label  [1 binding]
        Label  ia.display.label
      NrdyPerm  ia.container.flex
        Dot  ia.display.label  [1 binding]
        Label  ia.display.label
      NrdyIOFault  ia.container.flex
        Dot  ia.display.label  [1 binding]
        Label  ia.display.label
      NrdyFail  ia.container.flex
        Dot  ia.display.label  [1 binding]
        Label  ia.display.label
      NrdyNoMode  ia.container.flex
        Dot  ia.display.label  [1 binding]
        Label  ia.display.label
```

</details>

## Bindings

79 bindings: expr 76, expr-struct 2, property 1.

<details>
<summary>All 79 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Val_Sts')), tag({view.params.tagPath} + '/Motor/Val_Sts'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_FailToStart')), tag({view.params.tagPath} + '/Motor/Alm_FailToStart'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_FailToStop')), tag({view.params.tagPath} + '/Motor/Alm_FailToStop'), null), null)
```


- `custom.qg3`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_IOFault')), tag({view.params.tagPath} + '/Motor/Alm_IOFault'), null), null)
```


- `custom.qg4`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_IntlkTrip')), tag({view.params.tagPath} + '/Motor/Alm_IntlkTrip'), null), null)
```


- `custom.qg5`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Sts_FailToStart')), tag({view.params.tagPath} + '/Motor/Sts_FailToStart'), null), null)
```


- `custom.qg6`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Sts_FailToStop')), tag({view.params.tagPath} + '/Motor/Sts_FailToStop'), null), null)
```


- `custom.qg7`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Inp_NBPermOK')), tag({view.params.tagPath} + '/Motor/Inp_NBPermOK'), null), null)
```


- `custom.qg8`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Intlk/Sts_BypActive')), tag({view.params.tagPath} + '/Intlk/Sts_BypActive'), null), null)
```


- `custom.qg9`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Inp_PermOK')), tag({view.params.tagPath} + '/Motor/Inp_PermOK'), null), null)
```


- `custom.qg10`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Intlk/Sts_NBIntlkOK')), tag({view.params.tagPath} + '/Intlk/Sts_NBIntlkOK'), null), null)
```


- `custom.qg11`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Intlk/Sts_IntlkOK')), tag({view.params.tagPath} + '/Intlk/Sts_IntlkOK'), null), null)
```


- `custom.qg12`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Rdy_Start')), tag({view.params.tagPath} + '/Motor/Rdy_Start'), null), null)
```


- `custom.qg13`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Sts_Running')), tag({view.params.tagPath} + '/Motor/Sts_Running'), null), null)
```


- `custom.qg14`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Rdy_Stop')), tag({view.params.tagPath} + '/Motor/Rdy_Stop'), null), null)
```


- `custom.qg15`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Sts_Stopped')), tag({view.params.tagPath} + '/Motor/Sts_Stopped'), null), null)
```


- `custom.qg16`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Sts_IOFault')), tag({view.params.tagPath} + '/Motor/Sts_IOFault'), null), null)
```


- `custom.qg17`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/RunTime/Val_TotRunHrs')), tag({view.params.tagPath} + '/RunTime/Val_TotRunHrs'), null), null)
```


- `custom.qg18`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/RunTime/Val_Starts')), tag({view.params.tagPath} + '/RunTime/Val_Starts'), null), null)
```


- `custom.qg19`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Cfg_FailToStartT')), tag({view.params.tagPath} + '/Motor/Cfg_FailToStartT'), null), null)
```


- `custom.qg20`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Nrdy_Disabled')), tag({view.params.tagPath} + '/Motor/Nrdy_Disabled'), null), null)
```


- `custom.qg21`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Nrdy_CfgErr')), tag({view.params.tagPath} + '/Motor/Nrdy_CfgErr'), null), null)
```


- `custom.qg22`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Nrdy_Intlk')), tag({view.params.tagPath} + '/Motor/Nrdy_Intlk'), null), null)
```


- `custom.qg23`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Nrdy_Perm')), tag({view.params.tagPath} + '/Motor/Nrdy_Perm'), null), null)
```


- `custom.qg24`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Nrdy_IOFault')), tag({view.params.tagPath} + '/Motor/Nrdy_IOFault'), null), null)
```


- `custom.qg25`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Nrdy_Fail')), tag({view.params.tagPath} + '/Motor/Nrdy_Fail'), null), null)
```


- `custom.qg26`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Nrdy_NoMode')), tag({view.params.tagPath} + '/Motor/Nrdy_NoMode'), null), null)
```


- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roCommand`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Command'], null), true)
```


- `custom.tipCommand`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roCommand}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Command' + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
```

waitOnAll: `False`

Transform 1, script:

```python
tagPath = ''
try:
    tagPath = self.view.params.tagPath
except:
    pass
if tagPath is None or str(tagPath).strip() == '':
    tagPath = 'No TagPath: ' + self.view.id.split('@')[0].split('/')[-1]
items = [
    {
        "text": "Ticket Logger",
        "icon": {
            "path": "material/info",
            "color": "--neutral-80",
            "style": {}
        },
        "style": {
            "classes": "bg-component Fonts/Value",
            "height": 24,
            "width": 120
        },
        "type": "message",
        "children": [],
        "link": {"url": "", "target": "self"},
        "method": {"name": "", "params": {}},
        "message": {
            "type": "ticketLog",
            "payload": {
                "tagPath": tagPath,
                "viewName": self.view.id.split('@')[0], 'sender': self.view.id
            },
            "scope": "page"
        }
    }
]
return items
```


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../common-patterns.md#pattern-1).

**`root/Modes`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/StatusSection/StatusBanner`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—',
	if(try(isNull({view.custom.qg0}), true),
		'COMM LOSS',
		if(
			coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg4}), null, {view.custom.qg4}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg5}), null, {view.custom.qg5}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg6}), null, {view.custom.qg6}), null), false),
			'FAULTED',
			case(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), 0),
				1, 'STOPPED',
				2, 'RUNNING',
				7, 'STOPPING',
				8, 'STARTING',
				33, 'DISABLED',
				'UNKNOWN'))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'Refridgeration_STS faceplate-status-banner',
	if(try(isNull({view.custom.qg0}), true),
		'Refridgeration_STS sts-COMMLOSS faceplate-status-banner',
		if(
			coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg4}), null, {view.custom.qg4}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg5}), null, {view.custom.qg5}), null), false) ||
			coalesce(try(if(isNull({view.custom.qg6}), null, {view.custom.qg6}), null), false),
			'Refridgeration_STS sts-FAULT faceplate-status-banner',
			case(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), 0),
				1, 'Refridgeration_STS sts-STOP faceplate-status-banner',
				2, 'Refridgeration_STS sts-RUN faceplate-status-banner',
				7, 'Refridgeration_STS sts-STOPPING faceplate-status-banner',
				8, 'Refridgeration_STS sts-STARTING faceplate-status-banner',
				33, 'Refridgeration_STS sts-STOP faceplate-status-banner',
				'Refridgeration_STS sts-UNKNOWN faceplate-status-banner'))))
```


**`root/StatusSection/PiChips/Perm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg7}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(!coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), true), 'NOT OK',
		if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), false), 'BYPASSED',
			if(coalesce(try(if(isNull({view.custom.qg9}), null, {view.custom.qg9}), null), true), 'OK', 'NOT OK')))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg7}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(!coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), true), 'faceplate-fault-state faceplate-fault-active',
		if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), false), 'faceplate-fault-state faceplate-bypass-banner',
			if(coalesce(try(if(isNull({view.custom.qg9}), null, {view.custom.qg9}), null), true), 'faceplate-fault-state faceplate-fault-ok', 'faceplate-fault-state faceplate-fault-active')))))
```


**`root/StatusSection/PiChips/Intlk/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg10}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(!coalesce(try(if(isNull({view.custom.qg10}), null, {view.custom.qg10}), null), true), 'NOT OK',
		if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), false), 'BYPASSED',
			if(coalesce(try(if(isNull({view.custom.qg11}), null, {view.custom.qg11}), null), true), 'OK', 'NOT OK')))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg10}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(!coalesce(try(if(isNull({view.custom.qg10}), null, {view.custom.qg10}), null), true), 'faceplate-fault-state faceplate-fault-active',
		if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), false), 'faceplate-fault-state faceplate-bypass-banner',
			if(coalesce(try(if(isNull({view.custom.qg11}), null, {view.custom.qg11}), null), true), 'faceplate-fault-state faceplate-fault-ok', 'faceplate-fault-state faceplate-fault-active')))))
```


**`root/StatusSection/PiChips/Bypass/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg8}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), false), 'ACTIVE', 'OFF')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg8}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), false), 'faceplate-fault-state faceplate-bypass-banner', 'faceplate-fault-state faceplate-fault-ok')))
```


**`root/StatusSection/CmdRow/BtnStart`**

- `props.enabled`: expression

```js
(!{view.custom.roCommand} && coalesce(try(if(isNull({view.custom.qg12}), null, {view.custom.qg12}), null), true)) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-cmd-btn Fonts/Label',
	if(coalesce(try(if(isNull({view.custom.qg13}), null, {view.custom.qg13}), null), false),
		'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label',
		'faceplate-cmd-btn Fonts/Label'))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/StatusSection/CmdRow/BtnStop`**

- `props.enabled`: expression

```js
(!{view.custom.roCommand} && coalesce(try(if(isNull({view.custom.qg14}), null, {view.custom.qg14}), null), true)) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-cmd-btn Fonts/Label',
	if(coalesce(try(if(isNull({view.custom.qg15}), null, {view.custom.qg15}), null), false),
		'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label',
		'faceplate-cmd-btn Fonts/Label'))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/StatusSection/CmdRow/BtnReset`**

- `props.enabled`: expression

```js
(!{view.custom.roCommand}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/FaultsSection`**

- `position.display`: expression

```js
try(!isNull({view.custom.qg1}), false) || try(!isNull({view.custom.qg2}), false) || try(!isNull({view.custom.qg3}), false) || try(!isNull({view.custom.qg4}), false) || try(!isNull({view.custom.qg5}), false) || try(!isNull({view.custom.qg16}), false)
```


**`root/FaultsSection/FaultChips/FailToStartAlm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/FaultsSection/FaultChips/FailToStopAlm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg2}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg2}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/FaultsSection/FaultChips/IOFaultAlm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg3}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg3}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/FaultsSection/FaultChips/IntlkTripAlm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg4}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg4}), null, {view.custom.qg4}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg4}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg4}), null, {view.custom.qg4}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/FaultsSection/FaultChips/FailToStartSts/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg5}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg5}), null, {view.custom.qg5}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg5}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg5}), null, {view.custom.qg5}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/FaultsSection/FaultChips/IOFaultSts/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg16}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg16}), null, {view.custom.qg16}), null), false),
		'FAULT', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg16}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg16}), null, {view.custom.qg16}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/KpiSection/Runtime/RuntimeVal`**

- `props.text`: expression

```js
coalesce(try(if({view.params.tagPath} = '', '', numberFormat(toFloat({view.custom.qg17}), '#0.0')), null), '—')
```


- `props.style.classes`: expression

```js
if(isNull(try(if({view.params.tagPath} = '', '', numberFormat(toFloat({view.custom.qg17}), '#0.0')), null)), 'Fonts/Value value-bad', 'Fonts/Value')
```


**`root/KpiSection/Starts/StartsVal`**

- `props.text`: expression

```js
coalesce(try(if({view.params.tagPath} = '', '', numberFormat(toFloat({view.custom.qg18}), '#0')), null), '—')
```


- `props.style.classes`: expression

```js
if(isNull(try(if({view.params.tagPath} = '', '', numberFormat(toFloat({view.custom.qg18}), '#0')), null)), 'Fonts/Value value-bad', 'Fonts/Value')
```


**`root/KpiSection/FailTimer/FailTimerVal`**

- `props.text`: expression

```js
coalesce(try(if({view.params.tagPath} = '', '', numberFormat(toFloat({view.custom.qg19}), '#0.0')), null), '—')
```


- `props.style.classes`: expression

```js
if(isNull(try(if({view.params.tagPath} = '', '', numberFormat(toFloat({view.custom.qg19}), '#0.0')), null)), 'Fonts/Value value-bad', 'Fonts/Value')
```


**`root/NotReadySection/Rows/NrdyDisabled/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg20}), null, {view.custom.qg20}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyCfgErr/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg21}), null, {view.custom.qg21}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyIntlk/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg22}), null, {view.custom.qg22}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyPerm/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg23}), null, {view.custom.qg23}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyIOFault/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg24}), null, {view.custom.qg24}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyFail/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg25}), null, {view.custom.qg25}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyNoMode/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg26}), null, {view.custom.qg26}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```

</details>

## Event Scripts And Handlers

- **`root/StatusSection/StatusBanner`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Motor/Val_Sts')
```

- **`root/StatusSection/PiChips/Intlk`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
qv = system.tag.readBlocking([base + '/Motor/Cfg_HasIntlkObj'])[0]
if qv.quality.isGood() and qv.value:
    system.perspective.sendMessage('faceplateSelectTab', {'tab': 'Interlocks', 'tagPath': base}, scope='page')
```

- **`root/StatusSection/CmdRow/BtnStart`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.startPump(base)
```

- **`root/StatusSection/CmdRow/BtnStop`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.stopPump(base)
```

- **`root/StatusSection/CmdRow/BtnReset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.resetPump(base)
```

- **`root/KpiSection/Runtime/RuntimeVal`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/RunTime/Val_TotRunHrs')
```

- **`root/KpiSection/Starts/StartsVal`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/RunTime/Val_Starts')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Modes](../modes.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

<details>
<summary>30 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 26 | style class |
| `Fonts/Value` | 3 | style class |
| `Refridgeration_STS` | 1 | stylesheet |
| `faceplate-cmd-btn` | 3 | style class |
| `faceplate-cmd-row` | 1 | stylesheet |
| `faceplate-cmd-row-fill` | 1 | stylesheet |
| `faceplate-fault-chip` | 9 | style class |
| `faceplate-fault-chips` | 2 | stylesheet |
| `faceplate-fault-code` | 9 | style class |
| `faceplate-fault-ok` | 9 | stylesheet |
| `faceplate-fault-state` | 9 | stylesheet |
| `faceplate-kpi-label` | 3 | style class |
| `faceplate-kpi-row` | 3 | stylesheet |
| `faceplate-nrdy-dot` | 7 | stylesheet |
| `faceplate-nrdy-label` | 7 | stylesheet |
| `faceplate-section` | 4 | style class |
| `faceplate-section-card` | 4 | style class |
| `faceplate-section-title` | 4 | style class |
| `faceplate-status-banner` | 1 | stylesheet |
| `faceplate-bypass-banner` | bound | style class |
| `faceplate-cmd-btn-active` | bound | style class |
| `faceplate-fault-active` | bound | stylesheet |
| `faceplate-nrdy-active` | bound | stylesheet |
| `sts-COMMLOSS` | bound | stylesheet |
| `sts-FAULT` | bound | stylesheet |
| `sts-RUN` | bound | stylesheet |
| `sts-STARTING` | bound | stylesheet |
| `sts-STOP` | bound | stylesheet |
| `sts-STOPPING` | bound | stylesheet |
| `sts-UNKNOWN` | bound | stylesheet |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>32 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Intlk/Sts_BypActive`, `/Intlk/Sts_IntlkOK`, `/Intlk/Sts_NBIntlkOK`, `/Motor/Alm_FailToStart`, `/Motor/Alm_FailToStop`, `/Motor/Alm_IOFault`, `/Motor/Alm_IntlkTrip`, `/Motor/Cfg_FailToStartT`, `/Motor/Cfg_HasIntlkObj`, `/Motor/Inp_NBPermOK`, `/Motor/Inp_PermOK`, `/Motor/Nrdy_CfgErr`, `/Motor/Nrdy_Disabled`, `/Motor/Nrdy_Fail`, `/Motor/Nrdy_IOFault`, `/Motor/Nrdy_Intlk`, `/Motor/Nrdy_NoMode`, `/Motor/Nrdy_Perm`, `/Motor/Rdy_Start`, `/Motor/Rdy_Stop`, `/Motor/Sts_FailToStart`, `/Motor/Sts_FailToStop`, `/Motor/Sts_IOFault`, `/Motor/Sts_Running`, `/Motor/Sts_Stopped`, `/Motor/Val_Sts`, `/RunTime/Val_Starts`, `/RunTime/Val_TotRunHrs`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
