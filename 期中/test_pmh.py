
# Import PSO
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
# def easom(variables_values = [0, 0]):
#     x1, x2     = variables_values
#     func_value = -np.cos(x1)*np.cos(x2)*np.exp(-(x1 - np.pi)**2 - (x2 - np.pi)**2)
#     return func_value

# Run PSO
# parameters = {
#     'swarm_size': 250,
#     'min_values': (-5, -5),
#     'max_values': (5, 5),
#     'iterations': 500,
#     'decay': 0,
#     'w': 0.9,
#     'c1': 2,
#     'c2': 2,
#     'verbose': True,
#     'start_init': None,
#     'target_value': None
# }
run=args.run
dim=args.dim
run_all_result=[]
for r in range(run):
    
    parameters = {
        'Cr':0.5,
        'F':0.7,
        'n':10,
        'iterations':dim*10000,
        'evaluations':dim*10000
    }
    # pso = particle_swarm_optimization(target_function = easom, **parameters)
    # pso = particle_swarm_optimization(target_function = test_function.HappyCat, **parameters)
    # pso = algorithm.simulated_annealing(target_function = test_function.HappyCat)

    all_result = [ algorithm.differential_evolution(target_function = test_function.cal_function_objective(i),min_values=[test_function.set_search_range(i)[0]]*dim,max_values=[test_function.set_search_range(i)[1]]*dim,**parameters) for i in range(1,7)]
    run_all_result.append(all_result)


# Print Solution

for i in range(1,7):
    # file=open('result/'+test_function.cal_function_name(i)+'_{}D.txt'.format(dim),'w')
    file=open('result/'+test_function.cal_function_objective(i).__name__+'_{}D.txt'.format(dim),'w')
    for j in range(run):
        variables=run_all_result[j][i-1][:-1]
        minimum=run_all_result[j][i-1][-1]
        file.write('{}\n'.format(minimum))

    variables = all_result[i-1][:-1]
    minimum   = all_result[i-1][ -1]
    print('Variables: ', np.around(variables, 4) , ' Minimum Value Found: ', round(minimum, 4) )

    # Plot Solution
    # from pyMetaheuristic.utils import graphs
    # plot_parameters = {
    #     # 'min_values': (-5, -5),
    #     # 'max_values': (5, 5),
    #     # 'step': (0.1, 0.1),
    #     'solution': [variables],
    #     'proj_view': '3D',
    #     'view': 'browser'
    # }
    # graphs.plot_single_function(target_function = test_function.cal_function_objective(i),min_values=[test_function.set_search_range(i)[0]]*dim,max_values=[test_function.set_search_range(i)[1]]*dim,step=[abs(test_function.set_search_range(i)[0]-test_function.set_search_range(i)[1])/100]*dim, **plot_parameters)
