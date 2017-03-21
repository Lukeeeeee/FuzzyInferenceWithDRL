

class Reasoner(object):
	"""docstring for Reasoner"""
	def __init__(self, input_val, frs):
		self.input_val = input_val
		self.frs = frs

	def set_input_val(self, input_val):
		self.input_val = input_val

	def reason(self, input_val = None):
		if input_val is not None:
			self.set_input_val(input_val)
		pass
