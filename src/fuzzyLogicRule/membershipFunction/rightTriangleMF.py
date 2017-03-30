
from src.fuzzyLogicRule.membershipFunction.membershipFunction import MembershipFunction
class RightTriangleMF(MembershipFunction):
    def __init__(self, name, c, sl):
        self.c = float(c)
        self.sl = float(sl)
        MembershipFunction.__init__(self, name)

    def set_parameters(self, c = None, sl = None):
        if c is None:
            c = self.c
        if sl is None:
            sl = self.sl
        if c < sl:
            # todo error handel
            pass
        else:
            self.c = c
            self.sl = sl

    def calc(self, input_value):
        if input_value >= self.c:
            return 1.0
        elif input_value >= self.c - self.sl:
            return (1.0 - (self.c - input_value) / self.sl )
        else:
            return 0.0
    def inverse_calc(self, input_degree):
        if (input_degree > 1.0):
            #todo error value of degree
            return 0.0
        else:
            return self.sl * (input_degree - 1) + self.c





