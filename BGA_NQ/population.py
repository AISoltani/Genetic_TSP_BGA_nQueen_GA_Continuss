import numpy as np
from fitness import fitness


class Pop:
    def __init__(self, npop, nvar):
        self.pos = np.empty((npop, nvar), dtype=int)
        self.cost = np.empty(npop, dtype=int)

