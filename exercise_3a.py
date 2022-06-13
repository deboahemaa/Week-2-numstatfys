import matplotlib.pyplot as plt
import numpy as np

def laplace(N, M, V0, iteration):
    h = 1
    V = np.zeros((N,M), float)
    iteration_list = []
    con_mon_list = []
    V[:,:1] = V0
    E = 0

    for m in np.arange(1, iteration):
        for i in np.arange(N-h):
            for j in np.arange(h, M-h):
                V[i, j] = 0.25*(V[i+h, j] + V[i-h, j] + V[i, j+h] + V[i, j-h])
         
        for j in range(h, M-h):
            for i in range(h, N-h):
                E += (V[i,j] - V[i-1, j])**2 + (V[i,j] - V[i, j-1])**2
        
        con_mon_list.append(E)   
        iteration_list.append(m)
    plt.imshow(V)
    plt.colorbar()
    plt.show()
    return V

laplace(100, 100, 1, 50)