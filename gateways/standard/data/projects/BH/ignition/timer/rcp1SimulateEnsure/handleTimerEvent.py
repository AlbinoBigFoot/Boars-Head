def handleTimerEvent():
	"""Boot/periodic ensure: Memory Simulate does not fire tag-change at startup."""
	try:
		shared.Rcp1Simulate.ensureApplied()
	except Exception as e:
		system.util.getLogger("shared.Rcp1Simulate").warn(
			"rcp1SimulateEnsure timer failed: %s" % str(e)
		)
