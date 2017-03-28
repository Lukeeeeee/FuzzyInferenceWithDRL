'''
Output variable:
	name
	value
	range
	linguistic_label
	mf
'''

class OutputVariable(object):
	"""docstring for OutputVariable"""
	def __init__(self, name, range, defuzzifier, mf,
					linguistic_label):
		self._name = name
		self._upper_range = range[1]
		self._lower_range = range[0]
		self._defuzzifier = defuzzifier
		self._linguistic_label = linguistic_label

		self._value = 0.0
		self.mf = mf
		self._consequence = 0.0

	@property
	def consequence(self):
		return self._consequence

	@consequence.setter
	def consequece(self, new_consequence_val):
		self._consequence = new_consequence_val
		self.value = 0.0 # todo after finish defuzzifier

	@property
	def value(self):
		return self.value

	@value.setter
	def value(self, new_val):
		# compute value using defuzzfizer
		self.value = new_val
		pass
