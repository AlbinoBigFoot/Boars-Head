def doGet(request, session):
	# Marker GeoJSON for the globe iframe: a logged-in BH Perspective session in this browser (shared.WebAuth), or an
	# HMI admin login (HTTP Basic, shared.Globe.adminWriter) for tools. docs/security-access.md
	if not shared.WebAuth.perspectiveUser(request):
		if not shared.WebAuth.hasBasicHeader(request):
			return shared.WebAuth.deny(request)
		status, user = shared.Globe.adminWriter(request)
		if status != 200:
			return shared.WebAuth.deny(request, status)
	shared.WebAuth.noStore(request)
	# Read GeoJson from the MapMarkerGeoJson Tag
	geoJSON = system.tag.readBlocking(["[default]_Config/MapMarkerGeoJson"])[0].value
	if geoJSON is not None:
		geoJSON = system.util.jsonEncode(geoJSON.toDict(),5)
		return {'json': geoJSON}
	else:
		return shared.WebAuth.deny(request, 404, "no markers")
