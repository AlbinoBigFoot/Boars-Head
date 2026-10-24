"""
Faceplate Trend tab defaults.

	* defaultPens - pens preselected when a device faceplate's Trend tab opens (mirrors the FT trend displays)
"""


def defaultPens(tagPath):
	"""Full tag paths to preselect on the faceplate Trend tab for tagPath ([] = none).

	Sensors: the PV (Value/Value).
	Tanks (FT HTR-SP / LTR-SP "Level And Pump Pressure"): vessel level, plus the recirculator pumps pressure
	(Sensors/<H|L>SL-Pumps Pressure) when the tank has pumps (HPR has none).
	"""
	p = str(tagPath or "").rstrip("/")
	# PLC-mapped devices (pax-bindings): their historized PlantPAx members. Tanks follow FT HTR-SP / LTR-SP
	# "Level And Pump Pressure": vessel level + the <H|L>SL pumps pressure sensor (SYS_PT5 / SYS_PT4).
	try:
		paxKey = shared.Pax.part(p)
	except:
		paxKey = ''
	if paxKey == 'Motor':
		return [p + '/Motor/Val_Sts', p + '/RunTime/Val_TotRunHrs']
	if paxKey == 'Valve':
		return [p + '/Valve/Val_Sts']
	if paxKey == 'CG':   # zone air temp (CG_ZAT P_AIn) + the defrost step time left
		return [p + '/ZAT/Val', p + '/CG/Val_TimeLeft']
	if paxKey == 'Comp':   # FT (STELLAR)Comp Trend pens
		return [p + '/Comp/' + m for m in ('SucP', 'SucT', 'DisP', 'DisT', 'OilP', 'OilT', 'SVP', 'Rung')]
	if paxKey == 'AIn':
		return [p + '/AIn/Val']
	if paxKey == 'AInRef':
		return []   # the owning device (e.g. the CSV tank) historizes this transmitter
	if paxKey == 'Tank':
		pens = [p + '/LvlAIn/Val']
		if "/Tanks/" in p:
			root, name = p.split("/Tanks/", 1)
			sensor = root + "/Sensors/" + name[:1] + "SL-Pumps Pressure"
			try:
				if system.tag.exists(root + "/Pumps/" + name[:-1] + "LR-Pump 1") and shared.Pax.part(sensor) == 'AIn':
					pens.append(sensor + '/AIn/Val')
			except:
				pass
		return pens
	# PLC-mapped devices (pax-bindings): their historized PlantPAx members. Tanks follow FT HTR-SP / LTR-SP
	# "Level And Pump Pressure": vessel level + the <H|L>SL pumps pressure sensor (SYS_PT5 / SYS_PT4).
	try:
		paxKey = shared.Pax.part(p)
	except:
		paxKey = ''
	if paxKey == 'Motor':
		return [p + '/Motor/Val_Sts', p + '/RunTime/Val_TotRunHrs']
	if paxKey == 'Valve':
		return [p + '/Valve/Val_Sts']
	if paxKey == 'Comp':   # FT (STELLAR)Comp Trend pens
		return [p + '/Comp/' + m for m in ('SucP', 'SucT', 'DisP', 'DisT', 'OilP', 'OilT', 'SVP', 'Rung')]
	if paxKey == 'AIn':
		return [p + '/AIn/Val']
	if paxKey == 'AInRef':
		return []   # the owning device (e.g. the CSV tank) historizes this transmitter
	if paxKey == 'Tank':
		pens = [p + '/LvlAIn/Val']
		if "/Tanks/" in p:
			root, name = p.split("/Tanks/", 1)
			sensor = root + "/Sensors/" + name[:1] + "SL-Pumps Pressure"
			try:
				if system.tag.exists(root + "/Pumps/" + name[:-1] + "LR-Pump 1") and shared.Pax.part(sensor) == 'AIn':
					pens.append(sensor + '/AIn/Val')
			except:
				pass
		return pens
	# PLC-mapped devices (pax-bindings): their historized PlantPAx members. Tanks follow FT HTR-SP / LTR-SP
	# "Level And Pump Pressure": vessel level + the <H|L>SL pumps pressure sensor (SYS_PT5 / SYS_PT4).
	try:
		paxKey = shared.Pax.part(p)
	except:
		paxKey = ''
	if paxKey == 'Motor':
		return [p + '/Motor/Val_Sts', p + '/RunTime/Val_TotRunHrs']
	if paxKey == 'Valve':
		return [p + '/Valve/Val_Sts']
	if paxKey == 'AIn':
		return [p + '/AIn/Val']
	if paxKey == 'AInRef':
		return []   # the owning device (e.g. the CSV tank) historizes this transmitter
	if paxKey == 'Tank':
		pens = [p + '/LvlAIn/Val']
		if "/Tanks/" in p:
			root, name = p.split("/Tanks/", 1)
			sensor = root + "/Sensors/" + name[:1] + "SL-Pumps Pressure"
			try:
				if system.tag.exists(root + "/Pumps/" + name[:-1] + "LR-Pump 1") and shared.Pax.part(sensor) == 'AIn':
					pens.append(sensor + '/AIn/Val')
			except:
				pass
		return pens
	if "/Tanks/" in p:
		root, name = p.split("/Tanks/", 1)
		pens = [p + "/Level/Value"]
		pump = root + "/Pumps/" + name[:-1] + "LR-Pump 1"
		try:
			has_pumps = system.tag.exists(pump)
		except:
			has_pumps = False
		if has_pumps:
			pens.append(root + "/Sensors/" + name[:1] + "SL-Pumps Pressure/Value/Value")
		return pens
	# Sensors (FT P_AIn trend): the PV; the Trend tab adds its HH / H / L / LL lines + EU range.
	try:
		sensor = str(system.tag.getConfiguration(p, False)[0].get('typeId') or '') == 'Devices/Sensor'
	except:
		sensor = False
	if sensor:
		return [p + "/Value/Value"]
	return []
