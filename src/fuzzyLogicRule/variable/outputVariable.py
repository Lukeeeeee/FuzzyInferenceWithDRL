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
		self.name = name
		self.upper_range = range[1]
		self.lower_range = range[0]
		self.defuzzifier = defuzzifier
		self.linguistic_label = linguistic_label
		self.value = 0.0
		self.mf = mf
		self.consequence = 0.0

	def set_consequence(self, new_consequence):
		self.consequence = new_consequence
		self.value = self.defuzzifier(self)