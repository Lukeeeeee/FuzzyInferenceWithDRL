"""
DDPG initialization test

Usage:
    ddpginitializationTest.py epoch <epoch> mini_batch <mini_batch>
    
Options:
    -h --help

"""

from __future__ import print_function

from docopt import docopt

from test.common.common import *

try:
    import cPickle as pickle
except ImportError:
    import pickle


class DDPGInitializaionTest(object):
    def __init__(self, state_dim, action_dim):
        self.input_var_list = self.generate_input_var(input_dim=state_dim)
        self.output_var_list = self.generate_output_var(output_dim=action_dim)
        self.value = self.generate_value()
        self.section_list, self.value_rule = self.generate_section_list()
        self.section_num = None
        self.controller = None
        self.valuer = None

    def generate_input_var(self, input_dim=100):
        input_var_list = []
        for i in range(input_dim):
            var_i = construct_input(name="InputVar_" + str(i), rand_flag=True)
            input_var_list.append(var_i)
        return input_var_list

    def generate_output_var(self, output_dim=10):
        output_var_list = []
        for i in range(output_dim):
            var_i = construct_output(name="OutputVar_" + str(i), rand_flag=True)
            output_var_list.append(var_i)
        return output_var_list

    def generate_value(self):
        value = construct_output(name="Value", rand_flag=True)
        return value

    def generate_section_list(self, rule_per_seciont_num=10):
        section_num = len(self.output_var_list)
        # input_var_num = len(self.input_var_list)
        section_list = []
        for i in range(section_num):  # generate one section every iteration
            rule_list = []
            for j in range(rule_per_seciont_num):
                temp1 = random.choice(self.input_var_list)
                temp2 = random.choice(self.input_var_list)
                while temp2.name == temp1.name:
                    temp2 = random.choice(self.input_var_list)
                temp3 = random.choice(self.input_var_list)
                while temp3.name == temp1.name or temp3.name == temp2.name:
                    temp3 = random.choice(self.input_var_list)
                rule_list.append(construct_rule(temp1, temp2, temp3, self.output_var_list[i], section_id=i))
            section_list.append(rule_list)
        value_rule_list = []
        for j in range(rule_per_seciont_num):
            temp1 = random.choice(self.input_var_list)
            temp2 = random.choice(self.input_var_list)
            while temp2.name == temp1.name:
                temp2 = random.choice(self.input_var_list)
            temp3 = random.choice(self.input_var_list)
            while temp3.name == temp1.name or temp3.name == temp2.name:
                temp3 = random.choice(self.input_var_list)
            value_rule_list.append(construct_rule(temp1, temp2, temp3, self.value, section_id=1))
        return section_list, value_rule_list

    def generate_fuzzy_logic_controller(self, output_dim=10):
        self.section_num = output_dim
        self.controller = Controller(name="ControllerTest")
        section_num = len(self.section_list)
        for i in range(section_num):
            rule_list = self.section_list[i]
            temp_rule_set = FuzzyRuleSet(name=str(i) + "_OutputVarControlSection", section=i, rule_list=rule_list)
            self.controller.add_rule_section(temp_rule_set)
        return self.controller

    def generate_fuzzy_logic_valuer(self):
        self.valuer = Controller(name="ValuerTest")
        rule_list = self.value_rule
        temp_rule_set = FuzzyRuleSet(name="ValueControlSection", section=1, rule_list=rule_list)
        self.valuer.add_rule_section(temp_rule_set)
        return self.valuer


if __name__ == '__main__':
    arguments = docopt(__doc__)
    epoch = int(arguments["<epoch>"])
    mini_batch_size = int(arguments["<mini_batch>"])

    testInitializer = DDPGInitializaionTest(state_dim=100,
                                            action_dim=10)
    env = Environment(name="InitialTest",
                      state_set=testInitializer.input_var_list,
                      action_set=testInitializer.output_var_list)

    fuzzy_controller = testInitializer.generate_fuzzy_logic_controller()
    fuzzy_valuer = testInitializer.generate_fuzzy_logic_valuer()

    ddpgController = DDPGController(env)

    ddpgInitializer = DDPGInitializer(ddpg_controller=ddpgController,
                                      fuzzy_logic_controller=fuzzy_controller,
                                      fuzzy_logic_valuer=fuzzy_valuer,
                                      mini_batch_size=mini_batch_size)
    ddpgInitializer.train_DDPG(epoch=epoch)

    ddpgInitializer.save_all_model(epoch=epoch)

    # ddpgInitializer.load_model(path=log.LOG_PATH + 'initialTrain/6-12-14-38-48/model/DDPGControllerModel.ckpt-100')
    # ddpgInitializer.train_DDPG(epoch=100)
