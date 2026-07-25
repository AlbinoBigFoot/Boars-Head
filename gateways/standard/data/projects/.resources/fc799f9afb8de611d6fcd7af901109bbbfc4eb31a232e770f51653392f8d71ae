def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	"""
	Lightspeed-style Overview rebuild trigger.
	When any watched Overview/.../Rebuild tag goes True, rebuild Instances,
	DeviceCount, and ActiveAlarmCount via shared.Overview.
	"""
	# Run on startup too so counts seed after gateway restart / scan
	try:
		val = newValue.getValue() if hasattr(newValue, "getValue") else newValue
	except:
		val = newValue

	if val is not True and val != 1:
		return

	tagPath = None
	try:
		tagPath = str(event.getTagPath()) if event is not None and hasattr(event, "getTagPath") else None
	except:
		tagPath = None
	if not tagPath:
		try:
			tagPath = str(event.tagPath)
		except:
			pass
	if not tagPath:
		return

	shared.Overview.rebuildFromRebuildTag(tagPath)
