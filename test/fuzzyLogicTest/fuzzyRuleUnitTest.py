from __future__ import absolute_import

import sys
import unittest
from collections import namedtuple

sys.path.append('/home/zhongwang/Desktop/GARIC/src/')
from src import *

TriangleMFPara = namedtuple("TriangleMFPara", ['name', 'sl', 'c', 'sr'])

in_p1 = TriangleMFPara("low", 0, 0, 20)
in_p2 = TriangleMFPara("middle",10, 20, 10)
in_p3 = TriangleMFPara("high", 20, 40, 0)

out_p1 = TriangleMFPara("low", 0, -5.0, 5.0)
out_p2 = TriangleMFPara("middle", 2.0, 0, 2.0)
out_p3 = TriangleMFPara("high", 5.0, 5.0, 0)

def construct_inputvar(name, range=(-20,50), p1=in_p1, p2=in_p2, p3=in_p3):
    mf_1 = LeftTriangleMF(name=p1.name, c=p1.c, sr=p1.sr)
    mf_2 = TriangleMF(name=p2.name, sl=p2.sl, c=p2.c, sr=p2.sr)
    mf_3 = RightTriangleMF(name=p3.name, c=p3.c, sl=p3.sl)
    mf_list = [mf_1, mf_2, mf_3]
    return InputVariable(name, range, mf_list, 0)


def construct_outputvar(name, range=(-5,5), p1=out_p1, p2=out_p2, p3=out_p3):
    mf_1 = LeftTriangleMF(name=p1.name, c=p1.c, sr=p1.sr)
    mf_2 = TriangleMF(name=p2.name, sl=p2.sl, c=p2.c, sr=p2.sr)
    mf_3 = RightTriangleMF(name=p3.name, c=p3.c, sl=p3.sl)
    mf_list = [mf_1, mf_2, mf_3]
    defuzzifier = LMOMDefuzzifier(name)
    return OutputVariable(name=name, mf=mf_list, range=range, defuzzifier=defuzzifier)


class fuzzyRuleUnitTest(unittest.TestCase):

    def test_fuzzy_rule(self):
        print "checking the rule case1"

        test_rulestr = "IF temperature is low and humidity is middle THEN clothing is low"
        test_in_1 = construct_inputvar(name="temperature")
        test_in_2 = construct_inputvar(name="humidity")
        test_out = construct_outputvar(name="clothing")
        test_rule = FuzzyRule(input_var_list=[test_in_1, test_in_2], output_var_list=[test_out],
                                section=1, rule_str=test_rulestr, min_operation="min")

        self.assertEqual(test_rule._input_dict, {"temperature": "low", "humidity": "middle"})
        self.assertEqual(test_rule._output_dict, {"clothing": "low"})

        test_rule.set_input_var_value({"temperature":15, "humidity":15})
        self.assertEqual(test_rule._true_value, 0.25)

        test_rule.set_input_var_value({"temperature": 20, "humidity": 15})
        self.assertEqual(test_rule._true_value, 0.0)

        test_rule.set_input_var_value({"temperature": 15, "humidity": 10})
        self.assertEqual(test_rule._true_value, 0.0)


        # todo calc and assert the output_var_value and so on



if __name__ == '__main__':
   unittest.main()
