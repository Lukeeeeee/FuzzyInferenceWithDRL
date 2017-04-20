import argparse
import torchcraft as tc
import torchcraft.Constants as tcc
from src.environment.envrionment import Environment


class StarCraftEnvironment(Environment):
    def __init__(self, name, state_set, action_set, args):
        super(StarCraftEnvironment, self).__init__(name, state_set, action_set)
        self.args = args

    def connect(self):
        self.cl = tf.Client()
        self.cl.connect(self.args.hostname, self.args.port)

    def init(self):
        self.state = self.cl.init(micro_battles=True)
        self.cl.send([
            [tcc.set_speed, 0],
            [tcc.set_gui, 1],
            [tcc.set_cmd_optim, 1],
        ])

    def reset(self):
        self.connect()
        self.init()

    def step(self, action):
        self.cl.send(action)
        state = self.cl.recv()
        reward = 0.0
        if state.battle_just_ended:
            if state.battle_won:
                reward = +1.0
            else:
                reward = -1.0
        return state, reward

    def is_done(self, state):
        pass
