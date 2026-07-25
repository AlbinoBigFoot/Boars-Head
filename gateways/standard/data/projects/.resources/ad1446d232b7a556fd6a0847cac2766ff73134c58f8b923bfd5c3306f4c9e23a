SELECT
    id,
    trend_name,
    username,
    trend_config,
    is_shared,
    updated_at
FROM
    dbo.adhoc_trend_configs
WHERE
    is_shared = 1
    OR username = COALESCE(NULLIF(:currentUser, N''), N'anonymous')
ORDER BY
    created_at DESC
