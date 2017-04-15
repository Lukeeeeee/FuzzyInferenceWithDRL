from envrionment import Environment


class StarCraftEnvironment(Environment):
    def __init__(self, name, state_set, action_set):
        super(self, Environment).__init__(name, state_set, action_set)
