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
