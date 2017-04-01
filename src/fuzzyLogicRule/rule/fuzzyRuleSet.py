# Generate fuzzy rule set 


class FuzzyRuleSet():
	
	def __init__(self, name, section, rule_list = None,):
		self.name = name
		self.section = section
		self._input_var_dict = {}
		self.output_var_dict = {}
		self.rule_list = rule_list

	@property
	def input_var_dict(self):
		return self._input_var_dict
	@input_var_dict.setter
	def input_var_dict(self, new_input_var_dict):
		self._input_var_dict = new_input_var_dict
		self.set_input_value()

	def add_fuzzy_rule(self, fuzzy_rule):
		self.rule_list.append(fuzzy_rule)


	def set_input_value(self):
		for rule_i in self.rule_list:
			rule_input_var_dict = {}
			for input_var in rule_i.input_var_list:
				rule_input_var_dict[input_var.name] = self._input_var_dict[input_var.name]
			rule_i.set_input_var_value(rule_input_var_dict)


	def calc_value(self):
		value_numerator = 0.0
		value_denominator = 0.0
		for rule in self.rule_list:
			value_numerator += rule.true_value * rule.output_val_list[0].value
			value_denominator += rule.true_value
		return value_numerator / value_denominator