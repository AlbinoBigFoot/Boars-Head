SELECT v.category, MIN(v.category_order) AS category_order, COUNT(*) AS total,
       SUM(CASE WHEN c.verified = 1 THEN 1 ELSE 0 END) AS verified,
       SUM(CASE WHEN COALESCE(c.notes, '') <> '' THEN 1 ELSE 0 END) AS disc,
       SUM(CASE WHEN c.verified = 1 AND COALESCE(c.verified_by, '') = '' THEN 1 ELSE 0 END) AS incomplete
FROM dbo.ops_pid_valve v
LEFT JOIN dbo.ops_pid_check c ON c.valve_pk = v.valve_pk AND c.cycle_id = :cycleId
GROUP BY v.category
ORDER BY MIN(v.category_order)
