#!/usr/bin/env python
# -*- coding: utf-8 -*-
# drawing on documentation provided in 
#  https://buildmedia.readthedocs.org/media/pdf/amplpy/latest/amplpy.pdf
import sys
import os
from amplpy import AMPL, Environment

def main(argc, argv):

    ampl = AMPL(Environment('C:\\Users\\witho\\AMPL'))

    ampl.setOption('solver', 'cplex')

    # Read the model and data files.
    model_directory = 'C:\\Users\\witho\\Desktop\\AMPL-WORK-2024\\models\\diet'
    ampl.read(os.path.join(model_directory, 'diet.mod'))
    ampl.read_data(os.path.join(model_directory, 'diet.dat'))

    # Solve
    ampl.solve()

    # Get objective entity by AMPL name
    totalcost = ampl.get_objective('Total_Cost')
    # Print it
    print('Objective is:', totalcost.value())

    # Reassign data - specific instances
    cost = ampl.get_parameter('cost')
    cost.set_values({'BEEF': 5.01, 'HAM': 4.55})
    print('Increased costs of beef and ham.')

    # Resolve and display objective
    ampl.solve()
    print('New objective value:', totalcost.value())

    # Reassign data - all instances
    elements = [3, 5, 5, 6, 1, 2, 5.01, 4.55]
    cost.set_values(elements)
    print('Updated all costs.')

    # Resolve and display objective
    ampl.solve()
    print('New objective value:', totalcost.value())

    # Get the values of the variable Buy in a dataframe object
    buy = ampl.get_variable('Buy')
    df = buy.get_values()
    # Print them
    print(df)

    # Get the values of an expression into a DataFrame object
    df2 = ampl.get_data('{j in FOOD} 100*Buy[j]/Buy[j].ub')
    # Print them
    print(df2)

if __name__ == '__main__':
    try:
        main(len(sys.argv), sys.argv)
    except Exception as e:
        print(e)
        raise