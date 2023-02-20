import time
import numpy as np
from fitness import fitness
from population import Pop
from crossover import crossover
from crossover2 import crossover2
from crossovertour import crossovertour
from crossoverunif import crossoverunif
from mutation import mutation
from plotsolution import plotsolution
import matplotlib.pyplot as plt

# parameters setting
nvar = input('Number of Queens = ')  # number of variable
nvar = int(nvar)
npop = 10  # number of population
maxiter = 5000  # max of iteration
pc = 0.7  # percent of cross over
ncross = int(2 * (pc * npop // 2))  # number of cross over
pmut = 0.29  # percent of mutation
nmut = round(pmut * npop)  # number of mutation
nrep = npop - ncross - nmut  # number of repetition

# initialization
start = time.time()
pop = Pop(npop, nvar)
# pos = np.empty(npop, 1)  # position
# cost = np.empty(npop, 1)  # cost
for i in range(npop):
    pop.pos[i] = np.random.permutation(nvar)
    pop.cost[i] = fitness(pop.pos[i], nvar)
ind = np.argsort(pop.cost)
pop.cost = pop.cost[ind]
pop.pos = pop.pos[ind, ...]

#main loop
best = []
avr = []
iter = -1
while pop.cost[0] > 0 and iter < maxiter:
    iter += 1
    #cross
    crosspop = crossover(pop, nvar, ncross)
    #mutation
    mutpop = mutation(pop, nvar, nmut)
    #reproduction
    reppop = Pop(nrep, nvar)
    reppop.pos = pop.pos[:nrep, ...]
    reppop.cost = pop.cost[:nrep, ...]
    #merge

    pop.pos = np.concatenate((reppop.pos, crosspop.pos, mutpop.pos), axis=0)
    pop.cost = np.concatenate((reppop.cost, crosspop.cost, mutpop.cost), axis=0)

    ind = np.argsort(pop.cost)
    pop.cost = pop.cost[ind]
    pop.pos = pop.pos[ind, ...]
    best.append(pop.cost[0])
    avr.append(np.mean(pop.cost))

    print('iter:%d, Best:%d' % (iter, best[iter]))


end = time.time()

plotsolution(pop.pos[0], iter)
print('===================================')
print('Time:%02d:%02d '%(divmod((end - start), 60)))
print('===================================')
print('Best fitness:', pop.cost[0])
print('===================================')
print('Best solution:', pop.pos[0])
plt.plot(range(iter + 1), best, 'g', label='Best')
plt.plot(range(iter + 1), avr, 'b', label='Mean')
plt.legend()
plt.xlabel('Iteration')
plt.ylabel('Fitness')
plt.title('GA for %d_Queens' % (nvar))
plt.show()

