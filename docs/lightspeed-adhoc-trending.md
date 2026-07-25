# Adhoc + User-Saved Trending (Lightspeed port)

Port of Lightspeed-FrontEnd **AdhocTrend** into project **BH**. Source export:

`Documents/Cursor/Ignition QA/assets/Lightspeed-Frontend/projects/Lightspeed-FrontEnd/`

## Quick start

| URL | View |
|-----|------|
| `/trending` | `98_Configuration/AdhocTrend/Trend` — live/adhoc pens |
| `/trending/saved` | `98_Configuration/AdhocTrend/UserSavedTrendConfig` — load / delete saved configs |

**Session state:** `session.custom.AdhocTrend` (tags, colors, realtime, timeRange, pointCount, chartType, aggregate, start/end dates, trendId/Name, isShared). Max **10** pens.

**Chart:** `kyvislabs.display.apexchart` (Kyvis Labs ApexCharts module — install on the gateway or replace with an IA chart).

**Historian:** pens bind Tag History to `tagPath + "/Value"`. Tag tree is built on startup via `shared.tagsTree.getHistoricalTags()` / `createTree()` (historized AtomicTags named `Value`).

**DB:** **Microsoft SQL Server** connection named **`ignition`**. Run [`sql/adhoc_trend_configs.sql`](../sql/adhoc_trend_configs.sql) once (T-SQL). Lab connection uses Docker host `mssql`, database `ignition`.

---

## Named queries

All under `gateways/standard/data/projects/BH/ignition/named-query/AdhocTrend/`.  
Database attribute on each resource: **`ignition`**.

| Named query path | Type | Params | Used by |
|------------------|------|--------|---------|
| **`AdhocTrend/Select`** | Query | `currentUser` (string) | `UserSavedTrendConfig` table `props.data` ← `{session.props.auth.user.userName}` |
| **`AdhocTrend/SelectTrendConfigById`** | Query | `trendId` (int/text) | `Trend` view binding for reload-by-id |
| **`AdhocTrend/Insert`** | UpdateQuery | `username`, `trendName`, `trendConfig` (JSON as `NVARCHAR(MAX)`), `isShared` | `SaveTrendConfig` when `trendId` empty (`MERGE` upsert on `(username, trend_name)`) |
| **`AdhocTrend/Update`** | UpdateQuery | `trendId`, `trendName`, `trendConfig`, `isShared` | `SaveTrendConfig` when `trendId` set |
| **`AdhocTrend/Delete`** | UpdateQuery | `id` | `UserSavedTrendConfig` message handler `TrendDeleteConfirm` |

### SQL (MSSQL / T-SQL)

**Select** — own + shared:

```sql
SELECT id, trend_name, username, trend_config, is_shared, updated_at
FROM dbo.adhoc_trend_configs
WHERE username = :currentUser OR is_shared = 1
ORDER BY created_at DESC
```

**SelectTrendConfigById:**

```sql
SELECT id, trend_name, username, is_shared, trend_config
FROM dbo.adhoc_trend_configs
WHERE CAST(id AS NVARCHAR(50)) = CAST(:trendId AS NVARCHAR(50))
  AND CAST(:trendId AS NVARCHAR(50)) <> N''
```

**Insert** (upsert via `MERGE`):

```sql
MERGE dbo.adhoc_trend_configs AS target
USING (SELECT :username AS username, :trendName AS trend_name) AS source
ON (target.username = source.username AND target.trend_name = source.trend_name)
WHEN MATCHED THEN
  UPDATE SET trend_config = :trendConfig, is_shared = :isShared,
             updated_at = SYSUTCDATETIME()
WHEN NOT MATCHED THEN
  INSERT (username, trend_name, trend_config, is_shared)
  VALUES (:username, :trendName, :trendConfig, :isShared);
```

**Update / Delete:** see `Update/query.sql`, `Delete/query.sql` (`SYSUTCDATETIME()`, no `::JSONB` casts).

`trend_config` is `NVARCHAR(MAX)` JSON text — full `session.custom.AdhocTrend` (`system.util.jsonEncode` / `jsonDecode`).

---

## Scripting

There is **no** dedicated `AdhocTrend` project library. Behavior is Perspective event scripts + these shared modules (imported from Lightspeed):

| Module | Path | Role |
|--------|------|------|
| **`shared.Alerts`** | `ignition/script-python/shared/Alerts/code.py` | `showAlert(...)` → popup `01_Popups/00_Faceplates/Alerts/Alert`; validation / save errors / delete confirm |
| **`shared.tagsTree`** | `ignition/script-python/shared/tagsTree/code.py` | `getHistoricalTags()`, `getAlarmTags()`, `createTree(paths)` — historized tag discovery helper |
| **`Navigation.Nav`** | `ignition/script-python/Navigation/Nav/code.py` | `navigate(data)` — BH maps AdhocTrend `viewPath` → `/trending` or `/trending/saved`; other payloads keep Lightspeed `/data/...` encoding |

### Call sites (Perspective)

| Location | Scripting |
|----------|-----------|
| `Trend` — Add Tag | `shared.Alerts.showAlert` on duplicate / 10-pen cap |
| `_Assets/SaveTrendConfig` | `from shared import Alerts`; `system.db.runNamedQuery("AdhocTrend/Insert"\|"AdhocTrend/Update", …)` |
| `_Assets/LoadDeleteTrend` — Load | Decode `trend_config` → `session.custom.AdhocTrend`; `Navigation.Nav.navigate({"viewPath": "98_Configuration/AdhocTrend/Trend"})` |
| `_Assets/LoadDeleteTrend` — Delete | `shared.Alerts.showAlert` with `btnActionPrimary` → message `TrendDeleteConfirm` |
| `UserSavedTrendConfig` — `TrendDeleteConfirm` | `system.db.runNamedQuery("AdhocTrend/Delete", {"id": trend_id})` then refresh table |

### Message handlers on `Trend`

`AdhocTrendDeleteRow`, `AdhocTrendDisableRow`, `commitTrendConfig`, `closeAlert`, `AdhocTrendConfigData`, `issueLog` (latter calls `shared.Alerts.contextMenuIssueLog` — needs IssuesLogger view if used).

---

## Files imported

```
ignition/named-query/AdhocTrend/{Select,SelectTrendConfigById,Insert,Update,Delete}/
ignition/script-python/shared/{Alerts,tagsTree}/
ignition/script-python/Navigation/Nav/
com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/
  Trend/, UserSavedTrendConfig/,
  _Assets/{ToolBar,SaveTrendConfig,LoadDeleteTrend,Pen,PenEnable,PenColor,PenDelete}/
com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/{Alert,ContextMenu,Menu}/
com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/Trending/
session-props  → custom.AdhocTrend
page-config    → /trending, /trending/saved
sql/adhoc_trend_configs.sql
```

---

## Known gaps / BH adaptations

1. **`SaveCustomTrend`** is referenced from `SaveTrendConfig` but was **missing** in the Lightspeed export — ignore or remove that embed.
2. Views still use Lightspeed Designer style classes (`Fonts/Label`, etc.). BH CSS-only rule: restyle to Advanced Stylesheet when polishing.
3. `shared.Alerts.contextMenuIssueLog` points at `98_Configuration/IssuesLogger/IssuesLogGenerator` (not imported).
4. Docked `Trending` icon expects Lightspeed header chrome; BH pages are standalone — use `/trending` URL or wire the dock asset later.
5. CoreHistorian stores locally (not SQL Historian). Fine for lab trending; prod may want SqlHistorian later.

---

## Smoke checklist

1. Confirm Gateway → Databases → **`ignition`** is Valid, and History provider **`historian`** exists.
2. Change a few device `Temp/Value` or `Status/Value` tags so OnChange history records samples.
3. Open `/trending`, expand the tag tree (built via `shared.tagsTree.getHistoricalTags()`), add a pen, confirm ApexCharts draws.
4. Save trend → row appears on `/trending/saved`.
5. Load / delete via `LoadDeleteTrend` actions.
