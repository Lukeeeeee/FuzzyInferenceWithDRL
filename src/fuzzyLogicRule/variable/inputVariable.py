from src.fuzzyLogicRule.variable.variable import Variable


class InputVariable(Variable):
    """docstring for InputVariable"""

    def __init__(self, name, range,
                 mf, value=0.0):
        super(InputVariable, self).__init__(name, mf, range)
        self._value = value

    # Todo Add property decorator

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val
        self.degree = self.calc_degree()

    def calc_degree(self):
        antecedent = {}
        for i in range(len(self.linguistic_label)):
            antecedent[self.mf[i].name] = self.mf[i].calc(self.value)
        return antecedent
