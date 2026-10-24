---
title: Bindings
sidebar_position: 6
description: BH binding conventions - expression first, script last - Integration Toolkit functions, null-safety, LF-only expressions, empty tagPath defaults, indirect tag paths and PAX member paths, with real examples from the views.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Pump/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Utility/OverviewStatusTile/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/_Shared/CG/AhuEvapPanel/view.json"
  - "gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py"
last_verified: 2026-10-24
---

# Bindings

A **binding** makes a property follow something else: a tag, another property, an expression, a query. In the
Designer you add one with the chain-link icon next to a property in the Property Editor. In `view.json` it sits in
`propConfig.<property path>.binding`. Every binding in the project is listed on its view's
[reference page](./reference/views-index.md); bindings repeated in many views are on
[Common Binding Patterns](./reference/common-patterns.md).

The project has about 5,500 bindings: roughly 74 % expression, 17 % property, 7 % expression structure, 1 % tag,
plus a handful of named query and tag history bindings.

## Rule: Expression First, Script Last

Use the first one that works (a project rule):

1. **Expression** (`expr`): a single Ignition expression.
2. **Structured expression** (`expr-struct`): several named expressions combined into one object; the binding
   re-evaluates when any part changes.
3. **Expression transform** on a property or tag binding.
4. **Script or script transform**: only when nothing else can do it (one-shot commands, confirm dialogs, tag browse
   or configure, building lists).

Why: expressions evaluate in the gateway's expression engine without a Jython round trip, they are easy to read in
the Designer, and they fail soft with `try()` / `coalesce()`. Script transforms run on every change and are harder
to review.

### 1. Expression

```js
// Header root props.style.classes
if(coalesce({session.props.animations}, true), 'app-header', 'app-header animations-off')
```

### 2. Structured Expression

```js
// session.custom.Permissions (session props), then a script transform
matrix:   tag('[default]_Config/RolesPermissions')
roles:    {session.props.auth.user.roles}
full:     tag('[default]_Config/Security/FullPermissionRoles')
inherits: tag('[default]_Config/Security/RoleInherits')
```

The struct makes the result re-evaluate on login or role change as well as on a matrix edit. The transform is a
script only because building a nested `{Device: {Action: bool}}` map needs one
(`shared.Security.permissions(...)`).

### 3. Expression Transform

```js
// Header root/PermBadge props.style.classes: property binding on session.custom.ReadOnly, expression transform
if({value}, 'perm-badge perm-badge-read header-icon', 'perm-badge perm-badge-write header-icon')
```

### 4. Script Transform (When It Is Justified)

The nav Tree filters its items with a script transform, because it walks and rebuilds a nested list (see
[Navigation](./navigation.md#how-the-tree-is-filtered)). Change scripts (`onChange`) are used for one-shot actions,
for example the Header route guard's `system.perspective.navigate`.

## Integration Toolkit Functions

The project rules call these "the Integration Toolkit expressions". Most of them are core Ignition expression functions;
the **Integration Toolkit** module (Automation Professionals, `Integration Toolkit-2.1.5...-v83.modl` on the
Standard gateway) adds the iteration functions (`forEach()`, `it()` ...) and more. Both sets are available in every
BH expression:

| Function | Use |
|---|---|
| `tag(path)` | Read a tag whose path is built in the expression (an "indirect" read inside an expression). |
| `try(expr, fallback)` | Return `fallback` when `expr` errors (missing tag, bad cast). |
| `coalesce(a, b, ...)` | First non-null argument. |
| `isGood(x)`, `isBad(x)`, `isBadOrError(x)` | Test the quality of a qualified value. Test with **`isGood()`**: `isBad()` lets `Uncertain_LastKnownValue` through, which is what a dropped PLC link produces. |
| `qualityOf(x)` | The quality code as text (`Good`, `Bad_NotFound` ...). |
| `lookup(dataset, key, default, keyColumn, valueColumn)` | Look a value up in a DataSet (enum words, matrix rows). |
| `it()` | The current element inside iteration functions such as `forEach()`. |

`lookup()` is how coded members become words. The enum DataSets live in `[default]_Config/Enums/<Group>/<Name>`:

```js
// AhuEvapPanel CurrentMode label
if({view.params.tagPath} != '' && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), '—',
  if({view.params.tagPath} = '', '',
    try('Current Mode: ' + lookup({[default]_Config/Enums/Evaporator/DefrostStartMode},
        toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')),
        toStr(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode'))), 'value', 'label'), '')))
```

## Null-Safety

Two Ignition behaviours cause most binding error overlays (the red box with `null` text):

- **A comparison with null is null.** `{view.custom.x} = 'literal'` is null when `x` is null, not false.
- **`if(null, a, b)` is an error**, which puts the whole binding in an error state.

So wrap every comparison input in `coalesce()` (and every tag read in `try()`):

```js
// wrong: null x makes the if() fail
if({view.custom.pax} = 'Motor', '/Motor/Sts_Running', '/Sts_Running/Value')
// right
if(coalesce({view.custom.pax}, '') = 'Motor', '/Motor/Sts_Running', '/Sts_Running/Value')
```

A real example that guards the path, the quality and the cast:

```js
// Pump custom.oos: true when the device's UDT instance is disabled
if(coalesce({view.params.tagPath}, '') = '', false,
   !coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
```

## Value Quality

Shared value elements never show `null` or a stale number for a bad tag: they show a gray italic em dash (style
class `value-bad`). The "OK to show" test is an expression:

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath})), false), false)
  && !isNull(try(tag({view.params.tagPath}), null))
  && coalesce(try(abs(toFloat(tag({view.params.tagPath}))) < 1e30, true), true)
```

The last term treats PlantPAx's "no limit" (+/-1.5e38) as no value. See
[Faceplates](./faceplates.md#value-quality-gray-italic-dash).

**Quality rule (2026-10-24).** Rule: every tag binding is quality-gated, so nothing shows a stale value when the PLC
link is down.

- A device with data that is not Good shows a red **COMM LOSS** (symbol `device-comm-loss`, label, state text); a bad
  value shows the gray dash; a chart or table with no data says "No Data". The comm-loss test is `!isGood()` on the
  device's key status member (for example `Motor/Val_Sts`), not on the expression members, which stay Good while their
  inputs are stale.
- Perspective draws a black quality overlay on a component when any `props.*` binding is Bad, Uncertain or Pending. Set
  `overlayOptOut` on a `props.*` binding (Designer: the binding's **Overlay Opt-Out** checkbox) only **after** the
  expression is gated; the project's gated bindings already have it set.
- A tag-derived value inside a `view.params` path turns every binding of the embedded view Uncertain, so don't build a
  path param from a tag value.
- Details: [Comm Loss And Value Quality](../features/comm-loss-quality.md).

## Keep `params.tagPath` Empty

A component's `tagPath` param default must be `''`, never a Designer placeholder such as
`[default]Evaporators/EV-01`. A placeholder path makes the component subscribe to a missing tag in every embed that
forgets to set it, and it hides wiring mistakes. Guard every path expression with `{view.params.tagPath} = ''`, as
in the examples above. (Two old elements, `StatusIndicator` and `DeviceLabelAlarmIndicator`, still have placeholder
defaults; every embed overrides them.)

## Expressions Must Be LF-Only

The repo has `core.autocrlf=true`, so a careless Windows edit of a project file can turn the newlines inside a JSON
string into `\r\n`. Perspective expressions with `\r` in them fail to parse in some places. The Designer always writes
`\n`, so edit expressions in the Designer, not in a text editor.

## Indirect Tag Paths From The UDT Instance

Components get the **instance path** (`tagPath`) and build member paths from it. Two ways:

**Expression with `tag()`** (most views):

```js
// Pump custom.values.running
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/Motor/Val_Sts')),
   false,
   tag({view.params.tagPath} + '/Motor/Val_Sts') = 2 || tag({view.params.tagPath} + '/Motor/Val_Sts') = 8)
```

**Indirect tag binding** (tag binding in indirect mode, with references):

```text
// Pump custom.alarm.active
mode: indirect    tagPath: {tagPath}/_Alarms/_Active    references: tagPath = {view.params.tagPath}
fallback delay: 2.5 s, then an expression transform
```

Use a tag binding when you need the tag's own quality and overlays, or bidirectional writes; use `tag()` when the
path depends on several conditions.

Page-level views build paths from their own param in the same way:
`{view.params.tagPath} + "/Tanks/HTR"` on the Machine Room page.

## PAX Member Paths

**PAX** = Rockwell **PlantPAx**, the PLC object library the RCP1 program uses (P_Motor, P_ValveSO, P_AIn, P_DIn,
P_Intlk, P_RunTime ...). Since the October 2026 mapping, each device UDT (`Devices/<Type>`) has **nested parts**
that read the live controller objects (read only), for example a pump's `Motor` (P_Motor), `Intlk` (P_Intlk) and
`RunTime` (P_RunTime). The older flat members (`<Member>/Value`) stay behind for unmapped devices.

Views find out which world a device is in from **`custom.pax`**, the device's part key:

```js
// custom.pax (Common pattern 6): the UDT type picks the key; sensors / discrete inputs check which part is enabled
if(coalesce({view.params.tagPath}, '') = '', '',
  case(toStr(coalesce(try(tag({view.params.tagPath} + '.TypeId'), ''), '')),
    'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp',
    'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay',
    'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq',
    'Devices/Sensor', if(<AIn enabled>, 'AIn', if(<AInRef enabled>, 'AInRef', '')),
    'Devices/DiscreteInput', if(<DIn enabled>, 'DIn', ''), ''))
```

Then reads pick the PAX member or the old flat one:

```js
if(coalesce({view.custom.pax}, '') = 'Motor', '/Motor/Sts_Running', '/Sts_Running/Value')
```

Once every device of a type is mapped, these switches are replaced by the PAX path only (the Pump above already
reads `'/Motor/Val_Sts'` directly). Scripts use the same map:
`shared.Pax.part(device)`, `shared.Pax.resolve(base, leaf, pax)` (old leaf to PAX member),
`shared.Pax.livePath(path)` (for history and Fill From Live Values) and `shared.Pax.mapRows(rows)` (Details
tables). The map itself is `shared.Pax.FIELDS` (Project Library > `shared` > `Pax`); to map a new field, add its entry there
and test a faceplate.

`custom.pax` also locks commands: a non-empty key means "live PLC object", and command scripts return early (see
[Faceplates](./faceplates.md#write-paths-and-the-plc-write-lock)). The per-device mapping tables are in
`docs/pax-mapping/*.md` and on [Tags](../tags/index.md).

## Binding Checklist

- Start with an expression; reach for a script only with a reason.
- `coalesce()` every comparison input, `try()` every `tag()` read, guard empty paths.
- Gate controls on `session.custom.Permissions.<Device>.<Action>`, not on role names
  ([Security In The UI](./security-ui.md)).
- Title Case for every user-facing string in a binding (`'Out Of Service'`, not `'Out of service'`).
- Save, then test in a Perspective session: no red error overlays, charts render with empty data, light and dark
  themes.
