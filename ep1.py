# Gabriel Sarti Massukado - NUSP 10284177
# Henrique Cerquinho      - NUSP 9793700

from splines import *
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import functools

"""
Nesse EP será gerada uma spline exata (sem ruído) aleatória e então será
adicionado ruido aos seus valores, para assim recuperarmos eles novamente
utilizando os métodos vistos em aula. Para rodar o EP bastar rodar o comando
    'python ep1.py'
e ter na pasta o módulo splines.py.
Serão plotados, em um gráfico, uma spline original aleatória (com n = 10) junto
com os valores com ruído, e, em outro gráfico, a spline recuperada usando
as fórmulas.
"""

def ep1(n, min, max):
    # Gera uma spline exata
    ws = np.random.rand(n)
    ws-= 0.5
    s = spline(ws, min, max)
    t = np.arange(min, max, 0.001)
    m = len(t)
    plt.subplot(211)
    plt.plot(t, s(t), 'r')
    y = s(t) # Essa é a spline original

    # Gera os valores com ruído baseado em s
    noise = np.random.rand(m)
    noise-= 0.5
    noise*= 100
    ynoise =  y + noise
    plt.title("Spline original e valores com ruído")
    plt.grid(True)
    plt.plot(t, ynoise, 'b', alpha=0.4)

    # Cria uma spline temporária pra achar os beta_j's
    seed = [1]*n
    arraytemp = np.array(seed)
    temp = spline(arraytemp, min, max)
    B = np.zeros([m, n])
    for i in range(m):
        for j in range(n):
            B[i][j] = temp.beta_j(j, t[i])

    # Calcula a matriz M1, a M2 e a b ((M1+lM2)w = b) para acharmos w
    Bt = np.matrix.transpose(B)
    M1 = np.dot(Bt, B)
    M2 = matrix_m2(n)
    b = np.dot(Bt, ynoise)
    l = 6 # Completamente arbitrário
    M = M1 + (l*M2)

    # Resolve o sistema
    w = np.linalg.solve(M, b)

    # Plota a nova spline
    aprox = spline(w)
    plt.subplot(212)
    plt.title("Spline recuperada")
    plt.grid(True)
    plt.plot(t, aprox(t))
    plt.show()

# Roda a função com n = 10
ep1(10, 0, 1)