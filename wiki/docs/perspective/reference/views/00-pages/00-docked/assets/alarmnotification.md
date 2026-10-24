---
title: "AlarmNotification"
sidebar_label: "AlarmNotification"
description: "Perspective view 00_Pages/00_Docked/_Assets/AlarmNotification (Asset (embedded piece)): 3 components, 7 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/AlarmNotification", "AlarmNotification"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/AlarmNotification`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/AlarmNotification` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/AlarmNotification/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; AlarmNotification |
| Root | `ia.container.flex`, height 36, width 36 |
| Size | 3 components, 7 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T07:26:16Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]"` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1, ia.display.label x1.

```text
root  ia.container.flex  [4 bindings; 1 event]
  Icon  ia.display.icon
  Count  ia.display.label  [3 bindings]
```

## Bindings

7 bindings: expr 7.

**`root`**

- `meta.tooltip.text`: expression

```js
if((coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) + coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeAckCount')), 0), 0)) = 0, 'No active alarms', toStr((coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) + coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeAckCount')), 0), 0))) + ' active alarm' + if((coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) + coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeAckCount')), 0), 0)) = 1, '', 's') + if(coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) > 0, ' (' + toStr(coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0)) + ' unacknowledged)', ''))
```


- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Count`**

- `props.text`: expression

```js
if((coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) + coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeAckCount')), 0), 0)) > 99, '99+', toStr((coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) + coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeAckCount')), 0), 0))))
```


- `meta.visible`: expression

```js
(coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) + coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeAckCount')), 0), 0)) > 0
```


- `props.style.classes`: expression

```js
'Fonts/Value header-alarm-count alarm-priority-' + case(coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.highestActivePriority')), -1), -1), 4, 'critical', 3, 'high', 2, 'medium', 1, 'low', 'low') + if(coalesce(try(toInt(tag(if(right({view.params.tagPath}, 1) = ']', {view.params.tagPath}, {view.params.tagPath} + '/') + 'Alarm Metrics.activeUnackCount')), 0), 0) > 0, ' alarm-flash', '')
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/alarms')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [00\_Pages/00\_Docked/Header](../header.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `color-icon` | 1 | style class |
| `header-alarm-count` | 1 | stylesheet |
| `header-icon` | 1 | stylesheet |
| `nav-menu-btn` | 1 | stylesheet |
| `alarm-flash` | bound | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
