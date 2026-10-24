SELECT v.valve_pk, v.category, v.pid, v.unit_id, v.unit_desc, v.valve_id, v.size, v.valve_type, v.position,
       v.function_service, CAST(COALESCE(c.verified, 0) AS BIT) AS verified, c.verified_by, c.verified_date, c.notes,
       c.updated_by, c.updated_at
FROM dbo.ops_pid_valve v
LEFT JOIN dbo.ops_pid_check c ON c.valve_pk = v.valve_pk AND c.cycle_id = :cycleId
WHERE (:category = '' OR v.category = :category)
  AND (:unit = '' OR v.unit_id = :unit)
  AND (:search = ''
       OR v.valve_id LIKE '%' + :search + '%' OR v.unit_id LIKE '%' + :search + '%'
       OR v.function_service LIKE '%' + :search + '%' OR v.size LIKE '%' + :search + '%'
       OR v.valve_type LIKE '%' + :search + '%' OR c.notes LIKE '%' + :search + '%'
       OR c.verified_by LIKE '%' + :search + '%')
  AND (:show = 'All'
       OR (:show = 'Remaining' AND COALESCE(c.verified, 0) = 0)
       OR (:show = 'Verified' AND c.verified = 1)
       OR (:show = 'Discrepancies' AND COALESCE(c.notes, '') <> '')
       OR (:show = 'Incomplete' AND c.verified = 1 AND COALESCE(c.verified_by, '') = ''))
ORDER BY v.sort_order
