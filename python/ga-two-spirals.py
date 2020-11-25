from modgeneticalgorithm import geneticalgorithm as ga
from fitness import get_fitness
import numpy as np


def fitness_for_test(X):
    targ = 8880141
    return np.sqrt((targ - sum(X)) ** 2) / targ


algorithm_param = {'max_num_iteration': 4000,
                   'population_size':20,
                   'mutation_probability':0.1,
                   'elit_ratio': 0.01,
                   'crossover_probability': 0.5,
                   'parents_portion': 0.3,
                   'crossover_type':'uniform',
                   'max_iteration_without_improv': 20}






"""
Activations: (each corresponds to an element of the list, in order)
    - First 6 are hidden layers with the range of hidden units
    - Algorithm: [0, 1] (range 0 to 1; 0 for PSO, 1 for SGD)
    - Activation: [0, 4] (0: ReLU, 1: TanH, 2: Sigmoid, 3: Sin, 4: RBF)
    - Inputs: [0, 1] (whether we leave x**2 or not)
"""

varbound_ga = np.array([
    [0, 8],  # HL 1
    [0, 8],  # HL 2
    [0, 8],  # HL 3
    [0, 0],  # TODO Not HL4
    [0, 0],  # TODO Not HL4
    [0, 0],  # TODO Not HL4
    [1, 1],  # PSO
    [1, 1],  # TanH
    [0, 0],  # No x**2
])

varbound_gp = np.array([
    [6, 6],  # HL 1
    [0, 0],  # HL 2
    [0, 0],  # HL 3
    [0, 0],  # TODO Not HL4
    [0, 0],
    [0, 0],
    [0, 1],  # PSO
    [0, 4],  # TanH
    [0, 1],  # No x**2
])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t', type=str, default='ga',
                        help='ga or gp')
    parser.add_argument('--file', '-f', type=str, default='temp',
                        help="filename to save results")
    args = parser.parse_args()

    if args.type == 'ga':
        varbound = varbound_ga
    elif args.type == 'gp':
        varbound = varbound_gp

    model=ga(function=get_fitness, dimension=9, variable_type='int',variable_boundaries=varbound, algorithm_parameters=algorithm_param, function_timeout=4000, filename=args.file)
    model.run()