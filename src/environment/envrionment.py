import google.protobuf
import requests


class Environment(object):
    def __init__(self, name, state_dim=100, action_dim=100):
        self.timestep_limit = 1000
        self.name = name
        self.set_action_set(action_dim)
        self.set_reward()
        self.set_state_set(state_dim)

    def set_action_set(self, action_dim):
        self.action_dim = action_dim
        pass

    def set_reward(self):
        pass

    def set_state_set(self, state_dim):
        self.state_dim = state_dim
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
