class Action(object):
    def __init__(self, range, name):
        self.name = name
        self.upper_range = range[0]
        self.lower_range = range[1]
