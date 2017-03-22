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
	def __init__(self, name, range,
				linguistic_label, mf, value = 0.0):
		self.name = name
		self.upper_range = range[1]
		self.lower_range = range[0]
		self.linguistic_label = linguistic_label
		self.mf = mf
		self.set_value(value)

	def set_value(self, new_val):
		if(new_val.value > self.upper_range or new_val.value < self.lower_range):
			print ("Invalid input value")
			return 0
			pass
		self.input_value = new_val
		self.antecededent = self.mf.calc(self.input_value)
		return 1
	def get_value(self):
		return self.value

	def set_mf(self, new_mf):
		self.mf = new_mf
		self.set_value(self.get_value())



