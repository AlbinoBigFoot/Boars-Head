---
title: Scopes, Logging And Errors
sidebar_position: 3
description: Gateway vs Perspective session scope, Jython 2.7 rules, module state, logging and the error-handling patterns used in the BH scripts.
sources:
  - gateways/standard/data/projects/BH/ignition/script-python/**/code.py
  - gateways/standard/data/projects/BH/ignition/tag-change/**/*
  - gateways/standard/data/projects/BH/ignition/timer/**/*
last_verified: 2026-10-24
---

# Scopes, Logging And Errors

## Jython 2.7 in one paragraph

Ignition runs Python 2.7 syntax on the Java VM (Jython). So: `print x` works (but use a logger), strings are byte
strings unless you write `u"..."` (the code uses `unicode(v)` where non-ASCII text matters), integer division
`7 / 2` is `3`, there are no f-strings (use `"%s" % x`), and many Python 3 libraries do not exist. In exchange you
can import any Java class: `from java.util.concurrent.locks import ReentrantLock`,
`from java.lang import Thread`. Jython's own `json` module is slow; the BH code uses `system.util.jsonDecode`
/ `jsonEncode` for anything large.

## The three scopes

Ignition talks about **scopes**: where a script runs and what it can reach.

| Scope | Who runs it | What it has | BH examples |
|---|---|---|---|
| **Gateway** | the gateway itself: timer, tag-change and message events, tag event scripts, WebDev (which has no Perspective session of its own; it checks the caller with `shared.WebAuth`), report data sources | `system.tag`, `system.db`, `system.util`, `system.report`; **no user, no `self`** | `pingMonday` timer, `plcWriteLock` tag-change event, `overviewRebuild`, report `reportData` scripts |
| **Perspective session** | the gateway, on behalf of one browser session (component events, binding transforms, message handlers, session / page events) | everything above plus `self.session`, `self.page`, `self.view`, `system.perspective.*` | a button calling `shared.Audit.writeTag`, the Report Builder's `builderModel` transform |
| **Designer / Vision client** | the Designer's script console or a Vision client | client-side `system.*` variants | not used by BH at runtime |

A library function runs in **the scope of its caller**. The same `shared.Audit.writeTag` is a session call when a
button runs it and a gateway call when `shared.OutOfService` runs it from inside a gateway transaction. Code that
must behave differently asks:

- `shared.Security._currentSession()` returns the Perspective session running the script, or `None` in gateway
  scope. It tries Perspective's thread-locals first and then walks the Python call stack for a `self` with a
  `.session` (on 8.3.7 the thread-locals are empty in component scripts, so the stack walk is what actually works).
- `shared.Security.can(...)` returns **True outside a session**, so gateway logic (timers, tag events) is never
  blocked by user permissions. If a session's roles cannot be read it logs one warning and allows (the UI gates
  still apply).
- `shared.Audit._sessionMayWrite` refuses direct `<device>.Enabled` writes **only** when a session is present:
  sessions must use `shared.OutOfService`.

:::warning Pass the session, never a username
Functions that act for a user take `session` as their first argument and read the user from
`session.props.auth.user` on the gateway. A username passed in a view parameter could be faked by the browser.
Who / when is always the gateway's (user from the session, time from `system.date.now()`).
:::

### What is shared between calls

- **Module-level variables** live as long as the project's script interpreter. Saving or scanning the project
  **restarts** it, so module state is a cache, never storage. Examples: `shared.Audit._recentWrites` (1 s
  de-duplication of double clicks), `Navigation.Nav` tree cache, `shared.Reports` catalog cache (30 s).
- **`system.util.getGlobals()`** survives script reloads. `shared.PlcWriteLock` keeps its Java `ReentrantLock` and
  "pending" flag there so two workers can never run at once after a project save; `shared.Globe` keeps its
  per-gateway-run HMAC secret there.
- **Background work** uses `system.util.invokeAsynchronous(fn)` (for example the PLC write-lock worker that changes
  `readOnly` on about 37,000 tags in chunks of 5,000 with a 2 s pause).

## Logging

Every module that logs creates a named logger:

```python
_log = system.util.getLogger("shared.PlcWriteLock")
_log.info("PLC write lock (flip): Locked=%s ..." % locked)
```

Find the messages in the Gateway web UI under **Diagnostics > Logs** (filter by the logger name), or from a
shell with `docker logs --tail 200 bh-ignition-standard`. The full list of logger names is generated in
[Logger Names](./reference/loggers.md). The ones you will read most:

| Logger | Typical lines |
|---|---|
| `shared.PlcWriteLock` | every Locked flip with counts, "Refused write ... PLC writes locked" |
| `shared.Security` | "Denied Faceplates/Operate for 'user': path" (every server-side refusal) |
| `shared.Audit` | "Refused direct ... .Enabled write", OpsAudit insert failures |
| `shared.Forms`, `shared.Reports`, `shared.OutOfService` | failed SQL, refused permissions, PDF errors |
| `BH.TicketLogger` | one line per ticket: destination, rule match, dry run |
| `BH.WebAuth`, `BH.Rack3d` | WebDev login-check failures (debug), 3D rack state errors |
| `shared.ValveCommands` | refused writes to PLC-mapped devices, bad write qualities |

Set a logger to DEBUG in **Diagnostics > Logs > Logging Levels** while you investigate, and set it back after.

## Error-handling patterns

The project uses a small number of patterns consistently. Follow them in new code.

1. **Fail safe, show the raw value.** Display helpers never raise into a view: on any error they return the raw
   value or a dash. Example: `shared.Enums.describe()` falls back to `"%s" % value`; `shared.Alerts._describe`
   wraps it again.
2. **Fail safe towards "blocked" for safety checks.** `shared.PlcWriteLock` treats a bad, null or unreadable
   `Locked` as **locked**; if `writeAllowed` itself throws, `shared.Audit._plcWriteBlocked` still blocks any path
   that names `RCP1`.
3. **Catch Java exceptions too.** A Java exception (for example a JDBC error) is not always caught by
   `except Exception`. Modules that call the database import `from java.lang import Throwable` and use
   `except (Exception, Throwable) as e:` (see `shared.Forms`, `shared.Reports`).
4. **Return a result dict instead of raising** for operator actions:
   `shared.Audit.writeTag` returns `{ok, skipped, denied, plcLocked, oldValue, newValue, quality, statusCode}`;
   the caller decides what to show.
5. **Transactions keep SQL and tags consistent.** `shared.OutOfService.setOutOfService` writes the SQL row inside
   `system.db.beginTransaction(...)`, writes the tag, reads it back, and commits only when the tag really changed;
   otherwise it rolls back (and puts a written tag back). The log and the tag never disagree.
6. **Log refusals, not just errors.** `shared.Security.require()` logs who was denied what, so a "button does
   nothing" report can be answered from the gateway log.

## Quick checklist for a new script

- Which scope will call it? If a session, does it take `session` and check `shared.Security.require`?
- Does it write a tag? Use `shared.Audit.writeTag` (see [Write Paths](./write-path.md)).
- Does it touch SQL? Use a named query, never string-built SQL (see [Named Queries](./named-queries.md)).
- Does it hold state? Module variables are lost on every project save; use tags or SQL for anything durable.
- Does it log with a named logger and catch `(Exception, Throwable)` around Java / DB calls?
