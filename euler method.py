"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: Euler Method_practice
created: 31 Juli 2018
"""

import numpy as np
import matplotlib.pyplot as plt

def differential(x,y):
    dy_dx=-15*y
    return dy_dx

"variable definition_constant"
h=1/8     #performance
x_0=0     #initial value x_0
y_0=1     #initial value y_0
"variable definition_list"
x=[]
y=[]
dy_dx=[]

while x_0<=20:
    print(x_0,"     ",y_0)
    y_ii=differential(x_0,y_0)*h + y_0
    y_0=y_ii
    x_0=x_0+h
    
    x.append(x_0)
    y.append(y_0)
    dy_dx.append(differential(x_0,y_0))
 
    
plt.title('Euler Method')
plt.grid(True)
plt.plot(x,y,'b-o')
#plt.plot(x,dy_dx,'g--')
plt.show()
