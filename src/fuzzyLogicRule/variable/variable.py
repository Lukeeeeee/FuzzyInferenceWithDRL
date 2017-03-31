

class Variable(object):
    def __init__(self, name, mf, range):
        self.name = name
        self.mf = mf
        self.linguistic_label = []
        for mf_i in mf:
            self.linguistic_label.append(mf_i.name)
        self.upper_range = range[1]
        self.lower_range = range[0]
        self._value = {}
        self._degree = {}
        for linguistic_i in self.linguistic_label:
            self.degree[linguistic_i] = 0.0

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_val):
        self._value = new_val

    @property
    def degree(self):
        return self._degree
    @degree.setter
    def degree(self, new_degree):
        self._degree = new_degree
