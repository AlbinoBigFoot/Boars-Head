---
title: "HistoryActions"
sidebar_label: "HistoryActions"
description: "Perspective view 00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions (Asset (embedded piece)): 3 components, 4 bindings, 2 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions", "HistoryActions"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; Forms &gt; \_Assets &gt; HistoryActions |
| Root | `ia.container.flex`, height 34, width 200 |
| Size | 3 components, 4 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-11T03:55:53Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `value` | `""` | input |

## Component Tree

Component types: ia.input.button x2, ia.container.flex x1.

```text
root  ia.container.flex  [2 bindings]
  View  ia.input.button  [2 bindings; 1 event]
  Pdf  ia.input.button  [1 event]
```

## Bindings

4 bindings: expr 4.

**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../../common-patterns.md#pattern-3).

**`root/View`**

- `position.display`: expression

```js
!(indexOf(coalesce({view.params.value}, ''), 'PidCycle') = 0) || indexOf(coalesce({view.params.value}, ''), ':Open') > 0
```


- `props.text`: expression

```js
if(indexOf(coalesce({view.params.value}, ''), 'PidCycle') = 0, 'Open', 'View')
```


## Event Scripts And Handlers

- **`root/View`** `component.onActionPerformed`, script action, scope `G`

```python
parts = str(self.view.params.value or '').split(':')
if len(parts) < 2:
    return
kind, rid = parts[0], parts[1]
paths = {'DailyRounds': '00_Pages/Groveport/Operations/Forms/DailyRounds', 'ShiftLog': '00_Pages/Groveport/Operations/Forms/ShiftLog'}
if kind == 'PidCycle':
    system.perspective.navigate('/operations/forms/pid-verification')
    return
system.perspective.openPopup(id='opsFormView', view=paths[kind], params={'readOnly': True, 'submissionId': int(rid)}, title='', showCloseIcon=True, draggable=True, resizable=True, modal=True, overlayDismiss=True, position={'width': 1560, 'height': 880})
```

- **`root/Pdf`** `component.onActionPerformed`, script action, scope `G`

```python
parts = str(self.view.params.value or '').split(':')
if len(parts) >= 2:
    shared.Forms.downloadPdf(self.session, parts[0], int(parts[1]))
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [00\_Pages/Groveport/Operations/Forms/DailyRounds](../dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](../shiftlog.md)

**Opened or named by** (1): [00\_Pages/Groveport/Operations/Forms/History](../history.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `faceplate-cmd-btn` | 2 | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
