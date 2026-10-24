---
title: "AuditLogCell"
sidebar_label: "AuditLogCell"
description: "Perspective view 00_Pages/Boars Head/Operations/_Assets/AuditLogCell (Asset (embedded piece)): 2 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Assets/AuditLogCell", "AuditLogCell"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/Boars Head/Operations/_Assets/AuditLogCell`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Assets/AuditLogCell` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Assets/AuditLogCell/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Assets &gt; AuditLogCell |
| Root | `ia.container.flex`, height 34, width 180 |
| Size | 2 components, 3 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `value` | `""` | input |
| `column` | `""` | input |
| `rowData` | `{}` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1.

```text
root  ia.container.flex
  Text  ia.display.label  [3 bindings]
```

## Bindings

3 bindings: expr 3.

**`root/Text`**

- `props.text`: expression

```js
toStr(coalesce({view.params.value}, ''))
```


- `meta.tooltip.enabled`: expression

```js
try(case({view.params.column}, 'actor', coalesce({view.params.rowData.actor_host}, ''), 'action_text', coalesce({view.params.rowData.action}, ''), 'target_text', coalesce({view.params.rowData.target_tip}, ''), 'change_text', coalesce({view.params.rowData.action_value}, ''), 'source_text', coalesce({view.params.rowData.source_tip}, ''), ''), '') != ''
```


- `meta.tooltip.text`: expression

```js
try(case({view.params.column}, 'actor', coalesce({view.params.rowData.actor_host}, ''), 'action_text', coalesce({view.params.rowData.action}, ''), 'target_text', coalesce({view.params.rowData.target_tip}, ''), 'change_text', coalesce({view.params.rowData.action_value}, ''), 'source_text', coalesce({view.params.rowData.source_tip}, ''), ''), '')
```


## Related Views

**Opened or named by** (1): [00\_Pages/Boars Head/Operations/AuditLog](../auditlog.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `form-check` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
