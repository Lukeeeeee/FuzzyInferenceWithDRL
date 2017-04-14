import google.protobuf
import requests


class Environment(object):
    def __init__(self, name, state_set, action_set):
        self.timestep_limit = 1000
        self.name = name
        self.state_dim = len(state_set)
        self.state_set = state_set
        self.action_dim = len(action_set)
        self.action_set = action_set

    def set_action_set(self, action_set):
        self.action_set = action_set
        pass

    def set_reward(self):
        pass

    def set_state_set(self, state_set):
        self.state_set = state_set
        pass

    def reset(self):
        return 0.0
        pass

    def step(self, action):  # return next_state, reward, done
        pass

    def is_done(self, state):
        return False

if __name__ == '__main__':
    ss = google.protobuf.__version__
    ss = requests.__version__
