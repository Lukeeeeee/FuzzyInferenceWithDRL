

from membershipFunction import  MembershipFunction


class TriangleMF(MembershipFunction):

    def __init__(self, name, sl, sr, c):
        MembershipFunction.__init__(name)
        self.sl = sl
        self.sr = sr
        self.c = c


    def set_parameters(self, sl = None, sr = None, c = None):
        if sl is None:
            sl = self.sl
        if sr is None:
            sr = self.sr
        if c is None:
            c = self.s
        if sl > sr or sl > c or c > sr:
            print("Error when assign TriangleMf\n")
            pass
        self.sl = sl
        self.sr = sr
        self.c = c
    def get_value(self, value):
        if value >= self.c:
            return (1.0 - (value - self.c) / self.sr)
        elif value < self.c:
            return (1.0 - (self.c - value) / self.sl)
        else:
            return 0.0
        pass
