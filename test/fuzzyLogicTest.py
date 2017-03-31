from __future__ import absolute_import

import sys
import unittest

sys.path.append('/home/lukedong/PycharmProjects/GARIC/src/')
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
    rule_str = "IF temperature is low THEN "

class fuzzyLogicRuleTest(unittest.TestCase):
    def test_fuzzy_input_init(self):
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
        print("checking the basic output function")
        temp = construct_output("clothing")
        self.assertEqual(temp.name, "clothing")
        self.assertEqual(len(temp.mf), 3)
        self.assertEqual(len(temp.degree), 3)
        temp.degree = {"low": 0.0, "middle": 1, "high": 0.0}
        self.assertEqual(temp.value, {"low": 0, "middle": 0, "high": 0})
        print(temp.value)
        temp.degree = temp.degree = {"low": 2.0/7.0, "middle": 2.0/7.0, "high": 0.0}
        print(temp.value)

    def test_fuzzy_rule(self):
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
        temp_rule = FuzzyRule(section_input_val=input, output_val=output, section=1, rule_str=rule_str, min_operation="min")
        pass

if __name__ == '__main__':
   unittest.main()
