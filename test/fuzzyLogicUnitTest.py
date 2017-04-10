from __future__ import absolute_import

import os
import sys
import unittest

sys.path.append(os.getcwd() + '/src/')
from src import *

def construct_input(name):
    mf_l = LeftTriangleMF("low", c=0.0, sr=20)
    mf_m = TriangleMF("middle", sl=10, c=20, sr=10)
    mf_r = RightTriangleMF("high", c=40, sl=20)
    mf_list = [mf_l, mf_m, mf_r]
    temp = InputVariable(name, [-20, 50], mf_list, value=15)
    return temp

def construct_output(name):
    mf_l = LeftTriangleMF("low", c=-5.0, sr=5.0)
    mf_m = TriangleMF("middle", sl=2.0, c=0.0, sr=2.0)
    mf_r = RightTriangleMF("high", c=5.0, sl=5)
    mf_list = [mf_l, mf_m, mf_r]
    defuzzifier = LMOMDefuzzifier(name)
    temp = OutputVariable(name= name, mf= mf_list, range=[-5, 5], defuzzifier= defuzzifier)
    return temp

def construct_rule():
    temp_in_1 = construct_input("temperature")
    temp_in_2 = construct_input("humidity")
    temp_out = construct_output("clothing")
    rule_str_1 = "IF temperature is low and humidity is middle THEN clothing is low"
    rule_str_2 = "IF temperature is middle and humidity is middle THEN clothing is high"
    rule_str_3 = "IF temperature is high and humidity is low THEN clothing is middle"
    rule_str_4 = "IF temperature is low and humidity is high THEN clothing is low"
    rule_str = [rule_str_1, rule_str_2, rule_str_3, rule_str_4]
    input = [temp_in_1, temp_in_2]
    output = [temp_out]
    temp_rule_set = FuzzyRuleSet(name="clothing number control", section=1, rule_list=[])
    temp_rule_1 = FuzzyRule(input_var_list=input, output_var_list=output, section=1, rule_str=rule_str_1,
                            min_operation="min")
    temp_rule_2 = FuzzyRule(input_var_list=input, output_var_list=output, section=1, rule_str=rule_str_2,
                            min_operation="min")
    temp_rule_3 = FuzzyRule(input_var_list=input, output_var_list=output, section=1, rule_str=rule_str_3,
                            min_operation="min")
    temp_rule_4 = FuzzyRule(input_var_list=input, output_var_list=output, section=1, rule_str=rule_str_4,
                            min_operation="min")
    temp_rule_set.add_fuzzy_rule(temp_rule_1)
    temp_rule_set.add_fuzzy_rule(temp_rule_2)
    temp_rule_set.add_fuzzy_rule(temp_rule_3)
    temp_rule_set.add_fuzzy_rule(temp_rule_4)
    return [temp_rule_1, temp_rule_2, temp_rule_3, temp_rule_4], temp_rule_set


def construct_controller(rule_set = None):
    controller = Controller(name="clothing controller")
    if rule_set is not None:
        controller.add_rule_section(rule_set)
    return controller


class fuzzyLogicRuleTest(unittest.TestCase):
    def test_fuzzy_input(self):
        temp = construct_input("temperature")
        print("checking the basic input function")
        self.assertEqual(temp.name, "temperature")
        self.assertEqual(len(temp.mf), 3)
        self.assertEqual(len(temp.degree), 3)
        temp.value = 15
        print(temp.degree)
        self.assertEqual(temp.degree, {"low": 0.25, "middle": 0.5, "high":0.0})
        temp.value = 30
        self.assertEqual(temp.degree, {"low": 0.0, "middle": 0.0, "high": 0.5})
        print(temp.degree)

        print("test of basci input function finished")

    def test_fuzzy_output(self):
        print("checking the basic output function")
        temp = construct_output("clothing")
        self.assertEqual(temp.name, "clothing")
        self.assertEqual(len(temp.mf), 3)
        self.assertEqual(len(temp.degree), 3)
        temp.degree = {"low": 0.0, "middle": 1, "high": 0.0}
        self.assertEqual(temp.value, {"low": 0, "middle": 0, "high": 0})
        print(temp.value)
        temp.degree = temp.degree = {"low": 2.0 / 7.0, "middle": 2.0 / 7.0, "high": 0.0}
        print(temp.value)

        print("Test of basic output function finished")

    def test_fuzzy_rule_construct(self):
        print("checking the construction of rule set")
        rule_str_1 = "IF temperature is low and humidity is middle THEN clothing is low"
        rule_str_2 = "IF temperature is middle and humidity is middle THEN clothing is high"
        rule_str_3 = "IF temperature is high and humidity is low THEN clothing is middle"
        rule_str_4 = "IF temperature is low and humidity is high THEN clothing is low"
        rule_list, rule_set = construct_rule()
        # check the rule
        self.assertEqual(len(rule_list), 4)
        self.assertEqual(rule_list[0]._input_dict, {"temperature":"low", "humidity":"middle"})
        self.assertEqual(rule_list[0]._output_dict, {"clothing":"low"})
        self.assertEqual(rule_list[0]._section, 1)
        self.assertEqual(rule_list[0]._min_operation, "min")
        self.assertEqual(rule_list[0]._rule_str,rule_str_1)

        self.assertEqual(rule_list[1]._input_dict, {"temperature": "middle", "humidity": "middle"})
        self.assertEqual(rule_list[1]._output_dict, {"clothing": "high"})
        self.assertEqual(rule_list[1]._section, 1)
        self.assertEqual(rule_list[1]._min_operation, "min")
        self.assertEqual(rule_list[1]._rule_str,rule_str_2)


        self.assertEqual(rule_list[2]._input_dict, {"temperature": "high", "humidity": "low"})
        self.assertEqual(rule_list[2]._output_dict, {"clothing": "middle"})
        self.assertEqual(rule_list[2]._section, 1)
        self.assertEqual(rule_list[2]._min_operation, "min")
        self.assertEqual(rule_list[2]._rule_str,rule_str_3)


        self.assertEqual(rule_list[3]._input_dict, {"temperature": "low", "humidity": "high"})
        self.assertEqual(rule_list[3]._output_dict, {"clothing": "low"})
        self.assertEqual(rule_list[3]._section, 1)
        self.assertEqual(rule_list[3]._min_operation, "min")
        self.assertEqual(rule_list[3]._rule_str,rule_str_4)

        # check the rule set
        self.assertEqual(rule_set.name, "clothing number control")
        self.assertEqual(rule_set.section, 1)
        self.assertEqual(rule_set.rule_list, rule_list)

        print("Test of fuzzy rule and set finished")
    def test_fuzzy_rule_controller_construct(self):
        print("Checking the construction of controller")
        controller = construct_controller(rule_set = None)
        self.assertEqual(controller.name, "clothing controller")
        _, rule_set = construct_rule()
        controller.add_rule_section(rule_set)
        self.assertEqual(controller.rule_section_set[rule_set.name], rule_set)
        print("Test of controller finished")

    def test_fuzzy_rule_reason(self):
        rule_list, rule_set = construct_rule()
        rule = rule_list[3]
        input_val_dict = {"temperature": 15, "humidity": 30}
        rule.set_input_var_value(input_val_dict)
        self.assertEqual(rule.true_value, 0.25)
        self.assertEqual(rule.output_var_list[0].value, {'high': 0.0, 'middle': 0.0, 'low': -1.25})
        self.assertEqual(rule.output_var_value, {'high': 0.0, 'middle': 0.0, 'low': -1.25})

        #print(rule.output_var_list[0].value)

        input_val_dict = {"temperature": 30, "humidity": 15}
        rule.set_input_var_value(input_val_dict)
        self.assertEqual(rule.true_value, 0.0)
        self.assertEqual(rule.output_var_list[0].value, {'high': 0.0, 'middle': 0.0, 'low': 0.0})
        self.assertEqual(rule.output_var_value, {'high': 0.0, 'middle': 0.0, 'low': 0.0})


    def test_fuzzy_rule_set_reason(self):
        print("Checking the reasoning of single rule set")
        _, rule_set = construct_rule()
        input_val_dict = {"temperature": 15, "humidity": 30}
        rule_set.input_var_value_dict = input_val_dict
        self.assertEqual(rule_set.rule_set_output_value, -1.25)
        print(rule_set.rule_set_output_value)

        input_val_dict = {"temperature": 30, "humidity": 15}
        rule_set.input_var_value_dict = input_val_dict
        self.assertEqual(rule_set.rule_set_output_value, 0.0)
        print(rule_set.rule_set_output_value)
        print("Test of single rule set finished")

    def test_fuzzy_rule_controller_reason(self):
        print("Checking the reasoning of controller")
        _, rule_set = construct_rule()
        controller = construct_controller(rule_set)

        input_val_dict = {"temperature": 15, "humidity": 30}
        controller.input_value_dict = input_val_dict
        self.assertEqual(controller.output_value_dict, {"clothing": -1.25})
        print(controller.output_value_dict)

        input_val_dict = {"temperature": 30, "humidity": 15}
        controller.input_value_dict = input_val_dict
        self.assertEqual(controller.output_value_dict, {"clothing": 0.0})
        print(controller.output_value_dict)

        print("Test of controller reasoning finished")

if __name__ == '__main__':
   unittest.main()
