import gc
import os
import sys

from src import *

sys.path.append(os.getcwd() + '/src/')

gc.enable()


class StarCraftControllerTest(DDPGController):
    def __init__(self, env):
        super(StarCraftControllerTest, self).__init__(env)
        self.name = "StarCraftController"

    def construct_state_set(self):
        pass

    def construct_action_set(self):
        pass

    def construct_output_set(self):
        pass

    def construct_env(self):
        self.construct_state_set()
        self.construct_action_set()
        self.construct_output_set()
        pass

    def convert_output_to_action(self):
        pass


def construct_agent(state_set, action_set):
    env = Environment(name="StarCraftEnv",
                      state_set=state_set,
                      action_set=action_set)
    agent = StarCraftControllerTest(env)
    return agent


def get_action(state, agent):
    action = agent.noise_action(state)
    return action


def return_state(state, )
