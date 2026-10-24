---
title: "CommentEntry"
sidebar_label: "CommentEntry"
description: "Perspective view 00_Pages/Boars Head/Operations/OutOfService/_Assets/CommentEntry (Asset (embedded piece)): 6 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/OutOfService/_Assets/CommentEntry", "CommentEntry"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/Boars Head/Operations/OutOfService/_Assets/CommentEntry`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/OutOfService/_Assets/CommentEntry` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/OutOfService/_Assets/CommentEntry/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; OutOfService &gt; \_Assets &gt; CommentEntry |
| Root | `ia.container.flex`, height 70, width 440 |
| Size | 6 components, 6 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `id` | `0` | input |
| `display_name` | `""` | input |
| `username` | `""` | input |
| `created_text` | `""` | input |
| `status` | `""` | input |
| `comment` | `""` | input |

## Component Tree

Component types: ia.display.label x4, ia.container.flex x2.

```text
root  ia.container.flex
  Head  ia.container.flex
    Name  ia.display.label  [1 binding]
    Status  ia.display.label  [3 bindings]
    Time  ia.display.label  [1 binding]
  Comment  ia.display.label  [1 binding]
```

## Bindings

6 bindings: expr 3, property 3.

**`root/Head/Name`**

- `props.text`: expression

```js
coalesce({view.params.display_name}, '') + if(coalesce({view.params.username}, '') != '', ' (' + {view.params.username} + ')', '')
```


**`root/Head/Status`**

- `props.text`: property `view.params.status`

- `props.style.classes`: expression

```js
'oos-chip fs-11 fw-700 ' + case(coalesce({view.params.status}, ''), 'Returned', 'oos-chip-returned', 'In Progress', 'oos-chip-progress', 'Ready To Return', 'oos-chip-ready', 'Awaiting Parts', 'oos-chip-waiting', 'On Hold', 'oos-chip-waiting', '')
```


- `position.display`: expression

```js
coalesce({view.params.status}, '') != ''
```


**`root/Head/Time`**

- `props.text`: property `view.params.created_text`

**`root/Comment`**

- `props.text`: property `view.params.comment`

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](../outofservicelog.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 2 | style class |
| `fs-11` | 2 | style class |
| `fw-700` | 2 | style class |
| `oos-chip` | 1 | stylesheet |
| `oos-comment` | 1 | stylesheet |
| `oos-memo` | 1 | stylesheet |
| `text-muted` | 1 | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
