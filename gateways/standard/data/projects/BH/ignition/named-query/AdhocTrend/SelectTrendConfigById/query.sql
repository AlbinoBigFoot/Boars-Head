SELECT
    id,
    trend_name,
    username,
    is_shared,
    trend_config
FROM
    dbo.adhoc_trend_configs
WHERE
    -- Compare as strings so blank/empty trendId does not error
    CAST(id AS NVARCHAR(50)) = CAST(:trendId AS NVARCHAR(50))
    AND CAST(:trendId AS NVARCHAR(50)) <> N''
