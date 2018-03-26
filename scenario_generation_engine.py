
# Scenario generation engine for various stochastic processes
#   - Geometric Brownian motion
#

import abc
from math import exp, sqrt
from time import time
from numpy import cumsum, maximum, random, mean, std
from scipy.stats import norm
from numpy import *

#import numexpr as ne
# import from file : scenario_generation_engine.py
import parameters as pram

class Scenario_Genaration_Engine(pram.Parameters):
    ''' class to implement scenario generations
    - stock price
    - volatility
    - short rate
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, S0, K, T, r, sigma, steps, sim, op_type):
        # initialize attributes of the Parameter class
        super().__init__(S0, K, T, r, sigma, steps, sim, op_type)

    @abc.abstractmethod
    def geometric_brownian(self):
        # scenario simulation of stock price using Geometric Brownian Motion
        dt = self.T / self.steps
        S = []

        S = self.S0 * exp(cumsum((self.r - 0.5 * self.sigma ** 2) * dt + self.sigma *
                                 sqrt(dt) * random.standard_normal((self.steps + 1, self.sim)), axis=0))
        S[0] = self.S0

        return(S)
