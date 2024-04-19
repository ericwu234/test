
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

run=args.run
dim=args.dim
run_all_result=[]
all_list_evalua_min=[]
run_list_evalua_min=[]
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
    all_list_evalua_min=[]
    all_result = [ algorithm.differential_evolution(target_function = test_function.cal_function_objective(i),min_values=[test_function.set_search_range(i)[0]]*dim,max_values=[test_function.set_search_range(i)[1]]*dim,all_list_evalua_min=all_list_evalua_min,**parameters) for i in range(1,7)]
    run_all_result.append(all_result)
    run_list_evalua_min.append(all_list_evalua_min)
run_list_evalua_min=np.mean(np.array(run_list_evalua_min),axis=0)


import matplotlib.pyplot as plt

# Print Solution

for i in range(1,7):
    plt.figure()
    plt.plot(range(1,len(run_list_evalua_min[i-1])+1), run_list_evalua_min[i-1])
    plt.title('{}'.format(test_function.cal_function_objective(i).__name__))
    plt.xlabel('iterations')
    plt.ylabel('objective value')
    plt.savefig('result2/{}_{}D_{}run_plot.png'.format(test_function.cal_function_objective(i).__name__,dim,run))
    # file=open('result/'+test_function.cal_function_name(i)+'_{}D.txt'.format(dim),'w')
    file=open('result/'+test_function.cal_function_objective(i).__name__+'_{}D.txt'.format(dim),'w')
    file2=open('result2/'+test_function.cal_function_objective(i).__name__+'_{}D.txt'.format(dim),'w')
    best=np.inf
    sum=0
    for j in range(run):
        variables=run_all_result[j][i-1][:-1]
        minimum=run_all_result[j][i-1][-1]
        file.write('{}\n'.format(minimum))
        best=min(minimum,best)
        sum+=minimum

    file2.write('Best: {}\n'.format(best))
    file2.write('Average: {}\n'.format(sum/run))
    file2.write('iter_mean: '+np.array2string(run_list_evalua_min[i-1]))


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

#hpo
# def obj(x):
#     run=30
#     sum=0
#     for r in range(run):
#         parameters = {
#             'Cr':x[0],
#             'F':x[1],
#             'n':x[2]*100,
#             'iterations':dim*10000
#             }
#         all_result = [ algorithm.differential_evolution(target_function = test_function.cal_function_objective(i),min_values=[test_function.set_search_range(i)[0]]*dim,max_values=[test_function.set_search_range(i)[1]]*dim,**parameters) for i in range(1,2)]
        
#         sum+=all_result[0]
#     return sum/run
# dim=3
# result=algorithm.differential_evolution(target_function = obj,min_values=[0,0,0],max_values=[1,1,1],iterations=1000,evaluations=1000,Cr=0.5,F=0.7,n=10)
# variables = result[:-1]
# minimum   = result[ -1]
# print('Variables: ', np.around(variables, 4) , ' Minimum Value Found: ', round(minimum, 4) )