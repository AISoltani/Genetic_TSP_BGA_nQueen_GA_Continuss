import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
from fitness import fitness
from crossover import crossover
from mutation import mutation
import time

# GA_continuse-Amir Soltani

# Paramters Setting

nvar = 5  # number of variable
npop = 100  # number of population
maxiter = 10000  # max of iteration
pc = 0.1  # percent of crossover
ncross = 2 * round(npop * pc / 2)  # number of cross over offspring
pm = 1 - pc  # percent of mutation
nmut = round(npop * pm)  # number of mutation offsprig
lb = np.ones((1, nvar), dtype='int') * (-10)
ub = np.ones((1, nvar), dtype='int') * 10


# Create Class Empty
class Empty:
    def __init__(self):
        self.par = 0
        self.fit = 0


# Create Population Object

pop = np.array([[Empty() for i in range(npop)] for j in range(npop)], dtype=object)
pop = pop[:, 0:1]
# pop=numpy.matlib.repmat(Empty(),npop,1)

for x in range(npop):
    pop[x][0].par = lb + np.multiply(numpy.matlib.rand(1, nvar),
                                     (ub - lb))  # element wise multiplication like matlab (.*)
    pop[x][0].fit = fitness(pop[x][0].par)

# Main Loop

BEST = numpy.matlib.zeros((maxiter, 1))
MEAN = numpy.matlib.zeros((maxiter, 1))
index = []
MEAN_matrix = []
BEST_matrix = []

# Process Time

tic = time.process_time()

for k in range(maxiter):

    # Crossover Population

    crosspop = np.array([[Empty() for i in range(0, ncross)] for j in range(0, ncross)], dtype=object)
    crosspop = crosspop[:, 0:1]
    crosspop = crossover(crosspop, pop, ncross, npop)

    # Mutation Population

    mutpop = np.array([[Empty() for i in range(0, nmut)] for j in range(0, nmut)], dtype=object)
    mutpop = mutpop[:, 0:1]
    mutpop = mutation(mutpop, pop, nmut, npop, lb, ub, nvar)

    # Merging Pop, Crossover, Mutation

    pop = np.concatenate((pop, crosspop), axis=0)
    pop = np.concatenate((pop, mutpop), axis=0)
    f = np.zeros((npop + ncross + nmut, 1))
    for i in range(0, npop + ncross + nmut):
        f[i][0] = pop[i][0].fit
    # f=np.transpose(f)

    # Sorting Population Based On Fitness

    idx = np.argsort(f, axis=0)
    pop = pop[idx]
    pop = pop.reshape((npop + ncross + nmut, 1))

    # Select The Best 100 First

    pop = pop[0:npop, :]

    gpop = pop[0][0]
    BEST[k][0] = gpop.fit
    MEAN[k][0] = np.mean(f[0:npop, :])
    print('Iter = ', k, ' BEST = ', BEST[k][0])
    index.append(k)
    MEAN_matrix.append(MEAN[k][0])
    BEST_matrix.append((gpop.fit))

    # Stop Condition

    if ((k > 150) and (BEST[k][0] == BEST[k - 150])):
        break

MEAN_matrix = np.asarray(MEAN_matrix)
MEAN_matrix = MEAN_matrix.reshape(k + 1, )
BEST_matrix = np.asarray(BEST_matrix)
BEST_matrix = BEST_matrix.reshape(k + 1, )
toc = time.process_time()
process_times = toc - tic
print("inja ro dashte bash", MEAN_matrix.shape)
print('\nBest par = ', gpop.par)
print('Best fitness = ', gpop.fit)
print('Time = ', process_times)
plt.plot(index, MEAN_matrix, linestyle='-', color='b')
plt.plot(index, BEST_matrix, linestyle='-', color='r')
plt.xlabel('Iteration')
plt.ylabel('Fitness')
plt.title('GA for TSP')
plt.show()

# GA_continuse-Amir Soltani