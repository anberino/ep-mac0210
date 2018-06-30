# Gabriel Sarti Massukado - NUSP 10284177
# Henrique Cerquinho - NUSP 9793700

from splines import *
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import functools

def test(n, min, max):
    #gera o valor certo
<<<<<<< HEAD
    ws = np.random.rand(n)
    ws-= 0.5 
    s = spline(ws, min, max)
=======
    w = np.random.rand(n)
    w-= 0.5
    s = spline(w, min, max)
>>>>>>> 6872466a6549e5fd799a2dd79935faf0db47df33
    t = np.arange(min, max, 0.001)
    m = len(t)
    plt.plot(t, s(t), 'r')
    y = s(t) #esse é o spline de vdd, eu acho

    #gera o valor com ruído baseado em s
    noise = np.random.rand(m)
    noise-= 0.5
    noise*= 100
    ynoise =  y + noise
    plt.plot(t, ynoise, 'b', alpha=0.4)
    plt.show()

    #cria uma spline temporária pra pegar os betajs
    arraytemp = np.full(len(t), 1)
    #print(arraytemp) #test print
    temp = spline(arraytemp, min, max)
    Bt = np.zeros([n, m]) #deve ter um jeito melhor de fazer isso
    for i in range(n):
        for j in range(m):
            Bt[i][j] = temp.beta_j(i, t[j])
    #print(B) #test print

    #calcula a matrix M1, a M2 e a b ((M1+lM2)w = b) para acharmos w
    B = np.matrix.transpose(Bt)
    M1 = np.matmul(Bt, B)
    M2 = matrix_m2(n)
<<<<<<< HEAD
    b = np.matmul(Bt, ynoise)
    l = 1 #completamente arbitrário, segundo Mascarenhas
    M = M1 + l*M2
    
    #resolve o sistema 
    w = np.linalg.solve(M, b)
    
    #plota a nova spline
    aprox = spline(w)
    plt.plot(t, aprox(t))
    plt.show()
    
=======

    #b = np.matmul(Bt, ynoise) #falando que não bate os números, tem algo errado ali em cima

>>>>>>> 6872466a6549e5fd799a2dd79935faf0db47df33

test(10, 0, 1)