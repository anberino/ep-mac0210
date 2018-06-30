from splines import *
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import functools

def test(n):
    #gera o valor certo
    w = np.random.rand(n)
    w-= 0.5 
    s = spline(w)
    t = np.arange(0, 1, 0.001)
    plt.plot(t, s(t))
    plt.show()
    y = s(t)
    
    #gera o valor com ruído
    n = np.random.rand(len(t))
    n-= 0.5
    n*= 100
    ynoise =  y + n
    plt.plot(t, ynoise)
    plt.show()
    

test(10)