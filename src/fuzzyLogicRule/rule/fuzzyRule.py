# Generate fuzzy rule

import math
from src.fuzzyLogicRule.ruleParser import RuleParser

class FuzzyRule(object):
	
	def __init__(self,
				 input_var_list,
				 output_var_list,
				 rule_str,
				 section,
				 min_operation = "softmin"
				 ):

		self._true_value = 0.0

		self._input_var_list = input_var_list
		self.output_var_list = output_var_list
		self._min_operation = min_operation
		self._section = section
		self._input_dict =  {} # Dict pair{variable name, linguistic label}
		self._output_dict = {}
		self._rule_str = rule_str
		if(self._rule_str is not None):
			self.set_input_output_dict(self._rule_str)
		self.output_var_value = {}


	@property
	def rule_str(self):
		return self._rule_str
	@rule_str.setter
	def rule_str(self, new_rule_str):
		self._rule_str = new_rule_str
		self.set_input_output_dict()
	@property
	def true_value(self):
		return self._true_value
	@true_value.setter
	def true_value(self, new_true_value):
		# Todo Throw an error
		self._true_value = new_true_value

	@property
	def input_var_list(self):
		return self._input_var_list
	@input_var_list.setter
	def input_var_list(self, new_input_var_list):
		self._input_var_list = new_input_var_list

	def set_input_var_value(self, new_input_var_value_dict):
		for input_var in self._input_var_list:
			input_var.value = new_input_var_value_dict[input_var.name]
		self._get_true_value()
		self.set_output_var_degree()

	def set_input_output_dict(self, rule_str = None):
		ruleParser = RuleParser()
		self._rule_str = rule_str
		self._input_dict, self._output_dict = ruleParser.parse_if_then_rule(rule_str)

	def _get_true_value(self):
		if(self._min_operation is "min"):
			self.true_value = self._min_op()
		elif(self._min_operation is "softmin"):
			self.true_value = self._softmin_op()

	def set_output_var_degree(self):
		for out_var in self.output_var_list:
			new_degree = out_var.degree
			new_degree[self._output_dict[out_var.name]] = self.true_value
			out_var.degree = new_degree
			self.output_var_value = out_var.value

	def _min_op(self):
		true_value = 0xffff # todo remove the magic number
		for val in self._input_var_list:
			if (val.name in self._input_dict):
				true_value = min(true_value, val.degree[self._input_dict[val.name]])
		return true_value

	def _softmin_op(self):
		self.true_value = 0xffff
		true_value_numerator = 0.0
		true_value_denominator = 0.0
		for val in self._input_var_list:
			if(val.name in self._input_dict):
				true_value_numerator += 1.0 * val.degree[self._input_dict[val.name]] * math.exp(-val.degree[self._input_dict[val.name]])
				true_value_denominator += 1.0 * math.exp(-val.degree[self._input_dict[val.name]])
		return true_value_numerator / true_value_denominator





