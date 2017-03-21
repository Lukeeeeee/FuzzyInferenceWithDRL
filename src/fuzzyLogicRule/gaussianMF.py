from membershipFunction import  MembershipFunction

class GaussianMF(MembershipFunction):
    def __init__(self, name, mean, standerd_deviation):
        super(MembershipFunction, self).__init__(name)
        self.mean = mean
        self.stander_deviation = standerd_deviation



if __name__ == "main":
    ss = GaussianMF("s", 0, 1);
