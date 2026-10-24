SELECT unit_id, MAX(unit_desc) AS unit_desc, COUNT(*) AS n
FROM dbo.ops_pid_valve
WHERE (:category = '' OR category = :category)
GROUP BY unit_id
ORDER BY MIN(sort_order)
