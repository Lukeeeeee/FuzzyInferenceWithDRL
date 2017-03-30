from src.fuzzyLogicRule.variable.variable import Variable

class OutputVariable(Variable):
    """docstring for OutputVariable"""

    def __init__(self, name, mf, range, defuzzifier
                 ):
        super(OutputVariable, self).__init__(name, mf, range)
        self.defuzzifier = defuzzifier

    @property
    def degree(self):
        return self.degree

    @degree.setter
    def degree(self, new_value):
        self.degree = new_value

    @property
    def value(self):
        return self.value
    @value.setter
    def value(self, new_value):
        self.value = new_value