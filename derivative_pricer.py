
# Derivative pricing engine for the following methods
#   - Risk neutral 
#   - Black Scholes 
#   - Binomial tree 

import abc
from math import exp, sqrt
from time import time
import matplotlib.pyplot as plt
from numpy import cumsum, maximum, random, mean, std
from scipy.stats import norm
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns
import numexpr as ne

import scenario_generation_engine as sge




class DerivativePricer(sge.Scenario_Genaration_Engine):
    '''class implemetation of various methods of option prcing methods. Requires

        - risk neutral method
        - black-scholes method
        - Cox-Ross binomial tree method

    '''

    def __init__(self, S0, K, T, r, sigma, steps, sim, op_type):
        # initialize attributes of the Parameter class
        super().__init__(S0, K, T, r, sigma, steps, sim, op_type)

    # risk neural pricing using monte carlo
    # call option
    def riskNeutral(self, s_prices):
        ''' method to calculate option price using monte carlo risk neutral method
            required input of simulated asset price paths as : sim_prices

        '''
        try:

            if self.op_type == "c":
                pay_off = maximum(s_prices[-1] - self.K, 0)
                return(exp(-self.r * self.T) * sum(pay_off) / self.sim)

            else:
                pay_off = maximum(self.K - s_prices[-1], 0)
                return(exp(-self.r * self.T) * sum(pay_off) / self.sim)

        except ArithmeticError:
            print("Input parameters not correct")

    # black-scholes pricing
    def blackScholes(self):
        'method to calculate oprion price using black-scholes formula'

        self.d1 = (log(self.S0 / self.K) + (self.r + 0.5 *
                                            self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))

        self.d2 = self.d1 - self.sigma * sqrt(self.T)

        try:

            if self.op_type == "c":
                option_price = (self.S0 * norm.cdf(self.d1, 0.0, 1.0) -
                                self.K * exp(-self.r * self.T) * norm.cdf(self.d2, 0.0, 1.0))
                return(option_price)

            elif self.op_type == "p":
                option_price = (self.K * exp(-self.r * self.T) * norm.cdf(self.d1, 0.0,
                                                                          1.0)) - (self.S0 * norm.cdf(self.d2, 0.0, 1.0))
                return(option_price)

        except ArithmeticError:
            print("Input parameters not correct")

    def __repr__(self):
        'method used for debugging and meant to be seen by other developers showing how object is created'

        return "DerivativePricer({},{},{},{},{},{},{},{})".format(self.S0, self.K, self.T, self.r, self.sigma,
                                                                  self.steps, self.sim, self.op_type)

    def __str__(self):
        'is a readable presentation of an object presented to the end-user'
        return 'Initial asset price :{} strike price :{} maturity :{}'.format(self.S0, self.K, self.T)
