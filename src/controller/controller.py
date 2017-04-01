from  src.fuzzyLogicRule import *


class Controller(object):
    def __init__(self, name):
        self._input_value_dict = {}
        self.output_value_dict = {}
        self.rule_section_set = {}
        pass

    @property
    def input_value(self):
        return self._input_value_dict
    @input_value.setter
    def input_value(self, new_input):
        self._input_value_dict = new_input
        self.assign_input_to_secion()
        self.calc_output()


    def add_rule_section(self, rule_set):
        self.rule_section_set[rule_set.name] = rule_set
        for input_i in rule_set.input_val:
            self.input_value[input_i.name] = 0.0
        for output_i in rule_set.output_val:
            self.output_value_dict[output_i.name] = 0.0

    def assign_input_to_secion(self):
        for name_i, rule_set_i in self.rule_section_set.items():
            rule_set_input_dict = {}
            for rule_set_input_key in rule_set_i.input_var_dict:
                rule_set_input_dict[rule_set_input_key] = self._input_value_dict[rule_set_input_key]
            rule_set_i.input_var_dict = rule_set_input_dict
        pass

    def calc_output(self):
        pass