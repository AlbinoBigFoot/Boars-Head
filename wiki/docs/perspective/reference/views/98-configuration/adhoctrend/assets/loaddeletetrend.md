---
title: "LoadDeleteTrend"
sidebar_label: "LoadDeleteTrend"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend (Asset (embedded piece)): 3 components, 3 bindings, 2 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend", "LoadDeleteTrend"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; LoadDeleteTrend |
| Root | `ia.container.flex`, height 40, width 180 |
| Size | 3 components, 3 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:40:04Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `rowData` | `""` | input |

## Component Tree

Component types: ia.input.button x2, ia.container.flex x1.

```text
root  ia.container.flex  [2 bindings]
  LoadButton  ia.input.button  [1 event]
  DeleteButton  ia.input.button  [1 binding; 1 event]
```

## Bindings

3 bindings: expr-struct 3.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/DeleteButton`**

- `meta.visible`: structured expression (expr-struct), then script transform

```js
rowData: {view.params.rowData}
username: {session.props.auth.user.userName}
admin: coalesce({session.custom.Permissions.Trends.ManageLocked}, false)
```

waitOnAll: `True`

Transform 1, script:

```python
# Owner deletes their own trend; locked (system) trends only Trends/ManageLocked (2026-09-29).
# Unauthenticated sessions report blank userName; saves use "anonymous".
if not value.rowData or "username" not in value.rowData:
    return False
locked = False
try:
    locked = bool(value.rowData["is_locked"])
except:
    pass
if value.admin:
    return True
if locked:
    return False
session_user = value.username if value.username else "anonymous"
return session_user == value.rowData["username"]
```


## Event Scripts And Handlers

- **`root/LoadButton`** `component.onActionPerformed`, script action, scope `G`

```python
from shared import Alerts

row = self.view.params.rowData
if not row:
    Alerts.showAlert(
        state="warning",
        title="Cannot Load",
        message="Missing trend row data.",
        showCloseBtn=True,
        btnTextPrimary="OK",
        btnActionPrimary="closeAlert"
    )
    return

defaults = {
    "tags": [],
    "colors": ["#008FFB", "#34C759", "#FFA726", "#FF4560", "#775DD0", "#1C4E80", "#008080", "#26C6DA", "#4F4F4F", "#6C757D"],
    "realtime": True,
    "timeRange": 1,
    "pointCount": 120,
    "chartType": "line",
    "aggregate": "Average",
    "trendId": "",
    "trendName": "",
    "username": "",
# ... 27 more line(s): see the view.json
```

- **`root/DeleteButton`** `component.onActionPerformed`, script action, scope `G`

```python
from shared import Alerts

row = self.view.params.rowData
if not row:
    return
payload_data = {"trendId": row.id}
Alerts.showAlert(
    state="info",
    title="Confirm Deletion",
    message="Are you sure you want to permanently delete this custom trend?",
    showCloseBtn=False,
    btnTextPrimary="Delete",
    btnIconPrimary="material/delete",
    btnActionPrimary="TrendDeleteConfirm",
    btnTextSecondary="Cancel",
    btnIconSecondary="material/cancel",
    btnActionSecondary="TrendDeleteCancel",
    payload=payload_data
)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.AdhocTrend.default\_plots](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_pen\_plots](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_plots](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [98\_Configuration/AdhocTrend/UserSavedTrendConfig](../usersavedtrendconfig.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Container/Button` | 2 | no rule found |
| `adhoc-trend-load-delete-btn` | 2 | stylesheet |
| `adhoc-trend-load-delete-row` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
