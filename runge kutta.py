"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: Euler Method_practice
created: 31 Juli 2018
"""

import numpy as np
import matplotlib.pyplot as plt

def differential(x,y):
    dy_dx=2*x
    return dy_dx


"variable definition_constant"
h=0.5     #performance
x_0=-10     #initial value x_0
y_0=100     #initial value y_0
"variable definition_list"
x=[]
y_euler=[]
y_rk=[]
d=[]

while x_0<=10:
    "EULER"
    y_ii=differential(x_0,y_0)*h+y_0
    
    "RUNGE KUTTA"
    k1=differential(x_0,y_0)
    k2=differential((x_0+h)/2,k1/2)
    k3=differential((x_0+h)/2,k2/2)
    k4=differential(x_0+h,k3/2)
    y_rki=y_0+h*(k1+2*k2+2*k3+k4)/6
    
    error=y_ii-y_rki
    
    #print(x_0,"  ",y_ii,"  ",y_rki)
    y_0=y_ii
    x_0=x_0+h
    
    x.append(x_0)
    y_euler.append(y_ii)
    y_rk.append(y_rki)
    d.append(error)
    
plt.title('Euler Method')
plt.grid(True)
plt.plot(x,y_euler,'b--')
plt.plot(x,y_rk,'r--')
#plt.plot(x,d,'g--')
plt.show()
