import numpy as np
import matplotlib.pyplot as plt

def d2y_dx2(y,x):
    d2y_dx2=-((2*np.pi)**2)*np.cos(2*np.pi*x)
    return d2y_dx2

h=0.001
X=[]
dy_dx=[]
Y=[]

x_0=0
y_0=1
dy_dx_0=0


while x_0<4:
    X.append(x_0)
    Y.append(y_0)
    dy_dx.append(dy_dx_0)
    
    y_n1=y_0+dy_dx_0*h
    y_0=y_n1
    
    dy_dx_n1=dy_dx_0+d2y_dx2(y_0,x_0)*h-dy_dx_0/100
    dy_dx_0=dy_dx_n1
    
    x_0=x_0+h

plt.grid(True)
plt.plot(X,Y,'blue')
plt.plot(X,dy_dx,'orange')
plt.show()
    
                  