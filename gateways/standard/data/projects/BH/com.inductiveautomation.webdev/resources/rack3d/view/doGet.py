def doGet(request, session):
	# PLC Rack 3D page (iframe on /operations/plcs/:plc/3d): only for a logged-in BH Perspective session in this browser
	# (shared.WebAuth). .cursor/tasks/plc-rack-3d/build.py - docs/plc-rack-3d.md
	if not shared.WebAuth.perspectiveUser(request):
		try:
			request["servletResponse"].setStatus(401)
			request["servletResponse"].setHeader("Cache-Control", "no-store")
		except:
			pass
		return {"html": "<!doctype html><meta charset=utf-8><title>Login Required</title><body style='font:14px sans-serif;"
		                "padding:24px'>Login Required. Open this page from the BH Perspective client.</body>"}
	shared.WebAuth.noStore(request)
	r = shared.Rack3d.serveFile(request, "view.html")
	if r is None:
		return shared.WebAuth.deny(request, 404, "not found")
	return r
