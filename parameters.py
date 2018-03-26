# input parameters for derivative pricing
# Charles Sambo
# www.linkedin.com/charlessambo
# @stochasticquant
# quantengineer@outlook.com

from abc import ABCMeta, abstractmethod

class Parameters():
    ''' class which implemeting a parameter object 
    
        - initialization data is a list of parameters :
            S0: initial price
            K : strike price
            T : time ot maturity
            r : frisk free rate
            sigma : asset volatility
            sim : number of monte carlo simulations
            op_type : type of option (call/put)
    '''

    #_metaclass__ = abc.ABCMeta

    # Constructor of parameters required for pricing
    def __init__(self, prams):

        self.prams = prams

        if self.prams[7] not in ("c", "p"):
            raise ValueError(
                "{} is not a valid option type, should be 'c' or 'p'.".format(self.prams[7]))

        self.dt = self.prams[2] / self.prams[6]

    @abstractmethod
    def prameters(self):
        '''method prints the pricing parameters
        
        '''
        print("-------- Pricing parameters ------------------------\n")
        print("Initial asset price : {}".format(self.prams[0]))
        print("Strike price        : {}".format(self.prams[1]))
        print("Time to maturity    : {} years".format(self.prams[2]))
        print("Risk free rate      : {}".format(self.prams[3]))
        print("Asset volatility    : {}".format(self.prams[4]))
        print("Simulation steps    : {}".format(self.prams[5]))
        print("time per step       : {}".format(round(self.dt, 4)))
        print("No. of simulations) : {}".format(self.prams[6]))
        print("Option type         : {}".format(self.prams[7]))


    def __repr__(self):
        'method used for debugging and meant to be seen by other developers showing how object is created'

        return "Parameter({},{},{},{},{},{},{},{})".format(self.prams[0], self.prams[1], self.prams[2], self.prams[3], self.prams[4],
                                                                  self.prams[5], self.prams[6], self.prams[7])

    def __str__(self):
        'is a readable presentation of an object presented to the end-user'
        return "Pricing parameters : [Stock {}, strike {}, maturity {}, Risk free {}, Volatility {}, Sim steps {},sims {}, option type {}]".format(self.prams[0], self.prams[1], self.prams[2], self.prams[3], self.prams[4],
                                                                       self.prams[5], self.prams[6], self.prams[7])
       
# self test code
if __name__ == '__main__':

    # parameters
    pms = [105.0, 100.0, 2, 0.05, 0.25, 200, 100000, "c"]

    p1 = Parameters(pms)
    p1.prameters()
    print(p1)
    print()
    print(Parameters.__dict__)

    

