# Boar's Head SCADA Wiki

Docusaurus 3.10.2 site documenting the BH Ignition project (gateway, tags, Perspective, scripting,
database, features, deployment, git workflow). Docs-only, served at `/`, offline full-text search.

## Run

```powershell
cd wiki
npm install          # first time / after package.json changes
npm start            # dev server with live reload: http://localhost:3030 (no search in dev mode)
npm run build        # production build -> build/ (builds the search index)
npm run serve        # serve build/ on http://localhost:3031 (search works)
```

As a container (build + serve, search works):

```powershell
docker compose up -d --build wiki    # http://localhost:3030
docker restart bh-wiki               # rebuild after doc changes
```

## Regenerate And Check

```powershell
python -I wiki/tools/gen_all.py      # rewrite every generated reference page (docs/*/reference/**)
python -I wiki/tools/check_docs.py   # list stale hand-written pages (sources changed since last_verified)
cd wiki; npm run build               # must pass
```

## Layout

| Path | What |
|---|---|
| `docs/` | Pages. One folder per area with `index.md` + `_category_.json`; generated pages under `<area>/reference/` |
| `tools/gen_*.py` | Reference-page tools (stdlib only, `main(repo_root)`), run by `tools/gen_all.py` |
| `tools/check_docs.py` | Staleness check |
| `tools/manifest/sources.json` | Source hashes recorded by `gen_all.py` (commit it) |
| `static/img/` | Logos and screenshots |
| `src/css/custom.css` | Brand colours (red `#B00828`, light `#F3F3F5`, dark `#1E242E`) |
| `docusaurus.config.js` | Site config (search, Mermaid, link checks) |
| `Dockerfile` | The `bh-wiki` container |

## Options

- Strict by default: broken links, anchors and images fail the build. `WIKI_STRICT_LINKS=0` downgrades them to warnings for a draft build only.
- `WIKI_INCLUDE="gateway/**,tags/**"`: build only some folders (intro is always included).
- `DOCUSAURUS_GENERATED_FILES_DIR_NAME=.docusaurus-<name>` + `--out-dir build-<name>`: parallel builds in one checkout.

Conventions for pages (front matter `sources:` / `last_verified:`, style, Title Case): see
`docs/contributing/` (on the site: Contributing).
