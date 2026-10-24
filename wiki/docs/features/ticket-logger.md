---
title: Ticket Logger
sidebar_position: 18
description: Logging a ticket from any view, routing by type and area to Monday or Oracle, the dry run, and the Settings (OneShot only).
sources:
  - docs/ticket-logger.md
  - docs/ticket-logger-monday.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py
last_verified: 2026-10-24
---

# Ticket Logger

## What it does

Lets a user report an issue, bug, request or question about the screen they are looking at. The ticket carries the
view, the device tag path and the reporter, and is sent to a ticketing destination chosen by the ticket's **Type**
and **Area**: today Monday.com; Oracle is prepared and queued ("not yet connected").

## Who can use it

| Permission row | Who | Gates |
|---|---|---|
| `TicketLogger/Use` | **Every role** | The right-click Ticket Logger menu and Send |
| `TicketLogger/Settings` | **OneShot only** (a restricted row: it is not implied for Administrator and is hidden on Roles & Permissions from other users) | The settings gear and everything behind it (API setup, routing, dry run) |

Any signed-in user can log a ticket, and logging does not depend on Monday being connected: routing always finds a
destination (an unknown or missing rule falls back to Monday, and a ticket routed to Oracle is queued). If Monday is
down, a Monday-routed ticket fails at Send with the Monday error. Only the integrator role (OneShot) can open the
Settings, because they hold the API connection details.

On the Roles & Permissions page the two Ticket Logger rows are shown only to OneShot users; everyone else does not
see them in the matrix, the group counts or the role lists (the ticks themselves are still in effect). A **new role
gets `TicketLogger/Use` by default**: a role created in the New Role wizard has it pre-ticked, and a role created
directly in the Gateway gets it from the tag `[default]_Config/Security/NewRoleDefaults` (see
[Roles & Permissions](./roles-permissions.md#new-roles)).

## How to use it (every user)

1. Right-click a value or device on any page and choose **Ticket Logger** (or use the Ticket Logger menu entry).
2. Pick a **Type** (Issue, Bug, Request, Question), a **Priority** (1 to 4) and fill in at least one text section plus
   the title. The **Area** is taken from the device's tag path automatically.
3. The line under the type tells you where it goes: **Sends To Monday**, or **Sends To Oracle (Queued Until
   Connected)**. While the dry run is on you also see **Dry Run, Nothing Is Sent**.
4. Press **Send**. The result shows "Sent To Monday" with a link, or "Queued For Oracle (Not Yet Connected)".

## Routing

Routing decides the destination from Type and Area (Priority is sent but not used to route). The rules are the
Document tag `[default]_Config/TicketLogger/Routing`:

- An empty Type or Area means "Any". The **most specific** matching rule wins: Type and Area, then Type, then Area;
  if nothing matches the **Default Destination** is used. A rule must name a Type or an Area.
- Destinations are `Monday` and `Oracle`. A Monday rule may name its own Board and Group; empty means the Monday
  integration's own settings.
- **Oracle is a stub:** a ticket routed to Oracle is stored in the SQL table `dbo.ticket_outbox` with the status
  `Pending Oracle` and the user sees "Queued For Oracle (Not Yet Connected)". Nothing is sent. When the Oracle
  connection exists, a sender can drain those rows without changing the form, the routing or the settings.
- **Dry run:** the Boolean tag `[default]_Config/TicketLogger/DryRun`. While it is on, nothing is created in Monday
  and nothing is queued for Oracle; every ticket is recorded in the outbox as `Dry Run` and the user sees what would
  have happened. Leave it off in production.

## Settings (OneShot only)

Open the Ticket Logger popup and press the gear (visible only with `TicketLogger/Settings`).

- **Destinations tab:** the Monday card (endpoint, API version, board settings, **Test Connection**; the token field
  is write-only, so the page never shows an existing token), an **Oracle** card marked "Coming Soon" with disabled
  fields and the count of queued tickets, and the **Dry Run** card (state, Turn On / Off, how many were recorded).
- **Routing tab:** a table of rules (Type, Area, Destination, Board / Group). Click a row to edit it in the editor
  (dropdowns for Type, Area and Destination), then **Add Rule** or **Apply To Rule**; **New Rule** and **Remove
  Rule** manage the list; the **Default Destination** card sets the fallback. Edits are a draft: the bar shows
  **Unsaved Changes**, **Discard Changes** and **Save Routing**. Saving asks for confirmation and writes an entry to
  the [Audit Log](./audit-log.md) ("Ticket Routing Changed" with a summary of the rules and no secrets).

## Where the pieces live

| Piece | Where |
|---|---|
| Ticket form | Designer > Views > `98_Configuration` > `TicketLogger` |
| Settings | `98_Configuration/TicketLoggerSettings`, `98_Configuration/TicketRouting`, `98_Configuration/Integrations` |
| Script library | `shared.TicketLogger` (send, routing, adapters), `shared.Integrations` (settings, token) |
| Tags | Tag Browser > `[default]_Config` > `TicketLogger` (`Routing`, `DryRun`, `Types`), `Integrations/Monday` |
| SQL | table `dbo.ticket_outbox`; named queries `TicketLogger/OutboxInsert`, `OutboxCounts` |
| Permissions | rows `TicketLogger/Use` and `TicketLogger/Settings` on [Roles And Permissions](./roles-permissions.md) |

## How To Change It

- **Change where a type or area goes:** sign in as a OneShot user > Ticket Logger > gear > **Routing**. No Designer
  edit is needed.
- **Add a ticket Type:** Tag Browser > `[default]_Config/TicketLogger/Types` > edit the value, then add routing
  rules for it.
- **Stop one role from logging tickets:** sign in as OneShot > Admin > Roles & Permissions > untick **Use Ticket
  Logger** for that role > Save Changes. The rows are invisible to other users.
- **Change which rows are OneShot-only:** Tag Browser > `[default]_Config/Security/RestrictedRows` (a list such as
  `TicketLogger/Settings:OneShot, TicketLogger/Use:OneShot`). The `Settings` row is deliberately kept away from
  Administrator; do not remove it without the project owner's agreement.
- **Change what a new role gets automatically:** Tag Browser > `[default]_Config/Security/NewRoleDefaults` (comma
  separated `Device/Action` keys; today `TicketLogger/Use`).
- **Try the routing without sending anything:** sign in as OneShot > Ticket Logger > gear > Destinations > Dry Run >
  Turn On. Log a test ticket; the message says what would have happened and the ticket is recorded in the outbox as
  `Dry Run`. Turn it off again afterwards. Dry-run rows in `dbo.ticket_outbox` can be deleted freely.
- **Connect Oracle later:** add an Oracle integration instance under `[default]_Config/Integrations`, replace the
  Oracle stub in the `shared.TicketLogger` script with a sender that sends the `Pending Oracle` outbox rows and
  records the result, and enable the card's fields. The form, routing and settings pages keep working unchanged.
- **Add another destination:** add a function with the same signature as the Monday adapter in `ADAPTERS` and the
  name in `DESTINATIONS` (Designer > Project Library > `shared` > `TicketLogger`).
- Monday API details (board, columns, webhook) are in [Gateway REST API](../gateway/rest-api.md) and the project doc
  `docs/ticket-logger-monday.md`.

Never put a token or other credential into a view, a tag value shown to users, a log line or an audit entry. The
Monday token lives only in the write-only integration tag and is read only by gateway-side scripts.

## Known limitations and parked items

- Oracle delivery is not built yet.
- The Settings views are excluded from the Ticket Logger menu so a ticket cannot be raised about the settings page.

Source of truth: `docs/ticket-logger.md`.
