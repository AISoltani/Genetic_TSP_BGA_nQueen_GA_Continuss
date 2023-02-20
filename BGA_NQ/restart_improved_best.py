import numpy as np
from fitness import fitness

def restart_improved_best(pop, nvar):
    npop = len(pop.pos)
    for i in range(1, npop):
        pop.pos[i] = np.random.permutation(nvar)
        pop.cost[i] = fitness(pop.pos[i], nvar)