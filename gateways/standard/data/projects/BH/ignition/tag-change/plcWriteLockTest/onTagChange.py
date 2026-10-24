def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	# plc-write-lock (.cursor/tasks/plc-write-lock): readOnly = Locked on every TEST tag (memory, never the PLC); fail-safe locked on
	# bad / null. Logic + gateway log: shared.PlcWriteLock
	shared.PlcWriteLock.onTestChange(initialChange, newValue, event)
