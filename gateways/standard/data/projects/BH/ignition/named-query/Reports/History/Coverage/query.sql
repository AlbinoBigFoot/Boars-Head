-- First history sample per tag (SQL historian 'historian', sqlth_te.created = epoch ms); paths lower-case, '|'-joined
SELECT tagpath, MIN(created) AS first_ms
FROM dbo.sqlth_te
WHERE tagpath IN (SELECT value FROM STRING_SPLIT(:paths, '|'))
GROUP BY tagpath
