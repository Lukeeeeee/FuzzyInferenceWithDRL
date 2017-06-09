# import google.protobuf
import requests


class Environment(object):
    def __init__(self, name, state_set, action_set):
        self.time_step_limit = 1000
        self.name = name
        self.state_dim = len(state_set)
        self.state_set = state_set
        self.action_dim = len(action_set)
        self.action_set = action_set
        self.reward = None

    def set_action_set(self, action_set):
        self.action_set = action_set
        pass

    def set_reward(self, reward):
        self.reward = reward
        pass

    def set_state_set(self, state_set):
        self.state_set = state_set
        pass

    def reset(self):
        return 0.0

    def step(self, action):  # return next_state, reward, done
        next_state = 0.0
        reward = 0.0
        done = False
        return next_state, reward, done

    def is_done(self, state):
        return False

if __name__ == '__main__':
    # import tensorflow as tf
    # ss = google.protobuf.__version__
    ss = requests.__version__
