---
title: "RolesPermissions"
sidebar_label: "RolesPermissions"
description: "Perspective view 00_Pages/Boars Head/Operations/RolesPermissions (Page): 60 components, 64 bindings, 11 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/RolesPermissions", "RolesPermissions", "/operations/roles-permissions"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/Operations/RolesPermissions`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/RolesPermissions` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/RolesPermissions/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; RolesPermissions |
| Routes | `/operations/roles-permissions` (Roles & Permissions) |
| Root | `ia.container.flex`, height 900, width 1400 |
| Size | 60 components, 64 bindings, 11 event handlers, 0 change scripts, 12 message handlers |
| Last saved | 2026-10-24T17:40:25Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"_Config/RolesPermissions"` | input |

## Custom properties

<details>
<summary>33 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `canEdit` | `false` | bound (expr) |
| `catalog` | `null` | bound (tag) |
| `category` | `""` | |
| `cats` | `null` | bound (tag) |
| `diffOnly` | `false` | |
| `editCount` | `0` | bound (expr) |
| `editSummary` | `""` | |
| `edits` | `{}` | |
| `filtering` | `false` | bound (expr) |
| `focus` | `null` | |
| `fullCsv` | `""` | bound (tag) |
| `groupInst` | `[]` | bound (expr) |
| `groups` | `[]` | bound (expr) |
| `inherits` | `""` | bound (tag) |
| `lastSaved` | `""` | |
| `matrix` | `null` | bound (tag) |
| `open` | `{"General": true}` | |
| `pairs` | `[]` | bound (expr) |
| `q` | `""` | bound (expr) |
| `roleInfo` | `[]` | |
| `roleSel` | `""` | |
| `roles` | `[]` | bound (expr) |
| `roles0` | `[]` | bound (expr) |
| `rowRules` | `{"hidden": [], "restricted": []}` | bound (expr-struct) |
| `rows` | `[]` | bound (expr) |
| `rows0` | `[]` | bound (expr) |
| `rows1` | `[]` | bound (expr) |
| `rw` | `100` | bound (expr) |
| `search` | `""` | |
| `selRole` | `null` | bound (expr) |
| `shown` | `[]` | bound (expr) |
| `tab` | `"perm"` | |
| `vis` | `[]` | bound (expr) |

</details>

## Component Tree

Component types: ia.container.flex x23, ia.display.label x18, ia.input.button x8, ia.display.icon x3, ia.display.flex-repeater x3, ia.input.dropdown x2, ia.input.text-field x1, ia.input.checkbox x1, ia.display.markdown x1.

<details>
<summary>Component tree (60 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  AccessDenied  ia.container.flex  [1 binding]
    Icon  ia.display.icon
    Title  ia.display.label
    Text  ia.display.label
  Content  ia.container.flex  [1 binding]
    HeaderCard  ia.container.flex
      TitleRow  ia.container.flex
        TitleBlock  ia.container.flex
          Title  ia.display.label
          Subtitle  ia.display.label
        Tabs  ia.container.flex
          Tab_perm  ia.display.label  [2 bindings; 1 event]
          Tab_roles  ia.display.label  [2 bindings; 1 event]
      Toolbar  ia.container.flex  [1 binding]
        Search  ia.input.text-field  [1 binding]
        Category  ia.input.dropdown  [2 bindings]
        Roles  ia.input.dropdown  [2 bindings]
        DiffOnly  ia.input.checkbox  [1 binding]
        ExpandAll  ia.input.button  [1 binding; 1 event]
        CollapseAll  ia.input.button  [1 binding; 1 event]
    MatrixCard  ia.container.flex  [1 binding]
      MatrixHead  ia.container.flex
        PermHead  ia.container.flex
          Label  ia.display.label
          Count  ia.display.label  [1 binding]
        RoleHeads  ia.display.flex-repeater  [2 bindings; view: 00_Pages/Boars Head/Operations/_Admin/RPRoleHead]
      MatrixBody  ia.container.flex
        Groups  ia.display.flex-repeater  [1 binding; view: 00_Pages/Boars Head/Operations/_Admin/RPGroup]
        Empty  ia.container.flex  [1 binding]
          Icon  ia.display.icon
          Title  ia.display.label  [1 binding]
          Hint  ia.display.label
          Clear  ia.input.button  [1 event]
    ChangeBar  ia.container.flex  [2 bindings]
      Icon  ia.display.icon  [2 bindings]
      Status  ia.display.label  [2 bindings]
      Discard  ia.input.button  [1 binding; 1 event]
      Save  ia.input.button  [1 binding; 1 event]
    RolesBody  ia.container.flex  [1 binding]
      RoleList  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Source  ia.display.label
          AddRole  ia.input.button  [3 bindings; 1 event]
        Items  ia.display.flex-repeater  [1 binding; view: 00_Pages/Boars Head/Operations/_Admin/RoleItem]
        Note  ia.container.flex
          Text  ia.display.label
          OpenUM  ia.input.button  [1 event]
      RoleDetail  ia.container.flex
        Head  ia.container.flex
          TitleBlock  ia.container.flex
            Title  ia.display.label  [1 binding]
            Sub  ia.display.label  [1 binding]
          EditInMatrix  ia.input.button  [1 binding; 1 event]
        Users  ia.container.flex
          Label  ia.display.label
          List  ia.display.label  [1 binding]
        Summary  ia.container.flex
          Markdown  ia.display.markdown  [1 binding]
```

</details>

## Bindings

64 bindings: expr 52, tag 5, property 4, expr-struct 3.

<details>
<summary>All 64 bindings, grouped by component</summary>

**`(view)`**

- `custom.canEdit`: expression

```js
coalesce({session.custom.Permissions.RolesPermissions.Edit}, false)
```


- `custom.catalog`: tag

Mode `direct`, tag path `[default]_Config/Security/PermissionCatalog`, fallback delay 2.5 s


- `custom.cats`: tag

Mode `direct`, tag path `[default]_Config/Security/PermissionCategories`, fallback delay 2.5 s


- `custom.editCount`: expression

```js
len(forEach(coalesce({view.custom.edits}, asMap()), 1))
```


- `custom.filtering`: expression

```js
len({view.custom.q}) > 0 || len(coalesce({view.custom.category}, '')) > 0 || coalesce({view.custom.diffOnly}, false)
```


- `custom.fullCsv`: tag

Mode `direct`, tag path `[default]_Config/Security/FullPermissionRoles`, fallback delay 2.5 s


- `custom.groupInst`: expression

```js
forEach({view.custom.groups}, asMap('name', it()['name'], 'icon', it()['icon'], 'desc', it()['desc'], 'rows', it()['rows'], 'total', it()['total'], 'open', it()['open'], 'showSubs', !{view.custom.filtering} && it()['subs'] > 1, 'shown', {view.custom.shown}, 'rw', {view.custom.rw}, 'canEdit', {view.custom.canEdit}, 'filtering', {view.custom.filtering}, 'instancePosition', asMap('basis', toStr(45 + if(it()['open'], len(it()['rows']) * 48 + if(!{view.custom.filtering} && it()['subs'] > 1, it()['subs'] * 30, 0), 0)) + 'px', 'grow', 0, 'shrink', 0)))
```


- `custom.groups`: expression

```js
where(forEach(coalesce({view.custom.cats}, asList()), asMap('name', toStr(it()['Name']), 'icon', toStr(it()['Icon']), 'desc', toStr(it()['Description']), 'rows', where({view.custom.vis}, it()['cat'] = toStr(it(1)['Name'])), 'total', len(where({view.custom.rows}, it()['cat'] = toStr(it(1)['Name']))), 'subs', len(groupBy(where({view.custom.vis}, it()['cat'] = toStr(it(1)['Name'])), it()['sub'])), 'open', {view.custom.filtering} || coalesce({view.custom.open}[toStr(it()['Name'])], false))), len(it()['rows']) > 0)
```


- `custom.inherits`: tag

Mode `direct`, tag path `[default]_Config/Security/RoleInherits`, fallback delay 2.5 s


- `custom.matrix`: tag

Mode `direct`, tag path `[default]_Config/RolesPermissions`, fallback delay 2.5 s


- `custom.pairs`: expression

```js
where(forEach(split(coalesce({view.custom.inherits}, ''), ','), try(asMap('heir', lower(trim(substring(trim(it()[0]), 0, indexOf(trim(it()[0]), ':')))), 'base', trim(substring(trim(it()[0]), indexOf(trim(it()[0]), ':') + 1))), null)), !isNull(it()) && len(it()['heir']) > 0)
```


- `custom.q`: expression

```js
lower(trim(coalesce({view.custom.search}, '')))
```


- `custom.roles`: expression

```js
forEach({view.custom.roles0}, asMap('name', it()['name'], 'users', it()['users'], 'restricted', it()['restricted'], 'full', it()['full'], 'base', it()['base'], 'i', idx(), 'baseIdx', coalesce(try(where(forEach({view.custom.roles0}, asMap('i', idx(), 'n', lower(it()['name']))), len(it(1)['base']) > 0 && it()['n'] = lower(it(1)['base']))[0]['i'], -1), -1), 'baseName', coalesce(try(where({view.custom.roles0}, len(it(1)['base']) > 0 && lower(it()['name']) = lower(it(1)['base']))[0]['name'], ''), '')))
```


- `custom.roles0`: expression

```js
forEach(coalesce({view.custom.roleInfo}, asList()), asMap('name', it()['name'], 'users', it()['users'], 'restricted', it()['restricted'], 'full', indexOf(',' + lower(replace(coalesce({view.custom.fullCsv}, ''), ' ', '')) + ',', ',' + lower(replace(it()['name'], ' ', '')) + ',') >= 0, 'base', coalesce(try(where({view.custom.pairs}, it()['heir'] = lower(it(1)['name']))[0]['base'], ''), '')))
```


- `custom.rowRules`: structured expression (expr-struct), then script transform

```js
roles: {session.props.auth.user.roles}
rows: tag('[default]_Config/Security/RestrictedRows')
```

waitOnAll: `False`

Transform 1, script:

```python
return shared.Security.rowRules(value.roles, value.rows)
```


- `custom.rows`: expression

```js
forEach({view.custom.rows1}, asMap('key', it()['key'], 'dev', it()['dev'], 'act', it()['act'], 'desc', it()['desc'], 'label', it()['label'], 'cat', it()['cat'], 'sub', it()['sub'], 'raw', it()['raw'], 'restricted', it()['restricted'], 'eff', forEach({view.custom.roles}, (it()['full'] && !coalesce(try(it(1)['restricted'], false), false)) || coalesce({view.custom.edits}[it(1)['key'] + '|' + it()['name']], coalesce(try(it(1)['raw'][idx()], false), false)) || (it()['baseIdx'] >= 0 && coalesce({view.custom.edits}[it(1)['key'] + '|' + it()['baseName']], coalesce(try(it(1)['raw'][max(it()['baseIdx'], 0)], false), false)))), 'inh', forEach({view.custom.roles}, !(it()['full'] && !coalesce(try(it(1)['restricted'], false), false)) && (it()['baseIdx'] >= 0 && coalesce({view.custom.edits}[it(1)['key'] + '|' + it()['baseName']], coalesce(try(it(1)['raw'][max(it()['baseIdx'], 0)], false), false)))), 'chg', forEach({view.custom.roles}, !isNull({view.custom.edits}[it(1)['key'] + '|' + it()['name']])), 'saved', forEach({view.custom.roles}, (it()['full'] && !coalesce(try(it(1)['restricted'], false), false)) || coalesce(try(it(1)['raw'][idx()], false), false) || (it()['baseIdx'] >= 0 && coalesce(try(it(1)['raw'][max(it()['baseIdx'], 0)], false), false))), 'match', (len({view.custom.q}) = 0 || indexOf(lower(it()['label'] + ' ' + it()['key'] + ' ' + it()['desc'] + ' ' + it()['sub']), {view.custom.q}) >= 0) && (len(coalesce({view.custom.category}, '')) = 0 || it()['cat'] = {view.custom.category})))
```


- `custom.rows0`: expression

```js
forEach(where(groupBy(coalesce({view.custom.matrix}, asList()), toStr(it()['Devices']) + '/' + toStr(it()['Actions'])), len(where(coalesce(try({view.custom.rowRules}['hidden'], asList()), asList()), it() = it(1)[0])) = 0), asMap('key', it()[0], 'dev', toStr(it()[1][0, 'Devices']), 'act', toStr(it()[1][0, 'Actions']), 'desc', coalesce(toStr(it()[1][0, 'Description']), '') + if(len(it()[1]) > 1, ' / ' + coalesce(toStr(it()[1][1, 'Description']), ''), ''), 'catCol', coalesce(try(toStr(it()[1][0, 'Category']), ''), ''), 'n', idx(), 'raw', forEach({view.custom.roles}, len(where(it(1)[1], coalesce(try(toBoolean(it()[it(1)['name']]), false), false))) > 0)))
```


- `custom.rows1`: expression

```js
orderBy(forEach({view.custom.rows0}, asMap('key', it()['key'], 'dev', it()['dev'], 'act', it()['act'], 'desc', it()['desc'], 'n', it()['n'], 'raw', it()['raw'], 'label', if(len(lookup({view.custom.catalog}, it()['key'], '', 'Key', 'Label')) > 0, lookup({view.custom.catalog}, it()['key'], '', 'Key', 'Label'), if(len(trim(it()['desc'])) > 0, it()['desc'], it()['dev'] + ' ' + it()['act'])), 'cat', if(len(lookup({view.custom.cats}, lookup({view.custom.catalog}, it()['key'], '', 'Key', 'Category'), '', 'Name', 'Name')) > 0, lookup({view.custom.catalog}, it()['key'], '', 'Key', 'Category'), if(len(it()['catCol']) > 0 && len(lookup({view.custom.cats}, it()['catCol'], '', 'Name', 'Name')) > 0, it()['catCol'], if(len(it()['catCol']) > 0 && len(lookup({view.custom.cats}, lookup({view.custom.catalog}, it()['catCol'], '', 'Key', 'Category'), '', 'Name', 'Name')) > 0, lookup({view.custom.catalog}, it()['catCol'], '', 'Key', 'Category'), if(len(lookup({view.custom.cats}, lookup({view.custom.catalog}, it()['dev'], '', 'Key', 'Category'), '', 'Name', 'Name')) > 0, lookup({view.custom.catalog}, it()['dev'], '', 'Key', 'Category'), 'Other')))), 'sub', if(len(lookup({view.custom.catalog}, it()['dev'], '', 'Key', 'Label')) > 0, lookup({view.custom.catalog}, it()['dev'], '', 'Key', 'Label'), it()['dev']), 'devOrder', lookup({view.custom.catalog}, it()['dev'], 999, 'Key', 'Order'), 'restricted', len(where(coalesce(try({view.custom.rowRules}['restricted'], asList()), asList()), it() = it(1)['key'])) > 0)), lookup({view.custom.cats}, it()['cat'], 99, 'Name', 'Order'), it()['devOrder'], it()['n'])
```


- `custom.rw`: expression

```js
if(len({view.custom.shown}) <= 2, 160, if(len({view.custom.shown}) <= 4, 120, 100))
```


- `custom.selRole`: expression

```js
coalesce(try(where(coalesce({view.custom.roleInfo}, asList()), it()['name'] = {view.custom.roleSel})[0], null), try({view.custom.roleInfo}[0], null))
```


- `custom.shown`: expression

```js
where({view.custom.roles}, len(coalesce({view.custom.focus}, asList())) = 0 || len(where(coalesce({view.custom.focus}, asList()), it() = it(1)['name'])) > 0)
```


- `custom.vis`: expression

```js
where({view.custom.rows}, it()['match'] && (!{view.custom.diffOnly} || (len(where(where({view.custom.shown}, !it()['full']), coalesce(try(it(1)['eff'][it()['i']], false), false))) > 0 && len(where(where({view.custom.shown}, !it()['full']), !coalesce(try(it(1)['eff'][it()['i']], false), false))) > 0)))
```


**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

**`root/AccessDenied`**

- `position.display`: expression

```js
!(coalesce({session.custom.Administrator}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false) || coalesce({session.custom.Permissions.RolesPermissions.Edit}, false))
```


**`root/Content`**

- `position.display`: expression

```js
(coalesce({session.custom.Administrator}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false) || coalesce({session.custom.Permissions.RolesPermissions.Edit}, false))
```


**`root/Content/HeaderCard/TitleRow/Tabs/Tab_perm`**

- `props.style.classes`: expression

```js
if({view.custom.tab} = 'perm', 'admin-tab admin-tab-active', 'admin-tab')
```


- `props.text`: expression

```js
'Permissions  ' + toStr(len({view.custom.rows}))
```


**`root/Content/HeaderCard/TitleRow/Tabs/Tab_roles`**

- `props.style.classes`: expression

```js
if({view.custom.tab} = 'roles', 'admin-tab admin-tab-active', 'admin-tab')
```


- `props.text`: expression

```js
'Roles  ' + toStr(len(coalesce({view.custom.roleInfo}, asList())))
```


**`root/Content/HeaderCard/Toolbar`**

- `position.display`: expression

```js
{view.custom.tab} = 'perm'
```


**`root/Content/HeaderCard/Toolbar/Search`**

- `props.text`: property `view.custom.search` (bidirectional)

**`root/Content/HeaderCard/Toolbar/Category`**

- `props.options`: expression

```js
forEach(where(coalesce({view.custom.cats}, asList()), len(where({view.custom.rows}, it()['cat'] = toStr(it(1)['Name']))) > 0), asMap('value', toStr(it()['Name']), 'label', toStr(it()['Name'])))
```


- `props.value`: property `view.custom.category` (bidirectional)

**`root/Content/HeaderCard/Toolbar/Roles`**

- `props.options`: expression

```js
forEach({view.custom.roles}, asMap('value', it()['name'], 'label', it()['name']))
```


- `props.value`: property `view.custom.focus` (bidirectional)

**`root/Content/HeaderCard/Toolbar/DiffOnly`**

- `props.selected`: property `view.custom.diffOnly` (bidirectional)

**`root/Content/HeaderCard/Toolbar/ExpandAll`**

- `props.enabled`: expression

```js
!{view.custom.filtering}
```


**`root/Content/HeaderCard/Toolbar/CollapseAll`**

- `props.enabled`: expression

```js
!{view.custom.filtering}
```


**`root/Content/MatrixCard`**

- `position.display`: expression

```js
{view.custom.tab} = 'perm'
```


**`root/Content/MatrixCard/MatrixHead/PermHead/Count`**

- `props.text`: expression

```js
toStr(len({view.custom.vis})) + ' Of ' + toStr(len({view.custom.rows})) + ' Shown' + if(len(coalesce({view.custom.focus}, asList())) > 0, ' · Comparing ' + toStr(len({view.custom.shown})) + ' Roles', '') + if(coalesce({view.custom.diffOnly}, false), ' · Only Differences', '')
```


**`root/Content/MatrixCard/MatrixHead/RoleHeads`**

- `position.basis`: expression

```js
toStr(len({view.custom.shown}) * {view.custom.rw}) + 'px'
```


- `props.instances`: expression

```js
forEach({view.custom.shown}, asMap('name', it()['name'], 'users', it()['users'], 'full', it()['full'], 'base', it()['baseName'], 'instancePosition', asMap('basis', toStr({view.custom.rw}) + 'px', 'grow', 0, 'shrink', 0)))
```


**`root/Content/MatrixCard/MatrixBody/Groups`**

- `props.instances`: expression

```js
{view.custom.groupInst}
```


**`root/Content/MatrixCard/MatrixBody/Empty`**

- `position.display`: expression

```js
len({view.custom.vis}) = 0
```


**`root/Content/MatrixCard/MatrixBody/Empty/Title`**

- `props.text`: expression

```js
if(len({view.custom.q}) > 0, 'No Permissions Match "' + trim({view.custom.search}) + '"', 'No Permissions Match These Filters')
```


**`root/Content/ChangeBar`**

- `position.display`: expression

```js
{view.custom.tab} = 'perm'
```


- `props.style.classes`: expression

```js
if({view.custom.editCount} > 0, 'form-card admin-bar-pending', 'form-card')
```


**`root/Content/ChangeBar/Icon`**

- `props.path`: expression

```js
if(!{view.custom.canEdit}, 'material/visibility', if({view.custom.editCount} > 0, 'material/edit', 'material/check_circle'))
```


- `props.style.classes`: expression

```js
if({view.custom.editCount} > 0, 'admin-ico-on', if(!{view.custom.canEdit}, 'admin-ico-muted', 'text-ok'))
```


**`root/Content/ChangeBar/Status`**

- `props.style.classes`: expression

```js
if({view.custom.editCount} > 0, 'form-status admin-status-pending', 'form-status')
```


- `props.text`: expression

```js
if(!{view.custom.canEdit}, 'Read Only · You Can View But Not Change Permissions', if({view.custom.editCount} > 0, toStr({view.custom.editCount}) + if({view.custom.editCount} = 1, ' Unsaved Change', ' Unsaved Changes') + ' · ' + coalesce({view.custom.editSummary}, ''), if(len(coalesce({view.custom.lastSaved}, '')) > 0, {view.custom.lastSaved}, 'No Unsaved Changes')))
```


**`root/Content/ChangeBar/Discard`**

- `props.enabled`: expression

```js
{view.custom.canEdit} && {view.custom.editCount} > 0
```


**`root/Content/ChangeBar/Save`**

- `props.enabled`: expression

```js
{view.custom.canEdit} && {view.custom.editCount} > 0
```


**`root/Content/RolesBody`**

- `position.display`: expression

```js
{view.custom.tab} = 'roles'
```


**`root/Content/RolesBody/RoleList/Head/AddRole`**

- `meta.tooltip.enabled`: expression

```js
len(coalesce(if((coalesce({session.custom.Permissions.RolesPermissions.Edit}, false) && (coalesce({session.custom.Permissions.UserManagement.Add}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false))), '', 'Creating A Role Needs Add Users And Roles And Edit Roles & Permissions'), '')) > 0
```


- `meta.tooltip.text`: expression

```js
if((coalesce({session.custom.Permissions.RolesPermissions.Edit}, false) && (coalesce({session.custom.Permissions.UserManagement.Add}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false))), '', 'Creating A Role Needs Add Users And Roles And Edit Roles & Permissions')
```


- `props.enabled`: expression

```js
(coalesce({session.custom.Permissions.RolesPermissions.Edit}, false) && (coalesce({session.custom.Permissions.UserManagement.Add}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false)))
```


**`root/Content/RolesBody/RoleList/Items`**

- `props.instances`: expression

```js
forEach(coalesce({view.custom.roleInfo}, asList()), asMap('name', it()['name'], 'sub', toStr(it()['users']) + if(it()['users'] = 1, ' User', ' Users') + ' · ' + if(it()['full'], 'All ' + toStr(it()['total']), toStr(it()['granted']) + ' Of ' + toStr(it()['total'])), 'badge1', if(it()['full'], 'Full Access', if(len(it()['base']) > 0, 'Inherits ' + it()['base'], '')), 'badge2', if(it()['restricted'], 'Restricted', ''), 'full', it()['full'], 'selected', it()['name'] = {view.custom.roleSel}, 'msg', 'rpRoleSelect', 'instancePosition', asMap('basis', '62px', 'grow', 0, 'shrink', 0)))
```


**`root/Content/RolesBody/RoleDetail/Head/TitleBlock/Title`**

- `props.text`: expression

```js
coalesce(try({view.custom.selRole}['name'], ''), '')
```


**`root/Content/RolesBody/RoleDetail/Head/TitleBlock/Sub`**

- `props.text`: expression

```js
coalesce(try(if({view.custom.selRole}['full'], 'Full permission role · every permission, always', toStr({view.custom.selRole}['granted']) + ' Of ' + toStr({view.custom.selRole}['total']) + ' Permissions' + if(len({view.custom.selRole}['base']) > 0, ' · Inherits ' + {view.custom.selRole}['base'], '') + if(len({view.custom.selRole}['heirs']) > 0, ' · Inherited By ' + {view.custom.selRole}['heirs'], '')), ''), '')
```


**`root/Content/RolesBody/RoleDetail/Head/EditInMatrix`**

- `position.display`: expression

```js
!coalesce(try({view.custom.selRole}['full'], true), true)
```


**`root/Content/RolesBody/RoleDetail/Users/List`**

- `props.text`: expression

```js
coalesce(try({view.custom.selRole}['membersText'], ''), '')
```


**`root/Content/RolesBody/RoleDetail/Summary/Markdown`**

- `props.source`: expression

```js
coalesce(try({view.custom.selRole}['html'], ''), '')
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 23 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary('default', self.session.props.auth.user.roles)
```

- **`root/Content/HeaderCard/TitleRow/Tabs/Tab_perm`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.tab = 'perm'
```

- **`root/Content/HeaderCard/TitleRow/Tabs/Tab_roles`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.tab = 'roles'
self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary('default', self.session.props.auth.user.roles)
```

- **`root/Content/HeaderCard/Toolbar/ExpandAll`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('rpExpandAll', payload={'open': True}, scope='page')
```

- **`root/Content/HeaderCard/Toolbar/CollapseAll`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('rpExpandAll', payload={'open': False}, scope='page')
```

- **`root/Content/MatrixCard/MatrixBody/Empty/Clear`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
v.search = ''
v.category = ''
v.diffOnly = False
v.focus = None
```

- **`root/Content/ChangeBar/Discard`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('rpDiscard', scope='page')
```

- **`root/Content/ChangeBar/Save`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('rpSave', scope='page')
```

- **`root/Content/RolesBody/RoleList/Head/AddRole`** `component.onActionPerformed`, script action, scope `G`

```python
shared.PermissionMatrix.openWizard(self.page, 'default')
```

- **`root/Content/RolesBody/RoleList/Note/OpenUM`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.navigate('/operations/users')
```

- **`root/Content/RolesBody/RoleDetail/Head/EditInMatrix`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
v.focus = [v.selRole['name']]
v.tab = 'perm'
```

- **`root`** message handler `rpToggle` (scope: page)

```python
if not shared.Security.allowed(self.session, 'RolesPermissions', 'Edit'):
    return
v = self.view
edits = dict((str(k), bool(x)) for k, x in dict(v.custom.edits or {}).items())
k = payload['key'] + '|' + payload['role']
if k in edits:
    del edits[k]
else:
    roles = [str(r['name']) for r in (v.custom.roles or [])]
    row = next((r for r in (v.custom.rows1 or []) if str(r['key']) == payload['key']), None)
    if row is None or payload['role'] not in roles:
        return
    edits[k] = not bool(row['raw'][roles.index(payload['role'])])
v.custom.edits = edits
v.custom.editSummary = shared.PermissionMatrix.editSummary(edits)
v.custom.lastSaved = ''
```

- **`root`** message handler `rpBulk` (scope: page)

```python
if not shared.Security.allowed(self.session, 'RolesPermissions', 'Edit'):
    return
v = self.view
roles = [str(r['name']) for r in (v.custom.roles or [])]
if payload['role'] not in roles:
    return
i = roles.index(payload['role'])
grant = bool(payload['grant'])
rows = [r for r in (v.custom.vis or []) if str(r['cat']) == payload['cat']]
keys = [str(r['key']) for r in rows if bool(r['eff'][i]) != grant and not bool(r['inh'][i])]
if not keys:
    return
verb = 'Grant' if grant else 'Revoke'
shared.Alerts.showAlert(state='info', title='%s All In %s?' % (verb, payload['cat']),
    message='%s %d permission%s in %s %s %s. Nothing is saved until you press Save Changes.' % (verb, len(keys), '' if len(keys) == 1 else 's', payload['cat'], 'to' if grant else 'from', payload['role']),
    showCloseBtn=False, btnTextPrimary=verb + ' All', btnTextSecondary='Cancel', btnActionPrimary='rpBulkApply',
    btnActionSecondary='', payload={'keys': keys, 'role': payload['role'], 'grant': grant}, overlayDismiss=False)
```

- **`root`** message handler `rpBulkApply` (scope: page)

```python
if not shared.Security.allowed(self.session, 'RolesPermissions', 'Edit'):
    return
v = self.view
roles = [str(r['name']) for r in (v.custom.roles or [])]
role = str(payload['role'])
if role not in roles:
    return
i = roles.index(role)
grant = bool(payload['grant'])
raw = dict((str(r['key']), bool(r['raw'][i])) for r in (v.custom.rows1 or []))
edits = dict((str(k), bool(x)) for k, x in dict(v.custom.edits or {}).items())
for key in payload['keys']:
    k = str(key) + '|' + role
    if raw.get(str(key)) == grant:
        edits.pop(k, None)
    else:
        edits[k] = grant
v.custom.edits = edits
v.custom.editSummary = shared.PermissionMatrix.editSummary(edits)
v.custom.lastSaved = ''
```

- **`root`** message handler `rpGroupToggle` (scope: page)

```python
o = dict(self.view.custom.open or {})
n = str(payload['name'])
o[n] = not bool(o.get(n))
self.view.custom.open = o
```

- **`root`** message handler `rpExpandAll` (scope: page)

```python
self.view.custom.open = dict((str(c['Name']), bool(payload['open'])) for c in system.dataset.toPyDataSet(self.view.custom.cats))
```

- **`root`** message handler `rpSave` (scope: page)

```python
if not shared.Security.allowed(self.session, 'RolesPermissions', 'Edit'):
    return
edits = dict((str(k), bool(x)) for k, x in dict(self.view.custom.edits or {}).items())
if not edits:
    return
labels = dict((str(r['key']), str(r['label'])) for r in (self.view.custom.rows1 or []))
n = len(edits)
shared.Alerts.showAlert(state='info', title='Save %d Permission Change%s?' % (n, '' if n == 1 else 's'),
    message=shared.PermissionMatrix.describe(edits, labels) + '\n\nSaved to the Roles & Permissions matrix and recorded in the Audit Log. Sessions update right away.',
    showCloseBtn=False, btnTextPrimary='Save Changes', btnTextSecondary='Cancel', btnActionPrimary='rpSaveConfirmed',
    btnActionSecondary='', payload={'edits': edits}, overlayDismiss=False)
```

- **`root`** message handler `rpSaveConfirmed` (scope: page)

```python
if not shared.Security.allowed(self.session, 'RolesPermissions', 'Edit'):
    return
edits = dict((str(k), bool(x)) for k, x in dict(payload.get('edits') or {}).items())
res = shared.PermissionMatrix.save(self.session, edits)
if not res['ok']:
    shared.Alerts.showAlert(state='error', title='Cannot Save Permissions', message=res['message'], btnTextPrimary='OK')
    return
self.view.custom.edits = {}
self.view.custom.editSummary = ''
self.view.custom.lastSaved = res['message'] + ' ' + system.date.format(system.date.now(), 'h:mm a')
self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary('default', self.session.props.auth.user.roles)
```

- **`root`** message handler `rpDiscard` (scope: page)

```python
n = len(dict(self.view.custom.edits or {}))
if not n:
    return
shared.Alerts.showAlert(state='warning', title='Discard %d Unsaved Change%s?' % (n, '' if n == 1 else 's'),
    message='The matrix goes back to the saved permissions.', showCloseBtn=False, btnTextPrimary='Discard',
    btnTextSecondary='Cancel', btnActionPrimary='rpDiscardConfirmed', btnActionSecondary='', payload={},
    overlayDismiss=False)
```

- **`root`** message handler `rpDiscardConfirmed` (scope: page)

```python
self.view.custom.edits = {}
self.view.custom.editSummary = ''
```

- **`root`** message handler `rpRoleSelect` (scope: page)

```python
self.view.custom.roleSel = str(payload['name'])
```

- **`root`** message handler `nrCreated` (scope: page)

```python
self.view.custom.roleSel = str(payload['name'])
self.view.custom.tab = 'roles'
self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary('default', self.session.props.auth.user.roles)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.showAlert](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.PermissionMatrix.describe](../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.editSummary](../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.roleSummary](../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.PermissionMatrix.save](../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.Security.allowed](../../../../../../scripting/reference/modules/shared-security.md), [shared.Security.rowRules](../../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Embeds** (3): [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./admin/rpgroup.md) (flex repeater), [00\_Pages/Boars Head/Operations/\_Admin/RPRoleHead](./admin/rprolehead.md) (flex repeater), [00\_Pages/Boars Head/Operations/\_Admin/RoleItem](./admin/roleitem.md) (flex repeater)

**Opened or named by** (1): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md)

## Style Classes

<details>
<summary>22 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `admin-empty-title` | 1 | style class |
| `admin-head-label` | 1 | style class |
| `admin-head-sub` | 2 | style class |
| `admin-ico-muted` | 2 | style class |
| `admin-matrix-head` | 1 | style class |
| `admin-md` | 1 | stylesheet |
| `admin-section-label` | 1 | style class |
| `admin-tab` | 2 | style class |
| `admin-tabs` | 1 | style class |
| `admin-toolbar` | 1 | style class |
| `bg-page` | 1 | style class |
| `form-btn` | 5 | style class |
| `form-btn-primary` | 3 | style class |
| `form-card` | 6 | style class |
| `form-check` | 2 | style class |
| `form-input` | 3 | style class |
| `form-section-head` | 2 | style class |
| `form-section-title` | 2 | style class |
| `form-status` | 1 | style class |
| `form-subtitle` | 5 | style class |
| `form-title` | 2 | style class |
| `text-ok` | 1 | style class |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/RolesPermissions`
- `[default]_Config/Security/FullPermissionRoles`
- `[default]_Config/Security/PermissionCatalog`
- `[default]_Config/Security/PermissionCategories`
- `[default]_Config/Security/RestrictedRows`
- `[default]_Config/Security/RoleInherits`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
