import argparse
from pyMetaheuristic.algorithm import particle_swarm_optimization
from pyMetaheuristic import algorithm
# Import a Test Function. Available Test Functions: https://bit.ly/3KyluPp
from pyMetaheuristic.test_function import easom
from 規範 import test_function
# OR Define your Custom Function. The function input should be a list of values, 
# each value representing a dimension (x1, x2, ...xn) of the problem.
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument('--run',type=int, default=30)
parser.add_argument('--dim',type=int, default=2)
args = parser.parse_args()
dim=2
#hpo
def obj(x):
    run=1
    sum=0
    for r in range(run):
        parameters = {
            'Cr':x[0],
            'F':x[1],
            'n':int(x[2]*100),
            'iterations':dim*10000,
            'evaluations':dim*10000,
            'verbose':False
            }
        all_result = [ algorithm.differential_evolution(target_function = test_function.cal_function_objective(i),min_values=[test_function.set_search_range(i)[0]]*dim,max_values=[test_function.set_search_range(i)[1]]*dim,**parameters) for i in range(2,3)]
        # print(all_result[0][-1])
        sum+=all_result[0][-1]
        # print(sum)
    return sum/run

result=algorithm.differential_evolution(target_function = obj,min_values=[0.0,0.0,0.0],max_values=[1.0,1.0,1.0],iterations=1000,evaluations=1000,Cr=0.5,F=0.7,n=10)
variables = result[:-1]
minimum   = result[ -1]
print('Variables: ', np.around(variables, 4) , ' Minimum Value Found: ', minimum )
#Variables:  [0.3337 0.6459 0.2919] 1