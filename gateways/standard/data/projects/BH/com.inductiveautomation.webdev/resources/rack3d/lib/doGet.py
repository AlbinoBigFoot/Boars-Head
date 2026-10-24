def doGet(request, session):
	# PLC Rack 3D static files (whitelist in shared.Rack3d.FILES): three.js r170 (MIT), rack3d.js / .css, demo state.
	# Logged-in BH Perspective session only (shared.WebAuth). .cursor/tasks/plc-rack-3d/build.py - docs/plc-rack-3d.md
	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	name = str(request.get("remainingPath") or "").strip("/")
	r = shared.Rack3d.serveFile(request, name)
	if r is None:
		return shared.WebAuth.deny(request, 404, "not found")
	try:
		request["servletResponse"].setHeader("Cache-Control", "private, max-age=300")
	except:
		pass
	return r
