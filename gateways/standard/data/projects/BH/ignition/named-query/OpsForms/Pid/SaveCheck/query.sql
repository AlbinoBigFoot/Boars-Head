-- upsert the check of this cycle + append the audit row; only while the cycle is open
IF EXISTS (SELECT 1 FROM dbo.ops_pid_cycle WHERE id = :cycleId AND status = N'Open')
BEGIN
    MERGE dbo.ops_pid_check AS t
    USING (SELECT :cycleId AS cycle_id, :valvePk AS valve_pk) AS s
        ON t.cycle_id = s.cycle_id AND t.valve_pk = s.valve_pk
    WHEN MATCHED THEN UPDATE SET
        verified = :verified, verified_by = NULLIF(:verifiedBy, ''),
        verified_date = TRY_CAST(NULLIF(:verifiedDate, '') AS DATE), notes = NULLIF(:notes, ''),
        updated_by = :user, updated_at = :now
    WHEN NOT MATCHED THEN INSERT (cycle_id, valve_pk, verified, verified_by, verified_date, notes, updated_by, updated_at)
        VALUES (:cycleId, :valvePk, :verified, NULLIF(:verifiedBy, ''), TRY_CAST(NULLIF(:verifiedDate, '') AS DATE),
                NULLIF(:notes, ''), :user, :now);
    INSERT INTO dbo.ops_pid_check_log (cycle_id, valve_pk, verified, verified_by, verified_date, notes, updated_by, updated_at)
    VALUES (:cycleId, :valvePk, :verified, NULLIF(:verifiedBy, ''), TRY_CAST(NULLIF(:verifiedDate, '') AS DATE),
            NULLIF(:notes, ''), :user, :now);
END
