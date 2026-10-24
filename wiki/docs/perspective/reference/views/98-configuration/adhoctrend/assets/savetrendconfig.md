---
title: "SaveTrendConfig"
sidebar_label: "SaveTrendConfig"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/SaveTrendConfig (Asset (embedded piece)): 11 components, 5 bindings, 2 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/SaveTrendConfig", "SaveTrendConfig"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/SaveTrendConfig`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/SaveTrendConfig/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; SaveTrendConfig |
| Root | `ia.container.flex`, height 260, width 380 |
| Size | 11 components, 5 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:40:04Z by the Designer |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x3, ia.input.button x2, ia.input.text-field x1, ia.input.toggle-switch x1.

```text
root  ia.container.flex  [2 bindings]
  Label  ia.display.label
  TrendName  ia.container.flex
    Label  ia.display.label
    TextField  ia.input.text-field  [1 binding]
  ShareToggle  ia.container.flex
    Label  ia.display.label
    ToggleSwitch  ia.input.toggle-switch  [1 binding]
  Buttons  ia.container.flex
    Cancel  ia.input.button  [1 binding; 1 event]
    Save  ia.input.button  [1 event]
```

## Bindings

5 bindings: property 3, expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/TrendName/TextField`**

- `props.text`: property `session.custom.AdhocTrend.trendName` (bidirectional)

**`root/ShareToggle/ToggleSwitch`**

- `props.selected`: property `session.custom.AdhocTrend.isShared` (bidirectional)

**`root/Buttons/Cancel`**

- `custom.id`: property `session.props.auth.user.id`, then expression transform

Transform 1, expression:

```js
'SaveTrendConfig-' + coalesce(toString({value}), 'anon')
```


## Event Scripts And Handlers

- **`root/Buttons/Cancel`** `component.onActionPerformed`, popup action, scope `C`: close popup `{/root/Buttons/Cancel.custom.id}`, view [98\_Configuration/AdhocTrend/\_Assets/SaveTrendConfig](./savetrendconfig.md)

- **`root/Buttons/Save`** `component.onActionPerformed`, script action, scope `G`

```python
# security-tiers: Trends/Save in Roles & Permissions (own trends; every tier by default)
if not shared.Security.allowed(self.session, 'Trends', 'Save'):
    return
from shared import Alerts

trendId = self.session.custom.AdhocTrend.trendId
trendName = self.session.custom.AdhocTrend.trendName
isShared = self.session.custom.AdhocTrend.isShared
username = self.session.props.auth.user.userName
if not username:
    username = "anonymous"

try:
    popupId = self.getSibling("Cancel").custom.id
except:
    uid = self.session.props.auth.user.id
    popupId = "SaveTrendConfig-" + (str(uid) if uid not in (None, "") else "anon")

def _close_save_popup():
    candidates = [popupId]
    try:
        candidates.append(str(popupId).strip())
    except:
        pass
    candidates.extend(["SaveTrendConfig", "SaveTrendConfig ", "SaveTrendConfig-anon"])
# ... 83 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Security.allowed](../../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Opened or named by** (1): [98\_Configuration/AdhocTrend/Trend](../trend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 2 | style class |
| `Fonts/Value` | 1 | style class |
| `adhoc-trend-save-dialog` | 1 | stylesheet |
| `adhoc-trend-save-label` | 1 | stylesheet |
| `adhoc-trend-save-title` | 1 | stylesheet |
| `adhoc-trend-share-label` | 1 | stylesheet |
| `bg-component` | 1 | stylesheet |
| `container-button` | 2 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
