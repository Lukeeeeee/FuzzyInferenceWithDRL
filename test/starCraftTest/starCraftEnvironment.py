import os
import sys

from src.environment.envrionment import Environment
from test.starCraftTest.TorchCraft import *



class StarCraftEnvironment(Environment):
    def __init__(self, name, state_set, action_set):
        super(StarCraftEnvironment, self).__init__(name, state_set, action_set)

    def reset(self):
        pass

    def step(self, action):

        pass

    def is_done(self, state):
        pass
