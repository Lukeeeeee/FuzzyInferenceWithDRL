
from src.fuzzyLogicRule.defuzzifier import Defuzzifier

class TSKDefuzzifier(Defuzzifier):
    def __int__(self, name, weight):
        Defuzzifier.__init__(self, name)
        self._weight = weight
        self.consequence = 0.0
        pass

    def defuzzify(self, output_val):

        pass


