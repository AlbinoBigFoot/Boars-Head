DELETE FROM dbo.adhoc_trend_configs
WHERE id = :id
    AND (is_locked = 0 OR :isAdmin = 1)
