import numpy as np
import matplotlib.pyplot as plt

def plotsolution(sol, iter):
    nvar = len(sol)
    x, y = np.meshgrid(range(nvar), range(nvar))
    plt.plot(x, y, 'ks')
    plt.plot(sol, range(nvar), 'rs')
    k = 0
    for i in range(nvar):
        for j in range(i + 1, nvar):
            if abs(i - j)==abs(sol[i]-sol[j]):
                plt.plot([sol[i], sol[j]],[i, j], 'r--')
                k += 1
    plt.title('nvar:%d, iter:%d, k:%d' %(nvar, iter, k))
    plt.show()

if __name__ == '__main__':
    plotsolution(np.array([5, 3, 6, 0, 2, 4, 1, 7]))
    plotsolution(np.array([1, 3, 12, 10, 7, 14, 6, 2, 0, 13, 15, 5, 9, 11, 4, 8]))
    plotsolution(np.array([0, 7, 1, 6, 2, 5, 3, 4]))