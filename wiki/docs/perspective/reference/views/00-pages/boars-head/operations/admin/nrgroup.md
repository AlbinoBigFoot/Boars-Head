---
title: "NRGroup"
sidebar_label: "NRGroup"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/NRGroup (Page piece (not routed)): 10 components, 11 bindings, 2 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/NRGroup", "NRGroup"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/NRGroup`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/NRGroup` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/NRGroup/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; NRGroup |
| Root | `ia.container.flex`, height 44, width 700 |
| Size | 10 components, 11 bindings, 2 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-24T17:40:25Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `desc` | `""` | input |
| `icon` | `""` | input |
| `name` | `""` | input |
| `open` | `false` | input |
| `rows` | `[]` | input |

## Component Tree

Component types: ia.container.flex x3, ia.display.icon x3, ia.display.label x3, ia.display.flex-repeater x1.

```text
root  ia.container.flex
  Header  ia.container.flex
    HeadClick  ia.container.flex  [1 event]
      Chevron  ia.display.icon  [1 binding]
      Icon  ia.display.icon  [1 binding]
      Name  ia.display.label  [1 binding]
      Count  ia.display.label  [1 binding]
      Desc  ia.display.label  [1 binding]
    Bulk  ia.display.icon  [4 bindings; 1 event]
  Rows  ia.display.flex-repeater  [2 bindings; view: 00_Pages/Boars Head/Operations/_Admin/NRRow]
```

## Bindings

11 bindings: expr 7, property 4.

**`root/Header/HeadClick/Chevron`**

- `props.path`: expression

```js
if({view.params.open}, 'material/expand_more', 'material/chevron_right')
```


**`root/Header/HeadClick/Icon`**

- `props.path`: property `view.params.icon`

**`root/Header/HeadClick/Name`**

- `props.text`: property `view.params.name`

**`root/Header/HeadClick/Count`**

- `props.text`: expression

```js
toStr(len(where({view.params.rows}, it()['on']))) + '/' + toStr(len({view.params.rows}))
```


**`root/Header/HeadClick/Desc`**

- `props.text`: property `view.params.desc`

**`root/Header/Bulk`**

- `meta.tooltip.enabled`: expression

```js
len(coalesce(if(if(len(where({view.params.rows}, it()['on'])) = 0, 'none', if(len(where({view.params.rows}, it()['on'])) = len({view.params.rows}), 'all', 'some')) = 'all', 'Clear All In ' + {view.params.name}, 'Select All In ' + {view.params.name}), '')) > 0
```


- `meta.tooltip.text`: expression

```js
if(if(len(where({view.params.rows}, it()['on'])) = 0, 'none', if(len(where({view.params.rows}, it()['on'])) = len({view.params.rows}), 'all', 'some')) = 'all', 'Clear All In ' + {view.params.name}, 'Select All In ' + {view.params.name})
```


- `props.path`: expression

```js
case(if(len(where({view.params.rows}, it()['on'])) = 0, 'none', if(len(where({view.params.rows}, it()['on'])) = len({view.params.rows}), 'all', 'some')), 'all', 'material/check_box', 'some', 'material/indeterminate_check_box', 'material/check_box_outline_blank')
```


- `props.style.classes`: expression

```js
if(if(len(where({view.params.rows}, it()['on'])) = 0, 'none', if(len(where({view.params.rows}, it()['on'])) = len({view.params.rows}), 'all', 'some')) = 'none', 'admin-ico-off', 'admin-ico-on')
```


**`root/Rows`**

- `position.display`: property `view.params.open`

- `props.instances`: expression

```js
forEach({view.params.rows}, asMap('key', it()['key'], 'label', it()['label'], 'desc', it()['desc'], 'sub', it()['sub'], 'on', it()['on'], 'instancePosition', asMap('basis', '48px', 'grow', 0, 'shrink', 0)))
```


## Event Scripts And Handlers

- **`root/Header/HeadClick`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage('nrGroupToggle', payload={'name': self.view.params.name}, scope='page')
```

- **`root/Header/Bulk`** `dom.onClick`, script action, scope `G`

```python
p = self.view.params
grant = not all(bool(r['on']) for r in (p.rows or []))
system.perspective.sendMessage('nrBulk', payload={'keys': [str(r['key']) for r in (p.rows or [])], 'grant': grant}, scope='page')
```

## Related Views

**Embeds** (1): [00\_Pages/Boars Head/Operations/\_Admin/NRRow](./nrrow.md) (flex repeater)

**Embedded in** (1): [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./newrole.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-count` | 1 | style class |
| `admin-desc` | 1 | style class |
| `admin-group` | 1 | style class |
| `admin-group-name` | 1 | style class |
| `admin-ico-muted` | 1 | style class |
| `admin-ico-on` | 2 | style class |
| `admin-ico-off` | bound | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
