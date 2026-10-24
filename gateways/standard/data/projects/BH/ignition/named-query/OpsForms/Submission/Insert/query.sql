INSERT INTO dbo.ops_form_submission
    (form_type, form_date, submitted_by, submitted_name, submitted_at, shift_status, is_abnormal, release_logged,
     open_items, summary, data)
VALUES
    (:formType, CAST(:formDate AS DATE), :submittedBy, :submittedName, :submittedAt, NULLIF(:shiftStatus, ''),
     :isAbnormal, :releaseLogged, :openItems, :summary, :data)
