import random
import numpy as np
from population import Pop
from fitness import fitness

def mutation(pop, nvar, nmut):
    npop = len(pop.pos)
    mutpop = Pop(nmut, nvar)
    for n in range(nmut):
        i = random.randrange(npop)
        p = np.copy(pop.pos[i])
        j1 = random.randrange(nvar - 1)
        j2 = random.randrange(j1+1,nvar)
        nj1 = p[j1]
        nj2 = p[j2]
        p[j1] = nj2
        p[j2] = nj1
        mutpop.pos[n] = p
        mutpop.cost[n] = fitness(p, nvar)

    return mutpop


if __name__ == '__main__':

    pop = Pop(2,8)
    pop.pos = np.concatenate((np.random.permutation(8),np.random.permutation(8))).reshape(2,8)
    print(pop.pos)
    nvar = 8
    nmut = 1
    print(mutation(pop, nvar, nmut).pos)