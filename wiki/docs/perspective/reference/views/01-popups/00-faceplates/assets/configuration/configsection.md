---
title: "ConfigSection"
sidebar_label: "ConfigSection"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection (Asset (embedded piece)): 3 components, 5 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection", "ConfigSection"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Configuration &gt; ConfigSection |
| Root | `ia.container.flex`, height 140, width 400 |
| Size | 3 components, 5 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-19T16:34:51Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `rowsJson` | `"[]"` | input |
| `tagPath` | `""` | input |
| `title` | `""` | input |
| `engineering` | `false` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1, ia.display.flex-repeater x1.

```text
root  ia.container.flex  [3 bindings]
  Title  ia.display.label  [1 binding]
  Rows  ia.display.flex-repeater  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
```

## Bindings

5 bindings: expr 3, property 1, expr-struct 1.

**`root`**

- `position.display`: expression

```js
{view.params.tagPath} != ''
```


- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Title`**

- `props.text`: property `view.params.title`

**`root/Rows`**

- `props.instances`: structured expression (expr-struct), then script transform

```js
base: {view.params.tagPath}
rowsJson: {view.params.rowsJson}
engineering: coalesce({view.params.engineering}, false)
```

waitOnAll: `True`

Transform 1, script:

```python
import json
base = ''
raw = '[]'
try:
    base = str((value or {}).get('base') or '').strip()
except:
    base = ''
if not base:
    return []
try:
    raw = (value or {}).get('rowsJson')
except:
    raw = None
if raw is None or raw == '':
    raw = '[]'
elif not isinstance(raw, basestring):
    try:
        raw = json.dumps(raw)
    except:
        raw = '[]'
try:
    rows = json.loads(raw)
except:
    rows = []
pax = shared.Pax.part(shared.Pax.device(base))
out = []
for r in rows or []:
    if not isinstance(r, dict):
        continue
    leaf = str(r.get('leaf') or r.get('tag') or '').strip().strip('/')
    kind = str(r.get('kind') or r.get('inputKind') or 'checkbox').strip().lower() or 'checkbox'
    label = r.get('label') or leaf
    path = str(r.get('tagPath') or '').strip()
    paxPath = None
    if not path and leaf:
        paxPath = shared.Pax.resolve(base, leaf, pax)   # mapped device: the live PAX member, read only
        path = paxPath or (base.rstrip('/') + '/' + leaf)
        if not paxPath and not path.endswith('/Value'):
            path = path + '/Value'
    if not path:
# ... 12 more line(s): see the view.json
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Pax.device](../../../../../../../scripting/reference/modules/shared-pax.md), [shared.Pax.part](../../../../../../../scripting/reference/modules/shared-pax.md), [shared.Pax.resolve](../../../../../../../scripting/reference/modules/shared-pax.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./configfield.md) (flex repeater)

**Embedded in** (9): [01\_Popups/00\_Faceplates/\_Assets/Compressor/Configuration](../compressor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](../dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Configuration](../evaporator/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](../evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](../interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](../pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](../suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](../tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](../valve/configuration.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
