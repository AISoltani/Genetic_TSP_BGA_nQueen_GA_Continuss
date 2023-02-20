import numpy as np
import random
import numpy.matlib
from fitness import fitness

# Crossover Function

def crossover(crosspop, pop, ncross, npop):
    pop_fit = np.zeros((npop, 1))
    for i in range(0, npop):
        pop_fit[i][0] = pop[i][0].fit
    pop_fit = np.divide(pop_fit, numpy.matlib.sum(pop_fit))
    pop_fit = numpy.matlib.cumsum(pop_fit)
    # pop_fit = np.cumsum(f1)
    idx = np.argsort(pop_fit, axis=0)
    pop = pop[idx]
    pop = pop.reshape((npop, 1))

    for j in range(0, ncross, 2):
        # i1 = np.where(np.random.rand() < f)
        # i2 = np.where(np.random.rand() < f)[0][9]

        i1 = np.random.randint(0, npop - 1)
        i2 = np.random.randint(0, npop - 1)
        p1 = pop[i1][0].par
        p2 = pop[i2][0].par


        # p1 = pop[0][0].par
        # p2 = pop[1][0].par

        R = numpy.matlib.rand(numpy.matlib.size(p1))

        o1 = (np.multiply(p1, R)) + (np.multiply(p2, 1 - R))
        o2 = (np.multiply(p2, R)) + (np.multiply(p1, 1 - R))

        crosspop[j][0].par = o1
        crosspop[j][0].fit = fitness(o1)

        crosspop[j + 1][0].par = o2
        crosspop[j + 1][0].fit = fitness(o2)

    return crosspop
