---
title: "UserManagement"
sidebar_label: "UserManagement"
description: "Perspective view 00_Pages/Boars Head/Operations/UserManagement/UserManagement (Page): 118 components, 78 bindings, 12 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/UserManagement/UserManagement", "UserManagement", "/operations/users"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/Operations/UserManagement/UserManagement`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/UserManagement/UserManagement` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/UserManagement/UserManagement/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; UserManagement &gt; UserManagement |
| Routes | `/operations/users` (User Management) |
| Root | `ia.container.flex`, height 900, width 1400 |
| Size | 118 components, 78 bindings, 12 event handlers, 0 change scripts, 23 message handlers |
| Last saved | 2026-10-24T17:40:25Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `userSource` | `"default"` | input |

## Custom properties

<details>
<summary>16 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `canSave` | `false` | bound (expr) |
| `data` | `{"allNames": [], "languages": [], "roles": [], "schedules": [], "us...` | |
| `dirty` | `false` | bound (expr) |
| `draft` | `{}` | |
| `mode` | `""` | |
| `msg` | `""` | |
| `orig` | `{}` | |
| `roleFilter` | `""` | |
| `roleInfo` | `[]` | |
| `roleMode` | `""` | |
| `roleName` | `""` | |
| `roleSel` | `""` | |
| `search` | `""` | |
| `selected` | `""` | |
| `tab` | `"users"` | |
| `uq` | `""` | bound (expr) |

</details>

## Component Tree

Component types: ia.container.flex x51, ia.display.label x37, ia.input.button x9, ia.input.text-field x6, ia.display.flex-repeater x5, ia.display.icon x3, ia.input.dropdown x3, ia.input.password-field x2, ia.input.checkbox x1, ia.input.text-area x1.

<details>
<summary>Component tree (118 components)</summary>

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
          Tab_users  ia.display.label  [2 bindings; 1 event]
          Tab_roles  ia.display.label  [2 bindings; 1 event]
    UsersBody  ia.container.flex  [1 binding]
      UserList  ia.container.flex
        Toolbar  ia.container.flex
          R1  ia.container.flex
            Search  ia.input.text-field  [1 binding]
            Add  ia.input.button  [1 binding; 1 event]
          RoleFilter  ia.input.dropdown  [2 bindings]
        Scroll  ia.container.flex
          Users  ia.display.flex-repeater  [1 binding; view: 00_Pages/Boars Head/Operations/_Admin/UMUserRow]
          None  ia.display.label  [1 binding]
      UserDetail  ia.container.flex
        Editor  ia.container.flex  [1 binding]
          Head  ia.container.flex
            Avatar  ia.display.label  [1 binding]
            TitleBlock  ia.container.flex
              Title  ia.display.label  [1 binding]
              Sub  ia.display.label  [1 binding]
          Scroll  ia.container.flex
            Account  ia.container.flex
              H  ia.display.label
              Row  ia.container.flex
                Username  ia.container.flex
                  Label  ia.display.label
                  Input  ia.input.text-field  [2 bindings]
                Password  ia.container.flex
                  Cap  ia.container.flex
                    Label  ia.display.label
                    Change  ia.input.checkbox  [3 bindings]
                  Pw  ia.container.flex
                    P1  ia.input.password-field  [2 bindings]
                    P2  ia.input.password-field  [3 bindings]
            Profile  ia.container.flex
              H  ia.display.label
              R1  ia.container.flex
                First  ia.container.flex
                  Label  ia.display.label
                  Input  ia.input.text-field  [2 bindings]
                Last  ia.container.flex
                  Label  ia.display.label
                  Input  ia.input.text-field  [2 bindings]
              R2  ia.container.flex
                Language  ia.container.flex
                  Label  ia.display.label
                  Input  ia.input.dropdown  [3 bindings]
                Schedule  ia.container.flex
                  Label  ia.display.label
                  Input  ia.input.dropdown  [3 bindings]
                Badge  ia.container.flex
                  Label  ia.display.label
                  Input  ia.input.text-field  [2 bindings]
            Adjustments  ia.container.flex
              H  ia.display.label
              Hint  ia.display.label
              Rows  ia.display.flex-repeater  [2 bindings; view: 00_Pages/Boars Head/Operations/_Admin/UMAdjustRow]
              AddRow  ia.container.flex
                AddAdjustment  ia.input.button  [1 binding; 1 event]
            Roles  ia.container.flex
              H  ia.display.label
              Options  ia.display.flex-repeater  [1 binding; view: 00_Pages/Boars Head/Operations/_Admin/UMRoleOption]
            Contacts  ia.container.flex
              H  ia.display.label
              Rows  ia.display.flex-repeater  [2 bindings; view: 00_Pages/Boars Head/Operations/_Admin/UMContactRow]
              AddRow  ia.container.flex
                AddContact  ia.input.button  [1 binding; 1 event]
            Notes  ia.container.flex
              H  ia.display.label
              Input  ia.input.text-area  [2 bindings]
          ActionBar  ia.container.flex
            Delete  ia.input.button  [1 binding; 1 event]
            Status  ia.display.label  [2 bindings]
            Discard  ia.input.button  [1 binding; 1 event]
            Save  ia.input.button  [1 binding; 1 event]
        Empty  ia.container.flex  [1 binding]
          Icon  ia.display.icon
          Title  ia.display.label
          Hint  ia.display.label
    RolesBody  ia.container.flex  [1 binding]
      RoleList  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          AddRole  ia.input.button  [3 bindings; 1 event]
        Scroll  ia.container.flex
          Items  ia.display.flex-repeater  [1 binding; view: 00_Pages/Boars Head/Operations/_Admin/RoleItem]
      RoleEditor  ia.container.flex
        Editor  ia.container.flex  [1 binding]
          Head  ia.container.flex
            TitleBlock  ia.container.flex
              Title  ia.display.label  [1 binding]
              Sub  ia.display.label  [1 binding]
          Body  ia.container.flex
            Name  ia.container.flex
              Label  ia.display.label
              Input  ia.input.text-field  [2 bindings]
            Note  ia.display.label  [1 binding]
            MembersH  ia.display.label  [2 bindings]
            Members  ia.display.label  [2 bindings]
          ActionBar  ia.container.flex
            Delete  ia.input.button  [1 binding; 1 event]
            Status  ia.display.label  [1 binding]
            Save  ia.input.button  [1 binding; 1 event]
        Empty  ia.container.flex  [1 binding]
          Icon  ia.display.icon
          Title  ia.display.label
          Hint  ia.display.label
```

</details>

## Bindings

78 bindings: expr 63, property 13, expr-struct 2.

<details>
<summary>All 78 bindings, grouped by component</summary>

**`(view)`**

- `custom.canSave`: expression

```js
if({view.custom.mode} = 'add', coalesce({session.custom.Permissions.UserManagement.Add}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false), coalesce({session.custom.Permissions.UserManagement.Edit}, false))
```


- `custom.dirty`: expression

```js
{view.custom.mode} = 'add' || !(toStr(coalesce(try({view.custom.draft}['username'], ''), '')) = toStr(coalesce(try({view.custom.orig}['username'], ''), '')) && toStr(coalesce(try({view.custom.draft}['firstname'], ''), '')) = toStr(coalesce(try({view.custom.orig}['firstname'], ''), '')) && toStr(coalesce(try({view.custom.draft}['lastname'], ''), '')) = toStr(coalesce(try({view.custom.orig}['lastname'], ''), '')) && toStr(coalesce(try({view.custom.draft}['schedule'], ''), '')) = toStr(coalesce(try({view.custom.orig}['schedule'], ''), '')) && toStr(coalesce(try({view.custom.draft}['language'], ''), '')) = toStr(coalesce(try({view.custom.orig}['language'], ''), '')) && toStr(coalesce(try({view.custom.draft}['badge'], ''), '')) = toStr(coalesce(try({view.custom.orig}['badge'], ''), '')) && toStr(coalesce(try({view.custom.draft}['notes'], ''), '')) = toStr(coalesce(try({view.custom.orig}['notes'], ''), '')) && jsonEncode(coalesce(try({view.custom.draft}['roles'], asList()), asList())) = jsonEncode(coalesce(try({view.custom.orig}['roles'], asList()), asList())) && jsonEncode(coalesce(try({view.custom.draft}['contacts'], asList()), asList())) = jsonEncode(coalesce(try({view.custom.orig}['contacts'], asList()), asList())) && jsonEncode(coalesce(try({view.custom.draft}['adjustments'], asList()), asList())) = jsonEncode(coalesce(try({view.custom.orig}['adjustments'], asList()), asList())) && !coalesce(try({view.custom.draft}['changePassword'], false), false))
```


- `custom.uq`: expression

```js
lower(trim(coalesce({view.custom.search}, '')))
```


**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../../common-patterns.md#pattern-4).

**`root/AccessDenied`**

- `position.display`: expression

```js
!(coalesce({session.custom.Administrator}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false))
```


**`root/Content`**

- `position.display`: expression

```js
(coalesce({session.custom.Administrator}, false) || coalesce({session.custom.Permissions.UserManagement.Edit}, false))
```


**`root/Content/HeaderCard/TitleRow/Tabs/Tab_users`**

- `props.style.classes`: expression

```js
if({view.custom.tab} = 'users', 'admin-tab admin-tab-active', 'admin-tab')
```


- `props.text`: expression

```js
'Users  ' + toStr(len(coalesce(try({view.custom.data}['users'], asList()), asList())))
```


**`root/Content/HeaderCard/TitleRow/Tabs/Tab_roles`**

- `props.style.classes`: expression

```js
if({view.custom.tab} = 'roles', 'admin-tab admin-tab-active', 'admin-tab')
```


- `props.text`: expression

```js
'Roles  ' + toStr(len(coalesce(try({view.custom.data}['roles'], asList()), asList())))
```


**`root/Content/UsersBody`**

- `position.display`: expression

```js
{view.custom.tab} = 'users'
```


**`root/Content/UsersBody/UserList/Toolbar/R1/Search`**

- `props.text`: property `view.custom.search` (bidirectional)

**`root/Content/UsersBody/UserList/Toolbar/R1/Add`**

- `props.enabled`: expression

```js
coalesce({session.custom.Permissions.UserManagement.Add}, false)
```


**`root/Content/UsersBody/UserList/Toolbar/RoleFilter`**

- `props.options`: expression

```js
forEach(coalesce(try({view.custom.data}['roles'], asList()), asList()), asMap('value', it()['name'], 'label', it()['name']))
```


- `props.value`: property `view.custom.roleFilter` (bidirectional)

**`root/Content/UsersBody/UserList/Scroll/Users`**

- `props.instances`: expression

```js
forEach(where(coalesce(try({view.custom.data}['users'], asList()), asList()), (len({view.custom.uq}) = 0 || indexOf(it()['search'], {view.custom.uq}) >= 0) && (len(coalesce({view.custom.roleFilter}, '')) = 0 || len(where(it()['roles'], it() = {view.custom.roleFilter})) > 0)), asMap('username', it()['username'], 'display', it()['display'], 'initials', it()['initials'], 'role1', coalesce(try(it()['roles'][0], ''), ''), 'more', if(len(it()['roles']) > 1, '+' + toStr(len(it()['roles']) - 1), ''), 'selected', it()['username'] = {view.custom.selected} && {view.custom.mode} = 'edit', 'instancePosition', asMap('basis', '56px', 'grow', 0, 'shrink', 0)))
```


**`root/Content/UsersBody/UserList/Scroll/None`**

- `position.display`: expression

```js
len(forEach(where(coalesce(try({view.custom.data}['users'], asList()), asList()), (len({view.custom.uq}) = 0 || indexOf(it()['search'], {view.custom.uq}) >= 0) && (len(coalesce({view.custom.roleFilter}, '')) = 0 || len(where(it()['roles'], it() = {view.custom.roleFilter})) > 0)), asMap('username', it()['username'], 'display', it()['display'], 'initials', it()['initials'], 'role1', coalesce(try(it()['roles'][0], ''), ''), 'more', if(len(it()['roles']) > 1, '+' + toStr(len(it()['roles']) - 1), ''), 'selected', it()['username'] = {view.custom.selected} && {view.custom.mode} = 'edit', 'instancePosition', asMap('basis', '56px', 'grow', 0, 'shrink', 0)))) = 0
```


**`root/Content/UsersBody/UserDetail/Editor`**

- `position.display`: expression

```js
len(coalesce({view.custom.mode}, '')) > 0
```


**`root/Content/UsersBody/UserDetail/Editor/Head/Avatar`**

- `props.text`: expression

```js
if({view.custom.mode} = 'add', '+', coalesce(try(where({view.custom.data}['users'], it()['username'] = {view.custom.selected})[0]['initials'], ''), ''))
```


**`root/Content/UsersBody/UserDetail/Editor/Head/TitleBlock/Title`**

- `props.text`: expression

```js
if({view.custom.mode} = 'add', 'New User', coalesce(try(where({view.custom.data}['users'], it()['username'] = {view.custom.selected})[0]['display'], ''), ''))
```


**`root/Content/UsersBody/UserDetail/Editor/Head/TitleBlock/Sub`**

- `props.text`: expression

```js
if({view.custom.mode} = 'add', 'Add User · user source default', {view.custom.selected} + if({view.custom.selected} = {session.props.auth.user.userName}, ' · You are signed in as this user', ''))
```


**`root/Content/UsersBody/UserDetail/Editor/Scroll/Account/Row/Username/Input`**

- `props.enabled`: expression

```js
{view.custom.mode} = 'add' && {view.custom.canSave}
```


- `props.text`: property `view.custom.draft.username` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Account/Row/Password/Cap/Change`**

- `position.display`: expression

```js
{view.custom.mode} = 'edit'
```


- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.selected`: property `view.custom.draft.changePassword` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Account/Row/Password/Pw/P1`**

- `props.enabled`: expression

```js
coalesce({view.custom.draft.changePassword}, false) && {view.custom.canSave}
```


- `props.text`: property `view.custom.draft.password` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Account/Row/Password/Pw/P2`**

- `props.enabled`: expression

```js
coalesce({view.custom.draft.changePassword}, false) && {view.custom.canSave}
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.draft.changePassword}, false) && len(coalesce({view.custom.draft.confirm}, '')) > 0 && {view.custom.draft.confirm} != {view.custom.draft.password}, 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.draft.confirm` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Profile/R1/First/Input`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.text`: property `view.custom.draft.firstname` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Profile/R1/Last/Input`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.text`: property `view.custom.draft.lastname` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Profile/R2/Language/Input`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.options`: expression

```js
coalesce(try({view.custom.data}['languages'], asList()), asList())
```


- `props.value`: property `view.custom.draft.language` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Profile/R2/Schedule/Input`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.options`: expression

```js
coalesce(try({view.custom.data}['schedules'], asList()), asList())
```


- `props.value`: property `view.custom.draft.schedule` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Profile/R2/Badge/Input`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.text`: property `view.custom.draft.badge` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/Scroll/Adjustments/Rows`**

- `position.basis`: expression

```js
toStr(len(coalesce(try({view.custom.draft}['adjustments'], asList()), asList())) * 112) + 'px'
```


- `props.instances`: expression

```js
forEach(coalesce(try({view.custom.draft}['adjustments'], asList()), asList()), asMap('i', idx(), 'start', it()['start'], 'end', it()['end'], 'available', it()['available'], 'note', it()['note'], 'canEdit', {view.custom.canSave}, 'instancePosition', asMap('basis', '104px', 'grow', 0, 'shrink', 0)))
```


**`root/Content/UsersBody/UserDetail/Editor/Scroll/Adjustments/AddRow/AddAdjustment`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


**`root/Content/UsersBody/UserDetail/Editor/Scroll/Roles/Options`**

- `props.instances`: expression

```js
forEach(coalesce(try({view.custom.data}['roles'], asList()), asList()), asMap('name', it()['name'], 'sub', if(it()['full'], 'Full Access', toStr(it()['users']) + if(it()['users'] = 1, ' User', ' Users')) + if(it()['restricted'], ' · Restricted', ''), 'on', len(where(coalesce(try({view.custom.draft}['roles'], asList()), asList()), it() = it(1)['name'])) > 0, 'canEdit', {view.custom.canSave}, 'instancePosition', asMap('basis', '178px', 'grow', 0, 'shrink', 0)))
```


**`root/Content/UsersBody/UserDetail/Editor/Scroll/Contacts/Rows`**

- `position.basis`: expression

```js
toStr(len(coalesce(try({view.custom.draft}['contacts'], asList()), asList())) * 48) + 'px'
```


- `props.instances`: expression

```js
forEach(coalesce(try({view.custom.draft}['contacts'], asList()), asList()), asMap('i', idx(), 'type', it()['type'], 'value', it()['value'], 'canEdit', {view.custom.canSave}, 'instancePosition', asMap('basis', '40px', 'grow', 0, 'shrink', 0)))
```


**`root/Content/UsersBody/UserDetail/Editor/Scroll/Contacts/AddRow/AddContact`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


**`root/Content/UsersBody/UserDetail/Editor/Scroll/Notes/Input`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.text`: property `view.custom.draft.notes` (bidirectional)

**`root/Content/UsersBody/UserDetail/Editor/ActionBar/Delete`**

- `props.enabled`: expression

```js
coalesce({session.custom.Permissions.UserManagement.Edit}, false) && {view.custom.mode} = 'edit' && {view.custom.selected} != {session.props.auth.user.userName}
```


**`root/Content/UsersBody/UserDetail/Editor/ActionBar/Status`**

- `props.style.classes`: expression

```js
if({view.custom.dirty}, 'form-status admin-status-pending', 'form-status')
```


- `props.text`: expression

```js
if({view.custom.mode} = 'add', 'New User · Fill In The Account, Then Save', if({view.custom.dirty}, 'Unsaved Changes', if(len(coalesce({view.custom.msg}, '')) > 0, {view.custom.msg}, 'No Unsaved Changes')))
```


**`root/Content/UsersBody/UserDetail/Editor/ActionBar/Discard`**

- `props.enabled`: expression

```js
{view.custom.dirty} && {view.custom.mode} = 'edit'
```


**`root/Content/UsersBody/UserDetail/Editor/ActionBar/Save`**

- `props.enabled`: expression

```js
{view.custom.dirty} && {view.custom.canSave}
```


**`root/Content/UsersBody/UserDetail/Empty`**

- `position.display`: expression

```js
!len(coalesce({view.custom.mode}, '')) > 0
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


**`root/Content/RolesBody/RoleList/Scroll/Items`**

- `props.instances`: expression

```js
forEach(coalesce(try({view.custom.data}['roles'], asList()), asList()), asMap('name', it()['name'], 'sub', toStr(it()['users']) + if(it()['users'] = 1, ' User', ' Users'), 'badge1', if(it()['full'], 'Full Access', ''), 'badge2', if(it()['restricted'], 'Restricted', ''), 'full', it()['full'], 'selected', it()['name'] = {view.custom.roleSel} && {view.custom.roleMode} = 'edit', 'msg', 'umRoleSelect', 'instancePosition', asMap('basis', '62px', 'grow', 0, 'shrink', 0)))
```


**`root/Content/RolesBody/RoleEditor/Editor`**

- `position.display`: expression

```js
len(coalesce({view.custom.roleMode}, '')) > 0
```


**`root/Content/RolesBody/RoleEditor/Editor/Head/TitleBlock/Title`**

- `props.text`: expression

```js
if({view.custom.roleMode} = 'add', 'New Role', {view.custom.roleSel})
```


**`root/Content/RolesBody/RoleEditor/Editor/Head/TitleBlock/Sub`**

- `props.text`: expression

```js
if({view.custom.roleMode} = 'add', 'Add a role to user source default', coalesce(try(toStr(where(coalesce(try({view.custom.data}['roles'], asList()), asList()), it()['name'] = {view.custom.roleSel})[0]['users']) + if(where(coalesce(try({view.custom.data}['roles'], asList()), asList()), it()['name'] = {view.custom.roleSel})[0]['users'] = 1, ' User', ' Users') + if(where(coalesce(try({view.custom.data}['roles'], asList()), asList()), it()['name'] = {view.custom.roleSel})[0]['full'], ' · Full permission role', ''), ''), ''))
```


**`root/Content/RolesBody/RoleEditor/Editor/Body/Name/Input`**

- `props.enabled`: expression

```js
{view.custom.canSave}
```


- `props.text`: property `view.custom.roleName` (bidirectional)

**`root/Content/RolesBody/RoleEditor/Editor/Body/Note`**

- `position.display`: expression

```js
{view.custom.roleMode} = 'edit'
```


**`root/Content/RolesBody/RoleEditor/Editor/Body/MembersH`**

- `position.display`: expression

```js
{view.custom.roleMode} = 'edit'
```


- `props.text`: expression

```js
'Members · ' + coalesce(try(toStr(where(coalesce(try({view.custom.data}['roles'], asList()), asList()), it()['name'] = {view.custom.roleSel})[0]['users']), '0'), '0') + "  (change a user's roles on the Users tab)"
```


**`root/Content/RolesBody/RoleEditor/Editor/Body/Members`**

- `position.display`: expression

```js
{view.custom.roleMode} = 'edit'
```


- `props.text`: expression

```js
coalesce(try(where(coalesce(try({view.custom.roleInfo}, asList()), asList()), it()['name'] = {view.custom.roleSel})[0]['membersText'], ''), '')
```


**`root/Content/RolesBody/RoleEditor/Editor/ActionBar/Delete`**

- `props.enabled`: expression

```js
coalesce({session.custom.Permissions.UserManagement.Edit}, false) && {view.custom.roleMode} = 'edit' && !coalesce(try(where(coalesce(try({view.custom.data}['roles'], asList()), asList()), it()['name'] = {view.custom.roleSel})[0]['full'], true), true)
```


**`root/Content/RolesBody/RoleEditor/Editor/ActionBar/Status`**

- `props.text`: expression

```js
if({view.custom.roleMode} = 'add', 'New Role', if(coalesce({view.custom.roleName}, '') != {view.custom.roleSel}, 'Unsaved Changes', 'No Unsaved Changes'))
```


**`root/Content/RolesBody/RoleEditor/Editor/ActionBar/Save`**

- `props.enabled`: expression

```js
{view.custom.canSave} && len(trim(coalesce({view.custom.roleName}, ''))) > 0 && coalesce({view.custom.roleName}, '') != {view.custom.roleSel}
```


**`root/Content/RolesBody/RoleEditor/Empty`**

- `position.display`: expression

```js
len(coalesce({view.custom.roleMode}, '')) = 0
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 35 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
if not shared.Security.allowed(self.session, 'UserManagement', 'Edit'):
    return
self.view.custom.data = shared.UserAdmin.pageData(self.view.params.userSource, self.session.props.auth.user.roles)
self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary(self.view.params.userSource, self.session.props.auth.user.roles)
```

- **`root/Content/HeaderCard/TitleRow/Tabs/Tab_users`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.tab = 'users'
```

- **`root/Content/HeaderCard/TitleRow/Tabs/Tab_roles`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.tab = 'roles'
```

- **`root/Content/UsersBody/UserList/Toolbar/R1/Add`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umAdd', payload={}, scope='page')
```

- **`root/Content/UsersBody/UserDetail/Editor/Scroll/Adjustments/AddRow/AddAdjustment`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umAdjAdd', payload={}, scope='page')
```

- **`root/Content/UsersBody/UserDetail/Editor/Scroll/Contacts/AddRow/AddContact`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umContactAdd', payload={}, scope='page')
```

- **`root/Content/UsersBody/UserDetail/Editor/ActionBar/Delete`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umDelete', payload={}, scope='page')
```

- **`root/Content/UsersBody/UserDetail/Editor/ActionBar/Discard`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umDiscard', payload={}, scope='page')
```

- **`root/Content/UsersBody/UserDetail/Editor/ActionBar/Save`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umSave', payload={}, scope='page')
```

- **`root/Content/RolesBody/RoleList/Head/AddRole`** `component.onActionPerformed`, script action, scope `G`

```python
shared.PermissionMatrix.openWizard(self.page, 'default')
```

- **`root/Content/RolesBody/RoleEditor/Editor/ActionBar/Delete`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umRoleDelete', payload={}, scope='page')
```

- **`root/Content/RolesBody/RoleEditor/Editor/ActionBar/Save`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('umRoleSave', payload={}, scope='page')
```

- **`root`** message handler `umSelect` (scope: page)

```python
def draftOf(u):
    if u is None:
        return {'username': '', 'originalUsername': '', 'firstname': '', 'lastname': '', 'schedule': 'Always', 'language': 'en', 'badge': '', 'notes': '', 'roles': [], 'contacts': [], 'adjustments': [], 'changePassword': True, 'password': '', 'confirm': ''}
    return {'username': u['username'], 'originalUsername': u['username'], 'firstname': u['first'], 'lastname': u['last'], 'schedule': u['schedule'], 'language': u['language'], 'badge': u['badge'], 'notes': u['notes'], 'roles': [str(r) for r in u['roles']], 'contacts': [{'type': str(c['type']), 'value': str(c['value'])} for c in u['contacts']], 'adjustments': [{'start': a['start'], 'end': a['end'], 'available': bool(a['available']), 'note': str(a['note'])} for a in (u['adjustments'] or [])], 'changePassword': False, 'password': '', 'confirm': ''}
def userOf(name):
    return next((u for u in (self.view.custom.data['users'] or []) if str(u['username']) == name), None)
def select(name, mode):
    d = draftOf(userOf(name) if mode == 'edit' else None)
    self.view.custom.mode = mode
    self.view.custom.selected = name if mode == 'edit' else ''
    self.view.custom.draft = d
    self.view.custom.orig = dict(d)
if self.view.custom.dirty and not payload.get('force'):
    shared.Alerts.showAlert(state='warning', title='Discard Unsaved Changes?', message='Your changes to this user are not saved.', showCloseBtn=False, btnTextPrimary='Discard', btnTextSecondary='Cancel', btnActionPrimary='umSelect', btnActionSecondary='', payload=dict(payload, force=True), overlayDismiss=False)
    return
select(str(payload['name']), 'edit')
```

- **`root`** message handler `umAdd` (scope: page)

```python
def draftOf(u):
    if u is None:
        return {'username': '', 'originalUsername': '', 'firstname': '', 'lastname': '', 'schedule': 'Always', 'language': 'en', 'badge': '', 'notes': '', 'roles': [], 'contacts': [], 'adjustments': [], 'changePassword': True, 'password': '', 'confirm': ''}
    return {'username': u['username'], 'originalUsername': u['username'], 'firstname': u['first'], 'lastname': u['last'], 'schedule': u['schedule'], 'language': u['language'], 'badge': u['badge'], 'notes': u['notes'], 'roles': [str(r) for r in u['roles']], 'contacts': [{'type': str(c['type']), 'value': str(c['value'])} for c in u['contacts']], 'adjustments': [{'start': a['start'], 'end': a['end'], 'available': bool(a['available']), 'note': str(a['note'])} for a in (u['adjustments'] or [])], 'changePassword': False, 'password': '', 'confirm': ''}
def userOf(name):
    return next((u for u in (self.view.custom.data['users'] or []) if str(u['username']) == name), None)
def select(name, mode):
    d = draftOf(userOf(name) if mode == 'edit' else None)
    self.view.custom.mode = mode
    self.view.custom.selected = name if mode == 'edit' else ''
    self.view.custom.draft = d
    self.view.custom.orig = dict(d)
if self.view.custom.dirty and not payload.get('force'):
    shared.Alerts.showAlert(state='warning', title='Discard Unsaved Changes?', message='Your changes to this user are not saved.', showCloseBtn=False, btnTextPrimary='Discard', btnTextSecondary='Cancel', btnActionPrimary='umAdd', btnActionSecondary='', payload=dict(payload, force=True), overlayDismiss=False)
    return
select('', 'add')
```

- **`root`** message handler `umRoleToggle` (scope: page)

```python
d = dict(self.view.custom.draft)
roles = [str(r) for r in (d.get('roles') or [])]
n = str(payload['name'])
if n in roles:
    roles.remove(n)
else:
    roles.append(n)
d['roles'] = sorted(roles, key=lambda s: s.lower())
self.view.custom.draft = d
```

- **`root`** message handler `umContactSet` (scope: page)

```python
d = dict(self.view.custom.draft)
cs = [dict(c) for c in (d.get('contacts') or [])]
i = int(payload['i'])
if 0 <= i < len(cs):
    cs[i][str(payload['field'])] = payload['value'] or ''
    d['contacts'] = cs
    self.view.custom.draft = d
```

- **`root`** message handler `umContactRemove` (scope: page)

```python
d = dict(self.view.custom.draft)
cs = [dict(c) for c in (d.get('contacts') or [])]
i = int(payload['i'])
if 0 <= i < len(cs):
    del cs[i]
    d['contacts'] = cs
    self.view.custom.draft = d
```

- **`root`** message handler `umContactAdd` (scope: page)

```python
d = dict(self.view.custom.draft)
d['contacts'] = [dict(c) for c in (d.get('contacts') or [])] + [{'type': 'email', 'value': ''}]
self.view.custom.draft = d
```

- **`root`** message handler `umAdjSet` (scope: page)

```python
d = dict(self.view.custom.draft)
cs = [dict(c) for c in (d.get('adjustments') or [])]
i = int(payload['i'])
f = str(payload['field'])
if 0 <= i < len(cs):
    v = payload['value']
    if f in ('start', 'end'):
        v = shared.UserAdmin.adjMillis(v)
        if v is None:
            return
    elif f == 'available':
        v = bool(v)
    else:
        v = v or ''
    cs[i][f] = v
    d['adjustments'] = cs
    self.view.custom.draft = d
```

- **`root`** message handler `umAdjRemove` (scope: page)

```python
d = dict(self.view.custom.draft)
cs = [dict(c) for c in (d.get('adjustments') or [])]
i = int(payload['i'])
if 0 <= i < len(cs):
    del cs[i]
    d['adjustments'] = cs
    self.view.custom.draft = d
```

- **`root`** message handler `umAdjAdd` (scope: page)

```python
d = dict(self.view.custom.draft)
now = system.date.toMillis(system.date.midnight(system.date.now()))
d['adjustments'] = [dict(c) for c in (d.get('adjustments') or [])] + [{'start': now, 'end': now + 86399000, 'available': False, 'note': ''}]
self.view.custom.draft = d
```

- **`root`** message handler `umSave` (scope: page)

```python
d = self.view.custom.draft
mode = self.view.custom.mode
errs = shared.UserAdmin.validateUser(self.view.params.userSource, mode, d)
if errs:
    shared.Alerts.showAlert(state='error', title='Cannot Save User', message='\n'.join(errs), btnTextPrimary='OK')
    return
o = self.view.custom.orig
new = set(str(r) for r in (d['roles'] or []))
old = set(str(r) for r in (o['roles'] or [])) if mode == 'edit' else set()
lines = []
if new - old:
    lines.append('Add Roles: ' + ', '.join(sorted(new - old)))
if old - new:
    lines.append('Remove Roles: ' + ', '.join(sorted(old - new)))
if mode == 'edit' and d['changePassword']:
    lines.append('Change Password')
if not lines:
    lines.append('Update Profile / Contact Information')
title = ('Add User %s?' if mode == 'add' else 'Save User %s?') % d['username']
shared.Alerts.showAlert(state='info', title=title, message='\n'.join(lines) + '\n\nRecorded in the Audit Log.',
    showCloseBtn=False, btnTextPrimary='Save User', btnTextSecondary='Cancel', btnActionPrimary='umSaveConfirmed',
    btnActionSecondary='', payload={}, overlayDismiss=False)
```

- **`root`** message handler `umSaveConfirmed` (scope: page)

```python
def draftOf(u):
    if u is None:
        return {'username': '', 'originalUsername': '', 'firstname': '', 'lastname': '', 'schedule': 'Always', 'language': 'en', 'badge': '', 'notes': '', 'roles': [], 'contacts': [], 'adjustments': [], 'changePassword': True, 'password': '', 'confirm': ''}
    return {'username': u['username'], 'originalUsername': u['username'], 'firstname': u['first'], 'lastname': u['last'], 'schedule': u['schedule'], 'language': u['language'], 'badge': u['badge'], 'notes': u['notes'], 'roles': [str(r) for r in u['roles']], 'contacts': [{'type': str(c['type']), 'value': str(c['value'])} for c in u['contacts']], 'adjustments': [{'start': a['start'], 'end': a['end'], 'available': bool(a['available']), 'note': str(a['note'])} for a in (u['adjustments'] or [])], 'changePassword': False, 'password': '', 'confirm': ''}
def userOf(name):
    return next((u for u in (self.view.custom.data['users'] or []) if str(u['username']) == name), None)
def select(name, mode):
    d = draftOf(userOf(name) if mode == 'edit' else None)
    self.view.custom.mode = mode
    self.view.custom.selected = name if mode == 'edit' else ''
    self.view.custom.draft = d
    self.view.custom.orig = dict(d)
d = dict(self.view.custom.draft)
mode = self.view.custom.mode
draft = dict(d, roles=[str(r) for r in (d.get('roles') or [])], contacts=[dict(c) for c in (d.get('contacts') or [])])
if not shared.UserAdmin.saveUser(self.session, self.view.params.userSource, mode, draft):
    return
self.view.custom.data = shared.UserAdmin.pageData(self.view.params.userSource, self.session.props.auth.user.roles)
self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary(self.view.params.userSource, self.session.props.auth.user.roles)
select(str(d['username']).strip(), 'edit')
self.view.custom.msg = ('Added ' if mode == 'add' else 'Saved ') + str(d['username']).strip() + ' ' + system.date.format(system.date.now(), 'h:mm a')
```

- **`root`** message handler `umDiscard` (scope: page)

```python
if not self.view.custom.dirty:
    return
shared.Alerts.showAlert(state='warning', title='Discard Unsaved Changes?', message='The form goes back to the saved user.', showCloseBtn=False, btnTextPrimary='Discard', btnTextSecondary='Cancel', btnActionPrimary='umDiscardConfirmed', btnActionSecondary='', payload={}, overlayDismiss=False)
```

- **`root`** message handler `umDiscardConfirmed` (scope: page)

```python
self.view.custom.draft = dict(self.view.custom.orig)
```

- **`root`** message handler `umDelete` (scope: page)

```python
name = self.view.custom.selected
if not name:
    return
shared.Alerts.showAlert(state='warning', title='Delete User %s?' % name, message='The user is removed from the user source and can no longer sign in. This cannot be undone.', showCloseBtn=False, btnTextPrimary='Delete User', btnTextSecondary='Cancel', btnActionPrimary='umDeleteConfirmed', btnActionSecondary='', payload={'name': name}, overlayDismiss=False)
```

- **`root`** message handler `umDeleteConfirmed` (scope: page)

```python
if shared.UserAdmin.deleteUser(self.session, self.view.params.userSource, str(payload['name'])):
    self.view.custom.selected = ''
    self.view.custom.mode = ''
    self.view.custom.msg = 'Deleted ' + str(payload['name'])
    self.view.custom.data = shared.UserAdmin.pageData(self.view.params.userSource, self.session.props.auth.user.roles)
    self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary(self.view.params.userSource, self.session.props.auth.user.roles)
```

- **`root`** message handler `umRoleSelect` (scope: page)

```python
r = next((x for x in (self.view.custom.data['roles'] or []) if str(x['name']) == str(payload['name'])), None)
if r is None:
    return
self.view.custom.roleMode = 'edit'
self.view.custom.roleSel = str(r['name'])
self.view.custom.roleName = str(r['name'])
```

- **`root`** message handler `umRoleAdd` (scope: page)

```python
self.view.custom.roleMode = 'add'
self.view.custom.roleSel = ''
self.view.custom.roleName = ''
```

- **`root`** message handler `umRoleSave` (scope: page)

```python
mode = self.view.custom.roleMode
old = self.view.custom.roleSel
new = str(self.view.custom.roleName or '').strip()
if mode == 'edit' and new == old:
    return
msg = ('Add the role %s?' % new) if mode == 'add' else ('Rename %s to %s? The Roles & Permissions column and the _Config/Security role lists are not renamed automatically - update them after the rename.' % (old, new))
shared.Alerts.showAlert(state='info', title='Add Role?' if mode == 'add' else 'Rename Role?', message=msg, showCloseBtn=False, btnTextPrimary='Save Role', btnTextSecondary='Cancel', btnActionPrimary='umRoleSaveConfirmed', btnActionSecondary='', payload={}, overlayDismiss=False)
```

- **`root`** message handler `umRoleSaveConfirmed` (scope: page)

```python
mode = self.view.custom.roleMode
new = str(self.view.custom.roleName or '').strip()
if shared.UserAdmin.saveRole(self.session, self.view.params.userSource, mode, self.view.custom.roleSel, new):
    self.view.custom.data = shared.UserAdmin.pageData(self.view.params.userSource, self.session.props.auth.user.roles)
    self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary(self.view.params.userSource, self.session.props.auth.user.roles)
    self.view.custom.roleMode = 'edit'
    self.view.custom.roleSel = new
```

- **`root`** message handler `umRoleDelete` (scope: page)

```python
name = self.view.custom.roleSel
if not name:
    return
shared.Alerts.showAlert(state='warning', title='Delete Role %s?' % name, message='Users lose this role. Its Roles & Permissions column stays in the matrix (unused). This cannot be undone.', showCloseBtn=False, btnTextPrimary='Delete Role', btnTextSecondary='Cancel', btnActionPrimary='umRoleDeleteConfirmed', btnActionSecondary='', payload={'name': name}, overlayDismiss=False)
```

- **`root`** message handler `umRoleDeleteConfirmed` (scope: page)

```python
if shared.UserAdmin.deleteRole(self.session, self.view.params.userSource, str(payload['name'])):
    self.view.custom.data = shared.UserAdmin.pageData(self.view.params.userSource, self.session.props.auth.user.roles)
    self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary(self.view.params.userSource, self.session.props.auth.user.roles)
    self.view.custom.roleSel = ''
    self.view.custom.roleMode = ''
```

- **`root`** message handler `nrCreated` (scope: page)

```python
self.view.custom.data = shared.UserAdmin.pageData(self.view.params.userSource, self.session.props.auth.user.roles)
self.view.custom.roleInfo = shared.PermissionMatrix.roleSummary(self.view.params.userSource, self.session.props.auth.user.roles)
self.view.custom.tab = 'roles'
self.view.custom.roleMode = 'edit'
self.view.custom.roleSel = str(payload['name'])
self.view.custom.roleName = str(payload['name'])
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.showAlert](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.PermissionMatrix.roleSummary](../../../../../../../scripting/reference/modules/shared-permissionmatrix.md), [shared.Security.allowed](../../../../../../../scripting/reference/modules/shared-security.md), [shared.UserAdmin.adjMillis](../../../../../../../scripting/reference/modules/shared-useradmin.md), [shared.UserAdmin.deleteRole](../../../../../../../scripting/reference/modules/shared-useradmin.md), [shared.UserAdmin.deleteUser](../../../../../../../scripting/reference/modules/shared-useradmin.md), [shared.UserAdmin.pageData](../../../../../../../scripting/reference/modules/shared-useradmin.md), [shared.UserAdmin.saveRole](../../../../../../../scripting/reference/modules/shared-useradmin.md), [shared.UserAdmin.saveUser](../../../../../../../scripting/reference/modules/shared-useradmin.md), [shared.UserAdmin.validateUser](../../../../../../../scripting/reference/modules/shared-useradmin.md).

## Related Views

**Embeds** (5): [00\_Pages/Boars Head/Operations/\_Admin/RoleItem](../admin/roleitem.md) (flex repeater), [00\_Pages/Boars Head/Operations/\_Admin/UMAdjustRow](../admin/umadjustrow.md) (flex repeater), [00\_Pages/Boars Head/Operations/\_Admin/UMContactRow](../admin/umcontactrow.md) (flex repeater), [00\_Pages/Boars Head/Operations/\_Admin/UMRoleOption](../admin/umroleoption.md) (flex repeater), [00\_Pages/Boars Head/Operations/\_Admin/UMUserRow](../admin/umuserrow.md) (flex repeater)

**Opened or named by** (1): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md)

## Style Classes

<details>
<summary>21 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `admin-avatar` | 1 | style class |
| `admin-avatar-selected` | 1 | style class |
| `admin-btn-danger` | 2 | style class |
| `admin-empty-title` | 2 | style class |
| `admin-ico-muted` | 3 | style class |
| `admin-note` | 1 | style class |
| `admin-section-label` | 7 | style class |
| `admin-tab` | 2 | style class |
| `admin-tabs` | 1 | style class |
| `bg-page` | 1 | style class |
| `form-btn` | 3 | style class |
| `form-btn-primary` | 4 | style class |
| `form-card` | 6 | style class |
| `form-check` | 2 | style class |
| `form-input` | 12 | style class |
| `form-label` | 8 | style class |
| `form-section-head` | 3 | style class |
| `form-section-title` | 2 | style class |
| `form-status` | 2 | style class |
| `form-subtitle` | 8 | style class |
| `form-title` | 3 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
