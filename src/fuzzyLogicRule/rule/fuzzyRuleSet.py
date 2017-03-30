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

		