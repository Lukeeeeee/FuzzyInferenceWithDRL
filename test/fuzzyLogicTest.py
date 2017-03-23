from __future__ import absolute_import
import unittest
import sys
sys.path.append('/home/lukedong/PycharmProjects/GARIC/src/')
from fuzzyLogicRule import *



# For input variable and compute input an
class MyTestCase(unittest.TestCase):
    def test_fuzzy_input_init(self):
        mf_l = LeftTriangleMF("low", c = 0.0, sr = 20)
        mf_m = TriangleMF("middle", sl = 10, c = 20, sr = 10)
        mf_r = RightTriangleMF("high", c = 40, sl = 20)
        mf_list = [mf_l, mf_m, mf_r]
        temp = InputVariable("tempeature", [-20, 50], mf_list, value = 15)
        self.assertEqual(temp.linguistic_label_count, 3)
        self.assertEqual(len(temp.mf), 3)
        self.assertEqual(len(temp.antecedent), 3)
        print(temp.antecedent)

if __name__ == '__main__':
   unittest.main()
