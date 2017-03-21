'''
Input variable:
	name
	value
	range
	linguistic_label
	mf
'''

class InputVariable(object):
	"""docstring for InputVariable"""
	def __init__(self, name, value=0.0, range, 
				inguistic_label, mf):
		self.name = name
		self.value = value
		self.upper_range = range[1]
		self.lower_range = range[0]
		self.linguistic_label = linguistic_label
		self.mf = mf

	def set_value(self, value):
		if(value > upper_range or value < lower_range):
			error("Invalid input value")
			pass
		self.input_value = value
	def get_value(self):
		return self.value


