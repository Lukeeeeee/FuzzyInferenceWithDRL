# Generate fuzzy rule set 


class FuzzyRuleSet():
	
	def __init__(self, input_val, output_val, rule_list, name, section):
		self.name = name
		self.section = section
		self.input_val = input_val
		self.ouput_val = output_val
		self.rule_list = []

	def add_fuzzy_rule(self, fuzzy_rule):
		self.rule_list.append(fuzzy_rule)

	def calc_value(self):
		value_numerator = 0.0
		value_denominator = 0.0
		for rule in self.rule_list:
			value_numerator += rule.true_value * rule.output_val.value
			value_denominator += rule.true_value
		return value_numerator / value_denominator