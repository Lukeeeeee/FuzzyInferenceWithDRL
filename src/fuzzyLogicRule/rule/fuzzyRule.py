# Generate fuzzy rule


class FuzzyRule(object):
	
	def __init__(self,
				input_val_list,
				output_val,
				rule_str,
				section
				):
		self.input_val_list = input_val_list
		self.output_val = output_val
		self.rule_string = rule_str
		self.section = section
