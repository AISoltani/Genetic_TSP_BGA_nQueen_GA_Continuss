import numpy as np
import numpy.matlib


# Fitness Function

def fitness(a):
    myfit = numpy.matlib.sum(np.power(a, 2))
    # myfit = np.sum(np.power(a, 2))
    return myfit
