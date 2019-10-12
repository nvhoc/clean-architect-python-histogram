
class SourceNotSupport(Exception):
	"""Base class for other exceptions"""
	pass

class SourceParamRequired(Exception):
	"""Base class for other exceptions"""
	def __init__(self, param):
		self.description = "param \"{}\" is required".format(param)