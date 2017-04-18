# Generate fuzzy rule set 


class FuzzyRuleSet(object):
	
	def __init__(self, name, section, rule_list):
		# TODO not rule_list=[]
		self.name = name
		self.section = section
		#self._input_var_value_dict = {} # pair name : value
		self.output_var_value_dict = {} # pair name : value
		self.rule_list = rule_list
		self.rule_set_output_value = 0.0

	@property
	def input_var_value_dict(self):
		return self._input_var_value_dict
	@input_var_value_dict.setter
	def input_var_value_dict(self, new_input_var_dict):
		self._input_var_value_dict = new_input_var_dict
		self.assign_input_value()


	def add_fuzzy_rule(self, fuzzy_rule):
		self.rule_list.append(fuzzy_rule)
		# todo do we need to update the input and output value dict?
		# for input_var in fuzzy_rule.input_var_list:
		# 	self._input_var_value_dict[input_var.name] = 0.0
		# for output_var in fuzzy_rule.output_var_list:
		# 	self.output_var_value_dict[output_var.name] = 0.0

	def get_input_var_name(self):
		input_var_name = []
		for rule_i in self.rule_list:
			for input_var in rule_i.input_var_list:
				if input_var.name not in input_var_name:
					input_var_name.append(input_var.name)
		return input_var_name

	def get_output_var_name(self):
		output_var_name = []
		for rule_i in self.rule_list:
			for output_var in rule_i.output_var_list:
				if output_var.name not in output_var_name:
					output_var_name.append(output_var.name)
		return output_var_name


	def assign_input_value(self):
		for rule_i in self.rule_list:
			rule_input_var_dict = {}
			for input_var in rule_i.input_var_list:
				rule_input_var_dict[input_var.name] = self._input_var_value_dict[input_var.name]
			rule_i.set_input_var_value(rule_input_var_dict)
		self.rule_set_output_value = self._calc_value()



	def _calc_value(self):
		value_numerator = 0.0
		value_denominator = 0.0
		for rule in self.rule_list:
			output_var = rule.output_var_list[0]
			output_var_value = rule.output_var_value[rule._output_dict[output_var.name]]
			value_numerator += rule.true_value * output_var_value
			value_denominator += rule.true_value
		if value_denominator <= 0.000001:
			return 0.0
		else:
			return value_numerator / value_denominator