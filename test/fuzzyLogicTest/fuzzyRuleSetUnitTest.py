from __future__ import absolute_import

import sys
import unittest
from collections import namedtuple

sys.path.append('/home/zhongwang/Desktop/GARIC/src/')
from src import *

TriangleMFPara = namedtuple("TriangleMFPara", ['name', 'sl', 'c', 'sr'])

in_p1 = TriangleMFPara("low", 0, 0, 20)
in_p2 = TriangleMFPara("middle", 10, 20, 10)
in_p3 = TriangleMFPara("high", 20, 40, 0)

out_p1 = TriangleMFPara("low", 0, -5.0, 5.0)
out_p2 = TriangleMFPara("middle", 2.0, 0, 2.0)
out_p3 = TriangleMFPara("high", 5.0, 5.0, 0)


def construct_inputvar(name, range=(-20, 50), p1=in_p1, p2=in_p2, p3=in_p3):
    mf_1 = LeftTriangleMF(name=p1.name, c=p1.c, sr=p1.sr)
    mf_2 = TriangleMF(name=p2.name, sl=p2.sl, c=p2.c, sr=p2.sr)
    mf_3 = RightTriangleMF(name=p3.name, c=p3.c, sl=p3.sl)
    mf_list = [mf_1, mf_2, mf_3]
    return InputVariable(name, range, mf_list, 0)


def construct_outputvar(name, range=(-5, 5), p1=out_p1, p2=out_p2, p3=out_p3):
    mf_1 = LeftTriangleMF(name=p1.name, c=p1.c, sr=p1.sr)
    mf_2 = TriangleMF(name=p2.name, sl=p2.sl, c=p2.c, sr=p2.sr)
    mf_3 = RightTriangleMF(name=p3.name, c=p3.c, sl=p3.sl)
    mf_list = [mf_1, mf_2, mf_3]
    defuzzifier = LMOMDefuzzifier(name)
    return OutputVariable(name=name, mf=mf_list, range=range, defuzzifier=defuzzifier)


class fuzzyRuleSetUnitTest(unittest.TestCase):
    def test_fuzzy_rule_set(self):
        print "checking the rule_set case1"

        test_rulestr_1 = "IF temperature is low and humidity is middle THEN clothing is low"
        test_rulestr_2 = "IF temperature is high and humidity is low THEN clothing is low"

        test_in_1 = construct_inputvar(name="temperature")
        test_in_2 = construct_inputvar(name="humidity")
        test_out = construct_outputvar(name="clothing")
        test_rule_1 = FuzzyRule(input_var_list=[test_in_1, test_in_2], output_var_list=[test_out],
                              section=1, rule_str=test_rulestr_1, min_operation="min")
        test_rule_2 = FuzzyRule(input_var_list=[test_in_1, test_in_2], output_var_list=[test_out],
                                section=1, rule_str=test_rulestr_2, min_operation="min")
        test_ruleset = FuzzyRuleSet("test", 1, [test_rule_1, test_rule_2])

        self.assertEqual(test_ruleset.name, "test")
        self.assertEqual(test_ruleset.get_input_var_name(), ["temperature", "humidity"])
        self.assertEqual(test_ruleset.get_output_var_name(), ["clothing"])

        test_ruleset.input_var_value_dict={"temperature":15,"humidity":20}

        true_value1 = test_rule_1.true_value
        output_var_value1 = test_rule_1.output_var_value["low"]
        true_value2 = test_rule_2.true_value
        output_var_value2 = test_rule_2.output_var_value["low"]

        self.assertEqual(test_ruleset.rule_set_output_value,
                         (true_value1*output_var_value1+true_value2*output_var_value2)/(true_value1+true_value2))
        # todo still not check the defuzzifier

if __name__ == '__main__':
    unittest.main()
