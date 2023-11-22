import numpy as np
import random
import matplotlib.pyplot as plt

N = 5000
NN = N+0.0

M = 10

x_base = np.array([i / (NN-1.0) for i in range(N)])
for t in [[1.0 for i in range(N)],[1.0 +(i+1.0)/(N+0.0) for i in range(N)]]:
    dist_base = np.array(t)
    mult = np.sum(dist_base) / NN
    dist_base /= mult

    aver = 0.0
    for i in range(N):
        aver += (i/NN+0.5/NN) * dist_base[i]
    aver /= NN
    var = 0.0
    for i in range(N):
        var += (i/NN+0.5/NN-aver)**2 * dist_base[i]
    var /= NN
    print(aver,var) 
    dist_all = []
    dist_all.append(dist_base)

    for i in range(M):
        dist_last = dist_all[-1]
        
        dist_new = np.array([0.0 for i in range(N)])
        for i1 in range(N):
            x1 = i1
            for i2 in range(N):
                x2 = i2
                
                x = int((x1 * (i+1) + x2) / (i+2))
                dist_new[x] += dist_last[i1] * dist_base[i2]
                
        mult = np.sum(dist_new) / NN
        print(i)
        dist_new /= mult
        dist_all.append(dist_new)

    for i in range(len(dist_all)):
        plt.plot(x_base, dist_all[i], label='i={}'.format(i+1))
        th = np.exp(-0.5*(i+1.0)*((x_base-aver)**2)/var) / np.sqrt(2.0*np.pi/(i+1.0)*var)
        plt.plot(x_base, th, ':', label='theory i={}'.format(i+1))
        print(i,np.sum((th-dist_all[i])**2)/NN)

    plt.legend()
    plt.show()

