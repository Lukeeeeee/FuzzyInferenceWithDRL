from membershipFunction import  MembershipFunction

class GaussianMF(MembershipFunction):
    def __init__(self, name, mean, standerd_deviation):
        super(MembershipFunction, self).__init__(name)
        self.mean = mean
        self.stander_deviation = standerd_deviation
    def calc(self, value):
        return 0.0 #Todo Gaussian mf
        pass
