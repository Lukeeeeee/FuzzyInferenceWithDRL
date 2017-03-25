# Generate fuzzy rule set 


class FuzzyRuleSet:
	
	def __init__(self, input, name, section):
		self.name = name
		self.section = section
		self.rule_list = []

	def add_fuzzy_rule(self, fuzzy_rule):
		self.rule_list.append(fuzzy_rule)
		