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

def sin(t):
    a=np.sin(np.pi*t)
    return a
    
"variable definition_constant"
h=0.15     #performance
x_0=0     #initial value x_0
y_01=0
y_02=0     #initial value y_0
"variable definition_list"
t=np.linspace(0,2,101)
x=[]
y=[]
y1=[]
y2=[]
dy_dx=[]

while x_0<=2:
    y_ii1=y_01+differential(x_0,y_01)*h
    y_ii2=y_02+differential(x_0,y_02)*h+(h**2)*orde2(x_0,y_02)/2
    
    
    dy=y_ii1-y_ii2
    print(dy)
    
    y_01=y_ii1
    y_02=y_ii2
    x_0=x_0+h
    
    x.append(x_0)
    y1.append(y_01)
    y2.append(y_02)
    dy_dx.append(dy)
 
    
plt.title('Euler 2nd')
plt.grid(True)
#plt.plot(t,sin(t),'g--')
#plt.plot(x,y1,'r-o')
#plt.plot(x,y2,'b--')
plt.plot(x,dy_dx,'r--')
plt.show()
