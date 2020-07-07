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

def integral_f(x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    c=y1-(m*x1)
    F=(m*(x2**2-x1**2)/2)+c*(x2-x1)
    return F
    
"variable definition_constant"
h=0.05     #performance
x1=-10     #initial value x_0
y1=100     #initial value y_0
"variable definition_list"
x=[]
y=[]
yMS=[]
d=[]

while x1<=10:
    "Euler Method"
    y_ii=differential(x1,y1)*h+y1
    y1=y_ii
    x1=x1+h
    x.append(x1)
    y.append(y1)
    
    "Multiple Step"
    y2=y_ii
    x2=x1+h
    y_ms=y1+integral_f(x1,x2,y1,y2)
    yMS.append(y_ms)
    
    #print(x1," ",y_ms,"  ",y_ii)
    error=y_ms-y_ii
    d.append(error)
    
plt.title('Euler Method')
plt.grid(True)
#plt.plot(x,y,'b--')
#plt.plot(x,yMS,'g--')
plt.plot(x,d,'r--')
plt.show()