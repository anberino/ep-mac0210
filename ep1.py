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
    ws = np.random.rand(n)
    ws-= 0.5
    s = spline(ws, min, max)
    t = np.arange(min, max, 0.001)
    m = len(t)
    plt.subplot(211)
    plt.plot(t, s(t), 'r')
    y = s(t) #esse é o spline de vdd, eu acho

    #gera o valor com ruído baseado em s
    noise = np.random.rand(m)
    noise-= 0.5
    noise*= 100
    ynoise =  y + noise
    plt.plot(t, ynoise, 'b', alpha=0.4)

    #cria uma spline temporária pra pegar os betajs
    arraytemp = np.full(len(t), 1)
    #print(arraytemp) #test print
    temp = spline(arraytemp, min, max)
    B = np.zeros([m, n]) #deve ter um jeito melhor de fazer isso
    for i in range(m):
        for j in range(n):
            B[i][j] = temp.beta_j(j, t[i])
    # Bt = np.matrix.transpose(Bt)
    # print(len(t), n) #test print

    #calcula a matrix M1, a M2 e a b ((M1+lM2)w = b) para acharmos w
    Bt = np.matrix.transpose(B)
    M1 = np.dot(Bt, B)
    M2 = matrix_m2(n)
    b = np.dot(Bt, ynoise)
    l = 5 #completamente arbitrário, segundo The Mask
    M = M1 + (l*M2)

    # resolve o sistema
    w = np.linalg.solve(M, b)

    #plota a nova spline
    aprox = spline(w)
    plt.subplot(212)
    plt.plot(t, aprox(t))
    plt.show()

test(10, 0, 1)