import gc
import os
import sys

from src import *

sys.path.append(os.getcwd() + '/src/')

gc.enable()


class StarCraftController(DDPGController):
    def __init__(self, env):
        super(StarCraftController, self).__init__(env)
        self.name = "StarCraftController"
        self.construct_env()

    def construct_state_set(self, state_dict):
        pass

    def construct_action_set(self, action_dict):
        pass

    def construct_output_set(self, output_dict):
        pass

    def construct_env(self, state_dict, action_dict):
        self.construct_state_set(state_dict=state_dict)
        self.construct_action_set(action_dict=action_dict)
        output_dict = {}
        self.construct_output_set(output_dict=output_dict)
        pass

    def convert_output_to_action(self):
        pass

    def construct_agent(self, state_set, action_set):
        env = Environment(name="StarCraftEnv",
                          state_set=state_set,
                          action_set=action_set)
        agent = StarCraftController(env)
        return agent

    def get_action(self, state, agent):
        action = agent.noise_action(state)
        return action

    def return_state(self, state):
        pass


if __name__ == '__main__':
    pass
