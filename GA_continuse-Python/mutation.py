import numpy as np
import random
import numpy.matlib
from fitness import fitness


# Mutation Function

def mutation(mutpop, pop, nmut, npop, lb, ub, nvar):
    for n in range(0, nmut):
        i = np.random.randint(0, npop - 1)
        sol = pop[i][0].par
        j = np.random.randint(0, nvar - 1)
        d = 0.1 * np.random.uniform(-1, 1) * (ub[0][j] - lb[0][j])

        sol = np.array(sol).tolist()
        sol[0][j] = (sol[0][j]) + d
        sol = np.minimum(sol, ub)
        sol = np.maximum(sol, lb)

        mutpop[n][0].par = sol
        mutpop[n][0].fit = fitness(sol)

    return mutpop
