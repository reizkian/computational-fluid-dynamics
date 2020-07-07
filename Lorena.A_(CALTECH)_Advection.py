"""
Author  : Lorena Arba (Caltech)
web     : https://nbviewer.jupyter.org/github/barbagroup/CFDPython/blob/master/lessons/01_Step_1.ipynb
Program : Advection
Created : Thu Apr 25 22:04:20 2019
"""

import numpy
from matplotlib import pyplot
import time , sys

nx = 41
dx = 2 / (nx - 1)
nt = 25
dt = .025
c = 1

u = numpy.ones(nx)
u[10:20] = 2
pyplot.plot(numpy.linspace(0,2,nx) , u)

for n in range(nt):
    un = u.copy()
    for i in range(1,nx):
        u[i] = un[i] - c * dt / dx * (un[i]-un[i-1])

    pyplot.plot(numpy.linspace(0,2,nx) , u)