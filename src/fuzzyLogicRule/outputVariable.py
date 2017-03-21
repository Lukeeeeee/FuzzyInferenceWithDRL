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
	def __init__(self, name, range, defuzzifier,
					linguistic_label):
		self.name = name
		self.upper_range = range[1]
		self.lower_range = range[0]
		self.defuzzifier = defuzzifier
		self.linguistic_label = linguistic_label
		self.value = 0.0

	def set_value(self, value):
		self.value = value