---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Valve/Controls (Asset (embedded piece)): 57 components, 57 bindings, 2 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Valve/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Valve/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Valve/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Valve &gt; Controls |
| Root | `ia.container.flex`, height 420, width 520 |
| Size | 57 components, 57 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

<details>
<summary>26 custom properties</summary>

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

</details>

## Component Tree

Component types: ia.display.label x33, ia.container.flex x22, ia.display.view x2.

<details>
<summary>Component tree (57 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Modes  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Modes]
  StatusSection  ia.container.flex
    StatusTitle  ia.display.label
    StatusBanner  ia.display.label  [2 bindings; 1 event]
    LsChips  ia.container.flex
      Perm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Intlk  ia.container.flex  [1 event]
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Bypass  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      OpenLs  ia.container.flex  [1 binding]
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      ClosedLs  ia.container.flex  [1 binding]
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
  FaultsSection  ia.container.flex  [1 binding]
    FaultsTitle  ia.display.label
    FaultChips  ia.container.flex
      Failed  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Comm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
  CommandsSection  ia.container.flex
    CommandsTitle  ia.display.label
    CmdEmbed  ia.display.view  [2 bindings; view: (bound)]
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

57 bindings: expr 53, expr-struct 2, property 2.

<details>
<summary>All 57 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Val_Sts')), tag({view.params.tagPath} + '/Valve/Val_Sts'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Nrdy_Fail')), tag({view.params.tagPath} + '/Valve/Nrdy_Fail'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Alm_IOFault')), tag({view.params.tagPath} + '/Valve/Alm_IOFault'), null), null)
```


- `custom.qg3`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Alm_FullStall')), tag({view.params.tagPath} + '/Valve/Alm_FullStall'), null), null)
```


- `custom.qg4`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Alm_TransitStall')), tag({view.params.tagPath} + '/Valve/Alm_TransitStall'), null), null)
```


- `custom.qg5`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Alm_IntlkTrip')), tag({view.params.tagPath} + '/Valve/Alm_IntlkTrip'), null), null)
```


- `custom.qg6`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Inp_NBPermOK')), tag({view.params.tagPath} + '/Valve/Inp_NBPermOK'), null), null)
```


- `custom.qg7`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Sts_BypActive')), tag({view.params.tagPath} + '/Valve/Sts_BypActive'), null), null)
```


- `custom.qg8`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Inp_PermOK')), tag({view.params.tagPath} + '/Valve/Inp_PermOK'), null), null)
```


- `custom.qg9`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Inp_NBIntlkOK')), tag({view.params.tagPath} + '/Valve/Inp_NBIntlkOK'), null), null)
```


- `custom.qg10`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Inp_IntlkOK')), tag({view.params.tagPath} + '/Valve/Inp_IntlkOK'), null), null)
```


- `custom.qg11`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Sts_Bypass')), tag({view.params.tagPath} + '/Valve/Sts_Bypass'), null), null)
```


- `custom.qg12`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Cfg_HasOpenLS')), tag({view.params.tagPath} + '/Valve/Cfg_HasOpenLS'), null), null)
```


- `custom.qg13`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Inp_OpenLS')), tag({view.params.tagPath} + '/Valve/Inp_OpenLS'), null), null)
```


- `custom.qg14`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Cfg_HasClosedLS')), tag({view.params.tagPath} + '/Valve/Cfg_HasClosedLS'), null), null)
```


- `custom.qg15`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Inp_ClosedLS')), tag({view.params.tagPath} + '/Valve/Inp_ClosedLS'), null), null)
```


- `custom.qg16`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Sts_IOFault')), tag({view.params.tagPath} + '/Valve/Sts_IOFault'), null), null)
```


- `custom.qg17`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/valveType/Value')), tag({view.params.tagPath} + '/valveType/Value'), null), null)
```


- `custom.qg18`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/valveType')), tag({view.params.tagPath} + '/valveType'), null), null)
```


- `custom.qg19`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Nrdy_Disabled')), tag({view.params.tagPath} + '/Valve/Nrdy_Disabled'), null), null)
```


- `custom.qg20`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Nrdy_CfgErr')), tag({view.params.tagPath} + '/Valve/Nrdy_CfgErr'), null), null)
```


- `custom.qg21`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Nrdy_Intlk')), tag({view.params.tagPath} + '/Valve/Nrdy_Intlk'), null), null)
```


- `custom.qg22`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Nrdy_Perm')), tag({view.params.tagPath} + '/Valve/Nrdy_Perm'), null), null)
```


- `custom.qg23`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Nrdy_IOFault')), tag({view.params.tagPath} + '/Valve/Nrdy_IOFault'), null), null)
```


- `custom.qg24`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Nrdy_NoMode')), tag({view.params.tagPath} + '/Valve/Nrdy_NoMode'), null), null)
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
			coalesce(try(if(isNull({view.custom.qg5}), null, {view.custom.qg5}), null), false),
			'FAULTED',
			case(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), 0),
				1, 'CLOSED',
				2, 'OPEN',
				5, 'CLOSING',
				6, 'OPENING',
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
			coalesce(try(if(isNull({view.custom.qg5}), null, {view.custom.qg5}), null), false),
			'Refridgeration_STS sts-FAULT faceplate-status-banner',
			case(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), 0),
				1, 'Refridgeration_STS sts-STOP faceplate-status-banner',
				2, 'Refridgeration_STS sts-RUN faceplate-status-banner',
				5, 'Refridgeration_STS sts-STOPPING faceplate-status-banner',
				6, 'Refridgeration_STS sts-STARTING faceplate-status-banner',
				33, 'Refridgeration_STS sts-OFF faceplate-status-banner',
				'Refridgeration_STS sts-UNKNOWN faceplate-status-banner'))))
```


**`root/StatusSection/LsChips/Perm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg6}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(!coalesce(try(if(isNull({view.custom.qg6}), null, {view.custom.qg6}), null), true), 'NOT OK',
		if(coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), false), 'BYPASSED',
			if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), true), 'OK', 'NOT OK')))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg6}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(!coalesce(try(if(isNull({view.custom.qg6}), null, {view.custom.qg6}), null), true), 'faceplate-fault-state faceplate-fault-active',
		if(coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), false), 'faceplate-fault-state faceplate-bypass-banner',
			if(coalesce(try(if(isNull({view.custom.qg8}), null, {view.custom.qg8}), null), true), 'faceplate-fault-state faceplate-fault-ok', 'faceplate-fault-state faceplate-fault-active')))))
```


**`root/StatusSection/LsChips/Intlk/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg9}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(!coalesce(try(if(isNull({view.custom.qg9}), null, {view.custom.qg9}), null), true), 'NOT OK',
		if(coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), false), 'BYPASSED',
			if(coalesce(try(if(isNull({view.custom.qg10}), null, {view.custom.qg10}), null), true), 'OK', 'NOT OK')))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg9}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(!coalesce(try(if(isNull({view.custom.qg9}), null, {view.custom.qg9}), null), true), 'faceplate-fault-state faceplate-fault-active',
		if(coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), false), 'faceplate-fault-state faceplate-bypass-banner',
			if(coalesce(try(if(isNull({view.custom.qg10}), null, {view.custom.qg10}), null), true), 'faceplate-fault-state faceplate-fault-ok', 'faceplate-fault-state faceplate-fault-active')))))
```


**`root/StatusSection/LsChips/Bypass/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg7}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), false), 'ACTIVE',
		if(coalesce(try(if(isNull({view.custom.qg11}), null, {view.custom.qg11}), null), false), 'ON', 'OFF'))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg7}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg7}), null, {view.custom.qg7}), null), false), 'faceplate-fault-state faceplate-bypass-banner',
		if(coalesce(try(if(isNull({view.custom.qg11}), null, {view.custom.qg11}), null), false), 'faceplate-fault-state faceplate-bypass-banner', 'faceplate-fault-state faceplate-fault-ok'))))
```


**`root/StatusSection/LsChips/OpenLs`**

- `position.display`: expression

```js
coalesce(try(if(isNull({view.custom.qg12}), null, {view.custom.qg12}), null), false)
```


**`root/StatusSection/LsChips/OpenLs/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg13}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg13}), null, {view.custom.qg13}), null), false), 'ON', 'OFF')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg13}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg13}), null, {view.custom.qg13}), null), false),
		'faceplate-fault-state faceplate-ls-on',
		'faceplate-fault-state faceplate-ls-off')))
```


**`root/StatusSection/LsChips/ClosedLs`**

- `position.display`: expression

```js
coalesce(try(if(isNull({view.custom.qg14}), null, {view.custom.qg14}), null), false)
```


**`root/StatusSection/LsChips/ClosedLs/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg15}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg15}), null, {view.custom.qg15}), null), false), 'ON', 'OFF')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg15}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg15}), null, {view.custom.qg15}), null), false),
		'faceplate-fault-state faceplate-ls-on',
		'faceplate-fault-state faceplate-ls-off')))
```


**`root/FaultsSection`**

- `position.display`: expression

```js
try(!isNull({view.custom.qg1}), false) || try(!isNull({view.custom.qg16}), false)
```


**`root/FaultsSection/FaultChips/Failed/State`**

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


**`root/FaultsSection/FaultChips/Comm/State`**

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


**`root/CommandsSection/CmdEmbed`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `props.path`: expression

```js
case(
	if({view.params.tagPath} = '', 'SO',
		upper(coalesce(
			try(if(isNull({view.custom.qg17}), null, {view.custom.qg17}), null),
			try(if(isNull({view.custom.qg18}), null, {view.custom.qg18}), null),
			'SO'))),
	'SO', '01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO',
	'MO', '01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO',
	'MP', '01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position',
	'C', '01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position',
	'01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO')
```


**`root/NotReadySection/Rows/NrdyDisabled/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg19}), null, {view.custom.qg19}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyCfgErr/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg20}), null, {view.custom.qg20}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyIntlk/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg21}), null, {view.custom.qg21}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyPerm/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg22}), null, {view.custom.qg22}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyIOFault/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg23}), null, {view.custom.qg23}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyFail/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```


**`root/NotReadySection/Rows/NrdyNoMode/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-nrdy-dot',
	if(coalesce(try(if(isNull({view.custom.qg24}), null, {view.custom.qg24}), null), false),
		'faceplate-nrdy-dot faceplate-nrdy-active',
		'faceplate-nrdy-dot'))
```

</details>

## Event Scripts And Handlers

- **`root/StatusSection/StatusBanner`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Valve/Val_Sts')
```

- **`root/StatusSection/LsChips/Intlk`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
qv = system.tag.readBlocking([base + '/Valve/Cfg_HasIntlkObj'])[0]
if qv.quality.isGood() and qv.value:
    system.perspective.sendMessage('faceplateSelectTab', {'tab': 'Interlocks', 'tagPath': base}, scope='page')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Modes](../modes.md)

**Bound embeds** (view path set by a binding): `root/CommandsSection/CmdEmbed`

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_Position](./cmd-position.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./cmd-so.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

<details>
<summary>25 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 18 | style class |
| `Refridgeration_STS` | 1 | stylesheet |
| `faceplate-fault-chip` | 7 | style class |
| `faceplate-fault-code` | 7 | style class |
| `faceplate-fault-ok` | 5 | stylesheet |
| `faceplate-fault-state` | 7 | stylesheet |
| `faceplate-ls-off` | 2 | stylesheet |
| `faceplate-nrdy-dot` | 7 | stylesheet |
| `faceplate-nrdy-label` | 7 | stylesheet |
| `faceplate-section` | 4 | style class |
| `faceplate-section-card` | 4 | style class |
| `faceplate-section-title` | 4 | style class |
| `faceplate-status-banner` | 1 | stylesheet |
| `faceplate-bypass-banner` | bound | style class |
| `faceplate-fault-active` | bound | stylesheet |
| `faceplate-ls-on` | bound | stylesheet |
| `faceplate-nrdy-active` | bound | stylesheet |
| `sts-COMMLOSS` | bound | stylesheet |
| `sts-FAULT` | bound | stylesheet |
| `sts-OFF` | bound | stylesheet |
| `sts-RUN` | bound | stylesheet |
| `sts-STARTING` | bound | stylesheet |
| `sts-STOP` | bound | stylesheet |
| `sts-STOPPING` | bound | stylesheet |
| `sts-UNKNOWN` | bound | stylesheet |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>30 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Valve/Alm_FullStall`, `/Valve/Alm_IOFault`, `/Valve/Alm_IntlkTrip`, `/Valve/Alm_TransitStall`, `/Valve/Cfg_HasClosedLS`, `/Valve/Cfg_HasIntlkObj`, `/Valve/Cfg_HasOpenLS`, `/Valve/Inp_ClosedLS`, `/Valve/Inp_IntlkOK`, `/Valve/Inp_NBIntlkOK`, `/Valve/Inp_NBPermOK`, `/Valve/Inp_OpenLS`, `/Valve/Inp_PermOK`, `/Valve/Nrdy_CfgErr`, `/Valve/Nrdy_Disabled`, `/Valve/Nrdy_Fail`, `/Valve/Nrdy_IOFault`, `/Valve/Nrdy_Intlk`, `/Valve/Nrdy_NoMode`, `/Valve/Nrdy_Perm`, `/Valve/Sts_BypActive`, `/Valve/Sts_Bypass`, `/Valve/Sts_IOFault`, `/Valve/Val_Sts`, `/valveType`, `/valveType/Value`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
