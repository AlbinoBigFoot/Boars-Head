---
title: "Config/Integration"
sidebar_label: "Integration"
description: "UDT definition Config/Integration: One API endpoint / connection (_Config/Integrations/<Name>). shared.Integrations reads and edits it; Ticket Logger > Integrations lists them."
generated: true
---

:::note

:::
# UDT `Config/Integration`

One API endpoint / connection (\_Config/Integrations/&lt;Name&gt;). shared.Integrations reads and edits it; Ticket Logger &gt; Integrations lists them.

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; Config &gt; Integration |
| Tag path | `[default]_types_/Config/Integration` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Config/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 10 (10 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

_No parameters._

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Provider` | String | memory | | | | | | Provider key - picks the connection test and client (Monday, Oracle, HTTP) |
| `Description` | String | memory | | | | | | What this endpoint is used for |
| `Enabled` | Boolean | memory = `False` | | | | | | Off = never called, Connected stays false |
| `Endpoint URL` | String | memory | | | | | | Base URL of the API |
| `API Version` | String | memory | | | | | | API version header, where the provider has one (Monday API-Version) |
| `API Token` | String | memory = `(hidden)` | | | | | | Credential sent as Authorization. Write-only from the HMI; this folder is not in git |
| `Connected` | Boolean | memory = `False` | | | | | | Last connection test passed (pingMonday timer -&gt; shared.Integrations.pingAll) |
| `Last Check` | DateTime | memory | | | | | | When the connection was last tested |
| `Last Error` | String | memory | | | | | | Last connection test error ('' when connected) |
| `Settings` | Document | memory = `(document, 2 chars)` | | | | | | Provider-specific settings, e.g. Monday workspaceId / boardId / groupId / columns |

## Alarms

_No alarms defined on this type._

## Used By

1 direct instance(s):

| Instance | Instance page |
|---|---|
| `[default]_Config/Integrations/Monday` | `Integrations` |
