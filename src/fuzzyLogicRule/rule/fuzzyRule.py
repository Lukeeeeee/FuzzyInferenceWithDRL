# Generate fuzzy rule

import math

class FuzzyRule(object):
	
	def __init__(self,
				section_input_val, #all input at its section
				output_val,
				rule_str,
				section,
				min_operation = "softmin"
				):
		self.section_input_val = section_input_val
		self.rule_str = rule_str
		self.true_value = 0.0
		self.min_operation = min_operation

		self.input_dict =  {} # Dict pair{variable name, linguistic label}
		self.output_dict = {}
		self.output_val = output_val
		self.section = section


	@property
	def rule_str(self):
		return self.rule_str
	@rule_str.setter
	def rule_str(self, new_rule_str):
		self.rule_str = new_rule_str
		var_list = self.rule_str.split(" ")
		# todo parse the input and output with number
		self.input_dict = {}
		self.output_dict = {}
		n = len(var_list)
		for i in range(0, n-2, 2):
			self.input_dict[var_list[i]] = var_list[i+1]
		self.output_dict[var_list[n-2]] = var_list[n-1]

	def get_true_value(self):
		for input_val in self.section_input_val:
			input_val.calc_antecedent(input_val)
		if(self.min_operation is "min"):
			self.true_value = self.min_op(self)
		elif(self.min_operation is "softmin"):
			self.true_value = self.softmin_op(self)

	def min_op(self):
		true_value = 0xffff
		for val in self.section_input_val:
			if (val.name in self.input_dict):
				true_value = min(self.true_value, val.antecednet[self.input_dict[val.name]])
		return  true_value

	def softmin_op(self):
		self.true_value = 0xffff
		true_value_numerator = 0.0
		true_value_denominator = 0.0
		for val in self.section_input_val:
			if(val.name in self.input_dict):
				true_value_numerator += 1.0 * val.antecednet[self.input_dict[val.name]] * math.exp(-self.input_dict[val.name])
				true_value_denominator += 1.0 * math.exp(-self.input_dict[val.name])
		return true_value_numerator / true_value_denominator





