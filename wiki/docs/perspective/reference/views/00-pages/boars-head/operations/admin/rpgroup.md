---
title: "RPGroup"
sidebar_label: "RPGroup"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/RPGroup (Page piece (not routed)): 9 components, 10 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/RPGroup", "RPGroup"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/RPGroup`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/RPGroup` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/RPGroup/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; RPGroup |
| Root | `ia.container.flex`, height 45, width 900 |
| Size | 9 components, 10 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-24T01:51:34Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `canEdit` | `false` | input |
| `desc` | `""` | input |
| `filtering` | `false` | input |
| `icon` | `""` | input |
| `name` | `""` | input |
| `open` | `false` | input |
| `rows` | `[]` | input |
| `rw` | `100` | input |
| `showSubs` | `false` | input |
| `shown` | `[]` | input |
| `total` | `0` | input |

## Component Tree

Component types: ia.display.label x3, ia.container.flex x2, ia.display.icon x2, ia.display.flex-repeater x2.

```text
root  ia.container.flex
  Header  ia.container.flex  [1 event]
    Chevron  ia.display.icon  [2 bindings]
    Icon  ia.display.icon  [1 binding]
    Name  ia.display.label  [1 binding]
    Count  ia.display.label  [1 binding]
    Desc  ia.display.label  [1 binding]
    Bulk  ia.display.flex-repeater  [2 bindings; view: 00_Pages/Boars Head/Operations/_Admin/RPBulk]
  Rows  ia.display.flex-repeater  [2 bindings; view: 00_Pages/Boars Head/Operations/_Admin/RPRow]
```

## Bindings

10 bindings: expr 6, property 4.

**`root/Header/Chevron`**

- `props.path`: expression

```js
if({view.params.open}, 'material/expand_more', 'material/chevron_right')
```


- `props.style.classes`: expression

```js
if({view.params.filtering}, 'admin-ico-off', 'color-icon')
```


**`root/Header/Icon`**

- `props.path`: property `view.params.icon`

**`root/Header/Name`**

- `props.text`: property `view.params.name`

**`root/Header/Count`**

- `props.text`: expression

```js
if(len({view.params.rows}) = {view.params.total}, toStr({view.params.total}), toStr(len({view.params.rows})) + ' Of ' + toStr({view.params.total}))
```


**`root/Header/Desc`**

- `props.text`: property `view.params.desc`

**`root/Header/Bulk`**

- `position.basis`: expression

```js
toStr(len({view.params.shown}) * {view.params.rw}) + 'px'
```


- `props.instances`: expression

```js
forEach({view.params.shown}, asMap('cat', {view.params.name}, 'role', it()['name'], 'canEdit', {view.params.canEdit}, 'state', if(it()['full'], 'locked', if(len(where({view.params.rows}, coalesce(try(it()['eff'][it(1)['i']], false), false))) = len({view.params.rows}), 'all', if(len(where({view.params.rows}, coalesce(try(it()['eff'][it(1)['i']], false), false))) = 0, 'none', 'some'))), 'text', if(it()['full'], 'All', toStr(len(where({view.params.rows}, coalesce(try(it()['eff'][it(1)['i']], false), false)))) + '/' + toStr(len({view.params.rows}))), 'instancePosition', asMap('basis', toStr({view.params.rw}) + 'px', 'grow', 0, 'shrink', 0)))
```


**`root/Rows`**

- `position.display`: property `view.params.open`

- `props.instances`: expression

```js
if({view.params.showSubs}, flatten(forEach(groupBy({view.params.rows}, it()['sub']), flatten(asList(asList(asMap('kind', 'sub', 'title', it()[0], 'n', len(it()[1]), 'label', '', 'key', '', 'desc', '', 'rw', {view.params.rw}, 'cells', asList(), 'instancePosition', asMap('basis', '30px', 'grow', 0, 'shrink', 0))), forEach(it()[1], asMap('kind', 'row', 'title', '', 'n', 0, 'label', it()['label'], 'key', it()['key'], 'desc', it()['desc'], 'rw', {view.params.rw}, 'cells', forEach({view.params.shown}, asMap('key', it(1)['key'], 'role', it()['name'], 'state', if((it()['full'] && !coalesce(try(it(1)['restricted'], false), false)), 'locked', if(coalesce(try(it(1)['inh'][it()['i']], false), false), 'inherited', if(coalesce(try(it(1)['chg'][it()['i']], false), false), if(coalesce(try(it(1)['eff'][it()['i']], false), false), 'changedOn', 'changedOff'), if({view.params.canEdit}, if(coalesce(try(it(1)['eff'][it()['i']], false), false), 'on', 'off'), if(coalesce(try(it(1)['eff'][it()['i']], false), false), 'roOn', 'roOff'))))), 'tip', if((it()['full'] && !coalesce(try(it(1)['restricted'], false), false)), it()['name'] + ' is a full permission role: always every permission', if(coalesce(try(it(1)['inh'][it()['i']], false), false), 'Inherited from ' + it()['baseName'] + ' (RoleInherits)', if(coalesce(try(it(1)['chg'][it()['i']], false), false), 'Unsaved change', ''))), 'canEdit', {view.params.canEdit}, 'instancePosition', asMap('basis', toStr({view.params.rw}) + 'px', 'grow', 0, 'shrink', 0))), 'instancePosition', asMap('basis', '48px', 'grow', 0, 'shrink', 0))))))), forEach({view.params.rows}, asMap('kind', 'row', 'title', '', 'n', 0, 'label', it()['label'], 'key', it()['key'], 'desc', it()['desc'], 'rw', {view.params.rw}, 'cells', forEach({view.params.shown}, asMap('key', it(1)['key'], 'role', it()['name'], 'state', if((it()['full'] && !coalesce(try(it(1)['restricted'], false), false)), 'locked', if(coalesce(try(it(1)['inh'][it()['i']], false), false), 'inherited', if(coalesce(try(it(1)['chg'][it()['i']], false), false), if(coalesce(try(it(1)['eff'][it()['i']], false), false), 'changedOn', 'changedOff'), if({view.params.canEdit}, if(coalesce(try(it(1)['eff'][it()['i']], false), false), 'on', 'off'), if(coalesce(try(it(1)['eff'][it()['i']], false), false), 'roOn', 'roOff'))))), 'tip', if((it()['full'] && !coalesce(try(it(1)['restricted'], false), false)), it()['name'] + ' is a full permission role: always every permission', if(coalesce(try(it(1)['inh'][it()['i']], false), false), 'Inherited from ' + it()['baseName'] + ' (RoleInherits)', if(coalesce(try(it(1)['chg'][it()['i']], false), false), 'Unsaved change', ''))), 'canEdit', {view.params.canEdit}, 'instancePosition', asMap('basis', toStr({view.params.rw}) + 'px', 'grow', 0, 'shrink', 0))), 'instancePosition', asMap('basis', '48px', 'grow', 0, 'shrink', 0))))
```


## Event Scripts And Handlers

- **`root/Header`** `dom.onClick`, script action, scope `G`

```python
if not self.view.params.filtering:
    system.perspective.sendMessage('rpGroupToggle', payload={'name': self.view.params.name}, scope='page')
```

## Related Views

**Embeds** (2): [00\_Pages/Boars Head/Operations/\_Admin/RPBulk](./rpbulk.md) (flex repeater), [00\_Pages/Boars Head/Operations/\_Admin/RPRow](./rprow.md) (flex repeater)

**Embedded in** (1): [00\_Pages/Boars Head/Operations/RolesPermissions](../rolespermissions.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-count` | 1 | style class |
| `admin-desc` | 1 | style class |
| `admin-group` | 1 | style class |
| `admin-group-name` | 1 | style class |
| `admin-ico-muted` | 1 | style class |
| `admin-ico-on` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
