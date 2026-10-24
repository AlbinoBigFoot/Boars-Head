SELECT v.valve_pk, v.category, v.pid, v.unit_id, v.unit_desc, v.valve_id, v.size, v.valve_type, v.position,
       v.function_service, CAST(COALESCE(c.verified, 0) AS BIT) AS verified, c.verified_by, c.verified_date, c.notes,
       c.updated_by, c.updated_at
FROM dbo.ops_pid_valve v
LEFT JOIN dbo.ops_pid_check c ON c.valve_pk = v.valve_pk AND c.cycle_id = :cycleId
WHERE v.valve_pk = :valvePk
