---
title: Page Conventions
sidebar_position: 1
description: Front matter, folders, file names, links, images and generated pages in this wiki.
sources:
  - wiki/docusaurus.config.js
  - wiki/tools/check_docs.py
  - wiki/tools/gen_all.py
last_verified: 2026-10-23
---

# Page Conventions

## Front Matter

Every **hand-written** page starts with:

```yaml
---
title: Tag Providers And Tag Groups          # Title Case; shown in the sidebar and the browser tab
sidebar_position: 4                         # order inside its folder (optional)
description: One sentence for search results and link previews.
sources:                                    # repo-relative files or globs this page describes
  - gateways/standard/data/config/resources/core/ignition/tag-group/**/config.json
  - docs/rcp1-pax-inventory.md
last_verified: 2026-10-23                   # the day you last checked the page against those sources
---
```

- **`sources`** is what makes staleness detection work: `check_docs.py` flags the page when any listed file changed
  after `last_verified`. List the files a reader would have to re-read to check the page: config files, scripts,
  the `docs/*.md` notes. Globs are fine (`**`, `*`). A page with no sources is listed as a hygiene problem.
- **`last_verified`** is a date (`YYYY-MM-DD`, covers the whole day) or a date-time (`2026-10-23T14:30`). Bump it only
  after you actually re-checked the page.

**Generated** pages carry `generated: true` and the banner below; `check_docs.py` skips them (their freshness is
tracked by the source manifest):

```markdown
:::note
This reference page is generated from the project files.
:::
```

## Folders And Files

- One folder per area (`docs/gateway/`, `docs/tags/` ...), each with an `index.md` (the folder's landing page, URL
  `/gateway`) and a `_category_.json`:

```json
{ "label": "Gateway", "position": 3, "link": { "type": "doc", "id": "gateway/index" } }
```

- File names are lowercase-hyphenated (`tag-providers-and-groups.md`); the URL is the path without `.md`.
- Generated pages live in a `reference/` subfolder that only the reference tools write.
- **A `_category_.json` link to a doc id that doesn't exist breaks the whole build.** Write `index.md` first.

## Links

- Link with **relative paths to `.md` files**: `[Tag Groups](../gateway/tag-providers-and-groups.md#tag-groups)`.
  Docusaurus checks them at build time and they work in a plain Markdown viewer too.
- Anchors are the heading text lowercased with punctuation removed and spaces as hyphens
  (`## Why These Rates (2026-10-23)` → `#why-these-rates-2026-10-23`).
- Link to a folder's `index.md` when you don't know the exact page in someone else's area.
- External links: full URLs. Never link to SecureLink, VPN or credential pages.

## Images

- Put them in `wiki/static/img/<area>/name.png` and reference them as `/img/<area>/name.png`.
- Crop to what matters, around 1366 px wide. Mask user names and anything personal or secret before saving.
- Always write alt text: `![Connections > Devices with RCP1 connected](/img/gateway/device-connections.png)`.
- Good sources: `verify-screenshots/**` (before/after captures) and new read-only captures.

## Diagrams

Use Mermaid fenced blocks (` ```mermaid `). Keep node labels short; avoid `<`, `>` and `&` in labels (write `PORT`
rather than `<port>`).

## MDX Gotchas

Pages are MDX: outside code, `{`, `}` and `<` start JSX. Put tag paths, expressions and anything with braces or angle
brackets in `code spans` or code blocks: `` `{view.custom.mode}` ``, `` `<device>.Enabled` ``.
