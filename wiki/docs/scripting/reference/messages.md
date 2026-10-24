---
title: "Perspective Messages Reference"
sidebar_label: "Perspective Messages"
sidebar_position: 4
description: "Every Perspective message type: who sends it and which views handle it."
generated: true
custom_edit_url: null
---

:::note

:::

A Perspective **message** is sent with `system.perspective.sendMessage(type, payload, scope)` (or a menu item / message action) and received by a **message handler** on a view or component (Designer: select the component > **Configure Scripts > Message Handlers**). Scopes: `view`, `page`, `session`. Handlers listen on the scopes ticked below.

| Message type | Senders | Handlers |
|---|---|---|
| [`AdhocTrendConfigData`](#adhoctrendconfigdata) | 0 | 1 |
| [`AdhocTrendDeleteRow`](#adhoctrenddeleterow) | 1 | 1 |
| [`AdhocTrendDisableRow`](#adhoctrenddisablerow) | 1 | 1 |
| [`TrendDeleteCancel`](#trenddeletecancel) | 1 | 0 |
| [`TrendDeleteConfirm`](#trenddeleteconfirm) | 1 | 1 |
| [`UtilityOverviewHighlight`](#utilityoverviewhighlight) | 9 | 1 |
| [`cancel`](#cancel) | 2 | 8 |
| [`closeAlert`](#closealert) | 17 | 1 |
| [`commitTicketLog`](#committicketlog) | 1 | 1 |
| [`commitTrendConfig`](#committrendconfig) | 0 | 1 |
| [`faceplateSelectTab`](#faceplateselecttab) | 2 | 1 |
| [`globeHover`](#globehover) | 0 | 1 |
| [`globeNavigate`](#globenavigate) | 0 | 1 |
| [`integrationsToggle`](#integrationstoggle) | 1 | 1 |
| [`nrBulk`](#nrbulk) | 1 | 1 |
| [`nrCreateConfirmed`](#nrcreateconfirmed) | 1 | 1 |
| [`nrCreated`](#nrcreated) | 1 | 2 |
| [`nrExpand`](#nrexpand) | 2 | 1 |
| [`nrGroupToggle`](#nrgrouptoggle) | 1 | 1 |
| [`nrToggle`](#nrtoggle) | 1 | 1 |
| [`oosChanged`](#ooschanged) | 1 | 2 |
| [`oosHistory`](#ooshistory) | 9 | 9 |
| [`oosToggle`](#oostoggle) | 18 | 9 |
| [`opsFormsClearDailyRounds`](#opsformscleardailyrounds) | 1 | 1 |
| [`opsFormsClearShiftLog`](#opsformsclearshiftlog) | 1 | 1 |
| [`opsFormsPidComplete`](#opsformspidcomplete) | 1 | 1 |
| [`opsFormsSubmitDailyRounds`](#opsformssubmitdailyrounds) | 1 | 1 |
| [`opsFormsSubmitShiftLog`](#opsformssubmitshiftlog) | 1 | 1 |
| [`plcRackHover`](#plcrackhover) | 12 | 1 |
| [`plcRackSelect`](#plcrackselect) | 6 | 1 |
| [`redirectUrl`](#redirecturl) | 1 | 0 |
| [`rpBulk`](#rpbulk) | 1 | 1 |
| [`rpBulkApply`](#rpbulkapply) | 1 | 1 |
| [`rpDiscard`](#rpdiscard) | 1 | 1 |
| [`rpDiscardConfirmed`](#rpdiscardconfirmed) | 1 | 1 |
| [`rpExpandAll`](#rpexpandall) | 2 | 1 |
| [`rpGroupToggle`](#rpgrouptoggle) | 1 | 1 |
| [`rpRoleSelect`](#rproleselect) | 0 | 1 |
| [`rpSave`](#rpsave) | 1 | 1 |
| [`rpSaveConfirmed`](#rpsaveconfirmed) | 1 | 1 |
| [`rpToggle`](#rptoggle) | 1 | 1 |
| [`rptDeleteTemplate`](#rptdeletetemplate) | 1 | 1 |
| [`rptEdit`](#rptedit) | 13 | 1 |
| [`rptLoadSaved`](#rptloadsaved) | 1 | 1 |
| [`rptPageDelete`](#rptpagedelete) | 1 | 1 |
| [`rptSavedChanged`](#rptsavedchanged) | 6 | 1 |
| [`rptStart`](#rptstart) | 2 | 1 |
| [`ticketLog`](#ticketlog) | 250 | 250 |
| [`tlRoutingSave`](#tlroutingsave) | 1 | 1 |
| [`trendZoomReset`](#trendzoomreset) | 1 | 1 |
| [`umAdd`](#umadd) | 2 | 1 |
| [`umAdjAdd`](#umadjadd) | 1 | 1 |
| [`umAdjRemove`](#umadjremove) | 1 | 1 |
| [`umAdjSet`](#umadjset) | 4 | 1 |
| [`umContactAdd`](#umcontactadd) | 1 | 1 |
| [`umContactRemove`](#umcontactremove) | 1 | 1 |
| [`umContactSet`](#umcontactset) | 2 | 1 |
| [`umDelete`](#umdelete) | 1 | 1 |
| [`umDeleteConfirmed`](#umdeleteconfirmed) | 1 | 1 |
| [`umDiscard`](#umdiscard) | 1 | 1 |
| [`umDiscardConfirmed`](#umdiscardconfirmed) | 1 | 1 |
| [`umRoleAdd`](#umroleadd) | 0 | 1 |
| [`umRoleDelete`](#umroledelete) | 1 | 1 |
| [`umRoleDeleteConfirmed`](#umroledeleteconfirmed) | 1 | 1 |
| [`umRoleSave`](#umrolesave) | 1 | 1 |
| [`umRoleSaveConfirmed`](#umrolesaveconfirmed) | 1 | 1 |
| [`umRoleSelect`](#umroleselect) | 0 | 1 |
| [`umRoleToggle`](#umroletoggle) | 1 | 1 |
| [`umSave`](#umsave) | 1 | 1 |
| [`umSaveConfirmed`](#umsaveconfirmed) | 1 | 1 |
| [`umSelect`](#umselect) | 2 | 1 |
| [`writeValue`](#writevalue) | 2 | 8 |

## AdhocTrendConfigData {#adhoctrendconfigdata}

_No sender found by the scan (sent from a binding-built menu or a dynamic name)._

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | `root` | page |

## AdhocTrendDeleteRow {#adhoctrenddeleterow}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/AdhocTrend/_Assets/PenDelete` | `root/Button event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | `root` | page |

## AdhocTrendDisableRow {#adhoctrenddisablerow}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/AdhocTrend/_Assets/PenEnable` | `root/Icon event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | `root` | page |

## TrendDeleteCancel {#trenddeletecancel}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | `root/DeleteButton event component.onActionPerformed` | `Alert popup button (page)` |

_No handler in the project (a gateway message handler, or a leftover sender)._

## TrendDeleteConfirm {#trenddeleteconfirm}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | `root/DeleteButton event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/AdhocTrend/UserSavedTrendConfig` | `root` | page |

## UtilityOverviewHighlight {#utilityoverviewhighlight}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs binding props.currentTabIndex` | `default` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs/PanelOverview/TempCard/TempChart event component.dataPointSelectionHandler` | `default` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs/PanelOverview/DwellCard/DwellTabs/PanelDwellStatus/DwellChartMain event component.dataPointSelectionHandler` | `default` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs/PanelOverview/DwellCard/DwellTabs/PanelDwellDefrost/DwellChartDft event component.dataPointSelectionHandler` | `default` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs/PanelOverview/StatusCard/StatusChart event component.dataPointSelectionHandler` | `default` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs/PanelOverview/StatusCard/StatusChart event component.legendClickHandler` | `default` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs/PanelSections/SectionChartCard/SectionTempChart event component.dataPointSelectionHandler` | `default` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root/KpiTabs/PanelSections/SectionStatusCard/SectionStatusChart event component.dataPointSelectionHandler` | `default` |
| `view 03_Elements/03_Table/CgHit` | `root event dom.onClick` | `default` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Utility/Overview` | `root` | page |

## cancel {#cancel}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `script shared.Alerts.confirmApplyWrite` | | `Alert popup button (page)` |
| `view 03_Elements/00_Control/_Assets/Numeric` | `root/NumericEntryField binding props.value` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | `root` | page |
| `03_Elements/00_Control/AnalogInput` | `root` | page |
| `03_Elements/00_Control/MultiStateInput` | `root` | page |
| `03_Elements/00_Control/StringInput` | `root` | page |
| `03_Elements/00_Control/TimeInput` | `root` | page |
| `03_Elements/00_Control/_Assets/Numeric` | `root` | page |

## closeAlert {#closealert}

<details>
<summary>Senders (11)</summary>

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | `root/LoadButton event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/AdhocTrend/_Assets/NamePlot` | `root/Buttons/Confirm event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/AdhocTrend/_Assets/RemovePlot` | `root/Buttons/Confirm event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` | `root/Buttons/Save event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/AdhocTrend/Trend` | `root/TrendContainer/Trend/PlotToolbar/Buttons/RemovePlot event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/Integrations` | `root/AddRow/Add event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/IntegrationSection` | `root/Body/TokenRow/Replace event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/IntegrationSection` | `root/Body/Buttons/Test event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/IntegrationSection` | `root/Body/Buttons/Save event component.onActionPerformed` | `Alert popup button (page)` |
| `view 98_Configuration/TicketLogger` | `root/Buttons/SendButton event dom.onClick` | `Alert popup button (page)` |
| `view 98_Configuration/TicketLoggerSettings` | `root/Content/Destinations/DryRun/Head/Toggle event component.onActionPerformed` | `Alert popup button (page)` |
</details>

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | `root` | page |

## commitTicketLog {#committicketlog}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/TicketLogger` | `root/Buttons/SendButton event dom.onClick` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/TicketLogger` | `root` | page |

## commitTrendConfig {#committrendconfig}

_No sender found by the scan (sent from a binding-built menu or a dynamic name)._

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | `root` | page |

## faceplateSelectTab {#faceplateselecttab}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 01_Popups/00_Faceplates/_Assets/Pump/Controls` | `root/StatusSection/PiChips/Intlk event dom.onClick` | `page` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Controls` | `root/StatusSection/LsChips/Intlk event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `01_Popups/00_Faceplates/Faceplate` | `root` | page |

## globeHover {#globehover}

_No sender found by the scan (sent from a binding-built menu or a dynamic name)._

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/LandingPage/Globe` | `root` | page |

## globeNavigate {#globenavigate}

_No sender found by the scan (sent from a binding-built menu or a dynamic name)._

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/LandingPage/Globe` | `root` | page |

## integrationsToggle {#integrationstoggle}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/IntegrationSection` | `root/Header event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/Integrations` | `root` | page |

## nrBulk {#nrbulk}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/NRGroup` | `root/Header/Bulk event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | `root` | page |

## nrCreateConfirmed {#nrcreateconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/NewRole` | `root/ActionBar/Create event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | `root` | page |

## nrCreated {#nrcreated}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/NewRole` | `root message handler nrCreateConfirmed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## nrExpand {#nrexpand}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/NewRole` | `root/Step2/Toolbar/ExpandAll event component.onActionPerformed` | `page` |
| `view 00_Pages/Boars Head/Operations/_Admin/NewRole` | `root/Step2/Toolbar/CollapseAll event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | `root` | page |

## nrGroupToggle {#nrgrouptoggle}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/NRGroup` | `root/Header/HeadClick event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | `root` | page |

## nrToggle {#nrtoggle}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/NRRow` | `root event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | `root` | page |

## oosChanged {#ooschanged}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `script shared.OutOfService._notify` | | `session` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/00_Docked/_Assets/OosNotification` | `root` | session |
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | `root` | session |

## oosHistory {#ooshistory}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 02_Components/01_Devices/Compressor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/CoolingTower` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Evaporator` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/ExhaustFan` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/LTU` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Pump` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Sensor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/SolenoidValve` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Tank` | `root binding meta.contextMenu.items` | `menu item` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `02_Components/01_Devices/Compressor` | `root` | page |
| `02_Components/01_Devices/CoolingTower` | `root` | page |
| `02_Components/01_Devices/Evaporator` | `root` | page |
| `02_Components/01_Devices/ExhaustFan` | `root` | page |
| `02_Components/01_Devices/LTU` | `root` | page |
| `02_Components/01_Devices/Pump` | `root` | page |
| `02_Components/01_Devices/Sensor` | `root` | page |
| `02_Components/01_Devices/SolenoidValve` | `root` | page |
| `02_Components/01_Devices/Tank` | `root` | page |

## oosToggle {#oostoggle}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 02_Components/01_Devices/Compressor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/CoolingTower` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Evaporator` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/ExhaustFan` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/LTU` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Pump` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Sensor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/SolenoidValve` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Tank` | `root binding meta.contextMenu.items` | `menu item` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `02_Components/01_Devices/Compressor` | `root` | page |
| `02_Components/01_Devices/CoolingTower` | `root` | page |
| `02_Components/01_Devices/Evaporator` | `root` | page |
| `02_Components/01_Devices/ExhaustFan` | `root` | page |
| `02_Components/01_Devices/LTU` | `root` | page |
| `02_Components/01_Devices/Pump` | `root` | page |
| `02_Components/01_Devices/Sensor` | `root` | page |
| `02_Components/01_Devices/SolenoidValve` | `root` | page |
| `02_Components/01_Devices/Tank` | `root` | page |

## opsFormsClearDailyRounds {#opsformscleardailyrounds}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Groveport/Operations/Forms/DailyRounds` | `root/Footer/Bar/ActionBar/Clear event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | `root` | page |

## opsFormsClearShiftLog {#opsformsclearshiftlog}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Groveport/Operations/Forms/ShiftLog` | `root/Footer/Bar/ActionBar/Clear event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | `root` | page |

## opsFormsPidComplete {#opsformspidcomplete}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Groveport/Operations/Forms/PidVerification` | `root/Cycle/Row/Btns/Complete event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | `root` | page |

## opsFormsSubmitDailyRounds {#opsformssubmitdailyrounds}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Groveport/Operations/Forms/DailyRounds` | `root/Footer/Bar/ActionBar/Submit event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | `root` | page |

## opsFormsSubmitShiftLog {#opsformssubmitshiftlog}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Groveport/Operations/Forms/ShiftLog` | `root/Footer/Bar/ActionBar/Submit event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | `root` | page |

## plcRackHover {#plcrackhover}

<details>
<summary>Senders (12)</summary>

| Sender | Where | Scope |
|---|---|---|
| `view 02_Components/03_PLC/Controller_CompactLogix_5370` | `root event dom.onMouseEnter` | `page` |
| `view 02_Components/03_PLC/Controller_CompactLogix_5370` | `root event dom.onMouseLeave` | `page` |
| `view 02_Components/03_PLC/Module_1769_IA16` | `root event dom.onMouseEnter` | `page` |
| `view 02_Components/03_PLC/Module_1769_IA16` | `root event dom.onMouseLeave` | `page` |
| `view 02_Components/03_PLC/Module_1769_IF8` | `root event dom.onMouseEnter` | `page` |
| `view 02_Components/03_PLC/Module_1769_IF8` | `root event dom.onMouseLeave` | `page` |
| `view 02_Components/03_PLC/Module_1769_IQ16` | `root event dom.onMouseEnter` | `page` |
| `view 02_Components/03_PLC/Module_1769_IQ16` | `root event dom.onMouseLeave` | `page` |
| `view 02_Components/03_PLC/Module_1769_OA16` | `root event dom.onMouseEnter` | `page` |
| `view 02_Components/03_PLC/Module_1769_OA16` | `root event dom.onMouseLeave` | `page` |
| `view 02_Components/03_PLC/Module_1769_OW16` | `root event dom.onMouseEnter` | `page` |
| `view 02_Components/03_PLC/Module_1769_OW16` | `root event dom.onMouseLeave` | `page` |
</details>

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview` | `root` | page |

## plcRackSelect {#plcrackselect}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 02_Components/03_PLC/Controller_CompactLogix_5370` | `root event dom.onClick` | `page` |
| `view 02_Components/03_PLC/Module_1769_IA16` | `root event dom.onClick` | `page` |
| `view 02_Components/03_PLC/Module_1769_IF8` | `root event dom.onClick` | `page` |
| `view 02_Components/03_PLC/Module_1769_IQ16` | `root event dom.onClick` | `page` |
| `view 02_Components/03_PLC/Module_1769_OA16` | `root event dom.onClick` | `page` |
| `view 02_Components/03_PLC/Module_1769_OW16` | `root event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview` | `root` | page |

## redirectUrl {#redirecturl}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `script Navigation.Nav.navigate` | | `default` |

_No handler in the project (a gateway message handler, or a leftover sender)._

## rpBulk {#rpbulk}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/RPBulk` | `root event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpBulkApply {#rpbulkapply}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root message handler rpBulk` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpDiscard {#rpdiscard}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root/Content/ChangeBar/Discard event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpDiscardConfirmed {#rpdiscardconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root message handler rpDiscard` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpExpandAll {#rpexpandall}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root/Content/HeaderCard/Toolbar/ExpandAll event component.onActionPerformed` | `page` |
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root/Content/HeaderCard/Toolbar/CollapseAll event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpGroupToggle {#rpgrouptoggle}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/RPGroup` | `root/Header event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpRoleSelect {#rproleselect}

_No sender found by the scan (sent from a binding-built menu or a dynamic name)._

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpSave {#rpsave}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root/Content/ChangeBar/Save event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpSaveConfirmed {#rpsaveconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root message handler rpSave` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rpToggle {#rptoggle}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/RPCell` | `root event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |

## rptDeleteTemplate {#rptdeletetemplate}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 01_Popups/Reports/ReportBuilder` | `root/Body/Step4/Rail/Save/Body/TplRow/Delete event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | `root` | page |

## rptEdit {#rptedit}

<details>
<summary>Senders (13)</summary>

| Sender | Where | Scope |
|---|---|---|
| `view 01_Popups/Reports/_Assets/CheckItem` | `root/Check event component.onActionPerformed` | `page` |
| `view 01_Popups/Reports/_Assets/ChoiceTile` | `root event dom.onClick` | `page` |
| `view 01_Popups/Reports/_Assets/SectionItem` | `root/Line1/On event component.onActionPerformed` | `page` |
| `view 01_Popups/Reports/_Assets/SectionItem` | `root/Line1/Up event dom.onClick` | `page` |
| `view 01_Popups/Reports/_Assets/SectionItem` | `root/Line1/Down event dom.onClick` | `page` |
| `view 01_Popups/Reports/_Assets/SectionItem` | `root/TopNSettings/N binding props.value` | `page` |
| `view 01_Popups/Reports/_Assets/SectionItem` | `root/TopNSettings/TopN binding props.value` | `page` |
| `view 01_Popups/Reports/_Assets/SectionItem` | `root/TopNSettings/OrderBy binding props.value` | `page` |
| `view 01_Popups/Reports/_Assets/SourceCard` | `root event dom.onClick` | `page` |
| `view 01_Popups/Reports/ReportBuilder` | `root/Body/Step2/Main/Dates/From/Start binding props.value` | `page` |
| `view 01_Popups/Reports/ReportBuilder` | `root/Body/Step2/Main/Dates/To/End binding props.value` | `page` |
| `view 01_Popups/Reports/ReportBuilder` | `root/Body/Step3/Main/AdvancedPanels/Wording/Body/TitleField/Title binding props.text` | `page` |
| `view 01_Popups/Reports/ReportBuilder` | `root/Body/Step3/Main/AdvancedPanels/Wording/Body/NotesField/Notes binding props.text` | `page` |
</details>

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | `root` | page |

## rptLoadSaved {#rptloadsaved}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 01_Popups/Reports/_Assets/SavedRow` | `root event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | `root` | page |

## rptPageDelete {#rptpagedelete}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 01_Popups/Reports/_Assets/SavedListRow` | `root/Actions/Delete event dom.onClick` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/ReportsSaved` | `root` | page |

## rptSavedChanged {#rptsavedchanged}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 01_Popups/Reports/_Assets/SavedListRow` | `root/Actions/Share event dom.onClick` | `page` |
| `view 01_Popups/Reports/DownloadMenu` | `root/Pdf event component.onActionPerformed` | `page` |
| `view 01_Popups/Reports/DownloadMenu` | `root/Xls event component.onActionPerformed` | `page` |
| `view 01_Popups/Reports/DownloadMenu` | `root/Csv event component.onActionPerformed` | `page` |
| `view 01_Popups/Reports/RenameReport` | `root/Name event component.onActionPerformed` | `page` |
| `view 01_Popups/Reports/RenameReport` | `root/Buttons/Save event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/ReportsSaved` | `root` | page |

## rptStart {#rptstart}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 01_Popups/Reports/_Assets/StartCard` | `root event dom.onClick` | `page` |
| `view 01_Popups/Reports/_Assets/StartTile` | `root event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Groveport/Operations/ReportsBuilder` | `root` | page |

## ticketLog {#ticketlog}

<details>
<summary>Senders (250)</summary>

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/00_Docked/_Assets/AlarmNotification` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/BrandLogo` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/ChangeTheme` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/IntegratorContact` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/IntegratorLogo` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/OosNotification` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/User` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/UserRoles&Login` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/_Assets/UserSettings` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/Header` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/Legend` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/Navigation` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/00_Docked/TempNav` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Alarms/Journal` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Alarms/Summary` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Compressors/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Devices/DesignOverview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Devices/DetailsOverview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Devices/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Devices/TypeTable` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/ExhaustFans/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/ExhaustFans/Details` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/ExhaustFans/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/LandingPage/Globe` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/LandingPage/PlantPlaceholder` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Machine Room/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/NoViewPath` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Operations/AuditLog` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Operations/RolesPermissions` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Pumps/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Pumps/Details` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Pumps/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Sensors/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Sensors/Details` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Sensors/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Tanks/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Tanks/Details` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Tanks/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Unit/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Valves/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Valves/Details` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Boars Head/Valves/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/_Shared/CG/AhuEvapDisplay` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/_Shared/CG/AhuEvapHistory` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Area/DomainKpis` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Club/Utility/CG-C1` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/CondenserFans/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/CondenserFans/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Pumps/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Pumps/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Sensors/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Sensors/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Tanks/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Tanks/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Valves/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Condensers/Utility/Valves/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Dock/Utility/CG-G1` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Dock/Utility/CG-G2` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Dock/Utility/CG-G3` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Dock/Utility/CG-G4` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Dock/Utility/CG-G5` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Domains/EPMS` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Domains/Production` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Domains/Utility` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/East PH/Utility/CG-E1` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/East PH/Utility/CG-E2` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/East PH/Utility/CG-E3` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/East PH/Utility/CG-E4` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Freezer/Utility/CG-A1` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Freezer/Utility/CG-A2` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Compressors/Design` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Compressors/Details` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Compressors/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Pumps/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Sensors/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Tanks/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Machine Room/Utility/Valves/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Operations/Forms/DailyRounds` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Operations/Forms/History` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Operations/Forms/PidVerification` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Operations/Forms/ShiftLog` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Palletizing/Utility/CG-D1` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level1/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level2/Forming` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level2/Kpis` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level2/Packaging` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level2/Prep` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/Handtman` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/Hopper` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/Kpis` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/LazySusan` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/Loaders` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/RollStock` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/ShrinkTunnel` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Production/Level3/VatDumper` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Site/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Site/OverviewClassic` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Site/OverviewExecutive` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/SuperChill/Utility/CG-B1` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/SuperChill/Utility/CG-B2` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Utility/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Utility/OverviewKpis` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Utility/OverviewStatuses` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/Utility/OverviewStatusTile` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/West PH/Utility/CG-F1` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/West PH/Utility/CG-F2` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/West PH/Utility/CG-F3` | `root binding meta.contextMenu.items` | `menu item` |
| `view 00_Pages/Groveport/West PH/Utility/CG-F4` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/AlarmConfiguration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Alarms` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Compressor/Configuration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Compressor/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Compressor/Interlocks` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Configuration/Configuration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/CoolingTower/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/DiscreteInputs` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Evaporator/Configuration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/InterlockPanel` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Interlocks` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Modes` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Pump/Alarms` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Pump/Configuration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Pump/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Pump/Interlocks` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Sensor/Alarms` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Sensor/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Tank/Configuration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Tank/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Trend` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Alarms` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Configuration` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Controls` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/AdhocTrend` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/AdhocTrendConfig` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Alerts/Alert` | `dialog binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Alerts/ContextMenu` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Alerts/OutOfService` | `dialog binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Compressor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/CoolingTower` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/DischargeSequence` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/DiscreteInput` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Evaporator` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/ExhaustFan` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Faceplate` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Interlock` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Pump` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Sensor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/SolenoidValve` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/SolenoidValve3Way` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/SuctionSequence` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/Tank` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/00_Faceplates/TankOverview` | `root binding meta.contextMenu.items` | `menu item` |
| `view 01_Popups/Reports/ReportBuilder` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/00_Controls/InterlockButton` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Compressor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Condenser` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/CoolingTower` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Evaporator` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/ExhaustFan` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/LTU` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Pump` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/SafetyRelay` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Sensor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/SolenoidValve` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/Tank` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/01_Devices/VesselGeneric` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/02_Widgets/KPI` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/02_Widgets/MetricCard` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/02_Widgets/Safetys` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/02_Widgets/SiteCard` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/03_PLC/Controller_CompactLogix_5370` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/03_PLC/Module_1769_IA16` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/03_PLC/Module_1769_IF8` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/03_PLC/Module_1769_IQ16` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/03_PLC/Module_1769_OA16` | `root binding meta.contextMenu.items` | `menu item` |
| `view 02_Components/03_PLC/Module_1769_OW16` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/00_Control/_Assets/Numeric` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/00_Control/AnalogInput` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/00_Control/AnalogValue` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/00_Control/MultiStateInput` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/00_Control/StringInput` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/00_Control/TimeInput` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/AlarmHeader` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/IconHeader` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Auto` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/DoorStatus` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Exclude` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Faceplate` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Hand` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Interlock` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Maintenance` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/NoMode` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/NotAtSetpoint` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Operator` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/OutOfService` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Override` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Program` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Remote` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Simulate` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/Icons/Stale` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/NotificationIcons/Blank` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/NotificationIcons/CommLoss` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/StatusDot` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/01_Status/StatusIndicator` | `root binding meta.contextMenu.items` | `menu item` |
| `view 03_Elements/03_Table/DeviceLabelAlarmIndicator` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/NamePlot` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/Pen` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/PenColor` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/PenDelete` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/PenEnable` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/PenPlot` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/Plot` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/RemovePlot` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/_Assets/ToolBar` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/Trend` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/AdhocTrend/UserSavedTrendConfig` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/ComponentPreview/Condenser-SafetyRelay` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/ComponentPreview/VesselGeneric` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/TicketLogger` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/Tools/L5K/Message` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/Tools/L5K/Parser` | `root binding meta.contextMenu.items` | `menu item` |
| `view 98_Configuration/Tools/L5K/Tags` | `root binding meta.contextMenu.items` | `menu item` |
</details>

<details>
<summary>Handlers (250)</summary>

| View | Component | Listens on |
|---|---|---|
| `00_Pages/00_Docked/Header` | `root` | page |
| `00_Pages/00_Docked/Legend` | `root` | page |
| `00_Pages/00_Docked/Navigation` | `root` | page |
| `00_Pages/00_Docked/TempNav` | `root` | page |
| `00_Pages/00_Docked/_Assets/AlarmNotification` | `root` | page |
| `00_Pages/00_Docked/_Assets/BrandLogo` | `root` | page |
| `00_Pages/00_Docked/_Assets/ChangeTheme` | `root` | page |
| `00_Pages/00_Docked/_Assets/IntegratorContact` | `root` | page |
| `00_Pages/00_Docked/_Assets/IntegratorLogo` | `root` | page |
| `00_Pages/00_Docked/_Assets/OosNotification` | `root` | page |
| `00_Pages/00_Docked/_Assets/User` | `root` | page |
| `00_Pages/00_Docked/_Assets/UserRoles&Login` | `root` | page |
| `00_Pages/00_Docked/_Assets/UserSettings` | `root` | page |
| `00_Pages/Boars Head/Alarms/Journal` | `root` | page |
| `00_Pages/Boars Head/Alarms/Summary` | `root` | page |
| `00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable` | `root` | page |
| `00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable` | `root` | page |
| `00_Pages/Boars Head/Compressors/Overview` | `root` | page |
| `00_Pages/Boars Head/Devices/DesignOverview` | `root` | page |
| `00_Pages/Boars Head/Devices/DetailsOverview` | `root` | page |
| `00_Pages/Boars Head/Devices/Overview` | `root` | page |
| `00_Pages/Boars Head/Devices/TypeTable` | `root` | page |
| `00_Pages/Boars Head/ExhaustFans/Design` | `root` | page |
| `00_Pages/Boars Head/ExhaustFans/Details` | `root` | page |
| `00_Pages/Boars Head/ExhaustFans/Overview` | `root` | page |
| `00_Pages/Boars Head/LandingPage/Globe` | `root` | page |
| `00_Pages/Boars Head/LandingPage/PlantPlaceholder` | `root` | page |
| `00_Pages/Boars Head/Machine Room/Overview` | `root` | page |
| `00_Pages/Boars Head/NoViewPath` | `root` | page |
| `00_Pages/Boars Head/Operations/AuditLog` | `root` | page |
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | `root` | page |
| `00_Pages/Boars Head/Operations/RolesPermissions` | `root` | page |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |
| `00_Pages/Boars Head/Pumps/Design` | `root` | page |
| `00_Pages/Boars Head/Pumps/Details` | `root` | page |
| `00_Pages/Boars Head/Pumps/Overview` | `root` | page |
| `00_Pages/Boars Head/Sensors/Design` | `root` | page |
| `00_Pages/Boars Head/Sensors/Details` | `root` | page |
| `00_Pages/Boars Head/Sensors/Overview` | `root` | page |
| `00_Pages/Boars Head/Tanks/Design` | `root` | page |
| `00_Pages/Boars Head/Tanks/Details` | `root` | page |
| `00_Pages/Boars Head/Tanks/Overview` | `root` | page |
| `00_Pages/Boars Head/Unit/Overview` | `root` | page |
| `00_Pages/Boars Head/Valves/Design` | `root` | page |
| `00_Pages/Boars Head/Valves/Details` | `root` | page |
| `00_Pages/Boars Head/Valves/Overview` | `root` | page |
| `00_Pages/Groveport/Area/DomainKpis` | `root` | page |
| `00_Pages/Groveport/Club/Utility/CG-C1` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/CondenserFans/Design` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/CondenserFans/Overview` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Overview` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Pumps/Design` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Pumps/Overview` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Sensors/Design` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Sensors/Overview` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Tanks/Design` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Tanks/Overview` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Valves/Design` | `root` | page |
| `00_Pages/Groveport/Condensers/Utility/Valves/Overview` | `root` | page |
| `00_Pages/Groveport/Dock/Utility/CG-G1` | `root` | page |
| `00_Pages/Groveport/Dock/Utility/CG-G2` | `root` | page |
| `00_Pages/Groveport/Dock/Utility/CG-G3` | `root` | page |
| `00_Pages/Groveport/Dock/Utility/CG-G4` | `root` | page |
| `00_Pages/Groveport/Dock/Utility/CG-G5` | `root` | page |
| `00_Pages/Groveport/Domains/EPMS` | `root` | page |
| `00_Pages/Groveport/Domains/Production` | `root` | page |
| `00_Pages/Groveport/Domains/Utility` | `root` | page |
| `00_Pages/Groveport/East PH/Utility/CG-E1` | `root` | page |
| `00_Pages/Groveport/East PH/Utility/CG-E2` | `root` | page |
| `00_Pages/Groveport/East PH/Utility/CG-E3` | `root` | page |
| `00_Pages/Groveport/East PH/Utility/CG-E4` | `root` | page |
| `00_Pages/Groveport/Freezer/Utility/CG-A1` | `root` | page |
| `00_Pages/Groveport/Freezer/Utility/CG-A2` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Compressors/Design` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Compressors/Details` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Compressors/Overview` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Overview` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Pumps/Overview` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Sensors/Overview` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Tanks/Overview` | `root` | page |
| `00_Pages/Groveport/Machine Room/Utility/Valves/Overview` | `root` | page |
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | `root` | page |
| `00_Pages/Groveport/Operations/Forms/History` | `root` | page |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | `root` | page |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | `root` | page |
| `00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions` | `root` | page |
| `00_Pages/Groveport/Palletizing/Utility/CG-D1` | `root` | page |
| `00_Pages/Groveport/Production/Level1/Overview` | `root` | page |
| `00_Pages/Groveport/Production/Level2/Forming` | `root` | page |
| `00_Pages/Groveport/Production/Level2/Kpis` | `root` | page |
| `00_Pages/Groveport/Production/Level2/Packaging` | `root` | page |
| `00_Pages/Groveport/Production/Level2/Prep` | `root` | page |
| `00_Pages/Groveport/Production/Level3/Handtman` | `root` | page |
| `00_Pages/Groveport/Production/Level3/Hopper` | `root` | page |
| `00_Pages/Groveport/Production/Level3/Kpis` | `root` | page |
| `00_Pages/Groveport/Production/Level3/LazySusan` | `root` | page |
| `00_Pages/Groveport/Production/Level3/Loaders` | `root` | page |
| `00_Pages/Groveport/Production/Level3/RollStock` | `root` | page |
| `00_Pages/Groveport/Production/Level3/ShrinkTunnel` | `root` | page |
| `00_Pages/Groveport/Production/Level3/VatDumper` | `root` | page |
| `00_Pages/Groveport/Site/Overview` | `root` | page |
| `00_Pages/Groveport/Site/OverviewClassic` | `root` | page |
| `00_Pages/Groveport/Site/OverviewExecutive` | `root` | page |
| `00_Pages/Groveport/SuperChill/Utility/CG-B1` | `root` | page |
| `00_Pages/Groveport/SuperChill/Utility/CG-B2` | `root` | page |
| `00_Pages/Groveport/Utility/Overview` | `root` | page |
| `00_Pages/Groveport/Utility/OverviewKpis` | `root` | page |
| `00_Pages/Groveport/Utility/OverviewStatusTile` | `root` | page |
| `00_Pages/Groveport/Utility/OverviewStatuses` | `root` | page |
| `00_Pages/Groveport/West PH/Utility/CG-F1` | `root` | page |
| `00_Pages/Groveport/West PH/Utility/CG-F2` | `root` | page |
| `00_Pages/Groveport/West PH/Utility/CG-F3` | `root` | page |
| `00_Pages/Groveport/West PH/Utility/CG-F4` | `root` | page |
| `00_Pages/Groveport/_Shared/CG/AhuEvapDisplay` | `root` | page |
| `00_Pages/Groveport/_Shared/CG/AhuEvapHistory` | `root` | page |
| `00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar` | `root` | page |
| `01_Popups/00_Faceplates/AdhocTrend` | `root` | page |
| `01_Popups/00_Faceplates/AdhocTrendConfig` | `root` | page |
| `01_Popups/00_Faceplates/Alerts/Alert` | `dialog` | page |
| `01_Popups/00_Faceplates/Alerts/ContextMenu` | `root` | page |
| `01_Popups/00_Faceplates/Alerts/OutOfService` | `dialog` | page |
| `01_Popups/00_Faceplates/Compressor` | `root` | page |
| `01_Popups/00_Faceplates/CoolingTower` | `root` | page |
| `01_Popups/00_Faceplates/DischargeSequence` | `root` | page |
| `01_Popups/00_Faceplates/DiscreteInput` | `root` | page |
| `01_Popups/00_Faceplates/Evaporator` | `root` | page |
| `01_Popups/00_Faceplates/ExhaustFan` | `root` | page |
| `01_Popups/00_Faceplates/Faceplate` | `root` | page |
| `01_Popups/00_Faceplates/Interlock` | `root` | page |
| `01_Popups/00_Faceplates/Pump` | `root` | page |
| `01_Popups/00_Faceplates/Sensor` | `root` | page |
| `01_Popups/00_Faceplates/SolenoidValve` | `root` | page |
| `01_Popups/00_Faceplates/SolenoidValve3Way` | `root` | page |
| `01_Popups/00_Faceplates/SuctionSequence` | `root` | page |
| `01_Popups/00_Faceplates/Tank` | `root` | page |
| `01_Popups/00_Faceplates/TankOverview` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/AlarmConfiguration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Alarms` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Compressor/Configuration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Compressor/Interlocks` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Configuration/Configuration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/CoolingTower/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Configuration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Interlocks` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Modes` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Pump/Alarms` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Pump/Configuration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Pump/Interlocks` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Sensor/Alarms` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Trend` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Alarms` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Configuration` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Controls` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | `root` | page |
| `01_Popups/Reports/ReportBuilder` | `root` | page |
| `02_Components/00_Controls/InterlockButton` | `root` | page |
| `02_Components/01_Devices/Compressor` | `root` | page |
| `02_Components/01_Devices/Condenser` | `root` | page |
| `02_Components/01_Devices/CoolingTower` | `root` | page |
| `02_Components/01_Devices/Evaporator` | `root` | page |
| `02_Components/01_Devices/ExhaustFan` | `root` | page |
| `02_Components/01_Devices/LTU` | `root` | page |
| `02_Components/01_Devices/Pump` | `root` | page |
| `02_Components/01_Devices/SafetyRelay` | `root` | page |
| `02_Components/01_Devices/Sensor` | `root` | page |
| `02_Components/01_Devices/SolenoidValve` | `root` | page |
| `02_Components/01_Devices/Tank` | `root` | page |
| `02_Components/01_Devices/VesselGeneric` | `root` | page |
| `02_Components/02_Widgets/KPI` | `root` | page |
| `02_Components/02_Widgets/MetricCard` | `root` | page |
| `02_Components/02_Widgets/Safetys` | `root` | page |
| `02_Components/02_Widgets/SiteCard` | `root` | page |
| `02_Components/03_PLC/Controller_CompactLogix_5370` | `root` | page |
| `02_Components/03_PLC/Module_1769_IA16` | `root` | page |
| `02_Components/03_PLC/Module_1769_IF8` | `root` | page |
| `02_Components/03_PLC/Module_1769_IQ16` | `root` | page |
| `02_Components/03_PLC/Module_1769_OA16` | `root` | page |
| `02_Components/03_PLC/Module_1769_OW16` | `root` | page |
| `03_Elements/00_Control/AnalogInput` | `root` | page |
| `03_Elements/00_Control/AnalogValue` | `root` | page |
| `03_Elements/00_Control/MultiStateInput` | `root` | page |
| `03_Elements/00_Control/StringInput` | `root` | page |
| `03_Elements/00_Control/TimeInput` | `root` | page |
| `03_Elements/00_Control/_Assets/Numeric` | `root` | page |
| `03_Elements/01_Status/AlarmHeader` | `root` | page |
| `03_Elements/01_Status/IconHeader` | `root` | page |
| `03_Elements/01_Status/Icons/Auto` | `root` | page |
| `03_Elements/01_Status/Icons/DoorStatus` | `root` | page |
| `03_Elements/01_Status/Icons/Exclude` | `root` | page |
| `03_Elements/01_Status/Icons/Faceplate` | `root` | page |
| `03_Elements/01_Status/Icons/Hand` | `root` | page |
| `03_Elements/01_Status/Icons/Interlock` | `root` | page |
| `03_Elements/01_Status/Icons/Maintenance` | `root` | page |
| `03_Elements/01_Status/Icons/NoMode` | `root` | page |
| `03_Elements/01_Status/Icons/NotAtSetpoint` | `root` | page |
| `03_Elements/01_Status/Icons/Operator` | `root` | page |
| `03_Elements/01_Status/Icons/OutOfService` | `root` | page |
| `03_Elements/01_Status/Icons/Override` | `root` | page |
| `03_Elements/01_Status/Icons/Program` | `root` | page |
| `03_Elements/01_Status/Icons/Remote` | `root` | page |
| `03_Elements/01_Status/Icons/Simulate` | `root` | page |
| `03_Elements/01_Status/Icons/Stale` | `root` | page |
| `03_Elements/01_Status/NotificationIcons/Blank` | `root` | page |
| `03_Elements/01_Status/NotificationIcons/CommLoss` | `root` | page |
| `03_Elements/01_Status/StatusDot` | `root` | page |
| `03_Elements/01_Status/StatusIndicator` | `root` | page |
| `03_Elements/03_Table/DeviceLabelAlarmIndicator` | `root` | page |
| `98_Configuration/AdhocTrend/Trend` | `root` | page |
| `98_Configuration/AdhocTrend/UserSavedTrendConfig` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/NamePlot` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/Pen` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/PenColor` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/PenDelete` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/PenEnable` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/PenPlot` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/Plot` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/RemovePlot` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` | `root` | page |
| `98_Configuration/AdhocTrend/_Assets/ToolBar` | `root` | page |
| `98_Configuration/ComponentPreview/Condenser-SafetyRelay` | `root` | page |
| `98_Configuration/ComponentPreview/VesselGeneric` | `root` | page |
| `98_Configuration/TicketLogger` | `root` | page |
| `98_Configuration/Tools/L5K/Message` | `root` | page |
| `98_Configuration/Tools/L5K/Parser` | `root` | page |
| `98_Configuration/Tools/L5K/Tags` | `root` | page |
</details>

## tlRoutingSave {#tlroutingsave}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 98_Configuration/TicketRouting` | `root/Content/ActionBar/Save event component.onActionPerformed` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/TicketRouting` | `root` | page |

## trendZoomReset {#trendzoomreset}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `script shared.AdhocTrend.(module level)` | | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Plot` | `root` | page |

## umAdd {#umadd}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/UsersBody/UserList/Toolbar/R1/Add event component.onActionPerformed` | `page` |
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root message handler umAdd` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umAdjAdd {#umadjadd}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/UsersBody/UserDetail/Editor/Scroll/Adjustments/AddRow/AddAdjustment event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umAdjRemove {#umadjremove}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/UMAdjustRow` | `root/Dates/Remove event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umAdjSet {#umadjset}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/UMAdjustRow` | `root/Dates/Start/Input binding props.value` | `page` |
| `view 00_Pages/Boars Head/Operations/_Admin/UMAdjustRow` | `root/Dates/End/Input binding props.value` | `page` |
| `view 00_Pages/Boars Head/Operations/_Admin/UMAdjustRow` | `root/Dates/Available binding props.selected` | `page` |
| `view 00_Pages/Boars Head/Operations/_Admin/UMAdjustRow` | `root/Note binding props.text` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umContactAdd {#umcontactadd}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/UsersBody/UserDetail/Editor/Scroll/Contacts/AddRow/AddContact event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umContactRemove {#umcontactremove}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/UMContactRow` | `root/Remove event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umContactSet {#umcontactset}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/UMContactRow` | `root/Type binding props.value` | `page` |
| `view 00_Pages/Boars Head/Operations/_Admin/UMContactRow` | `root/Value binding props.text` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umDelete {#umdelete}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/UsersBody/UserDetail/Editor/ActionBar/Delete event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umDeleteConfirmed {#umdeleteconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root message handler umDelete` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umDiscard {#umdiscard}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/UsersBody/UserDetail/Editor/ActionBar/Discard event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umDiscardConfirmed {#umdiscardconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root message handler umDiscard` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umRoleAdd {#umroleadd}

_No sender found by the scan (sent from a binding-built menu or a dynamic name)._

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umRoleDelete {#umroledelete}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/RolesBody/RoleEditor/Editor/ActionBar/Delete event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umRoleDeleteConfirmed {#umroledeleteconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root message handler umRoleDelete` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umRoleSave {#umrolesave}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/RolesBody/RoleEditor/Editor/ActionBar/Save event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umRoleSaveConfirmed {#umrolesaveconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root message handler umRoleSave` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umRoleSelect {#umroleselect}

_No sender found by the scan (sent from a binding-built menu or a dynamic name)._

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umRoleToggle {#umroletoggle}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/UMRoleOption` | `root event dom.onClick` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umSave {#umsave}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root/Content/UsersBody/UserDetail/Editor/ActionBar/Save event component.onActionPerformed` | `page` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umSaveConfirmed {#umsaveconfirmed}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root message handler umSave` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## umSelect {#umselect}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `view 00_Pages/Boars Head/Operations/_Admin/UMUserRow` | `root event dom.onClick` | `page` |
| `view 00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root message handler umSelect` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | `root` | page |

## writeValue {#writevalue}

**Senders:**

| Sender | Where | Scope |
|---|---|---|
| `script shared.Alerts.confirmApplyWrite` | | `Alert popup button (page)` |
| `view 03_Elements/00_Control/_Assets/Numeric` | `root/NumericEntryField binding props.value` | `Alert popup button (page)` |

**Handlers:**

| View | Component | Listens on |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` | `root` | page |
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | `root` | page |
| `03_Elements/00_Control/AnalogInput` | `root` | page |
| `03_Elements/00_Control/MultiStateInput` | `root` | page |
| `03_Elements/00_Control/StringInput` | `root` | page |
| `03_Elements/00_Control/TimeInput` | `root` | page |
| `03_Elements/00_Control/_Assets/Numeric` | `root` | page |
