-- Area / Device pairs that have ever been out of service (Scope picker of the Out Of Service source)
SELECT area, device_name AS device, COUNT(*) AS cnt FROM dbo.oos_record
WHERE COALESCE(area, N'') <> N'' GROUP BY area, device_name ORDER BY area, device_name
