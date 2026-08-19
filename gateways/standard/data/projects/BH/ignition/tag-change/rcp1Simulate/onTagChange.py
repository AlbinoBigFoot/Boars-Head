def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	"""
	RCP1 Simulate toggle.
	When [default]RCP1/Simulate changes, reconfigure all RCP1 AtomicTags
	(except Simulate) between OPC UA and Memory via shared.Rcp1Simulate.

	Note: Simulate is a Memory tag — Gateway Tag Change does NOT fire at boot
	for unchanged Memory values. Boot apply is handled by timer rcp1SimulateEnsure
	and shared.Rcp1Simulate.ensureApplied() (also called from ValveCommands).
	"""
	try:
		val = newValue.getValue() if hasattr(newValue, "getValue") else newValue
	except:
		val = newValue

	simulate = False
	try:
		simulate = bool(val)
	except:
		simulate = False

	shared.Rcp1Simulate.applySimulate(simulate)
