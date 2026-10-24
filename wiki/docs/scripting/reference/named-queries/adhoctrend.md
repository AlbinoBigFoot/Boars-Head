---
title: "Named Queries: AdhocTrend"
sidebar_label: "AdhocTrend"
description: "Named queries under AdhocTrend/: SQL, parameters and callers."
generated: true
custom_edit_url: null
---

:::note

:::

Designer: **Project Browser > Data > Named Queries > AdhocTrend**. Files: `gateways/standard/data/projects/BH/ignition/named-query/AdhocTrend/<Query>/query.sql + resource.json`.

| Query | Type | Parameters | Callers |
|---|---|---|---|
| [`AdhocTrend/Delete`](#adhoctrend-delete) | `UpdateQuery` | `id, isAdmin` | 1 |
| [`AdhocTrend/Insert`](#adhoctrend-insert) | `UpdateQuery` | `username, trendName, isShared, trendConfig` | 1 |
| [`AdhocTrend/Select`](#adhoctrend-select) | `Query` | `currentUser` | 1 |
| [`AdhocTrend/SelectTrendConfigById`](#adhoctrend-selecttrendconfigbyid) | `Query` | `trendId` | 1 |
| [`AdhocTrend/Update`](#adhoctrend-update) | `UpdateQuery` | `trendId, trendName, trendConfig, isShared, isAdmin` | 1 |

## AdhocTrend/Delete {#adhoctrend-delete}

| Setting | Value |
|---|---|
| Path (what callers pass) | `AdhocTrend/Delete` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:id` | Parameter | `Int4` |
| `:isAdmin` | Parameter | `Boolean` |

```sql
DELETE FROM dbo.adhoc_trend_configs
WHERE id = :id
    AND (is_locked = 0 OR :isAdmin = 1)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/UserSavedTrendConfig` | view | `root message handler TrendDeleteConfirm` |

## AdhocTrend/Insert {#adhoctrend-insert}

| Setting | Value |
|---|---|
| Path (what callers pass) | `AdhocTrend/Insert` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:username` | Parameter | `String` |
| `:trendName` | Parameter | `String` |
| `:isShared` | Parameter | `Boolean` |
| `:trendConfig` | Parameter | `String` |

```sql
MERGE dbo.adhoc_trend_configs AS target
USING (
    SELECT
        :username AS username,
        :trendName AS trend_name
) AS source
ON (
    target.username = source.username
    AND target.trend_name = source.trend_name
)
WHEN MATCHED THEN
    UPDATE SET
        trend_config = :trendConfig,
        is_shared = :isShared,
        updated_at = SYSUTCDATETIME()
WHEN NOT MATCHED THEN
    INSERT (username, trend_name, trend_config, is_shared)
    VALUES (:username, :trendName, :trendConfig, :isShared);
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` | view | `root/Buttons/Save event component.onActionPerformed` |

## AdhocTrend/Select {#adhoctrend-select}

| Setting | Value |
|---|---|
| Path (what callers pass) | `AdhocTrend/Select` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:currentUser` | Parameter | `String` |

```sql
SELECT

    id,

    trend_name,

    username,

    trend_config,

    is_shared,
    is_locked,

    updated_at

FROM

    dbo.adhoc_trend_configs

WHERE

    is_shared = 1

    OR username = COALESCE(NULLIF(:currentUser, N''), N'anonymous')

ORDER BY

    created_at DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/UserSavedTrendConfig` | view | `root/TableContainer/Table binding props.data` |

## AdhocTrend/SelectTrendConfigById {#adhoctrend-selecttrendconfigbyid}

| Setting | Value |
|---|---|
| Path (what callers pass) | `AdhocTrend/SelectTrendConfigById` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:trendId` | Parameter | `Int4` |

```sql
SELECT
    id,
    trend_name,
    username,
    is_shared,
    is_locked,
    trend_config
FROM
    dbo.adhoc_trend_configs
WHERE
    -- Compare as strings so blank/empty trendId does not error
    CAST(id AS NVARCHAR(50)) = CAST(:trendId AS NVARCHAR(50))
    AND CAST(:trendId AS NVARCHAR(50)) <> N''
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.dbTrendConfig` |

## AdhocTrend/Update {#adhoctrend-update}

| Setting | Value |
|---|---|
| Path (what callers pass) | `AdhocTrend/Update` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:trendId` | Parameter | `Int4` |
| `:trendName` | Parameter | `String` |
| `:trendConfig` | Parameter | `String` |
| `:isShared` | Parameter | `Boolean` |
| `:isAdmin` | Parameter | `Boolean` |

```sql
UPDATE dbo.adhoc_trend_configs
SET
    trend_name = :trendName,
    is_shared = :isShared,
    trend_config = :trendConfig,
    updated_at = SYSUTCDATETIME()
WHERE
    id = :trendId
    AND (is_locked = 0 OR :isAdmin = 1)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` | view | `root/Buttons/Save event component.onActionPerformed` |
