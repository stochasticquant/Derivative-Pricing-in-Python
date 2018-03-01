
# helper functions 

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')

import derivative_pricer as dp


# plot simulated asset paths from monte carlo
def price_path_plot(data, simulations):
    # data : data to be plotted
    # simulations : number of simulations of the data to be plotted

    plt.figure(figsize=(15, 10))
    plt.plot(data[:, :simulations])
    plt.grid(True)
    plt.title('{} Asset Price Simulation'.format(simulations))
    plt.xlabel('time step')
    plt.ylabel('price level')
    plt.show()

# asset price histogram
def price_hist(data):
    plt.figure(figsize=(13, 7))
    plt.hist(data[-1], bins=70)
    plt.grid(True)
    plt.title('Asset price distribution')
    plt.xlabel('Asset prices')
    plt.ylabel('Frequency')
    plt.show()

# checks if methos is implemented in a class
def check_class(_class, attribute):
    try:
        assert hasattr(_class, attribute)
        print('Process check....')
        print('Implementation of {} ok!\n'.format(attribute))
    except:
        print('Process check....')
        print('{} is not implemented in {}\n'.format(attribute, _class))

# reporting
def pricer_report(S0, K, T, r, sigma, steps, sim, op_type):

    # create a pricer object
    pricer = dp.DerivativePricer(S0, K, T, r, sigma, steps, sim, op_type)
    # get asset price simulations
    asset_prices = pricer.geometric_brownian()

    # get option prices
    risk_neutral_price = round(pricer.riskNeutral(asset_prices), 4)
    black_scholes = round(pricer.blackScholes(), 4)
    pricing_error = round(pricer.blackScholes() -
                          pricer.riskNeutral(asset_prices), 10)
    percent_error = round(
        pricing_error / pricer.riskNeutral(asset_prices), 4) * 100

    print("........... Option Pricing ........................\n")
    print("Risk neutral pricing method")
    print("Option type     : {} ".format(pricer.op_type))
    print("Option price    : {} ".format(risk_neutral_price))
    print("\nBlack-Scholes pricing method")
    print("Option type     : {} ".format(pricer.op_type))
    print("Option price    : {} ".format(black_scholes))
    print("\nPricing error   : {} ".format(pricing_error))
    print("Percent error   : {} %\n".format(percent_error))
    print("..................................................")

    return [asset_prices, pricer]
