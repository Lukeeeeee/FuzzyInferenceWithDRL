

class State(object):
    def __init__(self, range, name):
        self.name = name
        self.lower_range = range[0]
        self.upper_range = range[1]
