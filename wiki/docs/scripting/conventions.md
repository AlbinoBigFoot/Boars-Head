---
title: Coding Conventions
sidebar_position: 9
description: How to write scripts that fit the BH project - binding preference, security, writes, SQL, encoding, naming, Title Case, comments and the edit workflow.
sources:
  - README.md
last_verified: 2026-10-23
---

# Coding Conventions

These rules come from the project's rule book and from how the existing code is written. Follow them
and your change will look like the rest of the project.

## Bindings and scripts

- **Scripting last.** Expression > expr-struct > expression transform > script. Scripts only for one-shot
  commands, confirms, tag browse / configure, and gateway work (SQL, permissions).
- **Null-safe expressions.** Wrap comparisons in `coalesce()`, reads in `try()` / `isGood()`. A null in `if()` puts
  the binding in an error state.
- **No designer placeholder paths.** Keep `params.tagPath` empty in a component's defaults.
- **Keep event scripts thin.** One call into `shared.*` with `self.session` and the view's params.

## Security and writes

- **Check on the gateway.** Every library entry point that acts for a user calls `shared.Security.require(device,
  action, what, session)` (or `allowed(self.session, ...)`). The UI gate (`session.custom.*`) is a convenience,
  not the enforcement.
- **No hard-coded role names.** Use the Roles & Permissions matrix (`session.custom.Permissions.<Device>.<Action>`)
  or the role-list tags in `[default]_Config/Security/*`. New gated features add a matrix row to
  `[default]_Config/RolesPermissions` (Tag Browser).
- **Writes go through `shared.Audit.writeTag`** (or `shared.ValveCommands`, `shared.OutOfService`). Never
  `system.tag.writeBlocking` a device value from a view.
- **Never write to the PLC.** Nothing writes `[RCP1]` / `[default]_RCP1_`; nobody but the user unlocks
  `_Config/PlcWriteLock/Locked`.
- **Who / when from the gateway.** `session.props.auth.user` and `system.date.now()`, never view params.

## SQL

- Named queries only, every value a parameter, database `ignition`.
- No `:name` text inside SQL comments.
- Schema changes go in an idempotent `sql/<feature>.sql` (`IF OBJECT_ID(...) IS NULL`, `IF NOT EXISTS (... index)`)
  applied with SSMS or `sqlcmd -I`.

## Text, encoding and line endings

- **UTF-8 without BOM** everywhere. On Windows never edit repo files with PowerShell `Get-Content` /
  `Set-Content` / `Out-File`: they produce the classic mojibake (a stray "A-circumflex" before a middle dot or degree
  sign) or add a BOM. Edit in the Designer, which always writes UTF-8.
- Perspective expressions inside JSON must stay **LF-only** (`core.autocrlf=true` would otherwise turn them into
  CRLF). The Designer writes `\n`.
- If a symbol shows a stray character, retype it in the Designer and save.

## Naming and wording

- **Title Case for every user-facing string**: section titles, KPI labels, buttons, table headers, dialog titles
  (`Take Out Of Service`, `Print / Download PDF`). Tag paths and member names keep their PLC / UDT casing
  (`Cfg_DefrostStartMode`).
- Library modules: `shared.<PascalCase>`; public functions `camelCase`; internal helpers start with `_`.
- Loggers: `system.util.getLogger("shared.<Module>")`.
- Popup ids are stable strings (`alertDialog`, `comp-fp-<tagPath>`), so a second open replaces the first.

## Comments

- Start each module with a comment block: what it does, and the doc page.
- Comment only constraints the code cannot show: why a fail-safe exists, a Perspective quirk, a user decision with
  its date ("user 2026-10-23: ..."). Do not narrate the code.

## Workflow for any change under `projects/`

1. Make the change in the Designer and save.
2. Verify in a Perspective session (Designer > Perspective > Launch Session, or
   `http://localhost:19088/data/perspective/client/BH`); restart the gateway only if the client still shows the old
   version after a browser reload.
3. Regenerate the wiki reference: `python -I wiki/tools/gen_all.py`, and update the hand-written page.
4. Commit only when the project owner asks (see [Git Workflow](../git-workflow/index.md)).
