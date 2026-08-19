# Alarm rollup rebuild for Config/_Alarms (ported from LGChem / Citadel Rebuild script).
# Called from UDT member Rebuild valueChanged via: shared.Alarms.rebuild(tagPath)

import re

logger = system.util.getLogger("shared.Alarms")

# Top-level tag folders used as Device Type (plant equipment families).
DEVICE_TYPE_FOLDERS = (
	"Evaporators",
	"Compressors",
	"Pumps",
	"ExhaustFans",
	"CoolingTowers",
)


def deviceTypeSourceFilter(selected):
	"""
	Build Alarm Status / Alarm Journal source filter from a multi-select Device Type list.

	Empty / None selection => '*' (show all device types).
	One or more selections => comma-delimited '*Folder*' wildcards (OR match).
	Device types map to tag path folders under [default], e.g. Evaporators → *Evaporators*.
	"""
	if selected is None or selected == "":
		return "*"

	items = []
	if isinstance(selected, basestring):
		if str(selected).strip():
			items = [str(selected).strip()]
	else:
		try:
			for item in selected:
				if item is None:
					continue
				text = str(item).strip()
				if text:
					items.append(text)
		except TypeError:
			text = str(selected).strip()
			if text:
				items = [text]

	if not items:
		return "*"

	return ",".join(["*%s*" % folder for folder in items])


def sourceWildcard(tagPath):
	"""Alarm Status source filter for a device tag path (same shape as the faceplate table)."""
	raw = str(tagPath or "").strip()
	if not raw:
		return None
	provider = "default"
	path = raw
	if raw.startswith("["):
		end = raw.find("]")
		if end > 1:
			provider = raw[1:end]
			path = raw[end + 1 :]
	path = path.lstrip("/")
	if not path:
		return None
	return "prov:%s:/tag:%s*" % (provider, path)


def _alarmEventId(event):
	for getter in (
		lambda e: e.getId(),
		lambda e: e.get("EventId") if hasattr(e, "get") else None,
		lambda e: getattr(e, "id", None),
	):
		try:
			value = getter(event)
			if value not in (None, ""):
				return str(value)
		except:
			pass
	return None


def _collectUnackedIds(sourceFilter):
	ids = []
	if not sourceFilter:
		return ids
	try:
		events = system.alarm.queryStatus(
			source=[sourceFilter],
			state=["ActiveUnacked", "ClearUnacked"],
		)
	except:
		return ids
	if events is None:
		return ids
	try:
		rowCount = events.getRowCount()
		names = list(events.getColumnNames()) if hasattr(events, "getColumnNames") else []
		col = "EventId" if "EventId" in names else (names[0] if names else None)
		if col is not None:
			for i in range(rowCount):
				value = events.getValueAt(i, col)
				if value not in (None, ""):
					ids.append(str(value))
			return ids
	except:
		pass
	try:
		for event in events:
			eid = _alarmEventId(event)
			if eid:
				ids.append(eid)
	except:
		pass
	return ids


def acknowledgeForTag(tagPath, username="", notes="Faceplate Ack / Reset"):
	"""Acknowledge unacked Ignition alarms associated with this device (same set as the faceplate table)."""
	filters = []
	primary = sourceWildcard(tagPath)
	if primary:
		filters.append(primary)
	raw = str(tagPath or "").strip()
	pathOnly = raw[raw.find("]") + 1:].lstrip("/") if raw.startswith("[") else raw.lstrip("/")
	if pathOnly:
		fallback = "*%s*" % pathOnly
		if fallback not in filters:
			filters.append(fallback)
	for member in ("Alm_IOFault", "Alm_FullStall", "Alm_TransitStall", "Alm_IntlkTrip"):
		memberPath = raw.rstrip("/") + "/" + member + "/Value"
		try:
			cfg = system.tag.getConfiguration(memberPath, False)[0]
			srcTag = cfg.get("sourceTagPath")
			wild = sourceWildcard(srcTag) if srcTag else None
			if wild and wild not in filters:
				filters.append(wild)
		except:
			pass
	ids = []
	seen = set()
	for src in filters:
		for eid in _collectUnackedIds(src):
			if eid not in seen:
				seen.add(eid)
				ids.append(eid)
	if not ids:
		return 0
	user = str(username or "")
	try:
		system.alarm.acknowledge(ids, notes or "Faceplate Ack / Reset", user)
	except:
		logger.warn("acknowledge failed for %s (%d events)" % (raw, len(ids)))
		raise
	return len(ids)


def rebuild(rebuildTagPath):
	"""
	Rebuild expression tags under an _Alarms UDT instance.
	rebuildTagPath should end with /_Alarms/Rebuild.
	"""
	path = str(rebuildTagPath).replace("/Rebuild", "")
	manualBuildTagPath = path + "/ManualBuild"

	try:
		if system.tag.readBlocking([manualBuildTagPath])[0].value:
			system.tag.writeBlocking([rebuildTagPath], [False])
			return
	except:
		pass

	activeTagPath = path + "/_Active.Expression"
	unackTagPath = path + "/_Unack.Expression"
	activeHighTagPath = path + "/_ActiveHighPriority.Expression"
	unackHighTagPath = path + "/_UnackHighPriority.Expression"
	criticalCountTagPath = path + "/_CriticalCount.Expression"
	highCountTagPath = path + "/_HighCount.Expression"
	mediumCountTagPath = path + "/_MediumCount.Expression"

	pathTagPath = path + "/Path"
	recursiveTagPath = path + "/Recursive"
	tagNameTagPath = path + "/TagName"
	parentPath = path.replace("/_Alarms", "")

	try:
		tagValues = system.tag.readBlocking([pathTagPath, recursiveTagPath, tagNameTagPath])
		searchPath = tagValues[0].value if tagValues[0].value else parentPath
		searchPath = [tag.strip() for tag in str(searchPath).split(",") if str(tag).strip()]
		recursive = bool(tagValues[1].value) if tagValues[1].value is not None else False
		tagName = str(tagValues[2].value) if tagValues[2].value is not None else ""
	except Exception as e:
		logger.warn("Alarms.rebuild config read failed: %s" % str(e))
		system.tag.writeBlocking([rebuildTagPath], [False])
		return

	tagsList = []
	alarmTagsList = []
	folderList = []
	udtList = []

	for tag in searchPath:
		try:
			filt = {"recursive": recursive}
			if tagName:
				filt["name"] = tagName
			for ea in system.tag.browse(tag, filter=filt):
				try:
					tagsList.append(str(ea["fullPath"]))
				except:
					try:
						tagsList.append(str(ea.getFullPath()))
					except:
						pass
		except Exception as e:
			logger.warn("browse failed for %s: %s" % (tag, str(e)))

	for browsePath in tagsList:
		try:
			tag_info = system.tag.getConfiguration(browsePath)[0]
		except:
			continue

		if "alarms" in tag_info.keys() and tag_info.get("alarms") and len(tag_info["alarms"]) > 0:
			alarmTagsList.append(str(browsePath))

		tt = str(tag_info.get("tagType", ""))
		name = str(tag_info.get("name", ""))

		if tt == "Folder":
			try:
				for child in system.tag.browse(browsePath).getResults():
					cname = str(child.getName()) if hasattr(child, "getName") else str(child["name"])
					if "_Alarms" in cname:
						folderList.append(str(browsePath))
						break
			except:
				pass

		if tt == "UdtInstance" and name != "_Alarms":
			try:
				for child in system.tag.browse(browsePath).getResults():
					cname = str(child.getName()) if hasattr(child, "getName") else str(child["name"])
					if "_Alarms" in cname:
						udtList.append(str(browsePath))
						break
			except:
				pass

	activeList = [tag + "/Alarms.HasActive" for tag in alarmTagsList]
	activeHighList = [tag + "/Alarms.HighestActivePriority" for tag in alarmTagsList]
	unackList = [tag + "/Alarms.HasUnacknowledged" for tag in alarmTagsList]
	unackHighList = [tag + "/Alarms.HighestUnackedPriority" for tag in alarmTagsList]

	activeList += [tag + "/_Alarms/_Active" for tag in udtList + folderList]
	activeHighList += [tag + "/_Alarms/_ActiveHighPriority" for tag in udtList + folderList]
	unackList += [tag + "/_Alarms/_Unack" for tag in udtList + folderList]
	unackHighList += [tag + "/_Alarms/_UnackHighPriority" for tag in udtList + folderList]

	activeExpression = " ||\n".join(["{" + tag + "}" for tag in activeList])
	activeHighExpression = "min(" + ",\n".join(["{" + tag + "}" for tag in activeHighList]) + ",\n10)" if activeHighList else "10"
	unackExpression = " ||\n".join(["{" + tag + "}" for tag in unackList])
	unackHighExpression = "min(" + ",\n".join(["{" + tag + "}" for tag in unackHighList]) + ",\n10)" if unackHighList else "10"

	stripped = re.sub(r"\[.*?\]", "", "/".join(str(parentPath).split("/")[0:-1])) if "/" in str(parentPath) else re.sub(r"\[.*?\]", "", str(parentPath))

	criticalCountExpression = (
		"toInt(runScript(\"len(system.alarm.queryStatus(state=['ActiveUnacked','ActiveAcked'],"
		"source=['*" + stripped + "*'],all_properties=[('Priority','=','Critical')]))\"))"
	)
	highCountExpression = (
		"toInt(runScript(\"len(system.alarm.queryStatus(state=['ActiveUnacked','ActiveAcked'],"
		"source=['*" + stripped + "*'],all_properties=[('Priority','=','High')]))\"))"
	)
	mediumCountExpression = (
		"toInt(runScript(\"len(system.alarm.queryStatus(state=['ActiveUnacked','ActiveAcked'],"
		"source=['*" + stripped + "*'],all_properties=[('Priority','=','Medium')]))\"))"
	)

	if not activeExpression:
		activeExpression = False
		unackExpression = False
		activeHighExpression = 10
		unackHighExpression = 10

	# Match LGChem: currently not tracking unack in expressions
	unackExpression = False
	unackHighExpression = 10

	expressionPaths = [
		activeTagPath,
		unackTagPath,
		activeHighTagPath,
		unackHighTagPath,
		criticalCountTagPath,
		highCountTagPath,
		mediumCountTagPath,
	]
	expressions = [
		activeExpression,
		unackExpression,
		activeHighExpression,
		unackHighExpression,
		criticalCountExpression,
		highCountExpression,
		mediumCountExpression,
	]

	try:
		system.tag.writeBlocking(expressionPaths, expressions)
		logger.info("Rebuilt alarm expressions for %s (%d alarm tags, %d child _Alarms)" % (
			path, len(alarmTagsList), len(udtList) + len(folderList)
		))
	except Exception as e:
		logger.error("Failed writing alarm expressions for %s: %s" % (path, str(e)))

	system.tag.writeBlocking([rebuildTagPath], [False])
