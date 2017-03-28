
class InputVariable(object):
	"""docstring for InputVariable"""
	def __init__(self, name, range,
				 mf, value = 0.0):
		self.name = name
		self._upper_range = range[1]
		self._lower_range = range[0]
		self.mf = mf
		self.linguistic_label = []
		for mf_i in self.mf:
			self.linguistic_label.append(mf_i.name)
		self.linguistic_label_count = len(self.linguistic_label)

		self.set_value(value)

	# Todo Add property decorator
	def set_value(self, new_val):
		if(new_val > self._upper_range or new_val < self._lower_range):
			# Todo Error handle
			return -1
		self.input_value = new_val
		self.antecedent = self.calc_antecedent()
		return 1

	def get_value(self):
		return self.input_value
	def get_antecedent(self):
		return  self.calc_antecedent()

	def set_mf(self, new_mf):
		self.mf = new_mf
		self.set_value(self.get_value())

	def calc_antecedent(self):
		antecedent = {}
		for i in range(self.linguistic_label_count):
			antecedent[self.mf[i].name] = self.mf[i].calc(self.input_value)
		return  antecedent
