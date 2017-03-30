from src.fuzzyLogicRule.variable.variable import Variable

class InputVariable(Variable):
	"""docstring for InputVariable"""
	def __init__(self, name, linguistic_label, range,
				 mf, value = 0.0):
		super(InputVariable, self).__init__(name, mf, range)

	# Todo Add property decorator
	def set_value(self, new_val):
		if(new_val > self.upper_range or new_val < self.lower_range):
			# Todo Error handle
			return -1
		self.input_value = new_val
		self.degree = self.calc_degree()
		return 1


	def calc_degree(self):
		antecedent = {}
		for i in range(len(self.linguistic_label)):
			antecedent[self.mf[i].name] = self.mf[i].calc(self.input_value)
		return  antecedent
