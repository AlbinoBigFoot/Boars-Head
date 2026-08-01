def doGet(request, session):
	# Read GeoJson from the MapMarkerGeoJson Tag
	geoJSON = system.tag.readBlocking(["[default]_Config/MapMarkerGeoJson"])[0].value
	if geoJSON is not None:
		geoJSON = system.util.jsonEncode(geoJSON.toDict(),5)
		return {'json': geoJSON}
	else:
		return geoJSON