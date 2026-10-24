---
title: "Summary"
sidebar_label: "Summary"
description: "Perspective view 00_Pages/Boars Head/Alarms/Summary (Page): 10 components, 4 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Alarms/Summary", "Summary", "/alarms"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/Alarms/Summary`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Alarms/Summary` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Alarms/Summary/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Alarms &gt; Summary |
| Routes | `/alarms` (Alarms) |
| Root | `ia.container.flex`, height 900, width 1200 |
| Size | 10 components, 4 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-23T19:45:31Z by the Designer |

## Component Tree

Component types: ia.display.label x4, ia.container.flex x2, ia.input.dropdown x2, ia.input.button x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Title  ia.display.label
  Subtitle  ia.display.label
  Filters  ia.container.flex
    DeviceTypeLabel  ia.display.label
    DeviceTypeDropdown  ia.input.dropdown
    AreaLabel  ia.display.label
    AreaDropdown  ia.input.dropdown
    GenerateReport  ia.input.button  [1 binding; 1 event]
  AlarmStatusTable  ia.display.view  [1 binding; view: 00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable]
```

## Bindings

4 bindings: expr-struct 3, expr 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Filters/GenerateReport`**

- `props.enabled`: expression

```js
coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/AlarmStatusTable`**

- `props.params.sourceFilter`: structured expression (expr-struct), then script transform

```js
types: {../Filters/DeviceTypeDropdown.props.value}
areas: {../Filters/AreaDropdown.props.value}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.Alarms.sourceFilter(value.types, value.areas)
```


## Event Scripts And Handlers

- **`root/Filters/GenerateReport`** `component.onActionPerformed`, script action, scope `G`

```python
# Report builder, pre-filled with the Alarms source and this page's Area filter
areas = self.parent.getChild('AreaDropdown').props.value or []
shared.Reports.open('alarms', {'areas': [str(a) for a in areas], 'origin': 'Alarm Status'})
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alarms.sourceFilter](../../../../../../scripting/reference/modules/shared-alarms.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/Boars Head/Alarms/\_Assets/AlarmStatusTable](./assets/alarmstatustable.md)

**Named in project scripts**: [Navigation.Nav](../../../../../../scripting/reference/modules/navigation-nav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 1 | style class |
| `Fonts/Label` | 3 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 2 | style class |
| `bg-component` | 2 | stylesheet |
| `bg-page` | 1 | style class |
| `container-card` | 2 | stylesheet |
| `fs-13` | 1 | style class |
| `fs-20` | 1 | style class |
| `fw-600` | 2 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
