from __future__ import absolute_import

import sys
import unittest
from collections import namedtuple

sys.path.append('/home/zhongwang/Desktop/GARIC/src/')
from src import *

TriangleMFPara = namedtuple("TriangleMFPara",['name', 'sl', 'c', 'sr'])

def construct_inputvar(name, range, p1, p2, p3):
    mf_1 = LeftTriangleMF(name=p1.name, c=p1.c, sr=p1.sr)
    mf_2 = TriangleMF(name=p2.name, sl=p2.sl, c=p2.c, sr=p2.sr)
    mf_3 = RightTriangleMF(name=p3.name, c=p3.c, sl=p3.sl)
    mf_list = [mf_1, mf_2, mf_3]

    return InputVariable(name, range, mf_list, 0)


def constuct_rule_set():
    pass



class fuzzyLogicRuleTest(unittest.TestCase):
    def test_leftTriangleMF(self):
        pass
    def test_rightTriangleMF(self):
        pass
    def test_triangleMF(self):
        pass

    def test_input_var(self):

        print "input_var test case1"

        test_name="temperature"
        test_range = [-20, 50]
        test_p1 = TriangleMFPara('low', 0, 0, 20)
        test_p2 = TriangleMFPara('middle', 10, 20, 10)
        test_p3 = TriangleMFPara('high', 20, 40, 0)
        test_value = 15 # the test value
        test_result = {test_p1.name:0.25, test_p2.name:0.5, test_p3.name:0.0}

        test_var = construct_inputvar(name=test_name, range=test_range, p1=test_p1,
                                      p2=test_p2, p3=test_p3)
        test_var.value = test_value

        self.assertEqual(test_var.name, test_name)
        self.assertEqual([test_var.lower_range, test_var.upper_range], test_range)
        self.assertEqual(test_var.degree, test_result)

        print "input_var test case2"

        test_name = "humidity"
        test_range = [-20, 50]
        test_p1 = TriangleMFPara('low', 0, 0, 10)
        test_p2 = TriangleMFPara('middle', 10, 10, 10)
        test_p3 = TriangleMFPara('high', 10, 20, 0)
        test_value = 5
        test_result = {test_p1.name: 0.5, test_p2.name: 0.5, test_p3.name: 0.0}


        test_var = construct_inputvar(name=test_name, range=test_range, p1=test_p1,
                                      p2=test_p2, p3=test_p3)
        test_var.value = test_value

        self.assertEqual(test_var.name, test_name)
        self.assertEqual([test_var.lower_range, test_var.upper_range], test_range)
        self.assertEqual(test_var.degree, test_result)

        print "input_var test case3"

        test_name = "humidity"
        test_range = [-20, 50]
        test_p1 = TriangleMFPara('low', 0, 0, 10)
        test_p2 = TriangleMFPara('middle', 10, 10, 10)
        test_p3 = TriangleMFPara('high', 10, 20, 0)
        test_value = 15
        test_result = {test_p1.name: 0.0, test_p2.name: 0.5, test_p3.name: 0.5}

        test_var = construct_inputvar(name=test_name, range=test_range, p1=test_p1,
                                      p2=test_p2, p3=test_p3)
        test_var.value = test_value

        self.assertEqual(test_var.name, test_name)
        self.assertEqual([test_var.lower_range, test_var.upper_range], test_range)
        self.assertEqual(test_var.degree, test_result)

    def test_output_var(self):
        pass

    def test_fuzzy_rule(self):
        pass

    def test_fuzzy_ruleset(self):
        pass







if __name__ == '__main__':
   unittest.main()
