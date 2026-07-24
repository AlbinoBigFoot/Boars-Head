# Multistate / boolean label helpers for Perspective table cells.

def getLabelValue(value, multistates):
	"""Return the label for an int/float value that matches a multistate entry."""
	result = ""
	if value is not None and value != "":
		if multistates is not None and len(multistates) > 0:
			for state in multistates:
				try:
					if hasattr(state, "__getitem__"):
						sv = state["value"]
						sl = state["label"]
					else:
						sv = getattr(state, "value", None)
						sl = getattr(state, "label", None)
					if sv is not None and int(value) == int(sv):
						result = sl if sl is not None else ""
						break
				except:
					continue
		else:
			if value:
				result = "True"
			else:
				result = "False"
	return result
