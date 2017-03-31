# Generate fuzzy rule set 


class FuzzyRuleSet():
	
	def __init__(self, input_var, output_var, rule_list, name, section):
		self.name = name
		self.section = section
		self.input_var = input_var
		self.output_var = output_var
		self.rule_list = []

	def add_fuzzy_rule(self, fuzzy_rule):
		self.rule_list.append(fuzzy_rule)

	def set_input_value(self, input_value):
		for input_val_i in self.input_var:
			input_val_i.value = input_value[input_val_i.name]
		self.output_var[0].degree = self.calc_value()



	def calc_value(self):
		value_numerator = 0.0
		value_denominator = 0.0
		for rule in self.rule_list:
			value_numerator += rule.true_value * rule.output_val.value
			value_denominator += rule.true_value
		return value_numerator / value_denominator