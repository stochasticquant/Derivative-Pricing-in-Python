# input parameters for derivative pricing

class Parameters():
    ''' class which implemeting a parameter object '''

    # Constructor of parameters required for pricing
    def __init__(self, S0, K, T, r, sigma, steps, sim, op_type):

        if op_type not in ("c", "p"):
            raise ValueError(
                "{} is not a valid option type, should be 'c' or 'p'.".format(op_type))

        ### list of constructor setters
        # This is the starting asset value
        self.S0 = S0
        # option strike price
        self.K = K
        # time to maturity in years
        self.T = T
        # risk free rate
        self.r = r
        # asset volatility
        self.sigma = sigma
        # simulation steps
        self.steps = steps
        # number of simulations
        self.sim = sim
        # option type (1 = call, 0 = put)
        self.op_type = op_type
