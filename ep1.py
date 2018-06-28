from splines import *
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import functools

def test():
    x = np.random.rand(10)
    print("oi")
    s = spline(x)
    t = np.arange(0, 1, 0.001)
    plt.plot(t, s(t))

test()