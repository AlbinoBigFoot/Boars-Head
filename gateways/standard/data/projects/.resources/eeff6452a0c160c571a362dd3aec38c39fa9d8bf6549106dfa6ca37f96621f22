UPDATE dbo.adhoc_trend_configs
SET
    trend_name = :trendName,
    is_shared = :isShared,
    trend_config = :trendConfig,
    updated_at = SYSUTCDATETIME()
WHERE
    id = :trendId
