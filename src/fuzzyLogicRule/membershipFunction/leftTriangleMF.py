
from src.fuzzyLogicRule.membershipFunction.membershipFunction import MembershipFunction

class LeftTriangleMF(MembershipFunction):
    def __init__(self, name, c, sr):
        self.c = float(c)
        self.sr = float(sr)
        MembershipFunction.__init__(self, name)

    def set_parameters(self, c = None, sr = None):
        if c is None:
            c = self.c
        if sr is None:
            sr = self.sr
        if c > sr:
            # todo error handel
            pass
        else:
            self.c = c
            self.sr = sr

    def calc(self, input_value):
        if input_value <= self.c:
            return 1.0
        elif input_value <= self.c + self.sr:
            return (1.0 - (input_value - self.c) / self.sr )
        else:
            return 0.0





