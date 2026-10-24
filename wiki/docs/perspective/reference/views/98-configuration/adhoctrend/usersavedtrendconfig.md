---
title: "UserSavedTrendConfig"
sidebar_label: "UserSavedTrendConfig"
description: "Perspective view 98_Configuration/AdhocTrend/UserSavedTrendConfig (Page): 3 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/UserSavedTrendConfig", "UserSavedTrendConfig", "/trending/saved"]
---

:::note

:::


**Page**: `98_Configuration/AdhocTrend/UserSavedTrendConfig`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/UserSavedTrendConfig` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/UserSavedTrendConfig/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; UserSavedTrendConfig |
| Routes | `/trending/saved` (User Saved Trends) |
| Root | `ia.container.flex`, no default size |
| Size | 3 components, 3 bindings, 0 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-07-24T18:40:04Z by the Designer |

## Component Tree

Component types: ia.container.flex x2, ia.display.table x1.

```text
root  ia.container.flex  [2 bindings]
  TableContainer  ia.container.flex
    Table  ia.display.table  [1 binding]
```

## Bindings

3 bindings: expr-struct 2, query 1.

**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

**`root/TableContainer/Table`**

- `props.data`: named query

Named query `AdhocTrend/Select`, return format `auto`

```js
currentUser: {session.props.auth.user.userName}
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

- **`root`** message handler `TrendDeleteConfirm` (scope: page)

```python
trend_id = payload["trendId"]
system.db.runNamedQuery("AdhocTrend/Delete", {"id": trend_id, "isAdmin": shared.Security.allowed(self.session, 'Trends', 'ManageLocked')})
system.perspective.closePopup("alertDialog")
self.getChild("TableContainer").getChild("Table").refreshBinding("props.data")
```

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Security.allowed](../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [98\_Configuration/AdhocTrend/\_Assets/LoadDeleteTrend](./assets/loaddeletetrend.md)

**Named in project scripts**: [Navigation.Nav](../../../../../scripting/reference/modules/navigation-nav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Colors/Container` | 1 | no rule found |
| `Container/Card` | 1 | no rule found |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Named queries: `AdhocTrend/Select`.

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
