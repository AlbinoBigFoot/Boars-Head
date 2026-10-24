---
title: Wiki Tools
sidebar_position: 3
description: gen_all.py, check_docs.py, the source manifest, and how to write or extend a reference tool.
sources:
  - wiki/tools/gen_all.py
  - wiki/tools/check_docs.py
  - wiki/package.json
last_verified: 2026-10-23
---

# Wiki Tools

All tools are stdlib-only Python under `wiki/tools/`, safe to run with `python -I` (isolated mode), UTF-8 throughout.
They only read the project; they never touch the gateway.

## `gen_all.py`: Regenerate The Reference

```powershell
python wiki/tools/gen_all.py              # every area
python wiki/tools/gen_all.py tags         # only some: tags, perspective, scripting
```

1. Imports each `wiki/tools/gen_<area>.py` that exists and calls its `main(repo_root)`. A failing tool is
   reported and the others still run.
2. Hashes (SHA-1) every source file the tool reads and records them in **`wiki/tools/manifest/sources.json`**
   (commit it with the regenerated pages).
3. Prints the number of generated pages per area (pages with `generated: true`).

| Tool | Writes | Reads (default source globs) |
|---|---|---|
| `gen_tags.py` | `docs/tags/reference/**` | `tag-definition/**`, `tag-type-definition/**`, `tag-group/**`, `tag-provider/**` |
| `gen_perspective.py` | `docs/perspective/reference/**` | `projects/BH/com.inductiveautomation.perspective/**`, gateway themes/icons |
| `gen_scripting.py` | `docs/scripting/reference/**`, `docs/database/reference/**` | `projects/BH/ignition/**`, reports, WebDev, `sql/**` |

A reference tool can declare its own `SOURCES = [...]` (repo-relative globs) to override the defaults.

## `check_docs.py`: What Needs Updating?

```powershell
python wiki/tools/check_docs.py             # report
python wiki/tools/check_docs.py --all       # also list up-to-date pages
python wiki/tools/check_docs.py --strict    # exit 1 if anything is stale (scripts, pre-commit)
```

It reports four things:

1. **Generated reference**: per area, source files changed / added / removed since the last `gen_all.py` (compared by
   hash against the manifest) → rerun `gen_all.py`.
2. **Stale hand-written pages**: pages whose `sources:` files changed after their `last_verified:`. The change time of
   a file is its **last commit date** when it is tracked and clean, otherwise its **modification time** (uncommitted
   edits, untracked and gitignored files such as gateway config).
3. Pages **missing** `sources` or `last_verified`.
4. `sources` entries that **match no file** (renamed or deleted sources).

Example output:

```text
== Generated reference (wiki/tools/manifest/sources.json) ==
  [ok]    perspective: 2210 sources unchanged since 2026-10-23T16:10:02
  [STALE] tags: 1 changed, 0 added, 0 removed since 2026-10-23T16:09:40 -> rerun gen_all.py tags
            changed: gateways/standard/data/config/resources/core/ignition/tag-group/default/PAX_Status/config.json

== Hand-written pages whose sources changed since last_verified ==
  docs/gateway/tag-providers-and-groups.md (last_verified 2026-10-23): 1 source file(s) newer
      2026-10-24 09:12 (mtime) gateways/standard/data/config/resources/core/ignition/tag-group/default/PAX_Status/config.json
```

Note: gateway config files are rewritten by the gateway itself (saves, scans), so their modification time can move
without a real change. When a flagged page is still right, just bump `last_verified`.

## Writing A Reference Tool

- File `wiki/tools/gen_<area>.py`, stdlib only, `main(repo_root)` entry point, optional `SOURCES`.
- Rewrite **only** your own `docs/<area>/reference/**` (delete pages for things that no longer exist).
- Each page: front matter with `generated: true`, the "generated from the project files" note, readable tables, `<details>`
  for long lists, no raw JSON dumps.
- Escape MDX: wrap `{`, `}`, `<`, `>` in code spans or escape them.
- Be deterministic (sorted output) so a rerun with no project change produces no diff.
- Test with `npm run build` (or a partial build, see [The Wiki Service](../infrastructure/wiki-service.md#partial-builds)).

## npm Scripts

| Command (in `wiki/`) | Does |
|---|---|
| `npm start` | Dev server on port 3030 with live reload (no search index) |
| `npm run build` | Production build into `build/` |
| `npm run serve` | Serve `build/` on port 3031 (search works) |
| `npm run gen` | `python -I tools/gen_all.py` |
| `npm run check` | `python -I tools/check_docs.py` |
| `npm run clear` | Delete the Docusaurus cache (`.docusaurus/`) when a build behaves oddly |
