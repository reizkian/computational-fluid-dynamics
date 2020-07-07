"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: Euler Method_practice
created: 31 Juli 2018
"""

import numpy as np
import matplotlib.pyplot as plt

def differential(x,y):
    dy_dx=np.cos(np.pi*x)*np.pi
    return dy_dx

def orde2(x,y):
    d2y_dx2=-np.sin(np.pi*x)/(np.pi**2)
    return d2y_dx2
    
"variable definition_constant"
h=0.01     #performance
x_0=0     #initial value x_0
y_0=0     #initial value y_0
"variable definition_list"
x=[]
y=[]
dy_dx=[]

while x_0<=2:
    print(x_0,"*pi","     ",y_0)
    y_ii=y_0+differential(x_0,y_0)*h+(h**2)*orde2(x_0,y_0)/2
    y_0=y_ii
    x_0=x_0+h
    
    x.append(x_0)
    y.append(y_0)
    dy_dx.append(differential(x_0,y_0))
 
    
plt.title('Euler 2nd')
plt.grid(True)
plt.plot(x,y,'b--')
#plt.plot(x,dy_dx,'r--')
plt.show()
