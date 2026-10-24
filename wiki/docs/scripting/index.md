---
title: Scripting
slug: /scripting
sidebar_position: 1
description: How the BH project uses Python (Jython 2.7) scripts - the shared project library, gateway events, Perspective scripts, named queries, WebDev and reports.
sources:
  - gateways/standard/data/projects/BH/ignition/**/*
  - gateways/standard/data/projects/BH/com.inductiveautomation.webdev/**/*
  - gateways/standard/data/projects/BH/com.inductiveautomation.reporting/**/*
last_verified: 2026-10-24
---

# Scripting

The BH HMI keeps as much logic as possible in **bindings and expressions** (see the project rule
"scripting last" in [Conventions](./conventions.md)). Python is used where nothing else works: commands that
write to tags, anything that touches SQL, permission checks that must run on the gateway, and generated helpers.

All Ignition scripts are **Jython 2.7** (Python 2 syntax and semantics running on the Java VM). You can import Java
classes (`from java.util import Date`) and you call the Ignition API through the `system.*` functions.

## Where scripts live

| What | Designer location | Files (under `gateways/standard/data/projects/BH/`) | Runs in |
|---|---|---|---|
| Project library (`shared.*`, `Navigation.*`, `L5K.*`) | Project Browser > Scripting > Project Library | `ignition/script-python/<package>/<Module>/code.py` | whoever calls it (gateway or a Perspective session thread) |
| Gateway timer / tag change / message events | Project Browser > Scripting > Gateway Events | `ignition/timer/*`, `ignition/tag-change/*`, `ignition/message/*` | gateway |
| Perspective component / view scripts (events, transforms, message handlers, custom methods) | inside each view (Configure Events, Configure Scripts, binding transforms) | `com.inductiveautomation.perspective/views/**/view.json` | gateway, on behalf of one Perspective session |
| Session props bindings | Project Browser > Perspective > Session Props | `com.inductiveautomation.perspective/session-props/props.json` | gateway, per session |
| Named queries (SQL) | Project Browser > Data > Named Queries | `ignition/named-query/<Folder>/<Query>/query.sql` | gateway database connection `ignition` |
| WebDev endpoints | Project Browser > Web Dev | `com.inductiveautomation.webdev/resources/*` | gateway (HTTP request thread) |
| Report data-source scripts | Project Browser > Reports | `com.inductiveautomation.reporting/reports/*/data.bin` | gateway (report engine) |
| Tag event scripts | Tag Editor > Events | `config/resources/core/ignition/tag-definition/**` | gateway |

:::tip Perspective scripts always run on the gateway
Unlike Vision, a Perspective "client" is only a browser. Every Perspective script (button `onActionPerformed`, a
script transform, a message handler) executes **on the gateway** in a thread tied to that user's session. That is
why `shared.Security` can check permissions server-side and why `print` output goes to the gateway log, not to the
browser.
:::

## Pages in this section

| Page | Read it when you want to |
|---|---|
| [Project Library](./project-library.md) | know what every `shared.*` module is for and how they call each other |
| [Scopes, Logging And Errors](./scopes-and-runtime.md) | understand gateway vs session scope, Jython 2.7 gotchas, loggers and error handling |
| [Write Paths And Guards](./write-path.md) | change anything that writes a tag (the audited, permission-checked, PLC-locked path) |
| [Gateway Events](./gateway-events.md) | change the timer / tag-change scripts (Overview rebuild, PLC write lock, Monday ping) |
| [Perspective Scripting](./perspective-scripting.md) | work with session props, message handlers, context menus and the Alert popup |
| [Named Queries](./named-queries.md) | add or change SQL (OpsForms, OutOfService, Reports, AdhocTrend, OpsAudit, TicketLogger) |
| [WebDev And Reporting](./webdev-and-reporting.md) | touch the globe WebDev endpoints or the PDF reports |
| [Conventions](./conventions.md) | write new script code that matches the project |
| [Reference (Generated)](./reference/index.md) | look up an exact function signature, docstring or "who calls this?" |

## The most important ideas in one list

1. **Everything is edited in the Designer.** Library modules live under Project Browser > Scripting > Project
   Library; open one, edit, save, test in a session.
2. **Every operator write goes through one path**: `shared.Alerts.confirmApplyWrite` (confirm dialog) then
   `shared.Audit.writeTag` (permission check, PLC write lock, audit entry). See [Write Paths](./write-path.md).
3. **Permissions are data, not code.** `shared.Security` reads the Roles & Permissions matrix tag; no role name is
   hard-coded. See [Roles & Permissions](../features/roles-permissions.md).
4. **Who / when always comes from the gateway** (`session.props.auth.user`, the gateway clock), never from a view
   parameter the browser could fake.
5. **Save in the Designer, then test in a Perspective session.** There is nothing else to run.
