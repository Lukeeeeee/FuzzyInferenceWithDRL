from __future__ import absolute_import

import sys
import unittest
from collections import namedtuple

sys.path.append('/home/zhongwang/Desktop/GARIC/src/')
from src import *

TriangleMFPara = namedtuple("TriangleMFPara", ['name', 'sl', 'c', 'sr'])

def construct_inputvar():
    pass


class outputVarUnitTest(unittest.TestCase):

    def test_output_var(self):
        pass

if __name__ == '__main__':
    unittest.main()
