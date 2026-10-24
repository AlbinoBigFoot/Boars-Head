-- History start of the live (non-retired) history row per tag (sqlth_te.created, epoch ms): the report ignores the
-- hours before it (the historian returns 0 for them). Paths lower-case, '|'-joined.
SELECT tagpath, MIN(created) AS first_ms
FROM dbo.sqlth_te
WHERE retired IS NULL AND tagpath IN (SELECT value FROM STRING_SPLIT(:paths, '|'))
GROUP BY tagpath
