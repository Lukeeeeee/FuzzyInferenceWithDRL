
from src.fuzzyLogicRule.defuzzifier import Defuzzifier

class TSKDefuzzifier(Defuzzifier):
    def __int__(self, weight):
        self._weight = weight
        self.consequence = 0.0
        pass

    def defuzzy(self, outputVar):

        pass


