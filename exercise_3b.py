import numpy as np
import matplotlib.pyplot as plt

def temp():
    C = 900
    k = 237
    rho = 2700
    dt = 1

    # Old temperature vector
    T_0 = np.zeros((100), float)
    
    # New temperature vector
    T_1 = np.zeros((100), float)
    T_1[1:-1] = 100

    temp_list = []

    eta = (k * dt) / (C * rho * 0.0005)
    
    if eta<0.5:
        for time in np.arange(0, 200, dt):
            T_0 = np.copy(T_1)
            for i in np.arange(1, 99):
                T_1[i] = T_0[i] + eta * (T_0[i+1] + T_0[i-1] - 2* T_0[i])
            temp_list.append(T_0)
            
    plt.imshow(temp_list)
    plt.colorbar()
    plt.show()
    return
temp()