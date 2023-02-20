import numpy as np

def fitness(sol, nvar):
    k = 0
    for i in range(nvar):
        for j in range(i + 1, nvar):
            if abs(i - j)==abs(sol[i]-sol[j]):
                k += 1

    return k

if __name__ == '__main__':
    nvar = 8
    print(fitness(np.array([4, 5, 6, 7, 8, 1, 2, 3]),nvar))
    print(fitness(np.array([1, 8, 2, 7, 3, 6, 4, 5]),nvar))
    print(fitness(np.array([1, 3, 5, 7, 8, 6, 4, 2]),nvar))
    print(fitness(np.array([5, 1, 8, 4, 2, 7, 3, 6]),nvar))
    print(fitness(np.array([5, 3, 4, 2, 0, 6, 7, 1]),nvar))
    print(fitness(np.array([0, 7, 1, 6, 2, 5, 3, 4]), nvar))

    print(fitness(np.array([1, 3, 12, 10, 7, 14, 6, 2, 0, 13, 15, 5, 9, 11, 4, 8]),16))
    print(fitness(np.array([ 5, 10,  8,  1,  3, 12,  6,  9,  0, 11, 15, 14,  2, 13,  7,  4]),16))
    print(fitness(np.array([ 4,  8,  7,  0, 15, 12,  5,  2, 13,  9,  3, 11, 14,  1, 10,  6]),16))
    print(fitness(np.array([4,7,13,6,9,3,14,0,5,10,15,12,11,1,8,2]),16))
    print(fitness(np.array([6,0,8,15,13,4,3,14,11,10,12,5,1,7,9,2]),16))
    print(fitness(np.array([4,8,7,0,15,12,5,9,11,10,14,2,1,13,6,3]),16))
    print(fitness(np.array([4,  7,  8, 10,  1, 15,  9,  0,  6, 14, 12,  5,  2, 13, 11,  3]),16))
    print(fitness(np.array([4, 14,  8, 10,  1, 15, 11,  0,  6, 12,  2,  7, 13,  3,  5,  9]),16))
    print(fitness(np.array([19, 12,  4, 26,  7, 11, 27, 25, 15,  5, 30, 24, 16, 21, 31, 10,  6, 29, 23,  8,  1,  9, 20,  3,  0,
 18, 13, 28, 22,  2, 14, 17]),32))
    print(fitness(np.array([47, 31, 46, 26, 54,  3, 22, 62, 17,  6, 51, 44,  4,  8, 10, 21, 15, 57, 28, 61, 37, 24, 11,  0, 59,
 52, 39,  7, 32, 49, 56, 60, 18, 48, 36, 16, 27,  2, 38, 40, 12, 53, 63,  1, 58, 30, 13,  9, 55, 19,
 23, 41, 20, 14, 33, 43, 34,  5, 42, 25, 29, 35, 45, 50]),64))
