---
title: "NewRole"
sidebar_label: "NewRole"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/NewRole (Page piece (not routed)): 49 components, 36 bindings, 8 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/NewRole", "NewRole"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/NewRole`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/NewRole` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/NewRole/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; NewRole |
| Root | `ia.container.flex`, height 660, width 760 |
| Size | 49 components, 36 bindings, 8 event handlers, 0 change scripts, 5 message handlers |
| Last saved | 2026-10-24T17:40:25Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `userSource` | `"default"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `copied` | `null` | |
| `copyFrom` | `""` | |
| `err` | `""` | |
| `groupInst` | `[]` | bound (expr) |
| `groups` | `[]` | bound (expr) |
| `model` | `{"defaults": [], "groups": [], "roles": [], "total": 0}` | |
| `name` | `""` | |
| `open` | `{}` | |
| `q` | `""` | bound (expr) |
| `search` | `""` | |
| `sel` | `[]` | |
| `step` | `1` | |

## Component Tree

Component types: ia.display.label x18, ia.container.flex x17, ia.input.button x6, ia.display.icon x4, ia.input.text-field x2, ia.input.dropdown x1, ia.display.flex-repeater x1.

<details>
<summary>Component tree (49 components)</summary>

```text
root  ia.container.flex  [1 event]
  Head  ia.container.flex
    TitleBlock  ia.container.flex
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
    Stepper  ia.container.flex
      Dot1  ia.container.flex  [1 binding]
        Num  ia.display.label  [2 bindings]
        Done  ia.display.icon  [1 binding]
      Cap1  ia.display.label  [1 binding]
      Line  ia.container.flex  [1 binding]
      Dot2  ia.container.flex  [1 binding]
        Num  ia.display.label  [2 bindings]
        Done  ia.display.icon  [1 binding]
      Cap2  ia.display.label  [1 binding]
    Close  ia.display.icon  [1 event]
  Step1  ia.container.flex  [1 binding]
    Name  ia.container.flex
      Label  ia.display.label
      Input  ia.input.text-field  [1 binding]
    NameHint  ia.display.label
    Error  ia.display.label  [2 bindings]
    Copy  ia.container.flex
      Label  ia.display.label
      Input  ia.input.dropdown  [2 bindings]
    CopyHint  ia.display.label
    Note  ia.container.flex
      Icon  ia.display.icon
      Text  ia.display.label
  Step2  ia.container.flex  [1 binding]
    Summary  ia.container.flex
      Name  ia.display.label  [1 binding]
      Chip  ia.display.label  [1 binding]
      Spacer  ia.display.label
      Count  ia.display.label  [1 binding]
    Toolbar  ia.container.flex
      Search  ia.input.text-field  [1 binding]
      ExpandAll  ia.input.button  [1 binding; 1 event]
      CollapseAll  ia.input.button  [1 binding; 1 event]
    Groups  ia.container.flex
      Items  ia.display.flex-repeater  [1 binding; view: 00_Pages/Boars Head/Operations/_Admin/NRGroup]
      Empty  ia.container.flex  [1 binding]
        Text  ia.display.label  [1 binding]
  ActionBar  ia.container.flex
    Back  ia.input.button  [1 binding; 1 event]
    Status  ia.display.label  [1 binding]
    Cancel  ia.input.button  [1 event]
    Next  ia.input.button  [2 bindings; 1 event]
    Create  ia.input.button  [1 binding; 1 event]
```

</details>

## Bindings

36 bindings: expr 32, property 4.

<details>
<summary>All 36 bindings, grouped by component</summary>

**`(view)`**

- `custom.groupInst`: expression

```js
forEach({view.custom.groups}, asMap('name', it()['name'], 'icon', it()['icon'], 'desc', it()['desc'], 'rows', it()['rows'], 'open', it()['open'], 'instancePosition', asMap('basis', toStr(44 + if(it()['open'], len(it()['rows']) * 48, 0)) + 'px', 'grow', 0, 'shrink', 0)))
```


- `custom.groups`: expression

```js
where(forEach(coalesce(try({view.custom.model}['groups'], asList()), asList()), asMap('name', it()['name'], 'icon', it()['icon'], 'desc', it()['desc'], 'rows', forEach(where(it()['rows'], len({view.custom.q}) = 0 || indexOf(lower(it()['label'] + ' ' + it()['key'] + ' ' + it()['desc'] + ' ' + it()['sub']), {view.custom.q}) >= 0), asMap('key', it()['key'], 'label', it()['label'], 'desc', it()['desc'], 'sub', it()['sub'], 'on', len(where({view.custom.sel}, it() = it(1)['key'])) > 0)), 'open', len({view.custom.q}) > 0 || coalesce(try({view.custom.open}[it()['name']], false), false))), len(it()['rows']) > 0)
```


- `custom.q`: expression

```js
lower(trim(coalesce({view.custom.search}, '')))
```


**`root/Head/TitleBlock/Sub`**

- `props.text`: expression

```js
if({view.custom.step} = 1, 'Name the role and pick where its permissions start from.', 'Choose what the role may do. Nothing is created until you press Create Role.')
```


**`root/Head/Stepper/Dot1`**

- `props.style.classes`: expression

```js
if({view.custom.step} >= 1, 'admin-step-dot admin-step-dot-on', 'admin-step-dot')
```


**`root/Head/Stepper/Dot1/Num`**

- `position.display`: expression

```js
!({view.custom.step} > 1)
```


- `props.style.classes`: expression

```js
if({view.custom.step} >= 1, 'admin-step-num admin-step-num-on', 'admin-step-num')
```


**`root/Head/Stepper/Dot1/Done`**

- `position.display`: expression

```js
{view.custom.step} > 1
```


**`root/Head/Stepper/Cap1`**

- `props.style.classes`: expression

```js
if({view.custom.step} = 1, 'admin-step-label admin-step-label-on', 'admin-step-label')
```


**`root/Head/Stepper/Line`**

- `props.style.classes`: expression

```js
if({view.custom.step} > 1, 'admin-step-line admin-step-line-on', 'admin-step-line')
```


**`root/Head/Stepper/Dot2`**

- `props.style.classes`: expression

```js
if({view.custom.step} >= 2, 'admin-step-dot admin-step-dot-on', 'admin-step-dot')
```


**`root/Head/Stepper/Dot2/Num`**

- `position.display`: expression

```js
!({view.custom.step} > 2)
```


- `props.style.classes`: expression

```js
if({view.custom.step} >= 2, 'admin-step-num admin-step-num-on', 'admin-step-num')
```


**`root/Head/Stepper/Dot2/Done`**

- `position.display`: expression

```js
{view.custom.step} > 2
```


**`root/Head/Stepper/Cap2`**

- `props.style.classes`: expression

```js
if({view.custom.step} = 2, 'admin-step-label admin-step-label-on', 'admin-step-label')
```


**`root/Step1`**

- `position.display`: expression

```js
{view.custom.step} = 1
```


**`root/Step1/Name/Input`**

- `props.text`: property `view.custom.name` (bidirectional)

**`root/Step1/Error`**

- `position.display`: expression

```js
len(coalesce({view.custom.err}, '')) > 0
```


- `props.text`: property `view.custom.err`

**`root/Step1/Copy/Input`**

- `props.options`: expression

```js
flatten(asList(asList(asMap('value', '', 'label', 'None (Start From The Defaults)')), forEach(coalesce(try({view.custom.model}['roles'], asList()), asList()), asMap('value', it(), 'label', it()))))
```


- `props.value`: property `view.custom.copyFrom` (bidirectional)

**`root/Step2`**

- `position.display`: expression

```js
{view.custom.step} = 2
```


**`root/Step2/Summary/Name`**

- `props.text`: expression

```js
trim(coalesce({view.custom.name}, ''))
```


**`root/Step2/Summary/Chip`**

- `props.text`: expression

```js
if(len(coalesce({view.custom.copied}, '')) > 0, 'Copied From ' + {view.custom.copied}, 'Starting From The Defaults')
```


**`root/Step2/Summary/Count`**

- `props.text`: expression

```js
toStr(len(coalesce({view.custom.sel}, asList()))) + ' Of ' + toStr(coalesce(try({view.custom.model}['total'], 0), 0)) + ' Selected'
```


**`root/Step2/Toolbar/Search`**

- `props.text`: property `view.custom.search` (bidirectional)

**`root/Step2/Toolbar/ExpandAll`**

- `props.enabled`: expression

```js
len({view.custom.q}) = 0
```


**`root/Step2/Toolbar/CollapseAll`**

- `props.enabled`: expression

```js
len({view.custom.q}) = 0
```


**`root/Step2/Groups/Items`**

- `props.instances`: expression

```js
{view.custom.groupInst}
```


**`root/Step2/Groups/Empty`**

- `position.display`: expression

```js
len({view.custom.groups}) = 0
```


**`root/Step2/Groups/Empty/Text`**

- `props.text`: expression

```js
'No Permissions Match "' + trim(coalesce({view.custom.search}, '')) + '"'
```


**`root/ActionBar/Back`**

- `position.display`: expression

```js
{view.custom.step} = 2
```


**`root/ActionBar/Status`**

- `props.text`: expression

```js
if({view.custom.step} = 1, 'Step 1 Of 2', 'Recorded In The Audit Log As Role Created')
```


**`root/ActionBar/Next`**

- `position.display`: expression

```js
{view.custom.step} = 1
```


- `props.enabled`: expression

```js
len(trim(coalesce({view.custom.name}, ''))) > 0
```


**`root/ActionBar/Create`**

- `position.display`: expression

```js
{view.custom.step} = 2
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 13 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
if not shared.PermissionMatrix.mayCreate(self.session):
    system.perspective.closePopup(shared.PermissionMatrix.WIZARD_ID)
    return
m = shared.PermissionMatrix.wizardModel(self.view.params.userSource or 'default', self.session.props.auth.user.roles)
self.view.custom.model = m
self.view.custom.sel = list(m['defaults'])
self.view.custom.open = dict((str(g['name']), i == 0) for i, g in enumerate(m['groups']))
```

- **`root/Head/Close`** `dom.onClick`, script action, scope `G`

```python
system.perspective.closePopup(shared.PermissionMatrix.WIZARD_ID)
```

- **`root/Step2/Toolbar/ExpandAll`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('nrExpand', payload={'open': True}, scope='page')
```

- **`root/Step2/Toolbar/CollapseAll`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('nrExpand', payload={'open': False}, scope='page')
```

- **`root/ActionBar/Back`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.step = 1
```

- **`root/ActionBar/Cancel`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.closePopup(shared.PermissionMatrix.WIZARD_ID)
```

- **`root/ActionBar/Next`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
err = shared.PermissionMatrix.checkRoleName(self.view.params.userSource or 'default', v.name)
v.err = err
if err:
    return
src = str(v.copyFrom or '')
if v.copied is None or str(v.copied) != src:
    v.sel = shared.PermissionMatrix.roleGrants(src, self.session.props.auth.user.roles) if src else list(v.model['defaults'])
    v.copied = src
v.step = 2
```

- **`root/ActionBar/Create`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
name = str(v.name or '').strip()
n = len(v.sel or [])
src = str(v.copied or '')
shared.Alerts.showAlert(state='info', title='Create Role %s?' % name,
    message='%d Of %d Permissions%s.\n\nThe role is added to user source %s with its own Roles & Permissions column and recorded in the Audit Log. It has no users until you assign it.' % (n, v.model['total'], (' (Copied From %s)' % src) if src else '', self.view.params.userSource or 'default'),
    showCloseBtn=False, btnTextPrimary='Create Role', btnTextSecondary='Cancel', btnActionPrimary='nrCreateConfirmed', btnActionSecondary='', payload={'name': name, 'grants': [str(k) for k in (v.sel or [])], 'copyFrom': src}, overlayDismiss=False)
```

- **`root`** message handler `nrToggle` (scope: page)

```python
sel = [str(k) for k in (self.view.custom.sel or [])]
k = str(payload['key'])
if k in sel:
    sel.remove(k)
else:
    sel.append(k)
self.view.custom.sel = sel
```

- **`root`** message handler `nrBulk` (scope: page)

```python
sel = [str(k) for k in (self.view.custom.sel or [])]
keys = [str(k) for k in (payload['keys'] or [])]
if payload['grant']:
    sel += [k for k in keys if k not in sel]
else:
    sel = [k for k in sel if k not in keys]
self.view.custom.sel = sel
```

- **`root`** message handler `nrGroupToggle` (scope: page)

```python
o = dict(self.view.custom.open or {})
n = str(payload['name'])
o[n] = not bool(o.get(n))
self.view.custom.open = o
```

- **`root`** message handler `nrExpand` (scope: page)

```python
self.view.custom.open = dict((str(g['name']), bool(payload['open'])) for g in (self.view.custom.model['groups'] or []))
```

- **`root`** message handler `nrCreateConfirmed` (scope: page)

```python
res = shared.PermissionMatrix.createRole(self.session, self.view.params.userSource or 'default', payload['name'], [str(k) for k in (payload['grants'] or [])], payload.get('copyFrom') or '')
if not res['ok']:
    shared.Alerts.showAlert(state='error', title='Cannot Create Role', message=res['message'], btnTextPrimary='OK')
    return
system.perspective.closePopup(shared.PermissionMatrix.WIZARD_ID)
system.perspective.sendMessage('nrCreated', payload={'name': str(payload['name']).strip()}, scope='page')
shared.Alerts.showAlert(state='success', title='Role Created', message=res['message'] + ' Assign it to users on User Management > Users.', btnTextPrimary='OK')
```

</details>

Project script calls: [shared.Alerts.showAlert](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.PermissionMatrix.WIZARD\_ID](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.checkRoleName](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.createRole](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.mayCreate](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.roleGrants](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.wizardModel](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md).

## Related Views

**Embeds** (1): [00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./nrgroup.md) (flex repeater)

**Named in project scripts**: [shared.PermissionMatrix](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md)

## Style Classes

<details>
<summary>21 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `admin-cell-text` | 1 | style class |
| `admin-chip` | 1 | style class |
| `admin-desc` | 1 | style class |
| `admin-ico-muted` | 1 | style class |
| `admin-ico-on` | 1 | style class |
| `admin-item-title` | 1 | style class |
| `admin-note` | 1 | style class |
| `admin-step-label` | 2 | style class |
| `admin-step-num-on` | 2 | style class |
| `form-btn` | 4 | style class |
| `form-btn-primary` | 2 | style class |
| `form-card` | 1 | style class |
| `form-check` | 1 | style class |
| `form-hint` | 2 | style class |
| `form-input` | 3 | style class |
| `form-label` | 2 | style class |
| `form-section-head` | 1 | style class |
| `form-status` | 2 | style class |
| `form-status-error` | 1 | style class |
| `form-subtitle` | 2 | style class |
| `form-title` | 1 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
