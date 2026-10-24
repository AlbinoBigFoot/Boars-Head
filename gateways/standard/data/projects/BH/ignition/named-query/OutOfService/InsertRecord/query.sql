-- New Out Of Service record (shared.OutOfService.setOutOfService, inside its transaction); returns the id.
INSERT INTO dbo.oos_record
    (tag_path, device_name, device_type, site, area, taken_by, taken_name, taken_at, reason, memo, status, is_backfill,
     updated_at)
OUTPUT INSERTED.id
VALUES
    (:tagPath, :deviceName, :deviceType, :site, :area, :takenBy, :takenName, :takenAt, :reason, :memo, :status,
     :isBackfill, :takenAt)
