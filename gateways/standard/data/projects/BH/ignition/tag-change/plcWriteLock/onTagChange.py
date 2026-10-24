def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	# plc-write-lock (.cursor/tasks/plc-write-lock): readOnly = Locked on every [default]_RCP1_ tag and PLC / Devices UDT OPC member; fail-safe locked on
	# bad / null and on gateway startup. Logic + gateway log: shared.PlcWriteLock
	shared.PlcWriteLock.onLockChange(initialChange, newValue, event)
