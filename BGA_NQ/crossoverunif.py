import random
import numpy as np
from population import Pop
from fitness import fitness


def crossoverunif(pop, nvar, ncross):
    crosspop = Pop(ncross, nvar)
    f = np.copy(pop.cost)
    f = 1 / f
    f = f / np.sum(f)
    f = np.cumsum(f)
    for n in range(0, ncross, 2):
        rnd = random.random()
        i1 = np.min(np.where(rnd <= f))
        rnd = random.random()
        i2 = np.min(np.where(rnd <= f))
        p1 = pop.pos[i1]
        p2 = pop.pos[i2]

        mask = random.choices([0,1], k=nvar)
        o1 = np.zeros(nvar, dtype=int)
        o2 = np.zeros(nvar, dtype=int)
        for i,j in enumerate(mask):
            if j ==1:
                o1[i] = p1[i]
                o2[i]=p2[i]
            else:
                o1[i] = p2[i]
                o2[i] = p1[i]
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
    npop = 4
    ncross = 2
    pop = Pop(npop, nvar)
    for i in range(npop):
        pop.pos[i] = np.random.permutation(nvar)
        pop.cost[i] = fitness(pop.pos[i], nvar)
    ind = np.argsort(pop.cost)
    pop.cost = pop.cost[ind]
    pop.pos = pop.pos[ind, ...]

    print(pop.pos)
    print(crossoverunif(pop, nvar, ncross).pos)
