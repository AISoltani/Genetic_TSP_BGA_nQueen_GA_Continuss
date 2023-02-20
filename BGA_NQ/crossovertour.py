import random
import numpy as np
from population import Pop
from fitness import fitness


def crossovertour(pop, nvar, ncross):
    crosspop = Pop(ncross, nvar)
    npop = len(pop.pos)
    ntour = 10
    for n in range(0, ncross, 2):
        g = np.random.permutation(npop)
        g = g[:ntour]
        tourpop = Pop(ntour, nvar)
        tourpop.pos = np.copy(pop.pos[g])
        tourpop.cost = np.copy(pop.cost[g])
        ind = np.argsort(tourpop.cost)
        tourpop.cost = tourpop.cost[ind]
        tourpop.pos = tourpop.pos[ind, ...]

        p1 = tourpop.pos[0]
        p2 = tourpop.pos[1]

        j = random.randrange(nvar - 1)
        o1 = np.concatenate((p1[:j+1], p2[j+1:]))
        o2 = np.concatenate((p2[:j+1], p1[j+1:]))
        o1 = np.concatenate((o1, np.random.permutation(nvar)))
        o2 = np.concatenate((o2, np.random.permutation(nvar)))

        ind = np.unique(o1, return_index=True)[1]
        ind = np.sort(ind)
        o1 = o1[ind]
        ind = np.unique(o2, return_index=True)[1]
        ind = np.sort(ind)
        o2 = o2[ind]

        crosspop.pos[n] = o1
        crosspop.cost[n] = fitness(o1, nvar)
        crosspop.pos[n + 1] = o2
        crosspop.cost[n + 1] = fitness(o2, nvar)

    return crosspop

if __name__ == '__main__':

    nvar = 8
    npop = 10
    ncross = 2
    pop = Pop(npop, nvar)
    for i in range(npop):
        pop.pos[i] = np.random.permutation(nvar)
        pop.cost[i] = fitness(pop.pos[i], nvar)
    ind = np.argsort(pop.cost)
    pop.cost = pop.cost[ind]
    pop.pos = pop.pos[ind, ...]

    print(pop.pos)
    print(crossovertour(pop, nvar, ncross).pos)
