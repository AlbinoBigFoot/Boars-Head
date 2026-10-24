---
title: "Session Properties"
sidebar_label: "Session Properties"
description: "BH session props and session custom properties, with their bindings."
generated: true
sidebar_position: 5
---

:::note

:::


Source: `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json` (Designer: Project Browser > Perspective > Session Properties). Session custom properties are read in views as `{session.custom.<name>}`.

Session permissions (`session-permissions/data.bin`): `AllOf`, levels `Authenticated`. A session needs a login before it opens.

## Session Props

| Prop | Value |
|---|---|
| `address` | `"x.x.x.x"` |
| `animations` | `true` |
| `appBar` | `{"togglePosition": "hidden"}` |
| `device` | `{}` |
| `geolocation` | `{}` |
| `locale` | `"en-US"` |
| `offline` | `{}` |
| `theme` | `"light-cool"` |
| `timeZoneId` | `"America/New_York"` |

## Session Custom Properties

### AdhocTrend

Access `default`. Default `{"aggregate": "Average", "chartType": "line", "colors": ["#008FFB", "#34C759", "#FFA726", "#FF4560", "#775DD0", "#1C4...`.

[00\_Pages/00\_Docked/Header](./views/00-pages/00-docked/header.md), [01\_Popups/00\_Faceplates/Alerts/ContextMenu](./views/01-popups/00-faceplates/alerts/contextmenu.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/LoadDeleteTrend](./views/98-configuration/adhoctrend/assets/loaddeletetrend.md), [98\_Configuration/AdhocTrend/\_Assets/NamePlot](./views/98-configuration/adhoctrend/assets/nameplot.md), [98\_Configuration/AdhocTrend/\_Assets/Pen](./views/98-configuration/adhoctrend/assets/pen.md), [98\_Configuration/AdhocTrend/\_Assets/PenPlot](./views/98-configuration/adhoctrend/assets/penplot.md), [98\_Configuration/AdhocTrend/\_Assets/Plot](./views/98-configuration/adhoctrend/assets/plot.md), [98\_Configuration/AdhocTrend/\_Assets/RemovePlot](./views/98-configuration/adhoctrend/assets/removeplot.md), [98\_Configuration/AdhocTrend/\_Assets/SaveTrendConfig](./views/98-configuration/adhoctrend/assets/savetrendconfig.md), [98\_Configuration/AdhocTrend/\_Assets/ToolBar](./views/98-configuration/adhoctrend/assets/toolbar.md)

### ReadOnly

Access `PROTECTED`. Default `true`.

Binding `custom.ReadOnly`: expression

```js
!coalesce({session.custom.Permissions.Faceplates.Operate}, false)
```


<details>
<summary>Read by 32 views</summary>

[00\_Pages/00\_Docked/Header](./views/00-pages/00-docked/header.md), [00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./views/00-pages/00-docked/assets/userrolesandlogin.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./views/01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigurationRow](./views/01-popups/00-faceplates/assets/configuration/configurationrow.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockRow](./views/01-popups/00-faceplates/assets/interlockrow.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./views/01-popups/00-faceplates/assets/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_Position](./views/01-popups/00-faceplates/assets/valve/cmd-position.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/02\_Widgets/Safetys](./views/02-components/02-widgets/safetys.md), [03\_Elements/00\_Control/AnalogInput](./views/03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/MultiStateInput](./views/03-elements/00-control/multistateinput.md), [03\_Elements/00\_Control/StringInput](./views/03-elements/00-control/stringinput.md), [03\_Elements/00\_Control/TimeInput](./views/03-elements/00-control/timeinput.md), [03\_Elements/00\_Control/\_Assets/Numeric](./views/03-elements/00-control/assets/numeric.md)

</details>

### CanOpenFaceplates

Access `PROTECTED`. Default `false`.

Binding `custom.CanOpenFaceplates`: expression

```js
coalesce({session.custom.Permissions.Faceplates.Open}, false)
```


[00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewStatusTile](./views/00-pages/groveport/utility/overviewstatustile.md), [02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](./views/02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](./views/02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](./views/02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](./views/02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Pump](./views/02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](./views/02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](./views/02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md)

### EngineeringView

Access `PROTECTED`. Default `false`.

Binding `custom.EngineeringView`: expression

```js
coalesce({session.custom.Permissions.Engineering.View}, false)
```


[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md)

### EngineeringReadOnly

Access `PROTECTED`. Default `true`.

Binding `custom.EngineeringReadOnly`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce({session.custom.Permissions.Engineering.Edit}, false)
```


[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./views/01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md)

### AlarmConfigReadOnly

Access `PROTECTED`. Default `true`.

Binding `custom.AlarmConfigReadOnly`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce({session.custom.Permissions.AlarmConfiguration.Edit}, false)
```


[01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./views/01-popups/00-faceplates/assets/alarmconfigurationrow.md)

### trend

Access `default`. Default `{"count": 0, "key": "||", "pens": []}`.

Binding `custom.trend`: property `session.custom.AdhocTrend`, then script transform

Transform 1, script:

```python
# read-only basket summary for the header badge / menus (docs/trending.md)
return shared.TrendContext.summary(value)
```


[01\_Popups/TrendContext/QuickHistory](./views/01-popups/trendcontext/quickhistory.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/Plot](./views/98-configuration/adhoctrend/assets/plot.md)

### trendTools

Access `default`. Default `{"autoScaleY": false, "dragMode": "time", "zoomHoldMax": null, "zoomHoldMin": null, "zoomKind": null, "zoomMax": null...`.

[98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/Plot](./views/98-configuration/adhoctrend/assets/plot.md)

### TicketLogSettings

Access `PROTECTED`. Default `false`.

Binding `custom.TicketLogSettings`: expression

```js
coalesce({session.custom.Permissions.TicketLogger.Settings}, false)
```


[98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md)

### Administrator

Access `PROTECTED`.

Binding `custom.Administrator`: structured expression (expr-struct), then script transform

```js
list: tag('[default]_Config/Security/AdminRoles')
roles: {session.props.auth.user.roles}
```

waitOnAll: `False`

Transform 1, script:

```python
return shared.Security.hasAnyRole(value.roles, value.list)
```


[00\_Pages/00\_Docked/Navigation](./views/00-pages/00-docked/navigation.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md)

### IntegrationAccess

Access `PROTECTED`.

Binding `custom.IntegrationAccess`: expression

```js
coalesce({session.custom.Permissions.TicketLogger.Settings}, false)
```


[98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/Integrations](./views/98-configuration/integrations.md)

### Permissions

Access `PROTECTED`.

Binding `custom.Permissions`: structured expression (expr-struct), then script transform

```js
matrix: tag('[default]_Config/RolesPermissions')
roles: {session.props.auth.user.roles}
full: tag('[default]_Config/Security/FullPermissionRoles')
inherits: tag('[default]_Config/Security/RoleInherits')
restricted: tag('[default]_Config/Security/RestrictedRows')
defaults: tag('[default]_Config/Security/NewRoleDefaults')
```

waitOnAll: `False`

Transform 1, script:

```python
# {Device: {Action: bool}} for the logged-in user from [default]_Config/RolesPermissions (one column per
# role, union over the user's roles + _Config/Security/RoleInherits; FullPermissionRoles hold every
# action). Struct so it re-evaluates on login / role change as well as on matrix edits.
# RestrictedRows (Ticket Logger) are not implied by FullPermissionRoles (device-perms 2026-10-24).
# A role without a matrix column yet holds _Config/Security/NewRoleDefaults (role-wizard 2026-10-24).
return shared.Security.permissions(value.roles, value.matrix, value.full, value.inherits,
    value.restricted, value.defaults)
```


<details>
<summary>Read by 57 views</summary>

[00\_Pages/00\_Docked/Header](./views/00-pages/00-docked/header.md), [00\_Pages/00\_Docked/Navigation](./views/00-pages/00-docked/navigation.md), [00\_Pages/00\_Docked/\_Assets/OosNotification](./views/00-pages/00-docked/assets/oosnotification.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Alarms/\_Assets/AlarmStatusTable](./views/00-pages/boars-head/alarms/assets/alarmstatustable.md), [00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_RPProbe](./views/00-pages/boars-head/operations/rpprobe.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./views/01-popups/00-faceplates/assets/alarmconfigurationrow.md), [01\_Popups/00\_Faceplates/\_Assets/Alarms](./views/01-popups/00-faceplates/assets/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./views/01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigurationRow](./views/01-popups/00-faceplates/assets/configuration/configurationrow.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockRow](./views/01-popups/00-faceplates/assets/interlockrow.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./views/01-popups/00-faceplates/assets/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_Position](./views/01-popups/00-faceplates/assets/valve/cmd-position.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md), [02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/01\_Devices/CoolingTower](./views/02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](./views/02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](./views/02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/01\_Devices/Pump](./views/02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](./views/02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](./views/02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [02\_Components/02\_Widgets/Safetys](./views/02-components/02-widgets/safetys.md), [98\_Configuration/AdhocTrend/\_Assets/LoadDeleteTrend](./views/98-configuration/adhoctrend/assets/loaddeletetrend.md)

</details>

### TicketLogAccess

Access `PROTECTED`.

Binding `custom.TicketLogAccess`: expression

```js
coalesce({session.custom.Permissions.TicketLogger.Use}, false)
```


<details>
<summary>Read by 250 views</summary>

[00\_Pages/00\_Docked/Header](./views/00-pages/00-docked/header.md), [00\_Pages/00\_Docked/Legend](./views/00-pages/00-docked/legend.md), [00\_Pages/00\_Docked/Navigation](./views/00-pages/00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](./views/00-pages/00-docked/tempnav.md), [00\_Pages/00\_Docked/\_Assets/AlarmNotification](./views/00-pages/00-docked/assets/alarmnotification.md), [00\_Pages/00\_Docked/\_Assets/BrandLogo](./views/00-pages/00-docked/assets/brandlogo.md), [00\_Pages/00\_Docked/\_Assets/ChangeTheme](./views/00-pages/00-docked/assets/changetheme.md), [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./views/00-pages/00-docked/assets/integratorcontact.md), [00\_Pages/00\_Docked/\_Assets/IntegratorLogo](./views/00-pages/00-docked/assets/integratorlogo.md), [00\_Pages/00\_Docked/\_Assets/OosNotification](./views/00-pages/00-docked/assets/oosnotification.md), [00\_Pages/00\_Docked/\_Assets/User](./views/00-pages/00-docked/assets/user.md), [00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./views/00-pages/00-docked/assets/userrolesandlogin.md), [00\_Pages/00\_Docked/\_Assets/UserSettings](./views/00-pages/00-docked/assets/usersettings.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Alarms/\_Assets/AlarmJournalTable](./views/00-pages/boars-head/alarms/assets/alarmjournaltable.md), [00\_Pages/Boars Head/Alarms/\_Assets/AlarmStatusTable](./views/00-pages/boars-head/alarms/assets/alarmstatustable.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/DesignOverview](./views/00-pages/boars-head/devices/designoverview.md), [00\_Pages/Boars Head/Devices/DetailsOverview](./views/00-pages/boars-head/devices/detailsoverview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/Devices/TypeTable](./views/00-pages/boars-head/devices/typetable.md), [00\_Pages/Boars Head/ExhaustFans/Design](./views/00-pages/boars-head/exhaustfans/design.md), [00\_Pages/Boars Head/ExhaustFans/Details](./views/00-pages/boars-head/exhaustfans/details.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/LandingPage/Globe](./views/00-pages/boars-head/landingpage/globe.md), [00\_Pages/Boars Head/LandingPage/PlantPlaceholder](./views/00-pages/boars-head/landingpage/plantplaceholder.md), [00\_Pages/Boars Head/Machine Room/Overview](./views/00-pages/boars-head/machine-room/overview.md), [00\_Pages/Boars Head/NoViewPath](./views/00-pages/boars-head/noviewpath.md), [00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Pumps/Design](./views/00-pages/boars-head/pumps/design.md), [00\_Pages/Boars Head/Pumps/Details](./views/00-pages/boars-head/pumps/details.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Design](./views/00-pages/boars-head/sensors/design.md), [00\_Pages/Boars Head/Sensors/Details](./views/00-pages/boars-head/sensors/details.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Design](./views/00-pages/boars-head/tanks/design.md), [00\_Pages/Boars Head/Tanks/Details](./views/00-pages/boars-head/tanks/details.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Unit/Overview](./views/00-pages/boars-head/unit/overview.md), [00\_Pages/Boars Head/Valves/Design](./views/00-pages/boars-head/valves/design.md), [00\_Pages/Boars Head/Valves/Details](./views/00-pages/boars-head/valves/details.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Area/DomainKpis](./views/00-pages/groveport/area/domainkpis.md), [00\_Pages/Groveport/Club/Utility/CG-C1](./views/00-pages/groveport/club/utility/cg-c1.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Design](./views/00-pages/groveport/condensers/utility/condenserfans/design.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Design](./views/00-pages/groveport/condensers/utility/pumps/design.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Design](./views/00-pages/groveport/condensers/utility/sensors/design.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Design](./views/00-pages/groveport/condensers/utility/tanks/design.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Design](./views/00-pages/groveport/condensers/utility/valves/design.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Dock/Utility/CG-G1](./views/00-pages/groveport/dock/utility/cg-g1.md), [00\_Pages/Groveport/Dock/Utility/CG-G2](./views/00-pages/groveport/dock/utility/cg-g2.md), [00\_Pages/Groveport/Dock/Utility/CG-G3](./views/00-pages/groveport/dock/utility/cg-g3.md), [00\_Pages/Groveport/Dock/Utility/CG-G4](./views/00-pages/groveport/dock/utility/cg-g4.md), [00\_Pages/Groveport/Dock/Utility/CG-G5](./views/00-pages/groveport/dock/utility/cg-g5.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/East PH/Utility/CG-E1](./views/00-pages/groveport/east-ph/utility/cg-e1.md), [00\_Pages/Groveport/East PH/Utility/CG-E2](./views/00-pages/groveport/east-ph/utility/cg-e2.md), [00\_Pages/Groveport/East PH/Utility/CG-E3](./views/00-pages/groveport/east-ph/utility/cg-e3.md), [00\_Pages/Groveport/East PH/Utility/CG-E4](./views/00-pages/groveport/east-ph/utility/cg-e4.md), [00\_Pages/Groveport/Freezer/Utility/CG-A1](./views/00-pages/groveport/freezer/utility/cg-a1.md), [00\_Pages/Groveport/Freezer/Utility/CG-A2](./views/00-pages/groveport/freezer/utility/cg-a2.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Design](./views/00-pages/groveport/machine-room/utility/compressors/design.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Details](./views/00-pages/groveport/machine-room/utility/compressors/details.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](./views/00-pages/groveport/machine-room/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](./views/00-pages/groveport/machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/Forms/\_Assets/HistoryActions](./views/00-pages/groveport/operations/forms/assets/historyactions.md), [00\_Pages/Groveport/Palletizing/Utility/CG-D1](./views/00-pages/groveport/palletizing/utility/cg-d1.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/SuperChill/Utility/CG-B1](./views/00-pages/groveport/superchill/utility/cg-b1.md), [00\_Pages/Groveport/SuperChill/Utility/CG-B2](./views/00-pages/groveport/superchill/utility/cg-b2.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewKpis](./views/00-pages/groveport/utility/overviewkpis.md), [00\_Pages/Groveport/Utility/OverviewStatusTile](./views/00-pages/groveport/utility/overviewstatustile.md), [00\_Pages/Groveport/Utility/OverviewStatuses](./views/00-pages/groveport/utility/overviewstatuses.md), [00\_Pages/Groveport/West PH/Utility/CG-F1](./views/00-pages/groveport/west-ph/utility/cg-f1.md), [00\_Pages/Groveport/West PH/Utility/CG-F2](./views/00-pages/groveport/west-ph/utility/cg-f2.md), [00\_Pages/Groveport/West PH/Utility/CG-F3](./views/00-pages/groveport/west-ph/utility/cg-f3.md), [00\_Pages/Groveport/West PH/Utility/CG-F4](./views/00-pages/groveport/west-ph/utility/cg-f4.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./views/00-pages/groveport/shared/cg/ahuevapdisplay.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapHistory](./views/00-pages/groveport/shared/cg/ahuevaphistory.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapStatusBar](./views/00-pages/groveport/shared/cg/ahuevapstatusbar.md), [01\_Popups/00\_Faceplates/AdhocTrend](./views/01-popups/00-faceplates/adhoctrend.md), [01\_Popups/00\_Faceplates/AdhocTrendConfig](./views/01-popups/00-faceplates/adhoctrendconfig.md), [01\_Popups/00\_Faceplates/Alerts/Alert](./views/01-popups/00-faceplates/alerts/alert.md), [01\_Popups/00\_Faceplates/Alerts/ContextMenu](./views/01-popups/00-faceplates/alerts/contextmenu.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [01\_Popups/00\_Faceplates/Compressor](./views/01-popups/00-faceplates/compressor.md), [01\_Popups/00\_Faceplates/CoolingTower](./views/01-popups/00-faceplates/coolingtower.md), [01\_Popups/00\_Faceplates/DischargeSequence](./views/01-popups/00-faceplates/dischargesequence.md), [01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/Evaporator](./views/01-popups/00-faceplates/evaporator.md), [01\_Popups/00\_Faceplates/ExhaustFan](./views/01-popups/00-faceplates/exhaustfan.md), [01\_Popups/00\_Faceplates/Faceplate](./views/01-popups/00-faceplates/faceplate.md), [01\_Popups/00\_Faceplates/Interlock](./views/01-popups/00-faceplates/interlock.md), [01\_Popups/00\_Faceplates/Pump](./views/01-popups/00-faceplates/pump.md), [01\_Popups/00\_Faceplates/Sensor](./views/01-popups/00-faceplates/sensor.md), [01\_Popups/00\_Faceplates/SolenoidValve](./views/01-popups/00-faceplates/solenoidvalve.md), [01\_Popups/00\_Faceplates/SolenoidValve3Way](./views/01-popups/00-faceplates/solenoidvalve3way.md), [01\_Popups/00\_Faceplates/SuctionSequence](./views/01-popups/00-faceplates/suctionsequence.md), [01\_Popups/00\_Faceplates/Tank](./views/01-popups/00-faceplates/tank.md), [01\_Popups/00\_Faceplates/TankOverview](./views/01-popups/00-faceplates/tankoverview.md), [01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./views/01-popups/00-faceplates/assets/alarmconfiguration.md), [01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./views/01-popups/00-faceplates/assets/alarmconfigurationrow.md), [01\_Popups/00\_Faceplates/\_Assets/Alarms](./views/01-popups/00-faceplates/assets/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Configuration](./views/01-popups/00-faceplates/assets/compressor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Interlocks](./views/01-popups/00-faceplates/assets/compressor/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./views/01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](./views/01-popups/00-faceplates/assets/configuration/configsection.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/Configuration](./views/01-popups/00-faceplates/assets/configuration/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigurationRow](./views/01-popups/00-faceplates/assets/configuration/configurationrow.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](./views/01-popups/00-faceplates/assets/dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Configuration](./views/01-popups/00-faceplates/assets/evaporator/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Interlocks](./views/01-popups/00-faceplates/assets/evaporator/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./views/01-popups/00-faceplates/assets/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Interlocks](./views/01-popups/00-faceplates/assets/pump/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./views/01-popups/00-faceplates/assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Interlocks](./views/01-popups/00-faceplates/assets/tankoverview/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [01\_Popups/00\_Faceplates/\_Assets/Trend](./views/01-popups/00-faceplates/assets/trend.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_Position](./views/01-popups/00-faceplates/assets/valve/cmd-position.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [02\_Components/00\_Controls/InterlockButton](./views/02-components/00-controls/interlockbutton.md), [02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](./views/02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](./views/02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](./views/02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](./views/02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/01\_Devices/Pump](./views/02-components/01-devices/pump.md), [02\_Components/01\_Devices/SafetyRelay](./views/02-components/01-devices/safetyrelay.md), [02\_Components/01\_Devices/Sensor](./views/02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](./views/02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [02\_Components/01\_Devices/VesselGeneric](./views/02-components/01-devices/vesselgeneric.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md), [02\_Components/02\_Widgets/MetricCard](./views/02-components/02-widgets/metriccard.md), [02\_Components/02\_Widgets/Safetys](./views/02-components/02-widgets/safetys.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md), [02\_Components/03\_PLC/Controller\_CompactLogix\_5370](./views/02-components/03-plc/controller-compactlogix-5370.md), [02\_Components/03\_PLC/Module\_1769\_IA16](./views/02-components/03-plc/module-1769-ia16.md), [02\_Components/03\_PLC/Module\_1769\_IF8](./views/02-components/03-plc/module-1769-if8.md), [02\_Components/03\_PLC/Module\_1769\_IQ16](./views/02-components/03-plc/module-1769-iq16.md), [02\_Components/03\_PLC/Module\_1769\_OA16](./views/02-components/03-plc/module-1769-oa16.md), [02\_Components/03\_PLC/Module\_1769\_OW16](./views/02-components/03-plc/module-1769-ow16.md), [03\_Elements/00\_Control/AnalogInput](./views/03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/AnalogValue](./views/03-elements/00-control/analogvalue.md), [03\_Elements/00\_Control/MultiStateInput](./views/03-elements/00-control/multistateinput.md), [03\_Elements/00\_Control/StringInput](./views/03-elements/00-control/stringinput.md), [03\_Elements/00\_Control/TimeInput](./views/03-elements/00-control/timeinput.md), [03\_Elements/00\_Control/\_Assets/Numeric](./views/03-elements/00-control/assets/numeric.md), [03\_Elements/01\_Status/AlarmHeader](./views/03-elements/01-status/alarmheader.md), [03\_Elements/01\_Status/IconHeader](./views/03-elements/01-status/iconheader.md), [03\_Elements/01\_Status/Icons/Auto](./views/03-elements/01-status/icons/auto.md), [03\_Elements/01\_Status/Icons/DoorStatus](./views/03-elements/01-status/icons/doorstatus.md), [03\_Elements/01\_Status/Icons/Exclude](./views/03-elements/01-status/icons/exclude.md), [03\_Elements/01\_Status/Icons/Faceplate](./views/03-elements/01-status/icons/faceplate.md), [03\_Elements/01\_Status/Icons/Hand](./views/03-elements/01-status/icons/hand.md), [03\_Elements/01\_Status/Icons/Interlock](./views/03-elements/01-status/icons/interlock.md), [03\_Elements/01\_Status/Icons/Maintenance](./views/03-elements/01-status/icons/maintenance.md), [03\_Elements/01\_Status/Icons/NoMode](./views/03-elements/01-status/icons/nomode.md), [03\_Elements/01\_Status/Icons/NotAtSetpoint](./views/03-elements/01-status/icons/notatsetpoint.md), [03\_Elements/01\_Status/Icons/Operator](./views/03-elements/01-status/icons/operator.md), [03\_Elements/01\_Status/Icons/OutOfService](./views/03-elements/01-status/icons/outofservice.md), [03\_Elements/01\_Status/Icons/Override](./views/03-elements/01-status/icons/override.md), [03\_Elements/01\_Status/Icons/Program](./views/03-elements/01-status/icons/program.md), [03\_Elements/01\_Status/Icons/Remote](./views/03-elements/01-status/icons/remote.md), [03\_Elements/01\_Status/Icons/Simulate](./views/03-elements/01-status/icons/simulate.md), [03\_Elements/01\_Status/Icons/Stale](./views/03-elements/01-status/icons/stale.md), [03\_Elements/01\_Status/NotificationIcons/Blank](./views/03-elements/01-status/notificationicons/blank.md), [03\_Elements/01\_Status/NotificationIcons/CommLoss](./views/03-elements/01-status/notificationicons/commloss.md), [03\_Elements/01\_Status/StatusDot](./views/03-elements/01-status/statusdot.md), [03\_Elements/01\_Status/StatusIndicator](./views/03-elements/01-status/statusindicator.md), [03\_Elements/03\_Table/DeviceLabelAlarmIndicator](./views/03-elements/03-table/devicelabelalarmindicator.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/UserSavedTrendConfig](./views/98-configuration/adhoctrend/usersavedtrendconfig.md), [98\_Configuration/AdhocTrend/\_Assets/LoadDeleteTrend](./views/98-configuration/adhoctrend/assets/loaddeletetrend.md), [98\_Configuration/AdhocTrend/\_Assets/NamePlot](./views/98-configuration/adhoctrend/assets/nameplot.md), [98\_Configuration/AdhocTrend/\_Assets/Pen](./views/98-configuration/adhoctrend/assets/pen.md), [98\_Configuration/AdhocTrend/\_Assets/PenColor](./views/98-configuration/adhoctrend/assets/pencolor.md), [98\_Configuration/AdhocTrend/\_Assets/PenDelete](./views/98-configuration/adhoctrend/assets/pendelete.md), [98\_Configuration/AdhocTrend/\_Assets/PenEnable](./views/98-configuration/adhoctrend/assets/penenable.md), [98\_Configuration/AdhocTrend/\_Assets/PenPlot](./views/98-configuration/adhoctrend/assets/penplot.md), [98\_Configuration/AdhocTrend/\_Assets/Plot](./views/98-configuration/adhoctrend/assets/plot.md), [98\_Configuration/AdhocTrend/\_Assets/RemovePlot](./views/98-configuration/adhoctrend/assets/removeplot.md), [98\_Configuration/AdhocTrend/\_Assets/SaveTrendConfig](./views/98-configuration/adhoctrend/assets/savetrendconfig.md), [98\_Configuration/AdhocTrend/\_Assets/ToolBar](./views/98-configuration/adhoctrend/assets/toolbar.md), [98\_Configuration/ComponentPreview/Condenser-SafetyRelay](./views/98-configuration/componentpreview/condenser-safetyrelay.md), [98\_Configuration/ComponentPreview/VesselGeneric](./views/98-configuration/componentpreview/vesselgeneric.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md), [98\_Configuration/Tools/L5K/Message](./views/98-configuration/tools/l5k/message.md), [98\_Configuration/Tools/L5K/Parser](./views/98-configuration/tools/l5k/parser.md), [98\_Configuration/Tools/L5K/Tags](./views/98-configuration/tools/l5k/tags.md)

</details>

## System Prop Access

| Prop | Access | Persistent |
|---|---|---|
| `props.auth` | `PRIVATE` | False |
| `props.device.accelerometer` | `SYSTEM` | False |
| `props.device.identifier` | `SYSTEM` | False |
| `props.device.timezone` | `SYSTEM` | False |
| `props.device.type` | `SYSTEM` | False |
| `props.device.userAgent` | `SYSTEM` | False |
| `props.gateway` | `SYSTEM` | False |
| `props.geolocation.data` | `SYSTEM` | False |
| `props.geolocation.permissionGranted` | `SYSTEM` | False |
| `props.host` | `SYSTEM` | False |
| `props.id` | `SYSTEM` | False |
| `props.lastActivity` | `SYSTEM` | False |
| `props.offline.capable` | `SYSTEM` | False |
| `props.offline.enabled` | `SYSTEM` | False |
| `props.offline.lastSynced` | `SYSTEM` | False |
