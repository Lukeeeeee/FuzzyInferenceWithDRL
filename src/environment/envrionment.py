import google.protobuf


class Environment(object):
    def __init__(self, action, reward, state):
        self.timestep_limit = 1000
        self.action = action
        self.reward = reward
        self.state = state
        # todo finish env

        pass
    def reset(self):
        return 0.0
        pass

    def step(self, action):
        pass

if __name__ == '__main__':
    ss = google.protobuf.__version__