---
title: Windows And Encoding Gotchas
sidebar_position: 5
description: The PowerShell, curl, line-ending and UTF-8 traps on the Windows lab machine, and how to avoid them.
sources:
  - README.md
last_verified: 2026-10-23
---

# Windows And Encoding Gotchas

The lab machine runs **Windows 11 with Windows PowerShell 5.1**. These traps have each caused real bugs in this
project.

## PowerShell

| Trap | What Happens | Do This Instead |
|---|---|---|
| `a && b` | Parser error in PowerShell 5.1 | `a; b`, or `a; if ($?) { b }` to run `b` only when `a` succeeded |
| `curl ...` | `curl` is an alias for `Invoke-WebRequest`, different flags | Always `curl.exe` |
| Parentheses in `docker exec ... sh -lc "..."` | PowerShell mangles them before `sh` sees them | Keep container commands simple, e.g. `docker exec bh-ignition-standard sed -n '3237p' <file>` |
| `2>&1` on native programs | Each stderr line becomes an error record; `$?` goes false even on exit 0 | Let stderr print normally |
| `VAR=x cmd` | Bash syntax, fails | `$env:VAR = 'x'; cmd` |

Git Bash (installed with Git for Windows) is available too, and the shell snippets in this wiki marked `bash` work
there.

## Encoding: The Recurring Mojibake Bug

Everything in the repo is **UTF-8 without a BOM**. Windows falls back to the **cp1252** code page wherever a tool
isn't told the encoding, and the result is mojibake: a stray capital A with a circumflex (U+00C2) appears before
the middle dot in `Defrost · Bleed` or before the degree sign in `°F`, and an em dash turns into three
characters starting with a-circumflex. In a `view.json` it can also appear JSON-escaped (a U+00C2 escape right before the middle-dot escape).

Rules:

1. **Never edit repo files with Windows PowerShell `Get-Content` / `Set-Content` / `Out-File`.** PowerShell 5.1 reads
   BOM-less UTF-8 as ANSI, and `-Encoding utf8` *writes a BOM*. Both corrupt files. Use the Designer or an editor set
   to UTF-8 without BOM.
2. **Don't pipe project files through PowerShell.** If you must, use an editor.
3. **Type symbols in the Designer** (`·`, `°`, `—`) rather than pasting from Word, which can bring odd characters. A Designer save always writes UTF-8 correctly.
4. **If a label shows a stray character before a symbol**, retype the label in the Designer and save.

## Line Endings (CRLF vs LF)

- Git is set to `core.autocrlf=true` on this machine, so files are checked out with CRLF and committed with LF.
- **Perspective expressions and scripts must stay LF-only inside their JSON strings.** A `\r\n` inside an
  expression string breaks it (see the old branch `feature/fix-expression-crlf`). The Designer always writes `\n`.
- Script bodies inside `view.json` (`"code"`, `"script"`) are **tab-indented** the way the Designer writes them.

## Paths

- Use forward slashes in Python and in this wiki (`gateways/standard/data/...`); Windows accepts them.
- Folder names with spaces (`Machine Room`, `East PH`, `Microsoft SQLServer`) need quotes in every shell.
- The user's Windows temp path is `C:\Users\DYLAN~1.JON\...` (8.3 short name). Some tools refuse short names; use
  the long form `C:\Users\dylan.jones\...` if a path is rejected.
