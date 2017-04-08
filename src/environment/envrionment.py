import google.protobuf
import requests


class Environment(object):
    def __init__(self, name):
        self.timestep_limit = 1000
        self.name = name
        self.action_set, self.action_dim = self.set_action_set()
        self.reward = self.set_reward()
        self.state_set, self.state_dim = self.set_state_set()

    def set_action_set(self):
        pass

    def set_reward(self):
        pass

    def set_state_set(self):
        pass

    def reset(self):
        return 0.0
        pass

    def step(self, action):  # return next_state, reward, done
        pass

    def is_done(self, state):
        return True

if __name__ == '__main__':
    ss = google.protobuf.__version__
    ss = requests.__version__
