############################################################################

# Created by: Prof. Valdecy Pereira, D.Sc.
# UFF - Universidade Federal Fluminense (Brazil)
# email:  valdecy.pereira@gmail.com 
# Metaheuristic: Differential Evolution

# PEREIRA, V. (2022). GitHub repository: https://github.com/Valdecy/pyMetaheuristic

############################################################################

# Required Libraries
import numpy  as np

############################################################################

# Function
def target_function():
    return

############################################################################

# Function: Initialize Variables
def initial_variables(size, min_values, max_values, target_function, start_init = None):
    dim = len(min_values)
    if (start_init is not None):
        start_init = np.atleast_2d(start_init)

        n_rows     = size - start_init.shape[0]
        if (n_rows > 0):
            rows       = np.random.uniform(min_values, max_values, (n_rows, dim))
            start_init = np.vstack((start_init[:, :dim], rows))
        else:
            start_init = start_init[:size, :dim]
        fitness_values = target_function(start_init) if hasattr(target_function, 'vectorized') else np.apply_along_axis(target_function, 1, start_init)
        population     = np.hstack((start_init, fitness_values[:, np.newaxis] if not hasattr(target_function, 'vectorized') else fitness_values))
    else:
        population     = np.random.uniform(min_values, max_values, (size, dim))
        fitness_values = target_function(population) if hasattr(target_function, 'vectorized') else np.apply_along_axis(target_function, 1, population)
        # print('fitness_values:',fitness_values)
        population     = np.hstack((population, fitness_values[:, np.newaxis] if not hasattr(target_function, 'vectorized') else fitness_values))
    return population

############################################################################

# Function: Velocity
def velocity(position, best_global, k0, k1, k2, F, min_values, max_values, Cr, target_function, evalua_count):
    v = np.copy(best_global)
    # print( 'len(best_global):',len(best_global))
    for i in range(0, len(best_global)):
        ri = np.random.rand()
        if (ri <= Cr):
            v[i] = best_global[i] + F*(position[k1, i] - position[k2, i])
        else:
            v[i] = position[k0, i]
        if (i < len(min_values) and v[i] > max_values[i]):
            v[i] = max_values[i]
        elif(i < len(min_values) and v[i] < min_values[i]):
            v[i] = min_values[i]
    v[-1] = target_function(v[0:len(min_values)])
    # print('v:',v)
    return v

############################################################################

# Function: DE/Best/1/Bin Scheme
def differential_evolution(n = 3, min_values = [-5,-5], max_values = [5,5], iterations = 50, F = 0.9, Cr = 0.2, target_function = target_function, verbose = True, start_init = None, target_value = None, evaluations = None,all_list_evalua_min=[]):    
    evalua_count= 0
    position    = initial_variables(n, min_values, max_values, target_function, start_init)
    
    evalua_count+= n
    best_global = np.copy(position [position [:,-1].argsort()][0,:])
    count       = 0
    list_iter_min=[]
    while (count <= iterations and evalua_count<=evaluations):
        if (verbose == True):
            print('Iteration = ', count, ' f(x) ', best_global[-1])
        for i in range(0, position.shape[0]):
            k1 = int(np.random.randint(position.shape[0], size = 1))
            k2 = int(np.random.randint(position.shape[0], size = 1))
            while k1 == k2:
                k1 = int(np.random.randint(position.shape[0], size = 1))
            vi = velocity(position, best_global, i, k1, k2, F, min_values, max_values, Cr, target_function, evalua_count)        
            evalua_count+=1
            
            if (vi[-1] <= position[i,-1]):
                for j in range(0, position.shape[1]):
                    position[i,j] = vi[j]
            
            if (best_global[-1] > position [position [:,-1].argsort()][0,:][-1]):
                best_global = np.copy(position [position [:,-1].argsort()][0,:])  
            # list_iter_min.append(best_global[-1])
            if evalua_count>=evaluations:
                break
        if (target_value is not None):
            if (best_global[-1] <= target_value):
                count = 2* iterations
            else:
                count = count + 1
        else:
            count = count + 1
        list_iter_min.append(best_global[-1])
        # print('evaluation:',evalua_count)  
    all_list_evalua_min.append(list_iter_min)  
    return best_global

############################################################################