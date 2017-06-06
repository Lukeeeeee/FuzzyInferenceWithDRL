from src.fuzzyLogicRule.defuzzifier.defuzzifier import Defuzzifier


class LMOMDefuzzifier(Defuzzifier):
    def __init__(self, name):
        Defuzzifier.__init__(self, name)
        pass

    def defuzzify(self, degree, mf):
        value = {}
        for mf_i in mf:
            value[mf_i.name] = mf_i.inverse_calc(degree[mf_i.name])
        return value
        pass

