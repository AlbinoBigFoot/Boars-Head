---
title: "TypeTable"
sidebar_label: "TypeTable"
description: "Perspective view 00_Pages/Boars Head/Devices/TypeTable (Page piece (not routed)): 2 components, 5 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Devices/TypeTable", "TypeTable"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Devices/TypeTable`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Devices/TypeTable` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Devices/TypeTable/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Devices &gt; TypeTable |
| Root | `ia.container.flex`, no default size |
| Size | 2 components, 5 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `typeId` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.table x1.

```text
root  ia.container.flex  [2 bindings]
  Table  ia.display.table  [3 bindings; 1 event]
```

## Bindings

5 bindings: expr-struct 4, expr 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Table`**

- `props.columns`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
typeId: {view.params.typeId}
instances: tag(toString({view.params.tagPath}) + '/Overview/Instances/Value')
```

waitOnAll: `False`

Transform 1, script:

```python
tagPath = value.get('tagPath')
typeId = value.get('typeId') or ''
instances = value.get('instances')
def _rows(p):
    try:
        return p.get('data') or []
    except:
        try:
            return p['data'] or []
        except:
            return []
def _cols(p):
    try:
        return p.get('columns') or []
    except:
        try:
            return p['columns'] or []
        except:
            return []
# typeId filter (mixed folders) wins; else Overview/Instances when rebuilt; else live browse.
if typeId:
    payload = shared.Overview.buildInstancesPayloadForType(tagPath, typeId)
elif instances and _rows(instances) and len(_cols(instances)) > 1:
    payload = instances
else:
    payload = shared.Overview.buildInstancesPayload(tagPath)
    if not _rows(payload) and instances and _rows(instances):
        payload = instances
if not payload:
    return []
# Plain-English headers, default column set, hidden internals (shared.DevicePages.COLUMNS)
return shared.DevicePages.applyColumns(_cols(payload), typeId)
```


- `props.data`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
typeId: {view.params.typeId}
instances: tag(toString({view.params.tagPath}) + '/Overview/Instances/Value')
```

waitOnAll: `False`

Transform 1, script:

```python
tagPath = value.get('tagPath')
typeId = value.get('typeId') or ''
instances = value.get('instances')
def _rows(p):
    try:
        return p.get('data') or []
    except:
        try:
            return p['data'] or []
        except:
            return []
def _cols(p):
    try:
        return p.get('columns') or []
    except:
        try:
            return p['columns'] or []
        except:
            return []
# typeId filter (mixed folders) wins; else Overview/Instances when rebuilt; else live browse.
if typeId:
    payload = shared.Overview.buildInstancesPayloadForType(tagPath, typeId)
elif instances and _rows(instances) and len(_cols(instances)) > 1:
    payload = instances
else:
    payload = shared.Overview.buildInstancesPayload(tagPath)
    if not _rows(payload) and instances and _rows(instances):
        payload = instances
if not payload:
    return []
return shared.Pax.mapRows(_rows(payload))  # pax-bindings: cached Overview rows -> PAX members
```


- `props.rows.style.cursor`: expression

```js
if(right(coalesce({view.params.typeId}, ''), 10) = 'ExhaustFan', 'default', 'pointer')
```


## Event Scripts And Handlers

- **`root/Table`** `component.onRowClick`, script action, scope `G`

```python
row = None
try:
    row = event.value
except:
    row = None
if not row:
    try:
        row = self.props.selection.data[0]
    except:
        return
tagPath = ''
try:
    tagPath = str(row['tagPath'] or '')
except:
    tagPath = ''
# Same faceplate the device graphic / nav tree leaf opens; status-only types open nothing
if tagPath and shared.DevicePages.hasFaceplate(self.view.params.typeId):
    Navigation.Faceplate.openDevice(tagPath)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.DevicePages.COLUMNS](../../../../../../scripting/reference/modules/shared-devicepages.md), [shared.DevicePages.applyColumns](../../../../../../scripting/reference/modules/shared-devicepages.md), [shared.DevicePages.hasFaceplate](../../../../../../scripting/reference/modules/shared-devicepages.md), [shared.Overview.buildInstancesPayload](../../../../../../scripting/reference/modules/shared-overview.md), [shared.Overview.buildInstancesPayloadForType](../../../../../../scripting/reference/modules/shared-overview.md), [shared.Pax.mapRows](../../../../../../scripting/reference/modules/shared-pax.md).

## Related Views

**Embedded in** (6): [00\_Pages/Boars Head/ExhaustFans/Details](../exhaustfans/details.md), [00\_Pages/Boars Head/Pumps/Details](../pumps/details.md), [00\_Pages/Boars Head/Sensors/Details](../sensors/details.md), [00\_Pages/Boars Head/Tanks/Details](../tanks/details.md), [00\_Pages/Boars Head/Valves/Details](../valves/details.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Details](../../groveport/machine-room/utility/compressors/details.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-container` | 1 | stylesheet |
| `container-card` | 1 | stylesheet |
| `unit-overview-host` | 1 | stylesheet |
| `unit-overview-table` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/Overview/Instances/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
