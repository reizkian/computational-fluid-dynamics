import numpy as np
import matplotlib.pyplot as plt

"Function Declaration"
def d2y_dx2(x):
    d2y_dx2=-(np.pi**2)*np.sin(np.pi*x)
    return d2y_dx2

def dy_dx(x,y_d01,y_d2):
    dy_dx=y_d01+h*y_d2
    return dy_dx

"Initial Condition"
X0=0
Y0=0
Y_d1_X0=np.pi

"Arrays and Variable cotainer" 
X=[]
Y=[]
h=0.001 #Performance

"Main Program Loop"
while X0<=2:
    y_i1=Y0+h*Y_d1_X0
    Y.append(y_i1)
    
    Y0=y_i1
    y_d01=Y_d1_X0
    y_d2=d2y_dx2(X0)
    y_d1=dy_dx(X0,y_d01,y_d2)
    Y_d1_X0=y_d1
    
    X0=X0+h
    X.append(X0)
    
"PLOTING GRAPH"
plt.title("2nd ORDER EULER")
plt.plot(X,Y,'r')
plt.grid(True)
plt.show    
    