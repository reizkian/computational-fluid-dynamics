"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: Euler Method_practice
created: 31 Juli 2018
"""

import numpy as np
import matplotlib.pyplot as plt

#VARIABLE DEFINITION
r=1.0
t=np.linspace(0,2,31)

#Coordinate functian
def x(t):
    x=r*np.cos(np.pi*t)
    return x

def y(t):
    y=r*np.sin(np.pi*t)
    return y

plt.title("POLAR COORDINATE")
plt.plot(x(t),y(t),'r-o')
plt.grid(True)

