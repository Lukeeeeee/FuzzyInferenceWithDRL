

class Reasoner(object):
	"""docstring for Reasoner"""
	def __init__(self, input_val, frs):
		self.input_val = input_val
		self.frs = frs
		self.antecedent = None

	def set_intput_val(self, intput_val):
		n = intput_val.count()
		for i in range(n):
			self.input_val.set_val(input_val[i].value)

	def reason(self, input_val = None):
		for input_variable in input_val:

		pass
