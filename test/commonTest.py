from __future__ import absolute_import

import random
import string

from src import *


def construct_input(name, rand_flag=False):
    if rand_flag is False:
        mf_l = LeftTriangleMF("low", c=0.25, sr=0.2)
        mf_m = TriangleMF("middle", sl=0.25, c=0.5, sr=0.25)
        mf_r = RightTriangleMF("high", c=0.75, sl=0.2)
        mf_list = [mf_l, mf_m, mf_r]
        temp = InputVariable(name, [0.0, 1.0], mf_list, value=0.5)
    else:
        list = []
        for i in range(7):
            list.append(random.random())
        list.sort()
        mf_l = LeftTriangleMF("low", c=list[0], sr=list[2] - list[0])
        mf_m = TriangleMF("middle", sl=list[3] - list[1], c=list[3], sr=list[5] - list[3])
        mf_r = RightTriangleMF("high", c=list[6], sl=list[6] - list[4])
        mf_list = [mf_l, mf_m, mf_r]
        temp = InputVariable(name, [0.0, 1.0], mf_list, value=0.5)
    return temp


def construct_output(name, rand_flag = False):
    if rand_flag is False:
        mf_l = LeftTriangleMF("low", c=0.25, sr=0.2)
        mf_m = TriangleMF("middle", sl=0.25, c=0.5, sr=0.25)
        mf_r = RightTriangleMF("high", c=0.75, sl=0.2)
        mf_list = [mf_l, mf_m, mf_r]
        defuzzifier = LMOMDefuzzifier(name)
        temp = OutputVariable(name=name, mf=mf_list, range=[0.0, 1.0], defuzzifier=defuzzifier)
    else:
        list = [random.random() for _ in range(7)]
        list.sort()
        mf_l = LeftTriangleMF("low", c=list[0], sr=list[2] - list[0])
        mf_m = TriangleMF("middle", sl=list[3] - list[1], c=list[3], sr=list[5] - list[3])
        mf_r = RightTriangleMF("high", c=list[6], sl=list[6] - list[4])
        mf_list = [mf_l, mf_m, mf_r]
        defuzzifier = LMOMDefuzzifier(name)
        temp = OutputVariable(name=name, mf=mf_list, range=[0.0, 1.0], defuzzifier=defuzzifier)
    return temp


def construct_rule(temp_in_1, temp_in_2, temp_in_3, temp_out, section_id):
    rule_str = string.Template("IF $in1_name is $in1_label and $in2_name is $in2_label "
                               "and $in3_name is $in3_label THEN $out_name is $out_label")
    in_list = [temp_in_1, temp_in_2, temp_in_3]
    rand_label = []
    for i in range(4):
        temp = random.randint(1, 3)
        if temp == 1:
            rand_label.append("low")
        if temp == 2:
            rand_label.append("middle")
        if temp == 3:
            rand_label.append("high")
    rule_str = rule_str.substitute(in1_name=temp_in_1.name, in1_label=rand_label[0],
                                   in2_name=temp_in_2.name, in2_label=rand_label[1],
                                   in3_name=temp_in_3.name, in3_label=rand_label[2],
                                   out_name=temp_out.name, out_label=rand_label[3],
                                   )
    output = [temp_out]
    temp_rule = FuzzyRule(input_var_list=in_list, output_var_list=output, section=section_id, rule_str=rule_str,
                          min_operation="min")
    return temp_rule

if __name__ == '__main__':
    pass
