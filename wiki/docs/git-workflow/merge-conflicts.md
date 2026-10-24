---
title: Merge Conflicts
sidebar_position: 4
description: Resolving conflicts in project and tag files, and what to check in the Designer after any merge, rebase or checkout.
sources:
  - README.md
last_verified: 2026-10-24
---

# Merge Conflicts

Ignition project resources are large JSON files, and every Designer save also updates the resource's `resource.json`
metadata. Conflicts are common when two branches touch the same view. The best prevention is small branches and
telling teammates which views you are editing.

## The Rules

1. **`resource.json` conflicts: take either side, then reopen the view in the Designer and save it once.** The
   metadata is derived data; never hand-merge two signatures. If the Designer still reports an error when opening the
   project, restore the last good version of that resource from git.
2. **`projects/.resources/*`: never resolve, never commit.** Take whatever is on disk; the gateway rebuilds it.
3. **View files (`view.json`): decide per component, not per line** (below), then open the view in the Designer to
   confirm it loads.
4. **Tags (`tags.json`, `udts.json`): merge, then re-import** the affected folder in the Designer (Tag Browser >
   right-click the folder > Import Tags) so the running gateway matches the files.

## Merging A `view.json`

- Use a JSON-aware diff (VS Code's merge editor works). Conflicts are usually inside `root.children[...]`: decide per
  component (matched by `meta.name`).
- Keep `propConfig` binding keys intact (`props.text`, `custom.*`, `position.*`): a broken scope prefix fails to load.
- Expression and script strings must stay on **LF** line endings inside the JSON and script bodies **tab-indented**. A
  merge tool that converts to CRLF inside a JSON string breaks the expression.
- Search the file for `<<<<<<<` before opening it in the Designer.

## After Any Merge, Rebase, Cherry-Pick Or Checkout

Git writes project files on disk behind the Designer's back. Afterwards:

1. In the Designer choose **File > Update Project** (or close and reopen the project).
2. Open each affected view and page in the client and look for error overlays.
3. If a view stays stale in the client, restart the gateway service, or ask the system integrator.

## Symptoms Of A Bad Merge

| Symptom | Cause | Fix |
|---|---|---|
| Designer shows an error opening or updating the project | `resource.json` metadata merged badly | Restore the resource's last good version from git, reopen, save |
| View shows "Error loading view" | Invalid JSON or a bad `propConfig` key | Fix the JSON or the key |
| Red binding overlays after merge | Expression broken (CRLF, merge markers in a string) | Search the file for `<<<<<<<` and `\r\n` |
| Text shows a stray character before `·` or `°` | Encoding damage (file saved as ANSI) | Re-save the file as UTF-8 without BOM |
| Tags missing on the gateway after merge | Files merged but not imported | Import the folder in the Designer Tag Browser |
