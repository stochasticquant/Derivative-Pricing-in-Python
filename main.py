# Charles Sambo
# www.linkedin.com/charlessambo
# @stochasticquant
# quantengineer@outlook.com

# Derivate pricing application
# A great scientist is a dreamer and a skeptic.

import helper_functions as hf
import scenario_generation_engine as sge


def main():

    # testing implementations
    hf.check_class(sge.Scenario_Genaration_Engine, 'geometric_brownian')

    # pricing report
    global report
    report = hf.pricer_report(105.0, 100.0, 2, 0.05, 0.25, 200, 100000, "c")

    # plot asset price paths
    hf.price_path_plot(report[0], 100)


if __name__ == "__main__":
    main()

