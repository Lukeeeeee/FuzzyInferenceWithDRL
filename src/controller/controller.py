from src.fuzzyLogicRule import *


class Controller(object):
    def __init__(self, name):
        self._input_value_dict = {}
        self.output_value_dict = {}
        self.rule_section_set = {}
        pass

    @property
    def input_value_dict(self):
        return self._input_value_dict
    @input_value_dict.setter
    def input_value_dict(self, new_input):
        self._input_value_dict = new_input
        self.assign_input_to_secion()
        self._calc_output()


    def add_rule_section(self, rule_set):
        self.rule_section_set[rule_set.name] = rule_set

    def assign_input_to_secion(self):
        for name_i, rule_set_i in self.rule_section_set.items():
            rule_set_input_dict = {}
            for rule_set_input_key in rule_set_i.input_var_dict:
                rule_set_input_dict[rule_set_input_key] = self._input_value_dict[rule_set_input_key]
            rule_set_i.input_var_value_dict = rule_set_input_dict

    def _calc_output(self):
        for rule_set_i in self.rule_section_set:
            rule_set_i_output_name_list = rule_set_i.get_output_var_name
            #Todo error hande if this list lenght is not 1
            self.output_value_dict[rule_set_i_output_name_list[0]] = \
                rule_set_i.rule_set_output_value