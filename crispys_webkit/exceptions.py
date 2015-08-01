
class SchemeError(Exception):
	def __init__(self, scheme, allowed_schemes):
		self.scheme = scheme
		self.allowed_schemes = allowed_schemes

	def __str__(self):
		return repr('Invalid scheme %s. Valid schemes %r' % (self.scheme, self.allowed_schemes))

class HostError(Exception):
	def __init__(self):
		pass
	def __str__(self):
		return repr('There is no host name')

