import numpy as np
import matplotlib.pyplot as plt

N=100

def factorial(n):
    f=1
    for i in range(1,n):
       f=f*(i+1)
    return f

x = np.linspace(0,2*np.pi,N)
y = np.sinh(x)
   
sums=np.zeros(N)

for i in range(50):
    a=((x)**(2*i+1))/factorial(2*i+1)
    sums=sums+a

z = sums
        
plt.plot(x,y,'b')
plt.plot(x,z,'r--')
plt.grid(True)
plt.show()