

from src.fuzzyLogicRule.membershipFunction.membershipFunction import  MembershipFunction


class TriangleMF(MembershipFunction):

    def __init__(self, name, sl, c, sr):
        self.sl = float(sl)
        self.sr = float(sr)
        self.c = float(c)
        super(TriangleMF, self).__init__(name)

    def set_parameters(self, sl = None, sr = None, c = None):
        if sl is None:
            sl = self.sl
        if sr is None:
            sr = self.sr
        if c is None:
            c = self.c
        if sl > sr or sl > c or c > sr:
            # Todo Error handle
            pass
        self.sl = sl
        self.sr = sr
        self.c = c

    def calc(self, value):
        if self.c <= value <= self.c + self.sr:
            return 1.0 - (value - self.c) / self.sr
        elif self.c > value >= self.c - self.sl:
            return 1.0 - (self.c - value) / self.sl
        else:
            return 0.0
        pass

    def inverse_calc(self, input_degree):
        if input_degree > 1.0:
            #todo error of degre value
            return 0.0
        else:
            return self.c + (1 - input_degree) * (self.sr - self.sl) / 2.0
