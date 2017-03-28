# Generate fuzzy rule


class FuzzyRule(object):
	
	def __init__(self,
				input_val_list,
				output_val,
				rule_str,
				section,
				min_operation = "softmin"
				):
		self.input_val_list = input_val_list
		self.output_val = output_val
		self._rule_string = rule_str
		self.section = section
		self.true_value = 0.0
		self.min_operation = min_operation
	def parse_rule_string(self):
		pass

	def get_true_value(self):
		for input_val in self.input_val_list:
			input_val.calc_antecedent(input_val)
		if(self.min_operation is "min"):
			self.true_value = self.min_op(self)
		elif(self.min_operation is "softmin"):
			self.true_value = self.softmin_op(self)

	def min_op(self):
		for val in self.input_val_list:
			if __name__ == '__main__':
				min_antecedent = val.antecedent['']
		pass

	def softmin_op(self):
		pass




