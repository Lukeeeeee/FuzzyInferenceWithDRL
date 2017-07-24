from src.fuzzyLogicRule.variable.variable import Variable


class OutputVariable(Variable):
    """docstring for OutputVariable"""

    def __init__(self, name, mf, range, defuzzifier):
        super(OutputVariable, self).__init__(name, mf, range)
        self.defuzzifier = defuzzifier
        self.value = {}

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, new_value):
        self._degree = new_value
        self.value = self.defuzzifier.defuzzify(self._degree, self.mf)