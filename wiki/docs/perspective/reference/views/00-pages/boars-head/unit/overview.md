---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Boars Head/Unit/Overview (Page piece (not routed)): 2 components, 4 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Unit/Overview", "Overview"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Unit/Overview`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Unit/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Unit/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Unit &gt; Overview |
| Root | `ia.container.flex`, no default size |
| Size | 2 components, 4 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T15:48:22Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Evaporators"` | input |
| `typeId` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.table x1.

```text
root  ia.container.flex  [2 bindings]
  Table  ia.display.table  [2 bindings; 1 event]
```

## Bindings

4 bindings: expr-struct 4.

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
    if not p:
        return []
    try:
        return p.get('data') or []
    except:
        try:
            return p['data']
        except:
            return []
def _cols(p):
    if not p:
        return []
    try:
        return p.get('columns') or []
    except:
        try:
            return p['columns']
        except:
            return []
# typeId filter (mixed folders) wins; else prefer Overview/Instances when rebuilt
# (more than Device Name); else live-browse the equipment folder.
if typeId:
    payload = shared.Overview.buildInstancesPayloadForType(tagPath, typeId)
elif _rows(instances) and len(_cols(instances)) > 1:
    payload = instances
else:
    payload = shared.Overview.buildInstancesPayload(tagPath)
    if not _rows(payload) and _rows(instances):
        payload = instances
if not payload:
    return []
try:
    return payload.get('columns', [])
except:
    return payload['columns'] if payload else []
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
    if not p:
        return []
    try:
        return p.get('data') or []
    except:
        try:
            return p['data']
        except:
            return []
def _cols(p):
    if not p:
        return []
    try:
        return p.get('columns') or []
    except:
        try:
            return p['columns']
        except:
            return []
if typeId:
    payload = shared.Overview.buildInstancesPayloadForType(tagPath, typeId)
elif _rows(instances) and len(_cols(instances)) > 1:
    payload = instances
else:
    payload = shared.Overview.buildInstancesPayload(tagPath)
    if not _rows(payload) and _rows(instances):
        payload = instances
if not payload:
    return []
try:
    return payload.get('data', [])
except:
    return payload['data'] if payload else []
```


## Event Scripts And Handlers

- **`root/Table`** `component.onRowClick`, script action, scope `G`

```python
selectedData = self.props.selection.data[0]
if 'tagPath' not in selectedData.keys() or not selectedData['tagPath']:
    return
tagPath = str(selectedData['tagPath'])
typeId = ''
try:
    cfg = system.tag.getConfiguration(tagPath, False)
    if cfg:
        typeId = str(cfg[0].get('typeId') or '')
except:
    typeId = ''
leaf = typeId.split('/')[-1] if typeId else ''
typeFaceplates = {
    'Tank': 'Tank',
    'Compressor': 'Compressor',
    'Pump': 'Pump',
    'ExhaustFan': 'ExhaustFan',
    'Valve': 'SolenoidValve',
    'SolenoidValve': 'SolenoidValve',
    'Sensor': 'Sensor',
    'Evaporator': 'Evaporator',
    'CoolingTower': 'CoolingTower',
}
faceplate = typeFaceplates.get(leaf, leaf)
if not faceplate:
# ... 23 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Overview.buildInstancesPayload](../../../../../../scripting/reference/modules/shared-overview.md), [shared.Overview.buildInstancesPayloadForType](../../../../../../scripting/reference/modules/shared-overview.md).

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Devices/DetailsOverview](../devices/detailsoverview.md)

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
