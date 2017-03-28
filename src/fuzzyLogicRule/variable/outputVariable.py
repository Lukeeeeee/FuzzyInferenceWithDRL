'''
Output variable:
	name
	value
	range
	linguistic_label
	mf
'''


class OutputVariable(object):
    """docstring for OutputVariable"""

    def __init__(self, name, range, defuzzifier, mf,
                 linguistic_label):
        self._name = name
        self._upper_range = range[1]
        self._lower_range = range[0]
        self._defuzzifier = defuzzifier
        self._linguistic_label = linguistic_label
        self._value = 0.0
        self.mf = mf
        self.consequence = 0.0

    @property
    def consequence(self):
        return self.consequence
    @consequence.setter
    def consequence(self, value):
        self.consequence = value
        self._value = self.compute_value()
        pass
    def compute_value(self):
        
        pass