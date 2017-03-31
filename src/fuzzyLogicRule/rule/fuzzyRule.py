# Generate fuzzy rule

import math
from src.fuzzyLogicRule.ruleParser import RuleParser

class FuzzyRule(object):
	
	def __init__(self,
				section_input_val, #all input at its section
				output_val,
				rule_str,
				section,
				min_operation = "softmin"
				):

		self._true_value = 0.0

		self._section_input_val = section_input_val
		self._min_operation = min_operation
		self._section = section
		self._input_dict =  {} # Dict pair{variable name, linguistic label}
		self._output_dict = {}
		self.output_val = output_val
		self._rule_str = rule_str
		if(self._rule_str is not None):
			self.set_input_output_dict()


	@property
	def rule_str(self):
		return self._rule_str
	@rule_str.setter
	def rule_str(self, new_rule_str):
		self._rule_str = new_rule_str
		self.set_input_output_dict()
	@property
	def true_value(self):
		return self.true_value
	@true_value.setter
	def true_value(self, new_true_value):
		# Todo Throw an error
		self.true_value = new_true_value
		pass
	def set_input_output_dict(self):
		ruleParser = RuleParser()
		self._input_dict, self._output_dict = ruleParser.parse_if_then_rule(self._rule_str)

	def _get_true_value(self):
		for input_val in self._section_input_val:
			input_val.calc_degree(input_val)
		if(self._min_operation is "min"):
			self.true_value = self._min_op()
		elif(self._min_operation is "softmin"):
			self.true_value = self._softmin_op()

	def _min_op(self):
		true_value = 0xffff # todo remove the magic number
		for val in self._section_input_val:
			if (val.name in self._input_dict):
				true_value = min(self.true_value, val.degree[self._input_dict[val.name]])
		return  true_value

	def _softmin_op(self):
		self.true_value = 0xffff
		true_value_numerator = 0.0
		true_value_denominator = 0.0
		for val in self._section_input_val:
			if(val.name in self._input_dict):
				true_value_numerator += 1.0 * val.degree[self._input_dict[val.name]] * math.exp(-val.degree[self._input_dict[val.name]])
				true_value_denominator += 1.0 * math.exp(-val.degree[self._input_dict[val.name]])
		return true_value_numerator / true_value_denominator





