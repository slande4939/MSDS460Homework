# Optimizing Nutritional Intake within Budgetary Constraints: A Personal Dietary Linear Programming Approach

##  Methods
Linear Programming Model Formulation:
In this section, I constructed a linear programming model to determine the most cost-effective weekly diet that satisfies my nutritional requirements. The decision variables represented the servings per week of five food items: almonds, brown rice, Greek yogurt, pizza, and tofu vegetables & hash brown. The objective was to minimize the total cost of these items while adhering to nutritional constraints on calories, protein, and essential vitamins and minerals.
Constraints Implementation:
I incorporated constraints to reflect the minimum and maximum nutritional requirements based on current dietary guidelines. These constraints ensured my diet would not exceed sodium limits while meeting my needs for energy, protein, vitamin D, calcium, iron, and potassium.

## Results
Initial Solution Analysis:
The initial solution to my diet problem highlighted a reliance on a single food item—pizza—due to its cost-effectiveness in meeting the set nutritional parameters. The total cost for my weekly diet plan was calculated to be $143.625.
Dietary Variety Constraints:
Recognizing the importance of dietary variety, I revised the model to include at least one serving of each food item. This adjustment aimed to promote a more balanced nutrient intake, even if it increased the overall cost.

### Implemented in AMPL and Python (amplpy)

I set up the necessary model and data files for the diet example in AMPL were under the models directory of the AMPL installation. It should be possible to work from the command line (terminal or Powershell) to execute the example program implemented in: amplpy-diet-example.py. 

Ensure that lines 11 and 16 of the program amplpy-diet-example.py refer to the directories where you have installed AMPL and have place the diet.dat and diet.mod files for the diet problem.

Reference

Fourer, Robert, David M. Gay, and Brian W. Kernighan. 2003. *AMPL: A Modeling Language for Mathematical Programming* (second edition). Belmont, CA: Brooks/Cole. [ISBN-13: 978-0-534-38809-6] Chapter 2, Diet and Other Input Models: Minimizing Costs, pages 27–42.
