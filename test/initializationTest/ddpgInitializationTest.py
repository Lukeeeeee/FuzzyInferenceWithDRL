from __future__ import print_function

import json

from test.commonTest import *

try:
    import cPickle as pickle
except ImportError:
    import pickle

sys.path.append(os.getcwd() + '/src/')


class ddpgInitializaionTest(object):
    def __init__(self, state_dim, action_dim):
        self.input_var_list = self.generate_input_var(input_dim=state_dim)
        self.output_var_list = self.generate_output_var(output_dim=action_dim)
        self.value = self.generate_value()
        self.section_list, self.value_rule = self.generate_section_list()

    def generate_input_var(self, input_dim=100):
        input_var_list = []
        for i in range(input_dim):
            var_i = construct_input(name="InputVar_" + str(i), rand_flag=True)
            input_var_list.append(var_i)
        return input_var_list

    def generate_output_var(self, output_dim = 10):
        output_var_list = []
        for i in range(output_dim):
            var_i = construct_output(name="OutputVar_" + str(i), rand_flag=True)
            output_var_list.append(var_i)
        return output_var_list

    def generate_value(self):
        value = construct_output(name="Value", rand_flag=True)
        return value

    def generate_section_list(self, rule_per_seciont_num = 10):
        section_num = len(self.output_var_list)
        input_var_num = len(self.input_var_list)
        section_list = []
        for i in range(section_num): # generate one section every iteration
            rule_list = []
            for j in range(rule_per_seciont_num):
                temp1 = random.choice(self.input_var_list)
                temp2 = random.choice(self.input_var_list)
                while temp2.name == temp1.name:
                    temp2 = random.choice(self.input_var_list)
                temp3 = random.choice(self.input_var_list)
                while(temp3.name == temp1.name or temp3.name == temp2.name):
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
            while (temp3.name == temp1.name or temp3.name == temp2.name):
                temp3 = random.choice(self.input_var_list)
            value_rule_list.append(construct_rule(temp1, temp2, temp3, self.value, section_id=1))
        return section_list, value_rule_list

    def generate_fuzzy_logic_controller(self, input_dim = 100, output_dim = 10, rule_num = 100):
        self.section_num = output_dim
        self.controller = Controller(name = "ControllerTest")
        section_num = len(self.section_list)
        for i in range(section_num):
            rule_list = self.section_list[i]
            temp_rule_set = FuzzyRuleSet(name=str(i) +"_OutputVarControllSection", section=i, rule_list=rule_list)
            self.controller.add_rule_section(temp_rule_set)
        return self.controller

    def generate_fuzzy_logic_valuer(self):
        self.valuer = Controller(name="ValuerTest")
        rule_list = self.value_rule
        temp_rule_set = FuzzyRuleSet(name = "ValueControllSection", section=1, rule_list=rule_list)
        self.valuer.add_rule_section(temp_rule_set)
        return self.valuer

    def save_to_json(self, fp):
        json.dump(self, fp, default=lambda obj: obj.__dict__)
        pass

if __name__ == '__main__':
    testInitializer = ddpgInitializaionTest(state_dim=100,
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
                                      mini_batch_size=100)
    ddpgInitializer.train_DDPG()
    #save something useful
    log_file = open("../../log/json/test.txt", "w")

    #print(pickle.dumps(ddpgInitializaionTest))
    #print(pickle.dumps(fuzzy_controller))
    #json.dumps(ddpgInitializaionTest, default=lambda obj: obj.__dict__)
    print(json.dumps(fuzzy_controller, default=lambda obj: obj.__dict__), file = log_file)
    #ddpgInitializaionTest.save_to_json()
