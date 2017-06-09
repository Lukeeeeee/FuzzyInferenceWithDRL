from __future__ import print_function

import datetime
import json
import os
import random
from collections import deque


class DDPGInitializer(object):
    def __init__(self,
                ddpg_controller,
                fuzzy_logic_controller,
                fuzzy_logic_valuer,
                mini_batch_size):
        self.ddpgController = ddpg_controller
        self.fuzzyLogicController = fuzzy_logic_controller
        self.fuzzyLogicValuer = fuzzy_logic_valuer
        self.mini_batch_size = mini_batch_size
        ti = datetime.datetime.now()
        self.log_file_dir = ('../../log/initialTrain/' + str(ti.month) + '-' + str(ti.day) + '-' + str(ti.hour) +
                             '-' + str(ti.minute) + '-' + str(ti.second) + '/')
        if not os.path.exists(self.log_file_dir):
            os.mkdir(self.log_file_dir)


    def generate_state_done_mini_batch(self, mini_batch_size):
        state_set = self.ddpgController.environment.state_set
        state_dim = self.ddpgController.environment.state_dim
        random_state_list = []
        random_done_list = []
        for i in range(mini_batch_size):
            random_state_sample = {}
            for state_i in state_set:
                random_state_sample[state_i.name] = random.uniform(0.0, 1.0)
            if self.ddpgController.environment.is_done(random_state_sample):
                random_done_list.append(1)
            else:
                random_done_list.append(0)
            random_state_list.append(random_state_sample)
        return random_state_list, random_done_list

    def generate_training_sample_mini_batch(self, mini_batch_size):
        mini_state_batch, done_list = self.generate_state_done_mini_batch(mini_batch_size)
        input_state_list = []
        for input_state_dict in mini_state_batch:
            input_state_dict.items().sort()
            input_state_list.append(input_state_dict.values())
        output_action_list = self.ddpgController.actor_network.actions(input_state_list)

        action_label_list = []
        value_label_list = []

        for input_state_dict in mini_state_batch:
            self.fuzzyLogicController.input_value_dict = input_state_dict
            action_label_dict = self.fuzzyLogicController.output_value_dict
            action_label_dict.items().sort()
            action_label_list.append(action_label_dict.values())

            self.fuzzyLogicValuer.input_value_dict = input_state_dict
            value_label_dict = self.fuzzyLogicValuer.output_value_dict
            value_label_dict.items().sort()
            value_label_list.append(value_label_dict.values())

        output_q_value_list = self.ddpgController.critic_network.q_value(
            state_batch=input_state_list,
            action_batch=action_label_list
        )
        mini_batch = deque()
        for i in range(mini_batch_size):
            sample = (input_state_list[i],
                      output_action_list[i],
                      action_label_list[i],
                      value_label_list[i],
                      done_list[i]
                      )
            mini_batch.append(sample)
        return mini_batch

    def train_DDPG(self, epoch):

        log_dict_list = []
        file_dir = self.log_file_dir + 'loss.txt'

        for i in range(epoch):
            mini_batch = self.generate_training_sample_mini_batch(self.mini_batch_size)
            critic_cost, actor_cost = self.ddpgController.initial_train(mini_batch=mini_batch)
            log_string = ("Epoch = %d Critic Cost = %.5f Actor Cost = %.5f" % (i, critic_cost, actor_cost))
            log_dict_list.append(
                {'epoch': i, 'Critic Cost': ('%.5f' % critic_cost), 'Actor Cost': ('%.5f' % actor_cost)})
            print(log_string)
        with open(file_dir, mode='w') as f:
            print(json.dumps(log_dict_list, indent=4), file=f)

if __name__ == '__main__':
    # ddpgInitializer = DDPGInitializer()
    pass
