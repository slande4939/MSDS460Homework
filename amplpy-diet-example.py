#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Based on AMPL Python API documentation: 
# https://buildmedia.readthedocs.org/media/pdf/amplpy/latest/amplpy.pdf
import sys
import os
from amplpy import AMPL, Environment

def main(argc, argv):
    # Set up the AMPL environment
    ampl = AMPL(Environment('C:/Users/Lavieestbelle$1/AMPL'))

    # Set the solver to CPLEX
    ampl.setOption('solver', 'cplex')

    # Path to the model and data files
    model_directory = 'C:/Users/Lavieestbelle$1/Desktop/MSDS460/Assignment1/AMPL-WORK-2024/models/diet'

    # Read the model and data files
    ampl.read(os.path.join(model_directory, 'diet.mod'))
    ampl.read_data(os.path.join(model_directory, 'diet.dat'))

    # Solve the linear programming problem
    ampl.solve()

    # Print the total cost from the objective
    total_cost = ampl.get_objective('Total_Cost')
    print('Total cost for the diet plan is:', total_cost.value())

    # Print the optimal solution - servings of each food item
    servings = ampl.get_variable('Buy')
    df_servings = servings.get_values()
    print(df_servings)

    # Additional code for updating costs or other parameters can be added here

if __name__ == '__main__':
    try:
        main(len(sys.argv), sys.argv)
    except Exception as e:
        print(e)
        raise
